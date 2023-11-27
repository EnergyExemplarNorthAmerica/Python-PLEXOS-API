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
import sqlite3 as sql

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

# Run the query
collections = sol.FetchAllCollectionIds()
results = sol.QueryToList(SimulationPhaseEnum.STSchedule,
                    collections["SystemGenerators"],
                    '',
                    '',
                    PeriodEnum.FiscalYear,
                    SeriesTypeEnum.Values,
                    '')
                    
#Important to Close() the Solution to clear working storage.
sol.Close()

# Check to see if the query had results
if results is None:
    print('No results')
    exit

# Create a DataFrame with a column for each column in the results
#fetch all columns except _date
#Use date_string or convert the type for _date since _date is not an sqlite3 compatible type.
columns = [n for n in results.Columns if n != "_date"]
#NOTE: Specifying a limited set of columns here may significantly improve performance.
# eg columns = ["child_name", "property_name", "date_string", "value"]
values = [[row.GetProperty.Overloads[String](n) for n in columns] for row in results]
df = pd.DataFrame([[row.GetProperty.Overloads[String](n) for n in columns] for row in results], columns=columns)

# push results to a SQLite3 database    
conn = sql.connect('plexos.db')
df.to_sql('MyQuery', conn, if_exists='replace') # 'MyQuery' is the name of the table

# try a query and push results to an Excel file
sql_df = pd.read_sql_query('SELECT * FROM MyQuery WHERE property_name = "Fuel Cost";', conn)
wb = pd.ExcelWriter('sql_query.xlsx')
sql_df.to_excel(wb, 'SQL Query')

# save the excel file
wb.close()

# close the sqlite3 connection
conn.close()
