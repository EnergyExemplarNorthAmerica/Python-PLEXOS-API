


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
    from System import Enum

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


def list_enum_names(t):
    """
    a function to format the presentation of enumerations
    :param t:
    :return:
    """
    lst = list()

    try:
        if t.IsEnum:

            names = t.GetEnumNames()
            for idx in range(0, len(names), 4):
                for jdx in range(idx, min(len(names), idx + 4)):
                    lst.append('{}'.format(names[jdx]))

        else:
            pass
    except:
        return lst

    return lst


def get_all_enums_structure():
    """

    :return:
    """
    data = dict()
    all_enums = get_all_enums()
    for cls in all_enums:
        if cls.IsEnum:
            data[cls.Name] = list_enum_names(cls)

    return data


def generate_enums_python_code():
    """
    Generate Python Enums for the .net CLR enums
    :return:
    """
    for key, values in get_all_enums_structure().items():

        if hasattr(plx_enums, key):
            cls = getattr(plx_enums, key)

            print('class ' + key + '(Enum):\n')
            for val in values:
                # print('\t' + val + ' = plx_enums.' + key + '.' + val)
                if hasattr(cls, val):
                    print('\t' + val + ' =', getattr(cls, val))

            print('\n')

# if you have run this script, you will notice that this is different
# from the native behavior of a .NET Enum value .ToString() method call
# In Pythonnet, enum values are *just* integers, with no attachment to
# the original enum name
# # suppose you need the string associated with a specific enum value
# # e.g., ClassEnum.System
# print(plx_enums.ClassEnum.System)  # prints 1
# print(str(plx_enums.ClassEnum.System))  # prints 1
#
# # to get from the value to the text do the following
# print(clr.GetClrType(plx_enums.ClassEnum).GetEnumName(plx_enums.ClassEnum.System))  # prints System
#
# # to get from the text to the value do the following
#
# print(Enum.Parse(clr.GetClrType(plx_enums.ClassEnum), 'System'))  # prints 1


if __name__ == '__main__':

    print(get_method_list())

    print(get_enum_values())

    enums_data = get_all_enums_structure()

    generate_enums_python_code()