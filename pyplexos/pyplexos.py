# -*- coding: utf-8 -*-
'''
Add PLEXOS API libraries for Python.

Created on Mon Jun 05 11:36:46 2017

@author: Steven
'''

import sys

# Python .NET interface
if not 'dotnet.seamless' in sys.modules:
    from dotnet.seamless import add_assemblies, load_assembly

# .NET related imports
if not 'PLEXOS7_NET.Core' in sys.modules:
    # load PLEXOS assemblies
    add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
    load_assembly('PLEXOS7_NET.Core')
    import PLEXOS7_NET.Core as plx

if not 'EEUTILITY.Enums' in sys.modules:
    # load PLEXOS assemblies
    add_assemblies('C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.4/')
    load_assembly('EEUTILITY')
    from EEUTILITY.Enums import *

if not 'System' in sys.modules:
    from System import *
    
if not 'System.IO' in sys.modules:
    from System.IO import SearchOption


