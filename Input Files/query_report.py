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
    plx.Connection(os.path.join(os.path.dirname(__file__),'rts_PLEXOS.xml'))

    report_names = plx.GetChildMembers(CollectionEnum.ModelReport, model_name)
    report_id = [plx.ObjectName2Id(ClassEnum.Report, x) for x in report_names]

    rst, x = plx.GetData('t_report',[])
    rr = rst.GetRows()
    report_df = pd.DataFrame([[rr[i, j] for i in range(rr.GetLength(0))] for j in range(rr.GetLength(1))],columns = [x.Name for x in rst.Fields])
    report_df['filtered_report'] = report_df['object_id'].apply(lambda x: x in report_id)
    report_df = report_df[report_df['filtered_report']]

    rst, x = plx.GetData('t_property_report',[])
    rr = rst.GetRows()
    report_prop_df = pd.DataFrame([[rr[i, j] for i in range(rr.GetLength(0))] for j in range(rr.GetLength(1))],columns = [x.Name for x in rst.Fields])
    report_prop_df = report_prop_df.set_index('property_id')
    df = report_df.join(report_prop_df,on='property_id',rsuffix='_prop')
    return df

def main():
    get_report_properties('Q3 DA').to_csv(os.path.join(os.path.dirname(__file__),'q3dareport.csv'), index=False)

if __name__ == '__main__':
    main()
