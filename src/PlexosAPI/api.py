

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
    from EEUTILITY.Enums import CollectionEnum, ClassEnum, PeriodEnum, NodeAttributeEnum, SystemNodesEnum
    from System import Enum  # do not delete, used in other modules

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

    fname = os.path.join(folder_name, 'Model {} Solution'.format(model_name), 'Model ( {} ) Log.txt'.format(model_name))
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


def __run__():
    run_model('test.xml', '.', 'Base')
    for res in parse_logfile('ST Schedule Completed', '.', 'Base', 25):
        print(res)


def add_plexos_prop(db, parent_class_id, child_class_id, collection_id,
                    parent_name, child_name, prop_name, prop_value,
                    category=''):
    """
    Create a plexos object and populate some system properties.
    :param db: Plexos database instance
    :param parent_class_id:
    :param child_class_id:
    :param collection_id:
    :param parent_name:
    :param child_name:
    :param prop_name:
    :param prop_value:
    :param category:
    :return:
    """

    '''
    
    '''

    # Add the category if it hasn't been added yet
    cats = db.GetCategories(child_class_id)
    if len(category) > 0:
        if cats is None or category not in db.GetCategories(child_class_id):
            db.AddCategory(child_class_id, category)

    # Add the object if it hasn't been added yet
    objs = db.GetObjects(child_class_id)
    if objs is None or child_name not in objs:
        if len(category) > 0:
            db.AddObject(child_name, child_class_id, True, category, 'Added from Python')
        else:
            db.AddObject(child_name, child_class_id, True, '', 'Added from Python')

    '''
    Int32 GetMembershipID(
    	CollectionEnum nCollectionId,
    	String strParent,
    	String strChild
    	)
    '''
    mem_id = db.GetMembershipID(collection_id, parent_name, child_name)
    '''
    Int32 PropertyName2EnumId(
    	String strParentClassName,
    	String strChildClassName,
    	String strCollectionName,
    	String strPropertyName
    	)
    '''
    enum_id = db.PropertyName2EnumId(Enum.GetName(clr.GetClrType(ClassEnum), parent_class_id),
                                     Enum.GetName(clr.GetClrType(ClassEnum), child_class_id),
                                     Enum.GetName(clr.GetClrType(ClassEnum), child_class_id) + 's',
                                     prop_name)

    db.AddProperty(mem_id, enum_id, 1, prop_value,
                   None, None, None, None, None, None,
                   0, PeriodEnum.Interval)



if __name__ == '__main__':

    print(get_method_list())

    print(get_enum_values())
