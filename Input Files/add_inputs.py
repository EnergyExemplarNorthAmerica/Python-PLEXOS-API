# -*- coding: utf-8 -*-
"""
Retrieve data from the PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os
from shutil import copyfile

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

if os.path.exists('rts_PLEXOS.xml'):

    # delete the modified file if it already exists
    if os.path.exists('rts2.xml'):
        os.remove('rts2.xml')

    # copy the PLEXOS input file
    copyfile('rts_PLEXOS.xml', 'rts2.xml')
    
    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection('rts2.xml')
    
    # Add a category
    '''
    Int32 AddCategory(
    	ClassEnum nClassId,
    	String strCategory
    	)
    '''
    db.AddCategory(ClassEnum.Generator, 'API')
    
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
    mem_id = db.GetMembershipID(CollectionEnum.SystemGenerators, \
                                'System', 'ApiGen')
                                
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
     
    Because of the number of parameters, we need
        a. An alias for AddProperty
        b. A tuple of parameter values
        c. A call to the alias
        
    Also we need to obtain the EnumId for each property
    that we intend to add
    '''
    # a. An alias for AddProperty
    addProp = db.AddProperty[Int32,Int32,Int32,Double,Object, \
                             Object,Object,Object,Object,Object, \
                             Object,PeriodEnum]
    
    # b. A tuple of parameter values
    params = (mem_id, int(PropertyIDEnum.SystemGenerators_Units), \
              1, 0.0, None, None, None, None, None, None, \
              0, PeriodEnum.Interval)
    
    # c. A call to the alias
    addProp.__invoke__(params)
    
    # save the data set
    db.Close()
    