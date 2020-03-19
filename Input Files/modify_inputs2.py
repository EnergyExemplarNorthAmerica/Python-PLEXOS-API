# -*- coding: utf-8 -*-
"""
Create scenarios and add data overlays to a PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os
from datetime import datetime
from shutil import copyfile

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/'
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from System import *

if os.path.exists('rts_PLEXOS.xml'):

    # delete the modified file if it already exists
    if os.path.exists('rts4.xml'):
        os.remove('rts4.xml')

    # copy the PLEXOS input file
    copyfile('rts_PLEXOS.xml', 'rts4.xml')
    
    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection('rts4.xml')

    # Add a category of scenarios if needed
    '''
    Boolean CategoryExists(
    	ClassEnum nClassId,
    	String strCategory
    	)
    Int32 AddCategory(
    	ClassEnum nClassId,
    	String strCategory
    	)
    '''
    if not db.CategoryExists(ClassEnum.Scenario, 'Added by API'):
        db.AddCategory(ClassEnum.Scenario, 'Added by API')

    # Add a scenario
    '''
    Int32 AddObject(
    	String strName,
    	ClassEnum nClassId,
    	Boolean bAddSystemMembership,
    	String strCategory[ = None],
    	String strDescription[ = None]
    	)
    '''
    scenario = 'API{:%Y%m%d%H%M}'.format(datetime.now())
    db.AddObject(scenario, ClassEnum.Scenario, True, 'Added by API')

    # Create data and tag it with the scenario
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
    # alias
    add_prop = db.AddProperty[Int32,Int32,Int32,Double,Object,Object, \
                              Object,Object,Object,Object,Object,PeriodEnum]
    
    # parameters
    mem_id = db.GetMembershipID(CollectionEnum.SystemFuels,'System','NG/CT')
    enum_id = int(SystemFuelsEnum.Price) 
    
    # we'll add three property rows... monthly gas prices for 3 months
    params = [(mem_id, enum_id, 1, 5.0, DateTime(2024,1,1), None, None, None, None, scenario, None, PeriodEnum.Interval),
              (mem_id, enum_id, 1, 5.1, DateTime(2024,2,1), None, None, None, None, scenario, None, PeriodEnum.Interval),
              (mem_id, enum_id, 1, 4.8, DateTime(2024,3,1), None, None, None, None, scenario, None, PeriodEnum.Interval)]
    
    # invoke
    for p in params:
        add_prop.__invoke__(p)
    
    # Add the scenario to a model
    '''
    Int32 AddMembership(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    '''
    db.AddMembership(CollectionEnum.ModelScenarios, 'Q1 DA', scenario)
    
    # save the data set
    db.Close()
    