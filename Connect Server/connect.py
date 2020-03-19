# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass

# Python .NET interface
from dotnet import add_assemblies, load_assembly

# load PLEXOS assemblies
add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/')
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
import PLEXOS7_NET.Core as plx
from EEUTILITY.Enums import *
from System import *

server = input('Server:   ')
username = input('Username: ')
password = getpass.getpass('Password: ')

# connect to the PLEXOS Connect server
cxn = plx.PLEXOSConnect()
cxn.Connection('Data Source={};User Id={};Password={}'.format(server,username,password))

if not cxn.CheckAccountExists(username):
    exit()

with open('connect_system.txt','w') as fout:
    fout.write('*'*30 + '\n')
    fout.write('Datasets' + '\n')
    fout.write('*'*30 + '\n')
    filecount = 0
    for folder in [''] + list(cxn.GetFolders()):
        fout.write(folder + '\n')
        for dataset in cxn.GetDatasets(folder):
            fout.write('\t' + dataset + '\n')
            filecount += 1
            for version in cxn.GetDatasetVersions(folder,dataset):
                fout.write('\t\t' + version + '\n')
        if filecount > 100:
            fout.write('\n\t\t...\n')
        fout.flush()

    fout.write('*'*30 + '\n')
    fout.write('Jobsets' + '\n')
    fout.write('*'*30 + '\n')
    for jobset in cxn.GetJobsets():
        fout.write(jobset + '\n')
        
    print
    fout.write('*'*30 + '\n')
    fout.write('Clients' + '\n')
    fout.write('*'*30 + '\n')
    for client in cxn.GetClients():
        fout.write(client + '\n')
        
    print
    fout.write('*'*30 + '\n')
    fout.write('Accounts' + '\n')
    fout.write('*'*30 + '\n')
    for acct in cxn.GetAccounts():
        fout.write(acct + '\n')
        
    print
    fout.write('*'*30 + '\n')
    fout.write('Engines' + '\n')
    fout.write('*'*30 + '\n')
    for engine in cxn.GetEngines():
        fout.write(engine + '\n')
        
