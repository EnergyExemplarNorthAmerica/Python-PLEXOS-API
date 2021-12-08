# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 09:41:33 2017

@author: Steven
"""

# Python .NET interface
import clr, sys

sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS_NET.Core import *
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *

def list_method(method):
    text = '{} {}('.format(method.ReturnType.Name, method.Name)
    isFirst = True
    for param in method.GetParameters():
        if isFirst:
            isFirst = False
            text += '\n\t{} {}'.format(param.ParameterType.Name, param.Name)
        else:
            text += ',\n\t{} {}'.format(param.ParameterType.Name, param.Name)
        if param.HasDefaultValue:
            text += '[ = {}]'.format(param.DefaultValue)
    text += '\n\t)\n'
    return text
       
with open('api_exploration.txt', 'w') as fout:
    sol = Solution()
    for method in sol.GetType().GetMethods():
        fout.write('{}\n'.format(list_method(method)))


