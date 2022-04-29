# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 16:03:57 2017

@author: Steven
"""

import os, sys, clr

sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Enum, Type

def list_enum_names(enum):
    try:
        if not enum.IsEnum:
            return ''
        return '\n\t'.join([''] + ['{} = {}'.format(a, int(b)) for a, b in zip(enum.GetEnumNames(), enum.GetEnumValues())])
    except:
        return ''

with open('query_enums.txt','w') as fout:
    # traverse all enums
    for t in clr.GetClrType(CollectionEnum).Assembly.GetTypes():
        if t.IsEnum:
            fout.write('{}{}\n\n'.format(t.Name, list_enum_names(t)))

with open('query_enums.txt','a') as fout:
    # traverse all enums
    for t in clr.GetClrType(AggregationEnum).Assembly.GetTypes():
        if t.IsEnum:
            fout.write('{}{}\n\n'.format(t.Name, list_enum_names(t)))

