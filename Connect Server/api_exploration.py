# -*- coding: utf-8 -*-
"""
Explore the DatabaseCore class

Created on Sat Sep 09 20:11:21 2017

@author: Steven

P9 Tested
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import PLEXOSConnect

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
       
with open('PLEXOSConnectMethods.txt','w') as fout:
    fout.writelines([list_method(method) for method in clr.GetClrType(PLEXOSConnect).GetMethods()])
