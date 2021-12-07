# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:55:30 2019

@author: Steven.Broad
"""

# standard Python/SciPy libraries
import os, clr, sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility import *
from System import *

# Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_file = 'Model Q2 Week1 DA Solution.zip' # replace with your solution file
if not os.path.exists(sol_file):
    print('No such file')
else:
        
    sol.Connection(sol_file)
    
    '''
    Simple query: works similarly to PLEXOS Solution Viewer
    
    Recordset Query(
    	SimulationPhaseEnum SimulationPhaseId,
    	CollectionEnum CollectionId,
    	String ParentName,
    	String ChildName,
    	PeriodEnum PeriodTypeId,
    	SeriesTypeEnum SeriesTypeId,
    	String PropertyList[ = None],
    	Object DateFrom[ = None],
    	Object DateTo[ = None],
    	String TimesliceList[ = None],
    	String SampleList[ = None],
    	String ModelName[ = None],
    	AggregationEnum AggregationType[ = None],
    	String Category[ = None],
    	String Filter[ = None]
    	)
    '''
    
    # Setup and run the query
    results = sol.Query(SimulationPhaseEnum.STSchedule, \
              CollectionEnum.SystemGenerators, \
              '', \
              '', \
              PeriodEnum.Interval, \
              SeriesTypeEnum.Values, \
              '1', \
              DateTime.Parse('4/1/2024'), \
              DateTime.Parse('4/1/2024'), \
              '0', \
              '', \
              '', \
              AggregationEnum.Category, \
              '', \
              '')

    # Check to see if the query had results
    if results == None or results.EOF:
        print('No results')
    
    else:
        results.MoveFirst()

        # Create a DataFrame with a column for each column in the results
        cols = [x.Name for x in results.Fields]
        names = cols[cols.index('phase_name')+1:]
        df = pd.DataFrame(columns=cols)
        
        # loop through the recordset
        idx = 0    
        while not results.EOF:
            df.loc[idx] = [datetime(x.Value.Year,x.Value.Month,x.Value.Day,x.Value.Hour,x.Value.Minute,0) if str(type(x.Value)) == 'System.DateTime' else x.Value for x in results.Fields]
            idx += 1
            results.MoveNext() #VERY IMPORTANT

    wb = pd.ExcelWriter('query_by_category.xlsx')
    df.to_excel(wb, 'Query') # 'Query' is the name of the worksheet
    wb.save()
