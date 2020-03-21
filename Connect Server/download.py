# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass, sys, os, clr

# .NET related imports
sys.path.append('C:/Program Files (x86)/Energy Exemplar/PLEXOS 8.1/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

from PLEXOS7_NET.Core import PLEXOSConnect
from EEUTILITY.Enums import *
import PLEXOS7_NET.Core as plx
from System.IO import SearchOption

server = input('Server:   ')
username = input('Username: ')
password = getpass.getpass('Password: ')
folder = input('Folder:   ')
local = input('Local Folder: ')
dataset = input('Dataset:  ')

if len(dataset) == 0:
    dataset = 'testdb'
    
# connect to the PLEXOS Connect server
cxn = PLEXOSConnect()
cxn.DisplayAlerts = False
cxn.Connection('Data Source={};User Id={};Password={}'.format(server,username,password))

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
    
    
