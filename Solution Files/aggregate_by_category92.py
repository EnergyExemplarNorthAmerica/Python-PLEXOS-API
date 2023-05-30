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
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.2 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')
clr.AddReference('PLEXOSCommon')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from PLEXOSCommon.Enums import *
from System import *

# Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_file = 'Model Base with Losses Solution.zip' # replace with your solution file
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
    propId = sol.PropertyName2EnumId("System", "Generator", "Generators", "Generation")
    results = sol.QueryToList(SimulationPhaseEnum.STSchedule, \
              CollectionEnum.SystemGenerators, \
              '', \
              '', \
              PeriodEnum.Interval, \
              SeriesTypeEnum.Values, \
              str(propId), \
              None, \
              None, \
              '0', \
              '', \
              '', \
              AggregationTypeEnum.CategoryAggregation, \
              '', \
              '', \
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
        wb = pd.ExcelWriter('query_by_category92.xlsx')
        df.to_excel(wb, 'Query') # 'Query' is the name of the worksheet
        wb.save()
