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

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')
clr.AddReference('PLEXOSCommon')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from PLEXOSCommon.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Enum, DateTime, String

#NOTE: Because None is a reserved word in Python we must use the Parse() method to get the value of AggregationEnum.None
aggregation_none = Enum.Parse(clr.GetClrType(AggregationTypeEnum), "None")

# Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_file = 'Model Q2 Week1 DA Solution.zip' # replace with your solution file
if not os.path.exists(sol_file):
    print('No such file')
else:
        
    sol.Connection(sol_file)
    
    '''
    Simple query: works similarly to PLEXOS Solution Viewer
    
    QueryToList(
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
    collections = sol.FetchAllCollectionIds()
    properties = sol.FetchAllPropertyEnums()
    propId = properties["SystemGenerators.Generation"]
    results = sol.QueryToList(SimulationPhaseEnum.STSchedule,
              collections["SystemGenerators"],
              '',
              '',
              PeriodEnum.Interval,
              SeriesTypeEnum.Names,
              str(propId),
              DateTime.Parse('2024-04-01'),
              DateTime.Parse('2024-04-01'),
              '0',
              '',
              '',
              aggregation_none,
              'Coal/Steam')

    #Important to Close() the Solution to clear working storage.
    sol.Close()
   
    # Check to see if the query had results
    if results is None:
        print('No results')
    else:
        # Create a DataFrame with a column for each column in the results
        cols = list(results.Columns)
        # phase_name is the last column before the name value columns
        names = cols[cols.index('phase_name')+1:]
        names.append("_date")
        values = [[row.GetProperty.Overloads[String](n) for n in names] for row in results]
        df = pd.DataFrame(values, columns=names)
        # plotting the results
        # https://matplotlib.org/api/pyplot_api.html
        df.index = df._date
        ax = df.plot(kind='area', title='Total Generation', figsize=(18,11), stacked=True)
        ax.set_xlabel('Date and Time Starting')
        ax.set_ylabel('Generation (MWh)')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), \
          ncol=1, fancybox=True, shadow=True)
        # save the plot to a file
        ax.figure.savefig('generation.png')
