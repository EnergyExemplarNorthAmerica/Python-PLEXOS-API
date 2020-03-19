# -*- coding: utf-8 -*-
'''
Add PLEXOS API libraries for Python.

Created on Mon Jun 05 11:36:46 2017

@author: Steven
'''

import sys

# Python .NET interface
if not 'dotnet' in sys.modules:
    from dotnet import add_assemblies, load_assembly
    from dotnet.overrides import type, isinstance, issubclass
    from dotnet.commontypes import *

def load_plexos(plexos_path = ''):

    # load PLEXOS assemblies
    add_assemblies(plexos_path)
    load_assembly('PLEXOS7_NET.Core')
    load_assembly('EEUTILITY')

