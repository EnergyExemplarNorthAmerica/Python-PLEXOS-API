# -*- coding: utf-8 -*-
"""
Explore the DatabaseCore class

Created on Sat Sep 09 20:11:21 2017

@author: Steven
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 8.3/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore

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
    text += '\n\t)\n\n'
    return text
              
with open('api_exploration.txt', 'w') as fout:
    for method in clr.GetClrType(DatabaseCore).GetMethods():
        fout.write(list_method(method))

