# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass, sys, os

# Python .NET interface
if not 'dotnet.seamless' in sys.modules:
    from dotnet.seamless import add_assemblies, load_assembly


# .NET related imports
if not 'PLEXOS7_NET.Core' in sys.modules:
    # load PLEXOS assemblies
    add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/')
    load_assembly('PLEXOS7_NET.Core')
    import PLEXOS7_NET.Core as plx

if not 'EEUTILITY.Enums' in sys.modules:
    # load PLEXOS assemblies
    add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/')
    load_assembly('EEUTILITY')
    from EEUTILITY.Enums import *

if not 'System' in sys.modules:
    from System import *
    
if not 'System.IO' in sys.modules:
    from System.IO import SearchOption

server = input('Server:   ')
username = input('Username: ')
password = getpass.getpass('Password: ')
folder = input('Folder:   ')
dataset = input('Dataset:  ')

if len(dataset) == 0:
    dataset = 'testdb'
    
# connect to the PLEXOS Connect server
cxn = plx.PLEXOSConnect()
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
    
    dest = os.path.join(folder,dataset)
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
    
    
