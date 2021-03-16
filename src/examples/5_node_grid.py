from PlexosAPI import PlexosDatabase

# must have the full path, otherwise it will complain about the folder not existing
file_name = r'C:\Users\penversa\Git\Python-PLEXOS-API\src\examples\my_5_node_grid.xml'

db = PlexosDatabase(file_name=file_name, force_new=True)

db.add_region('R1')

db.add_node('bus1', 'R1')
db.add_node('bus2', 'R1')
db.add_node('bus3', 'R1')
db.add_node('bus4', 'R1')
db.add_node('bus5', 'R1')

db.add_line('bus1', 'bus2', 'L1_2', 100, 0.001, 0.05, 0.002)

db.add_generator('bus1', 'G1', 1, 50, 1.5, 10, 'Gas')
db.add_generator('bus2', 'G2', 1, 20, 1.5, 10, 'Gas')
db.add_generator('bus3', 'G3', 1, 50, 3.0, 10, 'Fuel')


db.close()
print()
