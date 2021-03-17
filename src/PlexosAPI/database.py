import os
import pandas as pd
import clr
from PlexosAPI.api import plx, Enum, run_model, parse_logfile, add_plexos_prop, \
    CollectionEnum, ClassEnum, PeriodEnum, NodeAttributeEnum, SystemNodesEnum, ClassEnumType


class PlexosDatabase:

    def __init__(self, file_name, output_folder='.', model_name='Base', force_new=False):
        """
        Database constructor, it opens or creates a Plexos DataBase
        :param file_name: Plexos .xml file name
        :param output_folder:
        :param model_name:
        """

        # file name
        self.file_name = file_name

        # set the output folder
        if output_folder is None:
            self.output_folder = os.path.dirname(self.file_name)
        else:
            self.output_folder = output_folder

        # the model internal name
        self.model_name = model_name

        # database connection
        self.db = plx.DatabaseCore()

        if not os.path.exists(self.file_name) or force_new:

            # if the file does not exist, create the DB, and do not overwrite
            self.db.NewEmptyDatabase(self.file_name, force_new)

        # connect the database
        self.db.Connection(self.file_name)

    def close(self):
        """
        Close and save the DataBase
        :return:
        """
        self.db.Close()

    def run(self):
        """
        Run model and print the logs while it lasts
        :return: Nothing
        """
        run_model(self.file_name, self.output_folder, self.model_name)
        for res in parse_logfile('ST Schedule Completed', self.output_folder, self.model_name, 25):
            print(res)

    def get_collection_names(self, collection):
        """
        Get list of named of the objects in a collection
        :param collection: value from CollectionEnum
        :return: list of strings
        """
        obj = self.db.GetObjects(collection)
        if obj is not None:
            return [gen for gen in obj]
        else:
            return list()

    def get_record_set(self, collection, child_name_list):
        """
        Get record set for a collection
        :param collection: value from CollectionEnum
        :param child_name_list: lis of object names or simply the object name
        :return: record set
        """

        '''
        Recordset GetPropertiesTable(CollectionEnum CollectionId,
                                     String ParentNameList[ = None],
                                     String ChildNameList[ = None],
                                     String TimesliceList[ = None],
                                     String ScenarioList[ = None],
                                     String CategoryList[ = None])
        '''
        if isinstance(child_name_list, str):
            return self.db.GetPropertiesTable(collection, '', child_name_list)
        elif isinstance(child_name_list, list):
            return self.db.GetPropertiesTable(collection, '', ','.join(child_name_list))
        else:
            raise Exception('Unknown type for child_name_list')

    @staticmethod
    def get_list_of_records_dictionary(record_set: "ADODB.RecordsetClass"):
        """
        Get list of dictionaries with the records' data
        :param record_set: .Net ADODB record set
        :return: list of dictionaries with the properties and values
        """

        data = list()

        # go to the record first value
        record_set.MoveFirst()

        # read the record sequential
        if record_set is not None and not record_set.EOF:
            fileds = [x.Name for x in record_set.Fields]
            while not record_set.EOF:
                values = [x.Value for x in record_set.Fields]
                data.append({f.replace('_x0020', ''): d for f, d in zip(fileds, values)})
                record_set.MoveNext()

        return data

    def get_collection_df(self, collection, pivot_values=False):
        """
        Get the DataFrame with the data of a collection
        :param collection: i.e.: CollectionEnum.SystemGenerators
        :param pivot_values: if true, the table is converted to a DataFrame pivoted around the properties
        :return: DataFrame
        """
        names = self.get_collection_names(collection)

        if len(names) > 0:
            record_set = self.get_record_set(collection, names)

            data = self.get_list_of_records_dictionary(record_set)

            if pivot_values:
                df = pd.DataFrame(data)
                return pd.pivot_table(df, values='Value', index='Child_Object', columns='Property', aggfunc='max')
            else:
                return pd.DataFrame(data)
        else:
            return None

    def add_category(self, child_class_id, category):
        """
        Add the category if it hasn't been added yet
        :param child_class_id:
        :param category:
        :return:
        """
        #
        cats = self.db.GetCategories(child_class_id)
        if len(category) > 0:
            if cats is None or category not in self.db.GetCategories(child_class_id):
                self.db.AddCategory(child_class_id, category)

    def add_object(self, child_class_id, child_name, category='', ):
        """
        Add the object if it hasn't been added yet
        :param child_class_id: value from ClassEnum
        :param child_name: name of the object
        :param category: Category name, it it does not exist, it is created
        """

        # create category if it does not exist
        self.add_category(child_class_id, category)

        #
        objs = self.db.GetObjects(child_class_id)
        if objs is None or child_name not in objs:
            if len(category) > 0:
                self.db.AddObject(child_name, child_class_id, True, category, 'Added from Python')
            else:
                self.db.AddObject(child_name, child_class_id, True, '', 'Added from Python')

    def add_property(self, child_class_id, collection_id, child_name, prop_name, prop_value,
                     parent_class_id=ClassEnum.System, parent_name='System', data_file=None):
        """
        Add property to an existing object
        :param child_class_id: value from ClassEnum
        :param collection_id: value from CollectionEnum
        :param child_name: name of the object
        :param prop_name: name of the property
        :param prop_value: value of the property
        :param parent_class_id: parent class, normally ClassEnum.System
        :param parent_name: name of the parent class, normally 'System'
        :param data_file: Datafile of the property (None if none...)
        """

        '''
        Int32 GetMembershipID(CollectionEnum nCollectionId,
                              String strParent,
                              String strChild)
        '''
        mem_id = self.db.GetMembershipID(collection_id, parent_name, child_name)

        '''
        Int32 PropertyName2EnumId(String strParentClassName,
                                  String strChildClassName,
                                  String strCollectionName,
                                  String strPropertyName )
        '''
        enum_id = self.db.PropertyName2EnumId(Enum.GetName(ClassEnumType, parent_class_id),
                                              Enum.GetName(ClassEnumType, child_class_id),
                                              Enum.GetName(ClassEnumType, child_class_id) + 's',
                                              prop_name)

        '''
        Int32 AddProperty(Int32 MembershipId,
                          Int32 EnumId,
                          Int32 BandId,
                          Double Value,
                          Object DateFrom,
                          Object DateTo,
                          Object Variable,
                          Object DataFile,
                          Object Pattern,
                          Object Scenario,
                          Object Action,
                          PeriodEnum PeriodTypeId)                                               
        '''
        self.db.AddProperty(mem_id, enum_id, 1, prop_value,
                            None, None, None, data_file, None, None,
                            0, PeriodEnum.Interval)

    def add_or_update_attribute(self, class_enum, name, property_enum, value):
        """
        Add or update attribute
        :param class_enum: value from ClassEnum
        :param name: name of the object
        :param property_enum: Value from the corresponding property enumeration
        :param value: value of the attribute
        """
        if not self.db.UpdateAttribute(class_enum, name, property_enum, value):
            # if we cannot update it, add it
            self.db.AddAttribute(class_enum, name, property_enum, value)

    def add_region(self, name):
        """
        Add Region
        :param name: region name
        """
        add_plexos_prop(db=self.db,
                        parent_class_id=ClassEnum.System,
                        child_class_id=ClassEnum.Region,
                        collection_id=CollectionEnum.SystemRegions,
                        parent_name='System',
                        child_name=name,
                        prop_name='Load',
                        prop_value=0)

    def add_node(self, name, region=None, zone=None, V=None, Pload=None, Pgen=None, Pmax=None,
                 lat=None, lon=None, is_slack=False, category='Nodes'):
        """
        Add node to Database
        :param name: Node name
        :param region: Node Region
        :param zone: Node Zone
        :param V: Nominal voltage (kV)
        :param Pload: Fixed load power (MW)
        :param Pgen: Fixed generation power (MW)
        :param Pmax: Maximum injection power (MW)
        :param lat: Latitude (degrees)
        :param lon: Longitude (degrees)
        :param is_slack: Is slack?
        :param category: Node category
        """

        self.add_object(ClassEnum.Node, name, category)

        if V is not None:
            '''
            db, parent_class_id, child_class_id, collection_id,
                    parent_name, child_name, prop_name, prop_value,
                    category=''
            '''
            self.add_property(ClassEnum.Node, CollectionEnum.SystemNodes, name,
                              'Voltage', V, data_file=None)

        if Pload is not None:
            self.add_property(ClassEnum.Node, CollectionEnum.SystemNodes, name,
                              'Fixed Load', Pload, data_file=None)

        if Pgen is not None:
            self.add_property(ClassEnum.Node, CollectionEnum.SystemNodes, name,
                              'Fixed Generation', Pgen, data_file=None)

        if Pmax is not None:
            self.add_property(ClassEnum.Node, CollectionEnum.SystemNodes, name,
                              'Max Net Injection', Pmax, data_file=None)

        if lat is not None:
            self.add_or_update_attribute(ClassEnum.Node, name, NodeAttributeEnum.Latitude, lat)

        if lon is not None:
            self.add_or_update_attribute(ClassEnum.Node, name, NodeAttributeEnum.Longitude, lon)

        if region is not None:
            self.db.AddMembership(CollectionEnum.NodeRegion, name, region)

        if zone is not None:
            self.db.AddMembership(CollectionEnum.NodeZone, name, zone)

    def add_generator(self, node, name, units=1, max_capacity=9999, min_stable_level=0,
                      fuel_price=1, heat_rate=1, category='Thermal'):
        """
        Add Generator to the DataBase
        :param node:
        :param name:
        :param units:
        :param max_capacity:
        :param min_stable_level:
        :param fuel_price:
        :param heat_rate:
        :param category:
        :return:
        """
        self.add_object(ClassEnum.Generator, name, category)

        self.add_property(ClassEnum.Generator, CollectionEnum.SystemGenerators, name,
                          'Units', units, data_file=None)

        self.add_property(ClassEnum.Generator, CollectionEnum.SystemGenerators, name,
                          'Max Capacity', max_capacity, data_file=None)

        self.add_property(ClassEnum.Generator, CollectionEnum.SystemGenerators, name,
                          'Min Stable Level', min_stable_level, data_file=None)

        self.add_property(ClassEnum.Generator, CollectionEnum.SystemGenerators, name,
                          'Fuel Price', fuel_price, data_file=None)

        self.add_property(ClassEnum.Generator, CollectionEnum.SystemGenerators, name,
                          'Heat Rate', heat_rate, data_file=None)

        self.db.AddMembership(CollectionEnum.GeneratorNodes, name, node)

    def add_battery(self, node, name, units=1, capacity=99999, max_power=99999,
                    initial_soc=0.5, charge_efficiency=0.98, category='Storage'):
        """
        Add Battery to the DataBase
        :param node:
        :param name:
        :param units:
        :param capacity:
        :param max_power:
        :param initial_soc:
        :param charge_efficiency:
        :param category:
        :return:
        """
        # add_plexos_prop(self.db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries,
        #                 'System', name, 'Units', units, category)

        # add_plexos_prop(self.db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries,
        #                 'System', name, 'Charge Efficiency', charge_efficiency)

        add_plexos_prop(self.db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries,
                        'System', name, 'Capacity', capacity)

        add_plexos_prop(self.db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries,
                        'System', name, 'Max Power', max_power)

        add_plexos_prop(self.db, ClassEnum.System, ClassEnum.Battery, CollectionEnum.SystemBatteries,
                        'System', name, 'Initial SoC', initial_soc)

        self.db.AddMembership(CollectionEnum.BatteryNode, name, node)

    def add_line(self, node_from, node_to, name, r, x, b, max_flow=99999, min_flow=-99999,
                 overload_min_rating=None, overload_max_rating=None, category=''):
        """
        Add line to the Database
        :param node_from: name of the node from
        :param node_to: name of the node to
        :param name: name of the line
        :param r: Resistence (p.u.)
        :param x: Reactance (p.u.)
        :param b: Susceptance (p.u.)
        :param max_flow: Maximum allowed flow (MW)
        :param min_flow: Minimum allowed flow  (MW) (may be negative)
        :param overload_max_rating: Maximum contingency flow  (MW)
        :param overload_min_rating: Minimum contingency flow  (MW) (may be negative)
        :param category: line category
        """

        self.add_object(ClassEnum.Line, name, category)

        self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                          'Resistance', r, data_file=None)

        self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                          'Reactance', x, data_file=None)

        self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                          'Susceptance', b, data_file=None)

        self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                          'Max Flow', max_flow, data_file=None)

        self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                          'Min Flow', min_flow, data_file=None)

        if overload_max_rating is not None:
            self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                              'Overload Max Rating', overload_max_rating, data_file=None)

        if overload_min_rating is not None:
            self.add_property(ClassEnum.Line, CollectionEnum.SystemLines, name,
                              'Overload Min Rating', overload_min_rating, data_file=None)

        self.db.AddMembership(CollectionEnum.LineNodeFrom, name, node_from)
        self.db.AddMembership(CollectionEnum.LineNodeTo, name, node_to)

    def add_transformer(self, node_from, node_to, name, rate, r, x, b, category=''):
        """
        Add transformer to the Database
        :param node_from: name of the node from
        :param node_to: name of the node to
        :param name: name of the line
        :param rate: Rating (MW)
        :param r: Resistence (p.u.)
        :param x: Reactance (p.u.)
        :param b: Susceptance (p.u.)
        :param category: Category of the transformer
        :return:
        """
        self.add_object(ClassEnum.Transformer, name, category)

        self.add_property(ClassEnum.Transformer, CollectionEnum.SystemTransformers, name,
                          'Resistance', r, data_file=None)

        self.add_property(ClassEnum.Transformer, CollectionEnum.SystemTransformers, name,
                          'Reactance', x, data_file=None)

        self.add_property(ClassEnum.Transformer, CollectionEnum.SystemTransformers, name,
                          'Susceptance', b, data_file=None)

        self.add_property(ClassEnum.Transformer, CollectionEnum.SystemTransformers, name,
                          'Rating', rate, data_file=None)

        self.db.AddMembership(CollectionEnum.TransformerNodeFrom, name, node_from)
        self.db.AddMembership(CollectionEnum.TransformerNodeTo, name, node_to)

    def get_system_generators_df(self, pivot_values=False):
        """
        Get table of SystemGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGenerators, pivot_values)

    def get_system_fuels_df(self, pivot_values=False):
        """
        Get table of SystemFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemFuels, pivot_values)

    def get_system_fuel_contracts_df(self, pivot_values=False):
        """
        Get table of SystemFuelContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemFuelContracts, pivot_values)

    def get_system_emissions_df(self, pivot_values=False):
        """
        Get table of SystemEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemEmissions, pivot_values)

    def get_system_abatements_df(self, pivot_values=False):
        """
        Get table of SystemAbatements records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemAbatements, pivot_values)

    def get_system_storages_df(self, pivot_values=False):
        """
        Get table of SystemStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemStorages, pivot_values)

    def get_system_waterways_df(self, pivot_values=False):
        """
        Get table of SystemWaterways records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterways, pivot_values)

    def get_system_power_stations_df(self, pivot_values=False):
        """
        Get table of SystemPowerStations records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemPowerStations, pivot_values)

    def get_system_physical_contracts_df(self, pivot_values=False):
        """
        Get table of SystemPhysicalContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemPhysicalContracts, pivot_values)

    def get_system_purchasers_df(self, pivot_values=False):
        """
        Get table of SystemPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemPurchasers, pivot_values)

    def get_system_reserves_df(self, pivot_values=False):
        """
        Get table of SystemReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemReserves, pivot_values)

    def get_system_batteries_df(self, pivot_values=False):
        """
        Get table of SystemBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemBatteries, pivot_values)

    def get_system_maintenances_df(self, pivot_values=False):
        """
        Get table of SystemMaintenances records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemMaintenances, pivot_values)

    def get_system_heat_plants_df(self, pivot_values=False):
        """
        Get table of SystemHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemHeatPlants, pivot_values)

    def get_system_heat_nodes_df(self, pivot_values=False):
        """
        Get table of SystemHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemHeatNodes, pivot_values)

    def get_system_gas_fields_df(self, pivot_values=False):
        """
        Get table of SystemGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasFields, pivot_values)

    def get_system_gas_plants_df(self, pivot_values=False):
        """
        Get table of SystemGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasPlants, pivot_values)

    def get_system_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of SystemGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasPipelines, pivot_values)

    def get_system_gas_nodes_df(self, pivot_values=False):
        """
        Get table of SystemGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasNodes, pivot_values)

    def get_system_gas_storages_df(self, pivot_values=False):
        """
        Get table of SystemGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasStorages, pivot_values)

    def get_system_gas_demands_df(self, pivot_values=False):
        """
        Get table of SystemGasDemands records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasDemands, pivot_values)

    def get_system_gas_basins_df(self, pivot_values=False):
        """
        Get table of SystemGasBasins records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasBasins, pivot_values)

    def get_system_gas_zones_df(self, pivot_values=False):
        """
        Get table of SystemGasZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasZones, pivot_values)

    def get_system_gas_contracts_df(self, pivot_values=False):
        """
        Get table of SystemGasContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasContracts, pivot_values)

    def get_system_gas_transports_df(self, pivot_values=False):
        """
        Get table of SystemGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGasTransports, pivot_values)

    def get_system_water_plants_df(self, pivot_values=False):
        """
        Get table of SystemWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterPlants, pivot_values)

    def get_system_water_pipelines_df(self, pivot_values=False):
        """
        Get table of SystemWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterPipelines, pivot_values)

    def get_system_water_nodes_df(self, pivot_values=False):
        """
        Get table of SystemWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterNodes, pivot_values)

    def get_system_water_storages_df(self, pivot_values=False):
        """
        Get table of SystemWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterStorages, pivot_values)

    def get_system_water_demands_df(self, pivot_values=False):
        """
        Get table of SystemWaterDemands records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterDemands, pivot_values)

    def get_system_water_zones_df(self, pivot_values=False):
        """
        Get table of SystemWaterZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemWaterZones, pivot_values)

    def get_system_regions_df(self, pivot_values=False):
        """
        Get table of SystemRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemRegions, pivot_values)

    def get_system_zones_df(self, pivot_values=False):
        """
        Get table of SystemZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemZones, pivot_values)

    def get_system_nodes_df(self, pivot_values=False):
        """
        Get table of SystemNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemNodes, pivot_values)

    def get_system_lines_df(self, pivot_values=False):
        """
        Get table of SystemLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemLines, pivot_values)

    def get_system_ml_fs_df(self, pivot_values=False):
        """
        Get table of SystemMLFs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemMLFs, pivot_values)

    def get_system_transformers_df(self, pivot_values=False):
        """
        Get table of SystemTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemTransformers, pivot_values)

    def get_system_flow_controls_df(self, pivot_values=False):
        """
        Get table of SystemFlowControls records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemFlowControls, pivot_values)

    def get_system_interfaces_df(self, pivot_values=False):
        """
        Get table of SystemInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemInterfaces, pivot_values)

    def get_system_contingencies_df(self, pivot_values=False):
        """
        Get table of SystemContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemContingencies, pivot_values)

    def get_system_companies_df(self, pivot_values=False):
        """
        Get table of SystemCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemCompanies, pivot_values)

    def get_system_financial_contracts_df(self, pivot_values=False):
        """
        Get table of SystemFinancialContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemFinancialContracts, pivot_values)

    def get_system_hubs_df(self, pivot_values=False):
        """
        Get table of SystemHubs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemHubs, pivot_values)

    def get_system_transmission_rights_df(self, pivot_values=False):
        """
        Get table of SystemTransmissionRights records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemTransmissionRights, pivot_values)

    def get_system_cournots_df(self, pivot_values=False):
        """
        Get table of SystemCournots records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemCournots, pivot_values)

    def get_system_rs_is_df(self, pivot_values=False):
        """
        Get table of SystemRSIs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemRSIs, pivot_values)

    def get_system_markets_df(self, pivot_values=False):
        """
        Get table of SystemMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemMarkets, pivot_values)

    def get_system_constraints_df(self, pivot_values=False):
        """
        Get table of SystemConstraints records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemConstraints, pivot_values)

    def get_system_decision_variables_df(self, pivot_values=False):
        """
        Get table of SystemDecisionVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemDecisionVariables, pivot_values)

    def get_system_lists_df(self, pivot_values=False):
        """
        Get table of SystemLists records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemLists, pivot_values)

    def get_system_data_files_df(self, pivot_values=False):
        """
        Get table of SystemDataFiles records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemDataFiles, pivot_values)

    def get_system_variables_df(self, pivot_values=False):
        """
        Get table of SystemVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemVariables, pivot_values)

    def get_system_timeslices_df(self, pivot_values=False):
        """
        Get table of SystemTimeslices records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemTimeslices, pivot_values)

    def get_system_globals_df(self, pivot_values=False):
        """
        Get table of SystemGlobals records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemGlobals, pivot_values)

    def get_system_scenarios_df(self, pivot_values=False):
        """
        Get table of SystemScenarios records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemScenarios, pivot_values)

    def get_system_models_df(self, pivot_values=False):
        """
        Get table of SystemModels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemModels, pivot_values)

    def get_system_projects_df(self, pivot_values=False):
        """
        Get table of SystemProjects records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemProjects, pivot_values)

    def get_system_horizons_df(self, pivot_values=False):
        """
        Get table of SystemHorizons records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemHorizons, pivot_values)

    def get_system_reports_df(self, pivot_values=False):
        """
        Get table of SystemReports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemReports, pivot_values)

    def get_system_lt_plan_df(self, pivot_values=False):
        """
        Get table of SystemLTPlan records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemLTPlan, pivot_values)

    def get_system_pasa_df(self, pivot_values=False):
        """
        Get table of SystemPASA records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemPASA, pivot_values)

    def get_system_mt_schedule_df(self, pivot_values=False):
        """
        Get table of SystemMTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemMTSchedule, pivot_values)

    def get_system_st_schedule_df(self, pivot_values=False):
        """
        Get table of SystemSTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemSTSchedule, pivot_values)

    def get_system_transmission_df(self, pivot_values=False):
        """
        Get table of SystemTransmission records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemTransmission, pivot_values)

    def get_system_production_df(self, pivot_values=False):
        """
        Get table of SystemProduction records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemProduction, pivot_values)

    def get_system_competition_df(self, pivot_values=False):
        """
        Get table of SystemCompetition records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemCompetition, pivot_values)

    def get_system_stochastic_df(self, pivot_values=False):
        """
        Get table of SystemStochastic records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemStochastic, pivot_values)

    def get_system_performance_df(self, pivot_values=False):
        """
        Get table of SystemPerformance records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemPerformance, pivot_values)

    def get_system_diagnostics_df(self, pivot_values=False):
        """
        Get table of SystemDiagnostics records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.SystemDiagnostics, pivot_values)

    def get_generator_template_df(self, pivot_values=False):
        """
        Get table of GeneratorTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorTemplate, pivot_values)

    def get_fuel_template_df(self, pivot_values=False):
        """
        Get table of FuelTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelTemplate, pivot_values)

    def get_fuel_contract_template_df(self, pivot_values=False):
        """
        Get table of FuelContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelContractTemplate, pivot_values)

    def get_emission_template_df(self, pivot_values=False):
        """
        Get table of EmissionTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.EmissionTemplate, pivot_values)

    def get_abatement_template_df(self, pivot_values=False):
        """
        Get table of AbatementTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.AbatementTemplate, pivot_values)

    def get_storage_template_df(self, pivot_values=False):
        """
        Get table of StorageTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.StorageTemplate, pivot_values)

    def get_waterway_template_df(self, pivot_values=False):
        """
        Get table of WaterwayTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterwayTemplate, pivot_values)

    def get_power_station_template_df(self, pivot_values=False):
        """
        Get table of PowerStationTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PowerStationTemplate, pivot_values)

    def get_physical_contract_template_df(self, pivot_values=False):
        """
        Get table of PhysicalContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PhysicalContractTemplate, pivot_values)

    def get_purchaser_template_df(self, pivot_values=False):
        """
        Get table of PurchaserTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PurchaserTemplate, pivot_values)

    def get_reserve_template_df(self, pivot_values=False):
        """
        Get table of ReserveTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveTemplate, pivot_values)

    def get_battery_template_df(self, pivot_values=False):
        """
        Get table of BatteryTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.BatteryTemplate, pivot_values)

    def get_maintenance_template_df(self, pivot_values=False):
        """
        Get table of MaintenanceTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MaintenanceTemplate, pivot_values)

    def get_heat_plant_template_df(self, pivot_values=False):
        """
        Get table of HeatPlantTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatPlantTemplate, pivot_values)

    def get_heat_node_template_df(self, pivot_values=False):
        """
        Get table of HeatNodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatNodeTemplate, pivot_values)

    def get_gas_field_template_df(self, pivot_values=False):
        """
        Get table of GasFieldTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasFieldTemplate, pivot_values)

    def get_gas_plant_template_df(self, pivot_values=False):
        """
        Get table of GasPlantTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPlantTemplate, pivot_values)

    def get_gas_pipeline_template_df(self, pivot_values=False):
        """
        Get table of GasPipelineTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPipelineTemplate, pivot_values)

    def get_gas_node_template_df(self, pivot_values=False):
        """
        Get table of GasNodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasNodeTemplate, pivot_values)

    def get_gas_storage_template_df(self, pivot_values=False):
        """
        Get table of GasStorageTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasStorageTemplate, pivot_values)

    def get_gas_demand_template_df(self, pivot_values=False):
        """
        Get table of GasDemandTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasDemandTemplate, pivot_values)

    def get_gas_basin_template_df(self, pivot_values=False):
        """
        Get table of GasBasinTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasBasinTemplate, pivot_values)

    def get_gas_zone_template_df(self, pivot_values=False):
        """
        Get table of GasZoneTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneTemplate, pivot_values)

    def get_gas_contract_template_df(self, pivot_values=False):
        """
        Get table of GasContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasContractTemplate, pivot_values)

    def get_water_plant_template_df(self, pivot_values=False):
        """
        Get table of WaterPlantTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPlantTemplate, pivot_values)

    def get_water_pipeline_template_df(self, pivot_values=False):
        """
        Get table of WaterPipelineTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPipelineTemplate, pivot_values)

    def get_water_node_template_df(self, pivot_values=False):
        """
        Get table of WaterNodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterNodeTemplate, pivot_values)

    def get_water_storage_template_df(self, pivot_values=False):
        """
        Get table of WaterStorageTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterStorageTemplate, pivot_values)

    def get_water_demand_template_df(self, pivot_values=False):
        """
        Get table of WaterDemandTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterDemandTemplate, pivot_values)

    def get_water_zone_template_df(self, pivot_values=False):
        """
        Get table of WaterZoneTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneTemplate, pivot_values)

    def get_region_template_df(self, pivot_values=False):
        """
        Get table of RegionTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionTemplate, pivot_values)

    def get_zone_template_df(self, pivot_values=False):
        """
        Get table of ZoneTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneTemplate, pivot_values)

    def get_node_template_df(self, pivot_values=False):
        """
        Get table of NodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.NodeTemplate, pivot_values)

    def get_line_template_df(self, pivot_values=False):
        """
        Get table of LineTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.LineTemplate, pivot_values)

    def get_mlf_template_df(self, pivot_values=False):
        """
        Get table of MLFTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MLFTemplate, pivot_values)

    def get_transformer_template_df(self, pivot_values=False):
        """
        Get table of TransformerTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransformerTemplate, pivot_values)

    def get_flow_control_template_df(self, pivot_values=False):
        """
        Get table of FlowControlTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FlowControlTemplate, pivot_values)

    def get_interface_template_df(self, pivot_values=False):
        """
        Get table of InterfaceTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.InterfaceTemplate, pivot_values)

    def get_contingency_template_df(self, pivot_values=False):
        """
        Get table of ContingencyTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyTemplate, pivot_values)

    def get_company_template_df(self, pivot_values=False):
        """
        Get table of CompanyTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CompanyTemplate, pivot_values)

    def get_financial_contract_template_df(self, pivot_values=False):
        """
        Get table of FinancialContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractTemplate, pivot_values)

    def get_hub_template_df(self, pivot_values=False):
        """
        Get table of HubTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HubTemplate, pivot_values)

    def get_transmission_right_template_df(self, pivot_values=False):
        """
        Get table of TransmissionRightTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightTemplate, pivot_values)

    def get_cournot_template_df(self, pivot_values=False):
        """
        Get table of CournotTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CournotTemplate, pivot_values)

    def get_rsi_template_df(self, pivot_values=False):
        """
        Get table of RSITemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RSITemplate, pivot_values)

    def get_market_template_df(self, pivot_values=False):
        """
        Get table of MarketTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketTemplate, pivot_values)

    def get_constraint_template_df(self, pivot_values=False):
        """
        Get table of ConstraintTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintTemplate, pivot_values)

    def get_decision_variable_template_df(self, pivot_values=False):
        """
        Get table of DecisionVariableTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.DecisionVariableTemplate, pivot_values)

    def get_generator_heat_input_df(self, pivot_values=False):
        """
        Get table of GeneratorHeatInput records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorHeatInput, pivot_values)

    def get_generator_transition_df(self, pivot_values=False):
        """
        Get table of GeneratorTransition records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorTransition, pivot_values)

    def get_generator_fuels_df(self, pivot_values=False):
        """
        Get table of GeneratorFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorFuels, pivot_values)

    def get_generator_start_fuels_df(self, pivot_values=False):
        """
        Get table of GeneratorStartFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorStartFuels, pivot_values)

    def get_generator_head_storage_df(self, pivot_values=False):
        """
        Get table of GeneratorHeadStorage records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorHeadStorage, pivot_values)

    def get_generator_tail_storage_df(self, pivot_values=False):
        """
        Get table of GeneratorTailStorage records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorTailStorage, pivot_values)

    def get_generator_power_station_df(self, pivot_values=False):
        """
        Get table of GeneratorPowerStation records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorPowerStation, pivot_values)

    def get_generator_markto_markets_df(self, pivot_values=False):
        """
        Get table of GeneratorMarktoMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorMarktoMarkets, pivot_values)

    def get_generator_gas_node_df(self, pivot_values=False):
        """
        Get table of GeneratorGasNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorGasNode, pivot_values)

    def get_generator_water_node_df(self, pivot_values=False):
        """
        Get table of GeneratorWaterNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorWaterNode, pivot_values)

    def get_generator_nodes_df(self, pivot_values=False):
        """
        Get table of GeneratorNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorNodes, pivot_values)

    def get_generator_nodes_star__df(self, pivot_values=False):
        """
        Get table of GeneratorNodes_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorNodes_star_, pivot_values)

    def get_generator_companies_df(self, pivot_values=False):
        """
        Get table of GeneratorCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorCompanies, pivot_values)

    def get_fuel_gas_nodes_df(self, pivot_values=False):
        """
        Get table of FuelGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelGasNodes, pivot_values)

    def get_fuel_companies_df(self, pivot_values=False):
        """
        Get table of FuelCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelCompanies, pivot_values)

    def get_fuel_contract_generators_df(self, pivot_values=False):
        """
        Get table of FuelContractGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelContractGenerators, pivot_values)

    def get_fuel_contract_fuel_df(self, pivot_values=False):
        """
        Get table of FuelContractFuel records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelContractFuel, pivot_values)

    def get_fuel_contract_companies_df(self, pivot_values=False):
        """
        Get table of FuelContractCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelContractCompanies, pivot_values)

    def get_fuel_contract_constraints_df(self, pivot_values=False):
        """
        Get table of FuelContractConstraints records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FuelContractConstraints, pivot_values)

    def get_emission_generators_df(self, pivot_values=False):
        """
        Get table of EmissionGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.EmissionGenerators, pivot_values)

    def get_emission_fuels_df(self, pivot_values=False):
        """
        Get table of EmissionFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.EmissionFuels, pivot_values)

    def get_emission_gas_nodes_df(self, pivot_values=False):
        """
        Get table of EmissionGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.EmissionGasNodes, pivot_values)

    def get_emission_gas_plants_df(self, pivot_values=False):
        """
        Get table of EmissionGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.EmissionGasPlants, pivot_values)

    def get_emission_water_plants_df(self, pivot_values=False):
        """
        Get table of EmissionWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.EmissionWaterPlants, pivot_values)

    def get_abatement_generators_df(self, pivot_values=False):
        """
        Get table of AbatementGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.AbatementGenerators, pivot_values)

    def get_abatement_emissions_df(self, pivot_values=False):
        """
        Get table of AbatementEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.AbatementEmissions, pivot_values)

    def get_abatement_consumables_df(self, pivot_values=False):
        """
        Get table of AbatementConsumables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.AbatementConsumables, pivot_values)

    def get_storage_water_nodes_df(self, pivot_values=False):
        """
        Get table of StorageWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.StorageWaterNodes, pivot_values)

    def get_waterway_storage_from_df(self, pivot_values=False):
        """
        Get table of WaterwayStorageFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterwayStorageFrom, pivot_values)

    def get_waterway_storage_to_df(self, pivot_values=False):
        """
        Get table of WaterwayStorageTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterwayStorageTo, pivot_values)

    def get_power_station_nodes_df(self, pivot_values=False):
        """
        Get table of PowerStationNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PowerStationNodes, pivot_values)

    def get_physical_contract_generation_node_df(self, pivot_values=False):
        """
        Get table of PhysicalContractGenerationNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PhysicalContractGenerationNode, pivot_values)

    def get_physical_contract_load_node_df(self, pivot_values=False):
        """
        Get table of PhysicalContractLoadNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PhysicalContractLoadNode, pivot_values)

    def get_physical_contract_companies_df(self, pivot_values=False):
        """
        Get table of PhysicalContractCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PhysicalContractCompanies, pivot_values)

    def get_purchaser_nodes_df(self, pivot_values=False):
        """
        Get table of PurchaserNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PurchaserNodes, pivot_values)

    def get_purchaser_nodes_star__df(self, pivot_values=False):
        """
        Get table of PurchaserNodes_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PurchaserNodes_star_, pivot_values)

    def get_purchaser_companies_df(self, pivot_values=False):
        """
        Get table of PurchaserCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.PurchaserCompanies, pivot_values)

    def get_reserve_generators_df(self, pivot_values=False):
        """
        Get table of ReserveGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveGenerators, pivot_values)

    def get_reserve_purchasers_df(self, pivot_values=False):
        """
        Get table of ReservePurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReservePurchasers, pivot_values)

    def get_reserve_generator_contingencies_df(self, pivot_values=False):
        """
        Get table of ReserveGeneratorContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveGeneratorContingencies, pivot_values)

    def get_reserve_generator_cost_allocation_df(self, pivot_values=False):
        """
        Get table of ReserveGeneratorCostAllocation records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveGeneratorCostAllocation, pivot_values)

    def get_reserve_batteries_df(self, pivot_values=False):
        """
        Get table of ReserveBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveBatteries, pivot_values)

    def get_reserve_nested_reserves_df(self, pivot_values=False):
        """
        Get table of ReserveNestedReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveNestedReserves, pivot_values)

    def get_reserve_regions_df(self, pivot_values=False):
        """
        Get table of ReserveRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveRegions, pivot_values)

    def get_reserve_line_contingencies_df(self, pivot_values=False):
        """
        Get table of ReserveLineContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReserveLineContingencies, pivot_values)

    def get_battery_node_df(self, pivot_values=False):
        """
        Get table of BatteryNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.BatteryNode, pivot_values)

    def get_battery_nodes_star__df(self, pivot_values=False):
        """
        Get table of BatteryNodes_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.BatteryNodes_star_, pivot_values)

    def get_battery_companies_df(self, pivot_values=False):
        """
        Get table of BatteryCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.BatteryCompanies, pivot_values)

    def get_maintenance_generators_df(self, pivot_values=False):
        """
        Get table of MaintenanceGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MaintenanceGenerators, pivot_values)

    def get_maintenance_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of MaintenanceGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MaintenanceGasPipelines, pivot_values)

    def get_maintenance_lines_df(self, pivot_values=False):
        """
        Get table of MaintenanceLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MaintenanceLines, pivot_values)

    def get_maintenance_prerequisites_df(self, pivot_values=False):
        """
        Get table of MaintenancePrerequisites records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MaintenancePrerequisites, pivot_values)

    def get_generator_heat_input_nodes_df(self, pivot_values=False):
        """
        Get table of GeneratorHeatInputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorHeatInputNodes, pivot_values)

    def get_generator_heat_output_nodes_df(self, pivot_values=False):
        """
        Get table of GeneratorHeatOutputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GeneratorHeatOutputNodes, pivot_values)

    def get_heat_plant_fuels_df(self, pivot_values=False):
        """
        Get table of HeatPlantFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatPlantFuels, pivot_values)

    def get_heat_plant_nodes_df(self, pivot_values=False):
        """
        Get table of HeatPlantNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatPlantNodes, pivot_values)

    def get_heat_plant_heat_input_nodes_df(self, pivot_values=False):
        """
        Get table of HeatPlantHeatInputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatPlantHeatInputNodes, pivot_values)

    def get_heat_plant_heat_output_nodes_df(self, pivot_values=False):
        """
        Get table of HeatPlantHeatOutputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatPlantHeatOutputNodes, pivot_values)

    def get_heat_plant_start_fuels_df(self, pivot_values=False):
        """
        Get table of HeatPlantStartFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatPlantStartFuels, pivot_values)

    def get_heat_node_heat_export_nodes_df(self, pivot_values=False):
        """
        Get table of HeatNodeHeatExportNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatNodeHeatExportNodes, pivot_values)

    def get_heat_node_water_plants_df(self, pivot_values=False):
        """
        Get table of HeatNodeWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.HeatNodeWaterPlants, pivot_values)

    def get_gas_field_companies_df(self, pivot_values=False):
        """
        Get table of GasFieldCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasFieldCompanies, pivot_values)

    def get_gas_field_gas_node_df(self, pivot_values=False):
        """
        Get table of GasFieldGasNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasFieldGasNode, pivot_values)

    def get_gas_field_gas_basin_df(self, pivot_values=False):
        """
        Get table of GasFieldGasBasin records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasFieldGasBasin, pivot_values)

    def get_gas_plant_input_node_df(self, pivot_values=False):
        """
        Get table of GasPlantInputNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPlantInputNode, pivot_values)

    def get_gas_plant_output_node_df(self, pivot_values=False):
        """
        Get table of GasPlantOutputNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPlantOutputNode, pivot_values)

    def get_gas_plant_node_df(self, pivot_values=False):
        """
        Get table of GasPlantNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPlantNode, pivot_values)

    def get_gas_pipeline_gas_node_from_df(self, pivot_values=False):
        """
        Get table of GasPipelineGasNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPipelineGasNodeFrom, pivot_values)

    def get_gas_pipeline_gas_node_to_df(self, pivot_values=False):
        """
        Get table of GasPipelineGasNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasPipelineGasNodeTo, pivot_values)

    def get_gas_node_gas_zones_df(self, pivot_values=False):
        """
        Get table of GasNodeGasZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasNodeGasZones, pivot_values)

    def get_gas_storage_gas_node_df(self, pivot_values=False):
        """
        Get table of GasStorageGasNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasStorageGasNode, pivot_values)

    def get_gas_demand_gas_nodes_df(self, pivot_values=False):
        """
        Get table of GasDemandGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasDemandGasNodes, pivot_values)

    def get_gas_demand_companies_df(self, pivot_values=False):
        """
        Get table of GasDemandCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasDemandCompanies, pivot_values)

    def get_gas_zone_generators_df(self, pivot_values=False):
        """
        Get table of GasZoneGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneGenerators, pivot_values)

    def get_gas_zone_gas_fields_df(self, pivot_values=False):
        """
        Get table of GasZoneGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneGasFields, pivot_values)

    def get_gas_zone_gas_plants_df(self, pivot_values=False):
        """
        Get table of GasZoneGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneGasPlants, pivot_values)

    def get_gas_zone_exporting_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of GasZoneExportingGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneExportingGasPipelines, pivot_values)

    def get_gas_zone_importing_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of GasZoneImportingGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneImportingGasPipelines, pivot_values)

    def get_gas_zone_interzonal_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of GasZoneInterzonalGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneInterzonalGasPipelines, pivot_values)

    def get_gas_zone_intrazonal_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of GasZoneIntrazonalGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneIntrazonalGasPipelines, pivot_values)

    def get_gas_zone_gas_storages_df(self, pivot_values=False):
        """
        Get table of GasZoneGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneGasStorages, pivot_values)

    def get_gas_zone_gas_demands_df(self, pivot_values=False):
        """
        Get table of GasZoneGasDemands records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneGasDemands, pivot_values)

    def get_gas_zone_exporting_gas_transports_df(self, pivot_values=False):
        """
        Get table of GasZoneExportingGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneExportingGasTransports, pivot_values)

    def get_gas_zone_importing_gas_transports_df(self, pivot_values=False):
        """
        Get table of GasZoneImportingGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneImportingGasTransports, pivot_values)

    def get_gas_zone_interzonal_gas_transports_df(self, pivot_values=False):
        """
        Get table of GasZoneInterzonalGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneInterzonalGasTransports, pivot_values)

    def get_gas_zone_intrazonal_gas_transports_df(self, pivot_values=False):
        """
        Get table of GasZoneIntrazonalGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasZoneIntrazonalGasTransports, pivot_values)

    def get_gas_contract_gas_fields_df(self, pivot_values=False):
        """
        Get table of GasContractGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasContractGasFields, pivot_values)

    def get_gas_contract_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of GasContractGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasContractGasPipelines, pivot_values)

    def get_gas_contract_gas_transports_df(self, pivot_values=False):
        """
        Get table of GasContractGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasContractGasTransports, pivot_values)

    def get_gas_transport_export_node_df(self, pivot_values=False):
        """
        Get table of GasTransportExportNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasTransportExportNode, pivot_values)

    def get_gas_transport_import_node_df(self, pivot_values=False):
        """
        Get table of GasTransportImportNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GasTransportImportNode, pivot_values)

    def get_water_plant_input_node_df(self, pivot_values=False):
        """
        Get table of WaterPlantInputNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPlantInputNode, pivot_values)

    def get_water_plant_output_node_df(self, pivot_values=False):
        """
        Get table of WaterPlantOutputNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPlantOutputNode, pivot_values)

    def get_water_plant_node_df(self, pivot_values=False):
        """
        Get table of WaterPlantNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPlantNode, pivot_values)

    def get_water_pipeline_water_node_from_df(self, pivot_values=False):
        """
        Get table of WaterPipelineWaterNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPipelineWaterNodeFrom, pivot_values)

    def get_water_pipeline_water_node_to_df(self, pivot_values=False):
        """
        Get table of WaterPipelineWaterNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterPipelineWaterNodeTo, pivot_values)

    def get_water_node_water_zones_df(self, pivot_values=False):
        """
        Get table of WaterNodeWaterZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterNodeWaterZones, pivot_values)

    def get_water_node_node_df(self, pivot_values=False):
        """
        Get table of WaterNodeNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterNodeNode, pivot_values)

    def get_water_storage_water_node_df(self, pivot_values=False):
        """
        Get table of WaterStorageWaterNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterStorageWaterNode, pivot_values)

    def get_water_demand_water_nodes_df(self, pivot_values=False):
        """
        Get table of WaterDemandWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterDemandWaterNodes, pivot_values)

    def get_water_zone_water_plants_df(self, pivot_values=False):
        """
        Get table of WaterZoneWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneWaterPlants, pivot_values)

    def get_water_zone_water_storages_df(self, pivot_values=False):
        """
        Get table of WaterZoneWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneWaterStorages, pivot_values)

    def get_water_zone_exporting_water_pipelines_df(self, pivot_values=False):
        """
        Get table of WaterZoneExportingWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneExportingWaterPipelines, pivot_values)

    def get_water_zone_importing_water_pipelines_df(self, pivot_values=False):
        """
        Get table of WaterZoneImportingWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneImportingWaterPipelines, pivot_values)

    def get_water_zone_interzonal_water_pipelines_df(self, pivot_values=False):
        """
        Get table of WaterZoneInterzonalWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneInterzonalWaterPipelines, pivot_values)

    def get_water_zone_intrazonal_water_pipelines_df(self, pivot_values=False):
        """
        Get table of WaterZoneIntrazonalWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneIntrazonalWaterPipelines, pivot_values)

    def get_water_zone_water_demands_df(self, pivot_values=False):
        """
        Get table of WaterZoneWaterDemands records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.WaterZoneWaterDemands, pivot_values)

    def get_region_generators_df(self, pivot_values=False):
        """
        Get table of RegionGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionGenerators, pivot_values)

    def get_region_emissions_df(self, pivot_values=False):
        """
        Get table of RegionEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionEmissions, pivot_values)

    def get_region_generation_contracts_df(self, pivot_values=False):
        """
        Get table of RegionGenerationContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionGenerationContracts, pivot_values)

    def get_region_load_contracts_df(self, pivot_values=False):
        """
        Get table of RegionLoadContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionLoadContracts, pivot_values)

    def get_region_purchasers_df(self, pivot_values=False):
        """
        Get table of RegionPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionPurchasers, pivot_values)

    def get_region_markets_df(self, pivot_values=False):
        """
        Get table of RegionMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionMarkets, pivot_values)

    def get_region_batteries_df(self, pivot_values=False):
        """
        Get table of RegionBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionBatteries, pivot_values)

    def get_region_regions_df(self, pivot_values=False):
        """
        Get table of RegionRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionRegions, pivot_values)

    def get_region_reference_node_df(self, pivot_values=False):
        """
        Get table of RegionReferenceNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionReferenceNode, pivot_values)

    def get_region_exporting_lines_df(self, pivot_values=False):
        """
        Get table of RegionExportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionExportingLines, pivot_values)

    def get_region_importing_lines_df(self, pivot_values=False):
        """
        Get table of RegionImportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionImportingLines, pivot_values)

    def get_region_interregional_lines_df(self, pivot_values=False):
        """
        Get table of RegionInterregionalLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionInterregionalLines, pivot_values)

    def get_region_intraregional_lines_df(self, pivot_values=False):
        """
        Get table of RegionIntraregionalLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionIntraregionalLines, pivot_values)

    def get_region_exporting_transformers_df(self, pivot_values=False):
        """
        Get table of RegionExportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionExportingTransformers, pivot_values)

    def get_region_importing_transformers_df(self, pivot_values=False):
        """
        Get table of RegionImportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionImportingTransformers, pivot_values)

    def get_region_interregional_transformers_df(self, pivot_values=False):
        """
        Get table of RegionInterregionalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionInterregionalTransformers, pivot_values)

    def get_region_intraregional_transformers_df(self, pivot_values=False):
        """
        Get table of RegionIntraregionalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionIntraregionalTransformers, pivot_values)

    def get_region_utilities_df(self, pivot_values=False):
        """
        Get table of RegionUtilities records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RegionUtilities, pivot_values)

    def get_zone_capacity_generators_df(self, pivot_values=False):
        """
        Get table of ZoneCapacityGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneCapacityGenerators, pivot_values)

    def get_zone_generators_df(self, pivot_values=False):
        """
        Get table of ZoneGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneGenerators, pivot_values)

    def get_zone_emissions_df(self, pivot_values=False):
        """
        Get table of ZoneEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneEmissions, pivot_values)

    def get_zone_capacity_generation_contracts_df(self, pivot_values=False):
        """
        Get table of ZoneCapacityGenerationContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneCapacityGenerationContracts, pivot_values)

    def get_zone_capacity_load_contracts_df(self, pivot_values=False):
        """
        Get table of ZoneCapacityLoadContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneCapacityLoadContracts, pivot_values)

    def get_zone_generation_contracts_df(self, pivot_values=False):
        """
        Get table of ZoneGenerationContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneGenerationContracts, pivot_values)

    def get_zone_load_contracts_df(self, pivot_values=False):
        """
        Get table of ZoneLoadContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneLoadContracts, pivot_values)

    def get_zone_capacity_purchasers_df(self, pivot_values=False):
        """
        Get table of ZoneCapacityPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneCapacityPurchasers, pivot_values)

    def get_zone_purchasers_df(self, pivot_values=False):
        """
        Get table of ZonePurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZonePurchasers, pivot_values)

    def get_zone_markets_df(self, pivot_values=False):
        """
        Get table of ZoneMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneMarkets, pivot_values)

    def get_zone_capacity_markets_df(self, pivot_values=False):
        """
        Get table of ZoneCapacityMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneCapacityMarkets, pivot_values)

    def get_zone_capacity_batteries_df(self, pivot_values=False):
        """
        Get table of ZoneCapacityBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneCapacityBatteries, pivot_values)

    def get_zone_batteries_df(self, pivot_values=False):
        """
        Get table of ZoneBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneBatteries, pivot_values)

    def get_zone_region_df(self, pivot_values=False):
        """
        Get table of ZoneRegion records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneRegion, pivot_values)

    def get_zone_zones_df(self, pivot_values=False):
        """
        Get table of ZoneZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneZones, pivot_values)

    def get_zone_reference_node_df(self, pivot_values=False):
        """
        Get table of ZoneReferenceNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneReferenceNode, pivot_values)

    def get_zone_exporting_capacity_lines_df(self, pivot_values=False):
        """
        Get table of ZoneExportingCapacityLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneExportingCapacityLines, pivot_values)

    def get_zone_exporting_lines_df(self, pivot_values=False):
        """
        Get table of ZoneExportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneExportingLines, pivot_values)

    def get_zone_importing_capacity_lines_df(self, pivot_values=False):
        """
        Get table of ZoneImportingCapacityLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneImportingCapacityLines, pivot_values)

    def get_zone_importing_lines_df(self, pivot_values=False):
        """
        Get table of ZoneImportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneImportingLines, pivot_values)

    def get_zone_interzonal_lines_df(self, pivot_values=False):
        """
        Get table of ZoneInterzonalLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneInterzonalLines, pivot_values)

    def get_zone_intrazonal_lines_df(self, pivot_values=False):
        """
        Get table of ZoneIntrazonalLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneIntrazonalLines, pivot_values)

    def get_zone_exporting_capacity_transformers_df(self, pivot_values=False):
        """
        Get table of ZoneExportingCapacityTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneExportingCapacityTransformers, pivot_values)

    def get_zone_exporting_transformers_df(self, pivot_values=False):
        """
        Get table of ZoneExportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneExportingTransformers, pivot_values)

    def get_zone_importing_capacity_transformers_df(self, pivot_values=False):
        """
        Get table of ZoneImportingCapacityTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneImportingCapacityTransformers, pivot_values)

    def get_zone_importing_transformers_df(self, pivot_values=False):
        """
        Get table of ZoneImportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneImportingTransformers, pivot_values)

    def get_zone_interzonal_transformers_df(self, pivot_values=False):
        """
        Get table of ZoneInterzonalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneInterzonalTransformers, pivot_values)

    def get_zone_intrazonal_transformers_df(self, pivot_values=False):
        """
        Get table of ZoneIntrazonalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ZoneIntrazonalTransformers, pivot_values)

    def get_node_region_df(self, pivot_values=False):
        """
        Get table of NodeRegion records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.NodeRegion, pivot_values)

    def get_node_capacity_zone_df(self, pivot_values=False):
        """
        Get table of NodeCapacityZone records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.NodeCapacityZone, pivot_values)

    def get_node_zone_df(self, pivot_values=False):
        """
        Get table of NodeZone records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.NodeZone, pivot_values)

    def get_node_hubs_df(self, pivot_values=False):
        """
        Get table of NodeHubs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.NodeHubs, pivot_values)

    def get_line_node_from_df(self, pivot_values=False):
        """
        Get table of LineNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.LineNodeFrom, pivot_values)

    def get_line_node_to_df(self, pivot_values=False):
        """
        Get table of LineNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.LineNodeTo, pivot_values)

    def get_line_companies_df(self, pivot_values=False):
        """
        Get table of LineCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.LineCompanies, pivot_values)

    def get_mlf_regions_df(self, pivot_values=False):
        """
        Get table of MLFRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MLFRegions, pivot_values)

    def get_mlf_node_df(self, pivot_values=False):
        """
        Get table of MLFNode records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MLFNode, pivot_values)

    def get_mlf_line_df(self, pivot_values=False):
        """
        Get table of MLFLine records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MLFLine, pivot_values)

    def get_transformer_node_from_df(self, pivot_values=False):
        """
        Get table of TransformerNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransformerNodeFrom, pivot_values)

    def get_transformer_node_to_df(self, pivot_values=False):
        """
        Get table of TransformerNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransformerNodeTo, pivot_values)

    def get_flow_control_line_df(self, pivot_values=False):
        """
        Get table of FlowControlLine records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FlowControlLine, pivot_values)

    def get_flow_control_lines_star__df(self, pivot_values=False):
        """
        Get table of FlowControlLines_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FlowControlLines_star_, pivot_values)

    def get_interface_lines_df(self, pivot_values=False):
        """
        Get table of InterfaceLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.InterfaceLines, pivot_values)

    def get_interface_transformers_df(self, pivot_values=False):
        """
        Get table of InterfaceTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.InterfaceTransformers, pivot_values)

    def get_contingency_generators_df(self, pivot_values=False):
        """
        Get table of ContingencyGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyGenerators, pivot_values)

    def get_contingency_lines_df(self, pivot_values=False):
        """
        Get table of ContingencyLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyLines, pivot_values)

    def get_contingency_monitored_lines_df(self, pivot_values=False):
        """
        Get table of ContingencyMonitoredLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyMonitoredLines, pivot_values)

    def get_contingency_monitored_transformers_df(self, pivot_values=False):
        """
        Get table of ContingencyMonitoredTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyMonitoredTransformers, pivot_values)

    def get_contingency_transformers_df(self, pivot_values=False):
        """
        Get table of ContingencyTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyTransformers, pivot_values)

    def get_contingency_monitored_interfaces_df(self, pivot_values=False):
        """
        Get table of ContingencyMonitoredInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ContingencyMonitoredInterfaces, pivot_values)

    def get_company_fuels_df(self, pivot_values=False):
        """
        Get table of CompanyFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CompanyFuels, pivot_values)

    def get_company_emissions_df(self, pivot_values=False):
        """
        Get table of CompanyEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CompanyEmissions, pivot_values)

    def get_company_reserves_df(self, pivot_values=False):
        """
        Get table of CompanyReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CompanyReserves, pivot_values)

    def get_company_regions_df(self, pivot_values=False):
        """
        Get table of CompanyRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CompanyRegions, pivot_values)

    def get_financial_contract_generators_df(self, pivot_values=False):
        """
        Get table of FinancialContractGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractGenerators, pivot_values)

    def get_financial_contract_region_df(self, pivot_values=False):
        """
        Get table of FinancialContractRegion records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractRegion, pivot_values)

    def get_financial_contract_regions_df(self, pivot_values=False):
        """
        Get table of FinancialContractRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractRegions, pivot_values)

    def get_financial_contract_generating_companies_df(self, pivot_values=False):
        """
        Get table of FinancialContractGeneratingCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractGeneratingCompanies, pivot_values)

    def get_financial_contract_purchasing_companies_df(self, pivot_values=False):
        """
        Get table of FinancialContractPurchasingCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractPurchasingCompanies, pivot_values)

    def get_financial_contract_conditions_df(self, pivot_values=False):
        """
        Get table of FinancialContractConditions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.FinancialContractConditions, pivot_values)

    def get_transmission_right_node_from_df(self, pivot_values=False):
        """
        Get table of TransmissionRightNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightNodeFrom, pivot_values)

    def get_transmission_right_node_to_df(self, pivot_values=False):
        """
        Get table of TransmissionRightNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightNodeTo, pivot_values)

    def get_transmission_right_zone_from_df(self, pivot_values=False):
        """
        Get table of TransmissionRightZoneFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightZoneFrom, pivot_values)

    def get_transmission_right_zone_to_df(self, pivot_values=False):
        """
        Get table of TransmissionRightZoneTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightZoneTo, pivot_values)

    def get_transmission_right_hub_from_df(self, pivot_values=False):
        """
        Get table of TransmissionRightHubFrom records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightHubFrom, pivot_values)

    def get_transmission_right_hub_to_df(self, pivot_values=False):
        """
        Get table of TransmissionRightHubTo records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightHubTo, pivot_values)

    def get_transmission_right_line_df(self, pivot_values=False):
        """
        Get table of TransmissionRightLine records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightLine, pivot_values)

    def get_transmission_right_companies_df(self, pivot_values=False):
        """
        Get table of TransmissionRightCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.TransmissionRightCompanies, pivot_values)

    def get_cournot_region_df(self, pivot_values=False):
        """
        Get table of CournotRegion records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.CournotRegion, pivot_values)

    def get_rsi_region_df(self, pivot_values=False):
        """
        Get table of RSIRegion records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RSIRegion, pivot_values)

    def get_rsi_lines_df(self, pivot_values=False):
        """
        Get table of RSILines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RSILines, pivot_values)

    def get_rsi_interfaces_df(self, pivot_values=False):
        """
        Get table of RSIInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RSIInterfaces, pivot_values)

    def get_rsi_companies_df(self, pivot_values=False):
        """
        Get table of RSICompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.RSICompanies, pivot_values)

    def get_market_capacity_generators_df(self, pivot_values=False):
        """
        Get table of MarketCapacityGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketCapacityGenerators, pivot_values)

    def get_market_heat_generators_df(self, pivot_values=False):
        """
        Get table of MarketHeatGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketHeatGenerators, pivot_values)

    def get_market_fuels_df(self, pivot_values=False):
        """
        Get table of MarketFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketFuels, pivot_values)

    def get_market_emissions_df(self, pivot_values=False):
        """
        Get table of MarketEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketEmissions, pivot_values)

    def get_market_reserves_df(self, pivot_values=False):
        """
        Get table of MarketReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketReserves, pivot_values)

    def get_market_gas_nodes_df(self, pivot_values=False):
        """
        Get table of MarketGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketGasNodes, pivot_values)

    def get_market_nodes_df(self, pivot_values=False):
        """
        Get table of MarketNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketNodes, pivot_values)

    def get_market_companies_df(self, pivot_values=False):
        """
        Get table of MarketCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.MarketCompanies, pivot_values)

    def get_constraint_generators_df(self, pivot_values=False):
        """
        Get table of ConstraintGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGenerators, pivot_values)

    def get_constraint_fuels_df(self, pivot_values=False):
        """
        Get table of ConstraintFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintFuels, pivot_values)

    def get_constraint_fuel_contracts_df(self, pivot_values=False):
        """
        Get table of ConstraintFuelContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintFuelContracts, pivot_values)

    def get_constraint_emissions_df(self, pivot_values=False):
        """
        Get table of ConstraintEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintEmissions, pivot_values)

    def get_constraint_abatements_df(self, pivot_values=False):
        """
        Get table of ConstraintAbatements records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintAbatements, pivot_values)

    def get_constraint_storages_df(self, pivot_values=False):
        """
        Get table of ConstraintStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintStorages, pivot_values)

    def get_constraint_waterways_df(self, pivot_values=False):
        """
        Get table of ConstraintWaterways records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintWaterways, pivot_values)

    def get_constraint_physical_contracts_df(self, pivot_values=False):
        """
        Get table of ConstraintPhysicalContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintPhysicalContracts, pivot_values)

    def get_constraint_purchasers_df(self, pivot_values=False):
        """
        Get table of ConstraintPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintPurchasers, pivot_values)

    def get_constraint_reserves_df(self, pivot_values=False):
        """
        Get table of ConstraintReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintReserves, pivot_values)

    def get_constraint_batteries_df(self, pivot_values=False):
        """
        Get table of ConstraintBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintBatteries, pivot_values)

    def get_constraint_maintenances_df(self, pivot_values=False):
        """
        Get table of ConstraintMaintenances records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintMaintenances, pivot_values)

    def get_constraint_heat_plants_df(self, pivot_values=False):
        """
        Get table of ConstraintHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintHeatPlants, pivot_values)

    def get_constraint_heat_nodes_df(self, pivot_values=False):
        """
        Get table of ConstraintHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintHeatNodes, pivot_values)

    def get_constraint_gas_fields_df(self, pivot_values=False):
        """
        Get table of ConstraintGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasFields, pivot_values)

    def get_constraint_gas_plants_df(self, pivot_values=False):
        """
        Get table of ConstraintGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasPlants, pivot_values)

    def get_constraint_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of ConstraintGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasPipelines, pivot_values)

    def get_constraint_gas_nodes_df(self, pivot_values=False):
        """
        Get table of ConstraintGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasNodes, pivot_values)

    def get_constraint_gas_storages_df(self, pivot_values=False):
        """
        Get table of ConstraintGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasStorages, pivot_values)

    def get_constraint_gas_basins_df(self, pivot_values=False):
        """
        Get table of ConstraintGasBasins records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasBasins, pivot_values)

    def get_constraint_gas_contracts_df(self, pivot_values=False):
        """
        Get table of ConstraintGasContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasContracts, pivot_values)

    def get_constraint_gas_transports_df(self, pivot_values=False):
        """
        Get table of ConstraintGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintGasTransports, pivot_values)

    def get_constraint_water_plants_df(self, pivot_values=False):
        """
        Get table of ConstraintWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintWaterPlants, pivot_values)

    def get_constraint_water_pipelines_df(self, pivot_values=False):
        """
        Get table of ConstraintWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintWaterPipelines, pivot_values)

    def get_constraint_water_nodes_df(self, pivot_values=False):
        """
        Get table of ConstraintWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintWaterNodes, pivot_values)

    def get_constraint_water_storages_df(self, pivot_values=False):
        """
        Get table of ConstraintWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintWaterStorages, pivot_values)

    def get_constraint_regions_df(self, pivot_values=False):
        """
        Get table of ConstraintRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintRegions, pivot_values)

    def get_constraint_zones_df(self, pivot_values=False):
        """
        Get table of ConstraintZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintZones, pivot_values)

    def get_constraint_nodes_df(self, pivot_values=False):
        """
        Get table of ConstraintNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintNodes, pivot_values)

    def get_constraint_lines_df(self, pivot_values=False):
        """
        Get table of ConstraintLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintLines, pivot_values)

    def get_constraint_transformers_df(self, pivot_values=False):
        """
        Get table of ConstraintTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintTransformers, pivot_values)

    def get_constraint_flow_controls_df(self, pivot_values=False):
        """
        Get table of ConstraintFlowControls records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintFlowControls, pivot_values)

    def get_constraint_interfaces_df(self, pivot_values=False):
        """
        Get table of ConstraintInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintInterfaces, pivot_values)

    def get_constraint_companies_df(self, pivot_values=False):
        """
        Get table of ConstraintCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintCompanies, pivot_values)

    def get_constraint_hubs_df(self, pivot_values=False):
        """
        Get table of ConstraintHubs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintHubs, pivot_values)

    def get_constraint_markets_df(self, pivot_values=False):
        """
        Get table of ConstraintMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintMarkets, pivot_values)

    def get_constraint_decision_variables_df(self, pivot_values=False):
        """
        Get table of ConstraintDecisionVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintDecisionVariables, pivot_values)

    def get_constraint_variables_df(self, pivot_values=False):
        """
        Get table of ConstraintVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintVariables, pivot_values)

    def get_constraint_conditions_df(self, pivot_values=False):
        """
        Get table of ConstraintConditions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ConstraintConditions, pivot_values)

    def get_decision_variable_generators_df(self, pivot_values=False):
        """
        Get table of DecisionVariableGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.DecisionVariableGenerators, pivot_values)

    def get_decision_variable_nodes_df(self, pivot_values=False):
        """
        Get table of DecisionVariableNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.DecisionVariableNodes, pivot_values)

    def get_decision_variable_gas_plants_df(self, pivot_values=False):
        """
        Get table of DecisionVariableGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.DecisionVariableGasPlants, pivot_values)

    def get_decision_variable_water_plants_df(self, pivot_values=False):
        """
        Get table of DecisionVariableWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.DecisionVariableWaterPlants, pivot_values)

    def get_decision_variable_definition_df(self, pivot_values=False):
        """
        Get table of DecisionVariableDefinition records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.DecisionVariableDefinition, pivot_values)

    def get_variable_generators_df(self, pivot_values=False):
        """
        Get table of VariableGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableGenerators, pivot_values)

    def get_variable_fuels_df(self, pivot_values=False):
        """
        Get table of VariableFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableFuels, pivot_values)

    def get_variable_reserves_df(self, pivot_values=False):
        """
        Get table of VariableReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableReserves, pivot_values)

    def get_variable_regions_df(self, pivot_values=False):
        """
        Get table of VariableRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableRegions, pivot_values)

    def get_variable_zones_df(self, pivot_values=False):
        """
        Get table of VariableZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableZones, pivot_values)

    def get_variable_nodes_df(self, pivot_values=False):
        """
        Get table of VariableNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableNodes, pivot_values)

    def get_variable_lines_df(self, pivot_values=False):
        """
        Get table of VariableLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableLines, pivot_values)

    def get_variable_interfaces_df(self, pivot_values=False):
        """
        Get table of VariableInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableInterfaces, pivot_values)

    def get_variable_storages_df(self, pivot_values=False):
        """
        Get table of VariableStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableStorages, pivot_values)

    def get_variable_heat_nodes_df(self, pivot_values=False):
        """
        Get table of VariableHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableHeatNodes, pivot_values)

    def get_variable_heat_plants_df(self, pivot_values=False):
        """
        Get table of VariableHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableHeatPlants, pivot_values)

    def get_variable_conditions_df(self, pivot_values=False):
        """
        Get table of VariableConditions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableConditions, pivot_values)

    def get_variable_variables_df(self, pivot_values=False):
        """
        Get table of VariableVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.VariableVariables, pivot_values)

    def get_global_storages_df(self, pivot_values=False):
        """
        Get table of GlobalStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.GlobalStorages, pivot_values)

    def get_model_scenarios_df(self, pivot_values=False):
        """
        Get table of ModelScenarios records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelScenarios, pivot_values)

    def get_model_horizon_df(self, pivot_values=False):
        """
        Get table of ModelHorizon records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelHorizon, pivot_values)

    def get_model_report_df(self, pivot_values=False):
        """
        Get table of ModelReport records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelReport, pivot_values)

    def get_model_lt_plan_df(self, pivot_values=False):
        """
        Get table of ModelLTPlan records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelLTPlan, pivot_values)

    def get_model_pasa_df(self, pivot_values=False):
        """
        Get table of ModelPASA records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelPASA, pivot_values)

    def get_model_mt_schedule_df(self, pivot_values=False):
        """
        Get table of ModelMTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelMTSchedule, pivot_values)

    def get_model_st_schedule_df(self, pivot_values=False):
        """
        Get table of ModelSTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelSTSchedule, pivot_values)

    def get_model_transmission_df(self, pivot_values=False):
        """
        Get table of ModelTransmission records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelTransmission, pivot_values)

    def get_model_production_df(self, pivot_values=False):
        """
        Get table of ModelProduction records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelProduction, pivot_values)

    def get_model_competition_df(self, pivot_values=False):
        """
        Get table of ModelCompetition records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelCompetition, pivot_values)

    def get_model_stochastic_df(self, pivot_values=False):
        """
        Get table of ModelStochastic records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelStochastic, pivot_values)

    def get_model_performance_df(self, pivot_values=False):
        """
        Get table of ModelPerformance records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelPerformance, pivot_values)

    def get_model_diagnostic_df(self, pivot_values=False):
        """
        Get table of ModelDiagnostic records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelDiagnostic, pivot_values)

    def get_model_interleaved_df(self, pivot_values=False):
        """
        Get table of ModelInterleaved records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ModelInterleaved, pivot_values)

    def get_project_models_df(self, pivot_values=False):
        """
        Get table of ProjectModels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ProjectModels, pivot_values)

    def get_project_horizon_df(self, pivot_values=False):
        """
        Get table of ProjectHorizon records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ProjectHorizon, pivot_values)

    def get_project_report_df(self, pivot_values=False):
        """
        Get table of ProjectReport records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ProjectReport, pivot_values)

    def get_list_generators_df(self, pivot_values=False):
        """
        Get table of ListGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGenerators, pivot_values)

    def get_list_fuels_df(self, pivot_values=False):
        """
        Get table of ListFuels records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListFuels, pivot_values)

    def get_list_fuel_contracts_df(self, pivot_values=False):
        """
        Get table of ListFuelContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListFuelContracts, pivot_values)

    def get_list_emissions_df(self, pivot_values=False):
        """
        Get table of ListEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListEmissions, pivot_values)

    def get_list_abatements_df(self, pivot_values=False):
        """
        Get table of ListAbatements records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListAbatements, pivot_values)

    def get_list_storages_df(self, pivot_values=False):
        """
        Get table of ListStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListStorages, pivot_values)

    def get_list_waterways_df(self, pivot_values=False):
        """
        Get table of ListWaterways records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterways, pivot_values)

    def get_list_power_stations_df(self, pivot_values=False):
        """
        Get table of ListPowerStations records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListPowerStations, pivot_values)

    def get_list_physical_contracts_df(self, pivot_values=False):
        """
        Get table of ListPhysicalContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListPhysicalContracts, pivot_values)

    def get_list_purchasers_df(self, pivot_values=False):
        """
        Get table of ListPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListPurchasers, pivot_values)

    def get_list_reserves_df(self, pivot_values=False):
        """
        Get table of ListReserves records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListReserves, pivot_values)

    def get_list_batteries_df(self, pivot_values=False):
        """
        Get table of ListBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListBatteries, pivot_values)

    def get_list_maintenances_df(self, pivot_values=False):
        """
        Get table of ListMaintenances records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListMaintenances, pivot_values)

    def get_list_heat_plants_df(self, pivot_values=False):
        """
        Get table of ListHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListHeatPlants, pivot_values)

    def get_list_heat_nodes_df(self, pivot_values=False):
        """
        Get table of ListHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListHeatNodes, pivot_values)

    def get_list_gas_fields_df(self, pivot_values=False):
        """
        Get table of ListGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasFields, pivot_values)

    def get_list_gas_plants_df(self, pivot_values=False):
        """
        Get table of ListGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasPlants, pivot_values)

    def get_list_gas_pipelines_df(self, pivot_values=False):
        """
        Get table of ListGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasPipelines, pivot_values)

    def get_list_gas_nodes_df(self, pivot_values=False):
        """
        Get table of ListGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasNodes, pivot_values)

    def get_list_gas_storages_df(self, pivot_values=False):
        """
        Get table of ListGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasStorages, pivot_values)

    def get_list_gas_demands_df(self, pivot_values=False):
        """
        Get table of ListGasDemands records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasDemands, pivot_values)

    def get_list_gas_basins_df(self, pivot_values=False):
        """
        Get table of ListGasBasins records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasBasins, pivot_values)

    def get_list_gas_zones_df(self, pivot_values=False):
        """
        Get table of ListGasZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasZones, pivot_values)

    def get_list_gas_contracts_df(self, pivot_values=False):
        """
        Get table of ListGasContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasContracts, pivot_values)

    def get_list_gas_transports_df(self, pivot_values=False):
        """
        Get table of ListGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGasTransports, pivot_values)

    def get_list_water_plants_df(self, pivot_values=False):
        """
        Get table of ListWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterPlants, pivot_values)

    def get_list_water_pipelines_df(self, pivot_values=False):
        """
        Get table of ListWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterPipelines, pivot_values)

    def get_list_water_nodes_df(self, pivot_values=False):
        """
        Get table of ListWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterNodes, pivot_values)

    def get_list_water_storages_df(self, pivot_values=False):
        """
        Get table of ListWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterStorages, pivot_values)

    def get_list_water_demands_df(self, pivot_values=False):
        """
        Get table of ListWaterDemands records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterDemands, pivot_values)

    def get_list_water_zones_df(self, pivot_values=False):
        """
        Get table of ListWaterZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListWaterZones, pivot_values)

    def get_list_regions_df(self, pivot_values=False):
        """
        Get table of ListRegions records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListRegions, pivot_values)

    def get_list_zones_df(self, pivot_values=False):
        """
        Get table of ListZones records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListZones, pivot_values)

    def get_list_nodes_df(self, pivot_values=False):
        """
        Get table of ListNodes records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListNodes, pivot_values)

    def get_list_lines_df(self, pivot_values=False):
        """
        Get table of ListLines records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListLines, pivot_values)

    def get_list_ml_fs_df(self, pivot_values=False):
        """
        Get table of ListMLFs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListMLFs, pivot_values)

    def get_list_transformers_df(self, pivot_values=False):
        """
        Get table of ListTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListTransformers, pivot_values)

    def get_list_flow_controls_df(self, pivot_values=False):
        """
        Get table of ListFlowControls records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListFlowControls, pivot_values)

    def get_list_interfaces_df(self, pivot_values=False):
        """
        Get table of ListInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListInterfaces, pivot_values)

    def get_list_contingencies_df(self, pivot_values=False):
        """
        Get table of ListContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListContingencies, pivot_values)

    def get_list_companies_df(self, pivot_values=False):
        """
        Get table of ListCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListCompanies, pivot_values)

    def get_list_financial_contracts_df(self, pivot_values=False):
        """
        Get table of ListFinancialContracts records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListFinancialContracts, pivot_values)

    def get_list_hubs_df(self, pivot_values=False):
        """
        Get table of ListHubs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListHubs, pivot_values)

    def get_list_transmission_rights_df(self, pivot_values=False):
        """
        Get table of ListTransmissionRights records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListTransmissionRights, pivot_values)

    def get_list_cournots_df(self, pivot_values=False):
        """
        Get table of ListCournots records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListCournots, pivot_values)

    def get_list_rs_is_df(self, pivot_values=False):
        """
        Get table of ListRSIs records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListRSIs, pivot_values)

    def get_list_markets_df(self, pivot_values=False):
        """
        Get table of ListMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListMarkets, pivot_values)

    def get_list_constraints_df(self, pivot_values=False):
        """
        Get table of ListConstraints records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListConstraints, pivot_values)

    def get_list_decision_variables_df(self, pivot_values=False):
        """
        Get table of ListDecisionVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListDecisionVariables, pivot_values)

    def get_list_data_files_df(self, pivot_values=False):
        """
        Get table of ListDataFiles records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListDataFiles, pivot_values)

    def get_list_variables_df(self, pivot_values=False):
        """
        Get table of ListVariables records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListVariables, pivot_values)

    def get_list_timeslices_df(self, pivot_values=False):
        """
        Get table of ListTimeslices records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListTimeslices, pivot_values)

    def get_list_globals_df(self, pivot_values=False):
        """
        Get table of ListGlobals records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListGlobals, pivot_values)

    def get_list_scenarios_df(self, pivot_values=False):
        """
        Get table of ListScenarios records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListScenarios, pivot_values)

    def get_list_lists_df(self, pivot_values=False):
        """
        Get table of ListLists records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ListLists, pivot_values)

    def get_report_lists_df(self, pivot_values=False):
        """
        Get table of ReportLists records
        :return: DataFrame
        """
        return self.get_collection_df(CollectionEnum.ReportLists, pivot_values)


if __name__ == '__main__':

    fname = r'C:\Users\penversa\Git\Python-PLEXOS-API\Input Files\rts3.xml'
    plexos_db = PlexosDatabase(fname)

    gen_df = plexos_db.get_system_generators_df()

    xfo_df = plexos_db.get_system_transformers_df()

    nodes_df = plexos_db.get_system_nodes_df(pivot_values=True)

    print()
