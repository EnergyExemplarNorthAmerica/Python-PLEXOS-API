# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:54:57 2017

@author: Steven
"""

import os, sys, clr

# load PLEXOS assemblies
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.0 API')
clr.AddReference('EEUTILITY')

# .NET related imports
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility import *
from System import Enum

with open('EEUTILITY_Enums.txt', 'w') as fout:
    for t in clr.GetClrType(ClassEnum).Assembly.GetTypes():
        if t.IsEnum:
            fout.write('{}\n'.format(t.Name))
            for en in t.GetEnumNames():
                fout.write('\t{} = {}\n'.format(en, int(Enum.Parse(t, en))))
            fout.write('\n')
