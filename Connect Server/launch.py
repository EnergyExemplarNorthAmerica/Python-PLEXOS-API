# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass
from time import sleep
from datetime import datetime

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly

# load PLEXOS assemblies
add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
import PLEXOS7_NET.Core as plx
from EEUTILITY.Enums import *
from System import *

server = raw_input('Server:   ')
username = raw_input('Username: ')
password = getpass.getpass('Password: ')
folder = raw_input('Folder:   ')
dataset = raw_input('Dataset:  ')
jobset = raw_input('Jobset:   ')

if len(jobset) == 0:
    jobset = 'API{:%Y%m%d%H%M}'.format(datetime.now())

# connect to the PLEXOS Connect server
cxn = plx.PLEXOSConnect()
cxn.Connection('Data Source={};User Id={};Password={}'.format(server,username,password))

# verify that the dataset exists
if cxn.CheckDatasetExists(folder,dataset):
    
    print
    print 'Select the dataset version'
    # List out the versions
    for v in cxn.GetDatasetVersions(folder,dataset):
        print v
        
    version = raw_input('Which version? (Enter for latest)')
    
    print
    print 'Select the .xml database'
    files = cxn.GetDatasetFiles(folder,dataset,version)
    
    # list out all of the files
    for (idx, f) in zip(range(len(files)),files):
        print idx + 1, '--->', f
        
    file_num = int(raw_input('Which file? (Enter the number): '))
    
    # prompt user to select a Model
    xml_file = files[file_num - 1]
    model = raw_input('\nModel: (in this example you need to know the name) ')
    
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
            print cxn.GetRunProgress(run_id)
        
        # Download the result
        cxn.DownloadSolution('.', run_id)
        print 'Run', run_id, 'is complete.'
        
        
    else:
        print 'Jobset', jobset, 'not created.'
        
    
else:
    
    print 'Dataset does not exist'