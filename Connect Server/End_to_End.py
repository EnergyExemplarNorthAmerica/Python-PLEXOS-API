# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run
Created on Thu Aug 06 2020
@author: Harika Kuppa
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
from EnergyExemplar.PLEXOS.Utility import *
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
os.chdir('C:\\Users\\Sri.Harika.Kuppa\\Desktop\\testdb')
if os.path.exists('new.xml'):

    # delete the modified file if it already exists

    if os.path.exists('new2.xml'):
        os.remove('new2.xml')

    # copy the PLEXOS input file
    copyfile('new.xml', 'new2.xml')
    
    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection('new2.xml')
    
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

folder = input('Folder:   ')
dataset = input('Dataset:  ')

if len(dataset) == 0:
    dataset = 'testdb'
    
# verify that the dataset exists
if not cxn.CheckDatasetExists(folder,dataset):
    '''
    Boolean AddDataset(
    	String strFolderPath,
    	String strName
    	)
    '''
    cxn.AddDataset(folder,dataset)
    new_version = '1.0'
    
else:
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
source_folder = 'C:\\Users\\Sri.Harika.Kuppa\\Desktop\\testdb'
#source_folder = str(join(dirname(__file__),'testdb'))

print(source_folder)
cxn.UploadDataSet(source_folder, folder, dataset, new_version, SearchOption.AllDirectories, True)
print("Uploaded the dataset")

folder = input('Folder:   ')
dataset = input('Dataset:  ')
jobset = input('Jobset:   ')

if len(jobset) == 0:
    jobset = 'API{:%Y%m%d%H%M}'.format(datetime.now())

# verify that the dataset exists
if cxn.CheckDatasetExists(folder,dataset):
    
    print()
    print('Select the dataset version')
    # List out the versions
    for v in cxn.GetDatasetVersions(folder,dataset):
        print(v)
        
    version = input('Which version? (Enter for latest)')
    
    print
    print('Select the .xml database')
    files = cxn.GetDatasetFiles(folder,dataset,version)
    
    # list out all of the files
    for (idx, f) in zip(range(len(files)),files):
        print(idx + 1, '--->', f)
        
    file_num = int(input('Which file? (Enter the number): '))
    
    # prompt user to select a Model
    xml_file = files[file_num - 1]
    model = input('\nModel: (in this example you need to know the name) ')
    
    # Remove the jobset as needed
    if cxn.CheckJobsetExists(jobset):
        cxn.RemoveJobset(jobset)

    # set up the arguments for the job
    args = ['"{}" -m "{}"'.format(xml_file, model)]
    
    # create a job set and add a job to it
    if cxn.AddJobset(jobset):
        
        # add the job and run it
        job = cxn.AddJob(jobset, folder, dataset, version, args, '', '', 0)
        run_id = cxn.AddRun(job)
        
        # track the progress of the run
        while not cxn.IsRunComplete(run_id):
            print(cxn.GetRunProgress(run_id))
        
        # Download the result
        cxn.DownloadSolution('.', run_id)
        print('Run', run_id, 'is complete.')
        
        
    else:
        print('Jobset', jobset, 'not created.')
        
    
else:
    
    print('Dataset does not exist')

 # Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_file = 'Model Base Solution.zip' # replace with your solution file
csv_file = 'Generation.csv'
if not os.path.exists(sol_file):
    print('No such file')
    exit
else:
    
    sol.Connection(sol_file)

    #to query Generation properties
    results = sol.QueryToCSV( \
                csv_file, False,
                SimulationPhaseEnum.STSchedule, \
                CollectionEnum.SystemGenerators, \
                '', \
                '', \
                PeriodEnum.Interval, \
                SeriesTypeEnum.Names, \
                '1')        
    os.startfile(csv_file)   
 
