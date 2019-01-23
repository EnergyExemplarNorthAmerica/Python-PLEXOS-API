# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:42:56 2018

@author: Steven.Broad
"""

import os, datetime as dt
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

    '''
    String[] GetChildMembers(
    	CollectionEnum nCollectionId,
    	String strParent
    	)
    '''
    getchildren = db.GetChildMembers[CollectionEnum,String]
    
    '''
    Boolean UpdateAttribute(
    	ClassEnum nClassId,
    	String strObjectName,
    	Int32 nAttributeEnum,
    	Double dNewValue <--- always a Double... need to convert DateTime to Double
                         <--- using the ToOADate() method of the DateTime class
    	)
    '''

    # aliases for UpdateAttribute and AddAttribute methods      
    update = db.UpdateAttribute[ClassEnum,String,Int32,Double]
    add = db.AddAttribute[ClassEnum,String,Int32,Double]
    
    horizons = getchildren.__invoke__((CollectionEnum.ModelHorizon, modelname))
    for hor in horizons:
        update.__invoke__((ClassEnum.Horizon, hor, int(HorizonAttributeEnum.DateFrom), DateTime(start.Year, 1, 1).ToOADate()))
        update.__invoke__((ClassEnum.Horizon, hor, int(HorizonAttributeEnum.StepType), 4))
        update.__invoke__((ClassEnum.Horizon, hor, int(HorizonAttributeEnum.ChronoDateFrom), start.ToOADate()))
                    
    # save the data set
    db.Close()
    
    # return the path of the newly created plexos input file
    return tempfile
    
def main():
    modify_model_horizon('test.xml', 'Base', DateTime.Today)
    
if __name__ == '__main__':
    main()