# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os, sys, clr
from shutil import copyfile

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import DateTime

folder = os.path.dirname(__file__)
basefile = os.path.join(folder, 'rts_PLEXOS.xml')
copiedfile = os.path.join(folder, 'rts2.xml')
if os.path.exists(basefile):


    # delete the modified file if it already exists
    if os.path.exists(copiedfile):
        os.remove(copiedfile)

    # copy the PLEXOS input file
    copyfile(basefile, copiedfile)
    
    # Create an object to store the input data
    db = DatabaseCore()
    db.DisplayAlerts = False
    db.Connection(copiedfile)
    
    # Add a category
    '''
    Int32 AddCategory(
    	ClassEnum nClassId,
    	String strCategory
    	)
    '''
    db.AddCategory(ClassEnum.Generator, 'API')
    db.AddCategory(ClassEnum.GasPipeline, 'API')
    
    # Add an object (and the System Membership)
    '''
    Int32 AddObject(
    	String strName,
    	ClassEnum nClassId,
    	Boolean bAddSystemMembership,
    	String strCategory[ = None],
    	String strDescription[ = None]
    	)
    '''
    db.AddObject('ApiGen', ClassEnum.Generator, True, 'API', 'Testing the API')
    db.AddObject('ApiPipe', ClassEnum.GasPipeline, True, 'API', 'Testing the API')

    # Add memberships
    '''
    Int32 AddMembership(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    '''
    db.AddMembership(CollectionEnum.GeneratorNodes, 'ApiGen', '101')    
    db.AddMembership(CollectionEnum.GeneratorFuels, 'ApiGen', 'Coal/Steam')
    db.AddMembership(CollectionEnum.ReserveGenerators, 'Spin Up', 'ApiGen')
    
    # Get the System.Generators membership ID for this new generator
    '''
    Int32 GetMembershipID(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)    
    '''
    mem_id = db.GetMembershipID(
        CollectionEnum.SystemGenerators, 
        'System', 
        'ApiGen'
    )
                                
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
    # Add units for the new generator
    db.AddProperty(
        mem_id, 
        int(SystemGeneratorsEnum.Units), 
        1, 
        0.0, 
        None, 
        None, 
        None, 
        None, 
        None, 
        None, 
        0, 
        PeriodEnum.Interval
    )


    # Add IsAvailable for the new pipeline
    db.AddProperty(
        db.GetMembershipID(
            CollectionEnum.SystemGasPipelines, 
            'System', 
            'ApiPipe'
        ),
        int(SystemGasPipelinesEnum.IsAvailable), 
        1, 
        1, 
        DateTime(2024,1,1),
        None, 
        None, 
        None, 
        None, 
        None, 
        0, 
        PeriodEnum.Interval
    )
    
    # save the data set
    db.Close()
    