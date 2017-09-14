# -*- coding: utf-8 -*-
"""
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

if cxn.CheckDatasetExists(folder,dataset):
    
    for v in cxn.GetDatasetVersions(folder,dataset):
        print v
        
    version = raw_input('Which version? ')
    
    files = cxn.GetDatasetFiles(folder,dataset,version)
    
    for (idx, f) in zip(range(len(files)),files):
        print idx + 1, '--->', f
        
    file_num = int(raw_input('Which file? (Enter the number): '))
    
    xml_file = files[file_num - 1]
    model = raw_input('Model:    ')
    
    if cxn.CheckJobsetExists(jobset):
        cxn.RemoveJobset(jobset)

    args = ['"{}" -m "{}"'.format(xml_file, model)]
    if cxn.AddJobset(jobset):
        job = cxn.AddJob(jobset, folder, dataset, version, args, '', '', 0)
        run_id = cxn.AddRun(job)
    else:
        print 'Jobset', jobset, 'not created.'
        
    
else:
    
    print 'Dataset does not exist'