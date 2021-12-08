# -*- coding: utf-8 -*-
"""
Connect to a PLEXOS Solution File.

Created on Fri Sep 08 15:03:46 2017

@author: Steven
"""

# standard Python/SciPy libraries
import os, clr, sys

# Python .NET interface
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *

# Create a PLEXOS solution file object and load the solution
sol = Solution()
sol_file = 'Model Q2 Week1 DA Solution.zip' # replace with your solution file
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
results = sol.Query(SimulationPhaseEnum.STSchedule, \
                    CollectionEnum.SystemGenerators, \
                    '', \
                    '', \
                    PeriodEnum.FiscalYear, \
                    SeriesTypeEnum.Values, \
                    '')

# Check to see if the query had results
if results.EOF:
    print('No results')
    exit
else:
    results.MoveFirst()

print('\t'.join([x.Name for x in results.Fields]))

# loop through the recordset    
while not results.EOF:
    print('\t'.join([str(x.Value) for x in results.Fields]))
    results.MoveNext() #VERY IMPORTANT
    
