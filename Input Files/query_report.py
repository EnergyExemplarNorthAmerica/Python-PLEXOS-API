import os, sys, clr, pandas as pd

sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 10.0 API')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

from PLEXOS_NET.Core import DatabaseCore
from EnergyExemplar.PLEXOS.Utility.Enums import *
from EEUTILITY.Enums import *

def recordset_to_list(rs):
    result = []
    while rs.EOF == False:
        row = []
        for f in rs.Fields:
            row.append(rs[f.Name])
        result.append(row)
        rs.MoveNext()
    return result

def get_report_properties(model_name):
    plx = DatabaseCore()
    plx.Connection(os.path.join(os.path.dirname(__file__),'rts_PLEXOS.xml'))
    
    classes = plx.FetchAllClassIds()
    collections = plx.FetchAllCollectionIds()

    report_names = plx.GetChildMembers(collections["ModelReport"], model_name)
    report_id = [plx.ObjectName2Id(classes["Report"], x) for x in report_names]

    rst, x = plx.GetData('t_report',[])
    report_data = recordset_to_list(rst)
    report_df = pd.DataFrame(report_data, columns=[f.Name for f in rst.Fields])
    rst.Close()
    report_df['filtered_report'] = report_df['object_id'].apply(lambda x: x in report_id)
    report_df = report_df[report_df['filtered_report']]

    rst, x = plx.GetData('t_property_report',[])
    report_prop = recordset_to_list(rst)
    report_prop_df = pd.DataFrame(report_prop, columns=[f.Name for f in rst.Fields])
    rst.Close()
    report_prop_df = report_prop_df.set_index('property_id')
    df = report_df.join(report_prop_df,on='property_id',rsuffix='_prop')
    
    plx.Close()
    return df

def main():
    get_report_properties('Q3 DA').to_csv(os.path.join(os.path.dirname(__file__),'q3dareport.csv'), index=False)

if __name__ == '__main__':
    main()
