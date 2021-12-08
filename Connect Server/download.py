# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven

P9 Tested
"""

# standard Python/SciPy libraries
import getpass, sys, os, clr

# .NET related imports
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

from PLEXOS_NET.Core import PLEXOSConnect
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
import PLEXOS_NET.Core as plx
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
cxn = plx.PLEXOSConnect()
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
    
    
