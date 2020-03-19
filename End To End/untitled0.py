# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:59:45 2018

@author: Steven.Broad
"""

import end_to_end_api

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from System import *

db = DatabaseCore()
db.Connection('test2.xml')
res = db.GetPropertiesTable(CollectionEnum.SystemRegions, 'System', 'B')
while not res.EOF:
    for fld in res.Fields:
        print('"{}" = {}'.format(fld.Name, fld.Value))
    res.MoveNext()
    
