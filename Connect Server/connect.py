# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass

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

# connect to the PLEXOS Connect server
cxn = plx.PLEXOSConnect()
cxn.Connection('Data Source={};User Id={};Password={}'.format(server,username,password))

print '*'*30
print 'Datasets'
print '*'*30
for folder in [''] + list(cxn.GetFolders()):
    print folder
    for dataset in cxn.GetDatasets(folder):
        print '\t', dataset
        for version in cxn.GetDatasetVersions(folder,dataset):
            print '\t\t', version

print
print '*'*30
print 'Jobsets'
print '*'*30
for jobset in cxn.GetJobsets():
    print jobset
    
print
print '*'*30
print 'Clients'
print '*'*30
for client in cxn.GetClients():
    print client
    
print
print '*'*30
print 'Accounts'
print '*'*30
for acct in cxn.GetAccounts():
    print acct
    
print
print '*'*30
print 'Engines'
print '*'*30
for engine in cxn.GetEngines():
    print engine
    
