import sys, os, re
from shutil import copyfile
import subprocess as sp


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
            lines.append(line.strip())
            currentlines -= 1
            
        if currentlines == 0 and len(lines) > 0:
            retval = '\n'.join(lines)
            lines = []
            yield retval
            
def main():
    plexospath = "C:\\Program Files\\Energy Exemplar\\PLEXOS 10.0"
    run_model(plexospath, 'test.xml', '.', 'Base')
    for res in parse_logfile('ST Schedule Completed', '.', 'Base', 25):
        print(res)
        
if __name__ == '__main__':
    main()
    
    
    
    