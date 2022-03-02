# standard Python/SciPy libraries
import getpass, os, sys, clr, json

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API/')
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')

# .NET related imports
from PLEXOS_NET.Core import PLEXOSConnect
from System.Data.SqlClient import SqlConnectionStringBuilder
from System import DateTime

def is_run(x, prop, val):
    return eval('x.{} == {}'.format(prop, val))

def is_pass_filters(x, **filters):
    for k,v in filters:
        if not is_run(x, k, v): return False
    return True

class PlexosConnect(PLEXOSConnect):

    cxn_json = os.path.join(os.path.dirname(__file__), 'connect.json')
    cxn_details = json.load(open(cxn_json))[0]
    from_date = DateTime.Today.AddDays(-30)
    to_date = DateTime.Today

    def get_connection_string(self):
        return 'Data Source={server}:{port};User Id={username};Password={password}'.format(**self.cxn_details)

    def is_connected(self):
        try:
            return self.cxn.IsConnectionValid()
        except:
            return False

    def connect(self):
        if self.cxn.is_connected(): return

        # connect to the PLEXOS Connect server
        self.cxn = PLEXOSConnect()
        self.cxn.DisplayAlerts = False
        self.cxn.Connection(self.get_connection_string())

    def download_logs(self, target_folder, *run_id):
        for r in run_id: self.download_log(target_folder, run_id)

    def download_log(self, target_folder, run_id):
        return self.cxn.DownloadLog(target_folder, run_id)

    def get_run_ids(self, **filters):
        return [
                x.Index for x in self.cxn.GetRuns(False, self.from_date, self.to_date)
                if is_pass_filters(x, **filters)
            ]






