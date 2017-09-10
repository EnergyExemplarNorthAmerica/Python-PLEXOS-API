# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 20:33:10 2017

@author: Steven
"""

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/'
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from EEUTILITY.Enums import *

# a function to format the presentation of enumerations
def list_enum_names(t):
    try:
        if t.IsEnum:
            text = '{}\n'.format(t.Name)
            names = t.GetEnumNames()
            for idx in range(0,len(names),4):
                for jdx in range(idx,min(len(names),idx+4)):
                    text += '\t{}'.format(names[jdx])
                text += '\n'
        else:
            text = 'Not an enumeration'
    except:
        text = 'Not a type'
    finally:
        return text
    
# traverse all enums
for t in type(ClassEnum).Assembly.GetTypes():
    print list_enum_names(t)
    
# ClassEnum is immediately useful
print list_enum_names(type(ClassEnum))