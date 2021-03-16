from PlexosAPI.api import plx_enums, get_all_enums


def list_enum_names(t):
    """
    Returns a list of the enumerations if t is a C# Enum
    :param t: C# Enum ideally
    :return: list of Enum values
    """
    lst = list()

    try:
        if t.IsEnum:
            names = t.GetEnumNames()
            for idx in range(0, len(names), 4):
                for jdx in range(idx, min(len(names), idx + 4)):
                    lst.append('{}'.format(names[jdx]))

    except:
        return lst

    return lst


def get_all_enums_structure():
    """
    Dictionary of Enums
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
    :return: Nothing, it prints on the console
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


def generate_database_code():
    """
    Generate Python Enums for the .net CLR enums
    :return: Nothing, it prints on the console
    """

    template = '''    def get_{0}_df(self, pivot_values=False):
        """
        Get table of {1} records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.{2}, pivot_values)
    '''
    import re

    def camel_case_split(identifier):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
        return [m.group(0).lower() for m in matches]

    for key, values in get_all_enums_structure().items():

        if hasattr(plx_enums, key):
            cls = getattr(plx_enums, key)

            if key == 'CollectionEnum':
                for val in values:
                    if hasattr(cls, val):
                        title = '_'.join(camel_case_split(val))
                        print(template.format(title, val, val))


if __name__ == '__main__':

    enums_data = get_all_enums_structure()

    # generate_enums_python_code()

    generate_database_code()
