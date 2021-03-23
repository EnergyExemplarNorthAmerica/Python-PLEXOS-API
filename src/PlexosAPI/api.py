"""
PLEXOS API wrapper for easy interaction

The API wraps the low level interaction like loading the .net Dll's, etc.

Santiago Peñate-Vera, Red Eléctrica de España 2021
"""

import os
import sys
import re
import clr  # from package "pythonnet"
from shutil import copyfile
import subprocess as sp


__program_files__ = os.environ["ProgramFiles(x86)"]
__plexos_base_folder__ = os.path.join(__program_files__, 'Energy Exemplar', 'PLEXOS 8.0')


if os.path.exists(__plexos_base_folder__):

    # load PLEXOS assemblies
    sys.path.append(__plexos_base_folder__)
    clr.AddReference('PLEXOS7_NET.Core')
    clr.AddReference('EEUTILITY')

    # .NET related imports
    import PLEXOS7_NET.Core as plx
    from EEUTILITY.Enums import *
    from System import Enum  # do not delete, this is used in other modules

    ClassEnumType = clr.GetClrType(ClassEnum)

    print('Plexos API loaded')

else:
    raise Exception(__plexos_base_folder__ + ' Not found')


def get_method_list():
    """
    Example of getting method list
    the main item here is where clr.GetClrType is used
    :return:
    """

    return [m.Name for m in clr.GetClrType(plx.DatabaseCore).GetMethods()]


def get_enum_values():
    """
    Example of getting enum values
    the main item here is where clr.GetClrType is used
    we will get all values of the enum
    :return:
    """

    return [str(v) for v in clr.GetClrType(ClassEnum).GetEnumValues()]


def get_all_enums():
    """

    :return:
    """
    return clr.GetClrType(ClassEnum).Assembly.GetTypes()


def run_model(filename, foldername, modelname):
    """
     launch the model on the local desktop
    :param filename: .xml file name
    :param foldername: folder where to save the results
    :param modelname: model name
    :return:
    """

    # The \n argument is very important because it allows the PLEXOS engine to terminate after completing the simulation
    sp.call([os.path.join(__plexos_base_folder__, 'PLEXOS64.exe'), filename, r'\n', r'\o', foldername, r'\m', modelname])


def parse_logfile(pattern, folder_name, model_name, line_count=1):
    """

    :param pattern:
    :param folder_name:
    :param model_name:
    :param line_count:
    :return:
    """
    current_lines = 0
    lines = []
    regex = re.compile(pattern)

    fname = os.path.join(folder_name,
                         'Model {} Solution'.format(model_name),
                         'Model ( {} ) Log.txt'.format(model_name))
    
    for line in open(fname):
        if len(regex.findall(line)) > 0:
            current_lines = line_count

        if current_lines > 0:
            lines.append(line)
            current_lines -= 1

        if current_lines == 0 and len(lines) > 0:
            retval = '\n'.join(lines)
            lines = []
            yield retval


if __name__ == '__main__':

    print(get_method_list())

    print(get_enum_values())
