# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:/Program Files (x86)/Energy Exemplar/PLEXOS 8.0')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from System import Enum


def add_plexos_prop(db, parent_class_id, child_class_id, collection_id,
                    parent_name, child_name, prop_name, prop_value,
                    category=''):
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
        if len(category) > 0:
            db.AddObject(child_name, child_class_id, True, category, 'Added from Python')
        else:
            db.AddObject(child_name, child_class_id, True, '', 'Added from Python')
            
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
        Enum.GetName(clr.GetClrType(ClassEnum), parent_class_id),
        Enum.GetName(clr.GetClrType(ClassEnum), child_class_id),
        Enum.GetName(clr.GetClrType(ClassEnum), child_class_id)+'s',
        prop_name)

    db.AddProperty(mem_id, enum_id, 1, prop_value, None, None, None, None, None, None, 0, PeriodEnum.Interval)


# delete the modified file if it already exists
if os.path.exists('new.xml'):
    os.remove('new.xml')

# Create an object to store the input data
db = DatabaseCore()

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

#Two Batteries
#add_plexos_prop(db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries, 'System', 'Battery1', 'Units', 1)
#add_plexos_prop(db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries, 'System', 'Battery1', 'MaxSoC', 2)
#add_plexos_prop(db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries, 'System', 'Battery1', 'MaxPower', 100)

#add_plexos_prop(db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries, 'System', 'Battery2', 'Units', 2)
#add_plexos_prop(db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries, 'System', 'Battery2', 'MaxSoC', 4)
#add_plexos_prop(db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries, 'System', 'Battery2', 'MaxPower', 400)



# Two regions
add_plexos_prop(db, ClassEnum.System, ClassEnum.Region, CollectionEnum.SystemRegions, 'System', 'A', 'Load', 0)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Region, CollectionEnum.SystemRegions, 'System', 'B', 'Load', 120)

# Two nodes
add_plexos_prop(db, ClassEnum.System, ClassEnum.Node, CollectionEnum.SystemNodes, 'System', 'A', 'Load Participation Factor', 1)
add_plexos_prop(db, ClassEnum.System, ClassEnum.Node, CollectionEnum.SystemNodes, 'System', 'B', 'Load Participation Factor', 1)

# One line
add_plexos_prop(db, ClassEnum.System, ClassEnum.Line, CollectionEnum.SystemLines, 'System', 'AB', 'Max Flow', 90)

# Add Two Batteries 

db.AddObject('Battery1', ClassEnum.Battery, True, None, 'Testing the API')
db.AddObject('Battery2', ClassEnum.Battery, True, None, 'Testing the API')

# Adding Battery properties
'''
Steps: get Membership ID
#Step -2 Use that ID to add properties
'''

# Get the System.batteris membership ID for this new batteries
'''
Int32 GetMembershipID(
	CollectionEnum nCollectionId,
	String strParent,
	String strChild
	)    
'''
batt1_mem_id = db.GetMembershipID(CollectionEnum.SystemBatteries, 'System', 'Battery1')
batt2_mem_id = db.GetMembershipID(CollectionEnum.SystemBatteries, 'System', 'Battery2')
    
# Add properties
'''
Int32 AddProperty(
	Int32 MembershipId,
	Int32 EnumId,
	Int32 BandId,
	Double Value,
	Object DateFrom,
	Object DateTo,
	Object Variable,
	Object DataFile,
	Object Pattern,
	Object Scenario,
	Object Action,
	PeriodEnum PeriodTypeId
	)   
'''
# a. An alias for AddProperty
db.AddProperty(batt1_mem_id, int(SystemBatteriesEnum.Units), 1, 0.0, None, None, None, None, None, None, 0, PeriodEnum.Interval)

db.AddProperty(batt1_mem_id, int(SystemBatteriesEnum.Capacity), 1000, 0.0, None, None, None, None, None, None, 0, PeriodEnum.Interval)

db.AddProperty(batt1_mem_id, int(SystemBatteriesEnum.MaxLoad), 100, 0.0, None, None, None, None, None, None, 0, PeriodEnum.Interval)

db.AddProperty(batt2_mem_id, int(SystemBatteriesEnum.Units), 10, 0.0, None, None, None, None, None, None, 0, PeriodEnum.Interval)

    
# Modify the property
# Step-1: Remove the respective property using membership ID
# Step-2 : add the respective property using Membership ID

db.RemoveProperty(batt1_mem_id, int(SystemBatteriesEnum.MaxLoad), 0.0, None, None, None, None, None, None, 0, PeriodEnum.Interval)

db.AddProperty(batt1_mem_id, int(SystemBatteriesEnum.MaxLoad), 200, 0.0, None, None, None, None, None, None, 0, PeriodEnum.Interval)
    

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

db.AddMembership(CollectionEnum.BatteryNode, 'Battery1', 'A')
db.AddMembership(CollectionEnum.BatteryNode, 'Battery2', 'B')

db.AddMembership(CollectionEnum.NodeRegion,'A','A')
db.AddMembership(CollectionEnum.NodeRegion,'B','B')

db.AddMembership(CollectionEnum.LineNodeFrom,'AB','A')
db.AddMembership(CollectionEnum.LineNodeTo,'AB','B')

# save the data set
db.Close()
