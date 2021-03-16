

import os
import sys
import clr  # from package "pythonnet"


__program_files__ = os.environ["ProgramFiles(x86)"]
__plexos_base_folder__ = os.path.join(__program_files__, 'Energy Exemplar', 'PLEXOS 8.0')


if os.path.exists(__plexos_base_folder__):

    # load PLEXOS assemblies
    sys.path.append(__plexos_base_folder__)
    clr.AddReference('PLEXOS7_NET.Core')
    clr.AddReference('EEUTILITY')

    # .NET related imports
    import PLEXOS7_NET.Core as plx
    import EEUTILITY.Enums as plx_enums

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

    return [str(v) for v in clr.GetClrType(plx_enums.ClassEnum).GetEnumValues()]


def get_all_enums():
    """

    :return:
    """
    return clr.GetClrType(plx_enums.ClassEnum).Assembly.GetTypes()


if __name__ == '__main__':

    print(get_method_list())

    print(get_enum_values())
