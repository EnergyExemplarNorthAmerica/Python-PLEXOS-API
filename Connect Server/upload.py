# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass
from os.path import dirname, join
import sys

# Python .NET interface
if not 'dotnet.seamless' in sys.modules:
    from dotnet.seamless import add_assemblies, load_assembly


# .NET related imports
if not 'PLEXOS7_NET.Core' in sys.modules:
    # load PLEXOS assemblies
    add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
    load_assembly('PLEXOS7_NET.Core')
    import PLEXOS7_NET.Core as plx

if not 'EEUTILITY.Enums' in sys.modules:
    # load PLEXOS assemblies
    add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
    load_assembly('EEUTILITY')
    from EEUTILITY.Enums import *

if not 'System' in sys.modules:
    from System import *
    
if not 'System.IO' in sys.modules:
    from System.IO import SearchOption

server = raw_input('Server:   ')
username = raw_input('Username: ')
password = getpass.getpass('Password: ')
folder = raw_input('Folder:   ')
dataset = raw_input('Dataset:  ')

if len(dataset) == 0:
    dataset = 'testdb'
    
# connect to the PLEXOS Connect server
cxn = plx.PLEXOSConnect()
cxn.Connection('Data Source={};User Id={};Password={}'.format(server,username,password))

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
source_folder = str(join(dirname(__file__),'testdb'))
cxn.UploadDataSet(source_folder,folder,dataset,new_version,SearchOption.AllDirectories,True)
