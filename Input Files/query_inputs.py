# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven

P9 Tested
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *

# Create an object to store the input data
db = DatabaseCore()
'''
Void Connection(
	String strFile
	)
'''

if os.path.exists('Input Files'): os.chdir('Input Files')

db.Connection('rts_PLEXOS.xml')
db.DisplayAlerts = False

classes = db.FetchAllClassIds()
collections = db.FetchAllCollectionIds()

output_file = open('rts_PLEXOS.txt','w')

# list the generators
output_file.write('List of generators\n')
'''
String[] GetObjects(
	int nClassId
	)
'''
for gen in db.GetObjects(classes["Generator"]):
    output_file.write(gen + '\n')
    
# query data for a generator
'''
Recordset GetPropertiesTable(
	int CollectionId,
	String ParentNameList[ = None],
	String ChildNameList[ = None],
	String TimesliceList[ = None],
	String ScenarioList[ = None],
	String CategoryList[ = None]
	)
'''
rs = db.GetPropertiesTable(collections["SystemGenerators"],'','101_1')
rs.MoveFirst()

# write the data in the table from the ADODB.Recordset
if not rs is None and not rs.EOF:
    output_file.write('\n\nProperties of generator 101_1\n' + ','.join([x.Name for x in rs.Fields])+'\n')
    while not rs.EOF:
        output_file.write(','.join([str(x.Value) for x in rs.Fields])+'\n')
        rs.MoveNext()
rs.Close()

# close the output file
output_file.close()

db.Close()