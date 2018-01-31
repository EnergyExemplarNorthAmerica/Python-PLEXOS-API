# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:54:57 2017

@author: Steven
"""

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/'
add_assemblies(plexos_path)
load_assembly('EEUTILITY')

# .NET related imports
from EEUTILITY.Enums import *
from System import Enum

fout = open('EEUTILITY_Enums.txt', 'w')

for t in type(ClassEnum).Assembly.GetTypes():
    if t.IsEnum:
        fout.write('{}\n'.format(t.Name))
        for en in t.GetEnumNames():
            fout.write('\t{} = {}\n'.format(en, int(Enum.Parse(t, en))))
        fout.write('\n')

fout.close()
