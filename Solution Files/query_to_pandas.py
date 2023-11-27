# -*- coding: utf-8 -*-
"""
Connect to a PLEXOS Solution File, load data into pandas DataFrame,
and write an Excel file.

Created on Fri Sep 08 15:03:46 2017

@author: Steven
"""

# standard Python libraries
import os, clr, sys
import pandas as pd

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import String

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
    results = sol.QueryToList(SimulationPhaseEnum.STSchedule,
              collections["SystemGenerators"],
              '',
              '',
              PeriodEnum.FiscalYear,
              SeriesTypeEnum.Values)
              
    #Important to Close() the Solution to clear working storage.
    sol.Close()

    # Check to see if the query had results
    if results is None:
        print('No results')
    else:
        # Create a DataFrame with a column for each column in the results
        columns = results.Columns
        df = pd.DataFrame([[row.GetProperty.Overloads[String](n) for n in columns] for row in results], columns=columns)
        wb = pd.ExcelWriter('query.xlsx')
        df.to_excel(wb, 'Query') # 'Query' is the name of the worksheet
        wb.close()
