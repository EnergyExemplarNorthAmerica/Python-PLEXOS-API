# This code automates the adjustment of the fixed load neccesary to achieve a desired LOLE target.
# The user must define the number of fical years, name of the model, name of the scenario and the adjustment function.
# The code only works in a local machine.
# For more information, please contact Armando L. Figueroa Acevedo (afigueroa-acevedo@misoenergy.org)

import time
import datetime
import sys, os, re
import csv
from shutil import copyfile
import pandas as pd
import sqlite3 as sql
from shutil import copyfile
import subprocess as sp
import math

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly

plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/' # Modify based on local version of PLEXOS.
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

# .NET related imports
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *
from System import *

def query_lole(PASA_STUDY_NAME, totalyears):
    loletable = []
    
    sol_file = 'Model ' + PASA_STUDY_NAME + ' Solution\Model ' + PASA_STUDY_NAME + ' Solution.zip'
    sol = Solution()
    if not os.path.exists(sol_file):
        print("No such file")
        quit
    
    sol.Connection(sol_file)
        db.Close()
        
def parse_logfile(pattern, foldername, modelname, linecount = 1): #this makes the log file
    
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
        
def Launch_PASA(filename, foldername, modelname): #simply just launches PASA
    # launch the model on the local desktop
    # The \n argument is very important because it allows the PLEXOS
    # engine to terminate after completing the simulation
    sp.call([os.path.join(plexos_path, 'PLEXOS64.exe'), filename, r'\n', r'\o', foldername, r'\m', modelname])
  
def main():
    
    Fixed_Load = 1000 #Fixed load to start with for adjusting in MW
    PLEXOSMODEL = 'Automation.xml' #Original model (NOTE this will not be changed, it is only read from)
    PLEXOSMODEL_ADJUSTED = 'AutomationADJj.xml' #Desired name of .xml with additional fixed load
    PASA_STUDY_NAME = 'Study name' #PASA study name exactly
    Scenario = 'Scenario' #scenario that you want to run that is apart of your pasa
    StudyLengthYears = 1 #How many years are in the study
    StudyStartYear = 2007 #Study start years
    ## BE CAREFUL EDITING BELOW ##
    timed = datetime.datetime.now()
    timeformat = timed.strftime('%m/%d/%y at %H:%M')
    print("\n## PASA Automation started on: %s ##" %timeformat)
        
    writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'w')
    writer.write("## PASA Automation started on: %s ##" %timeformat)
    writer.close()
    
    iteration = 0
    start_time = time.time()
    FixedLoadTable = []
    Launch_PASA(PLEXOSMODEL,'',PASA_STUDY_NAME) #solve pasa initially to see if no adjustment is needed
    print("## Initial PASA solved after %s seconds ##" %(time.time() - start_time))
    writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'a')
    writer.write("\n ## Initial PASA solved after %s seconds ##" %(time.time() - start_time))
    
    Lole = query_lole(PASA_STUDY_NAME, StudyLengthYears) #query LOLE value from PASA

    LoleFlag = 0
    for year in range(StudyLengthYears):
        FixedLoadTable.append(Fixed_Load) #fills a table with fixed load value for each years
        
        if float(Lole[year]) < 0.105 and float(Lole[year]) > 0.0995: #initial LOLE check 
            writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'a')
            writer.write('\n STUDY NEEDED NO ADJUSTMENT')
            
            LoleFlag += 1 #max this value can be is the same value as StudyLengthYears
            
    while LoleFlag != (StudyLengthYears): #PLEXOS LOLE Fixed load adjustment loop
        start_time = time.time()
        print("\n")
        LoleFlag = 0
        query_adjustment(PLEXOSMODEL,PLEXOSMODEL_ADJUSTED, FixedLoadTable, Scenario, StudyStartYear) #This command copies the working model and creates a new one that it places fixed load into.
        
        Launch_PASA(PLEXOSMODEL_ADJUSTED,'',PASA_STUDY_NAME) #Launches PASA study inside new adjusted model
        
        Lole = query_lole(PASA_STUDY_NAME, StudyLengthYears) #grabs LOLE

        years = 0
        for years in range(StudyLengthYears): #loop checks and adjusts each years LOLE
        
            if (float(Lole[years])) > 0.105:
                print('For year %d: Total fixed load for an Lole of: %.3f is %d MW 1' %(StudyStartYear + years, float(Lole[years]) , FixedLoadTable[years]))
                writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'a')
                writer.write('\n For year %d: Total fixed load for an Lole of: %.3f is %d MW 1' %(StudyStartYear + years, float(Lole[years]) , FixedLoadTable[years]))
                if (float(Lole[years])) > 0.2: #below 0.2 the log function below goes negative, we dont want that to happen
                    changeamount = 1000*math.log(float(Lole[years])-0.1)+10000
                    FixedLoadTable[years] = FixedLoadTable[years]-changeamount
                else:
                    FixedLoadTable[years] = FixedLoadTable[years] - ((float(Lole[years])-0.1)*500) #Linear moving once LOLE gets close
                    
                    
            if float(Lole[years]) < 0.0995:
                print('For year %d: Total fixed load for an Lole of: %.3f is %d MW 2' %(StudyStartYear + years, float(Lole[years]) , FixedLoadTable[years]))
                writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'a')
                writer.write('\n For year %d: Total fixed load for an Lole of: %.3f is %d MW 2' %(StudyStartYear + years, float(Lole[years]) , FixedLoadTable[years]))
                if float(Lole[years]) == 0:
                    FixedLoadTable[years] = FixedLoadTable[years] + 2500 #If LOLE is just 0, increase amount incrementally until we get away from 0
                else:
                    FixedLoadTable[years] = FixedLoadTable[years] + (10000*(0.1-float(Lole[years]))+8) #Linear function to go up from 0
                
            if float(Lole[years]) < 0.105 and float(Lole[years]) > 0.0995: #If lole is good, dont do anything
                print('For year %d: Total fixed load for an Lole of: %.3f is %d MW DONE' %(StudyStartYear + years, float(Lole[years]) , FixedLoadTable[years]))
                writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'a')
                writer.write('\n For year %d: Total fixed load for an Lole of: %.3f is %d MW DONE' %(StudyStartYear + years, float(Lole[years]) , FixedLoadTable[years]))
                LoleFlag += 1
                
        print("## PASA iteration %d solved after %s seconds ##" %(iteration,(time.time() - start_time)))
        writer = open(`(PLEXOSMODEL)` + `(PASA_STUDY_NAME)` + `(Scenario)` + ".csv", 'a')
        writer.write("\n ## PASA iteration %d solved after %s seconds ##" %(iteration,(time.time() - start_time)))
        writer.close()             
        iteration = iteration + 1
    print("END")
        
if __name__ == '__main__':
    main()
