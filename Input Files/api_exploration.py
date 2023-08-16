# -*- coding: utf-8 -*-
"""
Explore the DatabaseCore class

Created on Sat Sep 09 20:11:21 2017

@author: Steven

P92 Tested
"""

import os, sys, pythonnet
pythonnet.load('coreclr')

# load PLEXOS assemblies

import clr
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.2')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore

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
              
with open(os.path.join(os.path.dirname(__file__), 'DatabaseCoreMethods.txt'), 'w') as fout:
    for method in clr.GetClrType(DatabaseCore).GetMethods():
        fout.write(list_method(method))

