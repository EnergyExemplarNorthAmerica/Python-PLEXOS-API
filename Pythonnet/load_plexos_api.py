'''
load_plexos_api.py

How to use Pythonnet with PLEXOS API

3/21/2020

S Broad
'''

'''
If you are familiar with pydotnet from previous examples, you will have
seen the following.

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files/Energy Exemplar/PLEXOS 9.0 API'
add_assemblies(plexos_path)
load_assembly('PLEXOS_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
'''

'''
There a few basic things to change in order to use Python for .NET instead.

1) import sys, clr
sys is the python system package
clr is the Pythonnet Common Language Runtime package
    that is what is used to connect Python to .NET

2) load PLEXOS assemblies
clr.AddReference(...) # instead of load_assembly(...)

Most other things are similar
'''

import sys, clr

# instead of add_assemblies(...) do this
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')

# instead of load_assemblies(...) do this
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# you can import .NET modules just like you used to...
from PLEXOS_NET.Core import DatabaseCore, PLEXOSConnect, Solution
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *

'''
API code as usual
'''
