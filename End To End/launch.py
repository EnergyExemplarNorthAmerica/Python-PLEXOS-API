import sys, os, re
from shutil import copyfile
import subprocess as sp

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/'

add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from System import *

def run_model(plexospath, filename, foldername, modelname):

    # launch the model on the local desktop
    # The \n argument is very important because it allows the PLEXOS
    # engine to terminate after completing the simulation
    sp.call([os.path.join(plexospath, 'PLEXOS64.exe'), filename, r'\n', r'\o', foldername, r'\m', modelname])

def parse_logfile(pattern, foldername, modelname, linecount = 1):
    
    currentlines = 0
    lines = []
    regex = re.compile(pattern)
    
    for line in open(os.path.join(foldername, 'Model {} Solution'.format(modelname), 'Model ( {} ) Log.txt'.format(modelname))):
        if len(regex.findall(line)) > 0:
            currentlines = linecount
            
        if currentlines > 0:
            lines.append(line)
            currentlines -= 1
            
        if currentlines == 0 and len(lines) > 0:
            retval = '\n'.join(lines)
            lines = []
            yield retval
            
def main():
    run_model(plexos_path, 'test.xml', '.', 'Base')
    for res in parse_logfile('ST Schedule Completed', '.', 'Base', 25):
        print res
        
if __name__ == '__main__':
    main()
    
    
    
    