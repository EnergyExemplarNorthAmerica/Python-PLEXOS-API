# -*- coding: utf-8 -*-
"""
Connect to a PLEXOS Solution File, load data into pandas DataFrame,
and write an Excel file.

Created on Fri Sep 08 15:03:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import os, clr, sys
import pandas as pd
import matplotlib.pyplot as plt

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
    exit
    
sol.Connection(sol_file)

'''
Simple query: works similarly to PLEXOS Solution Viewer

Solution.QueryToList(phase, collection, parent, child, period, series, props)
    phase -> SimulationPhaseEnum
    collection -> CollectionEnum
    parent -> the name of a parent object or ''
    child -> the name of a child object or ''
    period -> PeriodEnum
    series -> SeriesTypeEnum
    props -> a string containing an integer indicating the Property to query or ''
'''

collections = sol.FetchAllCollectionIds()
# Run the query
results = sol.QueryToList(SimulationPhaseEnum.STSchedule, \
                          collections["SystemGenerators"], \
                          '', \
                          '', \
                          PeriodEnum.FiscalYear, \
                          SeriesTypeEnum.Values, \
                          '')
                          
#Important to Close() the Solution to clear working storage.
sol.Close()

# Check to see if the query had results
if results is None:
    print('No results')
    exit

# Create a DataFrame with a column for each column in the results
#fetch all columns
columns = results.Columns
#NOTE: Specifying a limited set of columns here may significantly improve performance.
#eg columns = ["child_name", "property_name", "_date", "value"]
values = [[row.GetProperty.Overloads[String](n) for n in columns] for row in results]
df = pd.DataFrame(values, columns=columns)

# plotting the results
# https://matplotlib.org/api/pyplot_api.html
plot_df = df.loc[lambda df: df.property_name == 'Fuel Cost', ['child_name', 'value']]
plot_df = plot_df.loc[lambda df: df.value > 0, :]
ax = plot_df.plot(x='child_name', y='value', kind='bar', legend=None, \
                  title='Fuel Cost', figsize=(12,7))
ax.set_xlabel('Generator')
ax.set_ylabel('Fuel Cost $000')

# save the plot to a file
ax.figure.savefig('fuelcost.png')
