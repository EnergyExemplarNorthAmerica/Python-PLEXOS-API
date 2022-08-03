'''
reflection.py

How to use reflection in Pythonnet, and some tricks with Enums.
Specifically with respect to PLEXOS API.

3/21/2020

S Broad
'''

'''
The primary method to use in Pythonnet to leverage reflection in
a .NET type is clr.GetClrType(...). There are several scripts in
this repo that demonstrate this, but here it is summarized.

In pydotnet, you could simply use the type(...) overload which is
nicer, but it isn't difficult in PythonNet.
'''

# First load the PLEXOS API
import sys, clr
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

from PLEXOS_NET.Core import DatabaseCore, Solution, PLEXOSConnect
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *

# Example of getting method list
# the main item here is where clr.GetClrType is used
print(','.join([m.Name for m in clr.GetClrType(DatabaseCore).GetMethods()]) + '\n')

# Example of getting enum values
# the main item here is where clr.GetClrType is used
# we will get all values of the enum
print(','.join([str(v) for v in clr.GetClrType(ClassEnum).GetEnumValues()]) + '\n')

# if you have run this script, you will notice that this is different
# from the native behavior of a .NET Enum value .ToString() method call
# In Pythonnet, enum values are *just* integers, with no attachment to
# the original enum name

# suppose you need the string associated with a specific enum value
# e.g., ClassEnum.System
print (ClassEnum.System) # prints System
print (int(ClassEnum.System)) # prints 1
print (str(ClassEnum.System)) # prints System

# to get from the value to the text do the following
print (clr.GetClrType(ClassEnum).GetEnumName(ClassEnum.System)) # prints System

# to get from the text to the value do the following
from System import Enum
print (Enum.Parse(clr.GetClrType(ClassEnum), 'System')) # prints System




