# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/'
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *

# Create an object to store the input data
db = DatabaseCore()
db.Connection('rts_PLEXOS.xml')

# list the generators
for gen in db.GetObjects(ClassEnum.Generator):
    print gen
    
# query data for a generator
rs = db.GetPropertiesTable(CollectionEnum.SystemGenerators,'','101_1')
rs.MoveFirst()

if not rs is None and not rs.EOF:
    print ','.join([x.Name for x in rs.Fields])
    while not rs.EOF:
        print ','.join([str(x.Value) for x in rs.Fields])
        rs.MoveNext()
        
