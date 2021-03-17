# -*- coding: utf-8 -*-
"""
Connect to a PLEXOS Solution File, load data into pandas DataFrame,
and write an Excel file.

Created on Fri Sep 08 15:03:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import os, sys, clr
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
sys.path.append('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *
from System import Enum, DateTime

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
              SeriesTypeEnum.Names, \
              '1', \
              DateTime.Parse('4/1/2024'), \
              DateTime.Parse('4/1/2024'), \
              '0', \
              '', \
              '', \
              0, \
              'Coal/Steam', \
              '')
   
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
        
        # plotting the results
        # https://matplotlib.org/api/pyplot_api.html
        plot_df = df.loc[:,names]
        plot_df.index = df._date
        ax = plot_df.plot(kind='area', title='Total Generation', figsize=(18,11), stacked=True)
        ax.set_xlabel('Date and Time Starting')
        ax.set_ylabel('Generation (MWh)')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), \
          ncol=1, fancybox=True, shadow=True)
        # save the plot to a file
        ax.figure.savefig('generation.png')
