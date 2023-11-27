# -*- coding: utf-8 -*-
"""
Create scenarios and add data overlays to a PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven

P9 Tested
"""

import os, sys, clr
from datetime import datetime
from shutil import copyfile

# load PLEXOS assemblies
# unfortunately there was an error in the PLEXOS 8.1 API that caused
#   scenario tagging to fail. It was fixed in version 8.2.
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import DateTime

if os.path.exists('Input Files'): os.chdir('Input Files')

if os.path.exists('rts_PLEXOS.xml'):

    # delete the modified file if it already exists
    if os.path.exists('rts4.xml'):
        os.remove('rts4.xml')

    # copy the PLEXOS input file
    copyfile('rts_PLEXOS.xml', 'rts4.xml')
    
    # Create an object to store the input data
    db = DatabaseCore()
    db.DisplayAlerts = False
    db.Connection('rts4.xml')
    
    classes = db.FetchAllClassIds()
    collections = db.FetchAllCollectionIds()
    properties = db.FetchAllPropertyEnums()

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
    if not db.CategoryExists(classes["Scenario"], 'Added by API'):
        db.AddCategory(classes["Scenario"], 'Added by API')

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
    db.AddObject(scenario, classes["Scenario"], True, 'Added by API')

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
    
    # parameters
    mem_id = db.GetMembershipID(collections["SystemFuels"],'System','NG/CT')
    enum_id = properties["SystemFuels.Price"]
    
    # we'll add three property rows... monthly gas prices for 3 months
    params = [(mem_id, enum_id, 1, 5.0, DateTime(2024,1,1), None, None, None, None, scenario, None, PeriodEnum.Interval),
              (mem_id, enum_id, 1, 5.1, DateTime(2024,2,1), None, None, None, None, scenario, None, PeriodEnum.Interval),
              (mem_id, enum_id, 1, 4.8, DateTime(2024,3,1), None, None, None, None, scenario, None, PeriodEnum.Interval)]
    
    # invoke
    for p in params:
        '''
        If you use version 8.1 there will be an exception here stating 
        that the scenario couldn't be found. Switch to 8.0 or 8.2.
        '''
        db.AddProperty(*p)

    # Add the scenario to a model
    '''
    Int32 AddMembership(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    '''
    db.AddMembership(collections["ModelScenarios"], 'Q1 DA', scenario)
    
    # save the data set
    db.Close()
    