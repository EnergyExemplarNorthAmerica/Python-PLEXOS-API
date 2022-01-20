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
from datetime import datetime

def make_property_list(*property_enums):
    '''
    Provide a list of property enums as parameters (as many as you like).
    This function will return a string that can be used in the property_list 
    param of the Solution.Query() method.
    '''
    return ','.join([str(x) for x in property_enums])

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 8.3/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *

# Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_folder = os.path.dirname(__file__)
sol_file = os.path.join(sol_folder, 'Model Q2 Week1 DA Solution.zip') # replace with your solution file
if not os.path.exists(sol_file):
    print('No such file')
    exit
    
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
# This example selects a handful of outputs (instead of all of them) to query from the output
# Note that SystemOutGeneratorsEnum corresponds to the CollectionEnum.SystemGenerators that was
# also a parameter of this call. THey must correspond to each other.
#    e.g. 
#       CollectionEnum.SystemRegions and SystemOutRegionsEnum
#       CollectionEnum.ReserveGenerators and ReserveOutGeneratorsEnum
#   etc.
results = sol.Query(
    SimulationPhaseEnum.STSchedule, CollectionEnum.SystemGenerators, 
    '', '', PeriodEnum.FiscalYear, SeriesTypeEnum.Values, 
    make_property_list(
        SystemOutGeneratorsEnum.Generation,
        SystemOutGeneratorsEnum.TotalGenerationCost,
        SystemOutGeneratorsEnum.NetRevenue,
        SystemOutGeneratorsEnum.SRMC
        )
    )

# Check to see if the query had results
if results.EOF:
    print('No results')
    exit

# Create a DataFrame with a column for each selected column in the results.
resultsRows = results.GetRows()

# list out the fields you want to retain with headers in the order you prefer
my_columns = [
    ('parent_name', 'Parent'), 
    ('child_name', 'Name'),
    ('property_name', 'Property'),
    ('_date', 'Timestamp'), 
    ('value', 'Value'), 
    ('phase_name', 'Phase')
    ]
# my_columns = [(x.Name,x.Name) for x in results.Fields] # use this if you just want all fields
my_columns_idx = {x.Name: idx for (idx, x) in enumerate(results.Fields)} # map the field names to their indices

# construct the pandas data frame from a filtered 2D list
df = pd.DataFrame(
    [
        [
            resultsRows[i, j] 
            for i in [my_columns_idx[col] for col, hdr in my_columns] # obtain the field numbers in the correct order
        ] 
        for j in range(resultsRows.GetLength(1))
    ],
    columns = [hdr for col, hdr in my_columns] # obtain the column headers in the correct order
    )
    
# write the pandas data to an Excel worksheet
wb = pd.ExcelWriter(os.path.join(sol_folder, 'query.xlsx'))
df.to_excel(wb, 'Query') # 'Query' is the name of the worksheet
wb.save()
