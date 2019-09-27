# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 16:03:57 2017

@author: Steven
"""

import dotnet as dot

dot.add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
dot.load_assembly('EEUTILITY')

from EEUTILITY.Enums import *

def list_enum_names(enum):
    try:
        if not enum.IsEnum:
            return ''
        return '\n\t'.join([''] + ['{} = {}'.format(a, int(b)) for a, b in zip(enum.GetEnumNames(), enum.GetEnumValues())])
    except:
        return ''

with open('query_enums.txt','w') as fout:
    # traverse all enums
    for t in type(CollectionEnum).Assembly.GetTypes():
        fout.write('{}{}\n\n'.format(t.Name, list_enum_names(t)))

