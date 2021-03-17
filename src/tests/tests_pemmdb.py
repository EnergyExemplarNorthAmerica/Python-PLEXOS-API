import os
import pandas as pd
import numpy as np
import openpyxl
from PlexosAPI import PlexosDatabase


__this_dir__ = os.path.dirname(os.path.realpath(__file__))

# data common to all the tests

db = PlexosDatabase(file_name=os.path.join(__this_dir__, 'data', 'H2030_base.xml'))
gen_df = db.get_system_generators_df(True)

wb = openpyxl.load_workbook(os.path.join('data', 'PEMMDB21_ES00_NationalTrends_2030.xlsx'))
sheet = wb['Thermal']


def test1():
    '''
    -	POTENCIA INSTALADA NUCLEAR:
        En la pestaña ‘Thermal’ de la PEMMDB aparece la capacidad total en MW (columna C)
        y el número de unidades (columna D). En PLEXOS de nudo único eso se traduce como:
            -	En el objeto Generador, categoría NUCLEAR, generador ‘Nuclear ES00’:
                -	Units: 3
                -	Max Capacity: valor de potencia de la PEMMDB / nº unidades. En el ejemplo, 3054.31 / 3 = 1016.71 MW


    '''

    # PEMMDB values
    nuclear_capacity = sheet['C12'].value
    nuclear_units = sheet['D12'].value
    plx_nuclear_units = int(gen_df.at['Nuclear ES00', 'Units'])
    expected_nuclear_capacity = nuclear_capacity / nuclear_units

    # plexos values
    plx_nuclear_capacity = float(gen_df.at['Nuclear ES00', 'Max Capacity'])

    # checks
    assert plx_nuclear_units == nuclear_units
    assert np.allclose(plx_nuclear_capacity, expected_nuclear_capacity)


def test2():
    '''
    MÍNIMO TÉCNICO NUCLEAR
        En la pestaña ‘Thermal’ de la PEMMDB aparece el mínimo técnico por tecnología como un
        porcentaje sobre la capacidad instalada (columna AJ). En PLEXOS de nudo único eso se traduce como:
        - En el objeto Generador, categoría NUCLEAR, generador ‘Nuclear ES00’:
            Min Stable Level: porcentaje que aparece en la PEMMDB * (potencia instalada total que
            aparece en la PEMMBD (columna C) / nº de unidades (columna D)) / 100.
            En el ejemplo: 40 * (3054.31 / 3) / 100 = 407.24 MW.


    :return:
    '''

    # PEMMDB values
    nuclear_min_stable_level = sheet['AJ12'].value
    nuclear_capacity = sheet['C12'].value
    nuclear_units = sheet['D12'].value
    min_stable_level_expected = nuclear_min_stable_level * (nuclear_capacity / nuclear_units) / 100.0

    # plexos values
    plx_nuclear_min_stable_level = float(gen_df.at['Nuclear ES00', 'Min Stable Level'])

    # checks
    assert np.allclose(plx_nuclear_min_stable_level, min_stable_level_expected)


def test3():

    """
    RAMPAS DE LA NUCLEAR:
        En la pestaña ‘Thermal’ de la PEMMDB aparecen las rampas de subida (columna AK) y
        de bajada (columna AL) en MW/h. En PLEXOS de nudo único hay que pasarlo a MW/min. Eso se traduce como:
        o	En el objeto Generador, categoría NUCLEAR, generador ‘Nuclear ES00’:
            	Max Ramp Up: valor que aparece en la PEMMDB (columna AK) / 60. En el ejemplo: 3055.54 / 60 = 50.93 MW/min
            	Max Ramp Down: valor que aparece en la PEMMDB (columna AL) / 60. En el ejemplo: 3055.54 / 60 = 50.93 MW/min

    :return:
    """

    # PEMMDB values
    nuclear_ramp_up = sheet['AK12'].value
    nuclear_ramp_down = sheet['AL12'].value
    expected_ramp_up = nuclear_ramp_up / 60
    expected_ramp_down = nuclear_ramp_down / 60

    # plexos values
    plx_ramp_up = float(gen_df.at['Nuclear ES00', 'Max Ramp Up'])
    plx_ramp_down = float(gen_df.at['Nuclear ES00', 'Max Ramp Down'])

    # checks
    assert np.allclose(plx_ramp_up, expected_ramp_up)
    assert np.allclose(expected_ramp_down, plx_ramp_down)


if __name__ == '__main__':

    # test1()
    # test2()
    test3()
