# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 16:03:57 2017

@author: Steven
"""

import dotnet.seamless as dot

dot.add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
dot.load_assembly('EEUTILITY')

from EEUTILITY.Enums import *

def list_enum_names(enum):
    try:
        if not enum.IsEnum:
            return ''
        return '\n\t'.join([''] + list(enum.GetEnumNames()))
    except:
        return ''

print 'SimulationPhaseEnum', list_enum_names(type(SimulationPhaseEnum))
print 'CollectionEnum', list_enum_names(type(CollectionEnum))
print 'PeriodEnum', list_enum_names(type(PeriodEnum))
print 'SeriesTypeEnum', list_enum_names(type(SeriesTypeEnum))
