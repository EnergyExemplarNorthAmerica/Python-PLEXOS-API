# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 20:33:10 2017

@author: Steven
"""

import os, sys, clr

# load PLEXOS assemblies
__program_files__ = os.environ["ProgramFiles(x86)"]
__plexos_base_folder__ = os.path.join(__program_files__, 'Energy Exemplar', 'PLEXOS 8.0')

sys.path.append(__plexos_base_folder__)
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
            for idx in range(0, len(names), 4):
                for jdx in range(idx, min(len(names), idx + 4)):
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
