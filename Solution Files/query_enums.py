# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 16:03:57 2017

@author: Steven
"""

import os, sys, clr

sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 8.3/')
clr.AddReference('EEUTILITY')

from EEUTILITY import Enums
from EEUTILITY.Enums import *
from System import Enum, Type

def list_enum_names(enum):
    try:
        if not enum.IsEnum:
            return ''
        return '\n\t'.join([''] + ['{} = {}'.format(a, int(b)) for a, b in zip(enum.GetEnumNames(), enum.GetEnumValues())])
    except:
        return ''

folder = os.path.dirname(__file__)
with open(os.path.join(folder, 'query_enums.txt'),'w') as fout:
    # traverse all enums
    for t in clr.GetClrType(CollectionEnum).Assembly.GetTypes():
        if t.IsEnum:
            fout.write('{}{}\n\n'.format(t.Name, list_enum_names(t)))

