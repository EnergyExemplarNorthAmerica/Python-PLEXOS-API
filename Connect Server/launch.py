# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven

P9 Tested
"""

# standard Python/SciPy libraries
import getpass
from time import sleep
from datetime import datetime

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
import PLEXOS_NET.Core as plx
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import *

server =   input('Server:          ')
port =     input('Port (def:8888): ')
try:
    port = int(port)
except:
    port = 8888
username = input('Username:        ')
password = getpass.getpass('Password:        ')

# connect to the PLEXOS Connect server
cxn = plx.PLEXOSConnect()
cxn.DisplayAlerts = False
cxn.Connection('Data Source={}:{};User Id={};Password={}'.format(server,port,username,password))

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
    if version == '':
        version = cxn.GetDatasetLatestVersion(folder,dataset)

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
    