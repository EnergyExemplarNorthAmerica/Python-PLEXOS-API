# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 11:36:46 2017

@author: Steven

P9 Tested
"""

# standard Python/SciPy libraries
import getpass, os, sys, clr

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

print('*'*30)
print('Datasets')
print('*'*30)
for folder in [''] + list(cxn.GetFolders()):
    print(folder)
    idx = 0
    for dataset in list(cxn.GetDatasets(folder))[:5]:
        idx += 1
        print('\t', dataset)
        for version in list(cxn.GetDatasetVersions(folder,dataset))[-4:-1]:
            print('\t\t', version)
        if idx >= 10: break # only list 10 datasets (takes too long)

print()
print('*'*30)
print('Jobsets')
print('*'*30)
for jobset in cxn.GetJobsets():
    print(jobset)
    
print()
print('*'*30)
print('Clients')
print('*'*30)
for client in cxn.GetClients():
    print(client)
    
print()
print('*'*30)
print('Accounts')
print('*'*30)
for acct in cxn.GetAccounts():
    print(acct)
    
print()
print('*'*30)
print('Engines')
print('*'*30)
for engine in cxn.GetEngines():
    print(engine)
    
