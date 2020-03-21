# -*- coding: utf-8 -*-
"""
Launch a PLEXOS Connect run

Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import getpass, os, sys, clr
from os.path import dirname, join

sys.path.append('C:/Program Files (x86)/Energy Exemplar/PLEXOS 8.1/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

from PLEXOS7_NET.Core import PLEXOSConnect
from EEUTILITY.Enums import *
from System.IO import SearchOption

server = input('Server:   ')
username = input('Username: ')
password = getpass.getpass('Password: ')
folder = input('Folder:   ')
dataset = input('Dataset:  ')

if len(dataset) == 0:
    dataset = 'testdb'
    
# connect to the PLEXOS Connect server
cxn = PLEXOSConnect()
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
cxn.UploadDataSet(source_folder, folder, dataset, new_version, SearchOption.AllDirectories, True)
