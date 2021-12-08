# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run
Created on Thu Aug 06 2020
@author: Harika Kuppa

P9 partially functional
"""


# standard Python/SciPy libraries
import getpass, sys, os, clr,re
import subprocess as sp
import pandas as pd
from datetime import datetime
from time import sleep
from os.path import dirname, join
import csv
#from pandas.io.common import EmptyDataError
from shutil import copyfile

# .NET related imports
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System.IO import SearchOption

server =   input('Server:          ')
port =     input('Port (def:8888): ')
try:
    port = int(port)
except:
    port = 8888
username = input('Username:        ')
password = getpass.getpass('Password:        ')

# connect to the PLEXOS Connect server
cxn = PLEXOSConnect()
cxn.DisplayAlerts = False
cxn.Connection('Data Source={}:{};User Id={};Password={}'.format(server,port,username,password))

folder = input('Folder:   ')
local = input('Local Folder: ')
dataset = input('Dataset:  ')

if len(dataset) == 0:
    dataset = 'testdb'
    

# verify that the dataset exists
if not cxn.CheckDatasetExists(folder,dataset):
    print('Dataset', dataset, 'does not exist in folder', folder)
    
    
else:
    '''
    String GetDatasetLatestVersion(
    	String strFolderPath,
    	String strDatasetName
    	)
    '''
    ver = cxn.GetDatasetLatestVersion(folder,dataset)

    if not os.path.exists(local):
        os.mkdir(local)

    dest = os.path.join(local,dataset)
    if not os.path.exists(dest):
        os.mkdir(dest)

    '''
    Boolean DownloadDatasetVersion(
    	String strDestination,
    	String strFolderPath,
    	String strDatasetName,
    	String strVersion
    	)
    '''
    cxn.DownloadDatasetVersion(dest, folder, dataset, ver)
    
    #Edit the dataset
    #Direct to the directory
    for i, f in enumerate(os.listdir(dest)):
        if '.xml' in f:
            print('{}. {}'.format(i+1, f))
    
    f_i = input('Which file number?')
    xml_file = os.listdir(dest)[f_i - 1]

    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection(xml_file)
    
    # Add a category
    '''
    Int32 AddCategory(
        ClassEnum nClassId,
        String strCategory
        )
    '''
    db.AddCategory(ClassEnum.Generator, 'API')
    
    # Add an object (and the System Membership)
    '''
    Int32 AddObject(
        String strName,
        ClassEnum nClassId,
        Boolean bAddSystemMembership,
        String strCategory[ = None],
        String strDescription[ = None]
        )
    '''
    db.AddObject('ApiGen', ClassEnum.Generator, True, 'API', 'Testing the API')
    
    # Add memberships
    '''
    Int32 AddMembership(
        CollectionEnum nCollectionId,
        String strParent,
        String strChild
        )
    '''
    db.AddMembership(CollectionEnum.GeneratorNodes, 'ApiGen', 'A')    

    # Get the System.Generators membership ID for this new generator
    '''
    Int32 GetMembershipID(
        CollectionEnum nCollectionId,
        String strParent,
        String strChild
        )    
    '''
    mem_id = db.GetMembershipID(CollectionEnum.SystemGenerators, \
                                'System', 'ApiGen')
                                
    # Add properties
    '''
    Int32 AddProperty(
        Int32 MembershipId,
        Int32 EnumId,
        Int32 BandId,
        Double Value,
        Object DateFrom,
        Object DateTo,
        Object Variable,
        Object DataFile,
        Object Pattern,
        Object Scenario,
        Object Action,
        PeriodEnum PeriodTypeId
        )
    
    Because of the number of parameters, we need
            a. An alias for AddProperty
            b. A tuple of parameter values
            c. A call to the alias
        
    Also we need to obtain the EnumId for each property
        that we intend to add
    '''
    # b. A tuple of parameter values
    db.AddProperty(mem_id, int(SystemGeneratorsEnum.Units), \
            1, 1.0, None, None, None, None, None, None, \
            0, PeriodEnum.Interval)

    db.AddProperty(mem_id, int(SystemGeneratorsEnum.MaxCapacity), \
            1, 250, None, None, None, None, None, None, \
            0, PeriodEnum.Interval)

    db.AddProperty(mem_id, int(SystemGeneratorsEnum.FuelPrice), \
            1, 2.50, None, None, None, None, None, None, \
            0, PeriodEnum.Interval)

    db.AddProperty(mem_id, int(SystemGeneratorsEnum.HeatRate), \
            1, 9000, None, None, None, None, None, None, \
            0, PeriodEnum.Interval)   


    # save the data set
    db.Close()

    print("Downloaded and modified the input database")

    '''
    String GetDatasetLatestVersion(
        String strFolderPath,
        String strDatasetName
        )
    '''
    ver = cxn.GetDatasetLatestVersion(folder,dataset)
    
    # compute the new version number by adding one to the
    #  last element of the current version number
    sub_ver = [int(s) for s in ver.split('.')]
    sub_ver[-1] += 1
    new_version = '.'.join([str(v) for v in sub_ver])
    print(new_version)

    '''    
    Void UploadDataSet(
        String strSourcePath,
        String strFolderPath,
        String strDatasetName,
        String strNewVersion,
        SearchOption search,
        Boolean bIgnoreBaseVersion
        )
    '''
    cxn.UploadDataSet(dest, folder, dataset, new_version, SearchOption.AllDirectories, True)
    print("Uploaded the dataset")

    # prompt user to select a Model
    model = input('\nModel: (in this example you need to know the name) ')
    
    # set up the arguments for the job
    args = ['"{}" -m "{}"'.format(xml_file, model)]
        
    run_id = cxn.AddRun(job)
    
    # track the progress of the run
    while not cxn.IsRunComplete(run_id):
        print(cxn.GetRunProgress(run_id))
    
    # Download the result
    cxn.DownloadSolution('.', run_id)
    print('Run', run_id, 'is complete.')
            
