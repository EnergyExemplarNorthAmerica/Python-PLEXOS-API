import os
import pandas as pd
from PlexosAPI.api import plx, plx_enums
from PlexosAPI.enumerations import CollectionEnum


def format_property(val):
    return val.replace('_x0020', '')


class PlexosDatabase:

    def __init__(self, file_name):
        """
        Database constructor, it opens or creates a Plexos DataBase
        :param file_name: Plexos .xml file name
        """

        # file name
        self.file_name = file_name

        # database connection
        self.db = plx.DatabaseCore()

        if not os.path.exists(self.file_name):

            # if the file does not exist, create the DB, and do not overwrite
            self.db.NewEmptyDatabase(self.file_name, False)

        # connect the database
        self.db.Connection(self.file_name)

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
        :param record_set: .Net ADODB recordset
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
                data.append({format_property(f): d for f, d in zip(fileds, values)})
                record_set.MoveNext()

        return data

    def get_collection_df(self, collection):
        """
        Get the DataFrame with the data of a collection
        :param collection: i.e.: plx_enums.CollectionEnum.SystemGenerators
        :return: DataFrame
        """
        names = self.get_collection_names(collection)

        if len(names) > 0:
            record_set = self.get_record_set(collection, names)

            data = self.get_list_of_records_dictionary(record_set)
            return pd.DataFrame(data)
        else:
            return None

    def get_system_generators_df(self):
        """
        Get table of SystemGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGenerators)

    def get_system_fuels_df(self):
        """
        Get table of SystemFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemFuels)

    def get_system_fuel_contracts_df(self):
        """
        Get table of SystemFuelContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemFuelContracts)

    def get_system_emissions_df(self):
        """
        Get table of SystemEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemEmissions)

    def get_system_abatements_df(self):
        """
        Get table of SystemAbatements records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemAbatements)

    def get_system_storages_df(self):
        """
        Get table of SystemStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemStorages)

    def get_system_waterways_df(self):
        """
        Get table of SystemWaterways records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterways)

    def get_system_power_stations_df(self):
        """
        Get table of SystemPowerStations records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemPowerStations)

    def get_system_physical_contracts_df(self):
        """
        Get table of SystemPhysicalContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemPhysicalContracts)

    def get_system_purchasers_df(self):
        """
        Get table of SystemPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemPurchasers)

    def get_system_reserves_df(self):
        """
        Get table of SystemReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemReserves)

    def get_system_batteries_df(self):
        """
        Get table of SystemBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemBatteries)

    def get_system_maintenances_df(self):
        """
        Get table of SystemMaintenances records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemMaintenances)

    def get_system_heat_plants_df(self):
        """
        Get table of SystemHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemHeatPlants)

    def get_system_heat_nodes_df(self):
        """
        Get table of SystemHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemHeatNodes)

    def get_system_gas_fields_df(self):
        """
        Get table of SystemGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasFields)

    def get_system_gas_plants_df(self):
        """
        Get table of SystemGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasPlants)

    def get_system_gas_pipelines_df(self):
        """
        Get table of SystemGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasPipelines)

    def get_system_gas_nodes_df(self):
        """
        Get table of SystemGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasNodes)

    def get_system_gas_storages_df(self):
        """
        Get table of SystemGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasStorages)

    def get_system_gas_demands_df(self):
        """
        Get table of SystemGasDemands records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasDemands)

    def get_system_gas_basins_df(self):
        """
        Get table of SystemGasBasins records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasBasins)

    def get_system_gas_zones_df(self):
        """
        Get table of SystemGasZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasZones)

    def get_system_gas_contracts_df(self):
        """
        Get table of SystemGasContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasContracts)

    def get_system_gas_transports_df(self):
        """
        Get table of SystemGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGasTransports)

    def get_system_water_plants_df(self):
        """
        Get table of SystemWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterPlants)

    def get_system_water_pipelines_df(self):
        """
        Get table of SystemWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterPipelines)

    def get_system_water_nodes_df(self):
        """
        Get table of SystemWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterNodes)

    def get_system_water_storages_df(self):
        """
        Get table of SystemWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterStorages)

    def get_system_water_demands_df(self):
        """
        Get table of SystemWaterDemands records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterDemands)

    def get_system_water_zones_df(self):
        """
        Get table of SystemWaterZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemWaterZones)

    def get_system_regions_df(self):
        """
        Get table of SystemRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemRegions)

    def get_system_zones_df(self):
        """
        Get table of SystemZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemZones)

    def get_system_nodes_df(self):
        """
        Get table of SystemNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemNodes)

    def get_system_lines_df(self):
        """
        Get table of SystemLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemLines)

    def get_system_ml_fs_df(self):
        """
        Get table of SystemMLFs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemMLFs)

    def get_system_transformers_df(self):
        """
        Get table of SystemTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemTransformers)

    def get_system_flow_controls_df(self):
        """
        Get table of SystemFlowControls records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemFlowControls)

    def get_system_interfaces_df(self):
        """
        Get table of SystemInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemInterfaces)

    def get_system_contingencies_df(self):
        """
        Get table of SystemContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemContingencies)

    def get_system_companies_df(self):
        """
        Get table of SystemCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemCompanies)

    def get_system_financial_contracts_df(self):
        """
        Get table of SystemFinancialContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemFinancialContracts)

    def get_system_hubs_df(self):
        """
        Get table of SystemHubs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemHubs)

    def get_system_transmission_rights_df(self):
        """
        Get table of SystemTransmissionRights records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemTransmissionRights)

    def get_system_cournots_df(self):
        """
        Get table of SystemCournots records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemCournots)

    def get_system_rs_is_df(self):
        """
        Get table of SystemRSIs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemRSIs)

    def get_system_markets_df(self):
        """
        Get table of SystemMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemMarkets)

    def get_system_constraints_df(self):
        """
        Get table of SystemConstraints records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemConstraints)

    def get_system_decision_variables_df(self):
        """
        Get table of SystemDecisionVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemDecisionVariables)

    def get_system_lists_df(self):
        """
        Get table of SystemLists records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemLists)

    def get_system_data_files_df(self):
        """
        Get table of SystemDataFiles records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemDataFiles)

    def get_system_variables_df(self):
        """
        Get table of SystemVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemVariables)

    def get_system_timeslices_df(self):
        """
        Get table of SystemTimeslices records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemTimeslices)

    def get_system_globals_df(self):
        """
        Get table of SystemGlobals records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemGlobals)

    def get_system_scenarios_df(self):
        """
        Get table of SystemScenarios records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemScenarios)

    def get_system_models_df(self):
        """
        Get table of SystemModels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemModels)

    def get_system_projects_df(self):
        """
        Get table of SystemProjects records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemProjects)

    def get_system_horizons_df(self):
        """
        Get table of SystemHorizons records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemHorizons)

    def get_system_reports_df(self):
        """
        Get table of SystemReports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemReports)

    def get_system_lt_plan_df(self):
        """
        Get table of SystemLTPlan records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemLTPlan)

    def get_system_pasa_df(self):
        """
        Get table of SystemPASA records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemPASA)

    def get_system_mt_schedule_df(self):
        """
        Get table of SystemMTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemMTSchedule)

    def get_system_st_schedule_df(self):
        """
        Get table of SystemSTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemSTSchedule)

    def get_system_transmission_df(self):
        """
        Get table of SystemTransmission records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemTransmission)

    def get_system_production_df(self):
        """
        Get table of SystemProduction records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemProduction)

    def get_system_competition_df(self):
        """
        Get table of SystemCompetition records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemCompetition)

    def get_system_stochastic_df(self):
        """
        Get table of SystemStochastic records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemStochastic)

    def get_system_performance_df(self):
        """
        Get table of SystemPerformance records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemPerformance)

    def get_system_diagnostics_df(self):
        """
        Get table of SystemDiagnostics records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.SystemDiagnostics)

    def get_generator_template_df(self):
        """
        Get table of GeneratorTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorTemplate)

    def get_fuel_template_df(self):
        """
        Get table of FuelTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelTemplate)

    def get_fuel_contract_template_df(self):
        """
        Get table of FuelContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelContractTemplate)

    def get_emission_template_df(self):
        """
        Get table of EmissionTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.EmissionTemplate)

    def get_abatement_template_df(self):
        """
        Get table of AbatementTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.AbatementTemplate)

    def get_storage_template_df(self):
        """
        Get table of StorageTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.StorageTemplate)

    def get_waterway_template_df(self):
        """
        Get table of WaterwayTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterwayTemplate)

    def get_power_station_template_df(self):
        """
        Get table of PowerStationTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PowerStationTemplate)

    def get_physical_contract_template_df(self):
        """
        Get table of PhysicalContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PhysicalContractTemplate)

    def get_purchaser_template_df(self):
        """
        Get table of PurchaserTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PurchaserTemplate)

    def get_reserve_template_df(self):
        """
        Get table of ReserveTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveTemplate)

    def get_battery_template_df(self):
        """
        Get table of BatteryTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.BatteryTemplate)

    def get_maintenance_template_df(self):
        """
        Get table of MaintenanceTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MaintenanceTemplate)

    def get_heat_plant_template_df(self):
        """
        Get table of HeatPlantTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatPlantTemplate)

    def get_heat_node_template_df(self):
        """
        Get table of HeatNodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatNodeTemplate)

    def get_gas_field_template_df(self):
        """
        Get table of GasFieldTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasFieldTemplate)

    def get_gas_plant_template_df(self):
        """
        Get table of GasPlantTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPlantTemplate)

    def get_gas_pipeline_template_df(self):
        """
        Get table of GasPipelineTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPipelineTemplate)

    def get_gas_node_template_df(self):
        """
        Get table of GasNodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasNodeTemplate)

    def get_gas_storage_template_df(self):
        """
        Get table of GasStorageTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasStorageTemplate)

    def get_gas_demand_template_df(self):
        """
        Get table of GasDemandTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasDemandTemplate)

    def get_gas_basin_template_df(self):
        """
        Get table of GasBasinTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasBasinTemplate)

    def get_gas_zone_template_df(self):
        """
        Get table of GasZoneTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneTemplate)

    def get_gas_contract_template_df(self):
        """
        Get table of GasContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasContractTemplate)

    def get_water_plant_template_df(self):
        """
        Get table of WaterPlantTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPlantTemplate)

    def get_water_pipeline_template_df(self):
        """
        Get table of WaterPipelineTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPipelineTemplate)

    def get_water_node_template_df(self):
        """
        Get table of WaterNodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterNodeTemplate)

    def get_water_storage_template_df(self):
        """
        Get table of WaterStorageTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterStorageTemplate)

    def get_water_demand_template_df(self):
        """
        Get table of WaterDemandTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterDemandTemplate)

    def get_water_zone_template_df(self):
        """
        Get table of WaterZoneTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneTemplate)

    def get_region_template_df(self):
        """
        Get table of RegionTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionTemplate)

    def get_zone_template_df(self):
        """
        Get table of ZoneTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneTemplate)

    def get_node_template_df(self):
        """
        Get table of NodeTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.NodeTemplate)

    def get_line_template_df(self):
        """
        Get table of LineTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.LineTemplate)

    def get_mlf_template_df(self):
        """
        Get table of MLFTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MLFTemplate)

    def get_transformer_template_df(self):
        """
        Get table of TransformerTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransformerTemplate)

    def get_flow_control_template_df(self):
        """
        Get table of FlowControlTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FlowControlTemplate)

    def get_interface_template_df(self):
        """
        Get table of InterfaceTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.InterfaceTemplate)

    def get_contingency_template_df(self):
        """
        Get table of ContingencyTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyTemplate)

    def get_company_template_df(self):
        """
        Get table of CompanyTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CompanyTemplate)

    def get_financial_contract_template_df(self):
        """
        Get table of FinancialContractTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractTemplate)

    def get_hub_template_df(self):
        """
        Get table of HubTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HubTemplate)

    def get_transmission_right_template_df(self):
        """
        Get table of TransmissionRightTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightTemplate)

    def get_cournot_template_df(self):
        """
        Get table of CournotTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CournotTemplate)

    def get_rsi_template_df(self):
        """
        Get table of RSITemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RSITemplate)

    def get_market_template_df(self):
        """
        Get table of MarketTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketTemplate)

    def get_constraint_template_df(self):
        """
        Get table of ConstraintTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintTemplate)

    def get_decision_variable_template_df(self):
        """
        Get table of DecisionVariableTemplate records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.DecisionVariableTemplate)

    def get_generator_heat_input_df(self):
        """
        Get table of GeneratorHeatInput records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorHeatInput)

    def get_generator_transition_df(self):
        """
        Get table of GeneratorTransition records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorTransition)

    def get_generator_fuels_df(self):
        """
        Get table of GeneratorFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorFuels)

    def get_generator_start_fuels_df(self):
        """
        Get table of GeneratorStartFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorStartFuels)

    def get_generator_head_storage_df(self):
        """
        Get table of GeneratorHeadStorage records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorHeadStorage)

    def get_generator_tail_storage_df(self):
        """
        Get table of GeneratorTailStorage records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorTailStorage)

    def get_generator_power_station_df(self):
        """
        Get table of GeneratorPowerStation records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorPowerStation)

    def get_generator_markto_markets_df(self):
        """
        Get table of GeneratorMarktoMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorMarktoMarkets)

    def get_generator_gas_node_df(self):
        """
        Get table of GeneratorGasNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorGasNode)

    def get_generator_water_node_df(self):
        """
        Get table of GeneratorWaterNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorWaterNode)

    def get_generator_nodes_df(self):
        """
        Get table of GeneratorNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorNodes)

    def get_generator_nodes_star__df(self):
        """
        Get table of GeneratorNodes_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorNodes_star_)

    def get_generator_companies_df(self):
        """
        Get table of GeneratorCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorCompanies)

    def get_fuel_gas_nodes_df(self):
        """
        Get table of FuelGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelGasNodes)

    def get_fuel_companies_df(self):
        """
        Get table of FuelCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelCompanies)

    def get_fuel_contract_generators_df(self):
        """
        Get table of FuelContractGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelContractGenerators)

    def get_fuel_contract_fuel_df(self):
        """
        Get table of FuelContractFuel records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelContractFuel)

    def get_fuel_contract_companies_df(self):
        """
        Get table of FuelContractCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelContractCompanies)

    def get_fuel_contract_constraints_df(self):
        """
        Get table of FuelContractConstraints records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FuelContractConstraints)

    def get_emission_generators_df(self):
        """
        Get table of EmissionGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.EmissionGenerators)

    def get_emission_fuels_df(self):
        """
        Get table of EmissionFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.EmissionFuels)

    def get_emission_gas_nodes_df(self):
        """
        Get table of EmissionGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.EmissionGasNodes)

    def get_emission_gas_plants_df(self):
        """
        Get table of EmissionGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.EmissionGasPlants)

    def get_emission_water_plants_df(self):
        """
        Get table of EmissionWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.EmissionWaterPlants)

    def get_abatement_generators_df(self):
        """
        Get table of AbatementGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.AbatementGenerators)

    def get_abatement_emissions_df(self):
        """
        Get table of AbatementEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.AbatementEmissions)

    def get_abatement_consumables_df(self):
        """
        Get table of AbatementConsumables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.AbatementConsumables)

    def get_storage_water_nodes_df(self):
        """
        Get table of StorageWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.StorageWaterNodes)

    def get_waterway_storage_from_df(self):
        """
        Get table of WaterwayStorageFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterwayStorageFrom)

    def get_waterway_storage_to_df(self):
        """
        Get table of WaterwayStorageTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterwayStorageTo)

    def get_power_station_nodes_df(self):
        """
        Get table of PowerStationNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PowerStationNodes)

    def get_physical_contract_generation_node_df(self):
        """
        Get table of PhysicalContractGenerationNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PhysicalContractGenerationNode)

    def get_physical_contract_load_node_df(self):
        """
        Get table of PhysicalContractLoadNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PhysicalContractLoadNode)

    def get_physical_contract_companies_df(self):
        """
        Get table of PhysicalContractCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PhysicalContractCompanies)

    def get_purchaser_nodes_df(self):
        """
        Get table of PurchaserNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PurchaserNodes)

    def get_purchaser_nodes_star__df(self):
        """
        Get table of PurchaserNodes_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PurchaserNodes_star_)

    def get_purchaser_companies_df(self):
        """
        Get table of PurchaserCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.PurchaserCompanies)

    def get_reserve_generators_df(self):
        """
        Get table of ReserveGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveGenerators)

    def get_reserve_purchasers_df(self):
        """
        Get table of ReservePurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReservePurchasers)

    def get_reserve_generator_contingencies_df(self):
        """
        Get table of ReserveGeneratorContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveGeneratorContingencies)

    def get_reserve_generator_cost_allocation_df(self):
        """
        Get table of ReserveGeneratorCostAllocation records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveGeneratorCostAllocation)

    def get_reserve_batteries_df(self):
        """
        Get table of ReserveBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveBatteries)

    def get_reserve_nested_reserves_df(self):
        """
        Get table of ReserveNestedReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveNestedReserves)

    def get_reserve_regions_df(self):
        """
        Get table of ReserveRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveRegions)

    def get_reserve_line_contingencies_df(self):
        """
        Get table of ReserveLineContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReserveLineContingencies)

    def get_battery_node_df(self):
        """
        Get table of BatteryNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.BatteryNode)

    def get_battery_nodes_star__df(self):
        """
        Get table of BatteryNodes_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.BatteryNodes_star_)

    def get_battery_companies_df(self):
        """
        Get table of BatteryCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.BatteryCompanies)

    def get_maintenance_generators_df(self):
        """
        Get table of MaintenanceGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MaintenanceGenerators)

    def get_maintenance_gas_pipelines_df(self):
        """
        Get table of MaintenanceGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MaintenanceGasPipelines)

    def get_maintenance_lines_df(self):
        """
        Get table of MaintenanceLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MaintenanceLines)

    def get_maintenance_prerequisites_df(self):
        """
        Get table of MaintenancePrerequisites records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MaintenancePrerequisites)

    def get_generator_heat_input_nodes_df(self):
        """
        Get table of GeneratorHeatInputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorHeatInputNodes)

    def get_generator_heat_output_nodes_df(self):
        """
        Get table of GeneratorHeatOutputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GeneratorHeatOutputNodes)

    def get_heat_plant_fuels_df(self):
        """
        Get table of HeatPlantFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatPlantFuels)

    def get_heat_plant_nodes_df(self):
        """
        Get table of HeatPlantNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatPlantNodes)

    def get_heat_plant_heat_input_nodes_df(self):
        """
        Get table of HeatPlantHeatInputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatPlantHeatInputNodes)

    def get_heat_plant_heat_output_nodes_df(self):
        """
        Get table of HeatPlantHeatOutputNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatPlantHeatOutputNodes)

    def get_heat_plant_start_fuels_df(self):
        """
        Get table of HeatPlantStartFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatPlantStartFuels)

    def get_heat_node_heat_export_nodes_df(self):
        """
        Get table of HeatNodeHeatExportNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatNodeHeatExportNodes)

    def get_heat_node_water_plants_df(self):
        """
        Get table of HeatNodeWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.HeatNodeWaterPlants)

    def get_gas_field_companies_df(self):
        """
        Get table of GasFieldCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasFieldCompanies)

    def get_gas_field_gas_node_df(self):
        """
        Get table of GasFieldGasNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasFieldGasNode)

    def get_gas_field_gas_basin_df(self):
        """
        Get table of GasFieldGasBasin records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasFieldGasBasin)

    def get_gas_plant_input_node_df(self):
        """
        Get table of GasPlantInputNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPlantInputNode)

    def get_gas_plant_output_node_df(self):
        """
        Get table of GasPlantOutputNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPlantOutputNode)

    def get_gas_plant_node_df(self):
        """
        Get table of GasPlantNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPlantNode)

    def get_gas_pipeline_gas_node_from_df(self):
        """
        Get table of GasPipelineGasNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPipelineGasNodeFrom)

    def get_gas_pipeline_gas_node_to_df(self):
        """
        Get table of GasPipelineGasNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasPipelineGasNodeTo)

    def get_gas_node_gas_zones_df(self):
        """
        Get table of GasNodeGasZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasNodeGasZones)

    def get_gas_storage_gas_node_df(self):
        """
        Get table of GasStorageGasNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasStorageGasNode)

    def get_gas_demand_gas_nodes_df(self):
        """
        Get table of GasDemandGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasDemandGasNodes)

    def get_gas_demand_companies_df(self):
        """
        Get table of GasDemandCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasDemandCompanies)

    def get_gas_zone_generators_df(self):
        """
        Get table of GasZoneGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneGenerators)

    def get_gas_zone_gas_fields_df(self):
        """
        Get table of GasZoneGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneGasFields)

    def get_gas_zone_gas_plants_df(self):
        """
        Get table of GasZoneGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneGasPlants)

    def get_gas_zone_exporting_gas_pipelines_df(self):
        """
        Get table of GasZoneExportingGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneExportingGasPipelines)

    def get_gas_zone_importing_gas_pipelines_df(self):
        """
        Get table of GasZoneImportingGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneImportingGasPipelines)

    def get_gas_zone_interzonal_gas_pipelines_df(self):
        """
        Get table of GasZoneInterzonalGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneInterzonalGasPipelines)

    def get_gas_zone_intrazonal_gas_pipelines_df(self):
        """
        Get table of GasZoneIntrazonalGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneIntrazonalGasPipelines)

    def get_gas_zone_gas_storages_df(self):
        """
        Get table of GasZoneGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneGasStorages)

    def get_gas_zone_gas_demands_df(self):
        """
        Get table of GasZoneGasDemands records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneGasDemands)

    def get_gas_zone_exporting_gas_transports_df(self):
        """
        Get table of GasZoneExportingGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneExportingGasTransports)

    def get_gas_zone_importing_gas_transports_df(self):
        """
        Get table of GasZoneImportingGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneImportingGasTransports)

    def get_gas_zone_interzonal_gas_transports_df(self):
        """
        Get table of GasZoneInterzonalGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneInterzonalGasTransports)

    def get_gas_zone_intrazonal_gas_transports_df(self):
        """
        Get table of GasZoneIntrazonalGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasZoneIntrazonalGasTransports)

    def get_gas_contract_gas_fields_df(self):
        """
        Get table of GasContractGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasContractGasFields)

    def get_gas_contract_gas_pipelines_df(self):
        """
        Get table of GasContractGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasContractGasPipelines)

    def get_gas_contract_gas_transports_df(self):
        """
        Get table of GasContractGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasContractGasTransports)

    def get_gas_transport_export_node_df(self):
        """
        Get table of GasTransportExportNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasTransportExportNode)

    def get_gas_transport_import_node_df(self):
        """
        Get table of GasTransportImportNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GasTransportImportNode)

    def get_water_plant_input_node_df(self):
        """
        Get table of WaterPlantInputNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPlantInputNode)

    def get_water_plant_output_node_df(self):
        """
        Get table of WaterPlantOutputNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPlantOutputNode)

    def get_water_plant_node_df(self):
        """
        Get table of WaterPlantNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPlantNode)

    def get_water_pipeline_water_node_from_df(self):
        """
        Get table of WaterPipelineWaterNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPipelineWaterNodeFrom)

    def get_water_pipeline_water_node_to_df(self):
        """
        Get table of WaterPipelineWaterNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterPipelineWaterNodeTo)

    def get_water_node_water_zones_df(self):
        """
        Get table of WaterNodeWaterZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterNodeWaterZones)

    def get_water_node_node_df(self):
        """
        Get table of WaterNodeNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterNodeNode)

    def get_water_storage_water_node_df(self):
        """
        Get table of WaterStorageWaterNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterStorageWaterNode)

    def get_water_demand_water_nodes_df(self):
        """
        Get table of WaterDemandWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterDemandWaterNodes)

    def get_water_zone_water_plants_df(self):
        """
        Get table of WaterZoneWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneWaterPlants)

    def get_water_zone_water_storages_df(self):
        """
        Get table of WaterZoneWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneWaterStorages)

    def get_water_zone_exporting_water_pipelines_df(self):
        """
        Get table of WaterZoneExportingWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneExportingWaterPipelines)

    def get_water_zone_importing_water_pipelines_df(self):
        """
        Get table of WaterZoneImportingWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneImportingWaterPipelines)

    def get_water_zone_interzonal_water_pipelines_df(self):
        """
        Get table of WaterZoneInterzonalWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneInterzonalWaterPipelines)

    def get_water_zone_intrazonal_water_pipelines_df(self):
        """
        Get table of WaterZoneIntrazonalWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneIntrazonalWaterPipelines)

    def get_water_zone_water_demands_df(self):
        """
        Get table of WaterZoneWaterDemands records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.WaterZoneWaterDemands)

    def get_region_generators_df(self):
        """
        Get table of RegionGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionGenerators)

    def get_region_emissions_df(self):
        """
        Get table of RegionEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionEmissions)

    def get_region_generation_contracts_df(self):
        """
        Get table of RegionGenerationContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionGenerationContracts)

    def get_region_load_contracts_df(self):
        """
        Get table of RegionLoadContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionLoadContracts)

    def get_region_purchasers_df(self):
        """
        Get table of RegionPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionPurchasers)

    def get_region_markets_df(self):
        """
        Get table of RegionMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionMarkets)

    def get_region_batteries_df(self):
        """
        Get table of RegionBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionBatteries)

    def get_region_regions_df(self):
        """
        Get table of RegionRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionRegions)

    def get_region_reference_node_df(self):
        """
        Get table of RegionReferenceNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionReferenceNode)

    def get_region_exporting_lines_df(self):
        """
        Get table of RegionExportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionExportingLines)

    def get_region_importing_lines_df(self):
        """
        Get table of RegionImportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionImportingLines)

    def get_region_interregional_lines_df(self):
        """
        Get table of RegionInterregionalLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionInterregionalLines)

    def get_region_intraregional_lines_df(self):
        """
        Get table of RegionIntraregionalLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionIntraregionalLines)

    def get_region_exporting_transformers_df(self):
        """
        Get table of RegionExportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionExportingTransformers)

    def get_region_importing_transformers_df(self):
        """
        Get table of RegionImportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionImportingTransformers)

    def get_region_interregional_transformers_df(self):
        """
        Get table of RegionInterregionalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionInterregionalTransformers)

    def get_region_intraregional_transformers_df(self):
        """
        Get table of RegionIntraregionalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionIntraregionalTransformers)

    def get_region_utilities_df(self):
        """
        Get table of RegionUtilities records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RegionUtilities)

    def get_zone_capacity_generators_df(self):
        """
        Get table of ZoneCapacityGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneCapacityGenerators)

    def get_zone_generators_df(self):
        """
        Get table of ZoneGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneGenerators)

    def get_zone_emissions_df(self):
        """
        Get table of ZoneEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneEmissions)

    def get_zone_capacity_generation_contracts_df(self):
        """
        Get table of ZoneCapacityGenerationContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneCapacityGenerationContracts)

    def get_zone_capacity_load_contracts_df(self):
        """
        Get table of ZoneCapacityLoadContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneCapacityLoadContracts)

    def get_zone_generation_contracts_df(self):
        """
        Get table of ZoneGenerationContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneGenerationContracts)

    def get_zone_load_contracts_df(self):
        """
        Get table of ZoneLoadContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneLoadContracts)

    def get_zone_capacity_purchasers_df(self):
        """
        Get table of ZoneCapacityPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneCapacityPurchasers)

    def get_zone_purchasers_df(self):
        """
        Get table of ZonePurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZonePurchasers)

    def get_zone_markets_df(self):
        """
        Get table of ZoneMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneMarkets)

    def get_zone_capacity_markets_df(self):
        """
        Get table of ZoneCapacityMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneCapacityMarkets)

    def get_zone_capacity_batteries_df(self):
        """
        Get table of ZoneCapacityBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneCapacityBatteries)

    def get_zone_batteries_df(self):
        """
        Get table of ZoneBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneBatteries)

    def get_zone_region_df(self):
        """
        Get table of ZoneRegion records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneRegion)

    def get_zone_zones_df(self):
        """
        Get table of ZoneZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneZones)

    def get_zone_reference_node_df(self):
        """
        Get table of ZoneReferenceNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneReferenceNode)

    def get_zone_exporting_capacity_lines_df(self):
        """
        Get table of ZoneExportingCapacityLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneExportingCapacityLines)

    def get_zone_exporting_lines_df(self):
        """
        Get table of ZoneExportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneExportingLines)

    def get_zone_importing_capacity_lines_df(self):
        """
        Get table of ZoneImportingCapacityLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneImportingCapacityLines)

    def get_zone_importing_lines_df(self):
        """
        Get table of ZoneImportingLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneImportingLines)

    def get_zone_interzonal_lines_df(self):
        """
        Get table of ZoneInterzonalLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneInterzonalLines)

    def get_zone_intrazonal_lines_df(self):
        """
        Get table of ZoneIntrazonalLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneIntrazonalLines)

    def get_zone_exporting_capacity_transformers_df(self):
        """
        Get table of ZoneExportingCapacityTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneExportingCapacityTransformers)

    def get_zone_exporting_transformers_df(self):
        """
        Get table of ZoneExportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneExportingTransformers)

    def get_zone_importing_capacity_transformers_df(self):
        """
        Get table of ZoneImportingCapacityTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneImportingCapacityTransformers)

    def get_zone_importing_transformers_df(self):
        """
        Get table of ZoneImportingTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneImportingTransformers)

    def get_zone_interzonal_transformers_df(self):
        """
        Get table of ZoneInterzonalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneInterzonalTransformers)

    def get_zone_intrazonal_transformers_df(self):
        """
        Get table of ZoneIntrazonalTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ZoneIntrazonalTransformers)

    def get_node_region_df(self):
        """
        Get table of NodeRegion records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.NodeRegion)

    def get_node_capacity_zone_df(self):
        """
        Get table of NodeCapacityZone records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.NodeCapacityZone)

    def get_node_zone_df(self):
        """
        Get table of NodeZone records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.NodeZone)

    def get_node_hubs_df(self):
        """
        Get table of NodeHubs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.NodeHubs)

    def get_line_node_from_df(self):
        """
        Get table of LineNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.LineNodeFrom)

    def get_line_node_to_df(self):
        """
        Get table of LineNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.LineNodeTo)

    def get_line_companies_df(self):
        """
        Get table of LineCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.LineCompanies)

    def get_mlf_regions_df(self):
        """
        Get table of MLFRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MLFRegions)

    def get_mlf_node_df(self):
        """
        Get table of MLFNode records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MLFNode)

    def get_mlf_line_df(self):
        """
        Get table of MLFLine records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MLFLine)

    def get_transformer_node_from_df(self):
        """
        Get table of TransformerNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransformerNodeFrom)

    def get_transformer_node_to_df(self):
        """
        Get table of TransformerNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransformerNodeTo)

    def get_flow_control_line_df(self):
        """
        Get table of FlowControlLine records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FlowControlLine)

    def get_flow_control_lines_star__df(self):
        """
        Get table of FlowControlLines_star_ records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FlowControlLines_star_)

    def get_interface_lines_df(self):
        """
        Get table of InterfaceLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.InterfaceLines)

    def get_interface_transformers_df(self):
        """
        Get table of InterfaceTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.InterfaceTransformers)

    def get_contingency_generators_df(self):
        """
        Get table of ContingencyGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyGenerators)

    def get_contingency_lines_df(self):
        """
        Get table of ContingencyLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyLines)

    def get_contingency_monitored_lines_df(self):
        """
        Get table of ContingencyMonitoredLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyMonitoredLines)

    def get_contingency_monitored_transformers_df(self):
        """
        Get table of ContingencyMonitoredTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyMonitoredTransformers)

    def get_contingency_transformers_df(self):
        """
        Get table of ContingencyTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyTransformers)

    def get_contingency_monitored_interfaces_df(self):
        """
        Get table of ContingencyMonitoredInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ContingencyMonitoredInterfaces)

    def get_company_fuels_df(self):
        """
        Get table of CompanyFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CompanyFuels)

    def get_company_emissions_df(self):
        """
        Get table of CompanyEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CompanyEmissions)

    def get_company_reserves_df(self):
        """
        Get table of CompanyReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CompanyReserves)

    def get_company_regions_df(self):
        """
        Get table of CompanyRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CompanyRegions)

    def get_financial_contract_generators_df(self):
        """
        Get table of FinancialContractGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractGenerators)

    def get_financial_contract_region_df(self):
        """
        Get table of FinancialContractRegion records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractRegion)

    def get_financial_contract_regions_df(self):
        """
        Get table of FinancialContractRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractRegions)

    def get_financial_contract_generating_companies_df(self):
        """
        Get table of FinancialContractGeneratingCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractGeneratingCompanies)

    def get_financial_contract_purchasing_companies_df(self):
        """
        Get table of FinancialContractPurchasingCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractPurchasingCompanies)

    def get_financial_contract_conditions_df(self):
        """
        Get table of FinancialContractConditions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.FinancialContractConditions)

    def get_transmission_right_node_from_df(self):
        """
        Get table of TransmissionRightNodeFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightNodeFrom)

    def get_transmission_right_node_to_df(self):
        """
        Get table of TransmissionRightNodeTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightNodeTo)

    def get_transmission_right_zone_from_df(self):
        """
        Get table of TransmissionRightZoneFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightZoneFrom)

    def get_transmission_right_zone_to_df(self):
        """
        Get table of TransmissionRightZoneTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightZoneTo)

    def get_transmission_right_hub_from_df(self):
        """
        Get table of TransmissionRightHubFrom records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightHubFrom)

    def get_transmission_right_hub_to_df(self):
        """
        Get table of TransmissionRightHubTo records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightHubTo)

    def get_transmission_right_line_df(self):
        """
        Get table of TransmissionRightLine records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightLine)

    def get_transmission_right_companies_df(self):
        """
        Get table of TransmissionRightCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.TransmissionRightCompanies)

    def get_cournot_region_df(self):
        """
        Get table of CournotRegion records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.CournotRegion)

    def get_rsi_region_df(self):
        """
        Get table of RSIRegion records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RSIRegion)

    def get_rsi_lines_df(self):
        """
        Get table of RSILines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RSILines)

    def get_rsi_interfaces_df(self):
        """
        Get table of RSIInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RSIInterfaces)

    def get_rsi_companies_df(self):
        """
        Get table of RSICompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.RSICompanies)

    def get_market_capacity_generators_df(self):
        """
        Get table of MarketCapacityGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketCapacityGenerators)

    def get_market_heat_generators_df(self):
        """
        Get table of MarketHeatGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketHeatGenerators)

    def get_market_fuels_df(self):
        """
        Get table of MarketFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketFuels)

    def get_market_emissions_df(self):
        """
        Get table of MarketEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketEmissions)

    def get_market_reserves_df(self):
        """
        Get table of MarketReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketReserves)

    def get_market_gas_nodes_df(self):
        """
        Get table of MarketGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketGasNodes)

    def get_market_nodes_df(self):
        """
        Get table of MarketNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketNodes)

    def get_market_companies_df(self):
        """
        Get table of MarketCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.MarketCompanies)

    def get_constraint_generators_df(self):
        """
        Get table of ConstraintGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGenerators)

    def get_constraint_fuels_df(self):
        """
        Get table of ConstraintFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintFuels)

    def get_constraint_fuel_contracts_df(self):
        """
        Get table of ConstraintFuelContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintFuelContracts)

    def get_constraint_emissions_df(self):
        """
        Get table of ConstraintEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintEmissions)

    def get_constraint_abatements_df(self):
        """
        Get table of ConstraintAbatements records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintAbatements)

    def get_constraint_storages_df(self):
        """
        Get table of ConstraintStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintStorages)

    def get_constraint_waterways_df(self):
        """
        Get table of ConstraintWaterways records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintWaterways)

    def get_constraint_physical_contracts_df(self):
        """
        Get table of ConstraintPhysicalContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintPhysicalContracts)

    def get_constraint_purchasers_df(self):
        """
        Get table of ConstraintPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintPurchasers)

    def get_constraint_reserves_df(self):
        """
        Get table of ConstraintReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintReserves)

    def get_constraint_batteries_df(self):
        """
        Get table of ConstraintBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintBatteries)

    def get_constraint_maintenances_df(self):
        """
        Get table of ConstraintMaintenances records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintMaintenances)

    def get_constraint_heat_plants_df(self):
        """
        Get table of ConstraintHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintHeatPlants)

    def get_constraint_heat_nodes_df(self):
        """
        Get table of ConstraintHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintHeatNodes)

    def get_constraint_gas_fields_df(self):
        """
        Get table of ConstraintGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasFields)

    def get_constraint_gas_plants_df(self):
        """
        Get table of ConstraintGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasPlants)

    def get_constraint_gas_pipelines_df(self):
        """
        Get table of ConstraintGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasPipelines)

    def get_constraint_gas_nodes_df(self):
        """
        Get table of ConstraintGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasNodes)

    def get_constraint_gas_storages_df(self):
        """
        Get table of ConstraintGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasStorages)

    def get_constraint_gas_basins_df(self):
        """
        Get table of ConstraintGasBasins records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasBasins)

    def get_constraint_gas_contracts_df(self):
        """
        Get table of ConstraintGasContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasContracts)

    def get_constraint_gas_transports_df(self):
        """
        Get table of ConstraintGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintGasTransports)

    def get_constraint_water_plants_df(self):
        """
        Get table of ConstraintWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintWaterPlants)

    def get_constraint_water_pipelines_df(self):
        """
        Get table of ConstraintWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintWaterPipelines)

    def get_constraint_water_nodes_df(self):
        """
        Get table of ConstraintWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintWaterNodes)

    def get_constraint_water_storages_df(self):
        """
        Get table of ConstraintWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintWaterStorages)

    def get_constraint_regions_df(self):
        """
        Get table of ConstraintRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintRegions)

    def get_constraint_zones_df(self):
        """
        Get table of ConstraintZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintZones)

    def get_constraint_nodes_df(self):
        """
        Get table of ConstraintNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintNodes)

    def get_constraint_lines_df(self):
        """
        Get table of ConstraintLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintLines)

    def get_constraint_transformers_df(self):
        """
        Get table of ConstraintTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintTransformers)

    def get_constraint_flow_controls_df(self):
        """
        Get table of ConstraintFlowControls records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintFlowControls)

    def get_constraint_interfaces_df(self):
        """
        Get table of ConstraintInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintInterfaces)

    def get_constraint_companies_df(self):
        """
        Get table of ConstraintCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintCompanies)

    def get_constraint_hubs_df(self):
        """
        Get table of ConstraintHubs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintHubs)

    def get_constraint_markets_df(self):
        """
        Get table of ConstraintMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintMarkets)

    def get_constraint_decision_variables_df(self):
        """
        Get table of ConstraintDecisionVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintDecisionVariables)

    def get_constraint_variables_df(self):
        """
        Get table of ConstraintVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintVariables)

    def get_constraint_conditions_df(self):
        """
        Get table of ConstraintConditions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ConstraintConditions)

    def get_decision_variable_generators_df(self):
        """
        Get table of DecisionVariableGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.DecisionVariableGenerators)

    def get_decision_variable_nodes_df(self):
        """
        Get table of DecisionVariableNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.DecisionVariableNodes)

    def get_decision_variable_gas_plants_df(self):
        """
        Get table of DecisionVariableGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.DecisionVariableGasPlants)

    def get_decision_variable_water_plants_df(self):
        """
        Get table of DecisionVariableWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.DecisionVariableWaterPlants)

    def get_decision_variable_definition_df(self):
        """
        Get table of DecisionVariableDefinition records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.DecisionVariableDefinition)

    def get_variable_generators_df(self):
        """
        Get table of VariableGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableGenerators)

    def get_variable_fuels_df(self):
        """
        Get table of VariableFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableFuels)

    def get_variable_reserves_df(self):
        """
        Get table of VariableReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableReserves)

    def get_variable_regions_df(self):
        """
        Get table of VariableRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableRegions)

    def get_variable_zones_df(self):
        """
        Get table of VariableZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableZones)

    def get_variable_nodes_df(self):
        """
        Get table of VariableNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableNodes)

    def get_variable_lines_df(self):
        """
        Get table of VariableLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableLines)

    def get_variable_interfaces_df(self):
        """
        Get table of VariableInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableInterfaces)

    def get_variable_storages_df(self):
        """
        Get table of VariableStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableStorages)

    def get_variable_heat_nodes_df(self):
        """
        Get table of VariableHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableHeatNodes)

    def get_variable_heat_plants_df(self):
        """
        Get table of VariableHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableHeatPlants)

    def get_variable_conditions_df(self):
        """
        Get table of VariableConditions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableConditions)

    def get_variable_variables_df(self):
        """
        Get table of VariableVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.VariableVariables)

    def get_global_storages_df(self):
        """
        Get table of GlobalStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.GlobalStorages)

    def get_model_scenarios_df(self):
        """
        Get table of ModelScenarios records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelScenarios)

    def get_model_horizon_df(self):
        """
        Get table of ModelHorizon records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelHorizon)

    def get_model_report_df(self):
        """
        Get table of ModelReport records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelReport)

    def get_model_lt_plan_df(self):
        """
        Get table of ModelLTPlan records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelLTPlan)

    def get_model_pasa_df(self):
        """
        Get table of ModelPASA records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelPASA)

    def get_model_mt_schedule_df(self):
        """
        Get table of ModelMTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelMTSchedule)

    def get_model_st_schedule_df(self):
        """
        Get table of ModelSTSchedule records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelSTSchedule)

    def get_model_transmission_df(self):
        """
        Get table of ModelTransmission records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelTransmission)

    def get_model_production_df(self):
        """
        Get table of ModelProduction records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelProduction)

    def get_model_competition_df(self):
        """
        Get table of ModelCompetition records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelCompetition)

    def get_model_stochastic_df(self):
        """
        Get table of ModelStochastic records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelStochastic)

    def get_model_performance_df(self):
        """
        Get table of ModelPerformance records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelPerformance)

    def get_model_diagnostic_df(self):
        """
        Get table of ModelDiagnostic records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelDiagnostic)

    def get_model_interleaved_df(self):
        """
        Get table of ModelInterleaved records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ModelInterleaved)

    def get_project_models_df(self):
        """
        Get table of ProjectModels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ProjectModels)

    def get_project_horizon_df(self):
        """
        Get table of ProjectHorizon records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ProjectHorizon)

    def get_project_report_df(self):
        """
        Get table of ProjectReport records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ProjectReport)

    def get_list_generators_df(self):
        """
        Get table of ListGenerators records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGenerators)

    def get_list_fuels_df(self):
        """
        Get table of ListFuels records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListFuels)

    def get_list_fuel_contracts_df(self):
        """
        Get table of ListFuelContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListFuelContracts)

    def get_list_emissions_df(self):
        """
        Get table of ListEmissions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListEmissions)

    def get_list_abatements_df(self):
        """
        Get table of ListAbatements records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListAbatements)

    def get_list_storages_df(self):
        """
        Get table of ListStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListStorages)

    def get_list_waterways_df(self):
        """
        Get table of ListWaterways records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterways)

    def get_list_power_stations_df(self):
        """
        Get table of ListPowerStations records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListPowerStations)

    def get_list_physical_contracts_df(self):
        """
        Get table of ListPhysicalContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListPhysicalContracts)

    def get_list_purchasers_df(self):
        """
        Get table of ListPurchasers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListPurchasers)

    def get_list_reserves_df(self):
        """
        Get table of ListReserves records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListReserves)

    def get_list_batteries_df(self):
        """
        Get table of ListBatteries records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListBatteries)

    def get_list_maintenances_df(self):
        """
        Get table of ListMaintenances records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListMaintenances)

    def get_list_heat_plants_df(self):
        """
        Get table of ListHeatPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListHeatPlants)

    def get_list_heat_nodes_df(self):
        """
        Get table of ListHeatNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListHeatNodes)

    def get_list_gas_fields_df(self):
        """
        Get table of ListGasFields records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasFields)

    def get_list_gas_plants_df(self):
        """
        Get table of ListGasPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasPlants)

    def get_list_gas_pipelines_df(self):
        """
        Get table of ListGasPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasPipelines)

    def get_list_gas_nodes_df(self):
        """
        Get table of ListGasNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasNodes)

    def get_list_gas_storages_df(self):
        """
        Get table of ListGasStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasStorages)

    def get_list_gas_demands_df(self):
        """
        Get table of ListGasDemands records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasDemands)

    def get_list_gas_basins_df(self):
        """
        Get table of ListGasBasins records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasBasins)

    def get_list_gas_zones_df(self):
        """
        Get table of ListGasZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasZones)

    def get_list_gas_contracts_df(self):
        """
        Get table of ListGasContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasContracts)

    def get_list_gas_transports_df(self):
        """
        Get table of ListGasTransports records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGasTransports)

    def get_list_water_plants_df(self):
        """
        Get table of ListWaterPlants records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterPlants)

    def get_list_water_pipelines_df(self):
        """
        Get table of ListWaterPipelines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterPipelines)

    def get_list_water_nodes_df(self):
        """
        Get table of ListWaterNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterNodes)

    def get_list_water_storages_df(self):
        """
        Get table of ListWaterStorages records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterStorages)

    def get_list_water_demands_df(self):
        """
        Get table of ListWaterDemands records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterDemands)

    def get_list_water_zones_df(self):
        """
        Get table of ListWaterZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListWaterZones)

    def get_list_regions_df(self):
        """
        Get table of ListRegions records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListRegions)

    def get_list_zones_df(self):
        """
        Get table of ListZones records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListZones)

    def get_list_nodes_df(self):
        """
        Get table of ListNodes records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListNodes)

    def get_list_lines_df(self):
        """
        Get table of ListLines records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListLines)

    def get_list_ml_fs_df(self):
        """
        Get table of ListMLFs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListMLFs)

    def get_list_transformers_df(self):
        """
        Get table of ListTransformers records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListTransformers)

    def get_list_flow_controls_df(self):
        """
        Get table of ListFlowControls records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListFlowControls)

    def get_list_interfaces_df(self):
        """
        Get table of ListInterfaces records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListInterfaces)

    def get_list_contingencies_df(self):
        """
        Get table of ListContingencies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListContingencies)

    def get_list_companies_df(self):
        """
        Get table of ListCompanies records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListCompanies)

    def get_list_financial_contracts_df(self):
        """
        Get table of ListFinancialContracts records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListFinancialContracts)

    def get_list_hubs_df(self):
        """
        Get table of ListHubs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListHubs)

    def get_list_transmission_rights_df(self):
        """
        Get table of ListTransmissionRights records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListTransmissionRights)

    def get_list_cournots_df(self):
        """
        Get table of ListCournots records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListCournots)

    def get_list_rs_is_df(self):
        """
        Get table of ListRSIs records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListRSIs)

    def get_list_markets_df(self):
        """
        Get table of ListMarkets records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListMarkets)

    def get_list_constraints_df(self):
        """
        Get table of ListConstraints records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListConstraints)

    def get_list_decision_variables_df(self):
        """
        Get table of ListDecisionVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListDecisionVariables)

    def get_list_data_files_df(self):
        """
        Get table of ListDataFiles records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListDataFiles)

    def get_list_variables_df(self):
        """
        Get table of ListVariables records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListVariables)

    def get_list_timeslices_df(self):
        """
        Get table of ListTimeslices records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListTimeslices)

    def get_list_globals_df(self):
        """
        Get table of ListGlobals records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListGlobals)

    def get_list_scenarios_df(self):
        """
        Get table of ListScenarios records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListScenarios)

    def get_list_lists_df(self):
        """
        Get table of ListLists records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ListLists)

    def get_report_lists_df(self):
        """
        Get table of ReportLists records
        :return: DataFrame
        """
        return self.get_collection_df(plx_enums.CollectionEnum.ReportLists)



if __name__ == '__main__':

    fname = r'C:\Users\penversa\Git\Python-PLEXOS-API\Input Files\rts3.xml'
    plexos_db = PlexosDatabase(fname)

    gen_df = plexos_db.get_system_generators_df()

    xfo_df = plexos_db.get_system_transformers_df()

    nodes_df = plexos_db.get_system_nodes_df()

    print()
