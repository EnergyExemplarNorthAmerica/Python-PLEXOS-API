# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 20:33:10 2017

@author: Steven
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 8.3/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

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
for t in clr.GetClrType(ClassEnum).Assembly.GetTypes():
    print(list_enum_names(t))
