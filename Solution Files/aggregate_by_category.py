# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:55:30 2019

@author: Steven.Broad
"""

# standard Python/SciPy libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/')
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *
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
    # a. Alias the Query method with the arguments you plan to use.
    query = sol.Query[SimulationPhaseEnum,CollectionEnum,String,String, \
                      PeriodEnum, SeriesTypeEnum, String, Object, Object, \
                      String, String, String, AggregationEnum, String, \
                      String]

    # b. Construct a tuple of values to send as parameters.
    params = (SimulationPhaseEnum.STSchedule, \
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

    # c. Use the __invoke__ method of the alias to call the method.
    results = query.__invoke__(params)
    
    # Check to see if the query had results
    if results == None or results.EOF:
        print('No results')
    
    else:
    
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
