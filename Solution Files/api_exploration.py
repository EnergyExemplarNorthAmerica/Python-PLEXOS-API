# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 09:41:33 2017

@author: Steven
"""

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly

# load PLEXOS assemblies... replace the path below with the installation
#   installation folder for your PLEXOS installation.
add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *

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
       
for method in type(Solution).GetMethods():
    print list_method(method)

