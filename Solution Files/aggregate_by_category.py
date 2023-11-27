# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:55:30 2019

@author: Steven.Broad
"""

# standard Python libraries
import os, clr, sys
import pandas as pd
from datetime import datetime

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
    props = sol.FetchAllPropertyEnums()
    propId = sol.PropertyName2EnumId("System", "Generator", "Generators", "Generation")
    results = sol.QueryToList(SimulationPhaseEnum.STSchedule,
              collections["SystemGenerators"],
              '',
              '',
              PeriodEnum.Interval,
              SeriesTypeEnum.Values,
              str(propId),
              DateTime.Parse('2024-04-01'),
              DateTime.Parse('2024-04-07'),
              '0',
              '',
              '',
              AggregationTypeEnum.CategoryAggregation,
              '',
              '',
              OperationTypeEnum.SUM)
              
    #Important to Close() the Solution to clear working storage.
    sol.Close()

    # Check to see if the query had results
    if results is None:
        print('No results')
    else:
        # Create a DataFrame with a column for each column in the results
        columns = ["category_name", "property_name", "_date", "value"]
        df = pd.DataFrame([[row.GetProperty.Overloads[String](n) for n in columns] for row in results], columns=columns)
        wb = pd.ExcelWriter('query_by_category.xlsx')
        df.to_excel(wb, 'Query') # 'Query' is the name of the worksheet
        wb.close()
