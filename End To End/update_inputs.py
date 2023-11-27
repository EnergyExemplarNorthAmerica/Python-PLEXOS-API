# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 07:12:40 2018

@author: Steven.Broad
"""

# -*- coding: utf-8 -*-
"""
Create scenarios and add data overlays to a PLEXOS input dataset

Created on Sat Sep 09 19:19:57 2017

@author: Steven
"""

import os, sys, clr
from datetime import datetime
from shutil import copyfile

sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Object, String, Int32, Double

def create_datafile_object(plexosfile, datafilename, datafilepath, copyfileto=''):
    if not os.path.exists(plexosfile):
        raise Exception('"{}" does not exist'.format(plexosfile))
        
    if not copyfileto == '':
        if os.path.exists(copyfileto):
            os.remove(copyfileto)
        copyfile(plexosfile, copyfileto)
        plexosfile = copyfileto
        
    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection(plexosfile)

    classes = db.FetchAllClassIds()
    collections = db.FetchAllCollectionIds()
    properties = db.FetchAllPropertyEnums()
    
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
    db.AddObject(datafilename, classes["DataFile"], True)

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
    mem_id = db.GetMembershipID(collections["SystemDataFiles"], 'System', datafilename)
    enum_id = int(properties["SystemDataFiles.Filename"])
    
    # we'll add three property rows... monthly gas prices for 3 months
    params = [(mem_id, enum_id, 1, 0, None, None, None, datafilepath, None, None, None, PeriodEnum.Interval),]
    
    # invoke
    for p in params:
        db.AddProperty(*p)
    
    # Add the scenario to a model
    '''
    Int32 AddMembership(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    db.AddMembership(collections["ModelScenarios"], 'Q1 DA', scenario)
    '''
    
    # save the data set
    db.Close()
    
    # pass the plexos file path (.xml) whether copied or not
    return plexosfile
        
def attach_datafile_to_object(plexosfile, datafilename, collectionenum, propertyenum, objectname, parentname = 'System'):
    if not os.path.exists(plexosfile):
        raise Exception('"{}" does not exist'.format(plexosfile))
        
    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection(plexosfile)
    
    classes = db.FetchAllClassIds()
    collections = db.FetchAllCollectionIds()
    properties = db.FetchAllPropertyEnums()

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
    res = db.GetPropertiesTable(collections[collectionenum], parentname, objectname)
    
    '''
    Int32 RemoveProperty(
	Int32 MembershipId,
	Int32 EnumId,
	Int32 BandId,
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
    mem_id = db.GetMembershipID(collections[collectionenum], parentname, objectname)
    enum_id = properties[propertyenum]

    while not res.EOF:
        fields = dict([(res.Fields[i].Name.replace('_x0020_', ''), res.Fields[i].Value) for i in range(res.Fields.Count)])
        if fields['Property'] == str(propertyenum):
            db.RemoveProperty(mem_id, enum_id, \
                            1 if 'Band' not in fields else int(fields['Band']), \
                            None if 'DateFrom' not in fields else fields['DateFrom'], \
                            None if 'DateTo' not in fields else fields['DateTo'], \
                            None if 'Variable' not in fields else fields['Variable'], \
                            None if 'DataFile' not in fields else fields['DataFile'], \
                            None if 'Pattern' not in fields else fields['Pattern'], \
                            None if 'Scenario' not in fields else fields['Scenario'], \
                            '=' if 'Action' not in fields else fields['Action'], \
                            PeriodEnum.Interval)
        print(fields)
        
        res.MoveNext()
    
    
    
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
    mem_id = db.GetMembershipID(collections[collectionenum], parentname, objectname)
    enum_id = properties[propertyenum]
    
    # we'll add three property rows... monthly gas prices for 3 months
    params = [(mem_id, enum_id, 1, 0, None, None, None, datafilename, None, None, None, PeriodEnum.Interval),]
    
    # invoke
    for p in params:
        db.AddProperty(*p)
    
    # Add the scenario to a model
    '''
    Int32 AddMembership(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    db.AddMembership(collections["ModelScenarios"], 'Q1 DA', scenario)
    '''
    
    # save the data set
    db.Close()
    
def update_load_csv_file(csv_file, start_date, data, minutes_per_interval = 60):
    row_length = int(24*60/minutes_per_interval)
    rows = int((len(data) - 1)/row_length) + 1
    with open(csv_file, 'w') as fout:
        fout.write('Year,Month,Day,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24\n')
        for i in range(rows):
            fout.write('{},{},{},'.format(start_date.year, start_date.month, start_date.day))
            fout.write('{}\n'.format(','.join([str(val) for val in data[i*row_length:(i+1)*row_length]])))
    
    
def main():
    plexosfile = create_datafile_object('test.xml', 'Load File', r'CSV Files\load.csv', 'test2.xml')
    attach_datafile_to_object(plexosfile, 'Load File', "SystemRegions", "SystemRegions.Load", 'B')
    from random import random
    update_load_csv_file(r'CSV Files\load.csv', datetime.today(), [80 + int(40 * random()) for i in range(168)])
    
if __name__ == '__main__':
    main()