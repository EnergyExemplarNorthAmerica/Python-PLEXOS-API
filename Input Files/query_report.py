import os, re, sys, clr, pandas as pd

sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

from PLEXOS_NET.Core import DatabaseCore
from EnergyExemplar.PLEXOS.Utility.Enums import *
from EEUTILITY.Enums import *

def get_report_properties(model_name):
    plx = DatabaseCore()
    plx.Connection(r'C:\Users\Steven.Broad\Downloads\test_model.xml')

    print('\n'.join(plx.GetObjects(ClassEnum.Model)))
    report_names = plx.GetChildMembers(CollectionEnum.ModelReport, input('Model Name:'))
    model_id = [plx.ObjectName2Id(ClassEnum.Report, x) for x in report_names]
    print(model_id)

    rst, x = plx.GetData('t_report',[])
    rr = rst.GetRows()
    print('\n'.join([x.Name for x in rst.Fields]))
    report_df = pd.DataFrame([[rr[i, j] for i in range(rr.GetLength(0))] for j in range(rr.GetLength(1))],columns = [x.Name for x in rst.Fields])

    rst, x = plx.GetData('t_property_report',[])
    rr = rst.GetRows()
    print('\n'.join([x.Name for x in rst.Fields]))
    report_prop_df = pd.DataFrame([[rr[i, j] for i in range(rr.GetLength(0))] for j in range(rr.GetLength(1))],columns = [x.Name for x in rst.Fields])
    df = report_df.join(report_prop_df,on='property_id',rsuffix='_prop')
    print(df)

def main():
    get_report_properties('Nodal').to_csv('nodal_report.csv')

if __name__ == '__main__':
    main()
