# -*- coding: utf-8 -*-
"""
Explore the DatabaseCore class

Created on Sat Sep 09 20:11:21 2017

@author: Steven
"""

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/'
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

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
    text += '\n\t)\n'
    return text
       
def def_method(method):
    text = 'def {}({}):\n'.format(method.Name, ',\\\n\t\t\t'.join([str(p.Name).lower() + ('' if not p.HasDefaultValue else ' = {}'.format(p.DefaultValue)) for p in method.GetParameters()]))
    if method.ReturnType.Name == 'Void':
        text += '\tself.db.{}({})\n\n'.format(method.Name, ','.join([str(p.Name).lower() for p in method.GetParameters()]))
    else:
        text += '\treturn self.db.{}({})\n\n'.format(method.Name, ','.join([str(p.Name).lower() for p in method.GetParameters()]))
    return text
       
for method in type(DatabaseCore).GetMethods():
    print(def_method(method))

#print(def_method(type(DatabaseCore).GetMethod('AddProperty')))
