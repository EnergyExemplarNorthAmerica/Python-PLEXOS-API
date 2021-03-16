from PlexosAPI.api import plx


class PlexosConnect:

    def __init__(self, server, port, username, password):
        """

        :param server:
        :param port:
        :param username:
        :param password:
        """
        self.server = server
        self.port = port
        self.username = username
        self.password = password

        # connect to the PLEXOS Connect server
        self.cxn = plx.PLEXOSConnect()
        self.cxn.DisplayAlerts = False
        self.cxn.Connection('Data Source={}:{};User Id={};Password={}'.format(self.server,
                                                                              self.port,
                                                                              self.username,
                                                                              self.password))

    def get_job_sets(self):
        """

        :return:
        """
        return [jobset for jobset in self.cxn.GetJobsets()]

    def get_clients(self):
        """

        :return:
        """
        return[client for client in self.cxn.GetClients()]

    def get_accounts(self):
        """

        :return:
        """
        return [acct for acct in self.cxn.GetAccounts()]

    def get_engines(self):
        """

        :return:
        """
        return [engine for engine in self.cxn.GetEngines()]

    def get_data_sets(self):
        """

        :return:
        """
        data = dict()
        folders = [''] + list(self.cxn.GetFolders())

        for folder in folders:

            if folder not in data.keys():
                data[folder] = dict()

            for data_set in list(self.cxn.GetDatasets(folder))[:5]:

                versions = [version for version in list(self.cxn.GetDatasetVersions(folder, data_set))[-4:-1]]

                if data_set not in data[folder].keys():
                    data[folder][data_set] = versions

        return data
