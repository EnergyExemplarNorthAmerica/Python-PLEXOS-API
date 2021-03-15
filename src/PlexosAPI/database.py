from PlexosAPI.api import plx, plx_enums


class PlexosDatabase:

    def __init__(self, file_name):

        self.file_name = file_name

        self.db = plx.DatabaseCore()

        self.db.Connection(self.file_name)


if __name__ == '__main__':


    fname = r'C:\Users\penversa\Git\Python-PLEXOS-API\Input Files\rts3.xml'
    plexos_db = PlexosDatabase(fname)