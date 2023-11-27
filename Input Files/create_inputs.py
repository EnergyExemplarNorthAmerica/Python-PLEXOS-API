# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven

P9 Tested
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Enum

#Some methods require class and collection names instead of enums,
# so we will cache the conversion from enum to string
CLASS_NAMES = {}
SYSTEM_COLLECTION_NAMES = {}

def cache_classes(db):
    global CLASS_NAMES
    rs = db.GetData("t_class", None)[0]
    while rs.EOF == False:
        CLASS_NAMES[rs["class_id"]] = rs["name"]
        rs.MoveNext()
    rs.Close()
    
def cache_system_collections(db):
    global SYSTEM_COLLECTION_NAMES
    rs = db.GetData("t_collection", None)[0]
    while rs.EOF == False:
        if rs["parent_class_id"] == 1:
            SYSTEM_COLLECTION_NAMES[rs["child_class_id"]] = rs["name"]
        rs.MoveNext()
    rs.Close()
    
def add_plexos_prop(db, parent_class_id, child_class_id, collection_id, \
                    parent_name, child_name, prop_name, prop_value, \
                    category = ''):
    '''
    Create a simple plexos object and populate some
    system properties.
    '''
    
    # Add the category if it hasn't been added yet
    cats = db.GetCategories(child_class_id)
    if len(category) > 0:
        if cats is None or category not in cats:
            db.AddCategory(child_class_id, category)
    
    # Add the object if it hasn't been added yet
    objs = db.GetObjects(child_class_id)
    if objs is None or child_name not in objs:
        db.AddObject(child_name, child_class_id, True, category, 'Added from Python')

    '''
    Int32 GetMembershipID(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    '''
    mem_id = db.GetMembershipID(collection_id, parent_name, child_name)
    '''
    Int32 PropertyName2EnumId(
    	String strParentClassName,
    	String strChildClassName,
    	String strCollectionName,
    	String strPropertyName
    	)
    '''
    enum_id = db.PropertyName2EnumId(
        CLASS_NAMES[int(parent_class_id)],
        CLASS_NAMES[int(child_class_id)],
        SYSTEM_COLLECTION_NAMES[int(child_class_id)],
        prop_name
    )

    db.AddProperty(mem_id, enum_id, 1, prop_value, None, None, None, \
              None, None, None, 0, PeriodEnum.Interval)
    
# delete the modified file if it already exists
if os.path.exists('new.xml'):
    os.remove('new.xml')

# Create an object to store the input data
db = DatabaseCore()
db.DisplayAlerts = False

# create a new database
'''
Boolean NewEmptyDatabase(
	String filePath,
	Boolean overwrite[ = False]
	)
'''
db.NewEmptyDatabase('./new.xml', True)
db.Connection('new.xml')

# Build enum to string lookups
cache_classes(db)
cache_system_collections(db)

classes = db.FetchAllClassIds()
collections = db.FetchAllCollectionIds()

# Four generators
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A1', 'Units', 1, 'A')
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A1', 'Max Capacity', 50)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A1', 'Fuel Price', 1.5)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A1', 'Heat Rate', 10)

add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A2', 'Units', 1, 'A')
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A2', 'Max Capacity', 50)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A2', 'Fuel Price', 1.5)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'A2', 'Heat Rate', 11)

add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B1', 'Units', 1, 'B')
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B1', 'Max Capacity', 20)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B1', 'Fuel Price', 3)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B1', 'Heat Rate', 10)

add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B2', 'Units', 1, 'B')
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B2', 'Max Capacity', 50)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B2', 'Fuel Price', 3)
add_plexos_prop(db, classes["System"], classes["Generator"], collections["SystemGenerators"], 'System', 'B2', 'Heat Rate', 11)

# Two regions
add_plexos_prop(db, classes["System"], classes["Region"], collections["SystemRegions"], 'System', 'A', 'Load', 0)
add_plexos_prop(db, classes["System"], classes["Region"], collections["SystemRegions"], 'System', 'B', 'Load', 120)

# Two nodes
add_plexos_prop(db, classes["System"], classes["Node"], collections["SystemNodes"], 'System', 'A', 'Load Participation Factor', 1)
add_plexos_prop(db, classes["System"], classes["Node"], collections["SystemNodes"], 'System', 'B', 'Load Participation Factor', 1)

# One line
add_plexos_prop(db, classes["System"], classes["Line"], collections["SystemLines"], 'System', 'AB', 'Max Flow', 90)

add_plexos_prop(db, classes["System"], classes["GasPipeline"], collections["SystemGasPipelines"], 'System', 'Pip', "Is Available", 1)

# Memberships
'''
Int32 AddMembership(
	CollectionEnum nCollectionId,
	String strParent,
	String strChild
	)
'''
db.AddMembership(collections["GeneratorNodes"],'A1','A')
db.AddMembership(collections["GeneratorNodes"],'A2','A')
db.AddMembership(collections["GeneratorNodes"],'B1','B')
db.AddMembership(collections["GeneratorNodes"],'B2','B')

db.AddMembership(collections["NodeRegion"],'A','A')
db.AddMembership(collections["NodeRegion"],'B','B')

db.AddMembership(collections["LineNodeFrom"],'AB','A')
db.AddMembership(collections["LineNodeTo"],'AB','B')

db.AddObject('A', classes["GasNode"], True, '', 'Added from Python')
db.AddObject('B', classes["GasNode"], True, '', 'Added from Python')
db.AddMembership(collections["GasPipelineGasNodeFrom"], 'Pip', 'A')
db.AddMembership(collections["GasPipelineGasNodeTo"], 'Pip', 'B')

# save the data set
db.Close()
