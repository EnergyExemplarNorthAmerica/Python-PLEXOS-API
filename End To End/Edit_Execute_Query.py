
import os, sys, re, clr
import subprocess as sp
import pandas as pd
from datetime import datetime

from shutil import copyfile

plexospath = 'C:/Program Files/Energy Exemplar/PLEXOS 10.0'
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore, Solution, PLEXOSConnect
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *

def update_dataset(original_ds, new_ds):
    if os.path.exists(original_ds):

        # delete the modified file if it already exists
        if os.path.exists(new_ds):
            os.remove(new_ds)

        # copy the PLEXOS input file
        copyfile(original_ds, new_ds)
        
        # Create an object to store the input data
        db = DatabaseCore()
        db.Connection(new_ds)
        
        classes = db.FetchAllClassIds()
        collections = db.FetchAllCollectionIds()
        properties = db.FetchAllPropertyEnums()
        
        # Add a category
        '''
        Int32 AddCategory(
            ClassEnum nClassId,
            String strCategory
            )
        '''
        db.AddCategory(classes["Generator"], 'API')
        
        # Add an object (and the System Membership)
        '''
        Int32 AddObject(
            String strName,
            ClassEnum nClassId,
            Boolean bAddSystemMembership,
            String strCategory[ = None],
            String strDescription[ = None]
            )
        '''
        db.AddObject('ApiGen', classes["Generator"], True, 'API', 'Testing the API')
        
        # Add memberships
        '''
        Int32 AddMembership(
            CollectionEnum nCollectionId,
            String strParent,
            String strChild
            )
        '''
        db.AddMembership(collections["GeneratorNodes"], 'ApiGen', '101')    
        db.AddMembership(collections["GeneratorFuels"], 'ApiGen', 'Coal/Steam')
        db.AddMembership(collections["ReserveGenerators"], 'Spin Up', 'ApiGen')
        
        # Get the System.Generators membership ID for this new generator
        '''
        Int32 GetMembershipID(
            CollectionEnum nCollectionId,
            String strParent,
            String strChild
            )    
        '''
        mem_id = db.GetMembershipID(collections["SystemGenerators"], 'System', 'ApiGen')
                                    
        # Add properties
        '''
        Int32 AddProperty(
            Int32 MembershipId,
            Int32 EnumId,
            Int32 BandId,
            Double Value,
            Object DateFrom,
            Object DateTo,
            Object Variable,
            Object DataFile,
            Object Pattern,
            Object Scenario,
            Object Action,
            PeriodEnum PeriodTypeId
            )
        
        Also we need to obtain the EnumId for each property
        that we intend to add
        '''
        # Add a property
        db.AddProperty(mem_id, properties["SystemGenerators.Units"],
                1, 0.0, None, None, None, None, None, None,
                0, PeriodEnum.Interval)
        
        # save the data set
        db.Close()

#Execute = db.GetModelsToExecute('rts2.xml',\
                            #'Base',\
                           # '')
							
#Execute the model 
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

def query_results(sol_file, csv_file):
    #Query Results
    # Create a PLEXOS solution file object and load the solution
    if not os.path.exists(sol_file):
        print('No such file')
        return
        
    sol = Solution()
    sol.Connection(sol_file)
    sol.DisplayAlerts = False

    '''
    Simple query: works similarly to PLEXOS Solution Viewer

    Solution.Query(phase, collection, parent, child, period, series, props)
        phase -> SimulationPhaseEnum
        collection -> CollectionEnum
        parent -> the name of a parent object or ''
        child -> the name of a child object or ''
        period -> PeriodEnum
        series -> SeriesTypeEnum
        props -> a string containing an integer indicating the Property to query or ''
    returns a ADODB recordset... however, you don't *need* to worry about that...
    '''
    collections = sol.FetchAllCollectionIds()
    #to query Generation properties
    results = sol.QueryToCSV(
                        csv_file, False,
                        SimulationPhaseEnum.STSchedule,
                        collections["SystemGenerators"],
                        '',
                        '',
                        PeriodEnum.Interval,
                        SeriesTypeEnum.Names,
                        '1')
               
    df = pd.read_csv(csv_file)
    wb = pd.ExcelWriter(re.sub('\.csv$', '.xlsx', csv_file))
    df.to_excel(wb, 'Query') # 'Query' is the name of the worksheet

    wb.close()

def main():
    update_dataset('rts_PLEXOS.xml', 'rts2.xml')
    run_model(plexospath, 'rts2.xml', '.', 'Base')
    for res in parse_logfile('ST Schedule Completed', '.', 'Base', 25):
        print(res)
    query_results('Model Base Solution/Model Base Solution.zip', 'Gens.csv')   


if __name__ == '__main__':
    main()
