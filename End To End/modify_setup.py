# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:42:56 2018

@author: Steven.Broad
"""

import os, sys, clr, datetime as dt
from shutil import copyfile

# load PLEXOS assemblies
plexos_path = 'C:/Program Files/Energy Exemplar/PLEXOS 10.0 API'

sys.path.append(plexos_path)
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import DateTime, String, Int32, Double

def modify_model_horizon(datafile, modelname, start):
    
    tempfile = '{}{:%m%d%Y%H%M%S}.xml'.format(datafile[:-4], dt.datetime.now())
    
    if not os.path.exists(datafile):
        raise Exception('"{}" does not exist'.format(datafile))

    # delete the modified file if it already exists
    if os.path.exists(tempfile):
        os.remove(tempfile)

    # copy the PLEXOS input file
    copyfile(datafile, tempfile)
    
    # Create an object to store the input data
    db = DatabaseCore()
    db.Connection(tempfile)
    
    classes = db.FetchAllClassIds()
    collections = db.FetchAllCollectionIds()
    attributes = db.FetchAllAttributeEnums()

    '''
    String[] GetChildMembers(
    	CollectionEnum nCollectionId,
    	String strParent
    	)
    '''
    
    '''
    Boolean UpdateAttribute(
    	ClassEnum nClassId,
    	String strObjectName,
    	Int32 nAttributeEnum,
    	Double dNewValue <--- always a Double... need to convert DateTime to Double
                         <--- using the ToOADate() method of the DateTime class
    	)
    '''
   
    horizons = db.GetChildMembers(collections["ModelHorizon"], modelname)
    for hor in horizons:
        db.UpdateAttribute(classes["Horizon"], hor, int(attributes["Horizon.DateFrom"]), DateTime(start.Year, 1, 1).ToOADate())
        db.UpdateAttribute(classes["Horizon"], hor, int(attributes["Horizon.StepType"]), 4)
        db.UpdateAttribute(classes["Horizon"], hor, int(attributes["Horizon.ChronoDateFrom"]), start.ToOADate())
                    
    # save the data set
    db.Close()
    
    # return the path of the newly created plexos input file
    return tempfile
    
def main():
    modify_model_horizon('test.xml', 'Base', DateTime.Today)
    
if __name__ == '__main__':
    main()