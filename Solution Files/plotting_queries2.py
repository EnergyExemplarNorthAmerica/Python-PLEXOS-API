# -*- coding: utf-8 -*-
"""
Connect to a PLEXOS Solution File, load data into pandas DataFrame,
and write an Excel file.

Created on Fri Sep 08 15:03:46 2017

@author: Steven
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
add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *
import System

# Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_file = 'Model Q2 Week1 DA Solution.zip' # replace with your solution file
if not os.path.exists(sol_file):
    print 'No such file'
else:
        
    sol.Connection(sol_file)
    
    '''
    Simple query: works similarly to PLEXOS Solution Viewer
    
    Solution.Query(phase, collection, parent, child, period, series, props)
        phase -> SimulationPhaseEnum
        collection -> CollectionEnum
        parent -> the name of a parent object or ''
        child -> the name of a child object or ''
        period -> PeriodEnum
        series -> SeriesTypeEnum
        props -> a string containing an integer indicating the Property to query or ''
    returns a ADODB recordset... however, you don't *need* to worry about that...
    '''
    
    # Run the query
    results = sol.Query(SimulationPhaseEnum.STSchedule, \
                        CollectionEnum.SystemGenerators, \
                        '', \
                        '', \
                        PeriodEnum.Interval, \
                        SeriesTypeEnum.Names, \
                        '1')
    
    # Check to see if the query had results
    if results == None or results.EOF:
        print 'No results'
    
    else:
    
        # Create a DataFrame with a column for each column in the results
        cols = [x.Name for x in results.Fields]
        names = cols[cols.index('phase_name')+1:]
        df = pd.DataFrame(columns=cols)
        
        # loop through the recordset
        idx = 0    
        while not results.EOF:
            if results.Fields['category_name'].Value == 'Coal/Steam':
                df.loc[idx] = [datetime(x.Value.Year,x.Value.Month,x.Value.Day,x.Value.Hour,x.Value.Minute,0) if str(type(x.Value)) == 'System.DateTime' else x.Value for x in results.Fields]
                idx += 1
            results.MoveNext() #VERY IMPORTANT
        
        # plotting the results
        # https://matplotlib.org/api/pyplot_api.html
        plot_df = df.loc[:,names]
        plot_df.index = df._date
        ax = plot_df.plot(title='Total Generation', figsize=(18,11), stacked=True)
        ax.set_xlabel('Generator')
        ax.set_ylabel('Generation (MWh)')
        # save the plot to a file
        ax.figure.savefig('generation.png')
