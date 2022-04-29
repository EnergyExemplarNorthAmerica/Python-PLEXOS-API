# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven

P9 Tested
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Enum

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
        if cats is None or category not in db.GetCategories(child_class_id):
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
    if type(prop_name) == str:
        enum_id = db.PropertyName2EnumId(
            Enum.GetName(clr.GetClrType(ClassEnum), parent_class_id),
            Enum.GetName(clr.GetClrType(ClassEnum), child_class_id),
            Enum.GetName(clr.GetClrType(ClassEnum), child_class_id)+'s',
            prop_name
        )
    elif type(prop_name) == int:
        enum_id = prop_name

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

# Four generators
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A1', 'Units', 1, 'A')
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A1', 'Max Capacity', 50)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A1', 'Fuel Price', 1.5)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A1', 'Heat Rate', 10)

add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A2', 'Units', 1, 'A')
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A2', 'Max Capacity', 50)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A2', 'Fuel Price', 1.5)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'A2', 'Heat Rate', 11)

add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B1', 'Units', 1, 'B')
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B1', 'Max Capacity', 20)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B1', 'Fuel Price', 3)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B1', 'Heat Rate', 10)

add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B2', 'Units', 1, 'B')
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B2', 'Max Capacity', 50)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B2', 'Fuel Price', 3)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Generator, CollectionEnum.SystemGenerators, 'System', 'B2', 'Heat Rate', 11)

# Two regions
add_plexos_prop(db, ClassEnum.System, ClassEnum.Region, CollectionEnum.SystemRegions, 'System', 'A', 'Load', 0)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Region, CollectionEnum.SystemRegions, 'System', 'B', 'Load', 120)

# Two nodes
add_plexos_prop(db, ClassEnum.System, ClassEnum.Node, CollectionEnum.SystemNodes, 'System', 'A', 'Load Participation Factor', 1)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Node, CollectionEnum.SystemNodes, 'System', 'B', 'Load Participation Factor', 1)

# One line
add_plexos_prop(db, ClassEnum.System, ClassEnum.Line, CollectionEnum.SystemLines, 'System', 'AB', 'Max Flow', 90)

add_plexos_prop(db, ClassEnum.System, ClassEnum.GasPipeline, CollectionEnum.SystemGasPipelines, 'System', 'Pip', SystemGasPipelinesEnum.IsAvailable, 1)

# Memberships
'''
Int32 AddMembership(
	CollectionEnum nCollectionId,
	String strParent,
	String strChild
	)
'''
db.AddMembership(CollectionEnum.GeneratorNodes,'A1','A')
db.AddMembership(CollectionEnum.GeneratorNodes,'A2','A')
db.AddMembership(CollectionEnum.GeneratorNodes,'B1','B')
db.AddMembership(CollectionEnum.GeneratorNodes,'B2','B')

db.AddMembership(CollectionEnum.NodeRegion,'A','A')
db.AddMembership(CollectionEnum.NodeRegion,'B','B')

db.AddMembership(CollectionEnum.LineNodeFrom,'AB','A')
db.AddMembership(CollectionEnum.LineNodeTo,'AB','B')

db.AddObject('A', ClassEnum.GasNode, True, '', 'Added from Python')
db.AddObject('B', ClassEnum.GasNode, True, '', 'Added from Python')
db.AddMembership(CollectionEnum.GasPipelineGasNodeFrom, 'Pip', 'A')
db.AddMembership(CollectionEnum.GasPipelineGasNodeTo, 'Pip', 'B')

# save the data set
db.Close()
