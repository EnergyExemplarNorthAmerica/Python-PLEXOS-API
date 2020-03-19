# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os, re

# Python .NET interface
from dotnet import add_assemblies, load_assembly#, build_assembly
from dotnet.overrides import type, isinstance, issubclass
from dotnet.commontypes import *

# load PLEXOS assemblies
plexos_path = 'C:/Program Files/Energy Exemplar/PLEXOS 8.2/'
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *

# Create an object to store the input data
db = DatabaseCore()
'''
Void Connection(
	String strFile
	)
'''
db.Connection('rts_PLEXOS.xml')

with open('rts_PLEXOS.txt','w') as output_file:

    # list the generators
    output_file.write('List of lines\n')
    '''
    String[] GetObjects(
        ClassEnum nClassId
        )
    '''

    for from_node, to_node in zip(db.GetMemberships(CollectionEnum.LineNodeFrom), db.GetMemberships(CollectionEnum.LineNodeTo)):
        from_match = re.match('Line \( (.*?) \)\.Node From \( (.*?) \)', from_node)
        to_match = re.match('Line \( (.*?) \)\.Node To \( (.*?) \)', to_node)
        output_file.write('{}: {} --> {}\n'.format(from_match[1], from_match[2], to_node[2]))

    '''
    for line_name in db.GetObjects(ClassEnum.Line): 
        print(line_name)
        for child_1, child_2 in zip(db.GetChildMembers(CollectionEnum.LineNodeFrom, line_name), db.GetChildMembers(CollectionEnum.LineNodeTo, line_name)):
            print (child_1, child_2) 
    '''
    '''
    rst = db.GetPropertiesTable(CollectionEnum.SystemLines)

    try:
        rst.MoveFirst()

        while not rst.EOF:
            print(','.join(['{} --> {}'.format(fld.Name, fld.Value) for fld in rst.Fields]))
            rst.MoveNext()
    except:
        pass
    '''