# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:54:57 2017

@author: Steven

P92 Tested
"""

import os, sys, pythonnet
pythonnet.load('coreclr')

import clr
# load PLEXOS assemblies
sys.path.append('C:\Program Files\Energy Exemplar\PLEXOS 9.2')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Enum

def write_enums(*exemplars):
    for exemplar in exemplars:
        assembly = clr.GetClrType(exemplar).Assembly
        filename = assembly.GetName().Name
        with open(os.path.join(os.path.dirname(__file__), filename + '.txt'), 'w') as fout:
            for t in assembly.GetTypes():
                if t.IsEnum:
                    fout.write('{}\n'.format(t.Name))
                    for en in t.GetEnumNames():
                        fout.write('\t{} = {}\n'.format(en, int(Enum.Parse(t, en))))
                    fout.write('\n')

write_enums(ClassEnum, FlatFileFormatEnum)
