# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility import *

# Create an object to store the input data
db = DatabaseCore()
'''
Void Connection(
	String strFile
	)
'''
db.Connection('rts_PLEXOS.xml')

output_file = open('rts_PLEXOS.txt','w')

# list the generators
output_file.write('List of generators\n')
'''
String[] GetObjects(
	ClassEnum nClassId
	)
'''
for gen in db.GetObjects(ClassEnum.Generator):
    output_file.write(gen + '\n')
    
# query data for a generator
'''
Recordset GetPropertiesTable(
	CollectionEnum CollectionId,
	String ParentNameList[ = None],
	String ChildNameList[ = None],
	String TimesliceList[ = None],
	String ScenarioList[ = None],
	String CategoryList[ = None]
	)
'''
rs = db.GetPropertiesTable(CollectionEnum.SystemGenerators,'','101_1')
rs.MoveFirst()

# write the data in the table from the ADODB.Recordset
if not rs is None and not rs.EOF:
    output_file.write('\n\nProperties of generator 101_1\n' + ','.join([x.Name for x in rs.Fields])+'\n')
    while not rs.EOF:
        output_file.write(','.join([str(x.Value) for x in rs.Fields])+'\n')
        rs.MoveNext()

# close the output file
output_file.close()