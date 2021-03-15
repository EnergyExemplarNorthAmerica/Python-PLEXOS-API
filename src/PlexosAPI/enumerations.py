from PlexosAPI.api import plx, plx_enums
from enum import Enum


class t_actionEnums(Enum):
    action_id_col = plx_enums.t_actionEnums.action_id_col

    action_symbol_col = plx_enums.t_actionEnums.action_symbol_col


class t_assemblyEnums(Enum):
    assembly_id_col = plx_enums.t_assemblyEnums.assembly_id_col

    filename_col = plx_enums.t_assemblyEnums.filename_col

    namespace_col = plx_enums.t_assemblyEnums.namespace_col


class t_attributeEnums(Enum):
    attribute_id_col = plx_enums.t_attributeEnums.attribute_id_col

    class_id_col = plx_enums.t_attributeEnums.class_id_col

    enum_id_col = plx_enums.t_attributeEnums.enum_id_col

    name_col = plx_enums.t_attributeEnums.name_col

    unit_id_col = plx_enums.t_attributeEnums.unit_id_col

    default_value_col = plx_enums.t_attributeEnums.default_value_col

    validation_rule_col = plx_enums.t_attributeEnums.validation_rule_col

    input_mask_col = plx_enums.t_attributeEnums.input_mask_col

    is_enabled_col = plx_enums.t_attributeEnums.is_enabled_col

    is_integer_col = plx_enums.t_attributeEnums.is_integer_col

    lang_id_col = plx_enums.t_attributeEnums.lang_id_col

    description_col = plx_enums.t_attributeEnums.description_col


class t_attribute_dataEnums(Enum):
    object_id_col = plx_enums.t_attribute_dataEnums.object_id_col

    attribute_id_col = plx_enums.t_attribute_dataEnums.attribute_id_col

    value_col = plx_enums.t_attribute_dataEnums.value_col


class t_bandEnums(Enum):
    data_id_col = plx_enums.t_bandEnums.data_id_col

    band_id_col = plx_enums.t_bandEnums.band_id_col


class t_categoryEnums(Enum):
    category_id_col = plx_enums.t_categoryEnums.category_id_col

    class_id_col = plx_enums.t_categoryEnums.class_id_col

    rank_col = plx_enums.t_categoryEnums.rank_col

    name_col = plx_enums.t_categoryEnums.name_col


class t_classEnums(Enum):
    class_id_col = plx_enums.t_classEnums.class_id_col

    name_col = plx_enums.t_classEnums.name_col

    class_group_id_col = plx_enums.t_classEnums.class_group_id_col

    is_enabled_col = plx_enums.t_classEnums.is_enabled_col

    lang_id_col = plx_enums.t_classEnums.lang_id_col

    description_col = plx_enums.t_classEnums.description_col

    state_col = plx_enums.t_classEnums.state_col


class t_class_groupEnums(Enum):
    class_group_id_col = plx_enums.t_class_groupEnums.class_group_id_col

    name_col = plx_enums.t_class_groupEnums.name_col

    lang_id_col = plx_enums.t_class_groupEnums.lang_id_col


class t_collectionEnums(Enum):
    collection_id_col = plx_enums.t_collectionEnums.collection_id_col

    parent_class_id_col = plx_enums.t_collectionEnums.parent_class_id_col

    child_class_id_col = plx_enums.t_collectionEnums.child_class_id_col

    name_col = plx_enums.t_collectionEnums.name_col

    min_count_col = plx_enums.t_collectionEnums.min_count_col

    max_count_col = plx_enums.t_collectionEnums.max_count_col

    complement_name_col = plx_enums.t_collectionEnums.complement_name_col

    complement_min_count_col = plx_enums.t_collectionEnums.complement_min_count_col

    complement_max_count_col = plx_enums.t_collectionEnums.complement_max_count_col

    is_enabled_col = plx_enums.t_collectionEnums.is_enabled_col

    lang_id_col = plx_enums.t_collectionEnums.lang_id_col

    description_col = plx_enums.t_collectionEnums.description_col

    complement_description_col = plx_enums.t_collectionEnums.complement_description_col


class t_collection_reportEnums(Enum):
    collection_id_col = plx_enums.t_collection_reportEnums.collection_id_col

    left_collection_id_col = plx_enums.t_collection_reportEnums.left_collection_id_col

    right_collection_id_col = plx_enums.t_collection_reportEnums.right_collection_id_col

    rule_left_collection_id_col = plx_enums.t_collection_reportEnums.rule_left_collection_id_col

    rule_right_collection_id_col = plx_enums.t_collection_reportEnums.rule_right_collection_id_col

    rule_id_col = plx_enums.t_collection_reportEnums.rule_id_col


class t_configEnums(Enum):
    element_col = plx_enums.t_configEnums.element_col

    value_col = plx_enums.t_configEnums.value_col


class t_dataEnums(Enum):
    data_id_col = plx_enums.t_dataEnums.data_id_col

    membership_id_col = plx_enums.t_dataEnums.membership_id_col

    property_id_col = plx_enums.t_dataEnums.property_id_col

    value_col = plx_enums.t_dataEnums.value_col

    collection_id_col = plx_enums.t_dataEnums.collection_id_col

    enum_id_col = plx_enums.t_dataEnums.enum_id_col

    band_id_col = plx_enums.t_dataEnums.band_id_col

    period_type_id_col = plx_enums.t_dataEnums.period_type_id_col

    date_from_col = plx_enums.t_dataEnums.date_from_col

    date_to_col = plx_enums.t_dataEnums.date_to_col

    pattern_col = plx_enums.t_dataEnums.pattern_col

    filename_col = plx_enums.t_dataEnums.filename_col

    variable_id_col = plx_enums.t_dataEnums.variable_id_col

    action_id_col = plx_enums.t_dataEnums.action_id_col

    scenario_id_col = plx_enums.t_dataEnums.scenario_id_col

    source_data_id_col = plx_enums.t_dataEnums.source_data_id_col

    priority_col = plx_enums.t_dataEnums.priority_col

    expression_col = plx_enums.t_dataEnums.expression_col


class t_date_fromEnums(Enum):
    data_id_col = plx_enums.t_date_fromEnums.data_id_col

    date_col = plx_enums.t_date_fromEnums.date_col


class t_date_toEnums(Enum):
    data_id_col = plx_enums.t_date_toEnums.data_id_col

    date_col = plx_enums.t_date_toEnums.date_col


class t_membershipEnums(Enum):
    membership_id_col = plx_enums.t_membershipEnums.membership_id_col

    parent_class_id_col = plx_enums.t_membershipEnums.parent_class_id_col

    parent_object_id_col = plx_enums.t_membershipEnums.parent_object_id_col

    collection_id_col = plx_enums.t_membershipEnums.collection_id_col

    child_class_id_col = plx_enums.t_membershipEnums.child_class_id_col

    child_object_id_col = plx_enums.t_membershipEnums.child_object_id_col

    source_membership_id_col = plx_enums.t_membershipEnums.source_membership_id_col


class t_memo_dataEnums(Enum):
    data_id_col = plx_enums.t_memo_dataEnums.data_id_col

    value_col = plx_enums.t_memo_dataEnums.value_col

    state_col = plx_enums.t_memo_dataEnums.state_col


class t_memo_membershipEnums(Enum):
    membership_id_col = plx_enums.t_memo_membershipEnums.membership_id_col

    value_col = plx_enums.t_memo_membershipEnums.value_col

    state_col = plx_enums.t_memo_membershipEnums.state_col


class t_memo_objectEnums(Enum):
    object_id_col = plx_enums.t_memo_objectEnums.object_id_col

    value_col = plx_enums.t_memo_objectEnums.value_col

    state_col = plx_enums.t_memo_objectEnums.state_col


class t_messageEnums(Enum):
    number_col = plx_enums.t_messageEnums.number_col

    severity_col = plx_enums.t_messageEnums.severity_col

    default_action_col = plx_enums.t_messageEnums.default_action_col

    action_col = plx_enums.t_messageEnums.action_col


class t_objectEnums(Enum):
    object_id_col = plx_enums.t_objectEnums.object_id_col

    class_id_col = plx_enums.t_objectEnums.class_id_col

    name_col = plx_enums.t_objectEnums.name_col

    category_id_col = plx_enums.t_objectEnums.category_id_col

    description_col = plx_enums.t_objectEnums.description_col

    source_object_id_col = plx_enums.t_objectEnums.source_object_id_col

    index_col = plx_enums.t_objectEnums.index_col

    report_col = plx_enums.t_objectEnums.report_col

    filter_by_interval_col = plx_enums.t_objectEnums.filter_by_interval_col

    filter_by_summary_col = plx_enums.t_objectEnums.filter_by_summary_col

    X_col = plx_enums.t_objectEnums.X_col

    Y_col = plx_enums.t_objectEnums.Y_col

    Z_col = plx_enums.t_objectEnums.Z_col


class t_propertyEnums(Enum):
    property_id_col = plx_enums.t_propertyEnums.property_id_col

    collection_id_col = plx_enums.t_propertyEnums.collection_id_col

    property_group_id_col = plx_enums.t_propertyEnums.property_group_id_col

    enum_id_col = plx_enums.t_propertyEnums.enum_id_col

    name_col = plx_enums.t_propertyEnums.name_col

    unit_id_col = plx_enums.t_propertyEnums.unit_id_col

    default_value_col = plx_enums.t_propertyEnums.default_value_col

    validation_rule_col = plx_enums.t_propertyEnums.validation_rule_col

    input_mask_col = plx_enums.t_propertyEnums.input_mask_col

    is_integer_col = plx_enums.t_propertyEnums.is_integer_col

    period_type_id_col = plx_enums.t_propertyEnums.period_type_id_col

    is_key_col = plx_enums.t_propertyEnums.is_key_col

    is_enabled_col = plx_enums.t_propertyEnums.is_enabled_col

    is_dynamic_col = plx_enums.t_propertyEnums.is_dynamic_col

    is_multi_band_col = plx_enums.t_propertyEnums.is_multi_band_col

    max_band_id_col = plx_enums.t_propertyEnums.max_band_id_col

    lang_id_col = plx_enums.t_propertyEnums.lang_id_col

    description_col = plx_enums.t_propertyEnums.description_col

    averaged_in_aggregate_col = plx_enums.t_propertyEnums.averaged_in_aggregate_col

    prorated_in_aggregate_col = plx_enums.t_propertyEnums.prorated_in_aggregate_col


class t_property_groupEnums(Enum):
    property_group_id_col = plx_enums.t_property_groupEnums.property_group_id_col

    name_col = plx_enums.t_property_groupEnums.name_col

    lang_id_col = plx_enums.t_property_groupEnums.lang_id_col


class t_property_reportEnums(Enum):
    property_id_col = plx_enums.t_property_reportEnums.property_id_col

    collection_id_col = plx_enums.t_property_reportEnums.collection_id_col

    property_group_id_col = plx_enums.t_property_reportEnums.property_group_id_col

    enum_id_col = plx_enums.t_property_reportEnums.enum_id_col

    name_col = plx_enums.t_property_reportEnums.name_col

    summary_name_col = plx_enums.t_property_reportEnums.summary_name_col

    unit_id_col = plx_enums.t_property_reportEnums.unit_id_col

    summary_unit_id_col = plx_enums.t_property_reportEnums.summary_unit_id_col

    is_period_col = plx_enums.t_property_reportEnums.is_period_col

    is_summary_col = plx_enums.t_property_reportEnums.is_summary_col

    is_multi_band_col = plx_enums.t_property_reportEnums.is_multi_band_col

    is_quantity_col = plx_enums.t_property_reportEnums.is_quantity_col

    is_LT_col = plx_enums.t_property_reportEnums.is_LT_col

    is_PA_col = plx_enums.t_property_reportEnums.is_PA_col

    is_MT_col = plx_enums.t_property_reportEnums.is_MT_col

    is_ST_col = plx_enums.t_property_reportEnums.is_ST_col

    lang_id_col = plx_enums.t_property_reportEnums.lang_id_col

    summary_lang_id_col = plx_enums.t_property_reportEnums.summary_lang_id_col

    description_col = plx_enums.t_property_reportEnums.description_col


class t_property_tagEnums(Enum):
    tag_id_col = plx_enums.t_property_tagEnums.tag_id_col

    name_col = plx_enums.t_property_tagEnums.name_col


class t_reportEnums(Enum):
    object_id_col = plx_enums.t_reportEnums.object_id_col

    property_id_col = plx_enums.t_reportEnums.property_id_col

    phase_id_col = plx_enums.t_reportEnums.phase_id_col

    report_period_col = plx_enums.t_reportEnums.report_period_col

    report_summary_col = plx_enums.t_reportEnums.report_summary_col

    report_statistics_col = plx_enums.t_reportEnums.report_statistics_col

    report_samples_col = plx_enums.t_reportEnums.report_samples_col

    write_flat_files_col = plx_enums.t_reportEnums.write_flat_files_col


class t_tagEnums(Enum):
    data_id_col = plx_enums.t_tagEnums.data_id_col

    object_id_col = plx_enums.t_tagEnums.object_id_col


class t_textEnums(Enum):
    data_id_col = plx_enums.t_textEnums.data_id_col

    class_id_col = plx_enums.t_textEnums.class_id_col

    value_col = plx_enums.t_textEnums.value_col


class t_unitEnums(Enum):
    unit_id_col = plx_enums.t_unitEnums.unit_id_col

    default_col = plx_enums.t_unitEnums.default_col

    default_imperial_col = plx_enums.t_unitEnums.default_imperial_col

    value_col = plx_enums.t_unitEnums.value_col

    description_col = plx_enums.t_unitEnums.description_col

    lang_id_col = plx_enums.t_unitEnums.lang_id_col


class t_data_0Enums(Enum):
    key_id_col = plx_enums.t_data_0Enums.key_id_col

    period_id_col = plx_enums.t_data_0Enums.period_id_col

    value_col = plx_enums.t_data_0Enums.value_col


class t_data_1Enums(Enum):
    key_id_col = plx_enums.t_data_1Enums.key_id_col

    period_id_col = plx_enums.t_data_1Enums.period_id_col

    value_col = plx_enums.t_data_1Enums.value_col


class t_data_2Enums(Enum):
    key_id_col = plx_enums.t_data_2Enums.key_id_col

    period_id_col = plx_enums.t_data_2Enums.period_id_col

    value_col = plx_enums.t_data_2Enums.value_col


class t_data_3Enums(Enum):
    key_id_col = plx_enums.t_data_3Enums.key_id_col

    period_id_col = plx_enums.t_data_3Enums.period_id_col

    value_col = plx_enums.t_data_3Enums.value_col


class t_data_4Enums(Enum):
    key_id_col = plx_enums.t_data_4Enums.key_id_col

    period_id_col = plx_enums.t_data_4Enums.period_id_col

    value_col = plx_enums.t_data_4Enums.value_col


class t_data_currentEnums(Enum):
    key_id_col = plx_enums.t_data_currentEnums.key_id_col

    period_id_col = plx_enums.t_data_currentEnums.period_id_col

    value_col = plx_enums.t_data_currentEnums.value_col


class t_keyEnums(Enum):
    key_id_col = plx_enums.t_keyEnums.key_id_col

    membership_id_col = plx_enums.t_keyEnums.membership_id_col

    model_id_col = plx_enums.t_keyEnums.model_id_col

    phase_id_col = plx_enums.t_keyEnums.phase_id_col

    property_id_col = plx_enums.t_keyEnums.property_id_col

    period_type_id_col = plx_enums.t_keyEnums.period_type_id_col

    band_id_col = plx_enums.t_keyEnums.band_id_col

    sample_id_col = plx_enums.t_keyEnums.sample_id_col

    timeslice_id_col = plx_enums.t_keyEnums.timeslice_id_col


class t_key_indexEnums(Enum):
    key_id_col = plx_enums.t_key_indexEnums.key_id_col

    period_type_id_col = plx_enums.t_key_indexEnums.period_type_id_col

    position_col = plx_enums.t_key_indexEnums.position_col

    length_col = plx_enums.t_key_indexEnums.length_col

    period_offset_col = plx_enums.t_key_indexEnums.period_offset_col


class t_modelEnums(Enum):
    model_id_col = plx_enums.t_modelEnums.model_id_col

    name_col = plx_enums.t_modelEnums.name_col


class t_period_0Enums(Enum):
    interval_id_col = plx_enums.t_period_0Enums.interval_id_col

    hour_id_col = plx_enums.t_period_0Enums.hour_id_col

    day_id_col = plx_enums.t_period_0Enums.day_id_col

    week_id_col = plx_enums.t_period_0Enums.week_id_col

    month_id_col = plx_enums.t_period_0Enums.month_id_col

    quarter_id_col = plx_enums.t_period_0Enums.quarter_id_col

    fiscal_year_id_col = plx_enums.t_period_0Enums.fiscal_year_id_col

    datetime_col = plx_enums.t_period_0Enums.datetime_col

    period_of_day_col = plx_enums.t_period_0Enums.period_of_day_col


class t_period_1Enums(Enum):
    day_id_col = plx_enums.t_period_1Enums.day_id_col

    date_col = plx_enums.t_period_1Enums.date_col

    week_id_col = plx_enums.t_period_1Enums.week_id_col

    month_id_col = plx_enums.t_period_1Enums.month_id_col

    quarter_id_col = plx_enums.t_period_1Enums.quarter_id_col

    fiscal_year_id_col = plx_enums.t_period_1Enums.fiscal_year_id_col


class t_period_2Enums(Enum):
    week_id_col = plx_enums.t_period_2Enums.week_id_col

    week_ending_col = plx_enums.t_period_2Enums.week_ending_col


class t_period_3Enums(Enum):
    month_id_col = plx_enums.t_period_3Enums.month_id_col

    month_beginning_col = plx_enums.t_period_3Enums.month_beginning_col


class t_period_4Enums(Enum):
    fiscal_year_id_col = plx_enums.t_period_4Enums.fiscal_year_id_col

    year_ending_col = plx_enums.t_period_4Enums.year_ending_col


class t_period_6Enums(Enum):
    hour_id_col = plx_enums.t_period_6Enums.hour_id_col

    day_id_col = plx_enums.t_period_6Enums.day_id_col

    datetime_col = plx_enums.t_period_6Enums.datetime_col


class t_period_7Enums(Enum):
    quarter_id_col = plx_enums.t_period_7Enums.quarter_id_col

    quarter_beginning_col = plx_enums.t_period_7Enums.quarter_beginning_col


class t_phase_1Enums(Enum):
    interval_id_col = plx_enums.t_phase_1Enums.interval_id_col

    period_id_col = plx_enums.t_phase_1Enums.period_id_col


class t_phase_2Enums(Enum):
    interval_id_col = plx_enums.t_phase_2Enums.interval_id_col

    period_id_col = plx_enums.t_phase_2Enums.period_id_col


class t_phase_3Enums(Enum):
    interval_id_col = plx_enums.t_phase_3Enums.interval_id_col

    period_id_col = plx_enums.t_phase_3Enums.period_id_col


class t_phase_4Enums(Enum):
    interval_id_col = plx_enums.t_phase_4Enums.interval_id_col

    period_id_col = plx_enums.t_phase_4Enums.period_id_col


class t_sampleEnums(Enum):
    sample_id_col = plx_enums.t_sampleEnums.sample_id_col


class t_timesliceEnums(Enum):
    timeslice_id_col = plx_enums.t_timesliceEnums.timeslice_id_col

    name_col = plx_enums.t_timesliceEnums.name_col


class AbatementConsumablesEnum(Enum):
    ConsumptionBase = plx_enums.AbatementConsumablesEnum.ConsumptionBase

    ConsumptionIncr = plx_enums.AbatementConsumablesEnum.ConsumptionIncr


class AbatementEmissionsEnum(Enum):
    AbatementCost = plx_enums.AbatementEmissionsEnum.AbatementCost

    Efficiency = plx_enums.AbatementEmissionsEnum.Efficiency

    MaxAbatement = plx_enums.AbatementEmissionsEnum.MaxAbatement


class AbatementGeneratorsEnum(Enum):
    GenerationParticipationFactor = plx_enums.AbatementGeneratorsEnum.GenerationParticipationFactor


class ActionEnum(Enum):
    Equal = plx_enums.ActionEnum.Equal

    Multiply = plx_enums.ActionEnum.Multiply

    Divide = plx_enums.ActionEnum.Divide

    Add = plx_enums.ActionEnum.Add

    Subtract = plx_enums.ActionEnum.Subtract

    RaisetoPower = plx_enums.ActionEnum.RaisetoPower

    Test = plx_enums.ActionEnum.Test


class AggregationEnum(Enum):
    None_ = 0

    Category = plx_enums.AggregationEnum.Category

    All = plx_enums.AggregationEnum.All


class AncillaryServicesCostAllocationModelEnum(Enum):
    None_ = 0

    Runway = plx_enums.AncillaryServicesCostAllocationModelEnum.Runway

    ModifiedRunway = plx_enums.AncillaryServicesCostAllocationModelEnum.ModifiedRunway

    Prorata = plx_enums.AncillaryServicesCostAllocationModelEnum.Prorata


class AttributeIDEnum(Enum):
    Generator_Latitude = plx_enums.AttributeIDEnum.Generator_Latitude

    Generator_Longitude = plx_enums.AttributeIDEnum.Generator_Longitude

    Storage_Latitude = plx_enums.AttributeIDEnum.Storage_Latitude

    Storage_Longitude = plx_enums.AttributeIDEnum.Storage_Longitude

    Node_Latitude = plx_enums.AttributeIDEnum.Node_Latitude

    Node_Longitude = plx_enums.AttributeIDEnum.Node_Longitude

    Battery_Latitude = plx_enums.AttributeIDEnum.Battery_Latitude

    Battery_Longitude = plx_enums.AttributeIDEnum.Battery_Longitude

    GasStorage_Latitude = plx_enums.AttributeIDEnum.GasStorage_Latitude

    GasStorage_Longitude = plx_enums.AttributeIDEnum.GasStorage_Longitude

    GasNode_Latitude = plx_enums.AttributeIDEnum.GasNode_Latitude

    GasNode_Longitude = plx_enums.AttributeIDEnum.GasNode_Longitude

    WaterStorage_Latitude = plx_enums.AttributeIDEnum.WaterStorage_Latitude

    WaterStorage_Longitude = plx_enums.AttributeIDEnum.WaterStorage_Longitude

    WaterNode_Latitude = plx_enums.AttributeIDEnum.WaterNode_Latitude

    WaterNode_Longitude = plx_enums.AttributeIDEnum.WaterNode_Longitude

    Market_UnitCommitment = plx_enums.AttributeIDEnum.Market_UnitCommitment

    DecisionVariable_Type = plx_enums.AttributeIDEnum.DecisionVariable_Type

    DecisionVariable_TimeLag = plx_enums.AttributeIDEnum.DecisionVariable_TimeLag

    DecisionVariable_TimeInvariant = plx_enums.AttributeIDEnum.DecisionVariable_TimeInvariant

    List_Report = plx_enums.AttributeIDEnum.List_Report

    List_Filter = plx_enums.AttributeIDEnum.List_Filter

    List_InclusiveEmpty = plx_enums.AttributeIDEnum.List_InclusiveEmpty

    List_Transient = plx_enums.AttributeIDEnum.List_Transient

    DataFile_Enabled = plx_enums.AttributeIDEnum.DataFile_Enabled

    DataFile_GrowthPeriod = plx_enums.AttributeIDEnum.DataFile_GrowthPeriod

    DataFile_Method = plx_enums.AttributeIDEnum.DataFile_Method

    DataFile_RelativeGrowthatMin = plx_enums.AttributeIDEnum.DataFile_RelativeGrowthatMin

    DataFile_ShapeDistortion = plx_enums.AttributeIDEnum.DataFile_ShapeDistortion

    DataFile_DecimalPlaces = plx_enums.AttributeIDEnum.DataFile_DecimalPlaces

    DataFile_MissingValueMethod = plx_enums.AttributeIDEnum.DataFile_MissingValueMethod

    DataFile_PeriodsperDay = plx_enums.AttributeIDEnum.DataFile_PeriodsperDay

    DataFile_UpscalingMethod = plx_enums.AttributeIDEnum.DataFile_UpscalingMethod

    DataFile_DownscalingMethod = plx_enums.AttributeIDEnum.DataFile_DownscalingMethod

    DataFile_DatetimeConvention = plx_enums.AttributeIDEnum.DataFile_DatetimeConvention

    DataFile_Locale = plx_enums.AttributeIDEnum.DataFile_Locale

    DataFile_TimeShift = plx_enums.AttributeIDEnum.DataFile_TimeShift

    DataFile_WeekBeginning = plx_enums.AttributeIDEnum.DataFile_WeekBeginning

    DataFile_HistoricalSampling = plx_enums.AttributeIDEnum.DataFile_HistoricalSampling

    DataFile_HistoricalYearFrom = plx_enums.AttributeIDEnum.DataFile_HistoricalYearFrom

    DataFile_HistoricalYearTo = plx_enums.AttributeIDEnum.DataFile_HistoricalYearTo

    DataFile_HistoricalYearStart = plx_enums.AttributeIDEnum.DataFile_HistoricalYearStart

    DataFile_HistoricalYearEnding = plx_enums.AttributeIDEnum.DataFile_HistoricalYearEnding

    DataFile_HistoricalPeriodType = plx_enums.AttributeIDEnum.DataFile_HistoricalPeriodType

    DataFile_BaseYear = plx_enums.AttributeIDEnum.DataFile_BaseYear

    Variable_CompoundType = plx_enums.AttributeIDEnum.Variable_CompoundType

    Variable_CompoundStartDate = plx_enums.AttributeIDEnum.Variable_CompoundStartDate

    Horizon_PeriodsperDay = plx_enums.AttributeIDEnum.Horizon_PeriodsperDay

    Horizon_DateFrom = plx_enums.AttributeIDEnum.Horizon_DateFrom

    Horizon_StepType = plx_enums.AttributeIDEnum.Horizon_StepType

    Horizon_StepCount = plx_enums.AttributeIDEnum.Horizon_StepCount

    Horizon_DayBeginning = plx_enums.AttributeIDEnum.Horizon_DayBeginning

    Horizon_WeekBeginning = plx_enums.AttributeIDEnum.Horizon_WeekBeginning

    Horizon_YearEnding = plx_enums.AttributeIDEnum.Horizon_YearEnding

    Horizon_Chronology = plx_enums.AttributeIDEnum.Horizon_Chronology

    Horizon_TypicalWeek = plx_enums.AttributeIDEnum.Horizon_TypicalWeek

    Horizon_ChronoDateFrom = plx_enums.AttributeIDEnum.Horizon_ChronoDateFrom

    Horizon_ChronoPeriodFrom = plx_enums.AttributeIDEnum.Horizon_ChronoPeriodFrom

    Horizon_ChronoPeriodTo = plx_enums.AttributeIDEnum.Horizon_ChronoPeriodTo

    Horizon_ChronoStepType = plx_enums.AttributeIDEnum.Horizon_ChronoStepType

    Horizon_ChronoAtaTime = plx_enums.AttributeIDEnum.Horizon_ChronoAtaTime

    Horizon_ChronoStepCount = plx_enums.AttributeIDEnum.Horizon_ChronoStepCount

    Horizon_LookaheadIndicator = plx_enums.AttributeIDEnum.Horizon_LookaheadIndicator

    Horizon_LookaheadType = plx_enums.AttributeIDEnum.Horizon_LookaheadType

    Horizon_LookaheadAtaTime = plx_enums.AttributeIDEnum.Horizon_LookaheadAtaTime

    Horizon_LookaheadPeriodsperDay = plx_enums.AttributeIDEnum.Horizon_LookaheadPeriodsperDay

    Report_WriteDatabase = plx_enums.AttributeIDEnum.Report_WriteDatabase

    Report_WriteFlatFiles = plx_enums.AttributeIDEnum.Report_WriteFlatFiles

    Report_WriteXMLFiles = plx_enums.AttributeIDEnum.Report_WriteXMLFiles

    Report_XMLContent = plx_enums.AttributeIDEnum.Report_XMLContent

    Report_OutputResultsbyPeriod = plx_enums.AttributeIDEnum.Report_OutputResultsbyPeriod

    Report_OutputResultsbyHour = plx_enums.AttributeIDEnum.Report_OutputResultsbyHour

    Report_OutputResultsbyDay = plx_enums.AttributeIDEnum.Report_OutputResultsbyDay

    Report_OutputResultsbyWeek = plx_enums.AttributeIDEnum.Report_OutputResultsbyWeek

    Report_OutputResultsbyMonth = plx_enums.AttributeIDEnum.Report_OutputResultsbyMonth

    Report_OutputResultsbyQuarter = plx_enums.AttributeIDEnum.Report_OutputResultsbyQuarter

    Report_OutputResultsbyFiscalYear = plx_enums.AttributeIDEnum.Report_OutputResultsbyFiscalYear

    Report_OutputStatistics = plx_enums.AttributeIDEnum.Report_OutputStatistics

    Report_OutputResultsbySample = plx_enums.AttributeIDEnum.Report_OutputResultsbySample

    Report_FilterObjectsByInterval = plx_enums.AttributeIDEnum.Report_FilterObjectsByInterval

    Report_FilterObjectsInSummary = plx_enums.AttributeIDEnum.Report_FilterObjectsInSummary

    Report_WholeYearsOnly = plx_enums.AttributeIDEnum.Report_WholeYearsOnly

    Report_DatetimeConvention = plx_enums.AttributeIDEnum.Report_DatetimeConvention

    Report_Locale = plx_enums.AttributeIDEnum.Report_Locale

    Report_FlatFileFormat = plx_enums.AttributeIDEnum.Report_FlatFileFormat

    Model_Enabled = plx_enums.AttributeIDEnum.Model_Enabled

    Model_ExecutionOrder = plx_enums.AttributeIDEnum.Model_ExecutionOrder

    Model_RandomNumberSeed = plx_enums.AttributeIDEnum.Model_RandomNumberSeed

    Model_OutputtoFolder = plx_enums.AttributeIDEnum.Model_OutputtoFolder

    Model_MakeUniqueName = plx_enums.AttributeIDEnum.Model_MakeUniqueName

    Model_WriteInput = plx_enums.AttributeIDEnum.Model_WriteInput

    Model_LoadCustomAssemblies = plx_enums.AttributeIDEnum.Model_LoadCustomAssemblies

    Model_RunMode = plx_enums.AttributeIDEnum.Model_RunMode

    LTPlan_DiscountRate = plx_enums.AttributeIDEnum.LTPlan_DiscountRate

    LTPlan_DiscountPeriodType = plx_enums.AttributeIDEnum.LTPlan_DiscountPeriodType

    LTPlan_AtaTime = plx_enums.AttributeIDEnum.LTPlan_AtaTime

    LTPlan_Overlap = plx_enums.AttributeIDEnum.LTPlan_Overlap

    LTPlan_Chronology = plx_enums.AttributeIDEnum.LTPlan_Chronology

    LTPlan_LDCType = plx_enums.AttributeIDEnum.LTPlan_LDCType

    LTPlan_BlockCount = plx_enums.AttributeIDEnum.LTPlan_BlockCount

    LTPlan_LastBlockCount = plx_enums.AttributeIDEnum.LTPlan_LastBlockCount

    LTPlan_LDCSlicingMethod = plx_enums.AttributeIDEnum.LTPlan_LDCSlicingMethod

    LTPlan_LDCWeighta = plx_enums.AttributeIDEnum.LTPlan_LDCWeighta

    LTPlan_LDCWeightb = plx_enums.AttributeIDEnum.LTPlan_LDCWeightb

    LTPlan_LDCWeightc = plx_enums.AttributeIDEnum.LTPlan_LDCWeightc

    LTPlan_LDCWeightd = plx_enums.AttributeIDEnum.LTPlan_LDCWeightd

    LTPlan_LDCPinTop = plx_enums.AttributeIDEnum.LTPlan_LDCPinTop

    LTPlan_LDCPinBottom = plx_enums.AttributeIDEnum.LTPlan_LDCPinBottom

    LTPlan_SampleType = plx_enums.AttributeIDEnum.LTPlan_SampleType

    LTPlan_SamplingInterval = plx_enums.AttributeIDEnum.LTPlan_SamplingInterval

    LTPlan_ReducedSampleCount = plx_enums.AttributeIDEnum.LTPlan_ReducedSampleCount

    LTPlan_ReductionRelativeAccuracy = plx_enums.AttributeIDEnum.LTPlan_ReductionRelativeAccuracy

    LTPlan_Optimality = plx_enums.AttributeIDEnum.LTPlan_Optimality

    LTPlan_IntegerizationHorizon = plx_enums.AttributeIDEnum.LTPlan_IntegerizationHorizon

    LTPlan_EndEffectsMethod = plx_enums.AttributeIDEnum.LTPlan_EndEffectsMethod

    LTPlan_SolutionCount = plx_enums.AttributeIDEnum.LTPlan_SolutionCount

    LTPlan_SolutionQuality = plx_enums.AttributeIDEnum.LTPlan_SolutionQuality

    LTPlan_AlwaysAnnualizeBuildCost = plx_enums.AttributeIDEnum.LTPlan_AlwaysAnnualizeBuildCost

    LTPlan_DepreciationMethod = plx_enums.AttributeIDEnum.LTPlan_DepreciationMethod

    LTPlan_TaxRate = plx_enums.AttributeIDEnum.LTPlan_TaxRate

    LTPlan_InflationRate = plx_enums.AttributeIDEnum.LTPlan_InflationRate

    LTPlan_HeatRateDetail = plx_enums.AttributeIDEnum.LTPlan_HeatRateDetail

    LTPlan_OutageIncrement = plx_enums.AttributeIDEnum.LTPlan_OutageIncrement

    LTPlan_UseEffectiveLoadApproach = plx_enums.AttributeIDEnum.LTPlan_UseEffectiveLoadApproach

    LTPlan_MaintenanceSculpting = plx_enums.AttributeIDEnum.LTPlan_MaintenanceSculpting

    LTPlan_PricingMethod = plx_enums.AttributeIDEnum.LTPlan_PricingMethod

    LTPlan_TransmissionDetail = plx_enums.AttributeIDEnum.LTPlan_TransmissionDetail

    LTPlan_AllowCapacitySharing = plx_enums.AttributeIDEnum.LTPlan_AllowCapacitySharing

    LTPlan_CapacityPaymentsEnabled = plx_enums.AttributeIDEnum.LTPlan_CapacityPaymentsEnabled

    LTPlan_StartCostAmortizationPeriod = plx_enums.AttributeIDEnum.LTPlan_StartCostAmortizationPeriod

    LTPlan_ComputeReliabilityIndices = plx_enums.AttributeIDEnum.LTPlan_ComputeReliabilityIndices

    LTPlan_ComputeMultiareaReliabilityIndices = plx_enums.AttributeIDEnum.LTPlan_ComputeMultiareaReliabilityIndices

    LTPlan_StochasticMethod = plx_enums.AttributeIDEnum.LTPlan_StochasticMethod

    LTPlan_WriteExpansionPlanTextFiles = plx_enums.AttributeIDEnum.LTPlan_WriteExpansionPlanTextFiles

    PASA_StepType = plx_enums.AttributeIDEnum.PASA_StepType

    PASA_TransmissionDetail = plx_enums.AttributeIDEnum.PASA_TransmissionDetail

    PASA_IncludeDSP = plx_enums.AttributeIDEnum.PASA_IncludeDSP

    PASA_IncludeDemandBids = plx_enums.AttributeIDEnum.PASA_IncludeDemandBids

    PASA_IncludeContractGeneration = plx_enums.AttributeIDEnum.PASA_IncludeContractGeneration

    PASA_IncludeContractLoad = plx_enums.AttributeIDEnum.PASA_IncludeContractLoad

    PASA_IncludeMarketPurchases = plx_enums.AttributeIDEnum.PASA_IncludeMarketPurchases

    PASA_ConstraintsEnabled = plx_enums.AttributeIDEnum.PASA_ConstraintsEnabled

    PASA_InterfaceConstraintsEnabled = plx_enums.AttributeIDEnum.PASA_InterfaceConstraintsEnabled

    PASA_MaintenanceSculpting = plx_enums.AttributeIDEnum.PASA_MaintenanceSculpting

    PASA_ComputeReliabilityIndices = plx_enums.AttributeIDEnum.PASA_ComputeReliabilityIndices

    PASA_ComputeMultiareaReliabilityIndices = plx_enums.AttributeIDEnum.PASA_ComputeMultiareaReliabilityIndices

    PASA_WriteOutageTextFiles = plx_enums.AttributeIDEnum.PASA_WriteOutageTextFiles

    PASA_StochasticMethod = plx_enums.AttributeIDEnum.PASA_StochasticMethod

    MTSchedule_DiscountRate = plx_enums.AttributeIDEnum.MTSchedule_DiscountRate

    MTSchedule_DiscountPeriodType = plx_enums.AttributeIDEnum.MTSchedule_DiscountPeriodType

    MTSchedule_EndEffectsMethod = plx_enums.AttributeIDEnum.MTSchedule_EndEffectsMethod

    MTSchedule_StepType = plx_enums.AttributeIDEnum.MTSchedule_StepType

    MTSchedule_AtaTime = plx_enums.AttributeIDEnum.MTSchedule_AtaTime

    MTSchedule_Chronology = plx_enums.AttributeIDEnum.MTSchedule_Chronology

    MTSchedule_LDCType = plx_enums.AttributeIDEnum.MTSchedule_LDCType

    MTSchedule_BlockCount = plx_enums.AttributeIDEnum.MTSchedule_BlockCount

    MTSchedule_LastBlockCount = plx_enums.AttributeIDEnum.MTSchedule_LastBlockCount

    MTSchedule_LDCSlicingMethod = plx_enums.AttributeIDEnum.MTSchedule_LDCSlicingMethod

    MTSchedule_LDCWeighta = plx_enums.AttributeIDEnum.MTSchedule_LDCWeighta

    MTSchedule_LDCWeightb = plx_enums.AttributeIDEnum.MTSchedule_LDCWeightb

    MTSchedule_LDCWeightc = plx_enums.AttributeIDEnum.MTSchedule_LDCWeightc

    MTSchedule_LDCWeightd = plx_enums.AttributeIDEnum.MTSchedule_LDCWeightd

    MTSchedule_LDCPinTop = plx_enums.AttributeIDEnum.MTSchedule_LDCPinTop

    MTSchedule_LDCPinBottom = plx_enums.AttributeIDEnum.MTSchedule_LDCPinBottom

    MTSchedule_SampleType = plx_enums.AttributeIDEnum.MTSchedule_SampleType

    MTSchedule_SamplingInterval = plx_enums.AttributeIDEnum.MTSchedule_SamplingInterval

    MTSchedule_ReducedSampleCount = plx_enums.AttributeIDEnum.MTSchedule_ReducedSampleCount

    MTSchedule_ReductionRelativeAccuracy = plx_enums.AttributeIDEnum.MTSchedule_ReductionRelativeAccuracy

    MTSchedule_HeatRateDetail = plx_enums.AttributeIDEnum.MTSchedule_HeatRateDetail

    MTSchedule_UseEffectiveLoadApproach = plx_enums.AttributeIDEnum.MTSchedule_UseEffectiveLoadApproach

    MTSchedule_OutageIncrement = plx_enums.AttributeIDEnum.MTSchedule_OutageIncrement

    MTSchedule_PricingMethod = plx_enums.AttributeIDEnum.MTSchedule_PricingMethod

    MTSchedule_TransmissionDetail = plx_enums.AttributeIDEnum.MTSchedule_TransmissionDetail

    MTSchedule_NewEntryDriver = plx_enums.AttributeIDEnum.MTSchedule_NewEntryDriver

    MTSchedule_NewEntryCapacityMechanism = plx_enums.AttributeIDEnum.MTSchedule_NewEntryCapacityMechanism

    MTSchedule_NewEntryTimeLag = plx_enums.AttributeIDEnum.MTSchedule_NewEntryTimeLag

    MTSchedule_StartCostAmortizationPeriod = plx_enums.AttributeIDEnum.MTSchedule_StartCostAmortizationPeriod

    MTSchedule_StochasticMethod = plx_enums.AttributeIDEnum.MTSchedule_StochasticMethod

    MTSchedule_WriteBridgeTextFiles = plx_enums.AttributeIDEnum.MTSchedule_WriteBridgeTextFiles

    STSchedule_DiscountRate = plx_enums.AttributeIDEnum.STSchedule_DiscountRate

    STSchedule_DiscountPeriodType = plx_enums.AttributeIDEnum.STSchedule_DiscountPeriodType

    STSchedule_EndEffectsMethod = plx_enums.AttributeIDEnum.STSchedule_EndEffectsMethod

    STSchedule_HeatRateDetail = plx_enums.AttributeIDEnum.STSchedule_HeatRateDetail

    STSchedule_TransmissionDetail = plx_enums.AttributeIDEnum.STSchedule_TransmissionDetail

    STSchedule_StochasticMethod = plx_enums.AttributeIDEnum.STSchedule_StochasticMethod

    Transmission_MVABase = plx_enums.AttributeIDEnum.Transmission_MVABase

    Transmission_OPFMethod = plx_enums.AttributeIDEnum.Transmission_OPFMethod

    Transmission_ConstraintsEnabled = plx_enums.AttributeIDEnum.Transmission_ConstraintsEnabled

    Transmission_FormulateUpfront = plx_enums.AttributeIDEnum.Transmission_FormulateUpfront

    Transmission_ConstraintVoltageThreshold = plx_enums.AttributeIDEnum.Transmission_ConstraintVoltageThreshold

    Transmission_InterfaceConstraintsEnabled = plx_enums.AttributeIDEnum.Transmission_InterfaceConstraintsEnabled

    Transmission_EnforceLimitsOnLinesInInterfaces = plx_enums.AttributeIDEnum.Transmission_EnforceLimitsOnLinesInInterfaces

    Transmission_LossesEnabled = plx_enums.AttributeIDEnum.Transmission_LossesEnabled

    Transmission_LossVoltageThreshold = plx_enums.AttributeIDEnum.Transmission_LossVoltageThreshold

    Transmission_LossMethod = plx_enums.AttributeIDEnum.Transmission_LossMethod

    Transmission_MaxLossRelativeError = plx_enums.AttributeIDEnum.Transmission_MaxLossRelativeError

    Transmission_MaxLossAbsoluteError = plx_enums.AttributeIDEnum.Transmission_MaxLossAbsoluteError

    Transmission_MaxLossTranches = plx_enums.AttributeIDEnum.Transmission_MaxLossTranches

    Transmission_LossTolerance = plx_enums.AttributeIDEnum.Transmission_LossTolerance

    Transmission_MaxLossIterations = plx_enums.AttributeIDEnum.Transmission_MaxLossIterations

    Transmission_MaxEmbeddedLossIterations = plx_enums.AttributeIDEnum.Transmission_MaxEmbeddedLossIterations

    Transmission_DetectNonphysicalLosses = plx_enums.AttributeIDEnum.Transmission_DetectNonphysicalLosses

    Transmission_PTDFMethod = plx_enums.AttributeIDEnum.Transmission_PTDFMethod

    Transmission_FlowPTDFThreshold = plx_enums.AttributeIDEnum.Transmission_FlowPTDFThreshold

    Transmission_WheelingPTDFThreshold = plx_enums.AttributeIDEnum.Transmission_WheelingPTDFThreshold

    Transmission_CacheTransmissionMatrices = plx_enums.AttributeIDEnum.Transmission_CacheTransmissionMatrices

    Transmission_ReactanceCutoff = plx_enums.AttributeIDEnum.Transmission_ReactanceCutoff

    Transmission_AllowDumpEnergy = plx_enums.AttributeIDEnum.Transmission_AllowDumpEnergy

    Transmission_AllowUnservedEnergy = plx_enums.AttributeIDEnum.Transmission_AllowUnservedEnergy

    Transmission_BoundNodePhaseAngles = plx_enums.AttributeIDEnum.Transmission_BoundNodePhaseAngles

    Transmission_MaxAbsolutePhaseAngle = plx_enums.AttributeIDEnum.Transmission_MaxAbsolutePhaseAngle

    Transmission_InternalVoLL = plx_enums.AttributeIDEnum.Transmission_InternalVoLL

    Transmission_USEThreshold = plx_enums.AttributeIDEnum.Transmission_USEThreshold

    Transmission_RentalMethod = plx_enums.AttributeIDEnum.Transmission_RentalMethod

    Transmission_InterruptionSharing = plx_enums.AttributeIDEnum.Transmission_InterruptionSharing

    Transmission_ReportEnabled = plx_enums.AttributeIDEnum.Transmission_ReportEnabled

    Transmission_ReportVoltageThreshold = plx_enums.AttributeIDEnum.Transmission_ReportVoltageThreshold

    Transmission_ReportLinesInInterfaces = plx_enums.AttributeIDEnum.Transmission_ReportLinesInInterfaces

    Transmission_ReportAllInterregionalFlows = plx_enums.AttributeIDEnum.Transmission_ReportAllInterregionalFlows

    Transmission_ReportAllInterzonalFlows = plx_enums.AttributeIDEnum.Transmission_ReportAllInterzonalFlows

    Transmission_ReportInjectionandLoadNodes = plx_enums.AttributeIDEnum.Transmission_ReportInjectionandLoadNodes

    Transmission_ConvergenceReportLevel = plx_enums.AttributeIDEnum.Transmission_ConvergenceReportLevel

    Transmission_SCUCEnabled = plx_enums.AttributeIDEnum.Transmission_SCUCEnabled

    Transmission_SCUCConstraintVoltageThreshold = plx_enums.AttributeIDEnum.Transmission_SCUCConstraintVoltageThreshold

    Transmission_SCUCInterfaceConstraintsEnabled = plx_enums.AttributeIDEnum.Transmission_SCUCInterfaceConstraintsEnabled

    Transmission_EnforceN1Contingencies = plx_enums.AttributeIDEnum.Transmission_EnforceN1Contingencies

    Transmission_N1ContingencyVoltageThreshold = plx_enums.AttributeIDEnum.Transmission_N1ContingencyVoltageThreshold

    Transmission_ContingencyMonitoringThreshold = plx_enums.AttributeIDEnum.Transmission_ContingencyMonitoringThreshold

    Transmission_LimitThreshold = plx_enums.AttributeIDEnum.Transmission_LimitThreshold

    Transmission_LimitBootstrapInitialThreshold = plx_enums.AttributeIDEnum.Transmission_LimitBootstrapInitialThreshold

    Transmission_LimitBootstrapThresholdDecrement = plx_enums.AttributeIDEnum.Transmission_LimitBootstrapThresholdDecrement

    Transmission_MaxLimitIterations = plx_enums.AttributeIDEnum.Transmission_MaxLimitIterations

    Transmission_NetworkReduction = plx_enums.AttributeIDEnum.Transmission_NetworkReduction

    Production_DispatchbyPowerStation = plx_enums.AttributeIDEnum.Production_DispatchbyPowerStation

    Production_UnitCommitmentOptimality = plx_enums.AttributeIDEnum.Production_UnitCommitmentOptimality

    Production_RoundingUpThreshold = plx_enums.AttributeIDEnum.Production_RoundingUpThreshold

    Production_RoundedRelaxationCommitmentModel = plx_enums.AttributeIDEnum.Production_RoundedRelaxationCommitmentModel

    Production_RoundedRelaxationTuning = plx_enums.AttributeIDEnum.Production_RoundedRelaxationTuning

    Production_RoundedRelaxationStartThreshold = plx_enums.AttributeIDEnum.Production_RoundedRelaxationStartThreshold

    Production_RoundedRelaxationEndThreshold = plx_enums.AttributeIDEnum.Production_RoundedRelaxationEndThreshold

    Production_RoundedRelaxationThresholdIncrement = plx_enums.AttributeIDEnum.Production_RoundedRelaxationThresholdIncrement

    Production_DPCapacityFactorThreshold = plx_enums.AttributeIDEnum.Production_DPCapacityFactorThreshold

    Production_DPCapacityFactorErrorThreshold = plx_enums.AttributeIDEnum.Production_DPCapacityFactorErrorThreshold

    Production_FuelUseFunctionPrecision = plx_enums.AttributeIDEnum.Production_FuelUseFunctionPrecision

    Production_MaxHeatRateTranches = plx_enums.AttributeIDEnum.Production_MaxHeatRateTranches

    Production_HeatRateErrorMethod = plx_enums.AttributeIDEnum.Production_HeatRateErrorMethod

    Production_StartCostMethod = plx_enums.AttributeIDEnum.Production_StartCostMethod

    Production_CapacityFactorConstraintBasis = plx_enums.AttributeIDEnum.Production_CapacityFactorConstraintBasis

    Production_FormulateUpfront = plx_enums.AttributeIDEnum.Production_FormulateUpfront

    Production_FormulateRampUpfront = plx_enums.AttributeIDEnum.Production_FormulateRampUpfront

    Production_IntegersinLookahead = plx_enums.AttributeIDEnum.Production_IntegersinLookahead

    Production_ForcedOutageRelaxesMinDownTime = plx_enums.AttributeIDEnum.Production_ForcedOutageRelaxesMinDownTime

    Production_PumpandGenerate = plx_enums.AttributeIDEnum.Production_PumpandGenerate

    Competition_EquilibriumModel = plx_enums.AttributeIDEnum.Competition_EquilibriumModel

    Competition_DefaultElasticity = plx_enums.AttributeIDEnum.Competition_DefaultElasticity

    Competition_DemandScaling = plx_enums.AttributeIDEnum.Competition_DemandScaling

    Competition_RevenueTargetingMethod = plx_enums.AttributeIDEnum.Competition_RevenueTargetingMethod

    Competition_RevenueTargetingIterations = plx_enums.AttributeIDEnum.Competition_RevenueTargetingIterations

    Competition_PricingStrategy = plx_enums.AttributeIDEnum.Competition_PricingStrategy

    Competition_BertrandDetectActiveRampConstraints = plx_enums.AttributeIDEnum.Competition_BertrandDetectActiveRampConstraints

    Competition_BertrandOOMODEnabled = plx_enums.AttributeIDEnum.Competition_BertrandOOMODEnabled

    Competition_Epsilon = plx_enums.AttributeIDEnum.Competition_Epsilon

    Competition_RSIEnabled = plx_enums.AttributeIDEnum.Competition_RSIEnabled

    Competition_RSIBidCostMarkupMethod = plx_enums.AttributeIDEnum.Competition_RSIBidCostMarkupMethod

    Competition_NoLoadCostMarkup = plx_enums.AttributeIDEnum.Competition_NoLoadCostMarkup

    Competition_MarkupMinStableLevel = plx_enums.AttributeIDEnum.Competition_MarkupMinStableLevel

    Competition_StartCostMarkup = plx_enums.AttributeIDEnum.Competition_StartCostMarkup

    Competition_StartCostMarkupProductionBands = plx_enums.AttributeIDEnum.Competition_StartCostMarkupProductionBands

    Competition_StartCostMarkupWindow = plx_enums.AttributeIDEnum.Competition_StartCostMarkupWindow

    Competition_ContractsOptimizeOffers = plx_enums.AttributeIDEnum.Competition_ContractsOptimizeOffers

    Competition_ContractsSettlementMethod = plx_enums.AttributeIDEnum.Competition_ContractsSettlementMethod

    Competition_ContractsHandoffPoint = plx_enums.AttributeIDEnum.Competition_ContractsHandoffPoint

    Competition_MarketTradingFormat = plx_enums.AttributeIDEnum.Competition_MarketTradingFormat

    Stochastic_OutagePatternCount = plx_enums.AttributeIDEnum.Stochastic_OutagePatternCount

    Stochastic_MonteCarloMethod = plx_enums.AttributeIDEnum.Stochastic_MonteCarloMethod

    Stochastic_WeibullShape = plx_enums.AttributeIDEnum.Stochastic_WeibullShape

    Stochastic_ConvergentSmoothing = plx_enums.AttributeIDEnum.Stochastic_ConvergentSmoothing

    Stochastic_OutageScope = plx_enums.AttributeIDEnum.Stochastic_OutageScope

    Stochastic_ConvergencePeriodType = plx_enums.AttributeIDEnum.Stochastic_ConvergencePeriodType

    Stochastic_RiskSampleCount = plx_enums.AttributeIDEnum.Stochastic_RiskSampleCount

    Stochastic_ReducedOutagePatternCount = plx_enums.AttributeIDEnum.Stochastic_ReducedOutagePatternCount

    Stochastic_ReducedSampleCount = plx_enums.AttributeIDEnum.Stochastic_ReducedSampleCount

    Stochastic_ReductionRelativeAccuracy = plx_enums.AttributeIDEnum.Stochastic_ReductionRelativeAccuracy

    Stochastic_ForcedOutagesinLookahead = plx_enums.AttributeIDEnum.Stochastic_ForcedOutagesinLookahead

    Stochastic_EFORMaintenanceAdjust = plx_enums.AttributeIDEnum.Stochastic_EFORMaintenanceAdjust

    Scenario_ReadOrder = plx_enums.AttributeIDEnum.Scenario_ReadOrder

    Scenario_Locked = plx_enums.AttributeIDEnum.Scenario_Locked

    Performance_SOLVER = plx_enums.AttributeIDEnum.Performance_SOLVER

    Performance_SmallLPOptimizer = plx_enums.AttributeIDEnum.Performance_SmallLPOptimizer

    Performance_SmallLPNonzeroCount = plx_enums.AttributeIDEnum.Performance_SmallLPNonzeroCount

    Performance_ColdStartOptimizer1 = plx_enums.AttributeIDEnum.Performance_ColdStartOptimizer1

    Performance_ColdStartOptimizer2 = plx_enums.AttributeIDEnum.Performance_ColdStartOptimizer2

    Performance_ColdStartOptimizer3 = plx_enums.AttributeIDEnum.Performance_ColdStartOptimizer3

    Performance_HotStartOptimizer1 = plx_enums.AttributeIDEnum.Performance_HotStartOptimizer1

    Performance_HotStartOptimizer2 = plx_enums.AttributeIDEnum.Performance_HotStartOptimizer2

    Performance_HotStartOptimizer3 = plx_enums.AttributeIDEnum.Performance_HotStartOptimizer3

    Performance_MaximumThreads = plx_enums.AttributeIDEnum.Performance_MaximumThreads

    Performance_MIPRootOptimizer = plx_enums.AttributeIDEnum.Performance_MIPRootOptimizer

    Performance_MIPNodeOptimizer = plx_enums.AttributeIDEnum.Performance_MIPNodeOptimizer

    Performance_SmallMIPRelativeGap = plx_enums.AttributeIDEnum.Performance_SmallMIPRelativeGap

    Performance_SmallMIPImproveStartGap = plx_enums.AttributeIDEnum.Performance_SmallMIPImproveStartGap

    Performance_SmallMIPMaxTime = plx_enums.AttributeIDEnum.Performance_SmallMIPMaxTime

    Performance_SmallMIPIntegerCount = plx_enums.AttributeIDEnum.Performance_SmallMIPIntegerCount

    Performance_MIPRelativeGap = plx_enums.AttributeIDEnum.Performance_MIPRelativeGap

    Performance_MIPImproveStartGap = plx_enums.AttributeIDEnum.Performance_MIPImproveStartGap

    Performance_MIPMaxTime = plx_enums.AttributeIDEnum.Performance_MIPMaxTime

    Performance_MIPMaxRelaxationRepairTime = plx_enums.AttributeIDEnum.Performance_MIPMaxRelaxationRepairTime

    Performance_MIPMaximumThreads = plx_enums.AttributeIDEnum.Performance_MIPMaximumThreads

    Performance_MaximumParallelTasks = plx_enums.AttributeIDEnum.Performance_MaximumParallelTasks

    Performance_MIPStartSolution = plx_enums.AttributeIDEnum.Performance_MIPStartSolution

    Project_Enabled = plx_enums.AttributeIDEnum.Project_Enabled

    Diagnostic_ClearExisting = plx_enums.AttributeIDEnum.Diagnostic_ClearExisting

    Diagnostic_TaskSize = plx_enums.AttributeIDEnum.Diagnostic_TaskSize

    Diagnostic_TaskComponents = plx_enums.AttributeIDEnum.Diagnostic_TaskComponents

    Diagnostic_LPProgress = plx_enums.AttributeIDEnum.Diagnostic_LPProgress

    Diagnostic_MIPProgress = plx_enums.AttributeIDEnum.Diagnostic_MIPProgress

    Diagnostic_SolverSummary = plx_enums.AttributeIDEnum.Diagnostic_SolverSummary

    Diagnostic_SolutionStatus = plx_enums.AttributeIDEnum.Diagnostic_SolutionStatus

    Diagnostic_Times = plx_enums.AttributeIDEnum.Diagnostic_Times

    Diagnostic_SampleSummary = plx_enums.AttributeIDEnum.Diagnostic_SampleSummary

    Diagnostic_StepSummary = plx_enums.AttributeIDEnum.Diagnostic_StepSummary

    Diagnostic_PerformanceSummary = plx_enums.AttributeIDEnum.Diagnostic_PerformanceSummary

    Diagnostic_StepFrom = plx_enums.AttributeIDEnum.Diagnostic_StepFrom

    Diagnostic_StepTo = plx_enums.AttributeIDEnum.Diagnostic_StepTo

    Diagnostic_SampleFrom = plx_enums.AttributeIDEnum.Diagnostic_SampleFrom

    Diagnostic_SampleTo = plx_enums.AttributeIDEnum.Diagnostic_SampleTo

    Diagnostic_LPFiles = plx_enums.AttributeIDEnum.Diagnostic_LPFiles

    Diagnostic_MPSFiles = plx_enums.AttributeIDEnum.Diagnostic_MPSFiles

    Diagnostic_SolutionFiles = plx_enums.AttributeIDEnum.Diagnostic_SolutionFiles

    Diagnostic_GenericNames = plx_enums.AttributeIDEnum.Diagnostic_GenericNames

    Diagnostic_BinaryFiles = plx_enums.AttributeIDEnum.Diagnostic_BinaryFiles

    Diagnostic_UseGenericWriter = plx_enums.AttributeIDEnum.Diagnostic_UseGenericWriter

    Diagnostic_SortRowColumnNames = plx_enums.AttributeIDEnum.Diagnostic_SortRowColumnNames

    Diagnostic_StandardizeNames = plx_enums.AttributeIDEnum.Diagnostic_StandardizeNames

    Diagnostic_StripModelName = plx_enums.AttributeIDEnum.Diagnostic_StripModelName

    Diagnostic_Algebraic = plx_enums.AttributeIDEnum.Diagnostic_Algebraic

    Diagnostic_SkipZeroValues = plx_enums.AttributeIDEnum.Diagnostic_SkipZeroValues

    Diagnostic_ZeroToleranceLP = plx_enums.AttributeIDEnum.Diagnostic_ZeroToleranceLP

    Diagnostic_ZeroToleranceSOL = plx_enums.AttributeIDEnum.Diagnostic_ZeroToleranceSOL

    Diagnostic_DecimalPlacesLP = plx_enums.AttributeIDEnum.Diagnostic_DecimalPlacesLP

    Diagnostic_DecimalPlacesSOL = plx_enums.AttributeIDEnum.Diagnostic_DecimalPlacesSOL

    Diagnostic_Infeasibilities = plx_enums.AttributeIDEnum.Diagnostic_Infeasibilities

    Diagnostic_MaxInfeasibilityLogLines = plx_enums.AttributeIDEnum.Diagnostic_MaxInfeasibilityLogLines

    Diagnostic_FeasibilityRepairWeight = plx_enums.AttributeIDEnum.Diagnostic_FeasibilityRepairWeight

    Diagnostic_DatabaseLoad = plx_enums.AttributeIDEnum.Diagnostic_DatabaseLoad

    Diagnostic_Licensing = plx_enums.AttributeIDEnum.Diagnostic_Licensing

    Diagnostic_ComputerInformation = plx_enums.AttributeIDEnum.Diagnostic_ComputerInformation

    Diagnostic_DataFileRead = plx_enums.AttributeIDEnum.Diagnostic_DataFileRead

    Diagnostic_BertrandPricing = plx_enums.AttributeIDEnum.Diagnostic_BertrandPricing

    Diagnostic_RevenueRecovery = plx_enums.AttributeIDEnum.Diagnostic_RevenueRecovery

    Diagnostic_BidCostMarkup = plx_enums.AttributeIDEnum.Diagnostic_BidCostMarkup

    Diagnostic_NewEntry = plx_enums.AttributeIDEnum.Diagnostic_NewEntry

    Diagnostic_ShiftFactors = plx_enums.AttributeIDEnum.Diagnostic_ShiftFactors

    Diagnostic_UnservedEnergy = plx_enums.AttributeIDEnum.Diagnostic_UnservedEnergy

    Diagnostic_InterruptionSharing = plx_enums.AttributeIDEnum.Diagnostic_InterruptionSharing

    Diagnostic_NetworkTraversal = plx_enums.AttributeIDEnum.Diagnostic_NetworkTraversal

    Diagnostic_TransmissionTopology = plx_enums.AttributeIDEnum.Diagnostic_TransmissionTopology

    Diagnostic_TransmissionLosses = plx_enums.AttributeIDEnum.Diagnostic_TransmissionLosses

    Diagnostic_CongestionCharges = plx_enums.AttributeIDEnum.Diagnostic_CongestionCharges

    Diagnostic_MarginalLossCharges = plx_enums.AttributeIDEnum.Diagnostic_MarginalLossCharges

    Diagnostic_BindingContingencies = plx_enums.AttributeIDEnum.Diagnostic_BindingContingencies

    Diagnostic_UnitCommitment = plx_enums.AttributeIDEnum.Diagnostic_UnitCommitment

    Diagnostic_ConstraintDecomposition = plx_enums.AttributeIDEnum.Diagnostic_ConstraintDecomposition

    Diagnostic_ConstraintRollover = plx_enums.AttributeIDEnum.Diagnostic_ConstraintRollover

    Diagnostic_StorageDecomposition = plx_enums.AttributeIDEnum.Diagnostic_StorageDecomposition

    Diagnostic_UniformPricing = plx_enums.AttributeIDEnum.Diagnostic_UniformPricing

    Diagnostic_MarginalUnit = plx_enums.AttributeIDEnum.Diagnostic_MarginalUnit

    Diagnostic_MarginalUnitTransmissionDetail = plx_enums.AttributeIDEnum.Diagnostic_MarginalUnitTransmissionDetail

    Diagnostic_MarginalUnitIncrement = plx_enums.AttributeIDEnum.Diagnostic_MarginalUnitIncrement

    Diagnostic_MarginalExpansionUnit = plx_enums.AttributeIDEnum.Diagnostic_MarginalExpansionUnit

    Diagnostic_MarginalExpansionIncrement = plx_enums.AttributeIDEnum.Diagnostic_MarginalExpansionIncrement

    Diagnostic_RegionSupply = plx_enums.AttributeIDEnum.Diagnostic_RegionSupply

    Diagnostic_Annuities = plx_enums.AttributeIDEnum.Diagnostic_Annuities

    Diagnostic_NPV = plx_enums.AttributeIDEnum.Diagnostic_NPV

    Diagnostic_EmbeddedLosses = plx_enums.AttributeIDEnum.Diagnostic_EmbeddedLosses

    Diagnostic_Outages = plx_enums.AttributeIDEnum.Diagnostic_Outages

    Diagnostic_RandomNumberSeed = plx_enums.AttributeIDEnum.Diagnostic_RandomNumberSeed

    Diagnostic_Interleaved = plx_enums.AttributeIDEnum.Diagnostic_Interleaved

    Diagnostic_HeatRate = plx_enums.AttributeIDEnum.Diagnostic_HeatRate

    Diagnostic_ObjectiveFunction = plx_enums.AttributeIDEnum.Diagnostic_ObjectiveFunction

    Diagnostic_FutureCostFunction = plx_enums.AttributeIDEnum.Diagnostic_FutureCostFunction

    Diagnostic_HistoricalSampling = plx_enums.AttributeIDEnum.Diagnostic_HistoricalSampling

    Diagnostic_ScenarioTree = plx_enums.AttributeIDEnum.Diagnostic_ScenarioTree

    Diagnostic_SampleWeights = plx_enums.AttributeIDEnum.Diagnostic_SampleWeights


class BatteryAttributeEnum(Enum):
    Latitude = plx_enums.BatteryAttributeEnum.Latitude

    Longitude = plx_enums.BatteryAttributeEnum.Longitude


class ChronoStepTypeEnum(Enum):
    Minute = plx_enums.ChronoStepTypeEnum.Minute

    Hour = plx_enums.ChronoStepTypeEnum.Hour

    Day = plx_enums.ChronoStepTypeEnum.Day

    Week = plx_enums.ChronoStepTypeEnum.Week

    Second = plx_enums.ChronoStepTypeEnum.Second


class ChronologyEnum(Enum):
    Full = plx_enums.ChronologyEnum.Full

    TypicalWeek = plx_enums.ChronologyEnum.TypicalWeek

    Partial = plx_enums.ChronologyEnum.Partial

    Fitted = plx_enums.ChronologyEnum.Fitted

    Sampled = plx_enums.ChronologyEnum.Sampled


class ClassEnum(Enum):
    System = plx_enums.ClassEnum.System

    Generator = plx_enums.ClassEnum.Generator

    Fuel = plx_enums.ClassEnum.Fuel

    FuelContract = plx_enums.ClassEnum.FuelContract

    Emission = plx_enums.ClassEnum.Emission

    Abatement = plx_enums.ClassEnum.Abatement

    Storage = plx_enums.ClassEnum.Storage

    Waterway = plx_enums.ClassEnum.Waterway

    PowerStation = plx_enums.ClassEnum.PowerStation

    PhysicalContract = plx_enums.ClassEnum.PhysicalContract

    Purchaser = plx_enums.ClassEnum.Purchaser

    Reserve = plx_enums.ClassEnum.Reserve

    Battery = plx_enums.ClassEnum.Battery

    Maintenance = plx_enums.ClassEnum.Maintenance

    HeatPlant = plx_enums.ClassEnum.HeatPlant

    HeatNode = plx_enums.ClassEnum.HeatNode

    GasField = plx_enums.ClassEnum.GasField

    GasPlant = plx_enums.ClassEnum.GasPlant

    GasPipeline = plx_enums.ClassEnum.GasPipeline

    GasNode = plx_enums.ClassEnum.GasNode

    GasStorage = plx_enums.ClassEnum.GasStorage

    GasDemand = plx_enums.ClassEnum.GasDemand

    GasBasin = plx_enums.ClassEnum.GasBasin

    GasZone = plx_enums.ClassEnum.GasZone

    GasContract = plx_enums.ClassEnum.GasContract

    GasTransport = plx_enums.ClassEnum.GasTransport

    WaterPlant = plx_enums.ClassEnum.WaterPlant

    WaterPipeline = plx_enums.ClassEnum.WaterPipeline

    WaterNode = plx_enums.ClassEnum.WaterNode

    WaterStorage = plx_enums.ClassEnum.WaterStorage

    WaterDemand = plx_enums.ClassEnum.WaterDemand

    WaterZone = plx_enums.ClassEnum.WaterZone

    Region = plx_enums.ClassEnum.Region

    Zone = plx_enums.ClassEnum.Zone

    Node = plx_enums.ClassEnum.Node

    Line = plx_enums.ClassEnum.Line

    MLF = plx_enums.ClassEnum.MLF

    Transformer = plx_enums.ClassEnum.Transformer

    FlowControl = plx_enums.ClassEnum.FlowControl

    Interface = plx_enums.ClassEnum.Interface

    Contingency = plx_enums.ClassEnum.Contingency

    Company = plx_enums.ClassEnum.Company

    FinancialContract = plx_enums.ClassEnum.FinancialContract

    Hub = plx_enums.ClassEnum.Hub

    TransmissionRight = plx_enums.ClassEnum.TransmissionRight

    Cournot = plx_enums.ClassEnum.Cournot

    RSI = plx_enums.ClassEnum.RSI

    Market = plx_enums.ClassEnum.Market

    Constraint = plx_enums.ClassEnum.Constraint

    DecisionVariable = plx_enums.ClassEnum.DecisionVariable

    DataFile = plx_enums.ClassEnum.DataFile

    Variable = plx_enums.ClassEnum.Variable

    Timeslice = plx_enums.ClassEnum.Timeslice

    Global = plx_enums.ClassEnum.Global

    Scenario = plx_enums.ClassEnum.Scenario

    Model = plx_enums.ClassEnum.Model

    Project = plx_enums.ClassEnum.Project

    Horizon = plx_enums.ClassEnum.Horizon

    Report = plx_enums.ClassEnum.Report

    LTPlan = plx_enums.ClassEnum.LTPlan

    PASA = plx_enums.ClassEnum.PASA

    MTSchedule = plx_enums.ClassEnum.MTSchedule

    STSchedule = plx_enums.ClassEnum.STSchedule

    Transmission = plx_enums.ClassEnum.Transmission

    Production = plx_enums.ClassEnum.Production

    Competition = plx_enums.ClassEnum.Competition

    Stochastic = plx_enums.ClassEnum.Stochastic

    Performance = plx_enums.ClassEnum.Performance

    Diagnostic = plx_enums.ClassEnum.Diagnostic

    List = plx_enums.ClassEnum.List


class ClassGroupEnum(Enum):
    Electric = plx_enums.ClassGroupEnum.Electric

    Heat = plx_enums.ClassGroupEnum.Heat

    Gas = plx_enums.ClassGroupEnum.Gas

    Water = plx_enums.ClassGroupEnum.Water

    Transmission = plx_enums.ClassGroupEnum.Transmission

    Financial = plx_enums.ClassGroupEnum.Financial

    Generic = plx_enums.ClassGroupEnum.Generic

    Data = plx_enums.ClassGroupEnum.Data

    Execute = plx_enums.ClassGroupEnum.Execute

    Simulation = plx_enums.ClassGroupEnum.Simulation

    Settings = plx_enums.ClassGroupEnum.Settings

    List = plx_enums.ClassGroupEnum.List


class CollectionEnum(Enum):
    SystemGenerators = plx_enums.CollectionEnum.SystemGenerators

    SystemFuels = plx_enums.CollectionEnum.SystemFuels

    SystemFuelContracts = plx_enums.CollectionEnum.SystemFuelContracts

    SystemEmissions = plx_enums.CollectionEnum.SystemEmissions

    SystemAbatements = plx_enums.CollectionEnum.SystemAbatements

    SystemStorages = plx_enums.CollectionEnum.SystemStorages

    SystemWaterways = plx_enums.CollectionEnum.SystemWaterways

    SystemPowerStations = plx_enums.CollectionEnum.SystemPowerStations

    SystemPhysicalContracts = plx_enums.CollectionEnum.SystemPhysicalContracts

    SystemPurchasers = plx_enums.CollectionEnum.SystemPurchasers

    SystemReserves = plx_enums.CollectionEnum.SystemReserves

    SystemBatteries = plx_enums.CollectionEnum.SystemBatteries

    SystemMaintenances = plx_enums.CollectionEnum.SystemMaintenances

    SystemHeatPlants = plx_enums.CollectionEnum.SystemHeatPlants

    SystemHeatNodes = plx_enums.CollectionEnum.SystemHeatNodes

    SystemGasFields = plx_enums.CollectionEnum.SystemGasFields

    SystemGasPlants = plx_enums.CollectionEnum.SystemGasPlants

    SystemGasPipelines = plx_enums.CollectionEnum.SystemGasPipelines

    SystemGasNodes = plx_enums.CollectionEnum.SystemGasNodes

    SystemGasStorages = plx_enums.CollectionEnum.SystemGasStorages

    SystemGasDemands = plx_enums.CollectionEnum.SystemGasDemands

    SystemGasBasins = plx_enums.CollectionEnum.SystemGasBasins

    SystemGasZones = plx_enums.CollectionEnum.SystemGasZones

    SystemGasContracts = plx_enums.CollectionEnum.SystemGasContracts

    SystemGasTransports = plx_enums.CollectionEnum.SystemGasTransports

    SystemWaterPlants = plx_enums.CollectionEnum.SystemWaterPlants

    SystemWaterPipelines = plx_enums.CollectionEnum.SystemWaterPipelines

    SystemWaterNodes = plx_enums.CollectionEnum.SystemWaterNodes

    SystemWaterStorages = plx_enums.CollectionEnum.SystemWaterStorages

    SystemWaterDemands = plx_enums.CollectionEnum.SystemWaterDemands

    SystemWaterZones = plx_enums.CollectionEnum.SystemWaterZones

    SystemRegions = plx_enums.CollectionEnum.SystemRegions

    SystemZones = plx_enums.CollectionEnum.SystemZones

    SystemNodes = plx_enums.CollectionEnum.SystemNodes

    SystemLines = plx_enums.CollectionEnum.SystemLines

    SystemMLFs = plx_enums.CollectionEnum.SystemMLFs

    SystemTransformers = plx_enums.CollectionEnum.SystemTransformers

    SystemFlowControls = plx_enums.CollectionEnum.SystemFlowControls

    SystemInterfaces = plx_enums.CollectionEnum.SystemInterfaces

    SystemContingencies = plx_enums.CollectionEnum.SystemContingencies

    SystemCompanies = plx_enums.CollectionEnum.SystemCompanies

    SystemFinancialContracts = plx_enums.CollectionEnum.SystemFinancialContracts

    SystemHubs = plx_enums.CollectionEnum.SystemHubs

    SystemTransmissionRights = plx_enums.CollectionEnum.SystemTransmissionRights

    SystemCournots = plx_enums.CollectionEnum.SystemCournots

    SystemRSIs = plx_enums.CollectionEnum.SystemRSIs

    SystemMarkets = plx_enums.CollectionEnum.SystemMarkets

    SystemConstraints = plx_enums.CollectionEnum.SystemConstraints

    SystemDecisionVariables = plx_enums.CollectionEnum.SystemDecisionVariables

    SystemLists = plx_enums.CollectionEnum.SystemLists

    SystemDataFiles = plx_enums.CollectionEnum.SystemDataFiles

    SystemVariables = plx_enums.CollectionEnum.SystemVariables

    SystemTimeslices = plx_enums.CollectionEnum.SystemTimeslices

    SystemGlobals = plx_enums.CollectionEnum.SystemGlobals

    SystemScenarios = plx_enums.CollectionEnum.SystemScenarios

    SystemModels = plx_enums.CollectionEnum.SystemModels

    SystemProjects = plx_enums.CollectionEnum.SystemProjects

    SystemHorizons = plx_enums.CollectionEnum.SystemHorizons

    SystemReports = plx_enums.CollectionEnum.SystemReports

    SystemLTPlan = plx_enums.CollectionEnum.SystemLTPlan

    SystemPASA = plx_enums.CollectionEnum.SystemPASA

    SystemMTSchedule = plx_enums.CollectionEnum.SystemMTSchedule

    SystemSTSchedule = plx_enums.CollectionEnum.SystemSTSchedule

    SystemTransmission = plx_enums.CollectionEnum.SystemTransmission

    SystemProduction = plx_enums.CollectionEnum.SystemProduction

    SystemCompetition = plx_enums.CollectionEnum.SystemCompetition

    SystemStochastic = plx_enums.CollectionEnum.SystemStochastic

    SystemPerformance = plx_enums.CollectionEnum.SystemPerformance

    SystemDiagnostics = plx_enums.CollectionEnum.SystemDiagnostics

    GeneratorTemplate = plx_enums.CollectionEnum.GeneratorTemplate

    FuelTemplate = plx_enums.CollectionEnum.FuelTemplate

    FuelContractTemplate = plx_enums.CollectionEnum.FuelContractTemplate

    EmissionTemplate = plx_enums.CollectionEnum.EmissionTemplate

    AbatementTemplate = plx_enums.CollectionEnum.AbatementTemplate

    StorageTemplate = plx_enums.CollectionEnum.StorageTemplate

    WaterwayTemplate = plx_enums.CollectionEnum.WaterwayTemplate

    PowerStationTemplate = plx_enums.CollectionEnum.PowerStationTemplate

    PhysicalContractTemplate = plx_enums.CollectionEnum.PhysicalContractTemplate

    PurchaserTemplate = plx_enums.CollectionEnum.PurchaserTemplate

    ReserveTemplate = plx_enums.CollectionEnum.ReserveTemplate

    BatteryTemplate = plx_enums.CollectionEnum.BatteryTemplate

    MaintenanceTemplate = plx_enums.CollectionEnum.MaintenanceTemplate

    HeatPlantTemplate = plx_enums.CollectionEnum.HeatPlantTemplate

    HeatNodeTemplate = plx_enums.CollectionEnum.HeatNodeTemplate

    GasFieldTemplate = plx_enums.CollectionEnum.GasFieldTemplate

    GasPlantTemplate = plx_enums.CollectionEnum.GasPlantTemplate

    GasPipelineTemplate = plx_enums.CollectionEnum.GasPipelineTemplate

    GasNodeTemplate = plx_enums.CollectionEnum.GasNodeTemplate

    GasStorageTemplate = plx_enums.CollectionEnum.GasStorageTemplate

    GasDemandTemplate = plx_enums.CollectionEnum.GasDemandTemplate

    GasBasinTemplate = plx_enums.CollectionEnum.GasBasinTemplate

    GasZoneTemplate = plx_enums.CollectionEnum.GasZoneTemplate

    GasContractTemplate = plx_enums.CollectionEnum.GasContractTemplate

    WaterPlantTemplate = plx_enums.CollectionEnum.WaterPlantTemplate

    WaterPipelineTemplate = plx_enums.CollectionEnum.WaterPipelineTemplate

    WaterNodeTemplate = plx_enums.CollectionEnum.WaterNodeTemplate

    WaterStorageTemplate = plx_enums.CollectionEnum.WaterStorageTemplate

    WaterDemandTemplate = plx_enums.CollectionEnum.WaterDemandTemplate

    WaterZoneTemplate = plx_enums.CollectionEnum.WaterZoneTemplate

    RegionTemplate = plx_enums.CollectionEnum.RegionTemplate

    ZoneTemplate = plx_enums.CollectionEnum.ZoneTemplate

    NodeTemplate = plx_enums.CollectionEnum.NodeTemplate

    LineTemplate = plx_enums.CollectionEnum.LineTemplate

    MLFTemplate = plx_enums.CollectionEnum.MLFTemplate

    TransformerTemplate = plx_enums.CollectionEnum.TransformerTemplate

    FlowControlTemplate = plx_enums.CollectionEnum.FlowControlTemplate

    InterfaceTemplate = plx_enums.CollectionEnum.InterfaceTemplate

    ContingencyTemplate = plx_enums.CollectionEnum.ContingencyTemplate

    CompanyTemplate = plx_enums.CollectionEnum.CompanyTemplate

    FinancialContractTemplate = plx_enums.CollectionEnum.FinancialContractTemplate

    HubTemplate = plx_enums.CollectionEnum.HubTemplate

    TransmissionRightTemplate = plx_enums.CollectionEnum.TransmissionRightTemplate

    CournotTemplate = plx_enums.CollectionEnum.CournotTemplate

    RSITemplate = plx_enums.CollectionEnum.RSITemplate

    MarketTemplate = plx_enums.CollectionEnum.MarketTemplate

    ConstraintTemplate = plx_enums.CollectionEnum.ConstraintTemplate

    DecisionVariableTemplate = plx_enums.CollectionEnum.DecisionVariableTemplate

    GeneratorHeatInput = plx_enums.CollectionEnum.GeneratorHeatInput

    GeneratorTransition = plx_enums.CollectionEnum.GeneratorTransition

    GeneratorFuels = plx_enums.CollectionEnum.GeneratorFuels

    GeneratorStartFuels = plx_enums.CollectionEnum.GeneratorStartFuels

    GeneratorHeadStorage = plx_enums.CollectionEnum.GeneratorHeadStorage

    GeneratorTailStorage = plx_enums.CollectionEnum.GeneratorTailStorage

    GeneratorPowerStation = plx_enums.CollectionEnum.GeneratorPowerStation

    GeneratorMarktoMarkets = plx_enums.CollectionEnum.GeneratorMarktoMarkets

    GeneratorGasNode = plx_enums.CollectionEnum.GeneratorGasNode

    GeneratorWaterNode = plx_enums.CollectionEnum.GeneratorWaterNode

    GeneratorNodes = plx_enums.CollectionEnum.GeneratorNodes

    GeneratorNodes_star_ = plx_enums.CollectionEnum.GeneratorNodes_star_

    GeneratorCompanies = plx_enums.CollectionEnum.GeneratorCompanies

    FuelGasNodes = plx_enums.CollectionEnum.FuelGasNodes

    FuelCompanies = plx_enums.CollectionEnum.FuelCompanies

    FuelContractGenerators = plx_enums.CollectionEnum.FuelContractGenerators

    FuelContractFuel = plx_enums.CollectionEnum.FuelContractFuel

    FuelContractCompanies = plx_enums.CollectionEnum.FuelContractCompanies

    FuelContractConstraints = plx_enums.CollectionEnum.FuelContractConstraints

    EmissionGenerators = plx_enums.CollectionEnum.EmissionGenerators

    EmissionFuels = plx_enums.CollectionEnum.EmissionFuels

    EmissionGasNodes = plx_enums.CollectionEnum.EmissionGasNodes

    EmissionGasPlants = plx_enums.CollectionEnum.EmissionGasPlants

    EmissionWaterPlants = plx_enums.CollectionEnum.EmissionWaterPlants

    AbatementGenerators = plx_enums.CollectionEnum.AbatementGenerators

    AbatementEmissions = plx_enums.CollectionEnum.AbatementEmissions

    AbatementConsumables = plx_enums.CollectionEnum.AbatementConsumables

    StorageWaterNodes = plx_enums.CollectionEnum.StorageWaterNodes

    WaterwayStorageFrom = plx_enums.CollectionEnum.WaterwayStorageFrom

    WaterwayStorageTo = plx_enums.CollectionEnum.WaterwayStorageTo

    PowerStationNodes = plx_enums.CollectionEnum.PowerStationNodes

    PhysicalContractGenerationNode = plx_enums.CollectionEnum.PhysicalContractGenerationNode

    PhysicalContractLoadNode = plx_enums.CollectionEnum.PhysicalContractLoadNode

    PhysicalContractCompanies = plx_enums.CollectionEnum.PhysicalContractCompanies

    PurchaserNodes = plx_enums.CollectionEnum.PurchaserNodes

    PurchaserNodes_star_ = plx_enums.CollectionEnum.PurchaserNodes_star_

    PurchaserCompanies = plx_enums.CollectionEnum.PurchaserCompanies

    ReserveGenerators = plx_enums.CollectionEnum.ReserveGenerators

    ReservePurchasers = plx_enums.CollectionEnum.ReservePurchasers

    ReserveGeneratorContingencies = plx_enums.CollectionEnum.ReserveGeneratorContingencies

    ReserveGeneratorCostAllocation = plx_enums.CollectionEnum.ReserveGeneratorCostAllocation

    ReserveBatteries = plx_enums.CollectionEnum.ReserveBatteries

    ReserveNestedReserves = plx_enums.CollectionEnum.ReserveNestedReserves

    ReserveRegions = plx_enums.CollectionEnum.ReserveRegions

    ReserveLineContingencies = plx_enums.CollectionEnum.ReserveLineContingencies

    BatteryNode = plx_enums.CollectionEnum.BatteryNode

    BatteryNodes_star_ = plx_enums.CollectionEnum.BatteryNodes_star_

    BatteryCompanies = plx_enums.CollectionEnum.BatteryCompanies

    MaintenanceGenerators = plx_enums.CollectionEnum.MaintenanceGenerators

    MaintenanceGasPipelines = plx_enums.CollectionEnum.MaintenanceGasPipelines

    MaintenanceLines = plx_enums.CollectionEnum.MaintenanceLines

    MaintenancePrerequisites = plx_enums.CollectionEnum.MaintenancePrerequisites

    GeneratorHeatInputNodes = plx_enums.CollectionEnum.GeneratorHeatInputNodes

    GeneratorHeatOutputNodes = plx_enums.CollectionEnum.GeneratorHeatOutputNodes

    HeatPlantFuels = plx_enums.CollectionEnum.HeatPlantFuels

    HeatPlantNodes = plx_enums.CollectionEnum.HeatPlantNodes

    HeatPlantHeatInputNodes = plx_enums.CollectionEnum.HeatPlantHeatInputNodes

    HeatPlantHeatOutputNodes = plx_enums.CollectionEnum.HeatPlantHeatOutputNodes

    HeatPlantStartFuels = plx_enums.CollectionEnum.HeatPlantStartFuels

    HeatNodeHeatExportNodes = plx_enums.CollectionEnum.HeatNodeHeatExportNodes

    HeatNodeWaterPlants = plx_enums.CollectionEnum.HeatNodeWaterPlants

    GasFieldCompanies = plx_enums.CollectionEnum.GasFieldCompanies

    GasFieldGasNode = plx_enums.CollectionEnum.GasFieldGasNode

    GasFieldGasBasin = plx_enums.CollectionEnum.GasFieldGasBasin

    GasPlantInputNode = plx_enums.CollectionEnum.GasPlantInputNode

    GasPlantOutputNode = plx_enums.CollectionEnum.GasPlantOutputNode

    GasPlantNode = plx_enums.CollectionEnum.GasPlantNode

    GasPipelineGasNodeFrom = plx_enums.CollectionEnum.GasPipelineGasNodeFrom

    GasPipelineGasNodeTo = plx_enums.CollectionEnum.GasPipelineGasNodeTo

    GasNodeGasZones = plx_enums.CollectionEnum.GasNodeGasZones

    GasStorageGasNode = plx_enums.CollectionEnum.GasStorageGasNode

    GasDemandGasNodes = plx_enums.CollectionEnum.GasDemandGasNodes

    GasDemandCompanies = plx_enums.CollectionEnum.GasDemandCompanies

    GasZoneGenerators = plx_enums.CollectionEnum.GasZoneGenerators

    GasZoneGasFields = plx_enums.CollectionEnum.GasZoneGasFields

    GasZoneGasPlants = plx_enums.CollectionEnum.GasZoneGasPlants

    GasZoneExportingGasPipelines = plx_enums.CollectionEnum.GasZoneExportingGasPipelines

    GasZoneImportingGasPipelines = plx_enums.CollectionEnum.GasZoneImportingGasPipelines

    GasZoneInterzonalGasPipelines = plx_enums.CollectionEnum.GasZoneInterzonalGasPipelines

    GasZoneIntrazonalGasPipelines = plx_enums.CollectionEnum.GasZoneIntrazonalGasPipelines

    GasZoneGasStorages = plx_enums.CollectionEnum.GasZoneGasStorages

    GasZoneGasDemands = plx_enums.CollectionEnum.GasZoneGasDemands

    GasZoneExportingGasTransports = plx_enums.CollectionEnum.GasZoneExportingGasTransports

    GasZoneImportingGasTransports = plx_enums.CollectionEnum.GasZoneImportingGasTransports

    GasZoneInterzonalGasTransports = plx_enums.CollectionEnum.GasZoneInterzonalGasTransports

    GasZoneIntrazonalGasTransports = plx_enums.CollectionEnum.GasZoneIntrazonalGasTransports

    GasContractGasFields = plx_enums.CollectionEnum.GasContractGasFields

    GasContractGasPipelines = plx_enums.CollectionEnum.GasContractGasPipelines

    GasContractGasTransports = plx_enums.CollectionEnum.GasContractGasTransports

    GasTransportExportNode = plx_enums.CollectionEnum.GasTransportExportNode

    GasTransportImportNode = plx_enums.CollectionEnum.GasTransportImportNode

    WaterPlantInputNode = plx_enums.CollectionEnum.WaterPlantInputNode

    WaterPlantOutputNode = plx_enums.CollectionEnum.WaterPlantOutputNode

    WaterPlantNode = plx_enums.CollectionEnum.WaterPlantNode

    WaterPipelineWaterNodeFrom = plx_enums.CollectionEnum.WaterPipelineWaterNodeFrom

    WaterPipelineWaterNodeTo = plx_enums.CollectionEnum.WaterPipelineWaterNodeTo

    WaterNodeWaterZones = plx_enums.CollectionEnum.WaterNodeWaterZones

    WaterNodeNode = plx_enums.CollectionEnum.WaterNodeNode

    WaterStorageWaterNode = plx_enums.CollectionEnum.WaterStorageWaterNode

    WaterDemandWaterNodes = plx_enums.CollectionEnum.WaterDemandWaterNodes

    WaterZoneWaterPlants = plx_enums.CollectionEnum.WaterZoneWaterPlants

    WaterZoneWaterStorages = plx_enums.CollectionEnum.WaterZoneWaterStorages

    WaterZoneExportingWaterPipelines = plx_enums.CollectionEnum.WaterZoneExportingWaterPipelines

    WaterZoneImportingWaterPipelines = plx_enums.CollectionEnum.WaterZoneImportingWaterPipelines

    WaterZoneInterzonalWaterPipelines = plx_enums.CollectionEnum.WaterZoneInterzonalWaterPipelines

    WaterZoneIntrazonalWaterPipelines = plx_enums.CollectionEnum.WaterZoneIntrazonalWaterPipelines

    WaterZoneWaterDemands = plx_enums.CollectionEnum.WaterZoneWaterDemands

    RegionGenerators = plx_enums.CollectionEnum.RegionGenerators

    RegionEmissions = plx_enums.CollectionEnum.RegionEmissions

    RegionGenerationContracts = plx_enums.CollectionEnum.RegionGenerationContracts

    RegionLoadContracts = plx_enums.CollectionEnum.RegionLoadContracts

    RegionPurchasers = plx_enums.CollectionEnum.RegionPurchasers

    RegionMarkets = plx_enums.CollectionEnum.RegionMarkets

    RegionBatteries = plx_enums.CollectionEnum.RegionBatteries

    RegionRegions = plx_enums.CollectionEnum.RegionRegions

    RegionReferenceNode = plx_enums.CollectionEnum.RegionReferenceNode

    RegionExportingLines = plx_enums.CollectionEnum.RegionExportingLines

    RegionImportingLines = plx_enums.CollectionEnum.RegionImportingLines

    RegionInterregionalLines = plx_enums.CollectionEnum.RegionInterregionalLines

    RegionIntraregionalLines = plx_enums.CollectionEnum.RegionIntraregionalLines

    RegionExportingTransformers = plx_enums.CollectionEnum.RegionExportingTransformers

    RegionImportingTransformers = plx_enums.CollectionEnum.RegionImportingTransformers

    RegionInterregionalTransformers = plx_enums.CollectionEnum.RegionInterregionalTransformers

    RegionIntraregionalTransformers = plx_enums.CollectionEnum.RegionIntraregionalTransformers

    RegionUtilities = plx_enums.CollectionEnum.RegionUtilities

    ZoneCapacityGenerators = plx_enums.CollectionEnum.ZoneCapacityGenerators

    ZoneGenerators = plx_enums.CollectionEnum.ZoneGenerators

    ZoneEmissions = plx_enums.CollectionEnum.ZoneEmissions

    ZoneCapacityGenerationContracts = plx_enums.CollectionEnum.ZoneCapacityGenerationContracts

    ZoneCapacityLoadContracts = plx_enums.CollectionEnum.ZoneCapacityLoadContracts

    ZoneGenerationContracts = plx_enums.CollectionEnum.ZoneGenerationContracts

    ZoneLoadContracts = plx_enums.CollectionEnum.ZoneLoadContracts

    ZoneCapacityPurchasers = plx_enums.CollectionEnum.ZoneCapacityPurchasers

    ZonePurchasers = plx_enums.CollectionEnum.ZonePurchasers

    ZoneMarkets = plx_enums.CollectionEnum.ZoneMarkets

    ZoneCapacityMarkets = plx_enums.CollectionEnum.ZoneCapacityMarkets

    ZoneCapacityBatteries = plx_enums.CollectionEnum.ZoneCapacityBatteries

    ZoneBatteries = plx_enums.CollectionEnum.ZoneBatteries

    ZoneRegion = plx_enums.CollectionEnum.ZoneRegion

    ZoneZones = plx_enums.CollectionEnum.ZoneZones

    ZoneReferenceNode = plx_enums.CollectionEnum.ZoneReferenceNode

    ZoneExportingCapacityLines = plx_enums.CollectionEnum.ZoneExportingCapacityLines

    ZoneExportingLines = plx_enums.CollectionEnum.ZoneExportingLines

    ZoneImportingCapacityLines = plx_enums.CollectionEnum.ZoneImportingCapacityLines

    ZoneImportingLines = plx_enums.CollectionEnum.ZoneImportingLines

    ZoneInterzonalLines = plx_enums.CollectionEnum.ZoneInterzonalLines

    ZoneIntrazonalLines = plx_enums.CollectionEnum.ZoneIntrazonalLines

    ZoneExportingCapacityTransformers = plx_enums.CollectionEnum.ZoneExportingCapacityTransformers

    ZoneExportingTransformers = plx_enums.CollectionEnum.ZoneExportingTransformers

    ZoneImportingCapacityTransformers = plx_enums.CollectionEnum.ZoneImportingCapacityTransformers

    ZoneImportingTransformers = plx_enums.CollectionEnum.ZoneImportingTransformers

    ZoneInterzonalTransformers = plx_enums.CollectionEnum.ZoneInterzonalTransformers

    ZoneIntrazonalTransformers = plx_enums.CollectionEnum.ZoneIntrazonalTransformers

    NodeRegion = plx_enums.CollectionEnum.NodeRegion

    NodeCapacityZone = plx_enums.CollectionEnum.NodeCapacityZone

    NodeZone = plx_enums.CollectionEnum.NodeZone

    NodeHubs = plx_enums.CollectionEnum.NodeHubs

    LineNodeFrom = plx_enums.CollectionEnum.LineNodeFrom

    LineNodeTo = plx_enums.CollectionEnum.LineNodeTo

    LineCompanies = plx_enums.CollectionEnum.LineCompanies

    MLFRegions = plx_enums.CollectionEnum.MLFRegions

    MLFNode = plx_enums.CollectionEnum.MLFNode

    MLFLine = plx_enums.CollectionEnum.MLFLine

    TransformerNodeFrom = plx_enums.CollectionEnum.TransformerNodeFrom

    TransformerNodeTo = plx_enums.CollectionEnum.TransformerNodeTo

    FlowControlLine = plx_enums.CollectionEnum.FlowControlLine

    FlowControlLines_star_ = plx_enums.CollectionEnum.FlowControlLines_star_

    InterfaceLines = plx_enums.CollectionEnum.InterfaceLines

    InterfaceTransformers = plx_enums.CollectionEnum.InterfaceTransformers

    ContingencyGenerators = plx_enums.CollectionEnum.ContingencyGenerators

    ContingencyLines = plx_enums.CollectionEnum.ContingencyLines

    ContingencyMonitoredLines = plx_enums.CollectionEnum.ContingencyMonitoredLines

    ContingencyMonitoredTransformers = plx_enums.CollectionEnum.ContingencyMonitoredTransformers

    ContingencyTransformers = plx_enums.CollectionEnum.ContingencyTransformers

    ContingencyMonitoredInterfaces = plx_enums.CollectionEnum.ContingencyMonitoredInterfaces

    CompanyFuels = plx_enums.CollectionEnum.CompanyFuels

    CompanyEmissions = plx_enums.CollectionEnum.CompanyEmissions

    CompanyReserves = plx_enums.CollectionEnum.CompanyReserves

    CompanyRegions = plx_enums.CollectionEnum.CompanyRegions

    FinancialContractGenerators = plx_enums.CollectionEnum.FinancialContractGenerators

    FinancialContractRegion = plx_enums.CollectionEnum.FinancialContractRegion

    FinancialContractRegions = plx_enums.CollectionEnum.FinancialContractRegions

    FinancialContractGeneratingCompanies = plx_enums.CollectionEnum.FinancialContractGeneratingCompanies

    FinancialContractPurchasingCompanies = plx_enums.CollectionEnum.FinancialContractPurchasingCompanies

    FinancialContractConditions = plx_enums.CollectionEnum.FinancialContractConditions

    TransmissionRightNodeFrom = plx_enums.CollectionEnum.TransmissionRightNodeFrom

    TransmissionRightNodeTo = plx_enums.CollectionEnum.TransmissionRightNodeTo

    TransmissionRightZoneFrom = plx_enums.CollectionEnum.TransmissionRightZoneFrom

    TransmissionRightZoneTo = plx_enums.CollectionEnum.TransmissionRightZoneTo

    TransmissionRightHubFrom = plx_enums.CollectionEnum.TransmissionRightHubFrom

    TransmissionRightHubTo = plx_enums.CollectionEnum.TransmissionRightHubTo

    TransmissionRightLine = plx_enums.CollectionEnum.TransmissionRightLine

    TransmissionRightCompanies = plx_enums.CollectionEnum.TransmissionRightCompanies

    CournotRegion = plx_enums.CollectionEnum.CournotRegion

    RSIRegion = plx_enums.CollectionEnum.RSIRegion

    RSILines = plx_enums.CollectionEnum.RSILines

    RSIInterfaces = plx_enums.CollectionEnum.RSIInterfaces

    RSICompanies = plx_enums.CollectionEnum.RSICompanies

    MarketCapacityGenerators = plx_enums.CollectionEnum.MarketCapacityGenerators

    MarketHeatGenerators = plx_enums.CollectionEnum.MarketHeatGenerators

    MarketFuels = plx_enums.CollectionEnum.MarketFuels

    MarketEmissions = plx_enums.CollectionEnum.MarketEmissions

    MarketReserves = plx_enums.CollectionEnum.MarketReserves

    MarketGasNodes = plx_enums.CollectionEnum.MarketGasNodes

    MarketNodes = plx_enums.CollectionEnum.MarketNodes

    MarketCompanies = plx_enums.CollectionEnum.MarketCompanies

    ConstraintGenerators = plx_enums.CollectionEnum.ConstraintGenerators

    ConstraintFuels = plx_enums.CollectionEnum.ConstraintFuels

    ConstraintFuelContracts = plx_enums.CollectionEnum.ConstraintFuelContracts

    ConstraintEmissions = plx_enums.CollectionEnum.ConstraintEmissions

    ConstraintAbatements = plx_enums.CollectionEnum.ConstraintAbatements

    ConstraintStorages = plx_enums.CollectionEnum.ConstraintStorages

    ConstraintWaterways = plx_enums.CollectionEnum.ConstraintWaterways

    ConstraintPhysicalContracts = plx_enums.CollectionEnum.ConstraintPhysicalContracts

    ConstraintPurchasers = plx_enums.CollectionEnum.ConstraintPurchasers

    ConstraintReserves = plx_enums.CollectionEnum.ConstraintReserves

    ConstraintBatteries = plx_enums.CollectionEnum.ConstraintBatteries

    ConstraintMaintenances = plx_enums.CollectionEnum.ConstraintMaintenances

    ConstraintHeatPlants = plx_enums.CollectionEnum.ConstraintHeatPlants

    ConstraintHeatNodes = plx_enums.CollectionEnum.ConstraintHeatNodes

    ConstraintGasFields = plx_enums.CollectionEnum.ConstraintGasFields

    ConstraintGasPlants = plx_enums.CollectionEnum.ConstraintGasPlants

    ConstraintGasPipelines = plx_enums.CollectionEnum.ConstraintGasPipelines

    ConstraintGasNodes = plx_enums.CollectionEnum.ConstraintGasNodes

    ConstraintGasStorages = plx_enums.CollectionEnum.ConstraintGasStorages

    ConstraintGasBasins = plx_enums.CollectionEnum.ConstraintGasBasins

    ConstraintGasContracts = plx_enums.CollectionEnum.ConstraintGasContracts

    ConstraintGasTransports = plx_enums.CollectionEnum.ConstraintGasTransports

    ConstraintWaterPlants = plx_enums.CollectionEnum.ConstraintWaterPlants

    ConstraintWaterPipelines = plx_enums.CollectionEnum.ConstraintWaterPipelines

    ConstraintWaterNodes = plx_enums.CollectionEnum.ConstraintWaterNodes

    ConstraintWaterStorages = plx_enums.CollectionEnum.ConstraintWaterStorages

    ConstraintRegions = plx_enums.CollectionEnum.ConstraintRegions

    ConstraintZones = plx_enums.CollectionEnum.ConstraintZones

    ConstraintNodes = plx_enums.CollectionEnum.ConstraintNodes

    ConstraintLines = plx_enums.CollectionEnum.ConstraintLines

    ConstraintTransformers = plx_enums.CollectionEnum.ConstraintTransformers

    ConstraintFlowControls = plx_enums.CollectionEnum.ConstraintFlowControls

    ConstraintInterfaces = plx_enums.CollectionEnum.ConstraintInterfaces

    ConstraintCompanies = plx_enums.CollectionEnum.ConstraintCompanies

    ConstraintHubs = plx_enums.CollectionEnum.ConstraintHubs

    ConstraintMarkets = plx_enums.CollectionEnum.ConstraintMarkets

    ConstraintDecisionVariables = plx_enums.CollectionEnum.ConstraintDecisionVariables

    ConstraintVariables = plx_enums.CollectionEnum.ConstraintVariables

    ConstraintConditions = plx_enums.CollectionEnum.ConstraintConditions

    DecisionVariableGenerators = plx_enums.CollectionEnum.DecisionVariableGenerators

    DecisionVariableNodes = plx_enums.CollectionEnum.DecisionVariableNodes

    DecisionVariableGasPlants = plx_enums.CollectionEnum.DecisionVariableGasPlants

    DecisionVariableWaterPlants = plx_enums.CollectionEnum.DecisionVariableWaterPlants

    DecisionVariableDefinition = plx_enums.CollectionEnum.DecisionVariableDefinition

    VariableGenerators = plx_enums.CollectionEnum.VariableGenerators

    VariableFuels = plx_enums.CollectionEnum.VariableFuels

    VariableReserves = plx_enums.CollectionEnum.VariableReserves

    VariableRegions = plx_enums.CollectionEnum.VariableRegions

    VariableZones = plx_enums.CollectionEnum.VariableZones

    VariableNodes = plx_enums.CollectionEnum.VariableNodes

    VariableLines = plx_enums.CollectionEnum.VariableLines

    VariableInterfaces = plx_enums.CollectionEnum.VariableInterfaces

    VariableStorages = plx_enums.CollectionEnum.VariableStorages

    VariableHeatNodes = plx_enums.CollectionEnum.VariableHeatNodes

    VariableHeatPlants = plx_enums.CollectionEnum.VariableHeatPlants

    VariableConditions = plx_enums.CollectionEnum.VariableConditions

    VariableVariables = plx_enums.CollectionEnum.VariableVariables

    GlobalStorages = plx_enums.CollectionEnum.GlobalStorages

    ModelScenarios = plx_enums.CollectionEnum.ModelScenarios

    ModelHorizon = plx_enums.CollectionEnum.ModelHorizon

    ModelReport = plx_enums.CollectionEnum.ModelReport

    ModelLTPlan = plx_enums.CollectionEnum.ModelLTPlan

    ModelPASA = plx_enums.CollectionEnum.ModelPASA

    ModelMTSchedule = plx_enums.CollectionEnum.ModelMTSchedule

    ModelSTSchedule = plx_enums.CollectionEnum.ModelSTSchedule

    ModelTransmission = plx_enums.CollectionEnum.ModelTransmission

    ModelProduction = plx_enums.CollectionEnum.ModelProduction

    ModelCompetition = plx_enums.CollectionEnum.ModelCompetition

    ModelStochastic = plx_enums.CollectionEnum.ModelStochastic

    ModelPerformance = plx_enums.CollectionEnum.ModelPerformance

    ModelDiagnostic = plx_enums.CollectionEnum.ModelDiagnostic

    ModelInterleaved = plx_enums.CollectionEnum.ModelInterleaved

    ProjectModels = plx_enums.CollectionEnum.ProjectModels

    ProjectHorizon = plx_enums.CollectionEnum.ProjectHorizon

    ProjectReport = plx_enums.CollectionEnum.ProjectReport

    ListGenerators = plx_enums.CollectionEnum.ListGenerators

    ListFuels = plx_enums.CollectionEnum.ListFuels

    ListFuelContracts = plx_enums.CollectionEnum.ListFuelContracts

    ListEmissions = plx_enums.CollectionEnum.ListEmissions

    ListAbatements = plx_enums.CollectionEnum.ListAbatements

    ListStorages = plx_enums.CollectionEnum.ListStorages

    ListWaterways = plx_enums.CollectionEnum.ListWaterways

    ListPowerStations = plx_enums.CollectionEnum.ListPowerStations

    ListPhysicalContracts = plx_enums.CollectionEnum.ListPhysicalContracts

    ListPurchasers = plx_enums.CollectionEnum.ListPurchasers

    ListReserves = plx_enums.CollectionEnum.ListReserves

    ListBatteries = plx_enums.CollectionEnum.ListBatteries

    ListMaintenances = plx_enums.CollectionEnum.ListMaintenances

    ListHeatPlants = plx_enums.CollectionEnum.ListHeatPlants

    ListHeatNodes = plx_enums.CollectionEnum.ListHeatNodes

    ListGasFields = plx_enums.CollectionEnum.ListGasFields

    ListGasPlants = plx_enums.CollectionEnum.ListGasPlants

    ListGasPipelines = plx_enums.CollectionEnum.ListGasPipelines

    ListGasNodes = plx_enums.CollectionEnum.ListGasNodes

    ListGasStorages = plx_enums.CollectionEnum.ListGasStorages

    ListGasDemands = plx_enums.CollectionEnum.ListGasDemands

    ListGasBasins = plx_enums.CollectionEnum.ListGasBasins

    ListGasZones = plx_enums.CollectionEnum.ListGasZones

    ListGasContracts = plx_enums.CollectionEnum.ListGasContracts

    ListGasTransports = plx_enums.CollectionEnum.ListGasTransports

    ListWaterPlants = plx_enums.CollectionEnum.ListWaterPlants

    ListWaterPipelines = plx_enums.CollectionEnum.ListWaterPipelines

    ListWaterNodes = plx_enums.CollectionEnum.ListWaterNodes

    ListWaterStorages = plx_enums.CollectionEnum.ListWaterStorages

    ListWaterDemands = plx_enums.CollectionEnum.ListWaterDemands

    ListWaterZones = plx_enums.CollectionEnum.ListWaterZones

    ListRegions = plx_enums.CollectionEnum.ListRegions

    ListZones = plx_enums.CollectionEnum.ListZones

    ListNodes = plx_enums.CollectionEnum.ListNodes

    ListLines = plx_enums.CollectionEnum.ListLines

    ListMLFs = plx_enums.CollectionEnum.ListMLFs

    ListTransformers = plx_enums.CollectionEnum.ListTransformers

    ListFlowControls = plx_enums.CollectionEnum.ListFlowControls

    ListInterfaces = plx_enums.CollectionEnum.ListInterfaces

    ListContingencies = plx_enums.CollectionEnum.ListContingencies

    ListCompanies = plx_enums.CollectionEnum.ListCompanies

    ListFinancialContracts = plx_enums.CollectionEnum.ListFinancialContracts

    ListHubs = plx_enums.CollectionEnum.ListHubs

    ListTransmissionRights = plx_enums.CollectionEnum.ListTransmissionRights

    ListCournots = plx_enums.CollectionEnum.ListCournots

    ListRSIs = plx_enums.CollectionEnum.ListRSIs

    ListMarkets = plx_enums.CollectionEnum.ListMarkets

    ListConstraints = plx_enums.CollectionEnum.ListConstraints

    ListDecisionVariables = plx_enums.CollectionEnum.ListDecisionVariables

    ListDataFiles = plx_enums.CollectionEnum.ListDataFiles

    ListVariables = plx_enums.CollectionEnum.ListVariables

    ListTimeslices = plx_enums.CollectionEnum.ListTimeslices

    ListGlobals = plx_enums.CollectionEnum.ListGlobals

    ListScenarios = plx_enums.CollectionEnum.ListScenarios

    ListLists = plx_enums.CollectionEnum.ListLists

    ReportLists = plx_enums.CollectionEnum.ReportLists


class CompanyBridgeEnum(Enum):
    Generation = plx_enums.CompanyBridgeEnum.Generation

    PoolRevenue = plx_enums.CompanyBridgeEnum.PoolRevenue

    Penalty = plx_enums.CompanyBridgeEnum.Penalty


class CompanyEmissionsEnum(Enum):
    Allocation = plx_enums.CompanyEmissionsEnum.Allocation


class CompanyRegionsEnum(Enum):
    LoadParticipationFactor = plx_enums.CompanyRegionsEnum.LoadParticipationFactor


class CompetitionAttributeEnum(Enum):
    EquilibriumModel = plx_enums.CompetitionAttributeEnum.EquilibriumModel

    DefaultElasticity = plx_enums.CompetitionAttributeEnum.DefaultElasticity

    DemandScaling = plx_enums.CompetitionAttributeEnum.DemandScaling

    RevenueTargetingMethod = plx_enums.CompetitionAttributeEnum.RevenueTargetingMethod

    RevenueTargetingIterations = plx_enums.CompetitionAttributeEnum.RevenueTargetingIterations

    PricingStrategy = plx_enums.CompetitionAttributeEnum.PricingStrategy

    BertrandDetectActiveRampConstraints = plx_enums.CompetitionAttributeEnum.BertrandDetectActiveRampConstraints

    BertrandOOMODEnabled = plx_enums.CompetitionAttributeEnum.BertrandOOMODEnabled

    Epsilon = plx_enums.CompetitionAttributeEnum.Epsilon

    RSIEnabled = plx_enums.CompetitionAttributeEnum.RSIEnabled

    RSIBidCostMarkupMethod = plx_enums.CompetitionAttributeEnum.RSIBidCostMarkupMethod

    NoLoadCostMarkup = plx_enums.CompetitionAttributeEnum.NoLoadCostMarkup

    MarkupMinStableLevel = plx_enums.CompetitionAttributeEnum.MarkupMinStableLevel

    StartCostMarkup = plx_enums.CompetitionAttributeEnum.StartCostMarkup

    StartCostMarkupProductionBands = plx_enums.CompetitionAttributeEnum.StartCostMarkupProductionBands

    StartCostMarkupWindow = plx_enums.CompetitionAttributeEnum.StartCostMarkupWindow

    ContractsOptimizeOffers = plx_enums.CompetitionAttributeEnum.ContractsOptimizeOffers

    ContractsSettlementMethod = plx_enums.CompetitionAttributeEnum.ContractsSettlementMethod

    ContractsHandoffPoint = plx_enums.CompetitionAttributeEnum.ContractsHandoffPoint

    MarketTradingFormat = plx_enums.CompetitionAttributeEnum.MarketTradingFormat


class CompetitionEquilibriumModelEnum(Enum):
    PerfectCompetition = plx_enums.CompetitionEquilibriumModelEnum.PerfectCompetition

    CostRecovery = plx_enums.CompetitionEquilibriumModelEnum.CostRecovery

    Cournot = plx_enums.CompetitionEquilibriumModelEnum.Cournot


class CompetitionPricingStrategyEnum(Enum):
    None_ = 0

    NoCongestion = plx_enums.CompetitionPricingStrategyEnum.NoCongestion

    Interregional = plx_enums.CompetitionPricingStrategyEnum.Interregional

    Intraregional = plx_enums.CompetitionPricingStrategyEnum.Intraregional


class CompetitionRSIBidCostMarkupMethod(Enum):
    VariableByMeritOrder = plx_enums.CompetitionRSIBidCostMarkupMethod.VariableByMeritOrder

    VariableBySupplyCapacity = plx_enums.CompetitionRSIBidCostMarkupMethod.VariableBySupplyCapacity

    Uniform = plx_enums.CompetitionRSIBidCostMarkupMethod.Uniform


class CompetitionRSIScenario(Enum):
    Base = plx_enums.CompetitionRSIScenario.Base

    Low = plx_enums.CompetitionRSIScenario.Low

    High = plx_enums.CompetitionRSIScenario.High


class CompetitionRevenueTargetingMethodEnum(Enum):
    IncrementOnly = plx_enums.CompetitionRevenueTargetingMethodEnum.IncrementOnly

    DecrementOnly = plx_enums.CompetitionRevenueTargetingMethodEnum.DecrementOnly

    IncrementandDecrement = plx_enums.CompetitionRevenueTargetingMethodEnum.IncrementandDecrement


class ComplementEnum(Enum):
    GeneratorInheritors = plx_enums.ComplementEnum.GeneratorInheritors

    FuelInheritors = plx_enums.ComplementEnum.FuelInheritors

    FuelContractInheritors = plx_enums.ComplementEnum.FuelContractInheritors

    EmissionInheritors = plx_enums.ComplementEnum.EmissionInheritors

    AbatementInheritors = plx_enums.ComplementEnum.AbatementInheritors

    StorageInheritors = plx_enums.ComplementEnum.StorageInheritors

    WaterwayInheritors = plx_enums.ComplementEnum.WaterwayInheritors

    PowerStationInheritors = plx_enums.ComplementEnum.PowerStationInheritors

    PhysicalContractInheritors = plx_enums.ComplementEnum.PhysicalContractInheritors

    PurchaserInheritors = plx_enums.ComplementEnum.PurchaserInheritors

    ReserveInheritors = plx_enums.ComplementEnum.ReserveInheritors

    BatteryInheritors = plx_enums.ComplementEnum.BatteryInheritors

    MaintenanceInheritors = plx_enums.ComplementEnum.MaintenanceInheritors

    HeatPlantInheritors = plx_enums.ComplementEnum.HeatPlantInheritors

    HeatNodeInheritors = plx_enums.ComplementEnum.HeatNodeInheritors

    GasFieldInheritors = plx_enums.ComplementEnum.GasFieldInheritors

    GasPlantInheritors = plx_enums.ComplementEnum.GasPlantInheritors

    GasPipelineInheritors = plx_enums.ComplementEnum.GasPipelineInheritors

    GasNodeInheritors = plx_enums.ComplementEnum.GasNodeInheritors

    GasStorageInheritors = plx_enums.ComplementEnum.GasStorageInheritors

    GasDemandInheritors = plx_enums.ComplementEnum.GasDemandInheritors

    GasBasinInheritors = plx_enums.ComplementEnum.GasBasinInheritors

    GasZoneInheritors = plx_enums.ComplementEnum.GasZoneInheritors

    GasContractInheritors = plx_enums.ComplementEnum.GasContractInheritors

    WaterPlantInheritors = plx_enums.ComplementEnum.WaterPlantInheritors

    WaterPipelineInheritors = plx_enums.ComplementEnum.WaterPipelineInheritors

    WaterNodeInheritors = plx_enums.ComplementEnum.WaterNodeInheritors

    WaterStorageInheritors = plx_enums.ComplementEnum.WaterStorageInheritors

    WaterDemandInheritors = plx_enums.ComplementEnum.WaterDemandInheritors

    WaterZoneInheritors = plx_enums.ComplementEnum.WaterZoneInheritors

    RegionInheritors = plx_enums.ComplementEnum.RegionInheritors

    ZoneInheritors = plx_enums.ComplementEnum.ZoneInheritors

    NodeInheritors = plx_enums.ComplementEnum.NodeInheritors

    LineInheritors = plx_enums.ComplementEnum.LineInheritors

    MLFInheritors = plx_enums.ComplementEnum.MLFInheritors

    TransformerInheritors = plx_enums.ComplementEnum.TransformerInheritors

    FlowControlInheritors = plx_enums.ComplementEnum.FlowControlInheritors

    InterfaceInheritors = plx_enums.ComplementEnum.InterfaceInheritors

    ContingencyInheritors = plx_enums.ComplementEnum.ContingencyInheritors

    CompanyInheritors = plx_enums.ComplementEnum.CompanyInheritors

    FinancialContractInheritors = plx_enums.ComplementEnum.FinancialContractInheritors

    HubInheritors = plx_enums.ComplementEnum.HubInheritors

    TransmissionRightInheritors = plx_enums.ComplementEnum.TransmissionRightInheritors

    CournotInheritors = plx_enums.ComplementEnum.CournotInheritors

    RSIInheritors = plx_enums.ComplementEnum.RSIInheritors

    MarketInheritors = plx_enums.ComplementEnum.MarketInheritors

    ConstraintInheritors = plx_enums.ComplementEnum.ConstraintInheritors

    DecisionVariableInheritors = plx_enums.ComplementEnum.DecisionVariableInheritors

    GeneratorHeatOutput = plx_enums.ComplementEnum.GeneratorHeatOutput

    FuelGenerators = plx_enums.ComplementEnum.FuelGenerators

    FuelGeneratorsStarted = plx_enums.ComplementEnum.FuelGeneratorsStarted

    StorageExportingGenerators = plx_enums.ComplementEnum.StorageExportingGenerators

    StorageImportingGenerators = plx_enums.ComplementEnum.StorageImportingGenerators

    PowerStationGenerators = plx_enums.ComplementEnum.PowerStationGenerators

    MarketGenerators = plx_enums.ComplementEnum.MarketGenerators

    GasNodeGenerators = plx_enums.ComplementEnum.GasNodeGenerators

    WaterNodeGenerators = plx_enums.ComplementEnum.WaterNodeGenerators

    NodeGenerators = plx_enums.ComplementEnum.NodeGenerators

    NodeGenerators_star_ = plx_enums.ComplementEnum.NodeGenerators_star_

    CompanyGenerators = plx_enums.ComplementEnum.CompanyGenerators

    GasNodeFuels = plx_enums.ComplementEnum.GasNodeFuels

    CompanyFuels = plx_enums.ComplementEnum.CompanyFuels

    GeneratorFuelContracts = plx_enums.ComplementEnum.GeneratorFuelContracts

    FuelFuelContracts = plx_enums.ComplementEnum.FuelFuelContracts

    CompanyFuelContracts = plx_enums.ComplementEnum.CompanyFuelContracts

    GeneratorEmissions = plx_enums.ComplementEnum.GeneratorEmissions

    FuelEmissions = plx_enums.ComplementEnum.FuelEmissions

    GasNodeEmissions = plx_enums.ComplementEnum.GasNodeEmissions

    GasPlantEmissions = plx_enums.ComplementEnum.GasPlantEmissions

    WaterPlantEmissions = plx_enums.ComplementEnum.WaterPlantEmissions

    GeneratorAbatements = plx_enums.ComplementEnum.GeneratorAbatements

    EmissionAbatements = plx_enums.ComplementEnum.EmissionAbatements

    FuelAbatements = plx_enums.ComplementEnum.FuelAbatements

    WaterNodeStorages = plx_enums.ComplementEnum.WaterNodeStorages

    StorageExportingWaterways = plx_enums.ComplementEnum.StorageExportingWaterways

    StorageImportingWaterways = plx_enums.ComplementEnum.StorageImportingWaterways

    NodeGenerationContracts = plx_enums.ComplementEnum.NodeGenerationContracts

    NodeLoadContracts = plx_enums.ComplementEnum.NodeLoadContracts

    CompanyPhysicalContracts = plx_enums.ComplementEnum.CompanyPhysicalContracts

    NodePurchasers = plx_enums.ComplementEnum.NodePurchasers

    NodePurchasers_star_ = plx_enums.ComplementEnum.NodePurchasers_star_

    CompanyPurchasers = plx_enums.ComplementEnum.CompanyPurchasers

    GeneratorReserves = plx_enums.ComplementEnum.GeneratorReserves

    PurchaserReserves = plx_enums.ComplementEnum.PurchaserReserves

    GeneratorContingencyReserves = plx_enums.ComplementEnum.GeneratorContingencyReserves

    GeneratorReserveCostsAllocated = plx_enums.ComplementEnum.GeneratorReserveCostsAllocated

    BatteryReserves = plx_enums.ComplementEnum.BatteryReserves

    ReserveMasterReserves = plx_enums.ComplementEnum.ReserveMasterReserves

    RegionContingencyReserves = plx_enums.ComplementEnum.RegionContingencyReserves

    LineContingencyReserves = plx_enums.ComplementEnum.LineContingencyReserves

    NodeBatteries = plx_enums.ComplementEnum.NodeBatteries

    NodeBatteries_star_ = plx_enums.ComplementEnum.NodeBatteries_star_

    CompanyBatteries = plx_enums.ComplementEnum.CompanyBatteries

    GeneratorMaintenances = plx_enums.ComplementEnum.GeneratorMaintenances

    GasPipelineMaintenances = plx_enums.ComplementEnum.GasPipelineMaintenances

    LineMaintenances = plx_enums.ComplementEnum.LineMaintenances

    MaintenanceDependencies = plx_enums.ComplementEnum.MaintenanceDependencies

    HeatNodeGeneratorsSupplied = plx_enums.ComplementEnum.HeatNodeGeneratorsSupplied

    HeatNodeSupplyingGenerators = plx_enums.ComplementEnum.HeatNodeSupplyingGenerators

    FuelHeatPlants = plx_enums.ComplementEnum.FuelHeatPlants

    NodeHeatPlants = plx_enums.ComplementEnum.NodeHeatPlants

    HeatNodeInputHeatPlants = plx_enums.ComplementEnum.HeatNodeInputHeatPlants

    HeatNodeOutputHeatPlants = plx_enums.ComplementEnum.HeatNodeOutputHeatPlants

    FuelHeatPlantsStarted = plx_enums.ComplementEnum.FuelHeatPlantsStarted

    HeatNodeHeatImportNodes = plx_enums.ComplementEnum.HeatNodeHeatImportNodes

    WaterPlantHeatNodes = plx_enums.ComplementEnum.WaterPlantHeatNodes

    CompanyGasFields = plx_enums.ComplementEnum.CompanyGasFields

    GasNodeGasFields = plx_enums.ComplementEnum.GasNodeGasFields

    GasBasinGasFields = plx_enums.ComplementEnum.GasBasinGasFields

    GasNodeGasPlantsSupplied = plx_enums.ComplementEnum.GasNodeGasPlantsSupplied

    GasNodeSupplyingGasPlants = plx_enums.ComplementEnum.GasNodeSupplyingGasPlants

    NodeGasPlants = plx_enums.ComplementEnum.NodeGasPlants

    GasNodeExportingGasPipelines = plx_enums.ComplementEnum.GasNodeExportingGasPipelines

    GasNodeImportingGasPipelines = plx_enums.ComplementEnum.GasNodeImportingGasPipelines

    GasZoneGasNodes = plx_enums.ComplementEnum.GasZoneGasNodes

    GasNodeGasStorages = plx_enums.ComplementEnum.GasNodeGasStorages

    GasNodeGasDemands = plx_enums.ComplementEnum.GasNodeGasDemands

    CompanyGasDemands = plx_enums.ComplementEnum.CompanyGasDemands

    GasFieldGasContracts = plx_enums.ComplementEnum.GasFieldGasContracts

    GasPipelineGasContracts = plx_enums.ComplementEnum.GasPipelineGasContracts

    GasTransportGasContracts = plx_enums.ComplementEnum.GasTransportGasContracts

    GasNodeExportingGasTransports = plx_enums.ComplementEnum.GasNodeExportingGasTransports

    GasNodeImportingGasTransports = plx_enums.ComplementEnum.GasNodeImportingGasTransports

    WaterNodeWaterPlantSupplied = plx_enums.ComplementEnum.WaterNodeWaterPlantSupplied

    WaterNodeSupplyingWaterPlants = plx_enums.ComplementEnum.WaterNodeSupplyingWaterPlants

    NodeWaterPlants = plx_enums.ComplementEnum.NodeWaterPlants

    WaterNodeExportingWaterPipelines = plx_enums.ComplementEnum.WaterNodeExportingWaterPipelines

    WaterNodeImportingWaterPipelines = plx_enums.ComplementEnum.WaterNodeImportingWaterPipelines

    WaterZoneWaterNodes = plx_enums.ComplementEnum.WaterZoneWaterNodes

    NodeWaterNodes = plx_enums.ComplementEnum.NodeWaterNodes

    WaterNodeWaterStorages = plx_enums.ComplementEnum.WaterNodeWaterStorages

    WaterNodeWaterDemands = plx_enums.ComplementEnum.WaterNodeWaterDemands

    GeneratorRegions = plx_enums.ComplementEnum.GeneratorRegions

    EmissionRegions = plx_enums.ComplementEnum.EmissionRegions

    PurchaserRegions = plx_enums.ComplementEnum.PurchaserRegions

    BatteryRegions = plx_enums.ComplementEnum.BatteryRegions

    GeneratorCapacityZones = plx_enums.ComplementEnum.GeneratorCapacityZones

    GeneratorZones = plx_enums.ComplementEnum.GeneratorZones

    EmissionZones = plx_enums.ComplementEnum.EmissionZones

    PurchaserCapacityZones = plx_enums.ComplementEnum.PurchaserCapacityZones

    PurchaserZones = plx_enums.ComplementEnum.PurchaserZones

    BatteryCapacityZones = plx_enums.ComplementEnum.BatteryCapacityZones

    BatteryZones = plx_enums.ComplementEnum.BatteryZones

    RegionZones = plx_enums.ComplementEnum.RegionZones

    RegionNodes = plx_enums.ComplementEnum.RegionNodes

    ZoneCapacityNodes = plx_enums.ComplementEnum.ZoneCapacityNodes

    ZoneNodes = plx_enums.ComplementEnum.ZoneNodes

    HubNodes = plx_enums.ComplementEnum.HubNodes

    NodeExportingLines = plx_enums.ComplementEnum.NodeExportingLines

    NodeImportingLines = plx_enums.ComplementEnum.NodeImportingLines

    CompanyLines = plx_enums.ComplementEnum.CompanyLines

    NodeExportingTransformers = plx_enums.ComplementEnum.NodeExportingTransformers

    NodeImportingTransformers = plx_enums.ComplementEnum.NodeImportingTransformers

    LineFlowControls = plx_enums.ComplementEnum.LineFlowControls

    LineFlowControls_star_ = plx_enums.ComplementEnum.LineFlowControls_star_

    LineInterfaces = plx_enums.ComplementEnum.LineInterfaces

    TransformerInterfaces = plx_enums.ComplementEnum.TransformerInterfaces

    GeneratorContingencies = plx_enums.ComplementEnum.GeneratorContingencies

    LineContingencies = plx_enums.ComplementEnum.LineContingencies

    LineMonitoringContingencies = plx_enums.ComplementEnum.LineMonitoringContingencies

    TransformerMonitoringContingencies = plx_enums.ComplementEnum.TransformerMonitoringContingencies

    TransformerContingencies = plx_enums.ComplementEnum.TransformerContingencies

    InterfaceMonitoringContingencies = plx_enums.ComplementEnum.InterfaceMonitoringContingencies

    EmissionCompanies = plx_enums.ComplementEnum.EmissionCompanies

    RegionCompanies = plx_enums.ComplementEnum.RegionCompanies

    GeneratorFinancialContracts = plx_enums.ComplementEnum.GeneratorFinancialContracts

    RegionFinancialContracts = plx_enums.ComplementEnum.RegionFinancialContracts

    CompanyGenerationContracts = plx_enums.ComplementEnum.CompanyGenerationContracts

    CompanyPurchaseContracts = plx_enums.ComplementEnum.CompanyPurchaseContracts

    VariableFinancialContracts = plx_enums.ComplementEnum.VariableFinancialContracts

    CompanyTransmissionRights = plx_enums.ComplementEnum.CompanyTransmissionRights

    GeneratorCapacityMarkets = plx_enums.ComplementEnum.GeneratorCapacityMarkets

    GeneratorHeatMarkets = plx_enums.ComplementEnum.GeneratorHeatMarkets

    FuelMarkets = plx_enums.ComplementEnum.FuelMarkets

    EmissionMarkets = plx_enums.ComplementEnum.EmissionMarkets

    ReserveMarkets = plx_enums.ComplementEnum.ReserveMarkets

    GasNodeGasMarkets = plx_enums.ComplementEnum.GasNodeGasMarkets

    NodeEnergyMarkets = plx_enums.ComplementEnum.NodeEnergyMarkets

    CompanyMarkets = plx_enums.ComplementEnum.CompanyMarkets

    GeneratorConstraints = plx_enums.ComplementEnum.GeneratorConstraints

    FuelConstraints = plx_enums.ComplementEnum.FuelConstraints

    FuelContractConstraints = plx_enums.ComplementEnum.FuelContractConstraints

    EmissionConstraints = plx_enums.ComplementEnum.EmissionConstraints

    AbatementConstraints = plx_enums.ComplementEnum.AbatementConstraints

    StorageConstraints = plx_enums.ComplementEnum.StorageConstraints

    WaterwayConstraints = plx_enums.ComplementEnum.WaterwayConstraints

    PhysicalContractConstraints = plx_enums.ComplementEnum.PhysicalContractConstraints

    PurchaserConstraints = plx_enums.ComplementEnum.PurchaserConstraints

    ReserveConstraints = plx_enums.ComplementEnum.ReserveConstraints

    BatteryConstraints = plx_enums.ComplementEnum.BatteryConstraints

    MaintenanceConstraints = plx_enums.ComplementEnum.MaintenanceConstraints

    HeatPlantConstraints = plx_enums.ComplementEnum.HeatPlantConstraints

    HeatNodeConstraints = plx_enums.ComplementEnum.HeatNodeConstraints

    GasFieldConstraints = plx_enums.ComplementEnum.GasFieldConstraints

    GasPlantConstraints = plx_enums.ComplementEnum.GasPlantConstraints

    GasPipelineConstraints = plx_enums.ComplementEnum.GasPipelineConstraints

    GasNodeConstraints = plx_enums.ComplementEnum.GasNodeConstraints

    GasStorageConstraints = plx_enums.ComplementEnum.GasStorageConstraints

    GasBasinConstraints = plx_enums.ComplementEnum.GasBasinConstraints

    GasContractConstraints = plx_enums.ComplementEnum.GasContractConstraints

    GasTransportConstraints = plx_enums.ComplementEnum.GasTransportConstraints

    WaterPlantConstraints = plx_enums.ComplementEnum.WaterPlantConstraints

    WaterPipelineConstraints = plx_enums.ComplementEnum.WaterPipelineConstraints

    WaterNodeConstraints = plx_enums.ComplementEnum.WaterNodeConstraints

    WaterStorageConstraints = plx_enums.ComplementEnum.WaterStorageConstraints

    RegionConstraints = plx_enums.ComplementEnum.RegionConstraints

    ZoneConstraints = plx_enums.ComplementEnum.ZoneConstraints

    NodeConstraints = plx_enums.ComplementEnum.NodeConstraints

    LineConstraints = plx_enums.ComplementEnum.LineConstraints

    TransformerConstraints = plx_enums.ComplementEnum.TransformerConstraints

    FlowControlConstraints = plx_enums.ComplementEnum.FlowControlConstraints

    InterfaceConstraints = plx_enums.ComplementEnum.InterfaceConstraints

    CompanyConstraints = plx_enums.ComplementEnum.CompanyConstraints

    HubConstraints = plx_enums.ComplementEnum.HubConstraints

    MarketConstraints = plx_enums.ComplementEnum.MarketConstraints

    DecisionVariableConstraints = plx_enums.ComplementEnum.DecisionVariableConstraints

    VariableConstraints = plx_enums.ComplementEnum.VariableConstraints

    VariableConditionalConstraints = plx_enums.ComplementEnum.VariableConditionalConstraints

    GeneratorDecisionVariables = plx_enums.ComplementEnum.GeneratorDecisionVariables

    NodeDecisionVariables = plx_enums.ComplementEnum.NodeDecisionVariables

    GasPlantDecisionVariables = plx_enums.ComplementEnum.GasPlantDecisionVariables

    WaterPlantDecisionVariables = plx_enums.ComplementEnum.WaterPlantDecisionVariables

    ConstraintDefinitions = plx_enums.ComplementEnum.ConstraintDefinitions

    GeneratorConditions = plx_enums.ComplementEnum.GeneratorConditions

    FuelConditions = plx_enums.ComplementEnum.FuelConditions

    ReserveConditions = plx_enums.ComplementEnum.ReserveConditions

    RegionConditions = plx_enums.ComplementEnum.RegionConditions

    ZoneConditions = plx_enums.ComplementEnum.ZoneConditions

    NodeConditions = plx_enums.ComplementEnum.NodeConditions

    LineConditions = plx_enums.ComplementEnum.LineConditions

    InterfaceConditions = plx_enums.ComplementEnum.InterfaceConditions

    StorageConditions = plx_enums.ComplementEnum.StorageConditions

    HeatNodeConditions = plx_enums.ComplementEnum.HeatNodeConditions

    HeatPlantConditions = plx_enums.ComplementEnum.HeatPlantConditions

    StorageGlobals = plx_enums.ComplementEnum.StorageGlobals

    ScenarioModels = plx_enums.ComplementEnum.ScenarioModels

    HorizonModels = plx_enums.ComplementEnum.HorizonModels

    ReportModels = plx_enums.ComplementEnum.ReportModels

    LTPlanModels = plx_enums.ComplementEnum.LTPlanModels

    PASAModels = plx_enums.ComplementEnum.PASAModels

    MTScheduleModels = plx_enums.ComplementEnum.MTScheduleModels

    STScheduleModels = plx_enums.ComplementEnum.STScheduleModels

    TransmissionModels = plx_enums.ComplementEnum.TransmissionModels

    ProductionModels = plx_enums.ComplementEnum.ProductionModels

    CompetitionModels = plx_enums.ComplementEnum.CompetitionModels

    StochasticModels = plx_enums.ComplementEnum.StochasticModels

    PerformanceModels = plx_enums.ComplementEnum.PerformanceModels

    DiagnosticModels = plx_enums.ComplementEnum.DiagnosticModels

    ModelProjects = plx_enums.ComplementEnum.ModelProjects

    HorizonProjects = plx_enums.ComplementEnum.HorizonProjects

    ReportProjects = plx_enums.ComplementEnum.ReportProjects

    GeneratorLists = plx_enums.ComplementEnum.GeneratorLists

    FuelLists = plx_enums.ComplementEnum.FuelLists

    FuelContractLists = plx_enums.ComplementEnum.FuelContractLists

    EmissionLists = plx_enums.ComplementEnum.EmissionLists

    AbatementLists = plx_enums.ComplementEnum.AbatementLists

    StorageLists = plx_enums.ComplementEnum.StorageLists

    WaterwayLists = plx_enums.ComplementEnum.WaterwayLists

    PowerStationLists = plx_enums.ComplementEnum.PowerStationLists

    PhysicalContractLists = plx_enums.ComplementEnum.PhysicalContractLists

    PurchaserLists = plx_enums.ComplementEnum.PurchaserLists

    ReserveLists = plx_enums.ComplementEnum.ReserveLists

    BatteryLists = plx_enums.ComplementEnum.BatteryLists

    MaintenanceLists = plx_enums.ComplementEnum.MaintenanceLists

    HeatPlantLists = plx_enums.ComplementEnum.HeatPlantLists

    HeatNodeLists = plx_enums.ComplementEnum.HeatNodeLists

    GasFieldLists = plx_enums.ComplementEnum.GasFieldLists

    GasPlantLists = plx_enums.ComplementEnum.GasPlantLists

    GasPipelineLists = plx_enums.ComplementEnum.GasPipelineLists

    GasNodeLists = plx_enums.ComplementEnum.GasNodeLists

    GasStorageLists = plx_enums.ComplementEnum.GasStorageLists

    GasDemandLists = plx_enums.ComplementEnum.GasDemandLists

    GasBasinLists = plx_enums.ComplementEnum.GasBasinLists

    GasZoneLists = plx_enums.ComplementEnum.GasZoneLists

    GasContractLists = plx_enums.ComplementEnum.GasContractLists

    GasTransportLists = plx_enums.ComplementEnum.GasTransportLists

    WaterPlantLists = plx_enums.ComplementEnum.WaterPlantLists

    WaterPipelineLists = plx_enums.ComplementEnum.WaterPipelineLists

    WaterNodeLists = plx_enums.ComplementEnum.WaterNodeLists

    WaterStorageLists = plx_enums.ComplementEnum.WaterStorageLists

    WaterDemandLists = plx_enums.ComplementEnum.WaterDemandLists

    WaterZoneLists = plx_enums.ComplementEnum.WaterZoneLists

    RegionLists = plx_enums.ComplementEnum.RegionLists

    ZoneLists = plx_enums.ComplementEnum.ZoneLists

    NodeLists = plx_enums.ComplementEnum.NodeLists

    LineLists = plx_enums.ComplementEnum.LineLists

    MLFLists = plx_enums.ComplementEnum.MLFLists

    TransformerLists = plx_enums.ComplementEnum.TransformerLists

    FlowControlLists = plx_enums.ComplementEnum.FlowControlLists

    InterfaceLists = plx_enums.ComplementEnum.InterfaceLists

    ContingencyLists = plx_enums.ComplementEnum.ContingencyLists

    CompanyLists = plx_enums.ComplementEnum.CompanyLists

    FinancialContractLists = plx_enums.ComplementEnum.FinancialContractLists

    HubLists = plx_enums.ComplementEnum.HubLists

    TransmissionRightLists = plx_enums.ComplementEnum.TransmissionRightLists

    CournotLists = plx_enums.ComplementEnum.CournotLists

    RSILists = plx_enums.ComplementEnum.RSILists

    MarketLists = plx_enums.ComplementEnum.MarketLists

    ConstraintLists = plx_enums.ComplementEnum.ConstraintLists

    DecisionVariableLists = plx_enums.ComplementEnum.DecisionVariableLists

    DataFileLists = plx_enums.ComplementEnum.DataFileLists

    VariableLists = plx_enums.ComplementEnum.VariableLists

    TimesliceLists = plx_enums.ComplementEnum.TimesliceLists

    GlobalLists = plx_enums.ComplementEnum.GlobalLists

    ScenarioLists = plx_enums.ComplementEnum.ScenarioLists

    ListReports = plx_enums.ComplementEnum.ListReports


class ConstraintAbatementsEnum(Enum):
    AbatementCoefficient = plx_enums.ConstraintAbatementsEnum.AbatementCoefficient

    OperatingHoursCoefficient = plx_enums.ConstraintAbatementsEnum.OperatingHoursCoefficient


class ConstraintBatteriesEnum(Enum):
    EnergyCoefficient = plx_enums.ConstraintBatteriesEnum.EnergyCoefficient

    GenerationCoefficient = plx_enums.ConstraintBatteriesEnum.GenerationCoefficient

    LoadCoefficient = plx_enums.ConstraintBatteriesEnum.LoadCoefficient

    RampCoefficient = plx_enums.ConstraintBatteriesEnum.RampCoefficient

    RampUpCoefficient = plx_enums.ConstraintBatteriesEnum.RampUpCoefficient

    RampDownCoefficient = plx_enums.ConstraintBatteriesEnum.RampDownCoefficient

    RampUpViolationCoefficient = plx_enums.ConstraintBatteriesEnum.RampUpViolationCoefficient

    RampDownViolationCoefficient = plx_enums.ConstraintBatteriesEnum.RampDownViolationCoefficient

    ReserveProvisionCoefficient = plx_enums.ConstraintBatteriesEnum.ReserveProvisionCoefficient

    SpinningReserveCoefficient = plx_enums.ConstraintBatteriesEnum.SpinningReserveCoefficient

    PumpDispatchableLoadCoefficient = plx_enums.ConstraintBatteriesEnum.PumpDispatchableLoadCoefficient

    RaiseReserveProvisionCoefficient = plx_enums.ConstraintBatteriesEnum.RaiseReserveProvisionCoefficient

    LowerReserveProvisionCoefficient = plx_enums.ConstraintBatteriesEnum.LowerReserveProvisionCoefficient

    RegulationRaiseReserveProvisionCoefficient = plx_enums.ConstraintBatteriesEnum.RegulationRaiseReserveProvisionCoefficient

    RegulationLowerReserveProvisionCoefficient = plx_enums.ConstraintBatteriesEnum.RegulationLowerReserveProvisionCoefficient

    ReplacementReserveProvisionCoefficient = plx_enums.ConstraintBatteriesEnum.ReplacementReserveProvisionCoefficient

    ReserveUnitsCoefficient = plx_enums.ConstraintBatteriesEnum.ReserveUnitsCoefficient

    OperatingReserveUnitsCoefficient = plx_enums.ConstraintBatteriesEnum.OperatingReserveUnitsCoefficient

    CyclesCoefficient = plx_enums.ConstraintBatteriesEnum.CyclesCoefficient

    AgeCoefficient = plx_enums.ConstraintBatteriesEnum.AgeCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintBatteriesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintBatteriesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintBatteriesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintBatteriesEnum.UnitsRetiredinYearCoefficient

    CapacityBuiltCoefficient = plx_enums.ConstraintBatteriesEnum.CapacityBuiltCoefficient

    CapacityRetiredCoefficient = plx_enums.ConstraintBatteriesEnum.CapacityRetiredCoefficient

    CapacityReservesCoefficient = plx_enums.ConstraintBatteriesEnum.CapacityReservesCoefficient

    BuildCostCoefficient = plx_enums.ConstraintBatteriesEnum.BuildCostCoefficient

    BuiltCoefficient = plx_enums.ConstraintBatteriesEnum.BuiltCoefficient

    BuiltinYearCoefficient = plx_enums.ConstraintBatteriesEnum.BuiltinYearCoefficient


class ConstraintBridgeEnum(Enum):
    RHS = plx_enums.ConstraintBridgeEnum.RHS

    PenaltyQuantity = plx_enums.ConstraintBridgeEnum.PenaltyQuantity

    PenaltyPrice = plx_enums.ConstraintBridgeEnum.PenaltyPrice

    Slack = plx_enums.ConstraintBridgeEnum.Slack

    Activity = plx_enums.ConstraintBridgeEnum.Activity

    Violation = plx_enums.ConstraintBridgeEnum.Violation

    Price = plx_enums.ConstraintBridgeEnum.Price


class ConstraintCompaniesEnum(Enum):
    GenerationCoefficient = plx_enums.ConstraintCompaniesEnum.GenerationCoefficient

    CommittedCapacityCoefficient = plx_enums.ConstraintCompaniesEnum.CommittedCapacityCoefficient

    ContractVolumeCoefficient = plx_enums.ConstraintCompaniesEnum.ContractVolumeCoefficient


class ConstraintConditionLogicEnum(Enum):
    AND1 = plx_enums.ConstraintConditionLogicEnum.AND1

    OR1 = plx_enums.ConstraintConditionLogicEnum.OR1


class ConstraintConditionMethodEnum(Enum):
    Ignore = plx_enums.ConstraintConditionMethodEnum.Ignore

    Iterate = plx_enums.ConstraintConditionMethodEnum.Iterate

    Optimize = plx_enums.ConstraintConditionMethodEnum.Optimize


class ConstraintConditionsEnum(Enum):
    RHSCoefficient = plx_enums.ConstraintConditionsEnum.RHSCoefficient


class ConstraintDecisionVariablesEnum(Enum):
    ValueCoefficient = plx_enums.ConstraintDecisionVariablesEnum.ValueCoefficient

    ValueSquaredCoefficient = plx_enums.ConstraintDecisionVariablesEnum.ValueSquaredCoefficient


class ConstraintDecompositionMethodEnum(Enum):
    Quantity = plx_enums.ConstraintDecompositionMethodEnum.Quantity

    Price = plx_enums.ConstraintDecompositionMethodEnum.Price


class ConstraintEmissionsEnum(Enum):
    ProductionCoefficient = plx_enums.ConstraintEmissionsEnum.ProductionCoefficient

    AbatementCoefficient = plx_enums.ConstraintEmissionsEnum.AbatementCoefficient


class ConstraintFlowControlsEnum(Enum):
    AngleCoefficient = plx_enums.ConstraintFlowControlsEnum.AngleCoefficient

    PositiveAngleCoefficient = plx_enums.ConstraintFlowControlsEnum.PositiveAngleCoefficient

    NegativeAngleCoefficient = plx_enums.ConstraintFlowControlsEnum.NegativeAngleCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintFlowControlsEnum.UnitsBuiltCoefficient


class ConstraintFuelContractsEnum(Enum):
    OfftakeCoefficient = plx_enums.ConstraintFuelContractsEnum.OfftakeCoefficient


class ConstraintFuelsEnum(Enum):
    OfftakeCoefficient = plx_enums.ConstraintFuelsEnum.OfftakeCoefficient

    EmissionCoefficient = plx_enums.ConstraintFuelsEnum.EmissionCoefficient

    InUseCoefficient = plx_enums.ConstraintFuelsEnum.InUseCoefficient

    ClosingInventoryCoefficient = plx_enums.ConstraintFuelsEnum.ClosingInventoryCoefficient

    InventoryChangeCoefficient = plx_enums.ConstraintFuelsEnum.InventoryChangeCoefficient

    DeliveryCoefficient = plx_enums.ConstraintFuelsEnum.DeliveryCoefficient

    WithdrawalCoefficient = plx_enums.ConstraintFuelsEnum.WithdrawalCoefficient

    GenerationCoefficient = plx_enums.ConstraintFuelsEnum.GenerationCoefficient


class ConstraintGasBasinsEnum(Enum):
    ProductionCoefficient = plx_enums.ConstraintGasBasinsEnum.ProductionCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGasBasinsEnum.UnitsBuiltCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGasBasinsEnum.UnitsBuiltinYearCoefficient


class ConstraintGasContractsEnum(Enum):
    ProductionCoefficient = plx_enums.ConstraintGasContractsEnum.ProductionCoefficient


class ConstraintGasFieldsEnum(Enum):
    EndVolumeCoefficient = plx_enums.ConstraintGasFieldsEnum.EndVolumeCoefficient

    ProductionCoefficient = plx_enums.ConstraintGasFieldsEnum.ProductionCoefficient

    RampCoefficient = plx_enums.ConstraintGasFieldsEnum.RampCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGasFieldsEnum.UnitsBuiltCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGasFieldsEnum.UnitsBuiltinYearCoefficient


class ConstraintGasNodesEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintGasNodesEnum.FlowCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGasNodesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintGasNodesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGasNodesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintGasNodesEnum.UnitsRetiredinYearCoefficient


class ConstraintGasPipelinesEnum(Enum):
    EndVolumeCoefficient = plx_enums.ConstraintGasPipelinesEnum.EndVolumeCoefficient

    FlowCoefficient = plx_enums.ConstraintGasPipelinesEnum.FlowCoefficient

    FlowForwardCoefficient = plx_enums.ConstraintGasPipelinesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.ConstraintGasPipelinesEnum.FlowBackCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGasPipelinesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintGasPipelinesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGasPipelinesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintGasPipelinesEnum.UnitsRetiredinYearCoefficient


class ConstraintGasPlantsEnum(Enum):
    ProductionCoefficient = plx_enums.ConstraintGasPlantsEnum.ProductionCoefficient

    CapacityFactorCoefficient = plx_enums.ConstraintGasPlantsEnum.CapacityFactorCoefficient

    OperatingHoursCoefficient = plx_enums.ConstraintGasPlantsEnum.OperatingHoursCoefficient

    EnergyUsageCoefficient = plx_enums.ConstraintGasPlantsEnum.EnergyUsageCoefficient

    InstalledCapacityCoefficient = plx_enums.ConstraintGasPlantsEnum.InstalledCapacityCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGasPlantsEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintGasPlantsEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGasPlantsEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintGasPlantsEnum.UnitsRetiredinYearCoefficient

    CapacityBuiltCoefficient = plx_enums.ConstraintGasPlantsEnum.CapacityBuiltCoefficient

    CapacityRetiredCoefficient = plx_enums.ConstraintGasPlantsEnum.CapacityRetiredCoefficient

    BuildCostCoefficient = plx_enums.ConstraintGasPlantsEnum.BuildCostCoefficient

    BuiltCoefficient = plx_enums.ConstraintGasPlantsEnum.BuiltCoefficient

    BuiltinYearCoefficient = plx_enums.ConstraintGasPlantsEnum.BuiltinYearCoefficient


class ConstraintGasStoragesEnum(Enum):
    EndVolumeCoefficient = plx_enums.ConstraintGasStoragesEnum.EndVolumeCoefficient

    WithdrawalCoefficient = plx_enums.ConstraintGasStoragesEnum.WithdrawalCoefficient

    InjectionCoefficient = plx_enums.ConstraintGasStoragesEnum.InjectionCoefficient

    RampCoefficient = plx_enums.ConstraintGasStoragesEnum.RampCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGasStoragesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintGasStoragesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGasStoragesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintGasStoragesEnum.UnitsRetiredinYearCoefficient


class ConstraintGasTransportsEnum(Enum):
    ShipmentsCoefficient = plx_enums.ConstraintGasTransportsEnum.ShipmentsCoefficient


class ConstraintGeneratorsEnum(Enum):
    GenerationCoefficient = plx_enums.ConstraintGeneratorsEnum.GenerationCoefficient

    GenerationSquaredCoefficient = plx_enums.ConstraintGeneratorsEnum.GenerationSquaredCoefficient

    GenerationSUMSquaredCoefficient = plx_enums.ConstraintGeneratorsEnum.GenerationSUMSquaredCoefficient

    GenerationSentOutCoefficient = plx_enums.ConstraintGeneratorsEnum.GenerationSentOutCoefficient

    CapacityFactorCoefficient = plx_enums.ConstraintGeneratorsEnum.CapacityFactorCoefficient

    OperatingHoursCoefficient = plx_enums.ConstraintGeneratorsEnum.OperatingHoursCoefficient

    UnitsGeneratingCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsGeneratingCoefficient

    UnitsStartedCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsStartedCoefficient

    UnitsShutdownCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsShutdownCoefficient

    HoursDownCoefficient = plx_enums.ConstraintGeneratorsEnum.HoursDownCoefficient

    AvailableCapacityCoefficient = plx_enums.ConstraintGeneratorsEnum.AvailableCapacityCoefficient

    CommittedCapacityCoefficient = plx_enums.ConstraintGeneratorsEnum.CommittedCapacityCoefficient

    FuelOfftakeCoefficient = plx_enums.ConstraintGeneratorsEnum.FuelOfftakeCoefficient

    WasteHeatCoefficient = plx_enums.ConstraintGeneratorsEnum.WasteHeatCoefficient

    EmissionCoefficient = plx_enums.ConstraintGeneratorsEnum.EmissionCoefficient

    HeatProductionCoefficient = plx_enums.ConstraintGeneratorsEnum.HeatProductionCoefficient

    PumpLoadCoefficient = plx_enums.ConstraintGeneratorsEnum.PumpLoadCoefficient

    PumpOperatingHoursCoefficient = plx_enums.ConstraintGeneratorsEnum.PumpOperatingHoursCoefficient

    UnitsPumpingCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsPumpingCoefficient

    PumpUnitsStartedCoefficient = plx_enums.ConstraintGeneratorsEnum.PumpUnitsStartedCoefficient

    SyncCondLoadCoefficient = plx_enums.ConstraintGeneratorsEnum.SyncCondLoadCoefficient

    UnitsSyncCondCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsSyncCondCoefficient

    SyncCondOperatingHoursCoefficient = plx_enums.ConstraintGeneratorsEnum.SyncCondOperatingHoursCoefficient

    RampCoefficient = plx_enums.ConstraintGeneratorsEnum.RampCoefficient

    RampUpCoefficient = plx_enums.ConstraintGeneratorsEnum.RampUpCoefficient

    RampDownCoefficient = plx_enums.ConstraintGeneratorsEnum.RampDownCoefficient

    RampUpViolationCoefficient = plx_enums.ConstraintGeneratorsEnum.RampUpViolationCoefficient

    RampDownViolationCoefficient = plx_enums.ConstraintGeneratorsEnum.RampDownViolationCoefficient

    ReserveProvisionCoefficient = plx_enums.ConstraintGeneratorsEnum.ReserveProvisionCoefficient

    SpinningReserveCoefficient = plx_enums.ConstraintGeneratorsEnum.SpinningReserveCoefficient

    SyncCondReserveCoefficient = plx_enums.ConstraintGeneratorsEnum.SyncCondReserveCoefficient

    PumpDispatchableLoadCoefficient = plx_enums.ConstraintGeneratorsEnum.PumpDispatchableLoadCoefficient

    RaiseReserveProvisionCoefficient = plx_enums.ConstraintGeneratorsEnum.RaiseReserveProvisionCoefficient

    LowerReserveProvisionCoefficient = plx_enums.ConstraintGeneratorsEnum.LowerReserveProvisionCoefficient

    RegulationRaiseReserveProvisionCoefficient = plx_enums.ConstraintGeneratorsEnum.RegulationRaiseReserveProvisionCoefficient

    RegulationLowerReserveProvisionCoefficient = plx_enums.ConstraintGeneratorsEnum.RegulationLowerReserveProvisionCoefficient

    ReplacementReserveProvisionCoefficient = plx_enums.ConstraintGeneratorsEnum.ReplacementReserveProvisionCoefficient

    ReserveUnitsCoefficient = plx_enums.ConstraintGeneratorsEnum.ReserveUnitsCoefficient

    OperatingReserveUnitsCoefficient = plx_enums.ConstraintGeneratorsEnum.OperatingReserveUnitsCoefficient

    FlexibilityUpCoefficient = plx_enums.ConstraintGeneratorsEnum.FlexibilityUpCoefficient

    FlexibilityDownCoefficient = plx_enums.ConstraintGeneratorsEnum.FlexibilityDownCoefficient

    RampFlexibilityUpCoefficient = plx_enums.ConstraintGeneratorsEnum.RampFlexibilityUpCoefficient

    RampFlexibilityDownCoefficient = plx_enums.ConstraintGeneratorsEnum.RampFlexibilityDownCoefficient

    WithdrawalCoefficient = plx_enums.ConstraintGeneratorsEnum.WithdrawalCoefficient

    InjectionCoefficient = plx_enums.ConstraintGeneratorsEnum.InjectionCoefficient

    WaterOfftakeCoefficient = plx_enums.ConstraintGeneratorsEnum.WaterOfftakeCoefficient

    WaterConsumptionCoefficient = plx_enums.ConstraintGeneratorsEnum.WaterConsumptionCoefficient

    NetProfitCoefficient = plx_enums.ConstraintGeneratorsEnum.NetProfitCoefficient

    PoolRevenueCoefficient = plx_enums.ConstraintGeneratorsEnum.PoolRevenueCoefficient

    NetRevenueCoefficient = plx_enums.ConstraintGeneratorsEnum.NetRevenueCoefficient

    StartShutdownCostCoefficient = plx_enums.ConstraintGeneratorsEnum.StartShutdownCostCoefficient

    FixedCostsCoefficient = plx_enums.ConstraintGeneratorsEnum.FixedCostsCoefficient

    InstalledCapacityCoefficient = plx_enums.ConstraintGeneratorsEnum.InstalledCapacityCoefficient

    RatedCapacityCoefficient = plx_enums.ConstraintGeneratorsEnum.RatedCapacityCoefficient

    UnitsOutCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsOutCoefficient

    MaintenanceCoefficient = plx_enums.ConstraintGeneratorsEnum.MaintenanceCoefficient

    FirmCapacityCoefficient = plx_enums.ConstraintGeneratorsEnum.FirmCapacityCoefficient

    AgeCoefficient = plx_enums.ConstraintGeneratorsEnum.AgeCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintGeneratorsEnum.UnitsRetiredinYearCoefficient

    CapacityBuiltCoefficient = plx_enums.ConstraintGeneratorsEnum.CapacityBuiltCoefficient

    CapacityRetiredCoefficient = plx_enums.ConstraintGeneratorsEnum.CapacityRetiredCoefficient

    CapacityReservesCoefficient = plx_enums.ConstraintGeneratorsEnum.CapacityReservesCoefficient

    BuildCostCoefficient = plx_enums.ConstraintGeneratorsEnum.BuildCostCoefficient

    BuiltCoefficient = plx_enums.ConstraintGeneratorsEnum.BuiltCoefficient

    BuiltinYearCoefficient = plx_enums.ConstraintGeneratorsEnum.BuiltinYearCoefficient


class ConstraintHeatNodesEnum(Enum):
    HeatFlowCoefficient = plx_enums.ConstraintHeatNodesEnum.HeatFlowCoefficient


class ConstraintHeatPlantsEnum(Enum):
    UnitsGeneratingCoefficient = plx_enums.ConstraintHeatPlantsEnum.UnitsGeneratingCoefficient

    FuelOfftakeCoefficient = plx_enums.ConstraintHeatPlantsEnum.FuelOfftakeCoefficient

    HeatProductionCoefficient = plx_enums.ConstraintHeatPlantsEnum.HeatProductionCoefficient


class ConstraintHubsEnum(Enum):
    LoadCoefficient = plx_enums.ConstraintHubsEnum.LoadCoefficient

    GenerationCoefficient = plx_enums.ConstraintHubsEnum.GenerationCoefficient


class ConstraintInterfacesEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintInterfacesEnum.FlowCoefficient

    FlowForwardCoefficient = plx_enums.ConstraintInterfacesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.ConstraintInterfacesEnum.FlowBackCoefficient

    ExpansionCostCoefficient = plx_enums.ConstraintInterfacesEnum.ExpansionCostCoefficient


class ConstraintLHSTypeEnum(Enum):
    Sum = plx_enums.ConstraintLHSTypeEnum.Sum

    MaxSum = plx_enums.ConstraintLHSTypeEnum.MaxSum

    Max = plx_enums.ConstraintLHSTypeEnum.Max


class ConstraintLinesEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintLinesEnum.FlowCoefficient

    FlowForwardCoefficient = plx_enums.ConstraintLinesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.ConstraintLinesEnum.FlowBackCoefficient

    FlowSquaredCoefficient = plx_enums.ConstraintLinesEnum.FlowSquaredCoefficient

    FlowingForwardCoefficient = plx_enums.ConstraintLinesEnum.FlowingForwardCoefficient

    FlowingBackCoefficient = plx_enums.ConstraintLinesEnum.FlowingBackCoefficient

    SpareExportCapacityCoefficient = plx_enums.ConstraintLinesEnum.SpareExportCapacityCoefficient

    SpareImportCapacityCoefficient = plx_enums.ConstraintLinesEnum.SpareImportCapacityCoefficient

    UnitsOutCoefficient = plx_enums.ConstraintLinesEnum.UnitsOutCoefficient

    ExportCapacityCoefficient = plx_enums.ConstraintLinesEnum.ExportCapacityCoefficient

    ImportCapacityCoefficient = plx_enums.ConstraintLinesEnum.ImportCapacityCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintLinesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintLinesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintLinesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintLinesEnum.UnitsRetiredinYearCoefficient

    ExportCapacityBuiltCoefficient = plx_enums.ConstraintLinesEnum.ExportCapacityBuiltCoefficient

    ImportCapacityBuiltCoefficient = plx_enums.ConstraintLinesEnum.ImportCapacityBuiltCoefficient

    ExportCapacityRetiredCoefficient = plx_enums.ConstraintLinesEnum.ExportCapacityRetiredCoefficient

    ImportCapacityRetiredCoefficient = plx_enums.ConstraintLinesEnum.ImportCapacityRetiredCoefficient

    BuildCostCoefficient = plx_enums.ConstraintLinesEnum.BuildCostCoefficient


class ConstraintMaintenancesEnum(Enum):
    HoursActiveCoefficient = plx_enums.ConstraintMaintenancesEnum.HoursActiveCoefficient

    CostCoefficient = plx_enums.ConstraintMaintenancesEnum.CostCoefficient

    CrewCoefficient = plx_enums.ConstraintMaintenancesEnum.CrewCoefficient

    EquipmentCoefficient = plx_enums.ConstraintMaintenancesEnum.EquipmentCoefficient

    StartHourCoefficient = plx_enums.ConstraintMaintenancesEnum.StartHourCoefficient

    StartCoefficient = plx_enums.ConstraintMaintenancesEnum.StartCoefficient


class ConstraintMarketsEnum(Enum):
    SalesCoefficient = plx_enums.ConstraintMarketsEnum.SalesCoefficient

    PurchasesCoefficient = plx_enums.ConstraintMarketsEnum.PurchasesCoefficient

    RevenueCoefficient = plx_enums.ConstraintMarketsEnum.RevenueCoefficient

    CostCoefficient = plx_enums.ConstraintMarketsEnum.CostCoefficient


class ConstraintNodesEnum(Enum):
    LoadCoefficient = plx_enums.ConstraintNodesEnum.LoadCoefficient

    GenerationCoefficient = plx_enums.ConstraintNodesEnum.GenerationCoefficient

    UnservedEnergyCoefficient = plx_enums.ConstraintNodesEnum.UnservedEnergyCoefficient

    DumpEnergyCoefficient = plx_enums.ConstraintNodesEnum.DumpEnergyCoefficient

    NetLoadCoefficient = plx_enums.ConstraintNodesEnum.NetLoadCoefficient

    NetInjectionCoefficient = plx_enums.ConstraintNodesEnum.NetInjectionCoefficient

    PhaseAngleCoefficient = plx_enums.ConstraintNodesEnum.PhaseAngleCoefficient

    MLFCoefficient = plx_enums.ConstraintNodesEnum.MLFCoefficient


class ConstraintPaymentsCompatibilityEnum(Enum):
    Korea = plx_enums.ConstraintPaymentsCompatibilityEnum.Korea

    Ireland = plx_enums.ConstraintPaymentsCompatibilityEnum.Ireland


class ConstraintPhysicalContractsEnum(Enum):
    LoadCoefficient = plx_enums.ConstraintPhysicalContractsEnum.LoadCoefficient

    GenerationCoefficient = plx_enums.ConstraintPhysicalContractsEnum.GenerationCoefficient

    UnitsGeneratingCoefficient = plx_enums.ConstraintPhysicalContractsEnum.UnitsGeneratingCoefficient

    UnitsLoadCoefficient = plx_enums.ConstraintPhysicalContractsEnum.UnitsLoadCoefficient

    GenerationCapacityCoefficient = plx_enums.ConstraintPhysicalContractsEnum.GenerationCapacityCoefficient

    LoadObligationCoefficient = plx_enums.ConstraintPhysicalContractsEnum.LoadObligationCoefficient

    BuildCostCoefficient = plx_enums.ConstraintPhysicalContractsEnum.BuildCostCoefficient


class ConstraintPurchasersEnum(Enum):
    LoadCoefficient = plx_enums.ConstraintPurchasersEnum.LoadCoefficient

    LoadObligationCoefficient = plx_enums.ConstraintPurchasersEnum.LoadObligationCoefficient

    ReserveProvisionCoefficient = plx_enums.ConstraintPurchasersEnum.ReserveProvisionCoefficient


class ConstraintRegionsEnum(Enum):
    LoadCoefficient = plx_enums.ConstraintRegionsEnum.LoadCoefficient

    LoadSquaredCoefficient = plx_enums.ConstraintRegionsEnum.LoadSquaredCoefficient

    GenerationCoefficient = plx_enums.ConstraintRegionsEnum.GenerationCoefficient

    CommittedCapacityCoefficient = plx_enums.ConstraintRegionsEnum.CommittedCapacityCoefficient

    UnservedEnergyCoefficient = plx_enums.ConstraintRegionsEnum.UnservedEnergyCoefficient

    DumpEnergyCoefficient = plx_enums.ConstraintRegionsEnum.DumpEnergyCoefficient

    NetLoadCoefficient = plx_enums.ConstraintRegionsEnum.NetLoadCoefficient

    FirmCapacityCoefficient = plx_enums.ConstraintRegionsEnum.FirmCapacityCoefficient

    GenerationCapacityCoefficient = plx_enums.ConstraintRegionsEnum.GenerationCapacityCoefficient

    PeakLoadCoefficient = plx_enums.ConstraintRegionsEnum.PeakLoadCoefficient

    CapacityReservesCoefficient = plx_enums.ConstraintRegionsEnum.CapacityReservesCoefficient

    GenerationCapacityBuiltCoefficient = plx_enums.ConstraintRegionsEnum.GenerationCapacityBuiltCoefficient

    GenerationCapacityRetiredCoefficient = plx_enums.ConstraintRegionsEnum.GenerationCapacityRetiredCoefficient

    GeneratorBuildCostCoefficient = plx_enums.ConstraintRegionsEnum.GeneratorBuildCostCoefficient

    GeneratorsBuiltCoefficient = plx_enums.ConstraintRegionsEnum.GeneratorsBuiltCoefficient

    GeneratorsBuiltinYearCoefficient = plx_enums.ConstraintRegionsEnum.GeneratorsBuiltinYearCoefficient

    ImportCapacityCoefficient = plx_enums.ConstraintRegionsEnum.ImportCapacityCoefficient

    ExportCapacityCoefficient = plx_enums.ConstraintRegionsEnum.ExportCapacityCoefficient

    ImportCapacityBuiltCoefficient = plx_enums.ConstraintRegionsEnum.ImportCapacityBuiltCoefficient

    ExportCapacityBuiltCoefficient = plx_enums.ConstraintRegionsEnum.ExportCapacityBuiltCoefficient


class ConstraintReservesEnum(Enum):
    ProvisionCoefficient = plx_enums.ConstraintReservesEnum.ProvisionCoefficient

    RiskCoefficient = plx_enums.ConstraintReservesEnum.RiskCoefficient

    ShortageCoefficient = plx_enums.ConstraintReservesEnum.ShortageCoefficient


class ConstraintStatusEnum(Enum):
    InActive = plx_enums.ConstraintStatusEnum.InActive

    Active = plx_enums.ConstraintStatusEnum.Active


class ConstraintStoragesEnum(Enum):
    EndVolumeCoefficient = plx_enums.ConstraintStoragesEnum.EndVolumeCoefficient

    EndLevelCoefficient = plx_enums.ConstraintStoragesEnum.EndLevelCoefficient

    RampCoefficient = plx_enums.ConstraintStoragesEnum.RampCoefficient

    NaturalInflowCoefficient = plx_enums.ConstraintStoragesEnum.NaturalInflowCoefficient

    InflowCoefficient = plx_enums.ConstraintStoragesEnum.InflowCoefficient

    ReleaseCoefficient = plx_enums.ConstraintStoragesEnum.ReleaseCoefficient

    GeneratorReleaseCoefficient = plx_enums.ConstraintStoragesEnum.GeneratorReleaseCoefficient

    SpillCoefficient = plx_enums.ConstraintStoragesEnum.SpillCoefficient

    HoursFullCoefficient = plx_enums.ConstraintStoragesEnum.HoursFullCoefficient

    LossCoefficient = plx_enums.ConstraintStoragesEnum.LossCoefficient


class ConstraintTransformersEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintTransformersEnum.FlowCoefficient


class ConstraintVariablesEnum(Enum):
    ExpectedValueCoefficient = plx_enums.ConstraintVariablesEnum.ExpectedValueCoefficient

    ValueCoefficient = plx_enums.ConstraintVariablesEnum.ValueCoefficient

    ErrorCoefficient = plx_enums.ConstraintVariablesEnum.ErrorCoefficient

    PositiveErrorCoefficient = plx_enums.ConstraintVariablesEnum.PositiveErrorCoefficient

    NegativeErrorCoefficient = plx_enums.ConstraintVariablesEnum.NegativeErrorCoefficient


class ConstraintWaterNodesEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintWaterNodesEnum.FlowCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintWaterNodesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintWaterNodesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintWaterNodesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintWaterNodesEnum.UnitsRetiredinYearCoefficient


class ConstraintWaterPipelinesEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintWaterPipelinesEnum.FlowCoefficient

    FlowForwardCoefficient = plx_enums.ConstraintWaterPipelinesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.ConstraintWaterPipelinesEnum.FlowBackCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintWaterPipelinesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintWaterPipelinesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintWaterPipelinesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintWaterPipelinesEnum.UnitsRetiredinYearCoefficient


class ConstraintWaterPlantsEnum(Enum):
    ProductionCoefficient = plx_enums.ConstraintWaterPlantsEnum.ProductionCoefficient

    CapacityFactorCoefficient = plx_enums.ConstraintWaterPlantsEnum.CapacityFactorCoefficient

    OperatingHoursCoefficient = plx_enums.ConstraintWaterPlantsEnum.OperatingHoursCoefficient

    EnergyUsageCoefficient = plx_enums.ConstraintWaterPlantsEnum.EnergyUsageCoefficient

    InstalledCapacityCoefficient = plx_enums.ConstraintWaterPlantsEnum.InstalledCapacityCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintWaterPlantsEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintWaterPlantsEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintWaterPlantsEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintWaterPlantsEnum.UnitsRetiredinYearCoefficient

    CapacityBuiltCoefficient = plx_enums.ConstraintWaterPlantsEnum.CapacityBuiltCoefficient

    CapacityRetiredCoefficient = plx_enums.ConstraintWaterPlantsEnum.CapacityRetiredCoefficient

    BuildCostCoefficient = plx_enums.ConstraintWaterPlantsEnum.BuildCostCoefficient

    BuiltCoefficient = plx_enums.ConstraintWaterPlantsEnum.BuiltCoefficient

    BuiltinYearCoefficient = plx_enums.ConstraintWaterPlantsEnum.BuiltinYearCoefficient


class ConstraintWaterStoragesEnum(Enum):
    NaturalInflowCoefficient = plx_enums.ConstraintWaterStoragesEnum.NaturalInflowCoefficient

    EndVolumeCoefficient = plx_enums.ConstraintWaterStoragesEnum.EndVolumeCoefficient

    ReleaseCoefficient = plx_enums.ConstraintWaterStoragesEnum.ReleaseCoefficient

    InflowCoefficient = plx_enums.ConstraintWaterStoragesEnum.InflowCoefficient

    RampCoefficient = plx_enums.ConstraintWaterStoragesEnum.RampCoefficient

    UnitsBuiltCoefficient = plx_enums.ConstraintWaterStoragesEnum.UnitsBuiltCoefficient

    UnitsRetiredCoefficient = plx_enums.ConstraintWaterStoragesEnum.UnitsRetiredCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.ConstraintWaterStoragesEnum.UnitsBuiltinYearCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.ConstraintWaterStoragesEnum.UnitsRetiredinYearCoefficient


class ConstraintWaterwaysEnum(Enum):
    FlowCoefficient = plx_enums.ConstraintWaterwaysEnum.FlowCoefficient

    RampCoefficient = plx_enums.ConstraintWaterwaysEnum.RampCoefficient

    HoursFlowingCoefficient = plx_enums.ConstraintWaterwaysEnum.HoursFlowingCoefficient


class ConstraintZonesEnum(Enum):
    LoadCoefficient = plx_enums.ConstraintZonesEnum.LoadCoefficient

    LoadSquaredCoefficient = plx_enums.ConstraintZonesEnum.LoadSquaredCoefficient

    GenerationCoefficient = plx_enums.ConstraintZonesEnum.GenerationCoefficient

    CommittedCapacityCoefficient = plx_enums.ConstraintZonesEnum.CommittedCapacityCoefficient

    UnservedEnergyCoefficient = plx_enums.ConstraintZonesEnum.UnservedEnergyCoefficient

    DumpEnergyCoefficient = plx_enums.ConstraintZonesEnum.DumpEnergyCoefficient

    NetLoadCoefficient = plx_enums.ConstraintZonesEnum.NetLoadCoefficient

    FirmCapacityCoefficient = plx_enums.ConstraintZonesEnum.FirmCapacityCoefficient

    GenerationCapacityCoefficient = plx_enums.ConstraintZonesEnum.GenerationCapacityCoefficient

    PeakLoadCoefficient = plx_enums.ConstraintZonesEnum.PeakLoadCoefficient

    CapacityReservesCoefficient = plx_enums.ConstraintZonesEnum.CapacityReservesCoefficient

    GenerationCapacityBuiltCoefficient = plx_enums.ConstraintZonesEnum.GenerationCapacityBuiltCoefficient

    GenerationCapacityRetiredCoefficient = plx_enums.ConstraintZonesEnum.GenerationCapacityRetiredCoefficient

    GeneratorBuildCostCoefficient = plx_enums.ConstraintZonesEnum.GeneratorBuildCostCoefficient

    GeneratorsBuiltCoefficient = plx_enums.ConstraintZonesEnum.GeneratorsBuiltCoefficient

    GeneratorsBuiltinYearCoefficient = plx_enums.ConstraintZonesEnum.GeneratorsBuiltinYearCoefficient

    ImportCapacityCoefficient = plx_enums.ConstraintZonesEnum.ImportCapacityCoefficient

    ExportCapacityCoefficient = plx_enums.ConstraintZonesEnum.ExportCapacityCoefficient

    ImportCapacityBuiltCoefficient = plx_enums.ConstraintZonesEnum.ImportCapacityBuiltCoefficient

    ExportCapacityBuiltCoefficient = plx_enums.ConstraintZonesEnum.ExportCapacityBuiltCoefficient


class ContractHandoffPointEnum(Enum):
    Purchaser = plx_enums.ContractHandoffPointEnum.Purchaser

    Generator = plx_enums.ContractHandoffPointEnum.Generator


class ContractSettlementMethodEnum(Enum):
    Fixed = plx_enums.ContractSettlementMethodEnum.Fixed

    Prorata = plx_enums.ContractSettlementMethodEnum.Prorata

    LeastCost = plx_enums.ContractSettlementMethodEnum.LeastCost


class CycleTypeEnum(Enum):
    Day = plx_enums.CycleTypeEnum.Day

    Month = plx_enums.CycleTypeEnum.Month

    Year = plx_enums.CycleTypeEnum.Year

    Quarter = plx_enums.CycleTypeEnum.Quarter


class DataFileAttributeEnum(Enum):
    Enabled = plx_enums.DataFileAttributeEnum.Enabled

    GrowthPeriod = plx_enums.DataFileAttributeEnum.GrowthPeriod

    Method = plx_enums.DataFileAttributeEnum.Method

    RelativeGrowthatMin = plx_enums.DataFileAttributeEnum.RelativeGrowthatMin

    ShapeDistortion = plx_enums.DataFileAttributeEnum.ShapeDistortion

    DecimalPlaces = plx_enums.DataFileAttributeEnum.DecimalPlaces

    MissingValueMethod = plx_enums.DataFileAttributeEnum.MissingValueMethod

    PeriodsperDay = plx_enums.DataFileAttributeEnum.PeriodsperDay

    UpscalingMethod = plx_enums.DataFileAttributeEnum.UpscalingMethod

    DownscalingMethod = plx_enums.DataFileAttributeEnum.DownscalingMethod

    DatetimeConvention = plx_enums.DataFileAttributeEnum.DatetimeConvention

    Locale = plx_enums.DataFileAttributeEnum.Locale

    TimeShift = plx_enums.DataFileAttributeEnum.TimeShift

    WeekBeginning = plx_enums.DataFileAttributeEnum.WeekBeginning

    HistoricalSampling = plx_enums.DataFileAttributeEnum.HistoricalSampling

    HistoricalYearFrom = plx_enums.DataFileAttributeEnum.HistoricalYearFrom

    HistoricalYearTo = plx_enums.DataFileAttributeEnum.HistoricalYearTo

    HistoricalYearStart = plx_enums.DataFileAttributeEnum.HistoricalYearStart

    HistoricalYearEnding = plx_enums.DataFileAttributeEnum.HistoricalYearEnding

    HistoricalPeriodType = plx_enums.DataFileAttributeEnum.HistoricalPeriodType

    BaseYear = plx_enums.DataFileAttributeEnum.BaseYear


class DataFileDownScalingMethodEnum(Enum):
    Average = plx_enums.DataFileDownScalingMethodEnum.Average

    First = plx_enums.DataFileDownScalingMethodEnum.First

    Last = plx_enums.DataFileDownScalingMethodEnum.Last

    Auto = plx_enums.DataFileDownScalingMethodEnum.Auto


class DataFileMissingValueMethodEnum(Enum):
    LastKnownValue = plx_enums.DataFileMissingValueMethodEnum.LastKnownValue

    AssumeZero = plx_enums.DataFileMissingValueMethodEnum.AssumeZero

    AssumeDefault = plx_enums.DataFileMissingValueMethodEnum.AssumeDefault


class DataFileUpScalingMethodEnum(Enum):
    Step = plx_enums.DataFileUpScalingMethodEnum.Step

    Interpolate = plx_enums.DataFileUpScalingMethodEnum.Interpolate

    BoundaryInterpolate = plx_enums.DataFileUpScalingMethodEnum.BoundaryInterpolate

    Auto = plx_enums.DataFileUpScalingMethodEnum.Auto


class DatetimeConventionEnum(Enum):
    BeginningofInterval = plx_enums.DatetimeConventionEnum.BeginningofInterval

    EndofInterval = plx_enums.DatetimeConventionEnum.EndofInterval


class DecisionVariableAttributeEnum(Enum):
    Type = plx_enums.DecisionVariableAttributeEnum.Type

    TimeLag = plx_enums.DecisionVariableAttributeEnum.TimeLag

    TimeInvariant = plx_enums.DecisionVariableAttributeEnum.TimeInvariant


class DecisionVariableDefinitionEnum(Enum):
    ValueCoefficient = plx_enums.DecisionVariableDefinitionEnum.ValueCoefficient


class DecisionVariableGasPlantsEnum(Enum):
    EnergyUsageDefinitionCoefficient = plx_enums.DecisionVariableGasPlantsEnum.EnergyUsageDefinitionCoefficient


class DecisionVariableGeneratorsEnum(Enum):
    HeatInputDefinitionCoefficient = plx_enums.DecisionVariableGeneratorsEnum.HeatInputDefinitionCoefficient


class DecisionVariableNodesEnum(Enum):
    NetInjectionDefinitionCoefficient = plx_enums.DecisionVariableNodesEnum.NetInjectionDefinitionCoefficient


class DecisionVariableTypeEnum(Enum):
    Continuous = plx_enums.DecisionVariableTypeEnum.Continuous

    Integer = plx_enums.DecisionVariableTypeEnum.Integer


class DecisionVariableWaterPlantsEnum(Enum):
    EnergyUsageDefinitionCoefficient = plx_enums.DecisionVariableWaterPlantsEnum.EnergyUsageDefinitionCoefficient


class DepreciationMethodEnum(Enum):
    None_ = 0

    StraightLine = plx_enums.DepreciationMethodEnum.StraightLine

    Declining = plx_enums.DepreciationMethodEnum.Declining


class DesignBenefitFnShapeEnum(Enum):
    PiecewiseLinear = plx_enums.DesignBenefitFnShapeEnum.PiecewiseLinear

    Quadratic = plx_enums.DesignBenefitFnShapeEnum.Quadratic


class DesignOfferQuantityFormatEnum(Enum):
    Incremental = plx_enums.DesignOfferQuantityFormatEnum.Incremental

    Cumulative = plx_enums.DesignOfferQuantityFormatEnum.Cumulative


class DesignPoolTypeEnum(Enum):
    Gross = plx_enums.DesignPoolTypeEnum.Gross

    Net = plx_enums.DesignPoolTypeEnum.Net


class DesignSettlementModelEnum(Enum):
    Nodal = plx_enums.DesignSettlementModelEnum.Nodal

    ReferenceNode = plx_enums.DesignSettlementModelEnum.ReferenceNode

    LoadWeightedAverage = plx_enums.DesignSettlementModelEnum.LoadWeightedAverage

    PayAsBid = plx_enums.DesignSettlementModelEnum.PayAsBid

    UniformPrice = plx_enums.DesignSettlementModelEnum.UniformPrice

    None_ = 5

    Custom = plx_enums.DesignSettlementModelEnum.Custom

    MostExpensiveDispatched = plx_enums.DesignSettlementModelEnum.MostExpensiveDispatched


class DiagnosticAttributeEnum(Enum):
    ClearExisting = plx_enums.DiagnosticAttributeEnum.ClearExisting

    TaskSize = plx_enums.DiagnosticAttributeEnum.TaskSize

    TaskComponents = plx_enums.DiagnosticAttributeEnum.TaskComponents

    LPProgress = plx_enums.DiagnosticAttributeEnum.LPProgress

    MIPProgress = plx_enums.DiagnosticAttributeEnum.MIPProgress

    SolverSummary = plx_enums.DiagnosticAttributeEnum.SolverSummary

    SolutionStatus = plx_enums.DiagnosticAttributeEnum.SolutionStatus

    Times = plx_enums.DiagnosticAttributeEnum.Times

    SampleSummary = plx_enums.DiagnosticAttributeEnum.SampleSummary

    StepSummary = plx_enums.DiagnosticAttributeEnum.StepSummary

    PerformanceSummary = plx_enums.DiagnosticAttributeEnum.PerformanceSummary

    StepFrom = plx_enums.DiagnosticAttributeEnum.StepFrom

    StepTo = plx_enums.DiagnosticAttributeEnum.StepTo

    SampleFrom = plx_enums.DiagnosticAttributeEnum.SampleFrom

    SampleTo = plx_enums.DiagnosticAttributeEnum.SampleTo

    LPFiles = plx_enums.DiagnosticAttributeEnum.LPFiles

    MPSFiles = plx_enums.DiagnosticAttributeEnum.MPSFiles

    SolutionFiles = plx_enums.DiagnosticAttributeEnum.SolutionFiles

    GenericNames = plx_enums.DiagnosticAttributeEnum.GenericNames

    BinaryFiles = plx_enums.DiagnosticAttributeEnum.BinaryFiles

    UseGenericWriter = plx_enums.DiagnosticAttributeEnum.UseGenericWriter

    SortRowColumnNames = plx_enums.DiagnosticAttributeEnum.SortRowColumnNames

    StandardizeNames = plx_enums.DiagnosticAttributeEnum.StandardizeNames

    StripModelName = plx_enums.DiagnosticAttributeEnum.StripModelName

    Algebraic = plx_enums.DiagnosticAttributeEnum.Algebraic

    SkipZeroValues = plx_enums.DiagnosticAttributeEnum.SkipZeroValues

    ZeroToleranceLP = plx_enums.DiagnosticAttributeEnum.ZeroToleranceLP

    ZeroToleranceSOL = plx_enums.DiagnosticAttributeEnum.ZeroToleranceSOL

    DecimalPlacesLP = plx_enums.DiagnosticAttributeEnum.DecimalPlacesLP

    DecimalPlacesSOL = plx_enums.DiagnosticAttributeEnum.DecimalPlacesSOL

    Infeasibilities = plx_enums.DiagnosticAttributeEnum.Infeasibilities

    MaxInfeasibilityLogLines = plx_enums.DiagnosticAttributeEnum.MaxInfeasibilityLogLines

    FeasibilityRepairWeight = plx_enums.DiagnosticAttributeEnum.FeasibilityRepairWeight

    DatabaseLoad = plx_enums.DiagnosticAttributeEnum.DatabaseLoad

    Licensing = plx_enums.DiagnosticAttributeEnum.Licensing

    ComputerInformation = plx_enums.DiagnosticAttributeEnum.ComputerInformation

    DataFileRead = plx_enums.DiagnosticAttributeEnum.DataFileRead

    BertrandPricing = plx_enums.DiagnosticAttributeEnum.BertrandPricing

    RevenueRecovery = plx_enums.DiagnosticAttributeEnum.RevenueRecovery

    BidCostMarkup = plx_enums.DiagnosticAttributeEnum.BidCostMarkup

    NewEntry = plx_enums.DiagnosticAttributeEnum.NewEntry

    ShiftFactors = plx_enums.DiagnosticAttributeEnum.ShiftFactors

    UnservedEnergy = plx_enums.DiagnosticAttributeEnum.UnservedEnergy

    InterruptionSharing = plx_enums.DiagnosticAttributeEnum.InterruptionSharing

    NetworkTraversal = plx_enums.DiagnosticAttributeEnum.NetworkTraversal

    TransmissionTopology = plx_enums.DiagnosticAttributeEnum.TransmissionTopology

    TransmissionLosses = plx_enums.DiagnosticAttributeEnum.TransmissionLosses

    CongestionCharges = plx_enums.DiagnosticAttributeEnum.CongestionCharges

    MarginalLossCharges = plx_enums.DiagnosticAttributeEnum.MarginalLossCharges

    BindingContingencies = plx_enums.DiagnosticAttributeEnum.BindingContingencies

    UnitCommitment = plx_enums.DiagnosticAttributeEnum.UnitCommitment

    ConstraintDecomposition = plx_enums.DiagnosticAttributeEnum.ConstraintDecomposition

    ConstraintRollover = plx_enums.DiagnosticAttributeEnum.ConstraintRollover

    StorageDecomposition = plx_enums.DiagnosticAttributeEnum.StorageDecomposition

    UniformPricing = plx_enums.DiagnosticAttributeEnum.UniformPricing

    MarginalUnit = plx_enums.DiagnosticAttributeEnum.MarginalUnit

    MarginalUnitTransmissionDetail = plx_enums.DiagnosticAttributeEnum.MarginalUnitTransmissionDetail

    MarginalUnitIncrement = plx_enums.DiagnosticAttributeEnum.MarginalUnitIncrement

    MarginalExpansionUnit = plx_enums.DiagnosticAttributeEnum.MarginalExpansionUnit

    MarginalExpansionIncrement = plx_enums.DiagnosticAttributeEnum.MarginalExpansionIncrement

    RegionSupply = plx_enums.DiagnosticAttributeEnum.RegionSupply

    Annuities = plx_enums.DiagnosticAttributeEnum.Annuities

    NPV = plx_enums.DiagnosticAttributeEnum.NPV

    EmbeddedLosses = plx_enums.DiagnosticAttributeEnum.EmbeddedLosses

    Outages = plx_enums.DiagnosticAttributeEnum.Outages

    RandomNumberSeed = plx_enums.DiagnosticAttributeEnum.RandomNumberSeed

    Interleaved = plx_enums.DiagnosticAttributeEnum.Interleaved

    HeatRate = plx_enums.DiagnosticAttributeEnum.HeatRate

    ObjectiveFunction = plx_enums.DiagnosticAttributeEnum.ObjectiveFunction

    FutureCostFunction = plx_enums.DiagnosticAttributeEnum.FutureCostFunction

    HistoricalSampling = plx_enums.DiagnosticAttributeEnum.HistoricalSampling

    ScenarioTree = plx_enums.DiagnosticAttributeEnum.ScenarioTree

    SampleWeights = plx_enums.DiagnosticAttributeEnum.SampleWeights


class DiscountEndEffectsMethodEnum(Enum):
    None_ = 0

    Perpetuity = plx_enums.DiscountEndEffectsMethodEnum.Perpetuity


class EEIFormatEnum(Enum):
    TwoDigitYear = plx_enums.EEIFormatEnum.TwoDigitYear

    FourDigitYear = plx_enums.EEIFormatEnum.FourDigitYear


class EmissionFuelsEnum(Enum):
    ProductionRate = plx_enums.EmissionFuelsEnum.ProductionRate


class EmissionGasNodesEnum(Enum):
    ProductionRate = plx_enums.EmissionGasNodesEnum.ProductionRate


class EmissionGasPlantsEnum(Enum):
    ProductionRate = plx_enums.EmissionGasPlantsEnum.ProductionRate


class EmissionGeneratorsEnum(Enum):
    ProductionRate = plx_enums.EmissionGeneratorsEnum.ProductionRate

    RemovalRate = plx_enums.EmissionGeneratorsEnum.RemovalRate

    RemovalCost = plx_enums.EmissionGeneratorsEnum.RemovalCost

    ProductionatStart = plx_enums.EmissionGeneratorsEnum.ProductionatStart

    ShadowPriceScalar = plx_enums.EmissionGeneratorsEnum.ShadowPriceScalar

    PriceScalar = plx_enums.EmissionGeneratorsEnum.PriceScalar

    Allocation = plx_enums.EmissionGeneratorsEnum.Allocation


class EmissionWaterPlantsEnum(Enum):
    ProductionRate = plx_enums.EmissionWaterPlantsEnum.ProductionRate


class EnforceMinUpandDownTimesEnum(Enum):
    No = plx_enums.EnforceMinUpandDownTimesEnum.No

    Yes = plx_enums.EnforceMinUpandDownTimesEnum.Yes


class FileTypeEnum(Enum):
    FileTypeEnum_Input = plx_enums.FileTypeEnum.FileTypeEnum_Input

    FileTypeEnum_Output = plx_enums.FileTypeEnum.FileTypeEnum_Output


class FinancialContractGeneratingCompaniesEnum(Enum):
    Share = plx_enums.FinancialContractGeneratingCompaniesEnum.Share


class FinancialContractGeneratorsEnum(Enum):
    GenerationParticipationFactor = plx_enums.FinancialContractGeneratorsEnum.GenerationParticipationFactor


class FinancialContractPurchasingCompaniesEnum(Enum):
    Share = plx_enums.FinancialContractPurchasingCompaniesEnum.Share


class FinancialContractRegionEnum(Enum):
    LoadParticipationFactor = plx_enums.FinancialContractRegionEnum.LoadParticipationFactor


class FixedLoadTypeEnum(Enum):
    None_ = 0

    FixedLoad = plx_enums.FixedLoadTypeEnum.FixedLoad

    MinLoad = plx_enums.FixedLoadTypeEnum.MinLoad


class FlatFileFormatEnum(Enum):
    PeriodsInColumns = plx_enums.FlatFileFormatEnum.PeriodsInColumns

    NamedPeriodsInColumns = plx_enums.FlatFileFormatEnum.NamedPeriodsInColumns

    BandsInColumns = plx_enums.FlatFileFormatEnum.BandsInColumns

    NamesInColumns = plx_enums.FlatFileFormatEnum.NamesInColumns

    NamedBandsInColumns = plx_enums.FlatFileFormatEnum.NamedBandsInColumns

    Patterned = plx_enums.FlatFileFormatEnum.Patterned

    NamedPatterned = plx_enums.FlatFileFormatEnum.NamedPatterned

    PatternedNamesInColumns = plx_enums.FlatFileFormatEnum.PatternedNamesInColumns

    PatternsInColumns = plx_enums.FlatFileFormatEnum.PatternsInColumns

    NamedPatternsInColumns = plx_enums.FlatFileFormatEnum.NamedPatternsInColumns

    Unknown = plx_enums.FlatFileFormatEnum.Unknown


class FlowControlAngleVariationEnum(Enum):
    Variable = plx_enums.FlowControlAngleVariationEnum.Variable

    Fixed = plx_enums.FlowControlAngleVariationEnum.Fixed


class FlowControlTypeEnum(Enum):
    PST = plx_enums.FlowControlTypeEnum.PST

    DSR = plx_enums.FlowControlTypeEnum.DSR

    DSSC = plx_enums.FlowControlTypeEnum.DSSC

    MSSR = plx_enums.FlowControlTypeEnum.MSSR

    TCSC = plx_enums.FlowControlTypeEnum.TCSC

    SSSC = plx_enums.FlowControlTypeEnum.SSSC


class FlowModelEnum(Enum):
    None_ = 0

    Net = plx_enums.FlowModelEnum.Net

    Directed = plx_enums.FlowModelEnum.Directed


class FuelCompaniesEnum(Enum):
    Share = plx_enums.FuelCompaniesEnum.Share


class FuelContractCompaniesEnum(Enum):
    Share = plx_enums.FuelContractCompaniesEnum.Share


class GasDemandCompaniesEnum(Enum):
    Share = plx_enums.GasDemandCompaniesEnum.Share


class GasDemandGasNodesEnum(Enum):
    DemandParticipationFactor = plx_enums.GasDemandGasNodesEnum.DemandParticipationFactor


class GasFieldCompaniesEnum(Enum):
    Share = plx_enums.GasFieldCompaniesEnum.Share


class GasNodeAttributeEnum(Enum):
    Latitude = plx_enums.GasNodeAttributeEnum.Latitude

    Longitude = plx_enums.GasNodeAttributeEnum.Longitude


class GasStorageAttributeEnum(Enum):
    Latitude = plx_enums.GasStorageAttributeEnum.Latitude

    Longitude = plx_enums.GasStorageAttributeEnum.Longitude


class GeneratorAttributeEnum(Enum):
    Latitude = plx_enums.GeneratorAttributeEnum.Latitude

    Longitude = plx_enums.GeneratorAttributeEnum.Longitude


class GeneratorCommitmentModelEnum(Enum):
    None_ = 0

    Aggregated = plx_enums.GeneratorCommitmentModelEnum.Aggregated

    UnitbyUnit = plx_enums.GeneratorCommitmentModelEnum.UnitbyUnit


class GeneratorCompaniesEnum(Enum):
    Share = plx_enums.GeneratorCompaniesEnum.Share


class GeneratorFuelsEnum(Enum):
    TransportCharge = plx_enums.GeneratorFuelsEnum.TransportCharge

    MutuallyExclusive = plx_enums.GeneratorFuelsEnum.MutuallyExclusive

    Ratio = plx_enums.GeneratorFuelsEnum.Ratio

    MinRatio = plx_enums.GeneratorFuelsEnum.MinRatio

    MaxRatio = plx_enums.GeneratorFuelsEnum.MaxRatio

    MaxInput = plx_enums.GeneratorFuelsEnum.MaxInput

    Rating = plx_enums.GeneratorFuelsEnum.Rating

    IsAvailable = plx_enums.GeneratorFuelsEnum.IsAvailable

    HeatRateScalar = plx_enums.GeneratorFuelsEnum.HeatRateScalar

    HeatRateBase = plx_enums.GeneratorFuelsEnum.HeatRateBase

    HeatRate = plx_enums.GeneratorFuelsEnum.HeatRate

    HeatRateIncr = plx_enums.GeneratorFuelsEnum.HeatRateIncr

    HeatRateIncr2 = plx_enums.GeneratorFuelsEnum.HeatRateIncr2

    HeatRateIncr3 = plx_enums.GeneratorFuelsEnum.HeatRateIncr3

    TransitionCostDown = plx_enums.GeneratorFuelsEnum.TransitionCostDown

    TransitionCostUp = plx_enums.GeneratorFuelsEnum.TransitionCostUp

    DecouplingTime = plx_enums.GeneratorFuelsEnum.DecouplingTime

    CouplingTime = plx_enums.GeneratorFuelsEnum.CouplingTime

    EmissionScalar = plx_enums.GeneratorFuelsEnum.EmissionScalar

    OfferQuantity = plx_enums.GeneratorFuelsEnum.OfferQuantity

    OfferPrice = plx_enums.GeneratorFuelsEnum.OfferPrice


class GeneratorHeadStorageEnum(Enum):
    FlowFactor = plx_enums.GeneratorHeadStorageEnum.FlowFactor

    FlowatStart = plx_enums.GeneratorHeadStorageEnum.FlowatStart

    EfficiencyPoint = plx_enums.GeneratorHeadStorageEnum.EfficiencyPoint

    EfficiencyScalar = plx_enums.GeneratorHeadStorageEnum.EfficiencyScalar


class GeneratorHeatOutputNodesEnum(Enum):
    ParticipationFactor = plx_enums.GeneratorHeatOutputNodesEnum.ParticipationFactor


class GeneratorHeatRateDetailEnum(Enum):
    Detailed = plx_enums.GeneratorHeatRateDetailEnum.Detailed

    Simple = plx_enums.GeneratorHeatRateDetailEnum.Simple

    Simplest = plx_enums.GeneratorHeatRateDetailEnum.Simplest


class GeneratorHeatRateModelEnum(Enum):
    OfftakeFx = plx_enums.GeneratorHeatRateModelEnum.OfftakeFx

    Constant = plx_enums.GeneratorHeatRateModelEnum.Constant

    AvgAtPoints = plx_enums.GeneratorHeatRateModelEnum.AvgAtPoints

    IncrwithBase = plx_enums.GeneratorHeatRateModelEnum.IncrwithBase

    IncrwithAvg = plx_enums.GeneratorHeatRateModelEnum.IncrwithAvg

    EfficiencyIncr = plx_enums.GeneratorHeatRateModelEnum.EfficiencyIncr


class GeneratorNodesEnum(Enum):
    GenerationParticipationFactor = plx_enums.GeneratorNodesEnum.GenerationParticipationFactor

    LoadParticipationFactor = plx_enums.GeneratorNodesEnum.LoadParticipationFactor


class GeneratorPricingMethodEnum(Enum):
    Average = plx_enums.GeneratorPricingMethodEnum.Average

    Marginal = plx_enums.GeneratorPricingMethodEnum.Marginal


class GeneratorReserveMethodEnum(Enum):
    Constant = plx_enums.GeneratorReserveMethodEnum.Constant

    Unbounded = plx_enums.GeneratorReserveMethodEnum.Unbounded

    Bounded = plx_enums.GeneratorReserveMethodEnum.Bounded


class GeneratorStartFuelsEnum(Enum):
    OfftakeatStart = plx_enums.GeneratorStartFuelsEnum.OfftakeatStart

    TransportCharge = plx_enums.GeneratorStartFuelsEnum.TransportCharge

    EmissionScalar = plx_enums.GeneratorStartFuelsEnum.EmissionScalar


class GeneratorTailStorageEnum(Enum):
    FlowFactor = plx_enums.GeneratorTailStorageEnum.FlowFactor


class GeneratorTransitionEnum(Enum):
    TransitionCost = plx_enums.GeneratorTransitionEnum.TransitionCost


class GeneratorTransitionTypeEnum(Enum):
    Individual = plx_enums.GeneratorTransitionTypeEnum.Individual

    Group = plx_enums.GeneratorTransitionTypeEnum.Group


class GlobalStoragesEnum(Enum):
    FCFShadowPrice = plx_enums.GlobalStoragesEnum.FCFShadowPrice


class GrowthMethodEnum(Enum):
    None_ = 0

    Linear = plx_enums.GrowthMethodEnum.Linear

    Quadratic = plx_enums.GrowthMethodEnum.Quadratic

    Custom = plx_enums.GrowthMethodEnum.Custom


class HeadEffectsMethodEnum(Enum):
    BackwardLooking = plx_enums.HeadEffectsMethodEnum.BackwardLooking

    Dynamic = plx_enums.HeadEffectsMethodEnum.Dynamic


class HeatNodeHeatExportNodesEnum(Enum):
    ParticipationFactor = plx_enums.HeatNodeHeatExportNodesEnum.ParticipationFactor


class HeatNodeWaterPlantsEnum(Enum):
    ParticipationFactor = plx_enums.HeatNodeWaterPlantsEnum.ParticipationFactor


class HeatPlantFuelsEnum(Enum):
    MutuallyExclusive = plx_enums.HeatPlantFuelsEnum.MutuallyExclusive

    Ratio = plx_enums.HeatPlantFuelsEnum.Ratio

    MinRatio = plx_enums.HeatPlantFuelsEnum.MinRatio

    MaxRatio = plx_enums.HeatPlantFuelsEnum.MaxRatio

    MaxInput = plx_enums.HeatPlantFuelsEnum.MaxInput

    IsAvailable = plx_enums.HeatPlantFuelsEnum.IsAvailable

    HeatRateScalar = plx_enums.HeatPlantFuelsEnum.HeatRateScalar

    HeatRateBase = plx_enums.HeatPlantFuelsEnum.HeatRateBase

    HeatRate = plx_enums.HeatPlantFuelsEnum.HeatRate

    HeatRateIncr = plx_enums.HeatPlantFuelsEnum.HeatRateIncr


class HeatPlantHeatOutputNodesEnum(Enum):
    ParticipationFactor = plx_enums.HeatPlantHeatOutputNodesEnum.ParticipationFactor


class HeatPlantStartFuelsEnum(Enum):
    OfftakeatStart = plx_enums.HeatPlantStartFuelsEnum.OfftakeatStart


class HorizonAttributeEnum(Enum):
    PeriodsperDay = plx_enums.HorizonAttributeEnum.PeriodsperDay

    DateFrom = plx_enums.HorizonAttributeEnum.DateFrom

    StepType = plx_enums.HorizonAttributeEnum.StepType

    StepCount = plx_enums.HorizonAttributeEnum.StepCount

    DayBeginning = plx_enums.HorizonAttributeEnum.DayBeginning

    WeekBeginning = plx_enums.HorizonAttributeEnum.WeekBeginning

    YearEnding = plx_enums.HorizonAttributeEnum.YearEnding

    Chronology = plx_enums.HorizonAttributeEnum.Chronology

    TypicalWeek = plx_enums.HorizonAttributeEnum.TypicalWeek

    ChronoDateFrom = plx_enums.HorizonAttributeEnum.ChronoDateFrom

    ChronoPeriodFrom = plx_enums.HorizonAttributeEnum.ChronoPeriodFrom

    ChronoPeriodTo = plx_enums.HorizonAttributeEnum.ChronoPeriodTo

    ChronoStepType = plx_enums.HorizonAttributeEnum.ChronoStepType

    ChronoAtaTime = plx_enums.HorizonAttributeEnum.ChronoAtaTime

    ChronoStepCount = plx_enums.HorizonAttributeEnum.ChronoStepCount

    LookaheadIndicator = plx_enums.HorizonAttributeEnum.LookaheadIndicator

    LookaheadType = plx_enums.HorizonAttributeEnum.LookaheadType

    LookaheadAtaTime = plx_enums.HorizonAttributeEnum.LookaheadAtaTime

    LookaheadPeriodsperDay = plx_enums.HorizonAttributeEnum.LookaheadPeriodsperDay


class HubPricingMethodEnum(Enum):
    LoadWeightedAverage = plx_enums.HubPricingMethodEnum.LoadWeightedAverage

    GenerationWeigthedAverage = plx_enums.HubPricingMethodEnum.GenerationWeigthedAverage

    WeightedAverage = plx_enums.HubPricingMethodEnum.WeightedAverage


class HydroModelEnum(Enum):
    Auto = plx_enums.HydroModelEnum.Auto

    Energy = plx_enums.HydroModelEnum.Energy

    Level = plx_enums.HydroModelEnum.Level

    Volume = plx_enums.HydroModelEnum.Volume


class ImageEnum(Enum):
    ImageEnum_Closed = plx_enums.ImageEnum.ImageEnum_Closed

    ImageEnum_Open = plx_enums.ImageEnum.ImageEnum_Open

    ImageEnum_DatumInUse = plx_enums.ImageEnum.ImageEnum_DatumInUse

    ImageEnum_DatumNotInUse = plx_enums.ImageEnum.ImageEnum_DatumNotInUse


class IntegerOptimalityEnum(Enum):
    LinearRelaxation = plx_enums.IntegerOptimalityEnum.LinearRelaxation

    RoundedLinearRelaxation = plx_enums.IntegerOptimalityEnum.RoundedLinearRelaxation

    IntegerOptimal = plx_enums.IntegerOptimalityEnum.IntegerOptimal

    DynamicProgram = plx_enums.IntegerOptimalityEnum.DynamicProgram

    Free = plx_enums.IntegerOptimalityEnum.Free


class InterfaceLinesEnum(Enum):
    FlowCoefficient = plx_enums.InterfaceLinesEnum.FlowCoefficient

    FlowForwardCoefficient = plx_enums.InterfaceLinesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.InterfaceLinesEnum.FlowBackCoefficient


class InterfaceTransformersEnum(Enum):
    FlowCoefficient = plx_enums.InterfaceTransformersEnum.FlowCoefficient


class LDCSlicingMethodEnum(Enum):
    PeakOffpeakBias = plx_enums.LDCSlicingMethodEnum.PeakOffpeakBias

    WeightedLeastsquares = plx_enums.LDCSlicingMethodEnum.WeightedLeastsquares


class LTPlanAttributeEnum(Enum):
    DiscountRate = plx_enums.LTPlanAttributeEnum.DiscountRate

    DiscountPeriodType = plx_enums.LTPlanAttributeEnum.DiscountPeriodType

    AtaTime = plx_enums.LTPlanAttributeEnum.AtaTime

    Overlap = plx_enums.LTPlanAttributeEnum.Overlap

    Chronology = plx_enums.LTPlanAttributeEnum.Chronology

    LDCType = plx_enums.LTPlanAttributeEnum.LDCType

    BlockCount = plx_enums.LTPlanAttributeEnum.BlockCount

    LastBlockCount = plx_enums.LTPlanAttributeEnum.LastBlockCount

    LDCSlicingMethod = plx_enums.LTPlanAttributeEnum.LDCSlicingMethod

    LDCWeighta = plx_enums.LTPlanAttributeEnum.LDCWeighta

    LDCWeightb = plx_enums.LTPlanAttributeEnum.LDCWeightb

    LDCWeightc = plx_enums.LTPlanAttributeEnum.LDCWeightc

    LDCWeightd = plx_enums.LTPlanAttributeEnum.LDCWeightd

    LDCPinTop = plx_enums.LTPlanAttributeEnum.LDCPinTop

    LDCPinBottom = plx_enums.LTPlanAttributeEnum.LDCPinBottom

    SampleType = plx_enums.LTPlanAttributeEnum.SampleType

    SamplingInterval = plx_enums.LTPlanAttributeEnum.SamplingInterval

    ReducedSampleCount = plx_enums.LTPlanAttributeEnum.ReducedSampleCount

    ReductionRelativeAccuracy = plx_enums.LTPlanAttributeEnum.ReductionRelativeAccuracy

    Optimality = plx_enums.LTPlanAttributeEnum.Optimality

    IntegerizationHorizon = plx_enums.LTPlanAttributeEnum.IntegerizationHorizon

    EndEffectsMethod = plx_enums.LTPlanAttributeEnum.EndEffectsMethod

    SolutionCount = plx_enums.LTPlanAttributeEnum.SolutionCount

    SolutionQuality = plx_enums.LTPlanAttributeEnum.SolutionQuality

    AlwaysAnnualizeBuildCost = plx_enums.LTPlanAttributeEnum.AlwaysAnnualizeBuildCost

    DepreciationMethod = plx_enums.LTPlanAttributeEnum.DepreciationMethod

    TaxRate = plx_enums.LTPlanAttributeEnum.TaxRate

    InflationRate = plx_enums.LTPlanAttributeEnum.InflationRate

    HeatRateDetail = plx_enums.LTPlanAttributeEnum.HeatRateDetail

    OutageIncrement = plx_enums.LTPlanAttributeEnum.OutageIncrement

    UseEffectiveLoadApproach = plx_enums.LTPlanAttributeEnum.UseEffectiveLoadApproach

    MaintenanceSculpting = plx_enums.LTPlanAttributeEnum.MaintenanceSculpting

    PricingMethod = plx_enums.LTPlanAttributeEnum.PricingMethod

    TransmissionDetail = plx_enums.LTPlanAttributeEnum.TransmissionDetail

    AllowCapacitySharing = plx_enums.LTPlanAttributeEnum.AllowCapacitySharing

    CapacityPaymentsEnabled = plx_enums.LTPlanAttributeEnum.CapacityPaymentsEnabled

    StartCostAmortizationPeriod = plx_enums.LTPlanAttributeEnum.StartCostAmortizationPeriod

    ComputeReliabilityIndices = plx_enums.LTPlanAttributeEnum.ComputeReliabilityIndices

    ComputeMultiareaReliabilityIndices = plx_enums.LTPlanAttributeEnum.ComputeMultiareaReliabilityIndices

    StochasticMethod = plx_enums.LTPlanAttributeEnum.StochasticMethod

    WriteExpansionPlanTextFiles = plx_enums.LTPlanAttributeEnum.WriteExpansionPlanTextFiles


class attributeEnum(Enum):
    AllowCapacitySharing = plx_enums.attributeEnum.AllowCapacitySharing

    AllowDumpEnergy = plx_enums.attributeEnum.AllowDumpEnergy

    AllowUnservedEnergy = plx_enums.attributeEnum.AllowUnservedEnergy

    Annuities = plx_enums.attributeEnum.Annuities

    AtaTime = plx_enums.attributeEnum.AtaTime

    BertrandPricing = plx_enums.attributeEnum.BertrandPricing

    BidCostMarkup = plx_enums.attributeEnum.BidCostMarkup

    BinaryFiles = plx_enums.attributeEnum.BinaryFiles

    BlockCount = plx_enums.attributeEnum.BlockCount

    CapacityFactorConstraintBasis = plx_enums.attributeEnum.CapacityFactorConstraintBasis

    ChronoAtaTime = plx_enums.attributeEnum.ChronoAtaTime

    ChronoDateFrom = plx_enums.attributeEnum.ChronoDateFrom

    ChronoPeriodFrom = plx_enums.attributeEnum.ChronoPeriodFrom

    ChronoPeriodTo = plx_enums.attributeEnum.ChronoPeriodTo

    ChronoStepCount = plx_enums.attributeEnum.ChronoStepCount

    ChronoStepType = plx_enums.attributeEnum.ChronoStepType

    Chronology = plx_enums.attributeEnum.Chronology

    ColdStartOptimizer1 = plx_enums.attributeEnum.ColdStartOptimizer1

    ColdStartOptimizer2 = plx_enums.attributeEnum.ColdStartOptimizer2

    ColdStartOptimizer3 = plx_enums.attributeEnum.ColdStartOptimizer3

    ComputeReliabilityIndices = plx_enums.attributeEnum.ComputeReliabilityIndices

    ConstraintDecomposition = plx_enums.attributeEnum.ConstraintDecomposition

    ConstraintRollover = plx_enums.attributeEnum.ConstraintRollover

    ConstraintVoltageThreshold = plx_enums.attributeEnum.ConstraintVoltageThreshold

    ConstraintsEnabled = plx_enums.attributeEnum.ConstraintsEnabled

    ContractsHandoffPoint = plx_enums.attributeEnum.ContractsHandoffPoint

    ContractsOptimizeOffers = plx_enums.attributeEnum.ContractsOptimizeOffers

    ContractsSettlementMethod = plx_enums.attributeEnum.ContractsSettlementMethod

    ConvergenceReportLevel = plx_enums.attributeEnum.ConvergenceReportLevel

    DateFrom = plx_enums.attributeEnum.DateFrom

    DayBeginning = plx_enums.attributeEnum.DayBeginning

    DecimalPlaces = plx_enums.attributeEnum.DecimalPlaces

    DefaultElasticity = plx_enums.attributeEnum.DefaultElasticity

    DepreciationMethod = plx_enums.attributeEnum.DepreciationMethod

    DiscountRate = plx_enums.attributeEnum.DiscountRate

    DispatchbyPowerStation = plx_enums.attributeEnum.DispatchbyPowerStation

    Enabled = plx_enums.attributeEnum.Enabled

    EndEffectsMethod = plx_enums.attributeEnum.EndEffectsMethod

    EnforceLimitsOnLinesInInterfaces = plx_enums.attributeEnum.EnforceLimitsOnLinesInInterfaces

    EquilibriumModel = plx_enums.attributeEnum.EquilibriumModel

    FuelUseFunctionPrecision = plx_enums.attributeEnum.FuelUseFunctionPrecision

    HeatRate = plx_enums.attributeEnum.HeatRate

    HeatRateErrorMethod = plx_enums.attributeEnum.HeatRateErrorMethod

    HotStartOptimizer1 = plx_enums.attributeEnum.HotStartOptimizer1

    HotStartOptimizer2 = plx_enums.attributeEnum.HotStartOptimizer2

    HotStartOptimizer3 = plx_enums.attributeEnum.HotStartOptimizer3

    IncludeContractGeneration = plx_enums.attributeEnum.IncludeContractGeneration

    IncludeContractLoad = plx_enums.attributeEnum.IncludeContractLoad

    IncludeDemandBids = plx_enums.attributeEnum.IncludeDemandBids

    IncludeDSP = plx_enums.attributeEnum.IncludeDSP

    Infeasibilities = plx_enums.attributeEnum.Infeasibilities

    InflationRate = plx_enums.attributeEnum.InflationRate

    IntegerizationHorizon = plx_enums.attributeEnum.IntegerizationHorizon

    InterfaceConstraintsEnabled = plx_enums.attributeEnum.InterfaceConstraintsEnabled

    InternalVoLL = plx_enums.attributeEnum.InternalVoLL

    InterruptionSharing = plx_enums.attributeEnum.InterruptionSharing

    Latitude = plx_enums.attributeEnum.Latitude

    Longitude = plx_enums.attributeEnum.Longitude

    LookaheadAtaTime = plx_enums.attributeEnum.LookaheadAtaTime

    LookaheadIndicator = plx_enums.attributeEnum.LookaheadIndicator

    LookaheadPeriodsperDay = plx_enums.attributeEnum.LookaheadPeriodsperDay

    LookaheadType = plx_enums.attributeEnum.LookaheadType

    MaxLossRelativeError = plx_enums.attributeEnum.MaxLossRelativeError

    LossMethod = plx_enums.attributeEnum.LossMethod

    LossTolerance = plx_enums.attributeEnum.LossTolerance

    LossVoltageThreshold = plx_enums.attributeEnum.LossVoltageThreshold

    LossesEnabled = plx_enums.attributeEnum.LossesEnabled

    LPFiles = plx_enums.attributeEnum.LPFiles

    LPProgress = plx_enums.attributeEnum.LPProgress

    MakeUniqueName = plx_enums.attributeEnum.MakeUniqueName

    MarketTradingFormat = plx_enums.attributeEnum.MarketTradingFormat

    MarkupMinStableLevel = plx_enums.attributeEnum.MarkupMinStableLevel

    MaxEmbeddedLossIterations = plx_enums.attributeEnum.MaxEmbeddedLossIterations

    MaxHeatRateTranches = plx_enums.attributeEnum.MaxHeatRateTranches

    MaxLossIterations = plx_enums.attributeEnum.MaxLossIterations

    MaxLossTranches = plx_enums.attributeEnum.MaxLossTranches

    Epsilon = plx_enums.attributeEnum.Epsilon

    MaximumThreads = plx_enums.attributeEnum.MaximumThreads

    Method = plx_enums.attributeEnum.Method

    MIPMaxTime = plx_enums.attributeEnum.MIPMaxTime

    MIPMaximumThreads = plx_enums.attributeEnum.MIPMaximumThreads

    MIPNodeOptimizer = plx_enums.attributeEnum.MIPNodeOptimizer

    MIPProgress = plx_enums.attributeEnum.MIPProgress

    MIPRelativeGap = plx_enums.attributeEnum.MIPRelativeGap

    MIPRootOptimizer = plx_enums.attributeEnum.MIPRootOptimizer

    ConvergentSmoothing = plx_enums.attributeEnum.ConvergentSmoothing

    MonteCarloMethod = plx_enums.attributeEnum.MonteCarloMethod

    OutagePatternCount = plx_enums.attributeEnum.OutagePatternCount

    OutageScope = plx_enums.attributeEnum.OutageScope

    WeibullShape = plx_enums.attributeEnum.WeibullShape

    MVABase = plx_enums.attributeEnum.MVABase

    NewEntry = plx_enums.attributeEnum.NewEntry

    NewEntryCapacityMechanism = plx_enums.attributeEnum.NewEntryCapacityMechanism

    NewEntryDriver = plx_enums.attributeEnum.NewEntryDriver

    NewEntryTimeLag = plx_enums.attributeEnum.NewEntryTimeLag

    NoLoadCostMarkup = plx_enums.attributeEnum.NoLoadCostMarkup

    OPFMethod = plx_enums.attributeEnum.OPFMethod

    Optimality = plx_enums.attributeEnum.Optimality

    OutageIncrement = plx_enums.attributeEnum.OutageIncrement

    OutputResultsbyDay = plx_enums.attributeEnum.OutputResultsbyDay

    OutputResultsbyFiscalYear = plx_enums.attributeEnum.OutputResultsbyFiscalYear

    OutputResultsbyMonth = plx_enums.attributeEnum.OutputResultsbyMonth

    OutputResultsbyPeriod = plx_enums.attributeEnum.OutputResultsbyPeriod

    OutputResultsbySample = plx_enums.attributeEnum.OutputResultsbySample

    OutputResultsbyWeek = plx_enums.attributeEnum.OutputResultsbyWeek

    OutputStatistics = plx_enums.attributeEnum.OutputStatistics

    OutputtoFolder = plx_enums.attributeEnum.OutputtoFolder

    Overlap = plx_enums.attributeEnum.Overlap

    PeriodsperDay = plx_enums.attributeEnum.PeriodsperDay

    PricingMethod = plx_enums.attributeEnum.PricingMethod

    PricingStrategy = plx_enums.attributeEnum.PricingStrategy

    PTDFMethod = plx_enums.attributeEnum.PTDFMethod

    FlowPTDFThreshold = plx_enums.attributeEnum.FlowPTDFThreshold

    RandomNumberSeed = plx_enums.attributeEnum.RandomNumberSeed

    ReactanceCutoff = plx_enums.attributeEnum.ReactanceCutoff

    MarginalUnit = plx_enums.attributeEnum.MarginalUnit

    RegionSupply = plx_enums.attributeEnum.RegionSupply

    RelativeGrowthatMin = plx_enums.attributeEnum.RelativeGrowthatMin

    RentalMethod = plx_enums.attributeEnum.RentalMethod

    ReportAllInterregionalFlows = plx_enums.attributeEnum.ReportAllInterregionalFlows

    ReportEnabled = plx_enums.attributeEnum.ReportEnabled

    ReportInjectionandLoadNodes = plx_enums.attributeEnum.ReportInjectionandLoadNodes

    ReportLinesInInterfaces = plx_enums.attributeEnum.ReportLinesInInterfaces

    ReportVoltageThreshold = plx_enums.attributeEnum.ReportVoltageThreshold

    RevenueRecovery = plx_enums.attributeEnum.RevenueRecovery

    RevenueTargetingIterations = plx_enums.attributeEnum.RevenueTargetingIterations

    RevenueTargetingMethod = plx_enums.attributeEnum.RevenueTargetingMethod

    RiskSampleCount = plx_enums.attributeEnum.RiskSampleCount

    RoundingUpThreshold = plx_enums.attributeEnum.RoundingUpThreshold

    RSIBidCostMarkupMethod = plx_enums.attributeEnum.RSIBidCostMarkupMethod

    RSIEnabled = plx_enums.attributeEnum.RSIEnabled

    SCUCConstraintVoltageThreshold = plx_enums.attributeEnum.SCUCConstraintVoltageThreshold

    SCUCEnabled = plx_enums.attributeEnum.SCUCEnabled

    LimitThreshold = plx_enums.attributeEnum.LimitThreshold

    ShiftFactors = plx_enums.attributeEnum.ShiftFactors

    SmallLPNonzeroCount = plx_enums.attributeEnum.SmallLPNonzeroCount

    SmallLPOptimizer = plx_enums.attributeEnum.SmallLPOptimizer

    SmallMIPIntegerCount = plx_enums.attributeEnum.SmallMIPIntegerCount

    SmallMIPMaxTime = plx_enums.attributeEnum.SmallMIPMaxTime

    SmallMIPRelativeGap = plx_enums.attributeEnum.SmallMIPRelativeGap

    SolutionFiles = plx_enums.attributeEnum.SolutionFiles

    SOLVER = plx_enums.attributeEnum.SOLVER

    SolverSummary = plx_enums.attributeEnum.SolverSummary

    StepCount = plx_enums.attributeEnum.StepCount

    StepType = plx_enums.attributeEnum.StepType

    TaxRate = plx_enums.attributeEnum.TaxRate

    TransmissionDetail = plx_enums.attributeEnum.TransmissionDetail

    TransmissionLosses = plx_enums.attributeEnum.TransmissionLosses

    TypicalWeek = plx_enums.attributeEnum.TypicalWeek

    UniformPricing = plx_enums.attributeEnum.UniformPricing

    UnitCommitment = plx_enums.attributeEnum.UnitCommitment

    UnitCommitmentOptimality = plx_enums.attributeEnum.UnitCommitmentOptimality

    UnservedEnergy = plx_enums.attributeEnum.UnservedEnergy

    UseEffectiveLoadApproach = plx_enums.attributeEnum.UseEffectiveLoadApproach

    WeekBeginning = plx_enums.attributeEnum.WeekBeginning

    WriteDatabase = plx_enums.attributeEnum.WriteDatabase

    WriteFlatFiles = plx_enums.attributeEnum.WriteFlatFiles

    WriteXMLFiles = plx_enums.attributeEnum.WriteXMLFiles

    YearEnding = plx_enums.attributeEnum.YearEnding

    EmbeddedLosses = plx_enums.attributeEnum.EmbeddedLosses

    GrowthPeriod = plx_enums.attributeEnum.GrowthPeriod

    StartCostAmortizationPeriod = plx_enums.attributeEnum.StartCostAmortizationPeriod

    DPCapacityFactorErrorThreshold = plx_enums.attributeEnum.DPCapacityFactorErrorThreshold

    DetectNonphysicalLosses = plx_enums.attributeEnum.DetectNonphysicalLosses

    Outages = plx_enums.attributeEnum.Outages

    StochasticMethod = plx_enums.attributeEnum.StochasticMethod

    WriteOutageTextFiles = plx_enums.attributeEnum.WriteOutageTextFiles

    ReadOrder = plx_enums.attributeEnum.ReadOrder

    WriteExpansionPlanTextFiles = plx_enums.attributeEnum.WriteExpansionPlanTextFiles

    DPCapacityFactorThreshold = plx_enums.attributeEnum.DPCapacityFactorThreshold

    LDCType = plx_enums.attributeEnum.LDCType

    Type = plx_enums.attributeEnum.Type

    MissingValueMethod = plx_enums.attributeEnum.MissingValueMethod

    CompoundType = plx_enums.attributeEnum.CompoundType

    CompoundStartDate = plx_enums.attributeEnum.CompoundStartDate

    CongestionCharges = plx_enums.attributeEnum.CongestionCharges

    MarginalLossCharges = plx_enums.attributeEnum.MarginalLossCharges

    BindingContingencies = plx_enums.attributeEnum.BindingContingencies

    FilterObjectsByInterval = plx_enums.attributeEnum.FilterObjectsByInterval

    FilterObjectsInSummary = plx_enums.attributeEnum.FilterObjectsInSummary

    WholeYearsOnly = plx_enums.attributeEnum.WholeYearsOnly

    TaskComponents = plx_enums.attributeEnum.TaskComponents

    FormulateUpfront = plx_enums.attributeEnum.FormulateUpfront

    MaintenanceSculpting = plx_enums.attributeEnum.MaintenanceSculpting

    StartCostMethod = plx_enums.attributeEnum.StartCostMethod

    LimitBootstrapInitialThreshold = plx_enums.attributeEnum.LimitBootstrapInitialThreshold

    LimitBootstrapThresholdDecrement = plx_enums.attributeEnum.LimitBootstrapThresholdDecrement

    MaxLimitIterations = plx_enums.attributeEnum.MaxLimitIterations

    ClearExisting = plx_enums.attributeEnum.ClearExisting

    TaskSize = plx_enums.attributeEnum.TaskSize

    Times = plx_enums.attributeEnum.Times

    SampleSummary = plx_enums.attributeEnum.SampleSummary

    StepSummary = plx_enums.attributeEnum.StepSummary

    BoundNodePhaseAngles = plx_enums.attributeEnum.BoundNodePhaseAngles

    MaxAbsolutePhaseAngle = plx_enums.attributeEnum.MaxAbsolutePhaseAngle

    SCUCInterfaceConstraintsEnabled = plx_enums.attributeEnum.SCUCInterfaceConstraintsEnabled

    GenericNames = plx_enums.attributeEnum.GenericNames

    MPSFiles = plx_enums.attributeEnum.MPSFiles

    CapacityPaymentsEnabled = plx_enums.attributeEnum.CapacityPaymentsEnabled

    FeasibilityRepairWeight = plx_enums.attributeEnum.FeasibilityRepairWeight

    HeatRateDetail = plx_enums.attributeEnum.HeatRateDetail

    RoundedRelaxationTuning = plx_enums.attributeEnum.RoundedRelaxationTuning

    RoundedRelaxationStartThreshold = plx_enums.attributeEnum.RoundedRelaxationStartThreshold

    RoundedRelaxationEndThreshold = plx_enums.attributeEnum.RoundedRelaxationEndThreshold

    RoundedRelaxationThresholdIncrement = plx_enums.attributeEnum.RoundedRelaxationThresholdIncrement

    Locked = plx_enums.attributeEnum.Locked

    SolutionStatus = plx_enums.attributeEnum.SolutionStatus

    XMLContent = plx_enums.attributeEnum.XMLContent

    LDCSlicingMethod = plx_enums.attributeEnum.LDCSlicingMethod

    LDCWeighta = plx_enums.attributeEnum.LDCWeighta

    LDCWeightb = plx_enums.attributeEnum.LDCWeightb

    LDCWeightc = plx_enums.attributeEnum.LDCWeightc

    LDCWeightd = plx_enums.attributeEnum.LDCWeightd

    LDCPinTop = plx_enums.attributeEnum.LDCPinTop

    LDCPinBottom = plx_enums.attributeEnum.LDCPinBottom

    WriteInput = plx_enums.attributeEnum.WriteInput

    MarginalExpansionUnit = plx_enums.attributeEnum.MarginalExpansionUnit

    MarginalUnitIncrement = plx_enums.attributeEnum.MarginalUnitIncrement

    MarginalExpansionIncrement = plx_enums.attributeEnum.MarginalExpansionIncrement

    IncludeMarketPurchases = plx_enums.attributeEnum.IncludeMarketPurchases

    ShapeDistortion = plx_enums.attributeEnum.ShapeDistortion

    ExecutionOrder = plx_enums.attributeEnum.ExecutionOrder

    UpscalingMethod = plx_enums.attributeEnum.UpscalingMethod

    DownscalingMethod = plx_enums.attributeEnum.DownscalingMethod

    SmallMIPImproveStartGap = plx_enums.attributeEnum.SmallMIPImproveStartGap

    MIPImproveStartGap = plx_enums.attributeEnum.MIPImproveStartGap

    ReducedSampleCount = plx_enums.attributeEnum.ReducedSampleCount

    ForcedOutagesinLookahead = plx_enums.attributeEnum.ForcedOutagesinLookahead

    ConvergencePeriodType = plx_enums.attributeEnum.ConvergencePeriodType

    ReductionRelativeAccuracy = plx_enums.attributeEnum.ReductionRelativeAccuracy

    DatetimeConvention = plx_enums.attributeEnum.DatetimeConvention

    Locale = plx_enums.attributeEnum.Locale

    LoadCustomAssemblies = plx_enums.attributeEnum.LoadCustomAssemblies

    TimeLag = plx_enums.attributeEnum.TimeLag

    Report = plx_enums.attributeEnum.Report

    Filter = plx_enums.attributeEnum.Filter

    InclusiveEmpty = plx_enums.attributeEnum.InclusiveEmpty

    Transient = plx_enums.attributeEnum.Transient

    FlatFileFormat = plx_enums.attributeEnum.FlatFileFormat

    FormulateRampUpfront = plx_enums.attributeEnum.FormulateRampUpfront

    WheelingPTDFThreshold = plx_enums.attributeEnum.WheelingPTDFThreshold

    Interleaved = plx_enums.attributeEnum.Interleaved

    BertrandDetectActiveRampConstraints = plx_enums.attributeEnum.BertrandDetectActiveRampConstraints

    BertrandOOMODEnabled = plx_enums.attributeEnum.BertrandOOMODEnabled

    StepFrom = plx_enums.attributeEnum.StepFrom

    StepTo = plx_enums.attributeEnum.StepTo

    ObjectiveFunction = plx_enums.attributeEnum.ObjectiveFunction

    MaxInfeasibilityLogLines = plx_enums.attributeEnum.MaxInfeasibilityLogLines

    IntegersinLookahead = plx_enums.attributeEnum.IntegersinLookahead

    SampleType = plx_enums.attributeEnum.SampleType

    DemandScaling = plx_enums.attributeEnum.DemandScaling

    NetworkReduction = plx_enums.attributeEnum.NetworkReduction

    USEThreshold = plx_enums.attributeEnum.USEThreshold

    EnforceN1Contingencies = plx_enums.attributeEnum.EnforceN1Contingencies

    N1ContingencyVoltageThreshold = plx_enums.attributeEnum.N1ContingencyVoltageThreshold

    TimeInvariant = plx_enums.attributeEnum.TimeInvariant

    FutureCostFunction = plx_enums.attributeEnum.FutureCostFunction

    ReportAllInterzonalFlows = plx_enums.attributeEnum.ReportAllInterzonalFlows

    OutputResultsbyHour = plx_enums.attributeEnum.OutputResultsbyHour

    DiscountPeriodType = plx_enums.attributeEnum.DiscountPeriodType

    StorageDecomposition = plx_enums.attributeEnum.StorageDecomposition

    NPV = plx_enums.attributeEnum.NPV

    ContingencyMonitoringThreshold = plx_enums.attributeEnum.ContingencyMonitoringThreshold

    ScenarioTree = plx_enums.attributeEnum.ScenarioTree

    SampleWeights = plx_enums.attributeEnum.SampleWeights

    LastBlockCount = plx_enums.attributeEnum.LastBlockCount

    ComputeMultiareaReliabilityIndices = plx_enums.attributeEnum.ComputeMultiareaReliabilityIndices

    MarginalUnitTransmissionDetail = plx_enums.attributeEnum.MarginalUnitTransmissionDetail

    TimeShift = plx_enums.attributeEnum.TimeShift

    RunMode = plx_enums.attributeEnum.RunMode

    EFORMaintenanceAdjust = plx_enums.attributeEnum.EFORMaintenanceAdjust

    SolutionCount = plx_enums.attributeEnum.SolutionCount

    SolutionQuality = plx_enums.attributeEnum.SolutionQuality

    OutputResultsbyQuarter = plx_enums.attributeEnum.OutputResultsbyQuarter

    ForcedOutageRelaxesMinDownTime = plx_enums.attributeEnum.ForcedOutageRelaxesMinDownTime

    SamplingInterval = plx_enums.attributeEnum.SamplingInterval

    StartCostMarkup = plx_enums.attributeEnum.StartCostMarkup

    StartCostMarkupProductionBands = plx_enums.attributeEnum.StartCostMarkupProductionBands

    StartCostMarkupWindow = plx_enums.attributeEnum.StartCostMarkupWindow

    SampleFrom = plx_enums.attributeEnum.SampleFrom

    SampleTo = plx_enums.attributeEnum.SampleTo

    RoundedRelaxationCommitmentModel = plx_enums.attributeEnum.RoundedRelaxationCommitmentModel

    PerformanceSummary = plx_enums.attributeEnum.PerformanceSummary

    ReducedOutagePatternCount = plx_enums.attributeEnum.ReducedOutagePatternCount

    UseGenericWriter = plx_enums.attributeEnum.UseGenericWriter

    SortRowColumnNames = plx_enums.attributeEnum.SortRowColumnNames

    StandardizeNames = plx_enums.attributeEnum.StandardizeNames

    StripModelName = plx_enums.attributeEnum.StripModelName

    Algebraic = plx_enums.attributeEnum.Algebraic

    SkipZeroValues = plx_enums.attributeEnum.SkipZeroValues

    ZeroToleranceLP = plx_enums.attributeEnum.ZeroToleranceLP

    ZeroToleranceSOL = plx_enums.attributeEnum.ZeroToleranceSOL

    DecimalPlacesLP = plx_enums.attributeEnum.DecimalPlacesLP

    DecimalPlacesSOL = plx_enums.attributeEnum.DecimalPlacesSOL

    MIPMaxRelaxationRepairTime = plx_enums.attributeEnum.MIPMaxRelaxationRepairTime

    HistoricalSampling = plx_enums.attributeEnum.HistoricalSampling

    HistoricalYearFrom = plx_enums.attributeEnum.HistoricalYearFrom

    HistoricalYearTo = plx_enums.attributeEnum.HistoricalYearTo

    HistoricalYearStart = plx_enums.attributeEnum.HistoricalYearStart

    HistoricalPeriodType = plx_enums.attributeEnum.HistoricalPeriodType

    MaxLossAbsoluteError = plx_enums.attributeEnum.MaxLossAbsoluteError

    HistoricalYearEnding = plx_enums.attributeEnum.HistoricalYearEnding

    MaximumParallelTasks = plx_enums.attributeEnum.MaximumParallelTasks

    TransmissionTopology = plx_enums.attributeEnum.TransmissionTopology

    DatabaseLoad = plx_enums.attributeEnum.DatabaseLoad

    Licensing = plx_enums.attributeEnum.Licensing

    DataFileRead = plx_enums.attributeEnum.DataFileRead

    ComputerInformation = plx_enums.attributeEnum.ComputerInformation

    PumpandGenerate = plx_enums.attributeEnum.PumpandGenerate

    NetworkTraversal = plx_enums.attributeEnum.NetworkTraversal

    MIPStartSolution = plx_enums.attributeEnum.MIPStartSolution

    CacheTransmissionMatrices = plx_enums.attributeEnum.CacheTransmissionMatrices

    BaseYear = plx_enums.attributeEnum.BaseYear

    AlwaysAnnualizeBuildCost = plx_enums.attributeEnum.AlwaysAnnualizeBuildCost

    WriteBridgeTextFiles = plx_enums.attributeEnum.WriteBridgeTextFiles


class classEnum(Enum):
    System = plx_enums.classEnum.System

    Company = plx_enums.classEnum.Company

    Market = plx_enums.classEnum.Market

    FinancialContract = plx_enums.classEnum.FinancialContract

    TransmissionRight = plx_enums.classEnum.TransmissionRight

    Cournot = plx_enums.classEnum.Cournot

    RSI = plx_enums.classEnum.RSI

    Region = plx_enums.classEnum.Region

    Zone = plx_enums.classEnum.Zone

    Node = plx_enums.classEnum.Node

    Line = plx_enums.classEnum.Line

    MLF = plx_enums.classEnum.MLF

    Transformer = plx_enums.classEnum.Transformer

    FlowControl = plx_enums.classEnum.FlowControl

    Interface = plx_enums.classEnum.Interface

    Reserve = plx_enums.classEnum.Reserve

    Contingency = plx_enums.classEnum.Contingency

    Fuel = plx_enums.classEnum.Fuel

    Storage = plx_enums.classEnum.Storage

    Waterway = plx_enums.classEnum.Waterway

    Emission = plx_enums.classEnum.Emission

    Generator = plx_enums.classEnum.Generator

    PowerStation = plx_enums.classEnum.PowerStation

    FuelContract = plx_enums.classEnum.FuelContract

    PhysicalContract = plx_enums.classEnum.PhysicalContract

    Purchaser = plx_enums.classEnum.Purchaser

    Constraint = plx_enums.classEnum.Constraint

    DataFile = plx_enums.classEnum.DataFile

    Variable = plx_enums.classEnum.Variable

    Horizon = plx_enums.classEnum.Horizon

    Report = plx_enums.classEnum.Report

    Timeslice = plx_enums.classEnum.Timeslice

    Scenario = plx_enums.classEnum.Scenario

    Model = plx_enums.classEnum.Model

    Project = plx_enums.classEnum.Project

    LTPlan = plx_enums.classEnum.LTPlan

    PASA = plx_enums.classEnum.PASA

    MTSchedule = plx_enums.classEnum.MTSchedule

    STSchedule = plx_enums.classEnum.STSchedule

    Transmission = plx_enums.classEnum.Transmission

    Production = plx_enums.classEnum.Production

    Competition = plx_enums.classEnum.Competition

    Stochastic = plx_enums.classEnum.Stochastic

    Performance = plx_enums.classEnum.Performance

    Diagnostic = plx_enums.classEnum.Diagnostic

    GasField = plx_enums.classEnum.GasField

    GasStorage = plx_enums.classEnum.GasStorage

    GasPipeline = plx_enums.classEnum.GasPipeline

    GasNode = plx_enums.classEnum.GasNode

    GasDemand = plx_enums.classEnum.GasDemand

    List = plx_enums.classEnum.List

    Abatement = plx_enums.classEnum.Abatement

    GasZone = plx_enums.classEnum.GasZone

    DecisionVariable = plx_enums.classEnum.DecisionVariable

    Global = plx_enums.classEnum.Global

    Hub = plx_enums.classEnum.Hub

    GasBasin = plx_enums.classEnum.GasBasin

    Battery = plx_enums.classEnum.Battery

    Maintenance = plx_enums.classEnum.Maintenance

    WaterPlant = plx_enums.classEnum.WaterPlant

    WaterStorage = plx_enums.classEnum.WaterStorage

    WaterPipeline = plx_enums.classEnum.WaterPipeline

    WaterNode = plx_enums.classEnum.WaterNode

    WaterDemand = plx_enums.classEnum.WaterDemand

    WaterZone = plx_enums.classEnum.WaterZone

    GasContract = plx_enums.classEnum.GasContract

    GasPlant = plx_enums.classEnum.GasPlant

    GasTransport = plx_enums.classEnum.GasTransport

    HeatPlant = plx_enums.classEnum.HeatPlant

    HeatNode = plx_enums.classEnum.HeatNode


class class_groupEnum(Enum):
    Electric = plx_enums.class_groupEnum.Electric

    Transmission = plx_enums.class_groupEnum.Transmission

    Financial = plx_enums.class_groupEnum.Financial

    Generic = plx_enums.class_groupEnum.Generic

    Data = plx_enums.class_groupEnum.Data

    Execute = plx_enums.class_groupEnum.Execute

    Simulation = plx_enums.class_groupEnum.Simulation

    Settings = plx_enums.class_groupEnum.Settings

    Gas = plx_enums.class_groupEnum.Gas

    Water = plx_enums.class_groupEnum.Water

    List = plx_enums.class_groupEnum.List

    Heat = plx_enums.class_groupEnum.Heat


class collectionEnum(Enum):
    CapacityGenerationContracts = plx_enums.collectionEnum.CapacityGenerationContracts

    CapacityGenerators = plx_enums.collectionEnum.CapacityGenerators

    CapacityLoadContracts = plx_enums.collectionEnum.CapacityLoadContracts

    CapacityMarkets = plx_enums.collectionEnum.CapacityMarkets

    CapacityPurchasers = plx_enums.collectionEnum.CapacityPurchasers

    CapacityZone = plx_enums.collectionEnum.CapacityZone

    Companies = plx_enums.collectionEnum.Companies

    Competition = plx_enums.collectionEnum.Competition

    Conditions = plx_enums.collectionEnum.Conditions

    Constraints = plx_enums.collectionEnum.Constraints

    Contingencies = plx_enums.collectionEnum.Contingencies

    Cournots = plx_enums.collectionEnum.Cournots

    DataFiles = plx_enums.collectionEnum.DataFiles

    Diagnostic = plx_enums.collectionEnum.Diagnostic

    Diagnostics = plx_enums.collectionEnum.Diagnostics

    Emissions = plx_enums.collectionEnum.Emissions

    ExportingCapacityLines = plx_enums.collectionEnum.ExportingCapacityLines

    ExportingLines = plx_enums.collectionEnum.ExportingLines

    FinancialContracts = plx_enums.collectionEnum.FinancialContracts

    Fuel = plx_enums.collectionEnum.Fuel

    FuelContracts = plx_enums.collectionEnum.FuelContracts

    Fuels = plx_enums.collectionEnum.Fuels

    GeneratingCompanies = plx_enums.collectionEnum.GeneratingCompanies

    GenerationContracts = plx_enums.collectionEnum.GenerationContracts

    GenerationNode = plx_enums.collectionEnum.GenerationNode

    GeneratorContingencies = plx_enums.collectionEnum.GeneratorContingencies

    Generators = plx_enums.collectionEnum.Generators

    HeadStorage = plx_enums.collectionEnum.HeadStorage

    HeatGenerators = plx_enums.collectionEnum.HeatGenerators

    HeatInput = plx_enums.collectionEnum.HeatInput

    Horizon = plx_enums.collectionEnum.Horizon

    Horizons = plx_enums.collectionEnum.Horizons

    ImportingCapacityLines = plx_enums.collectionEnum.ImportingCapacityLines

    ImportingLines = plx_enums.collectionEnum.ImportingLines

    Interfaces = plx_enums.collectionEnum.Interfaces

    InterregionalLines = plx_enums.collectionEnum.InterregionalLines

    InterzonalLines = plx_enums.collectionEnum.InterzonalLines

    IntraregionalLines = plx_enums.collectionEnum.IntraregionalLines

    IntrazonalLines = plx_enums.collectionEnum.IntrazonalLines

    Line = plx_enums.collectionEnum.Line

    LineContingencies = plx_enums.collectionEnum.LineContingencies

    Lines = plx_enums.collectionEnum.Lines

    LoadContracts = plx_enums.collectionEnum.LoadContracts

    LoadNode = plx_enums.collectionEnum.LoadNode

    LTPlan = plx_enums.collectionEnum.LTPlan

    Markets = plx_enums.collectionEnum.Markets

    MLFs = plx_enums.collectionEnum.MLFs

    Models = plx_enums.collectionEnum.Models

    MTSchedule = plx_enums.collectionEnum.MTSchedule

    NestedReserves = plx_enums.collectionEnum.NestedReserves

    Node = plx_enums.collectionEnum.Node

    NodeFrom = plx_enums.collectionEnum.NodeFrom

    NodeTo = plx_enums.collectionEnum.NodeTo

    Nodes = plx_enums.collectionEnum.Nodes

    PASA = plx_enums.collectionEnum.PASA

    Performance = plx_enums.collectionEnum.Performance

    FlowControls = plx_enums.collectionEnum.FlowControls

    PhysicalContracts = plx_enums.collectionEnum.PhysicalContracts

    PowerStation = plx_enums.collectionEnum.PowerStation

    PowerStations = plx_enums.collectionEnum.PowerStations

    Production = plx_enums.collectionEnum.Production

    Projects = plx_enums.collectionEnum.Projects

    Purchasers = plx_enums.collectionEnum.Purchasers

    PurchasingCompanies = plx_enums.collectionEnum.PurchasingCompanies

    ReferenceNode = plx_enums.collectionEnum.ReferenceNode

    Region = plx_enums.collectionEnum.Region

    Regions = plx_enums.collectionEnum.Regions

    Report = plx_enums.collectionEnum.Report

    Reports = plx_enums.collectionEnum.Reports

    Reserves = plx_enums.collectionEnum.Reserves

    RSIs = plx_enums.collectionEnum.RSIs

    Scenarios = plx_enums.collectionEnum.Scenarios

    STSchedule = plx_enums.collectionEnum.STSchedule

    StartFuels = plx_enums.collectionEnum.StartFuels

    Stochastic = plx_enums.collectionEnum.Stochastic

    StorageFrom = plx_enums.collectionEnum.StorageFrom

    StorageTo = plx_enums.collectionEnum.StorageTo

    Storages = plx_enums.collectionEnum.Storages

    TailStorage = plx_enums.collectionEnum.TailStorage

    Timeslices = plx_enums.collectionEnum.Timeslices

    Transformers = plx_enums.collectionEnum.Transformers

    Transmission = plx_enums.collectionEnum.Transmission

    TransmissionRights = plx_enums.collectionEnum.TransmissionRights

    Utilities = plx_enums.collectionEnum.Utilities

    Variables = plx_enums.collectionEnum.Variables

    Waterways = plx_enums.collectionEnum.Waterways

    Zone = plx_enums.collectionEnum.Zone

    Zones = plx_enums.collectionEnum.Zones

    MonitoredLines = plx_enums.collectionEnum.MonitoredLines

    MonitoredTransformers = plx_enums.collectionEnum.MonitoredTransformers

    MonitoredInterfaces = plx_enums.collectionEnum.MonitoredInterfaces

    GeneratorCostAllocation = plx_enums.collectionEnum.GeneratorCostAllocation

    GasFields = plx_enums.collectionEnum.GasFields

    GasStorages = plx_enums.collectionEnum.GasStorages

    GasPipelines = plx_enums.collectionEnum.GasPipelines

    GasNodes = plx_enums.collectionEnum.GasNodes

    GasDemands = plx_enums.collectionEnum.GasDemands

    GasNode = plx_enums.collectionEnum.GasNode

    GasNodeFrom = plx_enums.collectionEnum.GasNodeFrom

    GasNodeTo = plx_enums.collectionEnum.GasNodeTo

    Lists = plx_enums.collectionEnum.Lists

    Interleaved = plx_enums.collectionEnum.Interleaved

    Template = plx_enums.collectionEnum.Template

    Abatements = plx_enums.collectionEnum.Abatements

    Consumables = plx_enums.collectionEnum.Consumables

    GasZones = plx_enums.collectionEnum.GasZones

    ExportingGasPipelines = plx_enums.collectionEnum.ExportingGasPipelines

    ImportingGasPipelines = plx_enums.collectionEnum.ImportingGasPipelines

    InterzonalGasPipelines = plx_enums.collectionEnum.InterzonalGasPipelines

    IntrazonalGasPipelines = plx_enums.collectionEnum.IntrazonalGasPipelines

    ExportingCapacityTransformers = plx_enums.collectionEnum.ExportingCapacityTransformers

    ImportingCapacityTransformers = plx_enums.collectionEnum.ImportingCapacityTransformers

    DecisionVariables = plx_enums.collectionEnum.DecisionVariables

    Globals = plx_enums.collectionEnum.Globals

    Definition = plx_enums.collectionEnum.Definition

    Hubs = plx_enums.collectionEnum.Hubs

    ZoneFrom = plx_enums.collectionEnum.ZoneFrom

    ZoneTo = plx_enums.collectionEnum.ZoneTo

    HubFrom = plx_enums.collectionEnum.HubFrom

    HubTo = plx_enums.collectionEnum.HubTo

    GasBasins = plx_enums.collectionEnum.GasBasins

    Batteries = plx_enums.collectionEnum.Batteries

    GasBasin = plx_enums.collectionEnum.GasBasin

    Nodes_star_ = plx_enums.collectionEnum.Nodes_star_

    Maintenances = plx_enums.collectionEnum.Maintenances

    Prerequisites = plx_enums.collectionEnum.Prerequisites

    ExportingTransformers = plx_enums.collectionEnum.ExportingTransformers

    ImportingTransformers = plx_enums.collectionEnum.ImportingTransformers

    InterregionalTransformers = plx_enums.collectionEnum.InterregionalTransformers

    InterzonalTransformers = plx_enums.collectionEnum.InterzonalTransformers

    IntraregionalTransformers = plx_enums.collectionEnum.IntraregionalTransformers

    IntrazonalTransformers = plx_enums.collectionEnum.IntrazonalTransformers

    Lines_star_ = plx_enums.collectionEnum.Lines_star_

    WaterPlants = plx_enums.collectionEnum.WaterPlants

    WaterStorages = plx_enums.collectionEnum.WaterStorages

    WaterPipelines = plx_enums.collectionEnum.WaterPipelines

    WaterNodes = plx_enums.collectionEnum.WaterNodes

    WaterDemands = plx_enums.collectionEnum.WaterDemands

    WaterZones = plx_enums.collectionEnum.WaterZones

    WaterNode = plx_enums.collectionEnum.WaterNode

    WaterNodeFrom = plx_enums.collectionEnum.WaterNodeFrom

    WaterNodeTo = plx_enums.collectionEnum.WaterNodeTo

    ExportingWaterPipelines = plx_enums.collectionEnum.ExportingWaterPipelines

    ImportingWaterPipelines = plx_enums.collectionEnum.ImportingWaterPipelines

    InterzonalWaterPipelines = plx_enums.collectionEnum.InterzonalWaterPipelines

    IntrazonalWaterPipelines = plx_enums.collectionEnum.IntrazonalWaterPipelines

    GasContracts = plx_enums.collectionEnum.GasContracts

    InputNode = plx_enums.collectionEnum.InputNode

    OutputNode = plx_enums.collectionEnum.OutputNode

    GasPlants = plx_enums.collectionEnum.GasPlants

    GasTransports = plx_enums.collectionEnum.GasTransports

    ExportNode = plx_enums.collectionEnum.ExportNode

    ImportNode = plx_enums.collectionEnum.ImportNode

    ExportingGasTransports = plx_enums.collectionEnum.ExportingGasTransports

    ImportingGasTransports = plx_enums.collectionEnum.ImportingGasTransports

    InterzonalGasTransports = plx_enums.collectionEnum.InterzonalGasTransports

    IntrazonalGasTransports = plx_enums.collectionEnum.IntrazonalGasTransports

    Transition = plx_enums.collectionEnum.Transition

    HeatPlants = plx_enums.collectionEnum.HeatPlants

    HeatNodes = plx_enums.collectionEnum.HeatNodes

    HeatInputNodes = plx_enums.collectionEnum.HeatInputNodes

    HeatOutputNodes = plx_enums.collectionEnum.HeatOutputNodes

    HeatExportNodes = plx_enums.collectionEnum.HeatExportNodes

    CapacityBatteries = plx_enums.collectionEnum.CapacityBatteries

    MarktoMarkets = plx_enums.collectionEnum.MarktoMarkets


class propertyEnum(Enum):
    AggregateTransmission = plx_enums.propertyEnum.AggregateTransmission

    Allocation = plx_enums.propertyEnum.Allocation

    AllocationDay = plx_enums.propertyEnum.AllocationDay

    AllocationMonth = plx_enums.propertyEnum.AllocationMonth

    AllocationWeek = plx_enums.propertyEnum.AllocationWeek

    AllocationYear = plx_enums.propertyEnum.AllocationYear

    AllowDumpEnergy = plx_enums.propertyEnum.AllowDumpEnergy

    AllowUnservedEnergy = plx_enums.propertyEnum.AllowUnservedEnergy

    CostAllocationModel = plx_enums.propertyEnum.CostAllocationModel

    DynamicRisk = plx_enums.propertyEnum.DynamicRisk

    InterruptibleLoadLogic = plx_enums.propertyEnum.InterruptibleLoadLogic

    Angle = plx_enums.propertyEnum.Angle

    AskSpread = plx_enums.propertyEnum.AskSpread

    AutoCorrelation = plx_enums.propertyEnum.AutoCorrelation

    AuxBase = plx_enums.propertyEnum.AuxBase

    AuxFixed = plx_enums.propertyEnum.AuxFixed

    AuxIncr = plx_enums.propertyEnum.AuxIncr

    AverageLoad = plx_enums.propertyEnum.AverageLoad

    BaseProfile = plx_enums.propertyEnum.BaseProfile

    BaseQuantity = plx_enums.propertyEnum.BaseQuantity

    BenefitFunctionShape = plx_enums.propertyEnum.BenefitFunctionShape

    BidCostMarkup = plx_enums.propertyEnum.BidCostMarkup

    BidPrice = plx_enums.propertyEnum.BidPrice

    BidQuantity = plx_enums.propertyEnum.BidQuantity

    BidSpread = plx_enums.propertyEnum.BidSpread

    BidAskSpread = plx_enums.propertyEnum.BidAskSpread

    BoilerEfficiency = plx_enums.propertyEnum.BoilerEfficiency

    BoilerHeatRateIncr = plx_enums.propertyEnum.BoilerHeatRateIncr

    BoundedLernerIndex = plx_enums.propertyEnum.BoundedLernerIndex

    BuildCost = plx_enums.propertyEnum.BuildCost

    BuyBlock = plx_enums.propertyEnum.BuyBlock

    BuyBlockDay = plx_enums.propertyEnum.BuyBlockDay

    BuyBlockMonth = plx_enums.propertyEnum.BuyBlockMonth

    BuyBlockWeek = plx_enums.propertyEnum.BuyBlockWeek

    BuyBlockYear = plx_enums.propertyEnum.BuyBlockYear

    BuyUnit = plx_enums.propertyEnum.BuyUnit

    HeatValue = plx_enums.propertyEnum.HeatValue

    CapPrice = plx_enums.propertyEnum.CapPrice

    CapacityBuiltCoefficient = plx_enums.propertyEnum.CapacityBuiltCoefficient

    CapacityExcessPrice = plx_enums.propertyEnum.CapacityExcessPrice

    CapacityFactorCoefficient = plx_enums.propertyEnum.CapacityFactorCoefficient

    FirmCapacity = plx_enums.propertyEnum.FirmCapacity

    CapacityReservesCoefficient = plx_enums.propertyEnum.CapacityReservesCoefficient

    CapacityRetiredCoefficient = plx_enums.propertyEnum.CapacityRetiredCoefficient

    CapacityShortagePrice = plx_enums.propertyEnum.CapacityShortagePrice

    CHPElectricHeatRateIncr = plx_enums.propertyEnum.CHPElectricHeatRateIncr

    CHPHeatSurrogateRateIncr = plx_enums.propertyEnum.CHPHeatSurrogateRateIncr

    LoadCoefficient = plx_enums.propertyEnum.LoadCoefficient

    GenerationCoefficient = plx_enums.propertyEnum.GenerationCoefficient

    Commit = plx_enums.propertyEnum.Commit

    CommittedCapacityCoefficient = plx_enums.propertyEnum.CommittedCapacityCoefficient

    ConditionLogic = plx_enums.propertyEnum.ConditionLogic

    ConstraintPaymentsCompatibility = plx_enums.propertyEnum.ConstraintPaymentsCompatibility

    ConstraintPaymentsEnabled = plx_enums.propertyEnum.ConstraintPaymentsEnabled

    ContractVolumeCoefficient = plx_enums.propertyEnum.ContractVolumeCoefficient

    ConversionRate = plx_enums.propertyEnum.ConversionRate

    Correlation = plx_enums.propertyEnum.Correlation

    Cost = plx_enums.propertyEnum.Cost

    CutoffSize = plx_enums.propertyEnum.CutoffSize

    DebtCharge = plx_enums.propertyEnum.DebtCharge

    DecliningDepreciationBalance = plx_enums.propertyEnum.DecliningDepreciationBalance

    DecompositionMethod = plx_enums.propertyEnum.DecompositionMethod

    Demand = plx_enums.propertyEnum.Demand

    DemandCurve = plx_enums.propertyEnum.DemandCurve

    DemandFnIntercept = plx_enums.propertyEnum.DemandFnIntercept

    DemandFnSlope = plx_enums.propertyEnum.DemandFnSlope

    DemandIntercept = plx_enums.propertyEnum.DemandIntercept

    LoadRisk = plx_enums.propertyEnum.LoadRisk

    DemandSlope = plx_enums.propertyEnum.DemandSlope

    LoadSquaredCoefficient = plx_enums.propertyEnum.LoadSquaredCoefficient

    DistributionType = plx_enums.propertyEnum.DistributionType

    DownstreamEfficiency = plx_enums.propertyEnum.DownstreamEfficiency

    DSPBidPrice = plx_enums.propertyEnum.DSPBidPrice

    DSPBidQuantity = plx_enums.propertyEnum.DSPBidQuantity

    DSPBidRatio = plx_enums.propertyEnum.DSPBidRatio

    EconomicLife = plx_enums.propertyEnum.EconomicLife

    Effectiveness = plx_enums.propertyEnum.Effectiveness

    EfficiencyIncr = plx_enums.propertyEnum.EfficiencyIncr

    EmissionCoefficient = plx_enums.propertyEnum.EmissionCoefficient

    EmissionScalar = plx_enums.propertyEnum.EmissionScalar

    EndEffectsMethod = plx_enums.propertyEnum.EndEffectsMethod

    EndVolumeCoefficient = plx_enums.propertyEnum.EndVolumeCoefficient

    Energy = plx_enums.propertyEnum.Energy

    EnergyUsage = plx_enums.propertyEnum.EnergyUsage

    EnergyValue = plx_enums.propertyEnum.EnergyValue

    EnforceLimits = plx_enums.propertyEnum.EnforceLimits

    EquityCharge = plx_enums.propertyEnum.EquityCharge

    ErrorStdDev = plx_enums.propertyEnum.ErrorStdDev

    ExpansionCost = plx_enums.propertyEnum.ExpansionCost

    ExpansionOptimality = plx_enums.propertyEnum.ExpansionOptimality

    ExportCapacityBuiltCoefficient = plx_enums.propertyEnum.ExportCapacityBuiltCoefficient

    ExportCapacityCoefficient = plx_enums.propertyEnum.ExportCapacityCoefficient

    ExportCapacityRetiredCoefficient = plx_enums.propertyEnum.ExportCapacityRetiredCoefficient

    Exports = plx_enums.propertyEnum.Exports

    Filename = plx_enums.propertyEnum.Filename

    FixedCostScalar = plx_enums.propertyEnum.FixedCostScalar

    FixedFlow = plx_enums.propertyEnum.FixedFlow

    FixedGeneration = plx_enums.propertyEnum.FixedGeneration

    CapacityCharge = plx_enums.propertyEnum.CapacityCharge

    FixedLoad = plx_enums.propertyEnum.FixedLoad

    CapacityChargeDay = plx_enums.propertyEnum.CapacityChargeDay

    FixedLoadMethod = plx_enums.propertyEnum.FixedLoadMethod

    FixedLoss = plx_enums.propertyEnum.FixedLoss

    FloorPrice = plx_enums.propertyEnum.FloorPrice

    FlowBackCoefficient = plx_enums.propertyEnum.FlowBackCoefficient

    FlowCoefficient = plx_enums.propertyEnum.FlowCoefficient

    FlowFactor = plx_enums.propertyEnum.FlowFactor

    FlowForwardCoefficient = plx_enums.propertyEnum.FlowForwardCoefficient

    FlowSquaredCoefficient = plx_enums.propertyEnum.FlowSquaredCoefficient

    FlowingBackCoefficient = plx_enums.propertyEnum.FlowingBackCoefficient

    FlowingForwardCoefficient = plx_enums.propertyEnum.FlowingForwardCoefficient

    FOMCharge = plx_enums.propertyEnum.FOMCharge

    ForcedOutage = plx_enums.propertyEnum.ForcedOutage

    ForcedOutageRate = plx_enums.propertyEnum.ForcedOutageRate

    FuelMixPenalty = plx_enums.propertyEnum.FuelMixPenalty

    FuelOfftakeCoefficient = plx_enums.propertyEnum.FuelOfftakeCoefficient

    FuelPrice = plx_enums.propertyEnum.FuelPrice

    GenerationCapacityBuiltCoefficient = plx_enums.propertyEnum.GenerationCapacityBuiltCoefficient

    GenerationCapacityCoefficient = plx_enums.propertyEnum.GenerationCapacityCoefficient

    GenerationCapacityRetiredCoefficient = plx_enums.propertyEnum.GenerationCapacityRetiredCoefficient

    GenerationParticipationFactor = plx_enums.propertyEnum.GenerationParticipationFactor

    GenerationSquaredCoefficient = plx_enums.propertyEnum.GenerationSquaredCoefficient

    GenerationSUMSquaredCoefficient = plx_enums.propertyEnum.GenerationSUMSquaredCoefficient

    GeneratorSettlementModel = plx_enums.propertyEnum.GeneratorSettlementModel

    HeatLoad = plx_enums.propertyEnum.HeatLoad

    HeatProductionCoefficient = plx_enums.propertyEnum.HeatProductionCoefficient

    HeatRate = plx_enums.propertyEnum.HeatRate

    HeatRateBase = plx_enums.propertyEnum.HeatRateBase

    HeatRateIncr = plx_enums.propertyEnum.HeatRateIncr

    HeatRateIncr2 = plx_enums.propertyEnum.HeatRateIncr2

    HeatRateIncr3 = plx_enums.propertyEnum.HeatRateIncr3

    HeatRateScalar = plx_enums.propertyEnum.HeatRateScalar

    HighRefArea = plx_enums.propertyEnum.HighRefArea

    HighRefLevel = plx_enums.propertyEnum.HighRefLevel

    Holiday = plx_enums.propertyEnum.Holiday

    MaxRampPenalty = plx_enums.propertyEnum.MaxRampPenalty

    MinFlowPenalty = plx_enums.propertyEnum.MinFlowPenalty

    ImportCapacityBuiltCoefficient = plx_enums.propertyEnum.ImportCapacityBuiltCoefficient

    ImportCapacityCoefficient = plx_enums.propertyEnum.ImportCapacityCoefficient

    ImportCapacityRetiredCoefficient = plx_enums.propertyEnum.ImportCapacityRetiredCoefficient

    Imports = plx_enums.propertyEnum.Imports

    Include = plx_enums.propertyEnum.Include

    IncludeinLTPlan = plx_enums.propertyEnum.IncludeinLTPlan

    IncludeinMTSchedule = plx_enums.propertyEnum.IncludeinMTSchedule

    IncludeinPASA = plx_enums.propertyEnum.IncludeinPASA

    IncludeinRegionSupply = plx_enums.propertyEnum.IncludeinRegionSupply

    IncludeinSTSchedule = plx_enums.propertyEnum.IncludeinSTSchedule

    IncludeinUniformPricing = plx_enums.propertyEnum.IncludeinUniformPricing

    InitialGeneration = plx_enums.propertyEnum.InitialGeneration

    InitialHoursDown = plx_enums.propertyEnum.InitialHoursDown

    InitialHoursUp = plx_enums.propertyEnum.InitialHoursUp

    InitialLevel = plx_enums.propertyEnum.InitialLevel

    InitialUnitsGenerating = plx_enums.propertyEnum.InitialUnitsGenerating

    InitialVolume = plx_enums.propertyEnum.InitialVolume

    InputScalar = plx_enums.propertyEnum.InputScalar

    InstalledCapacityCoefficient = plx_enums.propertyEnum.InstalledCapacityCoefficient

    Intercept = plx_enums.propertyEnum.Intercept

    IsAvailable = plx_enums.propertyEnum.IsAvailable

    IsEnabled = plx_enums.propertyEnum.IsEnabled

    IsForward = plx_enums.propertyEnum.IsForward

    IsMarginal = plx_enums.propertyEnum.IsMarginal

    IsSlackBus = plx_enums.propertyEnum.IsSlackBus

    IsStrategic = plx_enums.propertyEnum.IsStrategic

    LernerIndex = plx_enums.propertyEnum.LernerIndex

    LernerIndexCalibrationFactor = plx_enums.propertyEnum.LernerIndexCalibrationFactor

    LernerIndexStdDev = plx_enums.propertyEnum.LernerIndexStdDev

    LernerIndextstatistic = plx_enums.propertyEnum.LernerIndextstatistic

    LimitPenalty = plx_enums.propertyEnum.LimitPenalty

    Load = plx_enums.propertyEnum.Load

    LoadCapacityRatioCoefficient = plx_enums.propertyEnum.LoadCapacityRatioCoefficient

    LoadIncludesLosses = plx_enums.propertyEnum.LoadIncludesLosses

    LoadObligation = plx_enums.propertyEnum.LoadObligation

    LoadParticipationFactor = plx_enums.propertyEnum.LoadParticipationFactor

    LoadPoint = plx_enums.propertyEnum.LoadPoint

    LoadScalar = plx_enums.propertyEnum.LoadScalar

    LoadSettlementModel = plx_enums.propertyEnum.LoadSettlementModel

    LoadUnhedgedCoefficient = plx_enums.propertyEnum.LoadUnhedgedCoefficient

    LoadVariationCoefficient = plx_enums.propertyEnum.LoadVariationCoefficient

    LossAllocation = plx_enums.propertyEnum.LossAllocation

    LossBase = plx_enums.propertyEnum.LossBase

    LossBaseBack = plx_enums.propertyEnum.LossBaseBack

    MarginalLossFactor = plx_enums.propertyEnum.MarginalLossFactor

    MarginalLossFactorBack = plx_enums.propertyEnum.MarginalLossFactorBack

    LossIncr = plx_enums.propertyEnum.LossIncr

    LossIncrBack = plx_enums.propertyEnum.LossIncrBack

    LossIncr2 = plx_enums.propertyEnum.LossIncr2

    LossIncr2Back = plx_enums.propertyEnum.LossIncr2Back

    LowRefArea = plx_enums.propertyEnum.LowRefArea

    LowRefLevel = plx_enums.propertyEnum.LowRefLevel

    Maintenance = plx_enums.propertyEnum.Maintenance

    MaintenanceFactor = plx_enums.propertyEnum.MaintenanceFactor

    MaintenanceFrequency = plx_enums.propertyEnum.MaintenanceFrequency

    MaintenanceRate = plx_enums.propertyEnum.MaintenanceRate

    Markup = plx_enums.propertyEnum.Markup

    MarkupBias = plx_enums.propertyEnum.MarkupBias

    MaxAngle = plx_enums.propertyEnum.MaxAngle

    MaxBenefitFunctionTranches = plx_enums.propertyEnum.MaxBenefitFunctionTranches

    MaxBoilerHeat = plx_enums.propertyEnum.MaxBoilerHeat

    MaxCapacity = plx_enums.propertyEnum.MaxCapacity

    MaxCapacityFactor = plx_enums.propertyEnum.MaxCapacityFactor

    MaxCapacityFactorDay = plx_enums.propertyEnum.MaxCapacityFactorDay

    MaxCapacityFactorMonth = plx_enums.propertyEnum.MaxCapacityFactorMonth

    MaxCapacityFactorWeek = plx_enums.propertyEnum.MaxCapacityFactorWeek

    MaxCapacityFactorYear = plx_enums.propertyEnum.MaxCapacityFactorYear

    MaxCapacityReserveMargin = plx_enums.propertyEnum.MaxCapacityReserveMargin

    MaxCapacityReserves = plx_enums.propertyEnum.MaxCapacityReserves

    MaxEnergy = plx_enums.propertyEnum.MaxEnergy

    MaxEnergyDay = plx_enums.propertyEnum.MaxEnergyDay

    MaxEnergyMonth = plx_enums.propertyEnum.MaxEnergyMonth

    MaxEnergyWeek = plx_enums.propertyEnum.MaxEnergyWeek

    MaxEnergyYear = plx_enums.propertyEnum.MaxEnergyYear

    MaxExpansion = plx_enums.propertyEnum.MaxExpansion

    MaxFlow = plx_enums.propertyEnum.MaxFlow

    MaxGeneration = plx_enums.propertyEnum.MaxGeneration

    MaxHeatRateTranches = plx_enums.propertyEnum.MaxHeatRateTranches

    MaxInput = plx_enums.propertyEnum.MaxInput

    MaxLernerIndex = plx_enums.propertyEnum.MaxLernerIndex

    MaxLevel = plx_enums.propertyEnum.MaxLevel

    MaxLoad = plx_enums.propertyEnum.MaxLoad

    MaxLossTranches = plx_enums.propertyEnum.MaxLossTranches

    MaxMaintenance = plx_enums.propertyEnum.MaxMaintenance

    MaxNetInjection = plx_enums.propertyEnum.MaxNetInjection

    MaxNetOfftake = plx_enums.propertyEnum.MaxNetOfftake

    MaxProvision = plx_enums.propertyEnum.MaxProvision

    MaxPumpResponse = plx_enums.propertyEnum.MaxPumpResponse

    MaxPurchases = plx_enums.propertyEnum.MaxPurchases

    MaxRamp = plx_enums.propertyEnum.MaxRamp

    MaxRampDown = plx_enums.propertyEnum.MaxRampDown

    MaxRampUp = plx_enums.propertyEnum.MaxRampUp

    MaxRating = plx_enums.propertyEnum.MaxRating

    MaxRatio = plx_enums.propertyEnum.MaxRatio

    MaxRelease = plx_enums.propertyEnum.MaxRelease

    MaxReplacement = plx_enums.propertyEnum.MaxReplacement

    MaxResponse = plx_enums.propertyEnum.MaxResponse

    MaxRHS = plx_enums.propertyEnum.MaxRHS

    MaxSales = plx_enums.propertyEnum.MaxSales

    MaxSpill = plx_enums.propertyEnum.MaxSpill

    MaxSyncCondResponse = plx_enums.propertyEnum.MaxSyncCondResponse

    MaxTimeToRepair = plx_enums.propertyEnum.MaxTimeToRepair

    MaxUnitsBuilt = plx_enums.propertyEnum.MaxUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.propertyEnum.MaxUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.propertyEnum.MaxUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.propertyEnum.MaxUnitsRetiredinYear

    MaxValue = plx_enums.propertyEnum.MaxValue

    MaxValueStdDev = plx_enums.propertyEnum.MaxValueStdDev

    MaxVolume = plx_enums.propertyEnum.MaxVolume

    Maximum = plx_enums.propertyEnum.Maximum

    MeanReversion = plx_enums.propertyEnum.MeanReversion

    MeanTimetoRepair = plx_enums.propertyEnum.MeanTimetoRepair

    MinAngle = plx_enums.propertyEnum.MinAngle

    MinCapacityFactor = plx_enums.propertyEnum.MinCapacityFactor

    MinCapacityFactorDay = plx_enums.propertyEnum.MinCapacityFactorDay

    MinCapacityFactorMonth = plx_enums.propertyEnum.MinCapacityFactorMonth

    MinCapacityFactorWeek = plx_enums.propertyEnum.MinCapacityFactorWeek

    MinCapacityFactorYear = plx_enums.propertyEnum.MinCapacityFactorYear

    MinCapacityReserveMargin = plx_enums.propertyEnum.MinCapacityReserveMargin

    MinCapacityReserves = plx_enums.propertyEnum.MinCapacityReserves

    MinDownTime = plx_enums.propertyEnum.MinDownTime

    MinFlow = plx_enums.propertyEnum.MinFlow

    MinGeneration = plx_enums.propertyEnum.MinGeneration

    MinLernerIndex = plx_enums.propertyEnum.MinLernerIndex

    MinLevel = plx_enums.propertyEnum.MinLevel

    MinLoad = plx_enums.propertyEnum.MinLoad

    MinProvision = plx_enums.propertyEnum.MinProvision

    MinPumpLoad = plx_enums.propertyEnum.MinPumpLoad

    MinPurchases = plx_enums.propertyEnum.MinPurchases

    MinRating = plx_enums.propertyEnum.MinRating

    MinRatio = plx_enums.propertyEnum.MinRatio

    MinRelease = plx_enums.propertyEnum.MinRelease

    MinRHS = plx_enums.propertyEnum.MinRHS

    MinSales = plx_enums.propertyEnum.MinSales

    MinStableLevel = plx_enums.propertyEnum.MinStableLevel

    MinTimeToRepair = plx_enums.propertyEnum.MinTimeToRepair

    MinUnitsBuilt = plx_enums.propertyEnum.MinUnitsBuilt

    MinUnitsBuiltinYear = plx_enums.propertyEnum.MinUnitsBuiltinYear

    MinUnitsRetired = plx_enums.propertyEnum.MinUnitsRetired

    MinUnitsRetiredinYear = plx_enums.propertyEnum.MinUnitsRetiredinYear

    MinUpTime = plx_enums.propertyEnum.MinUpTime

    MinValue = plx_enums.propertyEnum.MinValue

    MinValueStdDev = plx_enums.propertyEnum.MinValueStdDev

    MinVolume = plx_enums.propertyEnum.MinVolume

    MLFCoefficient = plx_enums.propertyEnum.MLFCoefficient

    MustReport = plx_enums.propertyEnum.MustReport

    MustrunSyncCondUnits = plx_enums.propertyEnum.MustrunSyncCondUnits

    MustRunUnits = plx_enums.propertyEnum.MustRunUnits

    NaturalInflow = plx_enums.propertyEnum.NaturalInflow

    OfferBase = plx_enums.propertyEnum.OfferBase

    OfferNoLoadCost = plx_enums.propertyEnum.OfferNoLoadCost

    OfferPrice = plx_enums.propertyEnum.OfferPrice

    OfferPriceBack = plx_enums.propertyEnum.OfferPriceBack

    OfferQuantity = plx_enums.propertyEnum.OfferQuantity

    OfferQuantityBack = plx_enums.propertyEnum.OfferQuantityBack

    OfferQuantityFormat = plx_enums.propertyEnum.OfferQuantityFormat

    OffersMustClearinOrder = plx_enums.propertyEnum.OffersMustClearinOrder

    OfftakeatStart = plx_enums.propertyEnum.OfftakeatStart

    OfftakeCoefficient = plx_enums.propertyEnum.OfftakeCoefficient

    OutageMaxRating = plx_enums.propertyEnum.OutageMaxRating

    OutageMinRating = plx_enums.propertyEnum.OutageMinRating

    OutageRating = plx_enums.propertyEnum.OutageRating

    OutputScalar = plx_enums.propertyEnum.OutputScalar

    OverloadMaxRating = plx_enums.propertyEnum.OverloadMaxRating

    OverloadMinRating = plx_enums.propertyEnum.OverloadMinRating

    PeakLoadCoefficient = plx_enums.propertyEnum.PeakLoadCoefficient

    PeakPeriod = plx_enums.propertyEnum.PeakPeriod

    PeakPeriodCoefficient = plx_enums.propertyEnum.PeakPeriodCoefficient

    Penalty = plx_enums.propertyEnum.Penalty

    PenaltyCost = plx_enums.propertyEnum.PenaltyCost

    PenaltyPrice = plx_enums.propertyEnum.PenaltyPrice

    PenaltyQuantity = plx_enums.propertyEnum.PenaltyQuantity

    PoolType = plx_enums.propertyEnum.PoolType

    PowertoHeatRatio = plx_enums.propertyEnum.PowertoHeatRatio

    Price = plx_enums.propertyEnum.Price

    PriceCap = plx_enums.propertyEnum.PriceCap

    PriceFloor = plx_enums.propertyEnum.PriceFloor

    PriceofDumpEnergy = plx_enums.propertyEnum.PriceofDumpEnergy

    PriceSetting = plx_enums.propertyEnum.PriceSetting

    PricingMethod = plx_enums.propertyEnum.PricingMethod

    Probability = plx_enums.propertyEnum.Probability

    ProductionatStart = plx_enums.propertyEnum.ProductionatStart

    ProductionCoefficient = plx_enums.propertyEnum.ProductionCoefficient

    ProductionRate = plx_enums.propertyEnum.ProductionRate

    Profile = plx_enums.propertyEnum.Profile

    ProfileDay = plx_enums.propertyEnum.ProfileDay

    ProfileMonth = plx_enums.propertyEnum.ProfileMonth

    ProfileWeek = plx_enums.propertyEnum.ProfileWeek

    ProfileYear = plx_enums.propertyEnum.ProfileYear

    ProjectStartDate = plx_enums.propertyEnum.ProjectStartDate

    ProvisionCoefficient = plx_enums.propertyEnum.ProvisionCoefficient

    PumpEfficiency = plx_enums.propertyEnum.PumpEfficiency

    PumpDispatchableLoadCoefficient = plx_enums.propertyEnum.PumpDispatchableLoadCoefficient

    PumpLoad = plx_enums.propertyEnum.PumpLoad

    PumpLoadCoefficient = plx_enums.propertyEnum.PumpLoadCoefficient

    PumpOfferPrice = plx_enums.propertyEnum.PumpOfferPrice

    PumpUnits = plx_enums.propertyEnum.PumpUnits

    PurchasesCoefficient = plx_enums.propertyEnum.PurchasesCoefficient

    Quantity = plx_enums.propertyEnum.Quantity

    QuantityDay = plx_enums.propertyEnum.QuantityDay

    QuantityMonth = plx_enums.propertyEnum.QuantityMonth

    QuantityWeek = plx_enums.propertyEnum.QuantityWeek

    QuantityYear = plx_enums.propertyEnum.QuantityYear

    MaxRampDownPenalty = plx_enums.propertyEnum.MaxRampDownPenalty

    RampPenalty = plx_enums.propertyEnum.RampPenalty

    MaxRampUpPenalty = plx_enums.propertyEnum.MaxRampUpPenalty

    RandomNumberSeed = plx_enums.propertyEnum.RandomNumberSeed

    RatedCapacityCoefficient = plx_enums.propertyEnum.RatedCapacityCoefficient

    Rating = plx_enums.propertyEnum.Rating

    Ratio = plx_enums.propertyEnum.Ratio

    Reactance = plx_enums.propertyEnum.Reactance

    ReferenceGeneration = plx_enums.propertyEnum.ReferenceGeneration

    ReferenceLoad = plx_enums.propertyEnum.ReferenceLoad

    RegulationPoint = plx_enums.propertyEnum.RegulationPoint

    RegulationRange = plx_enums.propertyEnum.RegulationRange

    RemovalRate = plx_enums.propertyEnum.RemovalRate

    RentalBackShare = plx_enums.propertyEnum.RentalBackShare

    RentalShare = plx_enums.propertyEnum.RentalShare

    ReserveProvisionCoefficient = plx_enums.propertyEnum.ReserveProvisionCoefficient

    ReserveShare = plx_enums.propertyEnum.ReserveShare

    ReservesVOMCharge = plx_enums.propertyEnum.ReservesVOMCharge

    Resistance = plx_enums.propertyEnum.Resistance

    ResponseRatio = plx_enums.propertyEnum.ResponseRatio

    RetirementCost = plx_enums.propertyEnum.RetirementCost

    RHS = plx_enums.propertyEnum.RHS

    RHSCoefficient = plx_enums.propertyEnum.RHSCoefficient

    RHSDay = plx_enums.propertyEnum.RHSDay

    RHSMonth = plx_enums.propertyEnum.RHSMonth

    RHSWeek = plx_enums.propertyEnum.RHSWeek

    RHSYear = plx_enums.propertyEnum.RHSYear

    RiskAdjustmentFactor = plx_enums.propertyEnum.RiskAdjustmentFactor

    RoughRunningPoint = plx_enums.propertyEnum.RoughRunningPoint

    RoughRunningRange = plx_enums.propertyEnum.RoughRunningRange

    RoundingUpThreshold = plx_enums.propertyEnum.RoundingUpThreshold

    RSI = plx_enums.propertyEnum.RSI

    RSICoefficient = plx_enums.propertyEnum.RSICoefficient

    RSIInverseCoefficient = plx_enums.propertyEnum.RSIInverseCoefficient

    RSIsquaredCoefficient = plx_enums.propertyEnum.RSIsquaredCoefficient

    SalesCoefficient = plx_enums.propertyEnum.SalesCoefficient

    SamplingMethod = plx_enums.propertyEnum.SamplingMethod

    SellBlock = plx_enums.propertyEnum.SellBlock

    SellBlockDay = plx_enums.propertyEnum.SellBlockDay

    SellBlockMonth = plx_enums.propertyEnum.SellBlockMonth

    SellBlockWeek = plx_enums.propertyEnum.SellBlockWeek

    SellBlockYear = plx_enums.propertyEnum.SellBlockYear

    SellUnit = plx_enums.propertyEnum.SellUnit

    Sense = plx_enums.propertyEnum.Sense

    ShadowPrice = plx_enums.propertyEnum.ShadowPrice

    Share = plx_enums.propertyEnum.Share

    ShutdownCost = plx_enums.propertyEnum.ShutdownCost

    SpinningReserveCoefficient = plx_enums.propertyEnum.SpinningReserveCoefficient

    StartCost = plx_enums.propertyEnum.StartCost

    StartCostTime = plx_enums.propertyEnum.StartCostTime

    Strategic = plx_enums.propertyEnum.Strategic

    SummerPeriodCoefficient = plx_enums.propertyEnum.SummerPeriodCoefficient

    Susceptance = plx_enums.propertyEnum.Susceptance

    SyncCondLoad = plx_enums.propertyEnum.SyncCondLoad

    SyncCondOfferPrice = plx_enums.propertyEnum.SyncCondOfferPrice

    SyncCondReserveCoefficient = plx_enums.propertyEnum.SyncCondReserveCoefficient

    SyncCondUnits = plx_enums.propertyEnum.SyncCondUnits

    SyncCondVOMCharge = plx_enums.propertyEnum.SyncCondVOMCharge

    TakeorPayPrice = plx_enums.propertyEnum.TakeorPayPrice

    TakeorPayQuantity = plx_enums.propertyEnum.TakeorPayQuantity

    TakeorPayQuantityDay = plx_enums.propertyEnum.TakeorPayQuantityDay

    TakeorPayQuantityMonth = plx_enums.propertyEnum.TakeorPayQuantityMonth

    TakeorPayQuantityWeek = plx_enums.propertyEnum.TakeorPayQuantityWeek

    TakeorPayQuantityYear = plx_enums.propertyEnum.TakeorPayQuantityYear

    Tariff = plx_enums.propertyEnum.Tariff

    Tax = plx_enums.propertyEnum.Tax

    TechnicalLife = plx_enums.propertyEnum.TechnicalLife

    Timeframe = plx_enums.propertyEnum.Timeframe

    TransportCharge = plx_enums.propertyEnum.TransportCharge

    TraversalTime = plx_enums.propertyEnum.TraversalTime

    UniformPricingPumpedStoragePriceSetting = plx_enums.propertyEnum.UniformPricingPumpedStoragePriceSetting

    UniformPricingRelaxAncillaryServices = plx_enums.propertyEnum.UniformPricingRelaxAncillaryServices

    UniformPricingRelaxGeneratorConstraints = plx_enums.propertyEnum.UniformPricingRelaxGeneratorConstraints

    UniformPricingRelaxGenericConstraints = plx_enums.propertyEnum.UniformPricingRelaxGenericConstraints

    UniformPricingRelaxTransmissionLimits = plx_enums.propertyEnum.UniformPricingRelaxTransmissionLimits

    UnitCommitment = plx_enums.propertyEnum.UnitCommitment

    UnitCommitmentOptimality = plx_enums.propertyEnum.UnitCommitmentOptimality

    Units = plx_enums.propertyEnum.Units

    UnitsBuiltCoefficient = plx_enums.propertyEnum.UnitsBuiltCoefficient

    UnitsBuiltinYearCoefficient = plx_enums.propertyEnum.UnitsBuiltinYearCoefficient

    UnitsGeneratingCoefficient = plx_enums.propertyEnum.UnitsGeneratingCoefficient

    UnitsOut = plx_enums.propertyEnum.UnitsOut

    UnitsOutCoefficient = plx_enums.propertyEnum.UnitsOutCoefficient

    UnitsRetiredCoefficient = plx_enums.propertyEnum.UnitsRetiredCoefficient

    UnitsRetiredinYearCoefficient = plx_enums.propertyEnum.UnitsRetiredinYearCoefficient

    UnitsStartedCoefficient = plx_enums.propertyEnum.UnitsStartedCoefficient

    UpliftAlpha = plx_enums.propertyEnum.UpliftAlpha

    UpliftBeta = plx_enums.propertyEnum.UpliftBeta

    UpliftCompatibility = plx_enums.propertyEnum.UpliftCompatibility

    UpliftCostBasis = plx_enums.propertyEnum.UpliftCostBasis

    UpliftDetectActiveMinStableLevelConstraints = plx_enums.propertyEnum.UpliftDetectActiveMinStableLevelConstraints

    UpliftDetectActiveRampConstraints = plx_enums.propertyEnum.UpliftDetectActiveRampConstraints

    UpliftEnabled = plx_enums.propertyEnum.UpliftEnabled

    UpliftIncludeNoLoadCost = plx_enums.propertyEnum.UpliftIncludeNoLoadCost

    UpliftIncludeStartCost = plx_enums.propertyEnum.UpliftIncludeStartCost

    VoLL = plx_enums.propertyEnum.VoLL

    Voltage = plx_enums.propertyEnum.Voltage

    VOMCharge = plx_enums.propertyEnum.VOMCharge

    VoRS = plx_enums.propertyEnum.VoRS

    WACC = plx_enums.propertyEnum.WACC

    WaterValue = plx_enums.propertyEnum.WaterValue

    WaterValuePoint = plx_enums.propertyEnum.WaterValuePoint

    WheelingCharge = plx_enums.propertyEnum.WheelingCharge

    WheelingChargeBack = plx_enums.propertyEnum.WheelingChargeBack

    SpareExportCapacityCoefficient = plx_enums.propertyEnum.SpareExportCapacityCoefficient

    SpareImportCapacityCoefficient = plx_enums.propertyEnum.SpareImportCapacityCoefficient

    EnergyScalar = plx_enums.propertyEnum.EnergyScalar

    CapacityChargeWeek = plx_enums.propertyEnum.CapacityChargeWeek

    CapacityChargeMonth = plx_enums.propertyEnum.CapacityChargeMonth

    CapacityChargeYear = plx_enums.propertyEnum.CapacityChargeYear

    MaxGenerationUnits = plx_enums.propertyEnum.MaxGenerationUnits

    MaxLoadUnits = plx_enums.propertyEnum.MaxLoadUnits

    CapacityPrice = plx_enums.propertyEnum.CapacityPrice

    EfficiencyBase = plx_enums.propertyEnum.EfficiencyBase

    RepairTimeDistribution = plx_enums.propertyEnum.RepairTimeDistribution

    RepairTimeShape = plx_enums.propertyEnum.RepairTimeShape

    RepairTimeScale = plx_enums.propertyEnum.RepairTimeScale

    ShadowPriceScalar = plx_enums.propertyEnum.ShadowPriceScalar

    FlowControl = plx_enums.propertyEnum.FlowControl

    BuildNonanticipativity = plx_enums.propertyEnum.BuildNonanticipativity

    RetireNonanticipativity = plx_enums.propertyEnum.RetireNonanticipativity

    TrajectoryNonanticipativity = plx_enums.propertyEnum.TrajectoryNonanticipativity

    PriceScalar = plx_enums.propertyEnum.PriceScalar

    PriceIncr = plx_enums.propertyEnum.PriceIncr

    ReadOrder = plx_enums.propertyEnum.ReadOrder

    Circuits = plx_enums.propertyEnum.Circuits

    RemovalCost = plx_enums.propertyEnum.RemovalCost

    NetInjectionCoefficient = plx_enums.propertyEnum.NetInjectionCoefficient

    PhaseAngleCoefficient = plx_enums.propertyEnum.PhaseAngleCoefficient

    CompoundIndex = plx_enums.propertyEnum.CompoundIndex

    MustPumpUnits = plx_enums.propertyEnum.MustPumpUnits

    RiskCoefficient = plx_enums.propertyEnum.RiskCoefficient

    AbsErrorStdDev = plx_enums.propertyEnum.AbsErrorStdDev

    Type = plx_enums.propertyEnum.Type

    LoadMeteringPoint = plx_enums.propertyEnum.LoadMeteringPoint

    EnergyLimitDecompositionMethod = plx_enums.propertyEnum.EnergyLimitDecompositionMethod

    StartProfile = plx_enums.propertyEnum.StartProfile

    ShutdownProfile = plx_enums.propertyEnum.ShutdownProfile

    LastStartState = plx_enums.propertyEnum.LastStartState

    MaxOfftake = plx_enums.propertyEnum.MaxOfftake

    MaxOfftakeDay = plx_enums.propertyEnum.MaxOfftakeDay

    MaxOfftakeWeek = plx_enums.propertyEnum.MaxOfftakeWeek

    MaxOfftakeMonth = plx_enums.propertyEnum.MaxOfftakeMonth

    MaxOfftakeYear = plx_enums.propertyEnum.MaxOfftakeYear

    MinOfftake = plx_enums.propertyEnum.MinOfftake

    MinOfftakeDay = plx_enums.propertyEnum.MinOfftakeDay

    MinOfftakeWeek = plx_enums.propertyEnum.MinOfftakeWeek

    MinOfftakeMonth = plx_enums.propertyEnum.MinOfftakeMonth

    MinOfftakeYear = plx_enums.propertyEnum.MinOfftakeYear

    MaxProduction = plx_enums.propertyEnum.MaxProduction

    MaxProductionDay = plx_enums.propertyEnum.MaxProductionDay

    MaxProductionWeek = plx_enums.propertyEnum.MaxProductionWeek

    MaxProductionMonth = plx_enums.propertyEnum.MaxProductionMonth

    MaxProductionYear = plx_enums.propertyEnum.MaxProductionYear

    Target = plx_enums.propertyEnum.Target

    TargetDay = plx_enums.propertyEnum.TargetDay

    TargetWeek = plx_enums.propertyEnum.TargetWeek

    TargetMonth = plx_enums.propertyEnum.TargetMonth

    TargetYear = plx_enums.propertyEnum.TargetYear

    UnitCommitmentNonanticipativity = plx_enums.propertyEnum.UnitCommitmentNonanticipativity

    UnitCommitmentNonanticipativityTime = plx_enums.propertyEnum.UnitCommitmentNonanticipativityTime

    LoadObligationCoefficient = plx_enums.propertyEnum.LoadObligationCoefficient

    MinGenerationUnits = plx_enums.propertyEnum.MinGenerationUnits

    MinLoadUnits = plx_enums.propertyEnum.MinLoadUnits

    RatingFactor = plx_enums.propertyEnum.RatingFactor

    FormulateUpfront = plx_enums.propertyEnum.FormulateUpfront

    RunningCost = plx_enums.propertyEnum.RunningCost

    AllowNegativeMarkups = plx_enums.propertyEnum.AllowNegativeMarkups

    ARIMAalpha = plx_enums.propertyEnum.ARIMAalpha

    ARIMAbeta = plx_enums.propertyEnum.ARIMAbeta

    MutuallyExclusive = plx_enums.propertyEnum.MutuallyExclusive

    RaiseReserveProvisionCoefficient = plx_enums.propertyEnum.RaiseReserveProvisionCoefficient

    LowerReserveProvisionCoefficient = plx_enums.propertyEnum.LowerReserveProvisionCoefficient

    RegulationRaiseReserveProvisionCoefficient = plx_enums.propertyEnum.RegulationRaiseReserveProvisionCoefficient

    RegulationLowerReserveProvisionCoefficient = plx_enums.propertyEnum.RegulationLowerReserveProvisionCoefficient

    ReplacementReserveProvisionCoefficient = plx_enums.propertyEnum.ReplacementReserveProvisionCoefficient

    StaticRisk = plx_enums.propertyEnum.StaticRisk

    Lookupx = plx_enums.propertyEnum.Lookupx

    Lookupy = plx_enums.propertyEnum.Lookupy

    ARIMAd = plx_enums.propertyEnum.ARIMAd

    StrategicRating = plx_enums.propertyEnum.StrategicRating

    LookupUnit = plx_enums.propertyEnum.LookupUnit

    RunUpRate = plx_enums.propertyEnum.RunUpRate

    RunDownRate = plx_enums.propertyEnum.RunDownRate

    InternalVolumeScalar = plx_enums.propertyEnum.InternalVolumeScalar

    OverloadRating = plx_enums.propertyEnum.OverloadRating

    StrategicReferencePrice = plx_enums.propertyEnum.StrategicReferencePrice

    UoSCharge = plx_enums.propertyEnum.UoSCharge

    RHSCustom = plx_enums.propertyEnum.RHSCustom

    Model = plx_enums.propertyEnum.Model

    UpliftDelta = plx_enums.propertyEnum.UpliftDelta

    ShadowPriceIncr = plx_enums.propertyEnum.ShadowPriceIncr

    CompoundIndexDay = plx_enums.propertyEnum.CompoundIndexDay

    CompoundIndexWeek = plx_enums.propertyEnum.CompoundIndexWeek

    CompoundIndexMonth = plx_enums.propertyEnum.CompoundIndexMonth

    CompoundIndexYear = plx_enums.propertyEnum.CompoundIndexYear

    MarkupPoint = plx_enums.propertyEnum.MarkupPoint

    FixedLoadPenalty = plx_enums.propertyEnum.FixedLoadPenalty

    MinLoadPenalty = plx_enums.propertyEnum.MinLoadPenalty

    DecompositionPenaltya = plx_enums.propertyEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.propertyEnum.DecompositionPenaltyb

    MaxRampDay = plx_enums.propertyEnum.MaxRampDay

    MaxRampWeek = plx_enums.propertyEnum.MaxRampWeek

    MaxRampMonth = plx_enums.propertyEnum.MaxRampMonth

    MaxRampYear = plx_enums.propertyEnum.MaxRampYear

    MaxLoadFactor = plx_enums.propertyEnum.MaxLoadFactor

    MaxLoadFactorDay = plx_enums.propertyEnum.MaxLoadFactorDay

    MaxLoadFactorWeek = plx_enums.propertyEnum.MaxLoadFactorWeek

    MaxLoadFactorMonth = plx_enums.propertyEnum.MaxLoadFactorMonth

    MaxLoadFactorYear = plx_enums.propertyEnum.MaxLoadFactorYear

    MinLoadFactor = plx_enums.propertyEnum.MinLoadFactor

    MinLoadFactorDay = plx_enums.propertyEnum.MinLoadFactorDay

    MinLoadFactorWeek = plx_enums.propertyEnum.MinLoadFactorWeek

    MinLoadFactorMonth = plx_enums.propertyEnum.MinLoadFactorMonth

    MinLoadFactorYear = plx_enums.propertyEnum.MinLoadFactorYear

    MinEnergy = plx_enums.propertyEnum.MinEnergy

    MinEnergyDay = plx_enums.propertyEnum.MinEnergyDay

    MinEnergyWeek = plx_enums.propertyEnum.MinEnergyWeek

    MinEnergyMonth = plx_enums.propertyEnum.MinEnergyMonth

    MinEnergyYear = plx_enums.propertyEnum.MinEnergyYear

    FlowNonanticipativity = plx_enums.propertyEnum.FlowNonanticipativity

    FlowNonanticipativityTime = plx_enums.propertyEnum.FlowNonanticipativityTime

    FeasibilityRepairWeight = plx_enums.propertyEnum.FeasibilityRepairWeight

    UnitsLoadCoefficient = plx_enums.propertyEnum.UnitsLoadCoefficient

    GeneratorBuildCostCoefficient = plx_enums.propertyEnum.GeneratorBuildCostCoefficient

    BuildCostCoefficient = plx_enums.propertyEnum.BuildCostCoefficient

    InflowCoefficient = plx_enums.propertyEnum.InflowCoefficient

    ReleaseCoefficient = plx_enums.propertyEnum.ReleaseCoefficient

    SpillCoefficient = plx_enums.propertyEnum.SpillCoefficient

    GeneratorReleaseCoefficient = plx_enums.propertyEnum.GeneratorReleaseCoefficient

    RampCoefficient = plx_enums.propertyEnum.RampCoefficient

    SamplingFrequency = plx_enums.propertyEnum.SamplingFrequency

    NonphysicalInflowPenalty = plx_enums.propertyEnum.NonphysicalInflowPenalty

    NonphysicalSpillPenalty = plx_enums.propertyEnum.NonphysicalSpillPenalty

    TransitionCostDown = plx_enums.propertyEnum.TransitionCostDown

    TransitionCostUp = plx_enums.propertyEnum.TransitionCostUp

    DecouplingTime = plx_enums.propertyEnum.DecouplingTime

    CouplingTime = plx_enums.propertyEnum.CouplingTime

    TransitionCost = plx_enums.propertyEnum.TransitionCost

    MaxUnitsPumping = plx_enums.propertyEnum.MaxUnitsPumping

    GenerationSentOutCoefficient = plx_enums.propertyEnum.GenerationSentOutCoefficient

    UnitsPumpingCoefficient = plx_enums.propertyEnum.UnitsPumpingCoefficient

    MaxFlowPenalty = plx_enums.propertyEnum.MaxFlowPenalty

    StartPenalty = plx_enums.propertyEnum.StartPenalty

    ShutdownPenalty = plx_enums.propertyEnum.ShutdownPenalty

    InitialFlow = plx_enums.propertyEnum.InitialFlow

    UnitsShutdownCoefficient = plx_enums.propertyEnum.UnitsShutdownCoefficient

    ShortageCoefficient = plx_enums.propertyEnum.ShortageCoefficient

    RampUpCharge = plx_enums.propertyEnum.RampUpCharge

    RampDownCharge = plx_enums.propertyEnum.RampDownCharge

    EnforceBounds = plx_enums.propertyEnum.EnforceBounds

    DecompositionPenaltyc = plx_enums.propertyEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.propertyEnum.DecompositionPenaltyx

    TargetPenalty = plx_enums.propertyEnum.TargetPenalty

    MaxEnergyPenalty = plx_enums.propertyEnum.MaxEnergyPenalty

    MinEnergyPenalty = plx_enums.propertyEnum.MinEnergyPenalty

    MLFAdjustsOfferPrice = plx_enums.propertyEnum.MLFAdjustsOfferPrice

    MLFAdjustsBidPrice = plx_enums.propertyEnum.MLFAdjustsBidPrice

    MLFAdjustsNoLoadCost = plx_enums.propertyEnum.MLFAdjustsNoLoadCost

    MLFAdjustsStartCost = plx_enums.propertyEnum.MLFAdjustsStartCost

    FormulateNPLUpfront = plx_enums.propertyEnum.FormulateNPLUpfront

    FlowatStart = plx_enums.propertyEnum.FlowatStart

    Efficiency = plx_enums.propertyEnum.Efficiency

    MaxGeneratorRelease = plx_enums.propertyEnum.MaxGeneratorRelease

    MaxStarts = plx_enums.propertyEnum.MaxStarts

    MaxStartsDay = plx_enums.propertyEnum.MaxStartsDay

    MaxStartsWeek = plx_enums.propertyEnum.MaxStartsWeek

    MaxStartsMonth = plx_enums.propertyEnum.MaxStartsMonth

    MaxStartsYear = plx_enums.propertyEnum.MaxStartsYear

    MaxStartsPenalty = plx_enums.propertyEnum.MaxStartsPenalty

    ExpansionCostCoefficient = plx_enums.propertyEnum.ExpansionCostCoefficient

    PumpUoSCharge = plx_enums.propertyEnum.PumpUoSCharge

    DecompositionBoundPenalty = plx_enums.propertyEnum.DecompositionBoundPenalty

    SpillPenalty = plx_enums.propertyEnum.SpillPenalty

    MaxWithdrawal = plx_enums.propertyEnum.MaxWithdrawal

    WithdrawalCharge = plx_enums.propertyEnum.WithdrawalCharge

    MaxWithdrawalDay = plx_enums.propertyEnum.MaxWithdrawalDay

    MaxWithdrawalWeek = plx_enums.propertyEnum.MaxWithdrawalWeek

    MaxWithdrawalMonth = plx_enums.propertyEnum.MaxWithdrawalMonth

    MaxWithdrawalYear = plx_enums.propertyEnum.MaxWithdrawalYear

    InjectionCharge = plx_enums.propertyEnum.InjectionCharge

    MaxInjection = plx_enums.propertyEnum.MaxInjection

    MaxInjectionDay = plx_enums.propertyEnum.MaxInjectionDay

    MaxInjectionWeek = plx_enums.propertyEnum.MaxInjectionWeek

    MaxInjectionMonth = plx_enums.propertyEnum.MaxInjectionMonth

    MaxInjectionYear = plx_enums.propertyEnum.MaxInjectionYear

    MinWithdrawal = plx_enums.propertyEnum.MinWithdrawal

    MinWithdrawalDay = plx_enums.propertyEnum.MinWithdrawalDay

    MinWithdrawalWeek = plx_enums.propertyEnum.MinWithdrawalWeek

    MinWithdrawalMonth = plx_enums.propertyEnum.MinWithdrawalMonth

    MinWithdrawalYear = plx_enums.propertyEnum.MinWithdrawalYear

    MinInjection = plx_enums.propertyEnum.MinInjection

    MinInjectionDay = plx_enums.propertyEnum.MinInjectionDay

    MinInjectionWeek = plx_enums.propertyEnum.MinInjectionWeek

    MinInjectionMonth = plx_enums.propertyEnum.MinInjectionMonth

    MinInjectionYear = plx_enums.propertyEnum.MinInjectionYear

    FlowCharge = plx_enums.propertyEnum.FlowCharge

    ShortagePrice = plx_enums.propertyEnum.ShortagePrice

    ExcessPrice = plx_enums.propertyEnum.ExcessPrice

    Elasticity = plx_enums.propertyEnum.Elasticity

    ProductionCost = plx_enums.propertyEnum.ProductionCost

    MinProduction = plx_enums.propertyEnum.MinProduction

    MinProductionDay = plx_enums.propertyEnum.MinProductionDay

    MinProductionWeek = plx_enums.propertyEnum.MinProductionWeek

    MinProductionMonth = plx_enums.propertyEnum.MinProductionMonth

    MinProductionYear = plx_enums.propertyEnum.MinProductionYear

    AvailableCapacityCoefficient = plx_enums.propertyEnum.AvailableCapacityCoefficient

    RampDownCoefficient = plx_enums.propertyEnum.RampDownCoefficient

    RampUpCoefficient = plx_enums.propertyEnum.RampUpCoefficient

    RampDownViolationCoefficient = plx_enums.propertyEnum.RampDownViolationCoefficient

    RampUpViolationCoefficient = plx_enums.propertyEnum.RampUpViolationCoefficient

    MinNativeCapacityReserves = plx_enums.propertyEnum.MinNativeCapacityReserves

    MinNativeCapacityReserveMargin = plx_enums.propertyEnum.MinNativeCapacityReserveMargin

    IsPhysical = plx_enums.propertyEnum.IsPhysical

    LoadSubtracter = plx_enums.propertyEnum.LoadSubtracter

    PumpBidBase = plx_enums.propertyEnum.PumpBidBase

    PumpBidPrice = plx_enums.propertyEnum.PumpBidPrice

    PumpBidQuantity = plx_enums.propertyEnum.PumpBidQuantity

    MaxResponseFactor = plx_enums.propertyEnum.MaxResponseFactor

    MaxSyncCondResponseFactor = plx_enums.propertyEnum.MaxSyncCondResponseFactor

    MaxPumpResponseFactor = plx_enums.propertyEnum.MaxPumpResponseFactor

    MaxReplacementFactor = plx_enums.propertyEnum.MaxReplacementFactor

    PumpUnitsStartedCoefficient = plx_enums.propertyEnum.PumpUnitsStartedCoefficient

    FixedFlowPenalty = plx_enums.propertyEnum.FixedFlowPenalty

    FixedPumpLoad = plx_enums.propertyEnum.FixedPumpLoad

    FixedPumpLoadPenalty = plx_enums.propertyEnum.FixedPumpLoadPenalty

    FixedCharge = plx_enums.propertyEnum.FixedCharge

    CommissionDate = plx_enums.propertyEnum.CommissionDate

    EfficiencyPoint = plx_enums.propertyEnum.EfficiencyPoint

    EfficiencyScalar = plx_enums.propertyEnum.EfficiencyScalar

    x = plx_enums.propertyEnum.x

    y = plx_enums.propertyEnum.y

    ValueCoefficient = plx_enums.propertyEnum.ValueCoefficient

    ObjectiveFunctionCoefficient = plx_enums.propertyEnum.ObjectiveFunctionCoefficient

    LOLPTarget = plx_enums.propertyEnum.LOLPTarget

    RecyclePenalty = plx_enums.propertyEnum.RecyclePenalty

    MaxProductionPenalty = plx_enums.propertyEnum.MaxProductionPenalty

    IncludeinUplift = plx_enums.propertyEnum.IncludeinUplift

    OfferPriceScalar = plx_enums.propertyEnum.OfferPriceScalar

    PumpBidPriceScalar = plx_enums.propertyEnum.PumpBidPriceScalar

    OfferQuantityScalar = plx_enums.propertyEnum.OfferQuantityScalar

    PumpBidQuantityScalar = plx_enums.propertyEnum.PumpBidQuantityScalar

    MinStableFactor = plx_enums.propertyEnum.MinStableFactor

    MinSpinningProvision = plx_enums.propertyEnum.MinSpinningProvision

    MinRegulationProvision = plx_enums.propertyEnum.MinRegulationProvision

    Condition = plx_enums.propertyEnum.Condition

    PriceCoefficient = plx_enums.propertyEnum.PriceCoefficient

    InUseCoefficient = plx_enums.propertyEnum.InUseCoefficient

    SharingEnabled = plx_enums.propertyEnum.SharingEnabled

    SharingLossesEnabled = plx_enums.propertyEnum.SharingLossesEnabled

    OfferPriceIncr = plx_enums.propertyEnum.OfferPriceIncr

    PumpBidPriceIncr = plx_enums.propertyEnum.PumpBidPriceIncr

    z = plx_enums.propertyEnum.z

    PumpUnitCommitmentNonanticipativity = plx_enums.propertyEnum.PumpUnitCommitmentNonanticipativity

    PumpUnitCommitmentNonanticipativityTime = plx_enums.propertyEnum.PumpUnitCommitmentNonanticipativityTime

    NaturalInflowIncr = plx_enums.propertyEnum.NaturalInflowIncr

    NaturalInflowScalar = plx_enums.propertyEnum.NaturalInflowScalar

    OutagePumpLoad = plx_enums.propertyEnum.OutagePumpLoad

    OperatingHoursCoefficient = plx_enums.propertyEnum.OperatingHoursCoefficient

    MaxUpTime = plx_enums.propertyEnum.MaxUpTime

    FormulateNonconvex = plx_enums.propertyEnum.FormulateNonconvex

    AbatementCost = plx_enums.propertyEnum.AbatementCost

    MaxAbatement = plx_enums.propertyEnum.MaxAbatement

    ConsumptionBase = plx_enums.propertyEnum.ConsumptionBase

    ConsumptionIncr = plx_enums.propertyEnum.ConsumptionIncr

    AbatementCoefficient = plx_enums.propertyEnum.AbatementCoefficient

    Consumption = plx_enums.propertyEnum.Consumption

    GeneratorsBuiltCoefficient = plx_enums.propertyEnum.GeneratorsBuiltCoefficient

    BuyBlockFixedCharge = plx_enums.propertyEnum.BuyBlockFixedCharge

    SellBlockFixedCharge = plx_enums.propertyEnum.SellBlockFixedCharge

    IncludeinMarginalUnit = plx_enums.propertyEnum.IncludeinMarginalUnit

    DemandParticipationFactor = plx_enums.propertyEnum.DemandParticipationFactor

    BuiltCoefficient = plx_enums.propertyEnum.BuiltCoefficient

    BuiltinYearCoefficient = plx_enums.propertyEnum.BuiltinYearCoefficient

    GeneratorsBuiltinYearCoefficient = plx_enums.propertyEnum.GeneratorsBuiltinYearCoefficient

    MinMaintenance = plx_enums.propertyEnum.MinMaintenance

    BuildSetSize = plx_enums.propertyEnum.BuildSetSize

    LHSType = plx_enums.propertyEnum.LHSType

    MaxMaintenanceFactor = plx_enums.propertyEnum.MaxMaintenanceFactor

    MinMaintenanceFactor = plx_enums.propertyEnum.MinMaintenanceFactor

    WithdrawalCoefficient = plx_enums.propertyEnum.WithdrawalCoefficient

    InjectionCoefficient = plx_enums.propertyEnum.InjectionCoefficient

    ExternalInjection = plx_enums.propertyEnum.ExternalInjection

    FlexibilityUpCoefficient = plx_enums.propertyEnum.FlexibilityUpCoefficient

    FlexibilityDownCoefficient = plx_enums.propertyEnum.FlexibilityDownCoefficient

    RampFlexibilityUpCoefficient = plx_enums.propertyEnum.RampFlexibilityUpCoefficient

    RampFlexibilityDownCoefficient = plx_enums.propertyEnum.RampFlexibilityDownCoefficient

    Duration = plx_enums.propertyEnum.Duration

    Sampling = plx_enums.propertyEnum.Sampling

    HoursDownCoefficient = plx_enums.propertyEnum.HoursDownCoefficient

    UnservedEnergyCoefficient = plx_enums.propertyEnum.UnservedEnergyCoefficient

    DumpEnergyCoefficient = plx_enums.propertyEnum.DumpEnergyCoefficient

    NetLoadCoefficient = plx_enums.propertyEnum.NetLoadCoefficient

    FCFConstant = plx_enums.propertyEnum.FCFConstant

    FCFShadowPrice = plx_enums.propertyEnum.FCFShadowPrice

    SlicingBlock = plx_enums.propertyEnum.SlicingBlock

    TreeStageCount = plx_enums.propertyEnum.TreeStageCount

    TreePositionExpFactor = plx_enums.propertyEnum.TreePositionExpFactor

    TreeLeavesExpFactor = plx_enums.propertyEnum.TreeLeavesExpFactor

    TreeStagesPosition = plx_enums.propertyEnum.TreeStagesPosition

    TreeStagesLeaves = plx_enums.propertyEnum.TreeStagesLeaves

    LowerBound = plx_enums.propertyEnum.LowerBound

    UpperBound = plx_enums.propertyEnum.UpperBound

    SampleWeight = plx_enums.propertyEnum.SampleWeight

    ExpectedValueCoefficient = plx_enums.propertyEnum.ExpectedValueCoefficient

    ErrorCoefficient = plx_enums.propertyEnum.ErrorCoefficient

    PositiveErrorCoefficient = plx_enums.propertyEnum.PositiveErrorCoefficient

    NegativeErrorCoefficient = plx_enums.propertyEnum.NegativeErrorCoefficient

    NetProfitCoefficient = plx_enums.propertyEnum.NetProfitCoefficient

    PoolRevenueCoefficient = plx_enums.propertyEnum.PoolRevenueCoefficient

    NetRevenueCoefficient = plx_enums.propertyEnum.NetRevenueCoefficient

    StartShutdownCostCoefficient = plx_enums.propertyEnum.StartShutdownCostCoefficient

    FixedCostsCoefficient = plx_enums.propertyEnum.FixedCostsCoefficient

    FormulateRisk = plx_enums.propertyEnum.FormulateRisk

    AcceptableRisk = plx_enums.propertyEnum.AcceptableRisk

    OpeningHeat = plx_enums.propertyEnum.OpeningHeat

    MaxHeat = plx_enums.propertyEnum.MaxHeat

    MinHeat = plx_enums.propertyEnum.MinHeat

    HeatLoss = plx_enums.propertyEnum.HeatLoss

    HeatWithdrawalCharge = plx_enums.propertyEnum.HeatWithdrawalCharge

    HeatInjectionCharge = plx_enums.propertyEnum.HeatInjectionCharge

    MaxHeatWithdrawal = plx_enums.propertyEnum.MaxHeatWithdrawal

    MaxHeatWithdrawalDay = plx_enums.propertyEnum.MaxHeatWithdrawalDay

    MaxHeatWithdrawalWeek = plx_enums.propertyEnum.MaxHeatWithdrawalWeek

    MaxHeatWithdrawalMonth = plx_enums.propertyEnum.MaxHeatWithdrawalMonth

    MaxHeatWithdrawalYear = plx_enums.propertyEnum.MaxHeatWithdrawalYear

    MaxHeatInjection = plx_enums.propertyEnum.MaxHeatInjection

    MaxHeatInjectionDay = plx_enums.propertyEnum.MaxHeatInjectionDay

    MaxHeatInjectionWeek = plx_enums.propertyEnum.MaxHeatInjectionWeek

    MaxHeatInjectionMonth = plx_enums.propertyEnum.MaxHeatInjectionMonth

    MaxHeatInjectionYear = plx_enums.propertyEnum.MaxHeatInjectionYear

    MinHeatWithdrawal = plx_enums.propertyEnum.MinHeatWithdrawal

    MinHeatWithdrawalDay = plx_enums.propertyEnum.MinHeatWithdrawalDay

    MinHeatWithdrawalWeek = plx_enums.propertyEnum.MinHeatWithdrawalWeek

    MinHeatWithdrawalMonth = plx_enums.propertyEnum.MinHeatWithdrawalMonth

    MinHeatWithdrawalYear = plx_enums.propertyEnum.MinHeatWithdrawalYear

    MinHeatInjection = plx_enums.propertyEnum.MinHeatInjection

    MinHeatInjectionDay = plx_enums.propertyEnum.MinHeatInjectionDay

    MinHeatInjectionWeek = plx_enums.propertyEnum.MinHeatInjectionWeek

    MinHeatInjectionMonth = plx_enums.propertyEnum.MinHeatInjectionMonth

    MinHeatInjectionYear = plx_enums.propertyEnum.MinHeatInjectionYear

    MaintenanceCoefficient = plx_enums.propertyEnum.MaintenanceCoefficient

    NetInjectionDefinitionCoefficient = plx_enums.propertyEnum.NetInjectionDefinitionCoefficient

    MaxEnergyHour = plx_enums.propertyEnum.MaxEnergyHour

    MinEnergyHour = plx_enums.propertyEnum.MinEnergyHour

    MaxCapacityFactorHour = plx_enums.propertyEnum.MaxCapacityFactorHour

    MinCapacityFactorHour = plx_enums.propertyEnum.MinCapacityFactorHour

    MaxStartsHour = plx_enums.propertyEnum.MaxStartsHour

    MaxHeatWithdrawalHour = plx_enums.propertyEnum.MaxHeatWithdrawalHour

    MaxHeatInjectionHour = plx_enums.propertyEnum.MaxHeatInjectionHour

    MinHeatWithdrawalHour = plx_enums.propertyEnum.MinHeatWithdrawalHour

    MinHeatInjectionHour = plx_enums.propertyEnum.MinHeatInjectionHour

    MaxOfftakeHour = plx_enums.propertyEnum.MaxOfftakeHour

    MinOfftakeHour = plx_enums.propertyEnum.MinOfftakeHour

    QuantityHour = plx_enums.propertyEnum.QuantityHour

    TakeorPayQuantityHour = plx_enums.propertyEnum.TakeorPayQuantityHour

    MaxProductionHour = plx_enums.propertyEnum.MaxProductionHour

    MaxRampHour = plx_enums.propertyEnum.MaxRampHour

    TargetHour = plx_enums.propertyEnum.TargetHour

    CapacityChargeHour = plx_enums.propertyEnum.CapacityChargeHour

    MaxLoadFactorHour = plx_enums.propertyEnum.MaxLoadFactorHour

    MinLoadFactorHour = plx_enums.propertyEnum.MinLoadFactorHour

    SellBlockHour = plx_enums.propertyEnum.SellBlockHour

    BuyBlockHour = plx_enums.propertyEnum.BuyBlockHour

    MinProductionHour = plx_enums.propertyEnum.MinProductionHour

    MaxWithdrawalHour = plx_enums.propertyEnum.MaxWithdrawalHour

    MaxInjectionHour = plx_enums.propertyEnum.MaxInjectionHour

    MinWithdrawalHour = plx_enums.propertyEnum.MinWithdrawalHour

    MinInjectionHour = plx_enums.propertyEnum.MinInjectionHour

    RHSHour = plx_enums.propertyEnum.RHSHour

    CompoundIndexHour = plx_enums.propertyEnum.CompoundIndexHour

    ProfileHour = plx_enums.propertyEnum.ProfileHour

    AllocationHour = plx_enums.propertyEnum.AllocationHour

    LossRate = plx_enums.propertyEnum.LossRate

    MaxFlowHour = plx_enums.propertyEnum.MaxFlowHour

    MaxFlowDay = plx_enums.propertyEnum.MaxFlowDay

    MaxFlowWeek = plx_enums.propertyEnum.MaxFlowWeek

    MaxFlowMonth = plx_enums.propertyEnum.MaxFlowMonth

    MaxFlowYear = plx_enums.propertyEnum.MaxFlowYear

    MaxInventory = plx_enums.propertyEnum.MaxInventory

    MinInventory = plx_enums.propertyEnum.MinInventory

    OpeningInventory = plx_enums.propertyEnum.OpeningInventory

    Delivery = plx_enums.propertyEnum.Delivery

    InventoryCharge = plx_enums.propertyEnum.InventoryCharge

    DeliveryCharge = plx_enums.propertyEnum.DeliveryCharge

    ClosingInventoryCoefficient = plx_enums.propertyEnum.ClosingInventoryCoefficient

    DeliveryCoefficient = plx_enums.propertyEnum.DeliveryCoefficient

    InventoryChangeCoefficient = plx_enums.propertyEnum.InventoryChangeCoefficient

    ReservationCharge = plx_enums.propertyEnum.ReservationCharge

    TreePeriodType = plx_enums.propertyEnum.TreePeriodType

    GenerationNonanticipativity = plx_enums.propertyEnum.GenerationNonanticipativity

    GenerationNonanticipativityTime = plx_enums.propertyEnum.GenerationNonanticipativityTime

    PumpLoadNonanticipativity = plx_enums.propertyEnum.PumpLoadNonanticipativity

    PumpLoadNonanticipativityTime = plx_enums.propertyEnum.PumpLoadNonanticipativityTime

    TrajectoryNonanticipativityTime = plx_enums.propertyEnum.TrajectoryNonanticipativityTime

    StepHourActiveFrom = plx_enums.propertyEnum.StepHourActiveFrom

    StepHoursActive = plx_enums.propertyEnum.StepHoursActive

    StartProfileRange = plx_enums.propertyEnum.StartProfileRange

    SamplingPeriodType = plx_enums.propertyEnum.SamplingPeriodType

    IncludeinCapacityPayments = plx_enums.propertyEnum.IncludeinCapacityPayments

    ValueSquaredCoefficient = plx_enums.propertyEnum.ValueSquaredCoefficient

    SupplySettlementModel = plx_enums.propertyEnum.SupplySettlementModel

    DemandSettlementModel = plx_enums.propertyEnum.DemandSettlementModel

    MonitoringThreshold = plx_enums.propertyEnum.MonitoringThreshold

    MaxFlowBack = plx_enums.propertyEnum.MaxFlowBack

    MaxFlowBackHour = plx_enums.propertyEnum.MaxFlowBackHour

    MaxFlowBackDay = plx_enums.propertyEnum.MaxFlowBackDay

    MaxFlowBackWeek = plx_enums.propertyEnum.MaxFlowBackWeek

    MaxFlowBackMonth = plx_enums.propertyEnum.MaxFlowBackMonth

    MaxFlowBackYear = plx_enums.propertyEnum.MaxFlowBackYear

    FlowChargeBack = plx_enums.propertyEnum.FlowChargeBack

    OutageMaxFlow = plx_enums.propertyEnum.OutageMaxFlow

    OutageMaxFlowBack = plx_enums.propertyEnum.OutageMaxFlowBack

    PumpOperatingHoursCoefficient = plx_enums.propertyEnum.PumpOperatingHoursCoefficient

    SyncCondLoadCoefficient = plx_enums.propertyEnum.SyncCondLoadCoefficient

    UnitsSyncCondCoefficient = plx_enums.propertyEnum.UnitsSyncCondCoefficient

    SyncCondOperatingHoursCoefficient = plx_enums.propertyEnum.SyncCondOperatingHoursCoefficient

    PricingWeight = plx_enums.propertyEnum.PricingWeight

    MinDownTimeMode = plx_enums.propertyEnum.MinDownTimeMode

    SettlementModel = plx_enums.propertyEnum.SettlementModel

    VolumeImbalance = plx_enums.propertyEnum.VolumeImbalance

    ImbalanceCharge = plx_enums.propertyEnum.ImbalanceCharge

    Capacity = plx_enums.propertyEnum.Capacity

    MaxSoC = plx_enums.propertyEnum.MaxSoC

    MinSoC = plx_enums.propertyEnum.MinSoC

    ChargeEfficiency = plx_enums.propertyEnum.ChargeEfficiency

    DischargeEfficiency = plx_enums.propertyEnum.DischargeEfficiency

    InitialSoC = plx_enums.propertyEnum.InitialSoC

    TreeStagesHangingBranches = plx_enums.propertyEnum.TreeStagesHangingBranches

    TransmissionConstraintsEnabled = plx_enums.propertyEnum.TransmissionConstraintsEnabled

    TransmissionConstraintVoltageThreshold = plx_enums.propertyEnum.TransmissionConstraintVoltageThreshold

    TransmissionInterfaceConstraintsEnabled = plx_enums.propertyEnum.TransmissionInterfaceConstraintsEnabled

    EnforceTransmissionLimitsOnLinesInInterfaces = plx_enums.propertyEnum.EnforceTransmissionLimitsOnLinesInInterfaces

    TransmissionReportEnabled = plx_enums.propertyEnum.TransmissionReportEnabled

    TransmissionReportVoltageThreshold = plx_enums.propertyEnum.TransmissionReportVoltageThreshold

    TransmissionReportLinesInInterfaces = plx_enums.propertyEnum.TransmissionReportLinesInInterfaces

    TransmissionReportInjectionandLoadNodes = plx_enums.propertyEnum.TransmissionReportInjectionandLoadNodes

    WildcardMode = plx_enums.propertyEnum.WildcardMode

    Window = plx_enums.propertyEnum.Window

    Crew = plx_enums.propertyEnum.Crew

    Equipment = plx_enums.propertyEnum.Equipment

    HoursActiveCoefficient = plx_enums.propertyEnum.HoursActiveCoefficient

    CostCoefficient = plx_enums.propertyEnum.CostCoefficient

    CrewCoefficient = plx_enums.propertyEnum.CrewCoefficient

    EquipmentCoefficient = plx_enums.propertyEnum.EquipmentCoefficient

    MinOccurrence = plx_enums.propertyEnum.MinOccurrence

    MinOccurrenceHour = plx_enums.propertyEnum.MinOccurrenceHour

    MinOccurrenceDay = plx_enums.propertyEnum.MinOccurrenceDay

    MinOccurrenceWeek = plx_enums.propertyEnum.MinOccurrenceWeek

    MinOccurrenceMonth = plx_enums.propertyEnum.MinOccurrenceMonth

    MinOccurrenceYear = plx_enums.propertyEnum.MinOccurrenceYear

    TargetLevel = plx_enums.propertyEnum.TargetLevel

    TargetLevelHour = plx_enums.propertyEnum.TargetLevelHour

    TargetLevelDay = plx_enums.propertyEnum.TargetLevelDay

    TargetLevelWeek = plx_enums.propertyEnum.TargetLevelWeek

    TargetLevelMonth = plx_enums.propertyEnum.TargetLevelMonth

    TargetLevelYear = plx_enums.propertyEnum.TargetLevelYear

    HoursFullCoefficient = plx_enums.propertyEnum.HoursFullCoefficient

    HoursFlowingCoefficient = plx_enums.propertyEnum.HoursFlowingCoefficient

    Nonanticipativity = plx_enums.propertyEnum.Nonanticipativity

    OutageRatingFactor = plx_enums.propertyEnum.OutageRatingFactor

    OutageFirmCapacity = plx_enums.propertyEnum.OutageFirmCapacity

    OutageFirmCapacityFactor = plx_enums.propertyEnum.OutageFirmCapacityFactor

    FirmCapacityCoefficient = plx_enums.propertyEnum.FirmCapacityCoefficient

    EndLevelCoefficient = plx_enums.propertyEnum.EndLevelCoefficient

    ObjectiveFunctionCoefficientHour = plx_enums.propertyEnum.ObjectiveFunctionCoefficientHour

    ObjectiveFunctionCoefficientDay = plx_enums.propertyEnum.ObjectiveFunctionCoefficientDay

    ObjectiveFunctionCoefficientWeek = plx_enums.propertyEnum.ObjectiveFunctionCoefficientWeek

    ObjectiveFunctionCoefficientMonth = plx_enums.propertyEnum.ObjectiveFunctionCoefficientMonth

    ObjectiveFunctionCoefficientYear = plx_enums.propertyEnum.ObjectiveFunctionCoefficientYear

    ReplacementOfferQuantity = plx_enums.propertyEnum.ReplacementOfferQuantity

    ReplacementOfferPrice = plx_enums.propertyEnum.ReplacementOfferPrice

    RevenueCoefficient = plx_enums.propertyEnum.RevenueCoefficient

    ProcessingRate = plx_enums.propertyEnum.ProcessingRate

    ProcessingCharge = plx_enums.propertyEnum.ProcessingCharge

    MinReplacementProvision = plx_enums.propertyEnum.MinReplacementProvision

    ProductionVolume = plx_enums.propertyEnum.ProductionVolume

    WithdrawalRateScalar = plx_enums.propertyEnum.WithdrawalRateScalar

    WithdrawalVolume = plx_enums.propertyEnum.WithdrawalVolume

    InjectionRateScalar = plx_enums.propertyEnum.InjectionRateScalar

    InjectionVolume = plx_enums.propertyEnum.InjectionVolume

    TrajectoryNonanticipativityVolume = plx_enums.propertyEnum.TrajectoryNonanticipativityVolume

    StartWindow = plx_enums.propertyEnum.StartWindow

    EndWindow = plx_enums.propertyEnum.EndWindow

    LeadTime = plx_enums.propertyEnum.LeadTime

    CapacityPriceCap = plx_enums.propertyEnum.CapacityPriceCap

    CapacityPriceFloor = plx_enums.propertyEnum.CapacityPriceFloor

    MaxPower = plx_enums.propertyEnum.MaxPower

    DispatchPeriod = plx_enums.propertyEnum.DispatchPeriod

    BalancePeriod = plx_enums.propertyEnum.BalancePeriod

    PositiveAngleCoefficient = plx_enums.propertyEnum.PositiveAngleCoefficient

    NegativeAngleCoefficient = plx_enums.propertyEnum.NegativeAngleCoefficient

    AngleCoefficient = plx_enums.propertyEnum.AngleCoefficient

    AnglePoints = plx_enums.propertyEnum.AnglePoints

    FlowLoadingPoints = plx_enums.propertyEnum.FlowLoadingPoints

    JumpFrequency = plx_enums.propertyEnum.JumpFrequency

    JumpMagnitude = plx_enums.propertyEnum.JumpMagnitude

    JumpErrorStdDev = plx_enums.propertyEnum.JumpErrorStdDev

    GARCHalpha = plx_enums.propertyEnum.GARCHalpha

    GARCHbeta = plx_enums.propertyEnum.GARCHbeta

    GARCHomega = plx_enums.propertyEnum.GARCHomega

    LoadFollowingProfile = plx_enums.propertyEnum.LoadFollowingProfile

    LoadFollowingFactor = plx_enums.propertyEnum.LoadFollowingFactor

    PriceFollowing = plx_enums.propertyEnum.PriceFollowing

    WheelingMethod = plx_enums.propertyEnum.WheelingMethod

    MinImpedance = plx_enums.propertyEnum.MinImpedance

    MaxImpedance = plx_enums.propertyEnum.MaxImpedance

    MinVoltage = plx_enums.propertyEnum.MinVoltage

    MaxVoltage = plx_enums.propertyEnum.MaxVoltage

    IncludeinRoundedRelaxationMeritOrder = plx_enums.propertyEnum.IncludeinRoundedRelaxationMeritOrder

    FixedFlowMethod = plx_enums.propertyEnum.FixedFlowMethod

    WaterYield = plx_enums.propertyEnum.WaterYield

    Diameter = plx_enums.propertyEnum.Diameter

    Roughness = plx_enums.propertyEnum.Roughness

    Length = plx_enums.propertyEnum.Length

    WaterSecurity = plx_enums.propertyEnum.WaterSecurity

    StartHourCoefficient = plx_enums.propertyEnum.StartHourCoefficient

    WaterOfftake = plx_enums.propertyEnum.WaterOfftake

    MinPumpTime = plx_enums.propertyEnum.MinPumpTime

    WaterConsumption = plx_enums.propertyEnum.WaterConsumption

    WaterOfftakeCoefficient = plx_enums.propertyEnum.WaterOfftakeCoefficient

    WaterConsumptionCoefficient = plx_enums.propertyEnum.WaterConsumptionCoefficient

    NaturalInflowCoefficient = plx_enums.propertyEnum.NaturalInflowCoefficient

    ReportObjectsinRegion = plx_enums.propertyEnum.ReportObjectsinRegion

    GasSecurity = plx_enums.propertyEnum.GasSecurity

    ConsumptionAllocation = plx_enums.propertyEnum.ConsumptionAllocation

    ForcedOutageRateDenominator = plx_enums.propertyEnum.ForcedOutageRateDenominator

    InitialOperatingHours = plx_enums.propertyEnum.InitialOperatingHours

    RiskLevel = plx_enums.propertyEnum.RiskLevel

    DeterministicStages = plx_enums.propertyEnum.DeterministicStages

    InitialPumping = plx_enums.propertyEnum.InitialPumping

    InitialUnitsPumping = plx_enums.propertyEnum.InitialUnitsPumping

    MinPumpDownTime = plx_enums.propertyEnum.MinPumpDownTime

    PowerDegradation = plx_enums.propertyEnum.PowerDegradation

    EfficiencyDegradation = plx_enums.propertyEnum.EfficiencyDegradation

    MaxCycles = plx_enums.propertyEnum.MaxCycles

    MaxCyclesHour = plx_enums.propertyEnum.MaxCyclesHour

    MaxCyclesDay = plx_enums.propertyEnum.MaxCyclesDay

    MaxCyclesWeek = plx_enums.propertyEnum.MaxCyclesWeek

    MaxCyclesMonth = plx_enums.propertyEnum.MaxCyclesMonth

    MaxCyclesYear = plx_enums.propertyEnum.MaxCyclesYear

    CyclesCoefficient = plx_enums.propertyEnum.CyclesCoefficient

    StartCoefficient = plx_enums.propertyEnum.StartCoefficient

    ParticipationFactor = plx_enums.propertyEnum.ParticipationFactor

    VoyageTime = plx_enums.propertyEnum.VoyageTime

    LoadingTime = plx_enums.propertyEnum.LoadingTime

    DischargeTime = plx_enums.propertyEnum.DischargeTime

    ShippingCharge = plx_enums.propertyEnum.ShippingCharge

    BoiloffRate = plx_enums.propertyEnum.BoiloffRate

    MaxShipments = plx_enums.propertyEnum.MaxShipments

    MaxShipmentsHour = plx_enums.propertyEnum.MaxShipmentsHour

    MaxShipmentsDay = plx_enums.propertyEnum.MaxShipmentsDay

    MaxShipmentsWeek = plx_enums.propertyEnum.MaxShipmentsWeek

    MaxShipmentsMonth = plx_enums.propertyEnum.MaxShipmentsMonth

    MaxShipmentsYear = plx_enums.propertyEnum.MaxShipmentsYear

    AgeCoefficient = plx_enums.propertyEnum.AgeCoefficient

    InitialAge = plx_enums.propertyEnum.InitialAge

    NonanticipativityTime = plx_enums.propertyEnum.NonanticipativityTime

    EnergyCoefficient = plx_enums.propertyEnum.EnergyCoefficient

    EnergyTarget = plx_enums.propertyEnum.EnergyTarget

    EnergyTargetHour = plx_enums.propertyEnum.EnergyTargetHour

    EnergyTargetDay = plx_enums.propertyEnum.EnergyTargetDay

    EnergyTargetWeek = plx_enums.propertyEnum.EnergyTargetWeek

    EnergyTargetMonth = plx_enums.propertyEnum.EnergyTargetMonth

    EnergyTargetYear = plx_enums.propertyEnum.EnergyTargetYear

    EnergyTargetPenalty = plx_enums.propertyEnum.EnergyTargetPenalty

    ShipmentsCoefficient = plx_enums.propertyEnum.ShipmentsCoefficient

    Minimum = plx_enums.propertyEnum.Minimum

    TransitionType = plx_enums.propertyEnum.TransitionType

    HeatInputDefinitionCoefficient = plx_enums.propertyEnum.HeatInputDefinitionCoefficient

    EnergyUsageDefinitionCoefficient = plx_enums.propertyEnum.EnergyUsageDefinitionCoefficient

    WasteHeatCoefficient = plx_enums.propertyEnum.WasteHeatCoefficient

    EnergyUsageCoefficient = plx_enums.propertyEnum.EnergyUsageCoefficient

    OutageFactor = plx_enums.propertyEnum.OutageFactor

    HangingBranchesHistoricalYearStart = plx_enums.propertyEnum.HangingBranchesHistoricalYearStart

    HangingBranchesBlockCount = plx_enums.propertyEnum.HangingBranchesBlockCount

    HeadEffectsMethod = plx_enums.propertyEnum.HeadEffectsMethod

    HeatUsage = plx_enums.propertyEnum.HeatUsage

    AllowDumpHeat = plx_enums.propertyEnum.AllowDumpHeat

    MinStableProduction = plx_enums.propertyEnum.MinStableProduction

    MaxDownTime = plx_enums.propertyEnum.MaxDownTime

    InitialHoursPumping = plx_enums.propertyEnum.InitialHoursPumping

    GeneratortoPumpSwitchTime = plx_enums.propertyEnum.GeneratortoPumpSwitchTime

    PumptoGeneratorSwitchTime = plx_enums.propertyEnum.PumptoGeneratorSwitchTime

    InitialPumpLoadRaiseProvision = plx_enums.propertyEnum.InitialPumpLoadRaiseProvision

    InitialRaiseProvision = plx_enums.propertyEnum.InitialRaiseProvision

    InjectionRatchet = plx_enums.propertyEnum.InjectionRatchet

    WithdrawalRatchet = plx_enums.propertyEnum.WithdrawalRatchet

    HeatFlowCoefficient = plx_enums.propertyEnum.HeatFlowCoefficient

    HeatDemand = plx_enums.propertyEnum.HeatDemand

    LossCoefficient = plx_enums.propertyEnum.LossCoefficient

    HangingBranchesWeight = plx_enums.propertyEnum.HangingBranchesWeight

    MinReleasePenalty = plx_enums.propertyEnum.MinReleasePenalty

    MaxReleasePenalty = plx_enums.propertyEnum.MaxReleasePenalty

    OnetimeCost = plx_enums.propertyEnum.OnetimeCost

    FirmCapacityIncr = plx_enums.propertyEnum.FirmCapacityIncr

    CapacityDegradation = plx_enums.propertyEnum.CapacityDegradation

    OperatingReserveUnitsCoefficient = plx_enums.propertyEnum.OperatingReserveUnitsCoefficient

    ReserveUnitsCoefficient = plx_enums.propertyEnum.ReserveUnitsCoefficient


class property_reportEnum(Enum):
    Activity = plx_enums.property_reportEnum.Activity

    Allocation = plx_enums.property_reportEnum.Allocation

    Angle = plx_enums.property_reportEnum.Angle

    AuxiliaryUse = plx_enums.property_reportEnum.AuxiliaryUse

    AvailableCapacity = plx_enums.property_reportEnum.AvailableCapacity

    AverageHeatRate = plx_enums.property_reportEnum.AverageHeatRate

    BidCleared = plx_enums.property_reportEnum.BidCleared

    BidCostMarkup = plx_enums.property_reportEnum.BidCostMarkup

    BidPrice = plx_enums.property_reportEnum.BidPrice

    BidQuantity = plx_enums.property_reportEnum.BidQuantity

    BoilerHeatProduction = plx_enums.property_reportEnum.BoilerHeatProduction

    BoundedLernerIndex = plx_enums.property_reportEnum.BoundedLernerIndex

    BuildCost = plx_enums.property_reportEnum.BuildCost

    CapPrice = plx_enums.property_reportEnum.CapPrice

    CapacityBuilt = plx_enums.property_reportEnum.CapacityBuilt

    CapacityExcess = plx_enums.property_reportEnum.CapacityExcess

    CapacityFactor = plx_enums.property_reportEnum.CapacityFactor

    CapacityRevenue = plx_enums.property_reportEnum.CapacityRevenue

    CapacityReserveMargin = plx_enums.property_reportEnum.CapacityReserveMargin

    FirmCapacity = plx_enums.property_reportEnum.FirmCapacity

    CapacityRetired = plx_enums.property_reportEnum.CapacityRetired

    CapacityShadowPrice = plx_enums.property_reportEnum.CapacityShadowPrice

    CapacityShortage = plx_enums.property_reportEnum.CapacityShortage

    ClearedOfferCost = plx_enums.property_reportEnum.ClearedOfferCost

    CongestionCharge = plx_enums.property_reportEnum.CongestionCharge

    ConstrainedOffCost = plx_enums.property_reportEnum.ConstrainedOffCost

    ConstrainedOffRevenue = plx_enums.property_reportEnum.ConstrainedOffRevenue

    ConstrainedOnCost = plx_enums.property_reportEnum.ConstrainedOnCost

    ConstrainedOnRevenue = plx_enums.property_reportEnum.ConstrainedOnRevenue

    ContractCost = plx_enums.property_reportEnum.ContractCost

    ContractGeneration = plx_enums.property_reportEnum.ContractGeneration

    ContractGenerationCapacity = plx_enums.property_reportEnum.ContractGenerationCapacity

    ContractLoad = plx_enums.property_reportEnum.ContractLoad

    ContractLoadObligation = plx_enums.property_reportEnum.ContractLoadObligation

    ContractRevenue = plx_enums.property_reportEnum.ContractRevenue

    ContractSettlement = plx_enums.property_reportEnum.ContractSettlement

    ContractShortfall = plx_enums.property_reportEnum.ContractShortfall

    ContractVolume = plx_enums.property_reportEnum.ContractVolume

    Cost = plx_enums.property_reportEnum.Cost

    CostofCurtailment = plx_enums.property_reportEnum.CostofCurtailment

    CostPrice = plx_enums.property_reportEnum.CostPrice

    CosttoLoad = plx_enums.property_reportEnum.CosttoLoad

    CurtailableLoad = plx_enums.property_reportEnum.CurtailableLoad

    CustomerLoad = plx_enums.property_reportEnum.CustomerLoad

    DebtCost = plx_enums.property_reportEnum.DebtCost

    Demand = plx_enums.property_reportEnum.Demand

    DemandCurtailed = plx_enums.property_reportEnum.DemandCurtailed

    DemandIntercept = plx_enums.property_reportEnum.DemandIntercept

    DemandSlope = plx_enums.property_reportEnum.DemandSlope

    DiscreteMaintenance = plx_enums.property_reportEnum.DiscreteMaintenance

    DiscreteMaintenanceBack = plx_enums.property_reportEnum.DiscreteMaintenanceBack

    DispatchableCapacity = plx_enums.property_reportEnum.DispatchableCapacity

    DistributedMaintenance = plx_enums.property_reportEnum.DistributedMaintenance

    DistributedMaintenanceBack = plx_enums.property_reportEnum.DistributedMaintenanceBack

    DownstreamRelease = plx_enums.property_reportEnum.DownstreamRelease

    DSPBidPrice = plx_enums.property_reportEnum.DSPBidPrice

    DSPBidQuantity = plx_enums.property_reportEnum.DSPBidQuantity

    DumpEnergy = plx_enums.property_reportEnum.DumpEnergy

    EDNS = plx_enums.property_reportEnum.EDNS

    EENS = plx_enums.property_reportEnum.EENS

    EmissionsCost = plx_enums.property_reportEnum.EmissionsCost

    EndLevel = plx_enums.property_reportEnum.EndLevel

    EndVolume = plx_enums.property_reportEnum.EndVolume

    Energy = plx_enums.property_reportEnum.Energy

    EnergyCharge = plx_enums.property_reportEnum.EnergyCharge

    EquityCost = plx_enums.property_reportEnum.EquityCost

    Error = plx_enums.property_reportEnum.Error

    ExpansionCost = plx_enums.property_reportEnum.ExpansionCost

    ExportCapacity = plx_enums.property_reportEnum.ExportCapacity

    ExportCapacityBuilt = plx_enums.property_reportEnum.ExportCapacityBuilt

    ExportCapacityRetired = plx_enums.property_reportEnum.ExportCapacityRetired

    Exports = plx_enums.property_reportEnum.Exports

    FixedCost = plx_enums.property_reportEnum.FixedCost

    FixedCosts = plx_enums.property_reportEnum.FixedCosts

    FixedFlow = plx_enums.property_reportEnum.FixedFlow

    FixedGeneration = plx_enums.property_reportEnum.FixedGeneration

    FixedLoad = plx_enums.property_reportEnum.FixedLoad

    FloorPrice = plx_enums.property_reportEnum.FloorPrice

    Flow = plx_enums.property_reportEnum.Flow

    FlowBack = plx_enums.property_reportEnum.FlowBack

    FOMCost = plx_enums.property_reportEnum.FOMCost

    ForcedOutage = plx_enums.property_reportEnum.ForcedOutage

    ForcedOutageRate = plx_enums.property_reportEnum.ForcedOutageRate

    FuelContractCost = plx_enums.property_reportEnum.FuelContractCost

    FuelMarketRevenue = plx_enums.property_reportEnum.FuelMarketRevenue

    FuelOfftake = plx_enums.property_reportEnum.FuelOfftake

    FuelPrice = plx_enums.property_reportEnum.FuelPrice

    Generation = plx_enums.property_reportEnum.Generation

    GenerationatRRN = plx_enums.property_reportEnum.GenerationatRRN

    GenerationCapacity = plx_enums.property_reportEnum.GenerationCapacity

    GenerationCapacityBuilt = plx_enums.property_reportEnum.GenerationCapacityBuilt

    GenerationCapacityRetired = plx_enums.property_reportEnum.GenerationCapacityRetired

    GenerationCost = plx_enums.property_reportEnum.GenerationCost

    GenerationRevenue = plx_enums.property_reportEnum.GenerationRevenue

    GeneratorBuildCost = plx_enums.property_reportEnum.GeneratorBuildCost

    GeneratorFirmCapacity = plx_enums.property_reportEnum.GeneratorFirmCapacity

    TotalFixedCosts = plx_enums.property_reportEnum.TotalFixedCosts

    GeneratorMonopolyRent = plx_enums.property_reportEnum.GeneratorMonopolyRent

    GeneratorNetPoolRevenue = plx_enums.property_reportEnum.GeneratorNetPoolRevenue

    GeneratorNetProfit = plx_enums.property_reportEnum.GeneratorNetProfit

    GeneratorNetRevenue = plx_enums.property_reportEnum.GeneratorNetRevenue

    GeneratorPoolRevenue = plx_enums.property_reportEnum.GeneratorPoolRevenue

    GeneratorPumpCost = plx_enums.property_reportEnum.GeneratorPumpCost

    GeneratorRelease = plx_enums.property_reportEnum.GeneratorRelease

    GeneratorRetirementCost = plx_enums.property_reportEnum.GeneratorRetirementCost

    GeneratorStartShutdownCost = plx_enums.property_reportEnum.GeneratorStartShutdownCost

    HeatFuelOfftake = plx_enums.property_reportEnum.HeatFuelOfftake

    HeatLoad = plx_enums.property_reportEnum.HeatLoad

    HeatMarketRevenue = plx_enums.property_reportEnum.HeatMarketRevenue

    HeatProduction = plx_enums.property_reportEnum.HeatProduction

    HeatProductionCost = plx_enums.property_reportEnum.HeatProductionCost

    HeatRate = plx_enums.property_reportEnum.HeatRate

    HeatRevenue = plx_enums.property_reportEnum.HeatRevenue

    HoursActive = plx_enums.property_reportEnum.HoursActive

    HoursAvailable = plx_enums.property_reportEnum.HoursAvailable

    HoursBinding = plx_enums.property_reportEnum.HoursBinding

    HoursCongested = plx_enums.property_reportEnum.HoursCongested

    HoursCongestedBack = plx_enums.property_reportEnum.HoursCongestedBack

    HoursIncluded = plx_enums.property_reportEnum.HoursIncluded

    OperatingHours = plx_enums.property_reportEnum.OperatingHours

    UnservedEnergyHours = plx_enums.property_reportEnum.UnservedEnergyHours

    ViolationHours = plx_enums.property_reportEnum.ViolationHours

    ViolationBackHours = plx_enums.property_reportEnum.ViolationBackHours

    ImportCapacity = plx_enums.property_reportEnum.ImportCapacity

    ImportCapacityBuilt = plx_enums.property_reportEnum.ImportCapacityBuilt

    ImportCapacityRetired = plx_enums.property_reportEnum.ImportCapacityRetired

    Imports = plx_enums.property_reportEnum.Imports

    Inflow = plx_enums.property_reportEnum.Inflow

    InitialLevel = plx_enums.property_reportEnum.InitialLevel

    InitialVolume = plx_enums.property_reportEnum.InitialVolume

    InstalledCapacity = plx_enums.property_reportEnum.InstalledCapacity

    InterregionalTransmissionLosses = plx_enums.property_reportEnum.InterregionalTransmissionLosses

    InterregionalTransmissionRental = plx_enums.property_reportEnum.InterregionalTransmissionRental

    IntraregionalTransmissionLosses = plx_enums.property_reportEnum.IntraregionalTransmissionLosses

    IntraregionalTransmissionRental = plx_enums.property_reportEnum.IntraregionalTransmissionRental

    LargestSuppliersCapacity = plx_enums.property_reportEnum.LargestSuppliersCapacity

    LernerIndex = plx_enums.property_reportEnum.LernerIndex

    Load = plx_enums.property_reportEnum.Load

    LoadCapacityRatio = plx_enums.property_reportEnum.LoadCapacityRatio

    LoadObligation = plx_enums.property_reportEnum.LoadObligation

    LoadRevenue = plx_enums.property_reportEnum.LoadRevenue

    LoadUnhedged = plx_enums.property_reportEnum.LoadUnhedged

    LoadVariation = plx_enums.property_reportEnum.LoadVariation

    LoadweightedPrice = plx_enums.property_reportEnum.LoadweightedPrice

    LOLE = plx_enums.property_reportEnum.LOLE

    LOLP = plx_enums.property_reportEnum.LOLP

    Loss = plx_enums.property_reportEnum.Loss

    LossBack = plx_enums.property_reportEnum.LossBack

    MarginalLossFactor = plx_enums.property_reportEnum.MarginalLossFactor

    Maintenance = plx_enums.property_reportEnum.Maintenance

    MaintenanceBack = plx_enums.property_reportEnum.MaintenanceBack

    MaintenanceFactor = plx_enums.property_reportEnum.MaintenanceFactor

    MaintenanceRate = plx_enums.property_reportEnum.MaintenanceRate

    MarginalCost = plx_enums.property_reportEnum.MarginalCost

    ShadowPriceReceived = plx_enums.property_reportEnum.ShadowPriceReceived

    MarginalHeatRate = plx_enums.property_reportEnum.MarginalHeatRate

    MarginalLoss = plx_enums.property_reportEnum.MarginalLoss

    MarginalLossCharge = plx_enums.property_reportEnum.MarginalLossCharge

    MarginalValue = plx_enums.property_reportEnum.MarginalValue

    Markup = plx_enums.property_reportEnum.Markup

    MaxAngle = plx_enums.property_reportEnum.MaxAngle

    MaxCapacity = plx_enums.property_reportEnum.MaxCapacity

    MaxCapacityReserveMargin = plx_enums.property_reportEnum.MaxCapacityReserveMargin

    MaxCapacityReserves = plx_enums.property_reportEnum.MaxCapacityReserves

    MaxFlow = plx_enums.property_reportEnum.MaxFlow

    MaxFlowViolation = plx_enums.property_reportEnum.MaxFlowViolation

    MaxGeneration = plx_enums.property_reportEnum.MaxGeneration

    MaxRamp = plx_enums.property_reportEnum.MaxRamp

    MaxValue = plx_enums.property_reportEnum.MaxValue

    MaxVolume = plx_enums.property_reportEnum.MaxVolume

    MinAngle = plx_enums.property_reportEnum.MinAngle

    MinCapacityReserveMargin = plx_enums.property_reportEnum.MinCapacityReserveMargin

    MinCapacityReserves = plx_enums.property_reportEnum.MinCapacityReserves

    MinFlow = plx_enums.property_reportEnum.MinFlow

    MinFlowViolation = plx_enums.property_reportEnum.MinFlowViolation

    MinGeneration = plx_enums.property_reportEnum.MinGeneration

    MinLoad = plx_enums.property_reportEnum.MinLoad

    MinValue = plx_enums.property_reportEnum.MinValue

    MinVolume = plx_enums.property_reportEnum.MinVolume

    MonopolyRent = plx_enums.property_reportEnum.MonopolyRent

    NaturalInflow = plx_enums.property_reportEnum.NaturalInflow

    NetCapacityInterchange = plx_enums.property_reportEnum.NetCapacityInterchange

    NetContractLoad = plx_enums.property_reportEnum.NetContractLoad

    NetContractRevenue = plx_enums.property_reportEnum.NetContractRevenue

    NetContractSettlement = plx_enums.property_reportEnum.NetContractSettlement

    NetContractVolume = plx_enums.property_reportEnum.NetContractVolume

    NetCost = plx_enums.property_reportEnum.NetCost

    NetCostofExports = plx_enums.property_reportEnum.NetCostofExports

    NetCosttoLoad = plx_enums.property_reportEnum.NetCosttoLoad

    NetGeneration = plx_enums.property_reportEnum.NetGeneration

    NetGenerationCost = plx_enums.property_reportEnum.NetGenerationCost

    NetGenerationRevenue = plx_enums.property_reportEnum.NetGenerationRevenue

    NetInjection = plx_enums.property_reportEnum.NetInjection

    NetInterchange = plx_enums.property_reportEnum.NetInterchange

    NetLoad = plx_enums.property_reportEnum.NetLoad

    NetMarketSales = plx_enums.property_reportEnum.NetMarketSales

    NetNewCapacity = plx_enums.property_reportEnum.NetNewCapacity

    NetPoolRevenue = plx_enums.property_reportEnum.NetPoolRevenue

    NetProfit = plx_enums.property_reportEnum.NetProfit

    NetPurchases = plx_enums.property_reportEnum.NetPurchases

    NetReservesRevenue = plx_enums.property_reportEnum.NetReservesRevenue

    NetRevenue = plx_enums.property_reportEnum.NetRevenue

    NetSales = plx_enums.property_reportEnum.NetSales

    NonUtilityAvailableCapacity = plx_enums.property_reportEnum.NonUtilityAvailableCapacity

    NonUtilityContractVolume = plx_enums.property_reportEnum.NonUtilityContractVolume

    NonUtilityGeneration = plx_enums.property_reportEnum.NonUtilityGeneration

    NonUtilityContractSettlement = plx_enums.property_reportEnum.NonUtilityContractSettlement

    NonUtilityMonopolyRent = plx_enums.property_reportEnum.NonUtilityMonopolyRent

    NonUtilityNetRevenue = plx_enums.property_reportEnum.NonUtilityNetRevenue

    OfferBase = plx_enums.property_reportEnum.OfferBase

    OfferCleared = plx_enums.property_reportEnum.OfferCleared

    OfferClearedBack = plx_enums.property_reportEnum.OfferClearedBack

    OfferNoLoadCost = plx_enums.property_reportEnum.OfferNoLoadCost

    OfferPrice = plx_enums.property_reportEnum.OfferPrice

    OfferPriceBack = plx_enums.property_reportEnum.OfferPriceBack

    OfferQuantity = plx_enums.property_reportEnum.OfferQuantity

    OfferQuantityBack = plx_enums.property_reportEnum.OfferQuantityBack

    Offtake = plx_enums.property_reportEnum.Offtake

    PeakLoad = plx_enums.property_reportEnum.PeakLoad

    PeakPeriod = plx_enums.property_reportEnum.PeakPeriod

    Penalty = plx_enums.property_reportEnum.Penalty

    PenaltyCost = plx_enums.property_reportEnum.PenaltyCost

    PhaseAngle = plx_enums.property_reportEnum.PhaseAngle

    PlanningPeakLoad = plx_enums.property_reportEnum.PlanningPeakLoad

    PoolRevenue = plx_enums.property_reportEnum.PoolRevenue

    Price = plx_enums.property_reportEnum.Price

    PriceCostMarkup = plx_enums.property_reportEnum.PriceCostMarkup

    PricePaid = plx_enums.property_reportEnum.PricePaid

    PriceReceived = plx_enums.property_reportEnum.PriceReceived

    Production = plx_enums.property_reportEnum.Production

    Provision = plx_enums.property_reportEnum.Provision

    PumpCost = plx_enums.property_reportEnum.PumpCost

    PumpLoad = plx_enums.property_reportEnum.PumpLoad

    PurchaserLoad = plx_enums.property_reportEnum.PurchaserLoad

    Purchases = plx_enums.property_reportEnum.Purchases

    Quantity = plx_enums.property_reportEnum.Quantity

    Ramp = plx_enums.property_reportEnum.Ramp

    RampPrice = plx_enums.property_reportEnum.RampPrice

    RampViolation = plx_enums.property_reportEnum.RampViolation

    RatedCapacity = plx_enums.property_reportEnum.RatedCapacity

    Rating = plx_enums.property_reportEnum.Rating

    Release = plx_enums.property_reportEnum.Release

    Rental = plx_enums.property_reportEnum.Rental

    RentalBack = plx_enums.property_reportEnum.RentalBack

    ReservesCost = plx_enums.property_reportEnum.ReservesCost

    ReservesRevenue = plx_enums.property_reportEnum.ReservesRevenue

    RetirementCost = plx_enums.property_reportEnum.RetirementCost

    Revenue = plx_enums.property_reportEnum.Revenue

    RHS = plx_enums.property_reportEnum.RHS

    Risk = plx_enums.property_reportEnum.Risk

    RSI = plx_enums.property_reportEnum.RSI

    Sales = plx_enums.property_reportEnum.Sales

    ScheduledGeneration = plx_enums.property_reportEnum.ScheduledGeneration

    ScheduledGenerationCost = plx_enums.property_reportEnum.ScheduledGenerationCost

    ScheduledOfferCost = plx_enums.property_reportEnum.ScheduledOfferCost

    ScheduledRevenue = plx_enums.property_reportEnum.ScheduledRevenue

    ScheduledStartShutdownCost = plx_enums.property_reportEnum.ScheduledStartShutdownCost

    ServiceFactor = plx_enums.property_reportEnum.ServiceFactor

    Settlement = plx_enums.property_reportEnum.Settlement

    SettlementPrice = plx_enums.property_reportEnum.SettlementPrice

    SettlementQuantity = plx_enums.property_reportEnum.SettlementQuantity

    SettlementSurplus = plx_enums.property_reportEnum.SettlementSurplus

    ShadowPrice = plx_enums.property_reportEnum.ShadowPrice

    ShadowPriceBack = plx_enums.property_reportEnum.ShadowPriceBack

    Shortage = plx_enums.property_reportEnum.Shortage

    Slack = plx_enums.property_reportEnum.Slack

    Spill = plx_enums.property_reportEnum.Spill

    SRMC = plx_enums.property_reportEnum.SRMC

    StartShutdownCost = plx_enums.property_reportEnum.StartShutdownCost

    StartFuelOfftake = plx_enums.property_reportEnum.StartFuelOfftake

    StrategicShadowPrice = plx_enums.property_reportEnum.StrategicShadowPrice

    SummerPeriod = plx_enums.property_reportEnum.SummerPeriod

    SupplyCapacity = plx_enums.property_reportEnum.SupplyCapacity

    SyncCondLoad = plx_enums.property_reportEnum.SyncCondLoad

    TakeorPayPrice = plx_enums.property_reportEnum.TakeorPayPrice

    TakeorPayShadowPrice = plx_enums.property_reportEnum.TakeorPayShadowPrice

    Tax = plx_enums.property_reportEnum.Tax

    TimeweightedPrice = plx_enums.property_reportEnum.TimeweightedPrice

    TotalImportCapacity = plx_enums.property_reportEnum.TotalImportCapacity

    TotalInternalCapacity = plx_enums.property_reportEnum.TotalInternalCapacity

    TotalPrice = plx_enums.property_reportEnum.TotalPrice

    TotalSupplyCapacity = plx_enums.property_reportEnum.TotalSupplyCapacity

    TransmissionBuildCost = plx_enums.property_reportEnum.TransmissionBuildCost

    TransmissionControlRental = plx_enums.property_reportEnum.TransmissionControlRental

    TransmissionLosses = plx_enums.property_reportEnum.TransmissionLosses

    TransmissionRental = plx_enums.property_reportEnum.TransmissionRental

    TransmissionRetirementCost = plx_enums.property_reportEnum.TransmissionRetirementCost

    TransportCharge = plx_enums.property_reportEnum.TransportCharge

    UndispatchedCapacity = plx_enums.property_reportEnum.UndispatchedCapacity

    Units = plx_enums.property_reportEnum.Units

    UnitsBuilt = plx_enums.property_reportEnum.UnitsBuilt

    UnitsGenerating = plx_enums.property_reportEnum.UnitsGenerating

    UnitsOut = plx_enums.property_reportEnum.UnitsOut

    UnitsRetired = plx_enums.property_reportEnum.UnitsRetired

    UnitsStarted = plx_enums.property_reportEnum.UnitsStarted

    UnservedEnergy = plx_enums.property_reportEnum.UnservedEnergy

    Uplift = plx_enums.property_reportEnum.Uplift

    UtilityAvailableCapacity = plx_enums.property_reportEnum.UtilityAvailableCapacity

    UtilityContractSettlement = plx_enums.property_reportEnum.UtilityContractSettlement

    UtilityGeneration = plx_enums.property_reportEnum.UtilityGeneration

    UtilityMonopolyRent = plx_enums.property_reportEnum.UtilityMonopolyRent

    UtilityNetRevenue = plx_enums.property_reportEnum.UtilityNetRevenue

    Value = plx_enums.property_reportEnum.Value

    Violation = plx_enums.property_reportEnum.Violation

    ViolationBack = plx_enums.property_reportEnum.ViolationBack

    ViolationCost = plx_enums.property_reportEnum.ViolationCost

    ViolationCostBack = plx_enums.property_reportEnum.ViolationCostBack

    Voltage = plx_enums.property_reportEnum.Voltage

    VOMCharge = plx_enums.property_reportEnum.VOMCharge

    VOMCost = plx_enums.property_reportEnum.VOMCost

    WaterPumped = plx_enums.property_reportEnum.WaterPumped

    WaterRelease = plx_enums.property_reportEnum.WaterRelease

    WheelingCost = plx_enums.property_reportEnum.WheelingCost

    WheelingCostBack = plx_enums.property_reportEnum.WheelingCostBack

    RampCost = plx_enums.property_reportEnum.RampCost

    LoadFactor = plx_enums.property_reportEnum.LoadFactor

    MinLoadGeneration = plx_enums.property_reportEnum.MinLoadGeneration

    CapacityPrice = plx_enums.property_reportEnum.CapacityPrice

    FuelCost = plx_enums.property_reportEnum.FuelCost

    CapacityPayments = plx_enums.property_reportEnum.CapacityPayments

    OfftakeRatio = plx_enums.property_reportEnum.OfftakeRatio

    ClearedOfferPrice = plx_enums.property_reportEnum.ClearedOfferPrice

    GeneratorFOMCost = plx_enums.property_reportEnum.GeneratorFOMCost

    TaxCost = plx_enums.property_reportEnum.TaxCost

    TotalCost = plx_enums.property_reportEnum.TotalCost

    RemovalCost = plx_enums.property_reportEnum.RemovalCost

    IncrementalCost = plx_enums.property_reportEnum.IncrementalCost

    RaiseReserve = plx_enums.property_reportEnum.RaiseReserve

    LowerReserve = plx_enums.property_reportEnum.LowerReserve

    RegulationRaiseReserve = plx_enums.property_reportEnum.RegulationRaiseReserve

    RegulationLowerReserve = plx_enums.property_reportEnum.RegulationLowerReserve

    ReplacementReserve = plx_enums.property_reportEnum.ReplacementReserve

    Losses = plx_enums.property_reportEnum.Losses

    NetDCExport = plx_enums.property_reportEnum.NetDCExport

    HoursUp = plx_enums.property_reportEnum.HoursUp

    HoursDown = plx_enums.property_reportEnum.HoursDown

    MaxOfftake = plx_enums.property_reportEnum.MaxOfftake

    MinOfftake = plx_enums.property_reportEnum.MinOfftake

    WasteHeat = plx_enums.property_reportEnum.WasteHeat

    ReservesVOMCost = plx_enums.property_reportEnum.ReservesVOMCost

    StartFuelCost = plx_enums.property_reportEnum.StartFuelCost

    RunningCost = plx_enums.property_reportEnum.RunningCost

    AverageCost = plx_enums.property_reportEnum.AverageCost

    AvailableResponse = plx_enums.property_reportEnum.AvailableResponse

    TransportCost = plx_enums.property_reportEnum.TransportCost

    FuelTransportCost = plx_enums.property_reportEnum.FuelTransportCost

    FirmGenerationCapacity = plx_enums.property_reportEnum.FirmGenerationCapacity

    CapacityReserves = plx_enums.property_reportEnum.CapacityReserves

    TotalGenerationCost = plx_enums.property_reportEnum.TotalGenerationCost

    UnitsShutdown = plx_enums.property_reportEnum.UnitsShutdown

    LRMC = plx_enums.property_reportEnum.LRMC

    WheelingRevenue = plx_enums.property_reportEnum.WheelingRevenue

    UoSCost = plx_enums.property_reportEnum.UoSCost

    RampUpViolationHours = plx_enums.property_reportEnum.RampUpViolationHours

    RampDownViolationHours = plx_enums.property_reportEnum.RampDownViolationHours

    FixedLoadViolationCost = plx_enums.property_reportEnum.FixedLoadViolationCost

    RampUpViolationCost = plx_enums.property_reportEnum.RampUpViolationCost

    RampDownViolationCost = plx_enums.property_reportEnum.RampDownViolationCost

    FixedLoadViolationHours = plx_enums.property_reportEnum.FixedLoadViolationHours

    MinLoadViolationHours = plx_enums.property_reportEnum.MinLoadViolationHours

    MinLoadViolationCost = plx_enums.property_reportEnum.MinLoadViolationCost

    CHPGeneration = plx_enums.property_reportEnum.CHPGeneration

    CondenseModeGeneration = plx_enums.property_reportEnum.CondenseModeGeneration

    CHPHeatProduction = plx_enums.property_reportEnum.CHPHeatProduction

    CHPPowerFuelOfftake = plx_enums.property_reportEnum.CHPPowerFuelOfftake

    CHPHeatFuelOfftake = plx_enums.property_reportEnum.CHPHeatFuelOfftake

    CHPHeatSurrogateFuelOfftake = plx_enums.property_reportEnum.CHPHeatSurrogateFuelOfftake

    BoilerFuelOfftake = plx_enums.property_reportEnum.BoilerFuelOfftake

    HoursCurtailed = plx_enums.property_reportEnum.HoursCurtailed

    CurtailmentFactor = plx_enums.property_reportEnum.CurtailmentFactor

    SparkSpread = plx_enums.property_reportEnum.SparkSpread

    CleanSparkSpread = plx_enums.property_reportEnum.CleanSparkSpread

    RampViolationHours = plx_enums.property_reportEnum.RampViolationHours

    RampViolationCost = plx_enums.property_reportEnum.RampViolationCost

    NonphysicalInflow = plx_enums.property_reportEnum.NonphysicalInflow

    NonphysicalSpill = plx_enums.property_reportEnum.NonphysicalSpill

    MaxFlowViolationHours = plx_enums.property_reportEnum.MaxFlowViolationHours

    MinFlowViolationHours = plx_enums.property_reportEnum.MinFlowViolationHours

    MaxFlowViolationCost = plx_enums.property_reportEnum.MaxFlowViolationCost

    MinFlowViolationCost = plx_enums.property_reportEnum.MinFlowViolationCost

    ShortageHours = plx_enums.property_reportEnum.ShortageHours

    ShortageCost = plx_enums.property_reportEnum.ShortageCost

    Shortfall = plx_enums.property_reportEnum.Shortfall

    CostofUnservedEnergy = plx_enums.property_reportEnum.CostofUnservedEnergy

    DumpEnergyHours = plx_enums.property_reportEnum.DumpEnergyHours

    CostofDumpEnergy = plx_enums.property_reportEnum.CostofDumpEnergy

    RawValue = plx_enums.property_reportEnum.RawValue

    FuelTransitionCost = plx_enums.property_reportEnum.FuelTransitionCost

    TransitionCost = plx_enums.property_reportEnum.TransitionCost

    TotalGeneratorRevenue = plx_enums.property_reportEnum.TotalGeneratorRevenue

    ShadowCosttoLoad = plx_enums.property_reportEnum.ShadowCosttoLoad

    ShadowLoad = plx_enums.property_reportEnum.ShadowLoad

    ShadowGeneration = plx_enums.property_reportEnum.ShadowGeneration

    ShadowPoolRevenue = plx_enums.property_reportEnum.ShadowPoolRevenue

    RampUpPrice = plx_enums.property_reportEnum.RampUpPrice

    RampDownPrice = plx_enums.property_reportEnum.RampDownPrice

    RampUpViolation = plx_enums.property_reportEnum.RampUpViolation

    RampDownViolation = plx_enums.property_reportEnum.RampDownViolation

    NoCostCapacity = plx_enums.property_reportEnum.NoCostCapacity

    CapacityCurtailed = plx_enums.property_reportEnum.CapacityCurtailed

    NoCostGenerationCapacity = plx_enums.property_reportEnum.NoCostGenerationCapacity

    HoursGenerationCurtailed = plx_enums.property_reportEnum.HoursGenerationCurtailed

    GenerationCapacityCurtailed = plx_enums.property_reportEnum.GenerationCapacityCurtailed

    FixedLoadViolation = plx_enums.property_reportEnum.FixedLoadViolation

    MinLoadViolation = plx_enums.property_reportEnum.MinLoadViolation

    RampUpCost = plx_enums.property_reportEnum.RampUpCost

    RampDownCost = plx_enums.property_reportEnum.RampDownCost

    StartShutdownPenaltyCost = plx_enums.property_reportEnum.StartShutdownPenaltyCost

    AvailableTransferCapability = plx_enums.property_reportEnum.AvailableTransferCapability

    TargetViolation = plx_enums.property_reportEnum.TargetViolation

    TargetViolationCost = plx_enums.property_reportEnum.TargetViolationCost

    MaxEnergyViolation = plx_enums.property_reportEnum.MaxEnergyViolation

    MaxEnergyViolationCost = plx_enums.property_reportEnum.MaxEnergyViolationCost

    MinEnergyViolation = plx_enums.property_reportEnum.MinEnergyViolation

    MinEnergyViolationCost = plx_enums.property_reportEnum.MinEnergyViolationCost

    Efficiency = plx_enums.property_reportEnum.Efficiency

    MaxStartsViolation = plx_enums.property_reportEnum.MaxStartsViolation

    MaxStartsViolationCost = plx_enums.property_reportEnum.MaxStartsViolationCost

    CapacityShortageCost = plx_enums.property_reportEnum.CapacityShortageCost

    CapacityExcessCost = plx_enums.property_reportEnum.CapacityExcessCost

    UnitsPumping = plx_enums.property_reportEnum.UnitsPumping

    ExportCost = plx_enums.property_reportEnum.ExportCost

    ImportCost = plx_enums.property_reportEnum.ImportCost

    ExportRevenue = plx_enums.property_reportEnum.ExportRevenue

    ImportRevenue = plx_enums.property_reportEnum.ImportRevenue

    Loading = plx_enums.property_reportEnum.Loading

    LoadingBack = plx_enums.property_reportEnum.LoadingBack

    ExportLimit = plx_enums.property_reportEnum.ExportLimit

    ImportLimit = plx_enums.property_reportEnum.ImportLimit

    GeneratorAuxiliaryUse = plx_enums.property_reportEnum.GeneratorAuxiliaryUse

    GenerationSentOut = plx_enums.property_reportEnum.GenerationSentOut

    NetDemand = plx_enums.property_reportEnum.NetDemand

    ExcessCost = plx_enums.property_reportEnum.ExcessCost

    Elasticity = plx_enums.property_reportEnum.Elasticity

    ProductionCost = plx_enums.property_reportEnum.ProductionCost

    ForcedOutageHours = plx_enums.property_reportEnum.ForcedOutageHours

    MaintenanceHours = plx_enums.property_reportEnum.MaintenanceHours

    FixedLoadGeneration = plx_enums.property_reportEnum.FixedLoadGeneration

    WithdrawalCost = plx_enums.property_reportEnum.WithdrawalCost

    InjectionCost = plx_enums.property_reportEnum.InjectionCost

    Excess = plx_enums.property_reportEnum.Excess

    ExcessHours = plx_enums.property_reportEnum.ExcessHours

    Intensity = plx_enums.property_reportEnum.Intensity

    PumpBidBase = plx_enums.property_reportEnum.PumpBidBase

    PumpBidPrice = plx_enums.property_reportEnum.PumpBidPrice

    PumpBidQuantity = plx_enums.property_reportEnum.PumpBidQuantity

    PumpBidCleared = plx_enums.property_reportEnum.PumpBidCleared

    ClearedPumpBidPrice = plx_enums.property_reportEnum.ClearedPumpBidPrice

    PumpPricePaid = plx_enums.property_reportEnum.PumpPricePaid

    ClearedPumpBidCost = plx_enums.property_reportEnum.ClearedPumpBidCost

    SpinningReserveProvision = plx_enums.property_reportEnum.SpinningReserveProvision

    SyncCondReserveProvision = plx_enums.property_reportEnum.SyncCondReserveProvision

    PumpDispatchableLoadProvision = plx_enums.property_reportEnum.PumpDispatchableLoadProvision

    NonspinningReserveProvision = plx_enums.property_reportEnum.NonspinningReserveProvision

    RampDown = plx_enums.property_reportEnum.RampDown

    RampUp = plx_enums.property_reportEnum.RampUp

    MinutesofRampUp = plx_enums.property_reportEnum.MinutesofRampUp

    MinutesofRampDown = plx_enums.property_reportEnum.MinutesofRampDown

    PumpUnitsStarted = plx_enums.property_reportEnum.PumpUnitsStarted

    FixedFlowViolation = plx_enums.property_reportEnum.FixedFlowViolation

    FixedFlowViolationCost = plx_enums.property_reportEnum.FixedFlowViolationCost

    FixedFlowViolationHours = plx_enums.property_reportEnum.FixedFlowViolationHours

    FixedPumpLoad = plx_enums.property_reportEnum.FixedPumpLoad

    FixedPumpLoadViolationHours = plx_enums.property_reportEnum.FixedPumpLoadViolationHours

    FixedPumpLoadViolation = plx_enums.property_reportEnum.FixedPumpLoadViolation

    FixedPumpLoadViolationCost = plx_enums.property_reportEnum.FixedPumpLoadViolationCost

    AvailableTransferCapabilityBack = plx_enums.property_reportEnum.AvailableTransferCapabilityBack

    x = plx_enums.property_reportEnum.x

    y = plx_enums.property_reportEnum.y

    ObjectiveFunctionCoefficient = plx_enums.property_reportEnum.ObjectiveFunctionCoefficient

    MaxProductionViolation = plx_enums.property_reportEnum.MaxProductionViolation

    MaxProductionViolationCost = plx_enums.property_reportEnum.MaxProductionViolationCost

    Age = plx_enums.property_reportEnum.Age

    AverageTotalCost = plx_enums.property_reportEnum.AverageTotalCost

    HoursinUse = plx_enums.property_reportEnum.HoursinUse

    LevelizedCost = plx_enums.property_reportEnum.LevelizedCost

    AnnualizedBuildCost = plx_enums.property_reportEnum.AnnualizedBuildCost

    z = plx_enums.property_reportEnum.z

    Withdrawal = plx_enums.property_reportEnum.Withdrawal

    Injection = plx_enums.property_reportEnum.Injection

    NetWithdrawal = plx_enums.property_reportEnum.NetWithdrawal

    DSPBidCleared = plx_enums.property_reportEnum.DSPBidCleared

    ClearedDSPBidPrice = plx_enums.property_reportEnum.ClearedDSPBidPrice

    ClearedDSPBidCost = plx_enums.property_reportEnum.ClearedDSPBidCost

    GenerationweightedPrice = plx_enums.property_reportEnum.GenerationweightedPrice

    PerfectCompetitionDemand = plx_enums.property_reportEnum.PerfectCompetitionDemand

    PerfectCompetitionPrice = plx_enums.property_reportEnum.PerfectCompetitionPrice

    NetImport = plx_enums.property_reportEnum.NetImport

    PerfectCompetitionNetImport = plx_enums.property_reportEnum.PerfectCompetitionNetImport

    ConsumerSurplus = plx_enums.property_reportEnum.ConsumerSurplus

    ProducerSurplus = plx_enums.property_reportEnum.ProducerSurplus

    PerfectCompetitionConsumerSurplus = plx_enums.property_reportEnum.PerfectCompetitionConsumerSurplus

    PerfectCompetitionProducerSurplus = plx_enums.property_reportEnum.PerfectCompetitionProducerSurplus

    PerfectCompetitionProduction = plx_enums.property_reportEnum.PerfectCompetitionProduction

    PerfectCompetitionProducerRevenue = plx_enums.property_reportEnum.PerfectCompetitionProducerRevenue

    ProducerRevenue = plx_enums.property_reportEnum.ProducerRevenue

    AbatementCost = plx_enums.property_reportEnum.AbatementCost

    Abatement = plx_enums.property_reportEnum.Abatement

    GrossEmissions = plx_enums.property_reportEnum.GrossEmissions

    NetEmissions = plx_enums.property_reportEnum.NetEmissions

    ConsumablesCost = plx_enums.property_reportEnum.ConsumablesCost

    AbatementValue = plx_enums.property_reportEnum.AbatementValue

    AbatementNetCost = plx_enums.property_reportEnum.AbatementNetCost

    Consumption = plx_enums.property_reportEnum.Consumption

    GrossProduction = plx_enums.property_reportEnum.GrossProduction

    TakeorPayViolation = plx_enums.property_reportEnum.TakeorPayViolation

    TakeorPayViolationCost = plx_enums.property_reportEnum.TakeorPayViolationCost

    Removal = plx_enums.property_reportEnum.Removal

    NetMarketProfit = plx_enums.property_reportEnum.NetMarketProfit

    WorkingVolume = plx_enums.property_reportEnum.WorkingVolume

    Utilization = plx_enums.property_reportEnum.Utilization

    WorkingUtilization = plx_enums.property_reportEnum.WorkingUtilization

    AverageUtilization = plx_enums.property_reportEnum.AverageUtilization

    FlexibilityUp = plx_enums.property_reportEnum.FlexibilityUp

    FlexibilityDown = plx_enums.property_reportEnum.FlexibilityDown

    RampFlexibilityUp = plx_enums.property_reportEnum.RampFlexibilityUp

    RampFlexibilityDown = plx_enums.property_reportEnum.RampFlexibilityDown

    AverageWorkingUtilization = plx_enums.property_reportEnum.AverageWorkingUtilization

    Duration = plx_enums.property_reportEnum.Duration

    ExpectedValue = plx_enums.property_reportEnum.ExpectedValue

    LowerBound = plx_enums.property_reportEnum.LowerBound

    UpperBound = plx_enums.property_reportEnum.UpperBound

    ReducedCost = plx_enums.property_reportEnum.ReducedCost

    OpeningHeat = plx_enums.property_reportEnum.OpeningHeat

    MaxHeat = plx_enums.property_reportEnum.MaxHeat

    MinHeat = plx_enums.property_reportEnum.MinHeat

    HeatLoss = plx_enums.property_reportEnum.HeatLoss

    ClosingHeat = plx_enums.property_reportEnum.ClosingHeat

    HeatWithdrawal = plx_enums.property_reportEnum.HeatWithdrawal

    HeatInjection = plx_enums.property_reportEnum.HeatInjection

    NetHeatWithdrawal = plx_enums.property_reportEnum.NetHeatWithdrawal

    HeatWithdrawalCost = plx_enums.property_reportEnum.HeatWithdrawalCost

    HeatInjectionCost = plx_enums.property_reportEnum.HeatInjectionCost

    HeatShadowPrice = plx_enums.property_reportEnum.HeatShadowPrice

    MaxInventory = plx_enums.property_reportEnum.MaxInventory

    MinInventory = plx_enums.property_reportEnum.MinInventory

    OpeningInventory = plx_enums.property_reportEnum.OpeningInventory

    Delivery = plx_enums.property_reportEnum.Delivery

    ClosingInventory = plx_enums.property_reportEnum.ClosingInventory

    DeliveryCost = plx_enums.property_reportEnum.DeliveryCost

    InventoryCost = plx_enums.property_reportEnum.InventoryCost

    ReservationCost = plx_enums.property_reportEnum.ReservationCost

    FuelInventoryCost = plx_enums.property_reportEnum.FuelInventoryCost

    GenerationProduction = plx_enums.property_reportEnum.GenerationProduction

    UnitStartProduction = plx_enums.property_reportEnum.UnitStartProduction

    NaturalRevenue = plx_enums.property_reportEnum.NaturalRevenue

    NaturalCost = plx_enums.property_reportEnum.NaturalCost

    IncrementalProductionRate = plx_enums.property_reportEnum.IncrementalProductionRate

    AvailableCapacityReserves = plx_enums.property_reportEnum.AvailableCapacityReserves

    AvailableCapacityMargin = plx_enums.property_reportEnum.AvailableCapacityMargin

    InflexibleGeneration = plx_enums.property_reportEnum.InflexibleGeneration

    HoursatMinimum = plx_enums.property_reportEnum.HoursatMinimum

    PumpOperatingHours = plx_enums.property_reportEnum.PumpOperatingHours

    UnitsSyncCond = plx_enums.property_reportEnum.UnitsSyncCond

    SyncCondOperatingHours = plx_enums.property_reportEnum.SyncCondOperatingHours

    SyncCondCost = plx_enums.property_reportEnum.SyncCondCost

    SyncCondPricePaid = plx_enums.property_reportEnum.SyncCondPricePaid

    VolumeImbalance = plx_enums.property_reportEnum.VolumeImbalance

    ImbalanceCost = plx_enums.property_reportEnum.ImbalanceCost

    ClearedReserveOfferCost = plx_enums.property_reportEnum.ClearedReserveOfferCost

    ClearedBidValue = plx_enums.property_reportEnum.ClearedBidValue

    PotentialEnergy = plx_enums.property_reportEnum.PotentialEnergy

    SoC = plx_enums.property_reportEnum.SoC

    AvailableSoC = plx_enums.property_reportEnum.AvailableSoC

    HoursCharging = plx_enums.property_reportEnum.HoursCharging

    HoursDischarging = plx_enums.property_reportEnum.HoursDischarging

    HoursIdle = plx_enums.property_reportEnum.HoursIdle

    GasMarketRevenue = plx_enums.property_reportEnum.GasMarketRevenue

    ClearedBidPrice = plx_enums.property_reportEnum.ClearedBidPrice

    Crew = plx_enums.property_reportEnum.Crew

    Equipment = plx_enums.property_reportEnum.Equipment

    Outage = plx_enums.property_reportEnum.Outage

    HoursFull = plx_enums.property_reportEnum.HoursFull

    HoursFlowing = plx_enums.property_reportEnum.HoursFlowing

    StartDate = plx_enums.property_reportEnum.StartDate

    MultiareaLOLP = plx_enums.property_reportEnum.MultiareaLOLP

    MultiareaLOLE = plx_enums.property_reportEnum.MultiareaLOLE

    RawGas = plx_enums.property_reportEnum.RawGas

    Volatility = plx_enums.property_reportEnum.Volatility

    MarginalFuelCost = plx_enums.property_reportEnum.MarginalFuelCost

    Impedance = plx_enums.property_reportEnum.Impedance

    SourcePrice = plx_enums.property_reportEnum.SourcePrice

    SourceEnergyCharge = plx_enums.property_reportEnum.SourceEnergyCharge

    SourceCongestionCharge = plx_enums.property_reportEnum.SourceCongestionCharge

    SourceLossCharge = plx_enums.property_reportEnum.SourceLossCharge

    SinkPrice = plx_enums.property_reportEnum.SinkPrice

    SinkEnergyCharge = plx_enums.property_reportEnum.SinkEnergyCharge

    SinkCongestionCharge = plx_enums.property_reportEnum.SinkCongestionCharge

    SinkLossCharge = plx_enums.property_reportEnum.SinkLossCharge

    PriceDelta = plx_enums.property_reportEnum.PriceDelta

    WaterOfftake = plx_enums.property_reportEnum.WaterOfftake

    WaterConsumption = plx_enums.property_reportEnum.WaterConsumption

    WaterPricePaid = plx_enums.property_reportEnum.WaterPricePaid

    WaterCost = plx_enums.property_reportEnum.WaterCost

    RawWater = plx_enums.property_reportEnum.RawWater

    EnergyConsumption = plx_enums.property_reportEnum.EnergyConsumption

    NetFlow = plx_enums.property_reportEnum.NetFlow

    NativeLoad = plx_enums.property_reportEnum.NativeLoad

    OperatingorForcedOutageHours = plx_enums.property_reportEnum.OperatingorForcedOutageHours

    ShadowCapacityBuilt = plx_enums.property_reportEnum.ShadowCapacityBuilt

    ShadowGenerationCapacityBuilt = plx_enums.property_reportEnum.ShadowGenerationCapacityBuilt

    TotalSystemCost = plx_enums.property_reportEnum.TotalSystemCost

    ParticipationFactor = plx_enums.property_reportEnum.ParticipationFactor

    ContractImports = plx_enums.property_reportEnum.ContractImports

    SpotImports = plx_enums.property_reportEnum.SpotImports

    ShippingCost = plx_enums.property_reportEnum.ShippingCost

    RawRating = plx_enums.property_reportEnum.RawRating

    InflowRate = plx_enums.property_reportEnum.InflowRate

    ReleaseRate = plx_enums.property_reportEnum.ReleaseRate

    NaturalInflowRate = plx_enums.property_reportEnum.NaturalInflowRate

    GeneratorReleaseRate = plx_enums.property_reportEnum.GeneratorReleaseRate

    DownstreamReleaseRate = plx_enums.property_reportEnum.DownstreamReleaseRate

    SpillRate = plx_enums.property_reportEnum.SpillRate

    TransitionCount = plx_enums.property_reportEnum.TransitionCount

    ElectricLoad = plx_enums.property_reportEnum.ElectricLoad

    ElectricalUsage = plx_enums.property_reportEnum.ElectricalUsage

    UnitsProducingHeat = plx_enums.property_reportEnum.UnitsProducingHeat

    MinReleaseViolation = plx_enums.property_reportEnum.MinReleaseViolation

    MinReleaseViolationHours = plx_enums.property_reportEnum.MinReleaseViolationHours

    MinReleaseViolationCost = plx_enums.property_reportEnum.MinReleaseViolationCost

    MaxReleaseViolation = plx_enums.property_reportEnum.MaxReleaseViolation

    MaxReleaseViolationHours = plx_enums.property_reportEnum.MaxReleaseViolationHours

    MaxReleaseViolationCost = plx_enums.property_reportEnum.MaxReleaseViolationCost


class LicenseFeaturesEnum(Enum):
    MASTER = plx_enums.LicenseFeaturesEnum.MASTER

    MOSEKLicensed = plx_enums.LicenseFeaturesEnum.MOSEKLicensed

    PLEXOSSupportforMOSEK = plx_enums.LicenseFeaturesEnum.PLEXOSSupportforMOSEK

    MOSEKMixedInteger = plx_enums.LicenseFeaturesEnum.MOSEKMixedInteger

    PLEXOSInterface = plx_enums.LicenseFeaturesEnum.PLEXOSInterface

    PLEXOSDiagnostics = plx_enums.LicenseFeaturesEnum.PLEXOSDiagnostics

    PLEXOSBaseProduct = plx_enums.LicenseFeaturesEnum.PLEXOSBaseProduct

    PLEXOSModule1 = plx_enums.LicenseFeaturesEnum.PLEXOSModule1

    PLEXOSModule2 = plx_enums.LicenseFeaturesEnum.PLEXOSModule2

    PLEXOSModule3 = plx_enums.LicenseFeaturesEnum.PLEXOSModule3

    PLEXOSModule4 = plx_enums.LicenseFeaturesEnum.PLEXOSModule4

    LTPlan = plx_enums.LicenseFeaturesEnum.LTPlan

    PLEXOSConnect = plx_enums.LicenseFeaturesEnum.PLEXOSConnect

    PLEXOSSupportForGurobi = plx_enums.LicenseFeaturesEnum.PLEXOSSupportForGurobi

    PLEXOSGasModel = plx_enums.LicenseFeaturesEnum.PLEXOSGasModel

    PLEXOSSupportForGLPK = plx_enums.LicenseFeaturesEnum.PLEXOSSupportForGLPK

    PLEXOSModule10 = plx_enums.LicenseFeaturesEnum.PLEXOSModule10

    PLEXOSModule11 = plx_enums.LicenseFeaturesEnum.PLEXOSModule11

    PLEXOSModule12 = plx_enums.LicenseFeaturesEnum.PLEXOSModule12

    PLEXOSVersion5 = plx_enums.LicenseFeaturesEnum.PLEXOSVersion5

    PLEXOSSupportforCPLEX = plx_enums.LicenseFeaturesEnum.PLEXOSSupportforCPLEX

    PLEXOSSupportforXpressMP = plx_enums.LicenseFeaturesEnum.PLEXOSSupportforXpressMP

    MOSEKConic = plx_enums.LicenseFeaturesEnum.MOSEKConic

    PLEXOSVersion6 = plx_enums.LicenseFeaturesEnum.PLEXOSVersion6

    XpressMPBaseProduct = plx_enums.LicenseFeaturesEnum.XpressMPBaseProduct

    XpressMPParallel = plx_enums.LicenseFeaturesEnum.XpressMPParallel

    PLEXOSSupportforSoPlexSCIP = plx_enums.LicenseFeaturesEnum.PLEXOSSupportforSoPlexSCIP

    PLEXOSVersion7 = plx_enums.LicenseFeaturesEnum.PLEXOSVersion7

    PLEXOSIntegratedEnergyModel = plx_enums.LicenseFeaturesEnum.PLEXOSIntegratedEnergyModel

    PLEXOSForPowerSystems = plx_enums.LicenseFeaturesEnum.PLEXOSForPowerSystems

    PLEXOSValuebasedReliability = plx_enums.LicenseFeaturesEnum.PLEXOSValuebasedReliability

    PLEXOSRealtime = plx_enums.LicenseFeaturesEnum.PLEXOSRealtime

    PLEXOSforGas = plx_enums.LicenseFeaturesEnum.PLEXOSforGas

    PLEXOSforWater = plx_enums.LicenseFeaturesEnum.PLEXOSforWater

    PLEXOSTrial = plx_enums.LicenseFeaturesEnum.PLEXOSTrial

    PLEXOSAPI = plx_enums.LicenseFeaturesEnum.PLEXOSAPI


class LineCompaniesEnum(Enum):
    Share = plx_enums.LineCompaniesEnum.Share


class LineDispatchTypeEnum(Enum):
    Regulated = plx_enums.LineDispatchTypeEnum.Regulated

    Entrepreneurial = plx_enums.LineDispatchTypeEnum.Entrepreneurial


class LineEnforceLimitsEnum(Enum):
    Never = plx_enums.LineEnforceLimitsEnum.Never

    Voltage = plx_enums.LineEnforceLimitsEnum.Voltage

    Always = plx_enums.LineEnforceLimitsEnum.Always

    Contingency = plx_enums.LineEnforceLimitsEnum.Contingency


class LineTypeEnum(Enum):
    AC = plx_enums.LineTypeEnum.AC

    DC = plx_enums.LineTypeEnum.DC


class ListAttributeEnum(Enum):
    Report = plx_enums.ListAttributeEnum.Report

    Filter = plx_enums.ListAttributeEnum.Filter

    InclusiveEmpty = plx_enums.ListAttributeEnum.InclusiveEmpty

    Transient = plx_enums.ListAttributeEnum.Transient


class LoadMeteringPointEnum(Enum):
    GeneratorTerminal = plx_enums.LoadMeteringPointEnum.GeneratorTerminal

    SentOut = plx_enums.LoadMeteringPointEnum.SentOut


class LossMethodEnum(Enum):
    Auto = plx_enums.LossMethodEnum.Auto

    PiecewiseLinear = plx_enums.LossMethodEnum.PiecewiseLinear

    Conic = plx_enums.LossMethodEnum.Conic

    SuccessiveMLF = plx_enums.LossMethodEnum.SuccessiveMLF

    SinglePassGPF = plx_enums.LossMethodEnum.SinglePassGPF


class MLFRegionsEnum(Enum):
    LoadCoefficient = plx_enums.MLFRegionsEnum.LoadCoefficient


class MTScheduleAttributeEnum(Enum):
    DiscountRate = plx_enums.MTScheduleAttributeEnum.DiscountRate

    DiscountPeriodType = plx_enums.MTScheduleAttributeEnum.DiscountPeriodType

    EndEffectsMethod = plx_enums.MTScheduleAttributeEnum.EndEffectsMethod

    StepType = plx_enums.MTScheduleAttributeEnum.StepType

    AtaTime = plx_enums.MTScheduleAttributeEnum.AtaTime

    Chronology = plx_enums.MTScheduleAttributeEnum.Chronology

    LDCType = plx_enums.MTScheduleAttributeEnum.LDCType

    BlockCount = plx_enums.MTScheduleAttributeEnum.BlockCount

    LastBlockCount = plx_enums.MTScheduleAttributeEnum.LastBlockCount

    LDCSlicingMethod = plx_enums.MTScheduleAttributeEnum.LDCSlicingMethod

    LDCWeighta = plx_enums.MTScheduleAttributeEnum.LDCWeighta

    LDCWeightb = plx_enums.MTScheduleAttributeEnum.LDCWeightb

    LDCWeightc = plx_enums.MTScheduleAttributeEnum.LDCWeightc

    LDCWeightd = plx_enums.MTScheduleAttributeEnum.LDCWeightd

    LDCPinTop = plx_enums.MTScheduleAttributeEnum.LDCPinTop

    LDCPinBottom = plx_enums.MTScheduleAttributeEnum.LDCPinBottom

    SampleType = plx_enums.MTScheduleAttributeEnum.SampleType

    SamplingInterval = plx_enums.MTScheduleAttributeEnum.SamplingInterval

    ReducedSampleCount = plx_enums.MTScheduleAttributeEnum.ReducedSampleCount

    ReductionRelativeAccuracy = plx_enums.MTScheduleAttributeEnum.ReductionRelativeAccuracy

    HeatRateDetail = plx_enums.MTScheduleAttributeEnum.HeatRateDetail

    UseEffectiveLoadApproach = plx_enums.MTScheduleAttributeEnum.UseEffectiveLoadApproach

    OutageIncrement = plx_enums.MTScheduleAttributeEnum.OutageIncrement

    PricingMethod = plx_enums.MTScheduleAttributeEnum.PricingMethod

    TransmissionDetail = plx_enums.MTScheduleAttributeEnum.TransmissionDetail

    NewEntryDriver = plx_enums.MTScheduleAttributeEnum.NewEntryDriver

    NewEntryCapacityMechanism = plx_enums.MTScheduleAttributeEnum.NewEntryCapacityMechanism

    NewEntryTimeLag = plx_enums.MTScheduleAttributeEnum.NewEntryTimeLag

    StartCostAmortizationPeriod = plx_enums.MTScheduleAttributeEnum.StartCostAmortizationPeriod

    StochasticMethod = plx_enums.MTScheduleAttributeEnum.StochasticMethod

    WriteBridgeTextFiles = plx_enums.MTScheduleAttributeEnum.WriteBridgeTextFiles


class MaintenanceGasPipelinesEnum(Enum):
    OutageMaxFlow = plx_enums.MaintenanceGasPipelinesEnum.OutageMaxFlow

    OutageMaxFlowBack = plx_enums.MaintenanceGasPipelinesEnum.OutageMaxFlowBack


class MaintenanceGeneratorsEnum(Enum):
    OutageRating = plx_enums.MaintenanceGeneratorsEnum.OutageRating

    OutageRatingFactor = plx_enums.MaintenanceGeneratorsEnum.OutageRatingFactor

    OutageFirmCapacity = plx_enums.MaintenanceGeneratorsEnum.OutageFirmCapacity

    OutageFirmCapacityFactor = plx_enums.MaintenanceGeneratorsEnum.OutageFirmCapacityFactor


class MaintenanceLinesEnum(Enum):
    OutageMaxRating = plx_enums.MaintenanceLinesEnum.OutageMaxRating

    OutageMinRating = plx_enums.MaintenanceLinesEnum.OutageMinRating


class MarginalUnitTransmissionDetailEnum(Enum):
    Regional = plx_enums.MarginalUnitTransmissionDetailEnum.Regional

    System = plx_enums.MarginalUnitTransmissionDetailEnum.System


class MarketAttributeEnum(Enum):
    UnitCommitment = plx_enums.MarketAttributeEnum.UnitCommitment


class MarketCapacityGeneratorsEnum(Enum):
    OfferQuantity = plx_enums.MarketCapacityGeneratorsEnum.OfferQuantity

    OfferPrice = plx_enums.MarketCapacityGeneratorsEnum.OfferPrice


class MarketCompaniesEnum(Enum):
    Share = plx_enums.MarketCompaniesEnum.Share


class MarketHeatGeneratorsEnum(Enum):
    ConversionRate = plx_enums.MarketHeatGeneratorsEnum.ConversionRate


class MarketSettlementModelEnum(Enum):
    Natural = plx_enums.MarketSettlementModelEnum.Natural

    Buy = plx_enums.MarketSettlementModelEnum.Buy

    Sell = plx_enums.MarketSettlementModelEnum.Sell


class MarketTimescaleEnum(Enum):
    RealTime = plx_enums.MarketTimescaleEnum.RealTime

    DayAhead = plx_enums.MarketTimescaleEnum.DayAhead


class MarketTradingFormatEnum(Enum):
    Bilateral = plx_enums.MarketTradingFormatEnum.Bilateral

    POOLCO = plx_enums.MarketTradingFormatEnum.POOLCO


class MarketTypeEnum(Enum):
    None_ = 0

    Energy = plx_enums.MarketTypeEnum.Energy

    AncillaryServices = plx_enums.MarketTypeEnum.AncillaryServices

    Heat = plx_enums.MarketTypeEnum.Heat

    Capacity = plx_enums.MarketTypeEnum.Capacity

    Fuel = plx_enums.MarketTypeEnum.Fuel

    Emission = plx_enums.MarketTypeEnum.Emission

    Gas = plx_enums.MarketTypeEnum.Gas


class MinDownTimeModeEnum(Enum):
    Relaxed = plx_enums.MinDownTimeModeEnum.Relaxed

    Enforced = plx_enums.MinDownTimeModeEnum.Enforced


class ModelAttributeEnum(Enum):
    Enabled = plx_enums.ModelAttributeEnum.Enabled

    ExecutionOrder = plx_enums.ModelAttributeEnum.ExecutionOrder

    RandomNumberSeed = plx_enums.ModelAttributeEnum.RandomNumberSeed

    OutputtoFolder = plx_enums.ModelAttributeEnum.OutputtoFolder

    MakeUniqueName = plx_enums.ModelAttributeEnum.MakeUniqueName

    WriteInput = plx_enums.ModelAttributeEnum.WriteInput

    LoadCustomAssemblies = plx_enums.ModelAttributeEnum.LoadCustomAssemblies

    RunMode = plx_enums.ModelAttributeEnum.RunMode


class ModelScenariosEnum(Enum):
    ReadOrder = plx_enums.ModelScenariosEnum.ReadOrder


class MonteCarloMethodEnum(Enum):
    MonteCarlo = plx_enums.MonteCarloMethodEnum.MonteCarlo

    ConvergentMonteCarlo = plx_enums.MonteCarloMethodEnum.ConvergentMonteCarlo


class MonteCarloOutageScopeEnum(Enum):
    All = plx_enums.MonteCarloOutageScopeEnum.All

    ForcedOnly = plx_enums.MonteCarloOutageScopeEnum.ForcedOnly

    MaintenanceOnly = plx_enums.MonteCarloOutageScopeEnum.MaintenanceOnly

    None_ = 3


class NewEntryCapacityMechanismEnum(Enum):
    None_ = 0

    LOLPxVoLL = plx_enums.NewEntryCapacityMechanismEnum.LOLPxVoLL

    ReserveTrader = plx_enums.NewEntryCapacityMechanismEnum.ReserveTrader


class NewEntryContextEnum(Enum):
    Reliability = plx_enums.NewEntryContextEnum.Reliability

    Entrepreneurial = plx_enums.NewEntryContextEnum.Entrepreneurial


class NewEntryDriverEnum(Enum):
    None_ = 0

    ReliabilityOnly = plx_enums.NewEntryDriverEnum.ReliabilityOnly

    ReliabilityAndEntrepreneurial = plx_enums.NewEntryDriverEnum.ReliabilityAndEntrepreneurial

    EntrepreurialOnly = plx_enums.NewEntryDriverEnum.EntrepreurialOnly


class NodeAttributeEnum(Enum):
    Latitude = plx_enums.NodeAttributeEnum.Latitude

    Longitude = plx_enums.NodeAttributeEnum.Longitude


class NodeHubsEnum(Enum):
    PricingWeight = plx_enums.NodeHubsEnum.PricingWeight


class NodeTypeEnum(Enum):
    NodeTypeEnum_SystemObject = plx_enums.NodeTypeEnum.NodeTypeEnum_SystemObject

    NodeTypeEnum_ClassGroup = plx_enums.NodeTypeEnum.NodeTypeEnum_ClassGroup

    NodeTypeEnum_CategoryInSystemCollection = plx_enums.NodeTypeEnum.NodeTypeEnum_CategoryInSystemCollection

    NodeTypeEnum_SystemCollection = plx_enums.NodeTypeEnum.NodeTypeEnum_SystemCollection

    NodeTypeEnum_ObjectInSystemCollection = plx_enums.NodeTypeEnum.NodeTypeEnum_ObjectInSystemCollection

    NodeTypeEnum_ObjectCollection = plx_enums.NodeTypeEnum.NodeTypeEnum_ObjectCollection

    NodeTypeEnum_CategoryInObjectCollection = plx_enums.NodeTypeEnum.NodeTypeEnum_CategoryInObjectCollection

    NodeTypeEnum_ObjectInObjectCollection = plx_enums.NodeTypeEnum.NodeTypeEnum_ObjectInObjectCollection


class NonConvexModeEnum(Enum):
    Never = plx_enums.NonConvexModeEnum.Never

    Auto = plx_enums.NonConvexModeEnum.Auto

    Always = plx_enums.NonConvexModeEnum.Always


class OutAbatementConsumablesEnum(Enum):
    Consumption = plx_enums.OutAbatementConsumablesEnum.Consumption

    Cost = plx_enums.OutAbatementConsumablesEnum.Cost


class OutAbatementEmissionsEnum(Enum):
    GrossEmissions = plx_enums.OutAbatementEmissionsEnum.GrossEmissions

    Abatement = plx_enums.OutAbatementEmissionsEnum.Abatement

    NetEmissions = plx_enums.OutAbatementEmissionsEnum.NetEmissions

    Efficiency = plx_enums.OutAbatementEmissionsEnum.Efficiency

    AbatementValue = plx_enums.OutAbatementEmissionsEnum.AbatementValue


class OutCompanyEmissionsEnum(Enum):
    Production = plx_enums.OutCompanyEmissionsEnum.Production

    GrossProduction = plx_enums.OutCompanyEmissionsEnum.GrossProduction

    Removal = plx_enums.OutCompanyEmissionsEnum.Removal

    RemovalCost = plx_enums.OutCompanyEmissionsEnum.RemovalCost

    Abatement = plx_enums.OutCompanyEmissionsEnum.Abatement

    AbatementCost = plx_enums.OutCompanyEmissionsEnum.AbatementCost

    Generation = plx_enums.OutCompanyEmissionsEnum.Generation

    Intensity = plx_enums.OutCompanyEmissionsEnum.Intensity

    Allocation = plx_enums.OutCompanyEmissionsEnum.Allocation

    Cost = plx_enums.OutCompanyEmissionsEnum.Cost


class OutCompanyFuelsEnum(Enum):
    Offtake = plx_enums.OutCompanyFuelsEnum.Offtake

    OfftakeRatio = plx_enums.OutCompanyFuelsEnum.OfftakeRatio

    InventoryCost = plx_enums.OutCompanyFuelsEnum.InventoryCost


class OutCompanyRegionsEnum(Enum):
    Load = plx_enums.OutCompanyRegionsEnum.Load

    InstalledCapacity = plx_enums.OutCompanyRegionsEnum.InstalledCapacity

    AvailableCapacity = plx_enums.OutCompanyRegionsEnum.AvailableCapacity

    Generation = plx_enums.OutCompanyRegionsEnum.Generation

    MarginalCost = plx_enums.OutCompanyRegionsEnum.MarginalCost

    PriceReceived = plx_enums.OutCompanyRegionsEnum.PriceReceived

    PoolRevenue = plx_enums.OutCompanyRegionsEnum.PoolRevenue

    GenerationatRRN = plx_enums.OutCompanyRegionsEnum.GenerationatRRN

    ContractVolume = plx_enums.OutCompanyRegionsEnum.ContractVolume

    NetContractVolume = plx_enums.OutCompanyRegionsEnum.NetContractVolume

    ContractShortfall = plx_enums.OutCompanyRegionsEnum.ContractShortfall

    ContractSettlement = plx_enums.OutCompanyRegionsEnum.ContractSettlement

    NetContractSettlement = plx_enums.OutCompanyRegionsEnum.NetContractSettlement

    ShadowGeneration = plx_enums.OutCompanyRegionsEnum.ShadowGeneration


class OutCompanyReservesEnum(Enum):
    Provision = plx_enums.OutCompanyReservesEnum.Provision

    Revenue = plx_enums.OutCompanyReservesEnum.Revenue


class OutEmissionFuelsEnum(Enum):
    Production = plx_enums.OutEmissionFuelsEnum.Production

    GrossProduction = plx_enums.OutEmissionFuelsEnum.GrossProduction

    Removal = plx_enums.OutEmissionFuelsEnum.Removal

    RemovalCost = plx_enums.OutEmissionFuelsEnum.RemovalCost

    Abatement = plx_enums.OutEmissionFuelsEnum.Abatement

    AbatementCost = plx_enums.OutEmissionFuelsEnum.AbatementCost

    Generation = plx_enums.OutEmissionFuelsEnum.Generation

    Intensity = plx_enums.OutEmissionFuelsEnum.Intensity

    Cost = plx_enums.OutEmissionFuelsEnum.Cost


class OutEmissionGasNodesEnum(Enum):
    Production = plx_enums.OutEmissionGasNodesEnum.Production

    Cost = plx_enums.OutEmissionGasNodesEnum.Cost


class OutEmissionGeneratorsEnum(Enum):
    GenerationProduction = plx_enums.OutEmissionGeneratorsEnum.GenerationProduction

    UnitStartProduction = plx_enums.OutEmissionGeneratorsEnum.UnitStartProduction

    Production = plx_enums.OutEmissionGeneratorsEnum.Production

    GrossProduction = plx_enums.OutEmissionGeneratorsEnum.GrossProduction

    Removal = plx_enums.OutEmissionGeneratorsEnum.Removal

    RemovalCost = plx_enums.OutEmissionGeneratorsEnum.RemovalCost

    Abatement = plx_enums.OutEmissionGeneratorsEnum.Abatement

    AbatementCost = plx_enums.OutEmissionGeneratorsEnum.AbatementCost

    Generation = plx_enums.OutEmissionGeneratorsEnum.Generation

    Intensity = plx_enums.OutEmissionGeneratorsEnum.Intensity

    Cost = plx_enums.OutEmissionGeneratorsEnum.Cost

    IncrementalProductionRate = plx_enums.OutEmissionGeneratorsEnum.IncrementalProductionRate

    IncrementalCost = plx_enums.OutEmissionGeneratorsEnum.IncrementalCost

    SRMC = plx_enums.OutEmissionGeneratorsEnum.SRMC


class OutFinancialContractRegionsEnum(Enum):
    SettlementPrice = plx_enums.OutFinancialContractRegionsEnum.SettlementPrice

    Shortfall = plx_enums.OutFinancialContractRegionsEnum.Shortfall

    SettlementQuantity = plx_enums.OutFinancialContractRegionsEnum.SettlementQuantity

    Settlement = plx_enums.OutFinancialContractRegionsEnum.Settlement


class OutGasDemandCompaniesEnum(Enum):
    Demand = plx_enums.OutGasDemandCompaniesEnum.Demand

    Shortage = plx_enums.OutGasDemandCompaniesEnum.Shortage

    ShortageCost = plx_enums.OutGasDemandCompaniesEnum.ShortageCost

    Excess = plx_enums.OutGasDemandCompaniesEnum.Excess

    ExcessCost = plx_enums.OutGasDemandCompaniesEnum.ExcessCost

    NetDemand = plx_enums.OutGasDemandCompaniesEnum.NetDemand

    Cost = plx_enums.OutGasDemandCompaniesEnum.Cost


class OutGasFieldCompaniesEnum(Enum):
    Production = plx_enums.OutGasFieldCompaniesEnum.Production

    ProductionCost = plx_enums.OutGasFieldCompaniesEnum.ProductionCost

    FOMCost = plx_enums.OutGasFieldCompaniesEnum.FOMCost

    FixedCosts = plx_enums.OutGasFieldCompaniesEnum.FixedCosts

    ShadowPrice = plx_enums.OutGasFieldCompaniesEnum.ShadowPrice

    NetRevenue = plx_enums.OutGasFieldCompaniesEnum.NetRevenue

    NetProfit = plx_enums.OutGasFieldCompaniesEnum.NetProfit


class OutGasPipelineGasNodeFromEnum(Enum):
    ParticipationFactor = plx_enums.OutGasPipelineGasNodeFromEnum.ParticipationFactor


class OutGasPipelineGasNodeToEnum(Enum):
    ParticipationFactor = plx_enums.OutGasPipelineGasNodeToEnum.ParticipationFactor


class OutGeneratorCompaniesEnum(Enum):
    Generation = plx_enums.OutGeneratorCompaniesEnum.Generation

    DispatchableCapacity = plx_enums.OutGeneratorCompaniesEnum.DispatchableCapacity

    UndispatchedCapacity = plx_enums.OutGeneratorCompaniesEnum.UndispatchedCapacity

    FuelOfftake = plx_enums.OutGeneratorCompaniesEnum.FuelOfftake

    StartFuelOfftake = plx_enums.OutGeneratorCompaniesEnum.StartFuelOfftake

    HeatFuelOfftake = plx_enums.OutGeneratorCompaniesEnum.HeatFuelOfftake

    WasteHeat = plx_enums.OutGeneratorCompaniesEnum.WasteHeat

    NoCostCapacity = plx_enums.OutGeneratorCompaniesEnum.NoCostCapacity

    FixedLoadGeneration = plx_enums.OutGeneratorCompaniesEnum.FixedLoadGeneration

    MinLoadGeneration = plx_enums.OutGeneratorCompaniesEnum.MinLoadGeneration

    AuxiliaryUse = plx_enums.OutGeneratorCompaniesEnum.AuxiliaryUse

    PumpLoad = plx_enums.OutGeneratorCompaniesEnum.PumpLoad

    RaiseReserve = plx_enums.OutGeneratorCompaniesEnum.RaiseReserve

    LowerReserve = plx_enums.OutGeneratorCompaniesEnum.LowerReserve

    RegulationRaiseReserve = plx_enums.OutGeneratorCompaniesEnum.RegulationRaiseReserve

    RegulationLowerReserve = plx_enums.OutGeneratorCompaniesEnum.RegulationLowerReserve

    ReplacementReserve = plx_enums.OutGeneratorCompaniesEnum.ReplacementReserve

    HeatProduction = plx_enums.OutGeneratorCompaniesEnum.HeatProduction

    BoilerHeatProduction = plx_enums.OutGeneratorCompaniesEnum.BoilerHeatProduction

    FuelCost = plx_enums.OutGeneratorCompaniesEnum.FuelCost

    FuelTransportCost = plx_enums.OutGeneratorCompaniesEnum.FuelTransportCost

    FuelTransitionCost = plx_enums.OutGeneratorCompaniesEnum.FuelTransitionCost

    VOMCost = plx_enums.OutGeneratorCompaniesEnum.VOMCost

    UoSCost = plx_enums.OutGeneratorCompaniesEnum.UoSCost

    PumpCost = plx_enums.OutGeneratorCompaniesEnum.PumpCost

    ReservesVOMCost = plx_enums.OutGeneratorCompaniesEnum.ReservesVOMCost

    ReservesCost = plx_enums.OutGeneratorCompaniesEnum.ReservesCost

    HeatProductionCost = plx_enums.OutGeneratorCompaniesEnum.HeatProductionCost

    GenerationCost = plx_enums.OutGeneratorCompaniesEnum.GenerationCost

    StartShutdownCost = plx_enums.OutGeneratorCompaniesEnum.StartShutdownCost

    StartFuelCost = plx_enums.OutGeneratorCompaniesEnum.StartFuelCost

    EmissionsCost = plx_enums.OutGeneratorCompaniesEnum.EmissionsCost

    AbatementCost = plx_enums.OutGeneratorCompaniesEnum.AbatementCost

    TotalGenerationCost = plx_enums.OutGeneratorCompaniesEnum.TotalGenerationCost

    FOMCost = plx_enums.OutGeneratorCompaniesEnum.FOMCost

    EquityCost = plx_enums.OutGeneratorCompaniesEnum.EquityCost

    DebtCost = plx_enums.OutGeneratorCompaniesEnum.DebtCost

    ClearedOfferCost = plx_enums.OutGeneratorCompaniesEnum.ClearedOfferCost

    PoolRevenue = plx_enums.OutGeneratorCompaniesEnum.PoolRevenue

    ReservesRevenue = plx_enums.OutGeneratorCompaniesEnum.ReservesRevenue

    NetReservesRevenue = plx_enums.OutGeneratorCompaniesEnum.NetReservesRevenue

    HeatRevenue = plx_enums.OutGeneratorCompaniesEnum.HeatRevenue

    HeatMarketRevenue = plx_enums.OutGeneratorCompaniesEnum.HeatMarketRevenue

    FixedCosts = plx_enums.OutGeneratorCompaniesEnum.FixedCosts

    NetRevenue = plx_enums.OutGeneratorCompaniesEnum.NetRevenue

    NetProfit = plx_enums.OutGeneratorCompaniesEnum.NetProfit

    MonopolyRent = plx_enums.OutGeneratorCompaniesEnum.MonopolyRent

    ScheduledGeneration = plx_enums.OutGeneratorCompaniesEnum.ScheduledGeneration

    ScheduledRevenue = plx_enums.OutGeneratorCompaniesEnum.ScheduledRevenue

    ConstrainedOnRevenue = plx_enums.OutGeneratorCompaniesEnum.ConstrainedOnRevenue

    ConstrainedOffRevenue = plx_enums.OutGeneratorCompaniesEnum.ConstrainedOffRevenue

    ScheduledGenerationCost = plx_enums.OutGeneratorCompaniesEnum.ScheduledGenerationCost

    ScheduledOfferCost = plx_enums.OutGeneratorCompaniesEnum.ScheduledOfferCost

    ScheduledStartShutdownCost = plx_enums.OutGeneratorCompaniesEnum.ScheduledStartShutdownCost

    InstalledCapacity = plx_enums.OutGeneratorCompaniesEnum.InstalledCapacity

    RatedCapacity = plx_enums.OutGeneratorCompaniesEnum.RatedCapacity

    Maintenance = plx_enums.OutGeneratorCompaniesEnum.Maintenance

    ForcedOutage = plx_enums.OutGeneratorCompaniesEnum.ForcedOutage

    AvailableCapacity = plx_enums.OutGeneratorCompaniesEnum.AvailableCapacity

    CapacityBuilt = plx_enums.OutGeneratorCompaniesEnum.CapacityBuilt

    CapacityRetired = plx_enums.OutGeneratorCompaniesEnum.CapacityRetired

    NetNewCapacity = plx_enums.OutGeneratorCompaniesEnum.NetNewCapacity

    CapacityRevenue = plx_enums.OutGeneratorCompaniesEnum.CapacityRevenue

    BuildCost = plx_enums.OutGeneratorCompaniesEnum.BuildCost

    RetirementCost = plx_enums.OutGeneratorCompaniesEnum.RetirementCost


class OutGeneratorFuelsEnum(Enum):
    Offtake = plx_enums.OutGeneratorFuelsEnum.Offtake

    OfftakeRatio = plx_enums.OutGeneratorFuelsEnum.OfftakeRatio

    Generation = plx_enums.OutGeneratorFuelsEnum.Generation

    Price = plx_enums.OutGeneratorFuelsEnum.Price

    Cost = plx_enums.OutGeneratorFuelsEnum.Cost

    TransportCharge = plx_enums.OutGeneratorFuelsEnum.TransportCharge

    TransportCost = plx_enums.OutGeneratorFuelsEnum.TransportCost

    TransitionCost = plx_enums.OutGeneratorFuelsEnum.TransitionCost

    MarginalHeatRate = plx_enums.OutGeneratorFuelsEnum.MarginalHeatRate

    SRMC = plx_enums.OutGeneratorFuelsEnum.SRMC

    HoursAvailable = plx_enums.OutGeneratorFuelsEnum.HoursAvailable

    OfferQuantity = plx_enums.OutGeneratorFuelsEnum.OfferQuantity

    OfferPrice = plx_enums.OutGeneratorFuelsEnum.OfferPrice

    CostPrice = plx_enums.OutGeneratorFuelsEnum.CostPrice

    OfferCleared = plx_enums.OutGeneratorFuelsEnum.OfferCleared

    HoursinUse = plx_enums.OutGeneratorFuelsEnum.HoursinUse


class OutGeneratorStartFuelsEnum(Enum):
    Offtake = plx_enums.OutGeneratorStartFuelsEnum.Offtake

    Price = plx_enums.OutGeneratorStartFuelsEnum.Price

    Cost = plx_enums.OutGeneratorStartFuelsEnum.Cost

    TransportCost = plx_enums.OutGeneratorStartFuelsEnum.TransportCost


class OutGeneratorTransitionEnum(Enum):
    TransitionCost = plx_enums.OutGeneratorTransitionEnum.TransitionCost

    TransitionCount = plx_enums.OutGeneratorTransitionEnum.TransitionCount


class OutHeatPlantFuelsEnum(Enum):
    Offtake = plx_enums.OutHeatPlantFuelsEnum.Offtake

    OfftakeRatio = plx_enums.OutHeatPlantFuelsEnum.OfftakeRatio

    Price = plx_enums.OutHeatPlantFuelsEnum.Price

    Cost = plx_enums.OutHeatPlantFuelsEnum.Cost

    MarginalHeatRate = plx_enums.OutHeatPlantFuelsEnum.MarginalHeatRate

    SRMC = plx_enums.OutHeatPlantFuelsEnum.SRMC

    HoursinUse = plx_enums.OutHeatPlantFuelsEnum.HoursinUse


class OutHeatPlantStartFuelsEnum(Enum):
    Offtake = plx_enums.OutHeatPlantStartFuelsEnum.Offtake

    Price = plx_enums.OutHeatPlantStartFuelsEnum.Price

    Cost = plx_enums.OutHeatPlantStartFuelsEnum.Cost


class OutMarketCapacityGeneratorsEnum(Enum):
    Sales = plx_enums.OutMarketCapacityGeneratorsEnum.Sales

    Revenue = plx_enums.OutMarketCapacityGeneratorsEnum.Revenue

    ClearedOfferPrice = plx_enums.OutMarketCapacityGeneratorsEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.OutMarketCapacityGeneratorsEnum.ClearedOfferCost


class OutMarketFuelsEnum(Enum):
    Sales = plx_enums.OutMarketFuelsEnum.Sales

    Purchases = plx_enums.OutMarketFuelsEnum.Purchases

    Revenue = plx_enums.OutMarketFuelsEnum.Revenue

    Cost = plx_enums.OutMarketFuelsEnum.Cost


class OutMarketGasNodesEnum(Enum):
    Sales = plx_enums.OutMarketGasNodesEnum.Sales

    Purchases = plx_enums.OutMarketGasNodesEnum.Purchases

    NetSales = plx_enums.OutMarketGasNodesEnum.NetSales

    NetPurchases = plx_enums.OutMarketGasNodesEnum.NetPurchases

    Revenue = plx_enums.OutMarketGasNodesEnum.Revenue

    Cost = plx_enums.OutMarketGasNodesEnum.Cost

    NetRevenue = plx_enums.OutMarketGasNodesEnum.NetRevenue

    NetCost = plx_enums.OutMarketGasNodesEnum.NetCost


class OutMarketHeatGeneratorsEnum(Enum):
    Sales = plx_enums.OutMarketHeatGeneratorsEnum.Sales

    Revenue = plx_enums.OutMarketHeatGeneratorsEnum.Revenue


class OutMarketNodesEnum(Enum):
    Sales = plx_enums.OutMarketNodesEnum.Sales

    Purchases = plx_enums.OutMarketNodesEnum.Purchases

    NetSales = plx_enums.OutMarketNodesEnum.NetSales

    NetPurchases = plx_enums.OutMarketNodesEnum.NetPurchases

    Revenue = plx_enums.OutMarketNodesEnum.Revenue

    Cost = plx_enums.OutMarketNodesEnum.Cost

    NetRevenue = plx_enums.OutMarketNodesEnum.NetRevenue

    NetCost = plx_enums.OutMarketNodesEnum.NetCost


class OutMarketReservesEnum(Enum):
    Sales = plx_enums.OutMarketReservesEnum.Sales

    Purchases = plx_enums.OutMarketReservesEnum.Purchases

    NetSales = plx_enums.OutMarketReservesEnum.NetSales

    NetPurchases = plx_enums.OutMarketReservesEnum.NetPurchases

    Revenue = plx_enums.OutMarketReservesEnum.Revenue

    Cost = plx_enums.OutMarketReservesEnum.Cost

    NetRevenue = plx_enums.OutMarketReservesEnum.NetRevenue

    NetCost = plx_enums.OutMarketReservesEnum.NetCost


class OutRSICompaniesEnum(Enum):
    SupplyCapacity = plx_enums.OutRSICompaniesEnum.SupplyCapacity

    BidCostMarkup = plx_enums.OutRSICompaniesEnum.BidCostMarkup


class OutRSIInterfacesEnum(Enum):
    SupplyCapacity = plx_enums.OutRSIInterfacesEnum.SupplyCapacity


class OutRSILinesEnum(Enum):
    SupplyCapacity = plx_enums.OutRSILinesEnum.SupplyCapacity


class OutRegionEmissionsEnum(Enum):
    Production = plx_enums.OutRegionEmissionsEnum.Production

    GrossProduction = plx_enums.OutRegionEmissionsEnum.GrossProduction

    Removal = plx_enums.OutRegionEmissionsEnum.Removal

    RemovalCost = plx_enums.OutRegionEmissionsEnum.RemovalCost

    Abatement = plx_enums.OutRegionEmissionsEnum.Abatement

    AbatementCost = plx_enums.OutRegionEmissionsEnum.AbatementCost

    Generation = plx_enums.OutRegionEmissionsEnum.Generation

    Intensity = plx_enums.OutRegionEmissionsEnum.Intensity

    Cost = plx_enums.OutRegionEmissionsEnum.Cost


class OutRegionRegionsEnum(Enum):
    AvailableTransferCapability = plx_enums.OutRegionRegionsEnum.AvailableTransferCapability

    AvailableTransferCapabilityBack = plx_enums.OutRegionRegionsEnum.AvailableTransferCapabilityBack

    Imports = plx_enums.OutRegionRegionsEnum.Imports

    Exports = plx_enums.OutRegionRegionsEnum.Exports

    NetInterchange = plx_enums.OutRegionRegionsEnum.NetInterchange

    WheelingCost = plx_enums.OutRegionRegionsEnum.WheelingCost


class OutReserveBatteriesEnum(Enum):
    AvailableResponse = plx_enums.OutReserveBatteriesEnum.AvailableResponse

    Provision = plx_enums.OutReserveBatteriesEnum.Provision

    ClearedOfferPrice = plx_enums.OutReserveBatteriesEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.OutReserveBatteriesEnum.ClearedOfferCost

    Revenue = plx_enums.OutReserveBatteriesEnum.Revenue


class OutReserveGeneratorContingenciesEnum(Enum):
    Risk = plx_enums.OutReserveGeneratorContingenciesEnum.Risk

    ShadowPrice = plx_enums.OutReserveGeneratorContingenciesEnum.ShadowPrice


class OutReserveGeneratorCostAllocationEnum(Enum):
    Cost = plx_enums.OutReserveGeneratorCostAllocationEnum.Cost


class OutReserveGeneratorsEnum(Enum):
    AvailableResponse = plx_enums.OutReserveGeneratorsEnum.AvailableResponse

    Provision = plx_enums.OutReserveGeneratorsEnum.Provision

    SpinningReserveProvision = plx_enums.OutReserveGeneratorsEnum.SpinningReserveProvision

    SyncCondReserveProvision = plx_enums.OutReserveGeneratorsEnum.SyncCondReserveProvision

    PumpDispatchableLoadProvision = plx_enums.OutReserveGeneratorsEnum.PumpDispatchableLoadProvision

    NonspinningReserveProvision = plx_enums.OutReserveGeneratorsEnum.NonspinningReserveProvision

    ClearedOfferPrice = plx_enums.OutReserveGeneratorsEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.OutReserveGeneratorsEnum.ClearedOfferCost

    Revenue = plx_enums.OutReserveGeneratorsEnum.Revenue


class OutReserveLineContingenciesEnum(Enum):
    Risk = plx_enums.OutReserveLineContingenciesEnum.Risk

    ShadowPrice = plx_enums.OutReserveLineContingenciesEnum.ShadowPrice


class OutReservePurchasersEnum(Enum):
    AvailableResponse = plx_enums.OutReservePurchasersEnum.AvailableResponse

    Provision = plx_enums.OutReservePurchasersEnum.Provision

    Revenue = plx_enums.OutReservePurchasersEnum.Revenue

    ClearedOfferPrice = plx_enums.OutReservePurchasersEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.OutReservePurchasersEnum.ClearedOfferCost

    Cost = plx_enums.OutReservePurchasersEnum.Cost


class OutReserveRegionsEnum(Enum):
    Risk = plx_enums.OutReserveRegionsEnum.Risk


class OutZoneEmissionsEnum(Enum):
    Production = plx_enums.OutZoneEmissionsEnum.Production

    GrossProduction = plx_enums.OutZoneEmissionsEnum.GrossProduction

    Removal = plx_enums.OutZoneEmissionsEnum.Removal

    RemovalCost = plx_enums.OutZoneEmissionsEnum.RemovalCost

    Abatement = plx_enums.OutZoneEmissionsEnum.Abatement

    AbatementCost = plx_enums.OutZoneEmissionsEnum.AbatementCost

    Generation = plx_enums.OutZoneEmissionsEnum.Generation

    Intensity = plx_enums.OutZoneEmissionsEnum.Intensity

    Cost = plx_enums.OutZoneEmissionsEnum.Cost


class OutZoneZonesEnum(Enum):
    AvailableTransferCapability = plx_enums.OutZoneZonesEnum.AvailableTransferCapability

    AvailableTransferCapabilityBack = plx_enums.OutZoneZonesEnum.AvailableTransferCapabilityBack

    WheelingCost = plx_enums.OutZoneZonesEnum.WheelingCost


class OutageDataEnum(Enum):
    UnitsOut = plx_enums.OutageDataEnum.UnitsOut

    Maintenance = plx_enums.OutageDataEnum.Maintenance

    ForcedOutage = plx_enums.OutageDataEnum.ForcedOutage


class OutageRateDenominatorEnum(Enum):
    Time = plx_enums.OutageRateDenominatorEnum.Time

    OperatingTime = plx_enums.OutageRateDenominatorEnum.OperatingTime


class OutageTypeEnum(Enum):
    None_ = 0

    Maintenance = plx_enums.OutageTypeEnum.Maintenance

    Forced = plx_enums.OutageTypeEnum.Forced


class PASAAttributeEnum(Enum):
    StepType = plx_enums.PASAAttributeEnum.StepType

    TransmissionDetail = plx_enums.PASAAttributeEnum.TransmissionDetail

    IncludeDSP = plx_enums.PASAAttributeEnum.IncludeDSP

    IncludeDemandBids = plx_enums.PASAAttributeEnum.IncludeDemandBids

    IncludeContractGeneration = plx_enums.PASAAttributeEnum.IncludeContractGeneration

    IncludeContractLoad = plx_enums.PASAAttributeEnum.IncludeContractLoad

    IncludeMarketPurchases = plx_enums.PASAAttributeEnum.IncludeMarketPurchases

    ConstraintsEnabled = plx_enums.PASAAttributeEnum.ConstraintsEnabled

    InterfaceConstraintsEnabled = plx_enums.PASAAttributeEnum.InterfaceConstraintsEnabled

    MaintenanceSculpting = plx_enums.PASAAttributeEnum.MaintenanceSculpting

    ComputeReliabilityIndices = plx_enums.PASAAttributeEnum.ComputeReliabilityIndices

    ComputeMultiareaReliabilityIndices = plx_enums.PASAAttributeEnum.ComputeMultiareaReliabilityIndices

    WriteOutageTextFiles = plx_enums.PASAAttributeEnum.WriteOutageTextFiles

    StochasticMethod = plx_enums.PASAAttributeEnum.StochasticMethod


class PLEXOSVersionEnum(Enum):
    Minor = plx_enums.PLEXOSVersionEnum.Minor

    Major = plx_enums.PLEXOSVersionEnum.Major


class PageEnum(Enum):
    PageEnum_Objects = plx_enums.PageEnum.PageEnum_Objects

    PageEnum_Memberships = plx_enums.PageEnum.PageEnum_Memberships

    PageEnum_Properties = plx_enums.PageEnum.PageEnum_Properties


class PerformanceAttributeEnum(Enum):
    SOLVER = plx_enums.PerformanceAttributeEnum.SOLVER

    SmallLPOptimizer = plx_enums.PerformanceAttributeEnum.SmallLPOptimizer

    SmallLPNonzeroCount = plx_enums.PerformanceAttributeEnum.SmallLPNonzeroCount

    ColdStartOptimizer1 = plx_enums.PerformanceAttributeEnum.ColdStartOptimizer1

    ColdStartOptimizer2 = plx_enums.PerformanceAttributeEnum.ColdStartOptimizer2

    ColdStartOptimizer3 = plx_enums.PerformanceAttributeEnum.ColdStartOptimizer3

    HotStartOptimizer1 = plx_enums.PerformanceAttributeEnum.HotStartOptimizer1

    HotStartOptimizer2 = plx_enums.PerformanceAttributeEnum.HotStartOptimizer2

    HotStartOptimizer3 = plx_enums.PerformanceAttributeEnum.HotStartOptimizer3

    MaximumThreads = plx_enums.PerformanceAttributeEnum.MaximumThreads

    MIPRootOptimizer = plx_enums.PerformanceAttributeEnum.MIPRootOptimizer

    MIPNodeOptimizer = plx_enums.PerformanceAttributeEnum.MIPNodeOptimizer

    SmallMIPRelativeGap = plx_enums.PerformanceAttributeEnum.SmallMIPRelativeGap

    SmallMIPImproveStartGap = plx_enums.PerformanceAttributeEnum.SmallMIPImproveStartGap

    SmallMIPMaxTime = plx_enums.PerformanceAttributeEnum.SmallMIPMaxTime

    SmallMIPIntegerCount = plx_enums.PerformanceAttributeEnum.SmallMIPIntegerCount

    MIPRelativeGap = plx_enums.PerformanceAttributeEnum.MIPRelativeGap

    MIPImproveStartGap = plx_enums.PerformanceAttributeEnum.MIPImproveStartGap

    MIPMaxTime = plx_enums.PerformanceAttributeEnum.MIPMaxTime

    MIPMaxRelaxationRepairTime = plx_enums.PerformanceAttributeEnum.MIPMaxRelaxationRepairTime

    MIPMaximumThreads = plx_enums.PerformanceAttributeEnum.MIPMaximumThreads

    MaximumParallelTasks = plx_enums.PerformanceAttributeEnum.MaximumParallelTasks

    MIPStartSolution = plx_enums.PerformanceAttributeEnum.MIPStartSolution


class PerformanceEnum(Enum):
    MaximizeSpeed = plx_enums.PerformanceEnum.MaximizeSpeed

    MinimizeMemoryUse = plx_enums.PerformanceEnum.MinimizeMemoryUse


class PeriodEnum(Enum):
    Interval = plx_enums.PeriodEnum.Interval

    Day = plx_enums.PeriodEnum.Day

    Week = plx_enums.PeriodEnum.Week

    Month = plx_enums.PeriodEnum.Month

    FiscalYear = plx_enums.PeriodEnum.FiscalYear

    Custom = plx_enums.PeriodEnum.Custom

    Hour = plx_enums.PeriodEnum.Hour

    Quarter = plx_enums.PeriodEnum.Quarter

    Block = plx_enums.PeriodEnum.Block

    Undefined = plx_enums.PeriodEnum.Undefined


class PhysicalContractCompaniesEnum(Enum):
    Share = plx_enums.PhysicalContractCompaniesEnum.Share


class PowerStationNodesEnum(Enum):
    GenerationParticipationFactor = plx_enums.PowerStationNodesEnum.GenerationParticipationFactor


class ProductionAttributeEnum(Enum):
    DispatchbyPowerStation = plx_enums.ProductionAttributeEnum.DispatchbyPowerStation

    UnitCommitmentOptimality = plx_enums.ProductionAttributeEnum.UnitCommitmentOptimality

    RoundingUpThreshold = plx_enums.ProductionAttributeEnum.RoundingUpThreshold

    RoundedRelaxationCommitmentModel = plx_enums.ProductionAttributeEnum.RoundedRelaxationCommitmentModel

    RoundedRelaxationTuning = plx_enums.ProductionAttributeEnum.RoundedRelaxationTuning

    RoundedRelaxationStartThreshold = plx_enums.ProductionAttributeEnum.RoundedRelaxationStartThreshold

    RoundedRelaxationEndThreshold = plx_enums.ProductionAttributeEnum.RoundedRelaxationEndThreshold

    RoundedRelaxationThresholdIncrement = plx_enums.ProductionAttributeEnum.RoundedRelaxationThresholdIncrement

    DPCapacityFactorThreshold = plx_enums.ProductionAttributeEnum.DPCapacityFactorThreshold

    DPCapacityFactorErrorThreshold = plx_enums.ProductionAttributeEnum.DPCapacityFactorErrorThreshold

    FuelUseFunctionPrecision = plx_enums.ProductionAttributeEnum.FuelUseFunctionPrecision

    MaxHeatRateTranches = plx_enums.ProductionAttributeEnum.MaxHeatRateTranches

    HeatRateErrorMethod = plx_enums.ProductionAttributeEnum.HeatRateErrorMethod

    StartCostMethod = plx_enums.ProductionAttributeEnum.StartCostMethod

    CapacityFactorConstraintBasis = plx_enums.ProductionAttributeEnum.CapacityFactorConstraintBasis

    FormulateUpfront = plx_enums.ProductionAttributeEnum.FormulateUpfront

    FormulateRampUpfront = plx_enums.ProductionAttributeEnum.FormulateRampUpfront

    IntegersinLookahead = plx_enums.ProductionAttributeEnum.IntegersinLookahead

    ForcedOutageRelaxesMinDownTime = plx_enums.ProductionAttributeEnum.ForcedOutageRelaxesMinDownTime

    PumpandGenerate = plx_enums.ProductionAttributeEnum.PumpandGenerate


class ProductionCapacityFactorConstraintBasisEnum(Enum):
    MaxCapacity = plx_enums.ProductionCapacityFactorConstraintBasisEnum.MaxCapacity

    Rating = plx_enums.ProductionCapacityFactorConstraintBasisEnum.Rating


class ProductionEnergyConstraintDecompositionEnum(Enum):
    ToConstraints = plx_enums.ProductionEnergyConstraintDecompositionEnum.ToConstraints

    ToProfile = plx_enums.ProductionEnergyConstraintDecompositionEnum.ToProfile


class ProductionFixedLoadMethod(Enum):
    RelaxWhenZero = plx_enums.ProductionFixedLoadMethod.RelaxWhenZero

    EnforceAllPeriods = plx_enums.ProductionFixedLoadMethod.EnforceAllPeriods


class ProductionHeatRateErrorMethod(Enum):
    ThrowError = plx_enums.ProductionHeatRateErrorMethod.ThrowError

    WarnAndReportRawCurve = plx_enums.ProductionHeatRateErrorMethod.WarnAndReportRawCurve

    WarnAndReportAdjustedCurve = plx_enums.ProductionHeatRateErrorMethod.WarnAndReportAdjustedCurve

    AdjustAndContinue = plx_enums.ProductionHeatRateErrorMethod.AdjustAndContinue

    AllowNonconvex = plx_enums.ProductionHeatRateErrorMethod.AllowNonconvex


class ProductionIntegersinLookaheadEnum(Enum):
    Never = plx_enums.ProductionIntegersinLookaheadEnum.Never

    Auto = plx_enums.ProductionIntegersinLookaheadEnum.Auto

    Always = plx_enums.ProductionIntegersinLookaheadEnum.Always


class ProductionRampConstraintMethodEnum(Enum):
    TwoPassHeuristic = plx_enums.ProductionRampConstraintMethodEnum.TwoPassHeuristic

    Intertemporal = plx_enums.ProductionRampConstraintMethodEnum.Intertemporal


class ProjectAttributeEnum(Enum):
    Enabled = plx_enums.ProjectAttributeEnum.Enabled


class PropertyIDEnum(Enum):
    SystemGenerators_MustReport = plx_enums.PropertyIDEnum.SystemGenerators_MustReport

    SystemGenerators_RandomNumberSeed = plx_enums.PropertyIDEnum.SystemGenerators_RandomNumberSeed

    SystemGenerators_DispatchPeriod = plx_enums.PropertyIDEnum.SystemGenerators_DispatchPeriod

    SystemGenerators_MaxHeatRateTranches = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatRateTranches

    SystemGenerators_FormulateNonconvex = plx_enums.PropertyIDEnum.SystemGenerators_FormulateNonconvex

    SystemGenerators_HeadEffectsMethod = plx_enums.PropertyIDEnum.SystemGenerators_HeadEffectsMethod

    SystemGenerators_MinDownTimeMode = plx_enums.PropertyIDEnum.SystemGenerators_MinDownTimeMode

    SystemGenerators_ForcedOutageRateDenominator = plx_enums.PropertyIDEnum.SystemGenerators_ForcedOutageRateDenominator

    SystemGenerators_RepairTimeDistribution = plx_enums.PropertyIDEnum.SystemGenerators_RepairTimeDistribution

    SystemGenerators_FixedLoadMethod = plx_enums.PropertyIDEnum.SystemGenerators_FixedLoadMethod

    SystemGenerators_PriceSetting = plx_enums.PropertyIDEnum.SystemGenerators_PriceSetting

    SystemGenerators_OfferQuantityFormat = plx_enums.PropertyIDEnum.SystemGenerators_OfferQuantityFormat

    SystemGenerators_OffersMustClearinOrder = plx_enums.PropertyIDEnum.SystemGenerators_OffersMustClearinOrder

    SystemGenerators_UnitCommitmentOptimality = plx_enums.PropertyIDEnum.SystemGenerators_UnitCommitmentOptimality

    SystemGenerators_RoundingUpThreshold = plx_enums.PropertyIDEnum.SystemGenerators_RoundingUpThreshold

    SystemGenerators_IncludeinRoundedRelaxationMeritOrder = plx_enums.PropertyIDEnum.SystemGenerators_IncludeinRoundedRelaxationMeritOrder

    SystemGenerators_StartProfileRange = plx_enums.PropertyIDEnum.SystemGenerators_StartProfileRange

    SystemGenerators_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemGenerators_ExpansionOptimality

    SystemGenerators_DecliningDepreciationBalance = plx_enums.PropertyIDEnum.SystemGenerators_DecliningDepreciationBalance

    SystemGenerators_EnergyLimitDecompositionMethod = plx_enums.PropertyIDEnum.SystemGenerators_EnergyLimitDecompositionMethod

    SystemGenerators_IncludeinUplift = plx_enums.PropertyIDEnum.SystemGenerators_IncludeinUplift

    SystemGenerators_IncludeinCapacityPayments = plx_enums.PropertyIDEnum.SystemGenerators_IncludeinCapacityPayments

    SystemGenerators_BalancePeriod = plx_enums.PropertyIDEnum.SystemGenerators_BalancePeriod

    SystemGenerators_InternalVolumeScalar = plx_enums.PropertyIDEnum.SystemGenerators_InternalVolumeScalar

    SystemGenerators_EndEffectsMethod = plx_enums.PropertyIDEnum.SystemGenerators_EndEffectsMethod

    SystemGenerators_RecyclePenalty = plx_enums.PropertyIDEnum.SystemGenerators_RecyclePenalty

    SystemGenerators_DecompositionMethod = plx_enums.PropertyIDEnum.SystemGenerators_DecompositionMethod

    SystemGenerators_DecompositionPenaltya = plx_enums.PropertyIDEnum.SystemGenerators_DecompositionPenaltya

    SystemGenerators_DecompositionPenaltyb = plx_enums.PropertyIDEnum.SystemGenerators_DecompositionPenaltyb

    SystemGenerators_DecompositionPenaltyc = plx_enums.PropertyIDEnum.SystemGenerators_DecompositionPenaltyc

    SystemGenerators_DecompositionPenaltyx = plx_enums.PropertyIDEnum.SystemGenerators_DecompositionPenaltyx

    SystemGenerators_DecompositionBoundPenalty = plx_enums.PropertyIDEnum.SystemGenerators_DecompositionBoundPenalty

    SystemGenerators_EnforceBounds = plx_enums.PropertyIDEnum.SystemGenerators_EnforceBounds

    SystemGenerators_IsStrategic = plx_enums.PropertyIDEnum.SystemGenerators_IsStrategic

    SystemGenerators_TransitionType = plx_enums.PropertyIDEnum.SystemGenerators_TransitionType

    SystemGenerators_Units = plx_enums.PropertyIDEnum.SystemGenerators_Units

    SystemGenerators_MaxCapacity = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacity

    SystemGenerators_MinStableLevel = plx_enums.PropertyIDEnum.SystemGenerators_MinStableLevel

    SystemGenerators_MinStableFactor = plx_enums.PropertyIDEnum.SystemGenerators_MinStableFactor

    SystemGenerators_FuelPrice = plx_enums.PropertyIDEnum.SystemGenerators_FuelPrice

    SystemGenerators_LoadPoint = plx_enums.PropertyIDEnum.SystemGenerators_LoadPoint

    SystemGenerators_HeatRate = plx_enums.PropertyIDEnum.SystemGenerators_HeatRate

    SystemGenerators_HeatRateBase = plx_enums.PropertyIDEnum.SystemGenerators_HeatRateBase

    SystemGenerators_HeatRateIncr = plx_enums.PropertyIDEnum.SystemGenerators_HeatRateIncr

    SystemGenerators_HeatRateIncr2 = plx_enums.PropertyIDEnum.SystemGenerators_HeatRateIncr2

    SystemGenerators_HeatRateIncr3 = plx_enums.PropertyIDEnum.SystemGenerators_HeatRateIncr3

    SystemGenerators_VOMCharge = plx_enums.PropertyIDEnum.SystemGenerators_VOMCharge

    SystemGenerators_UoSCharge = plx_enums.PropertyIDEnum.SystemGenerators_UoSCharge

    SystemGenerators_RunningCost = plx_enums.PropertyIDEnum.SystemGenerators_RunningCost

    SystemGenerators_StartCost = plx_enums.PropertyIDEnum.SystemGenerators_StartCost

    SystemGenerators_StartCostTime = plx_enums.PropertyIDEnum.SystemGenerators_StartCostTime

    SystemGenerators_RunUpRate = plx_enums.PropertyIDEnum.SystemGenerators_RunUpRate

    SystemGenerators_StartProfile = plx_enums.PropertyIDEnum.SystemGenerators_StartProfile

    SystemGenerators_StartPenalty = plx_enums.PropertyIDEnum.SystemGenerators_StartPenalty

    SystemGenerators_ShutdownCost = plx_enums.PropertyIDEnum.SystemGenerators_ShutdownCost

    SystemGenerators_RunDownRate = plx_enums.PropertyIDEnum.SystemGenerators_RunDownRate

    SystemGenerators_ShutdownProfile = plx_enums.PropertyIDEnum.SystemGenerators_ShutdownProfile

    SystemGenerators_ShutdownPenalty = plx_enums.PropertyIDEnum.SystemGenerators_ShutdownPenalty

    SystemGenerators_Rating = plx_enums.PropertyIDEnum.SystemGenerators_Rating

    SystemGenerators_RatingFactor = plx_enums.PropertyIDEnum.SystemGenerators_RatingFactor

    SystemGenerators_MinUpTime = plx_enums.PropertyIDEnum.SystemGenerators_MinUpTime

    SystemGenerators_MinDownTime = plx_enums.PropertyIDEnum.SystemGenerators_MinDownTime

    SystemGenerators_MaxUpTime = plx_enums.PropertyIDEnum.SystemGenerators_MaxUpTime

    SystemGenerators_MaxDownTime = plx_enums.PropertyIDEnum.SystemGenerators_MaxDownTime

    SystemGenerators_MustRunUnits = plx_enums.PropertyIDEnum.SystemGenerators_MustRunUnits

    SystemGenerators_FixedLoad = plx_enums.PropertyIDEnum.SystemGenerators_FixedLoad

    SystemGenerators_FixedLoadPenalty = plx_enums.PropertyIDEnum.SystemGenerators_FixedLoadPenalty

    SystemGenerators_MinLoad = plx_enums.PropertyIDEnum.SystemGenerators_MinLoad

    SystemGenerators_MinLoadPenalty = plx_enums.PropertyIDEnum.SystemGenerators_MinLoadPenalty

    SystemGenerators_MaxLoad = plx_enums.PropertyIDEnum.SystemGenerators_MaxLoad

    SystemGenerators_Commit = plx_enums.PropertyIDEnum.SystemGenerators_Commit

    SystemGenerators_FuelMixPenalty = plx_enums.PropertyIDEnum.SystemGenerators_FuelMixPenalty

    SystemGenerators_RampUpCharge = plx_enums.PropertyIDEnum.SystemGenerators_RampUpCharge

    SystemGenerators_RampDownCharge = plx_enums.PropertyIDEnum.SystemGenerators_RampDownCharge

    SystemGenerators_MaxRampUp = plx_enums.PropertyIDEnum.SystemGenerators_MaxRampUp

    SystemGenerators_MaxRampUpPenalty = plx_enums.PropertyIDEnum.SystemGenerators_MaxRampUpPenalty

    SystemGenerators_MaxRampDown = plx_enums.PropertyIDEnum.SystemGenerators_MaxRampDown

    SystemGenerators_MaxRampDownPenalty = plx_enums.PropertyIDEnum.SystemGenerators_MaxRampDownPenalty

    SystemGenerators_RoughRunningPoint = plx_enums.PropertyIDEnum.SystemGenerators_RoughRunningPoint

    SystemGenerators_RoughRunningRange = plx_enums.PropertyIDEnum.SystemGenerators_RoughRunningRange

    SystemGenerators_RegulationPoint = plx_enums.PropertyIDEnum.SystemGenerators_RegulationPoint

    SystemGenerators_RegulationRange = plx_enums.PropertyIDEnum.SystemGenerators_RegulationRange

    SystemGenerators_AuxFixed = plx_enums.PropertyIDEnum.SystemGenerators_AuxFixed

    SystemGenerators_AuxBase = plx_enums.PropertyIDEnum.SystemGenerators_AuxBase

    SystemGenerators_AuxIncr = plx_enums.PropertyIDEnum.SystemGenerators_AuxIncr

    SystemGenerators_MarginalLossFactor = plx_enums.PropertyIDEnum.SystemGenerators_MarginalLossFactor

    SystemGenerators_EfficiencyBase = plx_enums.PropertyIDEnum.SystemGenerators_EfficiencyBase

    SystemGenerators_EfficiencyIncr = plx_enums.PropertyIDEnum.SystemGenerators_EfficiencyIncr

    SystemGenerators_PumpEfficiency = plx_enums.PropertyIDEnum.SystemGenerators_PumpEfficiency

    SystemGenerators_PumpLoad = plx_enums.PropertyIDEnum.SystemGenerators_PumpLoad

    SystemGenerators_PumpUnits = plx_enums.PropertyIDEnum.SystemGenerators_PumpUnits

    SystemGenerators_MinPumpLoad = plx_enums.PropertyIDEnum.SystemGenerators_MinPumpLoad

    SystemGenerators_MustPumpUnits = plx_enums.PropertyIDEnum.SystemGenerators_MustPumpUnits

    SystemGenerators_MaxUnitsPumping = plx_enums.PropertyIDEnum.SystemGenerators_MaxUnitsPumping

    SystemGenerators_FixedPumpLoad = plx_enums.PropertyIDEnum.SystemGenerators_FixedPumpLoad

    SystemGenerators_FixedPumpLoadPenalty = plx_enums.PropertyIDEnum.SystemGenerators_FixedPumpLoadPenalty

    SystemGenerators_PumpUoSCharge = plx_enums.PropertyIDEnum.SystemGenerators_PumpUoSCharge

    SystemGenerators_MinPumpTime = plx_enums.PropertyIDEnum.SystemGenerators_MinPumpTime

    SystemGenerators_MinPumpDownTime = plx_enums.PropertyIDEnum.SystemGenerators_MinPumpDownTime

    SystemGenerators_ReservesVOMCharge = plx_enums.PropertyIDEnum.SystemGenerators_ReservesVOMCharge

    SystemGenerators_SyncCondUnits = plx_enums.PropertyIDEnum.SystemGenerators_SyncCondUnits

    SystemGenerators_MustrunSyncCondUnits = plx_enums.PropertyIDEnum.SystemGenerators_MustrunSyncCondUnits

    SystemGenerators_SyncCondLoad = plx_enums.PropertyIDEnum.SystemGenerators_SyncCondLoad

    SystemGenerators_SyncCondVOMCharge = plx_enums.PropertyIDEnum.SystemGenerators_SyncCondVOMCharge

    SystemGenerators_ReserveShare = plx_enums.PropertyIDEnum.SystemGenerators_ReserveShare

    SystemGenerators_InitialGeneration = plx_enums.PropertyIDEnum.SystemGenerators_InitialGeneration

    SystemGenerators_InitialUnitsGenerating = plx_enums.PropertyIDEnum.SystemGenerators_InitialUnitsGenerating

    SystemGenerators_InitialHoursUp = plx_enums.PropertyIDEnum.SystemGenerators_InitialHoursUp

    SystemGenerators_InitialHoursDown = plx_enums.PropertyIDEnum.SystemGenerators_InitialHoursDown

    SystemGenerators_InitialPumping = plx_enums.PropertyIDEnum.SystemGenerators_InitialPumping

    SystemGenerators_InitialUnitsPumping = plx_enums.PropertyIDEnum.SystemGenerators_InitialUnitsPumping

    SystemGenerators_InitialHoursPumping = plx_enums.PropertyIDEnum.SystemGenerators_InitialHoursPumping

    SystemGenerators_GeneratortoPumpSwitchTime = plx_enums.PropertyIDEnum.SystemGenerators_GeneratortoPumpSwitchTime

    SystemGenerators_PumptoGeneratorSwitchTime = plx_enums.PropertyIDEnum.SystemGenerators_PumptoGeneratorSwitchTime

    SystemGenerators_EfficiencyDegradation = plx_enums.PropertyIDEnum.SystemGenerators_EfficiencyDegradation

    SystemGenerators_LastStartState = plx_enums.PropertyIDEnum.SystemGenerators_LastStartState

    SystemGenerators_ReferenceGeneration = plx_enums.PropertyIDEnum.SystemGenerators_ReferenceGeneration

    SystemGenerators_LoadSubtracter = plx_enums.PropertyIDEnum.SystemGenerators_LoadSubtracter

    SystemGenerators_PriceFollowing = plx_enums.PropertyIDEnum.SystemGenerators_PriceFollowing

    SystemGenerators_LoadFollowingProfile = plx_enums.PropertyIDEnum.SystemGenerators_LoadFollowingProfile

    SystemGenerators_LoadFollowingFactor = plx_enums.PropertyIDEnum.SystemGenerators_LoadFollowingFactor

    SystemGenerators_BoilerEfficiency = plx_enums.PropertyIDEnum.SystemGenerators_BoilerEfficiency

    SystemGenerators_HeatLoad = plx_enums.PropertyIDEnum.SystemGenerators_HeatLoad

    SystemGenerators_PowertoHeatRatio = plx_enums.PropertyIDEnum.SystemGenerators_PowertoHeatRatio

    SystemGenerators_CHPElectricHeatRateIncr = plx_enums.PropertyIDEnum.SystemGenerators_CHPElectricHeatRateIncr

    SystemGenerators_CHPHeatSurrogateRateIncr = plx_enums.PropertyIDEnum.SystemGenerators_CHPHeatSurrogateRateIncr

    SystemGenerators_BoilerHeatRateIncr = plx_enums.PropertyIDEnum.SystemGenerators_BoilerHeatRateIncr

    SystemGenerators_MaxBoilerHeat = plx_enums.PropertyIDEnum.SystemGenerators_MaxBoilerHeat

    SystemGenerators_MaxHeat = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeat

    SystemGenerators_MinHeat = plx_enums.PropertyIDEnum.SystemGenerators_MinHeat

    SystemGenerators_OpeningHeat = plx_enums.PropertyIDEnum.SystemGenerators_OpeningHeat

    SystemGenerators_HeatWithdrawalCharge = plx_enums.PropertyIDEnum.SystemGenerators_HeatWithdrawalCharge

    SystemGenerators_HeatInjectionCharge = plx_enums.PropertyIDEnum.SystemGenerators_HeatInjectionCharge

    SystemGenerators_FixedCharge = plx_enums.PropertyIDEnum.SystemGenerators_FixedCharge

    SystemGenerators_HeatLoss = plx_enums.PropertyIDEnum.SystemGenerators_HeatLoss

    SystemGenerators_WaterOfftake = plx_enums.PropertyIDEnum.SystemGenerators_WaterOfftake

    SystemGenerators_WaterConsumption = plx_enums.PropertyIDEnum.SystemGenerators_WaterConsumption

    SystemGenerators_MaxRelease = plx_enums.PropertyIDEnum.SystemGenerators_MaxRelease

    SystemGenerators_MaxEnergy = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergy

    SystemGenerators_MaxEnergyHour = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergyHour

    SystemGenerators_MaxEnergyDay = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergyDay

    SystemGenerators_MaxEnergyWeek = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergyWeek

    SystemGenerators_MaxEnergyMonth = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergyMonth

    SystemGenerators_MaxEnergyYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergyYear

    SystemGenerators_MinEnergy = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergy

    SystemGenerators_MinEnergyHour = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergyHour

    SystemGenerators_MinEnergyDay = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergyDay

    SystemGenerators_MinEnergyWeek = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergyWeek

    SystemGenerators_MinEnergyMonth = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergyMonth

    SystemGenerators_MinEnergyYear = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergyYear

    SystemGenerators_MaxCapacityFactor = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacityFactor

    SystemGenerators_MaxCapacityFactorHour = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacityFactorHour

    SystemGenerators_MaxCapacityFactorDay = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacityFactorDay

    SystemGenerators_MaxCapacityFactorWeek = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacityFactorWeek

    SystemGenerators_MaxCapacityFactorMonth = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacityFactorMonth

    SystemGenerators_MaxCapacityFactorYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxCapacityFactorYear

    SystemGenerators_MinCapacityFactor = plx_enums.PropertyIDEnum.SystemGenerators_MinCapacityFactor

    SystemGenerators_MinCapacityFactorHour = plx_enums.PropertyIDEnum.SystemGenerators_MinCapacityFactorHour

    SystemGenerators_MinCapacityFactorDay = plx_enums.PropertyIDEnum.SystemGenerators_MinCapacityFactorDay

    SystemGenerators_MinCapacityFactorWeek = plx_enums.PropertyIDEnum.SystemGenerators_MinCapacityFactorWeek

    SystemGenerators_MinCapacityFactorMonth = plx_enums.PropertyIDEnum.SystemGenerators_MinCapacityFactorMonth

    SystemGenerators_MinCapacityFactorYear = plx_enums.PropertyIDEnum.SystemGenerators_MinCapacityFactorYear

    SystemGenerators_MaxEnergyPenalty = plx_enums.PropertyIDEnum.SystemGenerators_MaxEnergyPenalty

    SystemGenerators_MinEnergyPenalty = plx_enums.PropertyIDEnum.SystemGenerators_MinEnergyPenalty

    SystemGenerators_MaxStarts = plx_enums.PropertyIDEnum.SystemGenerators_MaxStarts

    SystemGenerators_MaxStartsHour = plx_enums.PropertyIDEnum.SystemGenerators_MaxStartsHour

    SystemGenerators_MaxStartsDay = plx_enums.PropertyIDEnum.SystemGenerators_MaxStartsDay

    SystemGenerators_MaxStartsWeek = plx_enums.PropertyIDEnum.SystemGenerators_MaxStartsWeek

    SystemGenerators_MaxStartsMonth = plx_enums.PropertyIDEnum.SystemGenerators_MaxStartsMonth

    SystemGenerators_MaxStartsYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxStartsYear

    SystemGenerators_MaxStartsPenalty = plx_enums.PropertyIDEnum.SystemGenerators_MaxStartsPenalty

    SystemGenerators_EnergyScalar = plx_enums.PropertyIDEnum.SystemGenerators_EnergyScalar

    SystemGenerators_MaxHeatWithdrawal = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatWithdrawal

    SystemGenerators_MaxHeatWithdrawalHour = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatWithdrawalHour

    SystemGenerators_MaxHeatWithdrawalDay = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatWithdrawalDay

    SystemGenerators_MaxHeatWithdrawalWeek = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatWithdrawalWeek

    SystemGenerators_MaxHeatWithdrawalMonth = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatWithdrawalMonth

    SystemGenerators_MaxHeatWithdrawalYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatWithdrawalYear

    SystemGenerators_MaxHeatInjection = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatInjection

    SystemGenerators_MaxHeatInjectionHour = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatInjectionHour

    SystemGenerators_MaxHeatInjectionDay = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatInjectionDay

    SystemGenerators_MaxHeatInjectionWeek = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatInjectionWeek

    SystemGenerators_MaxHeatInjectionMonth = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatInjectionMonth

    SystemGenerators_MaxHeatInjectionYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxHeatInjectionYear

    SystemGenerators_MinHeatWithdrawal = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatWithdrawal

    SystemGenerators_MinHeatWithdrawalHour = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatWithdrawalHour

    SystemGenerators_MinHeatWithdrawalDay = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatWithdrawalDay

    SystemGenerators_MinHeatWithdrawalWeek = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatWithdrawalWeek

    SystemGenerators_MinHeatWithdrawalMonth = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatWithdrawalMonth

    SystemGenerators_MinHeatWithdrawalYear = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatWithdrawalYear

    SystemGenerators_MinHeatInjection = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatInjection

    SystemGenerators_MinHeatInjectionHour = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatInjectionHour

    SystemGenerators_MinHeatInjectionDay = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatInjectionDay

    SystemGenerators_MinHeatInjectionWeek = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatInjectionWeek

    SystemGenerators_MinHeatInjectionMonth = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatInjectionMonth

    SystemGenerators_MinHeatInjectionYear = plx_enums.PropertyIDEnum.SystemGenerators_MinHeatInjectionYear

    SystemGenerators_OfferBase = plx_enums.PropertyIDEnum.SystemGenerators_OfferBase

    SystemGenerators_OfferNoLoadCost = plx_enums.PropertyIDEnum.SystemGenerators_OfferNoLoadCost

    SystemGenerators_OfferQuantity = plx_enums.PropertyIDEnum.SystemGenerators_OfferQuantity

    SystemGenerators_OfferPrice = plx_enums.PropertyIDEnum.SystemGenerators_OfferPrice

    SystemGenerators_OfferQuantityScalar = plx_enums.PropertyIDEnum.SystemGenerators_OfferQuantityScalar

    SystemGenerators_OfferPriceIncr = plx_enums.PropertyIDEnum.SystemGenerators_OfferPriceIncr

    SystemGenerators_OfferPriceScalar = plx_enums.PropertyIDEnum.SystemGenerators_OfferPriceScalar

    SystemGenerators_Markup = plx_enums.PropertyIDEnum.SystemGenerators_Markup

    SystemGenerators_BidCostMarkup = plx_enums.PropertyIDEnum.SystemGenerators_BidCostMarkup

    SystemGenerators_MarkupPoint = plx_enums.PropertyIDEnum.SystemGenerators_MarkupPoint

    SystemGenerators_PumpBidBase = plx_enums.PropertyIDEnum.SystemGenerators_PumpBidBase

    SystemGenerators_PumpBidQuantity = plx_enums.PropertyIDEnum.SystemGenerators_PumpBidQuantity

    SystemGenerators_PumpBidPrice = plx_enums.PropertyIDEnum.SystemGenerators_PumpBidPrice

    SystemGenerators_PumpBidQuantityScalar = plx_enums.PropertyIDEnum.SystemGenerators_PumpBidQuantityScalar

    SystemGenerators_PumpBidPriceIncr = plx_enums.PropertyIDEnum.SystemGenerators_PumpBidPriceIncr

    SystemGenerators_PumpBidPriceScalar = plx_enums.PropertyIDEnum.SystemGenerators_PumpBidPriceScalar

    SystemGenerators_StrategicRating = plx_enums.PropertyIDEnum.SystemGenerators_StrategicRating

    SystemGenerators_StrategicReferencePrice = plx_enums.PropertyIDEnum.SystemGenerators_StrategicReferencePrice

    SystemGenerators_InitialAge = plx_enums.PropertyIDEnum.SystemGenerators_InitialAge

    SystemGenerators_PowerDegradation = plx_enums.PropertyIDEnum.SystemGenerators_PowerDegradation

    SystemGenerators_CapacityDegradation = plx_enums.PropertyIDEnum.SystemGenerators_CapacityDegradation

    SystemGenerators_FOMCharge = plx_enums.PropertyIDEnum.SystemGenerators_FOMCharge

    SystemGenerators_EquityCharge = plx_enums.PropertyIDEnum.SystemGenerators_EquityCharge

    SystemGenerators_DebtCharge = plx_enums.PropertyIDEnum.SystemGenerators_DebtCharge

    SystemGenerators_FirmCapacity = plx_enums.PropertyIDEnum.SystemGenerators_FirmCapacity

    SystemGenerators_UnitsOut = plx_enums.PropertyIDEnum.SystemGenerators_UnitsOut

    SystemGenerators_Maintenance = plx_enums.PropertyIDEnum.SystemGenerators_Maintenance

    SystemGenerators_ForcedOutage = plx_enums.PropertyIDEnum.SystemGenerators_ForcedOutage

    SystemGenerators_MaintenanceRate = plx_enums.PropertyIDEnum.SystemGenerators_MaintenanceRate

    SystemGenerators_MaintenanceFrequency = plx_enums.PropertyIDEnum.SystemGenerators_MaintenanceFrequency

    SystemGenerators_ForcedOutageRate = plx_enums.PropertyIDEnum.SystemGenerators_ForcedOutageRate

    SystemGenerators_OutageFactor = plx_enums.PropertyIDEnum.SystemGenerators_OutageFactor

    SystemGenerators_OutageRating = plx_enums.PropertyIDEnum.SystemGenerators_OutageRating

    SystemGenerators_OutagePumpLoad = plx_enums.PropertyIDEnum.SystemGenerators_OutagePumpLoad

    SystemGenerators_InitialOperatingHours = plx_enums.PropertyIDEnum.SystemGenerators_InitialOperatingHours

    SystemGenerators_MeanTimetoRepair = plx_enums.PropertyIDEnum.SystemGenerators_MeanTimetoRepair

    SystemGenerators_MinTimeToRepair = plx_enums.PropertyIDEnum.SystemGenerators_MinTimeToRepair

    SystemGenerators_MaxTimeToRepair = plx_enums.PropertyIDEnum.SystemGenerators_MaxTimeToRepair

    SystemGenerators_RepairTimeShape = plx_enums.PropertyIDEnum.SystemGenerators_RepairTimeShape

    SystemGenerators_RepairTimeScale = plx_enums.PropertyIDEnum.SystemGenerators_RepairTimeScale

    SystemGenerators_BuildCost = plx_enums.PropertyIDEnum.SystemGenerators_BuildCost

    SystemGenerators_RetirementCost = plx_enums.PropertyIDEnum.SystemGenerators_RetirementCost

    SystemGenerators_OnetimeCost = plx_enums.PropertyIDEnum.SystemGenerators_OnetimeCost

    SystemGenerators_LeadTime = plx_enums.PropertyIDEnum.SystemGenerators_LeadTime

    SystemGenerators_ProjectStartDate = plx_enums.PropertyIDEnum.SystemGenerators_ProjectStartDate

    SystemGenerators_CommissionDate = plx_enums.PropertyIDEnum.SystemGenerators_CommissionDate

    SystemGenerators_TechnicalLife = plx_enums.PropertyIDEnum.SystemGenerators_TechnicalLife

    SystemGenerators_WACC = plx_enums.PropertyIDEnum.SystemGenerators_WACC

    SystemGenerators_EconomicLife = plx_enums.PropertyIDEnum.SystemGenerators_EconomicLife

    SystemGenerators_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemGenerators_MaxUnitsBuilt

    SystemGenerators_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemGenerators_MaxUnitsRetired

    SystemGenerators_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemGenerators_MinUnitsBuilt

    SystemGenerators_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemGenerators_MinUnitsRetired

    SystemGenerators_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxUnitsBuiltinYear

    SystemGenerators_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGenerators_MaxUnitsRetiredinYear

    SystemGenerators_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGenerators_MinUnitsBuiltinYear

    SystemGenerators_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGenerators_MinUnitsRetiredinYear

    SystemGenerators_BuildSetSize = plx_enums.PropertyIDEnum.SystemGenerators_BuildSetSize

    SystemGenerators_CapacityPrice = plx_enums.PropertyIDEnum.SystemGenerators_CapacityPrice

    SystemGenerators_UnitCommitmentNonanticipativity = plx_enums.PropertyIDEnum.SystemGenerators_UnitCommitmentNonanticipativity

    SystemGenerators_UnitCommitmentNonanticipativityTime = plx_enums.PropertyIDEnum.SystemGenerators_UnitCommitmentNonanticipativityTime

    SystemGenerators_PumpUnitCommitmentNonanticipativity = plx_enums.PropertyIDEnum.SystemGenerators_PumpUnitCommitmentNonanticipativity

    SystemGenerators_PumpUnitCommitmentNonanticipativityTime = plx_enums.PropertyIDEnum.SystemGenerators_PumpUnitCommitmentNonanticipativityTime

    SystemGenerators_GenerationNonanticipativity = plx_enums.PropertyIDEnum.SystemGenerators_GenerationNonanticipativity

    SystemGenerators_GenerationNonanticipativityTime = plx_enums.PropertyIDEnum.SystemGenerators_GenerationNonanticipativityTime

    SystemGenerators_PumpLoadNonanticipativity = plx_enums.PropertyIDEnum.SystemGenerators_PumpLoadNonanticipativity

    SystemGenerators_PumpLoadNonanticipativityTime = plx_enums.PropertyIDEnum.SystemGenerators_PumpLoadNonanticipativityTime

    SystemGenerators_BuildNonanticipativity = plx_enums.PropertyIDEnum.SystemGenerators_BuildNonanticipativity

    SystemGenerators_RetireNonanticipativity = plx_enums.PropertyIDEnum.SystemGenerators_RetireNonanticipativity

    SystemGenerators_x = plx_enums.PropertyIDEnum.SystemGenerators_x

    SystemGenerators_y = plx_enums.PropertyIDEnum.SystemGenerators_y

    SystemGenerators_z = plx_enums.PropertyIDEnum.SystemGenerators_z

    SystemFuels_BalancePeriod = plx_enums.PropertyIDEnum.SystemFuels_BalancePeriod

    SystemFuels_DecompositionMethod = plx_enums.PropertyIDEnum.SystemFuels_DecompositionMethod

    SystemFuels_DecompositionPenaltya = plx_enums.PropertyIDEnum.SystemFuels_DecompositionPenaltya

    SystemFuels_DecompositionPenaltyb = plx_enums.PropertyIDEnum.SystemFuels_DecompositionPenaltyb

    SystemFuels_DecompositionPenaltyc = plx_enums.PropertyIDEnum.SystemFuels_DecompositionPenaltyc

    SystemFuels_DecompositionPenaltyx = plx_enums.PropertyIDEnum.SystemFuels_DecompositionPenaltyx

    SystemFuels_DecompositionBoundPenalty = plx_enums.PropertyIDEnum.SystemFuels_DecompositionBoundPenalty

    SystemFuels_Units = plx_enums.PropertyIDEnum.SystemFuels_Units

    SystemFuels_Price = plx_enums.PropertyIDEnum.SystemFuels_Price

    SystemFuels_Tax = plx_enums.PropertyIDEnum.SystemFuels_Tax

    SystemFuels_PriceIncr = plx_enums.PropertyIDEnum.SystemFuels_PriceIncr

    SystemFuels_PriceScalar = plx_enums.PropertyIDEnum.SystemFuels_PriceScalar

    SystemFuels_HeatValue = plx_enums.PropertyIDEnum.SystemFuels_HeatValue

    SystemFuels_MaxOfftake = plx_enums.PropertyIDEnum.SystemFuels_MaxOfftake

    SystemFuels_MaxOfftakeHour = plx_enums.PropertyIDEnum.SystemFuels_MaxOfftakeHour

    SystemFuels_MaxOfftakeDay = plx_enums.PropertyIDEnum.SystemFuels_MaxOfftakeDay

    SystemFuels_MaxOfftakeWeek = plx_enums.PropertyIDEnum.SystemFuels_MaxOfftakeWeek

    SystemFuels_MaxOfftakeMonth = plx_enums.PropertyIDEnum.SystemFuels_MaxOfftakeMonth

    SystemFuels_MaxOfftakeYear = plx_enums.PropertyIDEnum.SystemFuels_MaxOfftakeYear

    SystemFuels_MinOfftake = plx_enums.PropertyIDEnum.SystemFuels_MinOfftake

    SystemFuels_MinOfftakeHour = plx_enums.PropertyIDEnum.SystemFuels_MinOfftakeHour

    SystemFuels_MinOfftakeDay = plx_enums.PropertyIDEnum.SystemFuels_MinOfftakeDay

    SystemFuels_MinOfftakeWeek = plx_enums.PropertyIDEnum.SystemFuels_MinOfftakeWeek

    SystemFuels_MinOfftakeMonth = plx_enums.PropertyIDEnum.SystemFuels_MinOfftakeMonth

    SystemFuels_MinOfftakeYear = plx_enums.PropertyIDEnum.SystemFuels_MinOfftakeYear

    SystemFuels_ShadowPrice = plx_enums.PropertyIDEnum.SystemFuels_ShadowPrice

    SystemFuels_ShadowPriceIncr = plx_enums.PropertyIDEnum.SystemFuels_ShadowPriceIncr

    SystemFuels_ShadowPriceScalar = plx_enums.PropertyIDEnum.SystemFuels_ShadowPriceScalar

    SystemFuels_MaxInventory = plx_enums.PropertyIDEnum.SystemFuels_MaxInventory

    SystemFuels_MinInventory = plx_enums.PropertyIDEnum.SystemFuels_MinInventory

    SystemFuels_OpeningInventory = plx_enums.PropertyIDEnum.SystemFuels_OpeningInventory

    SystemFuels_Delivery = plx_enums.PropertyIDEnum.SystemFuels_Delivery

    SystemFuels_DeliveryCharge = plx_enums.PropertyIDEnum.SystemFuels_DeliveryCharge

    SystemFuels_InventoryCharge = plx_enums.PropertyIDEnum.SystemFuels_InventoryCharge

    SystemFuels_ReservationCharge = plx_enums.PropertyIDEnum.SystemFuels_ReservationCharge

    SystemFuels_WithdrawalCharge = plx_enums.PropertyIDEnum.SystemFuels_WithdrawalCharge

    SystemFuels_MaxWithdrawal = plx_enums.PropertyIDEnum.SystemFuels_MaxWithdrawal

    SystemFuels_MaxWithdrawalHour = plx_enums.PropertyIDEnum.SystemFuels_MaxWithdrawalHour

    SystemFuels_MaxWithdrawalDay = plx_enums.PropertyIDEnum.SystemFuels_MaxWithdrawalDay

    SystemFuels_MaxWithdrawalWeek = plx_enums.PropertyIDEnum.SystemFuels_MaxWithdrawalWeek

    SystemFuels_MaxWithdrawalMonth = plx_enums.PropertyIDEnum.SystemFuels_MaxWithdrawalMonth

    SystemFuels_MaxWithdrawalYear = plx_enums.PropertyIDEnum.SystemFuels_MaxWithdrawalYear

    SystemFuels_MinWithdrawal = plx_enums.PropertyIDEnum.SystemFuels_MinWithdrawal

    SystemFuels_MinWithdrawalHour = plx_enums.PropertyIDEnum.SystemFuels_MinWithdrawalHour

    SystemFuels_MinWithdrawalDay = plx_enums.PropertyIDEnum.SystemFuels_MinWithdrawalDay

    SystemFuels_MinWithdrawalWeek = plx_enums.PropertyIDEnum.SystemFuels_MinWithdrawalWeek

    SystemFuels_MinWithdrawalMonth = plx_enums.PropertyIDEnum.SystemFuels_MinWithdrawalMonth

    SystemFuels_MinWithdrawalYear = plx_enums.PropertyIDEnum.SystemFuels_MinWithdrawalYear

    SystemFuels_FOMCharge = plx_enums.PropertyIDEnum.SystemFuels_FOMCharge

    SystemFuels_x = plx_enums.PropertyIDEnum.SystemFuels_x

    SystemFuels_y = plx_enums.PropertyIDEnum.SystemFuels_y

    SystemFuels_z = plx_enums.PropertyIDEnum.SystemFuels_z

    SystemFuelContracts_Quantity = plx_enums.PropertyIDEnum.SystemFuelContracts_Quantity

    SystemFuelContracts_QuantityHour = plx_enums.PropertyIDEnum.SystemFuelContracts_QuantityHour

    SystemFuelContracts_QuantityDay = plx_enums.PropertyIDEnum.SystemFuelContracts_QuantityDay

    SystemFuelContracts_QuantityWeek = plx_enums.PropertyIDEnum.SystemFuelContracts_QuantityWeek

    SystemFuelContracts_QuantityMonth = plx_enums.PropertyIDEnum.SystemFuelContracts_QuantityMonth

    SystemFuelContracts_QuantityYear = plx_enums.PropertyIDEnum.SystemFuelContracts_QuantityYear

    SystemFuelContracts_Price = plx_enums.PropertyIDEnum.SystemFuelContracts_Price

    SystemFuelContracts_PriceIncr = plx_enums.PropertyIDEnum.SystemFuelContracts_PriceIncr

    SystemFuelContracts_PriceScalar = plx_enums.PropertyIDEnum.SystemFuelContracts_PriceScalar

    SystemFuelContracts_TakeorPayQuantity = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayQuantity

    SystemFuelContracts_TakeorPayQuantityHour = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayQuantityHour

    SystemFuelContracts_TakeorPayQuantityDay = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayQuantityDay

    SystemFuelContracts_TakeorPayQuantityWeek = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayQuantityWeek

    SystemFuelContracts_TakeorPayQuantityMonth = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayQuantityMonth

    SystemFuelContracts_TakeorPayQuantityYear = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayQuantityYear

    SystemFuelContracts_TakeorPayPrice = plx_enums.PropertyIDEnum.SystemFuelContracts_TakeorPayPrice

    SystemFuelContracts_FOMCharge = plx_enums.PropertyIDEnum.SystemFuelContracts_FOMCharge

    SystemFuelContracts_x = plx_enums.PropertyIDEnum.SystemFuelContracts_x

    SystemFuelContracts_y = plx_enums.PropertyIDEnum.SystemFuelContracts_y

    SystemFuelContracts_z = plx_enums.PropertyIDEnum.SystemFuelContracts_z

    SystemEmissions_Price = plx_enums.PropertyIDEnum.SystemEmissions_Price

    SystemEmissions_MaxProduction = plx_enums.PropertyIDEnum.SystemEmissions_MaxProduction

    SystemEmissions_MaxProductionHour = plx_enums.PropertyIDEnum.SystemEmissions_MaxProductionHour

    SystemEmissions_MaxProductionDay = plx_enums.PropertyIDEnum.SystemEmissions_MaxProductionDay

    SystemEmissions_MaxProductionWeek = plx_enums.PropertyIDEnum.SystemEmissions_MaxProductionWeek

    SystemEmissions_MaxProductionMonth = plx_enums.PropertyIDEnum.SystemEmissions_MaxProductionMonth

    SystemEmissions_MaxProductionYear = plx_enums.PropertyIDEnum.SystemEmissions_MaxProductionYear

    SystemEmissions_MaxProductionPenalty = plx_enums.PropertyIDEnum.SystemEmissions_MaxProductionPenalty

    SystemEmissions_ShadowPrice = plx_enums.PropertyIDEnum.SystemEmissions_ShadowPrice

    SystemEmissions_x = plx_enums.PropertyIDEnum.SystemEmissions_x

    SystemEmissions_y = plx_enums.PropertyIDEnum.SystemEmissions_y

    SystemEmissions_z = plx_enums.PropertyIDEnum.SystemEmissions_z

    SystemAbatements_Units = plx_enums.PropertyIDEnum.SystemAbatements_Units

    SystemAbatements_AbatementCost = plx_enums.PropertyIDEnum.SystemAbatements_AbatementCost

    SystemAbatements_RunningCost = plx_enums.PropertyIDEnum.SystemAbatements_RunningCost

    SystemAbatements_VOMCharge = plx_enums.PropertyIDEnum.SystemAbatements_VOMCharge

    SystemAbatements_Efficiency = plx_enums.PropertyIDEnum.SystemAbatements_Efficiency

    SystemAbatements_MaxAbatement = plx_enums.PropertyIDEnum.SystemAbatements_MaxAbatement

    SystemAbatements_FOMCharge = plx_enums.PropertyIDEnum.SystemAbatements_FOMCharge

    SystemAbatements_UnitsOut = plx_enums.PropertyIDEnum.SystemAbatements_UnitsOut

    SystemAbatements_x = plx_enums.PropertyIDEnum.SystemAbatements_x

    SystemAbatements_y = plx_enums.PropertyIDEnum.SystemAbatements_y

    SystemAbatements_z = plx_enums.PropertyIDEnum.SystemAbatements_z

    SystemStorages_Model = plx_enums.PropertyIDEnum.SystemStorages_Model

    SystemStorages_BalancePeriod = plx_enums.PropertyIDEnum.SystemStorages_BalancePeriod

    SystemStorages_InternalVolumeScalar = plx_enums.PropertyIDEnum.SystemStorages_InternalVolumeScalar

    SystemStorages_EndEffectsMethod = plx_enums.PropertyIDEnum.SystemStorages_EndEffectsMethod

    SystemStorages_RecyclePenalty = plx_enums.PropertyIDEnum.SystemStorages_RecyclePenalty

    SystemStorages_DecompositionMethod = plx_enums.PropertyIDEnum.SystemStorages_DecompositionMethod

    SystemStorages_DecompositionPenaltya = plx_enums.PropertyIDEnum.SystemStorages_DecompositionPenaltya

    SystemStorages_DecompositionPenaltyb = plx_enums.PropertyIDEnum.SystemStorages_DecompositionPenaltyb

    SystemStorages_DecompositionPenaltyc = plx_enums.PropertyIDEnum.SystemStorages_DecompositionPenaltyc

    SystemStorages_DecompositionPenaltyx = plx_enums.PropertyIDEnum.SystemStorages_DecompositionPenaltyx

    SystemStorages_DecompositionBoundPenalty = plx_enums.PropertyIDEnum.SystemStorages_DecompositionBoundPenalty

    SystemStorages_EnforceBounds = plx_enums.PropertyIDEnum.SystemStorages_EnforceBounds

    SystemStorages_SpillPenalty = plx_enums.PropertyIDEnum.SystemStorages_SpillPenalty

    SystemStorages_NonphysicalInflowPenalty = plx_enums.PropertyIDEnum.SystemStorages_NonphysicalInflowPenalty

    SystemStorages_NonphysicalSpillPenalty = plx_enums.PropertyIDEnum.SystemStorages_NonphysicalSpillPenalty

    SystemStorages_Units = plx_enums.PropertyIDEnum.SystemStorages_Units

    SystemStorages_MaxVolume = plx_enums.PropertyIDEnum.SystemStorages_MaxVolume

    SystemStorages_InitialVolume = plx_enums.PropertyIDEnum.SystemStorages_InitialVolume

    SystemStorages_MinVolume = plx_enums.PropertyIDEnum.SystemStorages_MinVolume

    SystemStorages_MaxLevel = plx_enums.PropertyIDEnum.SystemStorages_MaxLevel

    SystemStorages_InitialLevel = plx_enums.PropertyIDEnum.SystemStorages_InitialLevel

    SystemStorages_MinLevel = plx_enums.PropertyIDEnum.SystemStorages_MinLevel

    SystemStorages_LowRefLevel = plx_enums.PropertyIDEnum.SystemStorages_LowRefLevel

    SystemStorages_LowRefArea = plx_enums.PropertyIDEnum.SystemStorages_LowRefArea

    SystemStorages_HighRefLevel = plx_enums.PropertyIDEnum.SystemStorages_HighRefLevel

    SystemStorages_HighRefArea = plx_enums.PropertyIDEnum.SystemStorages_HighRefArea

    SystemStorages_NaturalInflow = plx_enums.PropertyIDEnum.SystemStorages_NaturalInflow

    SystemStorages_NaturalInflowIncr = plx_enums.PropertyIDEnum.SystemStorages_NaturalInflowIncr

    SystemStorages_NaturalInflowScalar = plx_enums.PropertyIDEnum.SystemStorages_NaturalInflowScalar

    SystemStorages_WaterValue = plx_enums.PropertyIDEnum.SystemStorages_WaterValue

    SystemStorages_EnergyValue = plx_enums.PropertyIDEnum.SystemStorages_EnergyValue

    SystemStorages_WaterValuePoint = plx_enums.PropertyIDEnum.SystemStorages_WaterValuePoint

    SystemStorages_DownstreamEfficiency = plx_enums.PropertyIDEnum.SystemStorages_DownstreamEfficiency

    SystemStorages_LossRate = plx_enums.PropertyIDEnum.SystemStorages_LossRate

    SystemStorages_MinRelease = plx_enums.PropertyIDEnum.SystemStorages_MinRelease

    SystemStorages_MaxRelease = plx_enums.PropertyIDEnum.SystemStorages_MaxRelease

    SystemStorages_MaxGeneratorRelease = plx_enums.PropertyIDEnum.SystemStorages_MaxGeneratorRelease

    SystemStorages_MinReleasePenalty = plx_enums.PropertyIDEnum.SystemStorages_MinReleasePenalty

    SystemStorages_MaxReleasePenalty = plx_enums.PropertyIDEnum.SystemStorages_MaxReleasePenalty

    SystemStorages_MaxSpill = plx_enums.PropertyIDEnum.SystemStorages_MaxSpill

    SystemStorages_MaxRamp = plx_enums.PropertyIDEnum.SystemStorages_MaxRamp

    SystemStorages_MaxRampHour = plx_enums.PropertyIDEnum.SystemStorages_MaxRampHour

    SystemStorages_MaxRampDay = plx_enums.PropertyIDEnum.SystemStorages_MaxRampDay

    SystemStorages_MaxRampWeek = plx_enums.PropertyIDEnum.SystemStorages_MaxRampWeek

    SystemStorages_MaxRampMonth = plx_enums.PropertyIDEnum.SystemStorages_MaxRampMonth

    SystemStorages_MaxRampYear = plx_enums.PropertyIDEnum.SystemStorages_MaxRampYear

    SystemStorages_MaxRampPenalty = plx_enums.PropertyIDEnum.SystemStorages_MaxRampPenalty

    SystemStorages_Target = plx_enums.PropertyIDEnum.SystemStorages_Target

    SystemStorages_TargetHour = plx_enums.PropertyIDEnum.SystemStorages_TargetHour

    SystemStorages_TargetDay = plx_enums.PropertyIDEnum.SystemStorages_TargetDay

    SystemStorages_TargetWeek = plx_enums.PropertyIDEnum.SystemStorages_TargetWeek

    SystemStorages_TargetMonth = plx_enums.PropertyIDEnum.SystemStorages_TargetMonth

    SystemStorages_TargetYear = plx_enums.PropertyIDEnum.SystemStorages_TargetYear

    SystemStorages_TargetLevel = plx_enums.PropertyIDEnum.SystemStorages_TargetLevel

    SystemStorages_TargetLevelHour = plx_enums.PropertyIDEnum.SystemStorages_TargetLevelHour

    SystemStorages_TargetLevelDay = plx_enums.PropertyIDEnum.SystemStorages_TargetLevelDay

    SystemStorages_TargetLevelWeek = plx_enums.PropertyIDEnum.SystemStorages_TargetLevelWeek

    SystemStorages_TargetLevelMonth = plx_enums.PropertyIDEnum.SystemStorages_TargetLevelMonth

    SystemStorages_TargetLevelYear = plx_enums.PropertyIDEnum.SystemStorages_TargetLevelYear

    SystemStorages_TargetPenalty = plx_enums.PropertyIDEnum.SystemStorages_TargetPenalty

    SystemStorages_TrajectoryNonanticipativity = plx_enums.PropertyIDEnum.SystemStorages_TrajectoryNonanticipativity

    SystemStorages_TrajectoryNonanticipativityVolume = plx_enums.PropertyIDEnum.SystemStorages_TrajectoryNonanticipativityVolume

    SystemStorages_TrajectoryNonanticipativityTime = plx_enums.PropertyIDEnum.SystemStorages_TrajectoryNonanticipativityTime

    SystemStorages_x = plx_enums.PropertyIDEnum.SystemStorages_x

    SystemStorages_y = plx_enums.PropertyIDEnum.SystemStorages_y

    SystemStorages_z = plx_enums.PropertyIDEnum.SystemStorages_z

    SystemWaterways_TraversalTime = plx_enums.PropertyIDEnum.SystemWaterways_TraversalTime

    SystemWaterways_FlowControl = plx_enums.PropertyIDEnum.SystemWaterways_FlowControl

    SystemWaterways_MaxFlow = plx_enums.PropertyIDEnum.SystemWaterways_MaxFlow

    SystemWaterways_MinFlow = plx_enums.PropertyIDEnum.SystemWaterways_MinFlow

    SystemWaterways_InitialFlow = plx_enums.PropertyIDEnum.SystemWaterways_InitialFlow

    SystemWaterways_MaxRamp = plx_enums.PropertyIDEnum.SystemWaterways_MaxRamp

    SystemWaterways_MaxFlowPenalty = plx_enums.PropertyIDEnum.SystemWaterways_MaxFlowPenalty

    SystemWaterways_MinFlowPenalty = plx_enums.PropertyIDEnum.SystemWaterways_MinFlowPenalty

    SystemWaterways_MaxRampPenalty = plx_enums.PropertyIDEnum.SystemWaterways_MaxRampPenalty

    SystemWaterways_InputScalar = plx_enums.PropertyIDEnum.SystemWaterways_InputScalar

    SystemWaterways_OutputScalar = plx_enums.PropertyIDEnum.SystemWaterways_OutputScalar

    SystemWaterways_x = plx_enums.PropertyIDEnum.SystemWaterways_x

    SystemWaterways_y = plx_enums.PropertyIDEnum.SystemWaterways_y

    SystemWaterways_z = plx_enums.PropertyIDEnum.SystemWaterways_z

    SystemPowerStations_IsEnabled = plx_enums.PropertyIDEnum.SystemPowerStations_IsEnabled

    SystemPhysicalContracts_OfferQuantityFormat = plx_enums.PropertyIDEnum.SystemPhysicalContracts_OfferQuantityFormat

    SystemPhysicalContracts_PriceSetting = plx_enums.PropertyIDEnum.SystemPhysicalContracts_PriceSetting

    SystemPhysicalContracts_Units = plx_enums.PropertyIDEnum.SystemPhysicalContracts_Units

    SystemPhysicalContracts_MaxGeneration = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MaxGeneration

    SystemPhysicalContracts_MaxLoad = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MaxLoad

    SystemPhysicalContracts_MinGeneration = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MinGeneration

    SystemPhysicalContracts_MinLoad = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MinLoad

    SystemPhysicalContracts_OfferQuantity = plx_enums.PropertyIDEnum.SystemPhysicalContracts_OfferQuantity

    SystemPhysicalContracts_OfferPrice = plx_enums.PropertyIDEnum.SystemPhysicalContracts_OfferPrice

    SystemPhysicalContracts_BidQuantity = plx_enums.PropertyIDEnum.SystemPhysicalContracts_BidQuantity

    SystemPhysicalContracts_BidPrice = plx_enums.PropertyIDEnum.SystemPhysicalContracts_BidPrice

    SystemPhysicalContracts_FirmCapacity = plx_enums.PropertyIDEnum.SystemPhysicalContracts_FirmCapacity

    SystemPhysicalContracts_LoadObligation = plx_enums.PropertyIDEnum.SystemPhysicalContracts_LoadObligation

    SystemPhysicalContracts_CapacityCharge = plx_enums.PropertyIDEnum.SystemPhysicalContracts_CapacityCharge

    SystemPhysicalContracts_CapacityChargeHour = plx_enums.PropertyIDEnum.SystemPhysicalContracts_CapacityChargeHour

    SystemPhysicalContracts_CapacityChargeDay = plx_enums.PropertyIDEnum.SystemPhysicalContracts_CapacityChargeDay

    SystemPhysicalContracts_CapacityChargeWeek = plx_enums.PropertyIDEnum.SystemPhysicalContracts_CapacityChargeWeek

    SystemPhysicalContracts_CapacityChargeMonth = plx_enums.PropertyIDEnum.SystemPhysicalContracts_CapacityChargeMonth

    SystemPhysicalContracts_CapacityChargeYear = plx_enums.PropertyIDEnum.SystemPhysicalContracts_CapacityChargeYear

    SystemPhysicalContracts_MaxGenerationUnits = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MaxGenerationUnits

    SystemPhysicalContracts_MaxLoadUnits = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MaxLoadUnits

    SystemPhysicalContracts_MinGenerationUnits = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MinGenerationUnits

    SystemPhysicalContracts_MinLoadUnits = plx_enums.PropertyIDEnum.SystemPhysicalContracts_MinLoadUnits

    SystemPhysicalContracts_BuildNonanticipativity = plx_enums.PropertyIDEnum.SystemPhysicalContracts_BuildNonanticipativity

    SystemPhysicalContracts_x = plx_enums.PropertyIDEnum.SystemPhysicalContracts_x

    SystemPhysicalContracts_y = plx_enums.PropertyIDEnum.SystemPhysicalContracts_y

    SystemPhysicalContracts_z = plx_enums.PropertyIDEnum.SystemPhysicalContracts_z

    SystemPurchasers_BenefitFunctionShape = plx_enums.PropertyIDEnum.SystemPurchasers_BenefitFunctionShape

    SystemPurchasers_MaxBenefitFunctionTranches = plx_enums.PropertyIDEnum.SystemPurchasers_MaxBenefitFunctionTranches

    SystemPurchasers_InterruptibleLoadLogic = plx_enums.PropertyIDEnum.SystemPurchasers_InterruptibleLoadLogic

    SystemPurchasers_PriceSetting = plx_enums.PropertyIDEnum.SystemPurchasers_PriceSetting

    SystemPurchasers_Units = plx_enums.PropertyIDEnum.SystemPurchasers_Units

    SystemPurchasers_MinLoad = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoad

    SystemPurchasers_MaxLoad = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoad

    SystemPurchasers_FixedLoad = plx_enums.PropertyIDEnum.SystemPurchasers_FixedLoad

    SystemPurchasers_MaxRampDown = plx_enums.PropertyIDEnum.SystemPurchasers_MaxRampDown

    SystemPurchasers_MaxRampUp = plx_enums.PropertyIDEnum.SystemPurchasers_MaxRampUp

    SystemPurchasers_MaxEnergy = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergy

    SystemPurchasers_MaxEnergyHour = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergyHour

    SystemPurchasers_MaxEnergyDay = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergyDay

    SystemPurchasers_MaxEnergyWeek = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergyWeek

    SystemPurchasers_MaxEnergyMonth = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergyMonth

    SystemPurchasers_MaxEnergyYear = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergyYear

    SystemPurchasers_MinEnergy = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergy

    SystemPurchasers_MinEnergyHour = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergyHour

    SystemPurchasers_MinEnergyDay = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergyDay

    SystemPurchasers_MinEnergyWeek = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergyWeek

    SystemPurchasers_MinEnergyMonth = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergyMonth

    SystemPurchasers_MinEnergyYear = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergyYear

    SystemPurchasers_MaxLoadFactor = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoadFactor

    SystemPurchasers_MaxLoadFactorHour = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoadFactorHour

    SystemPurchasers_MaxLoadFactorDay = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoadFactorDay

    SystemPurchasers_MaxLoadFactorWeek = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoadFactorWeek

    SystemPurchasers_MaxLoadFactorMonth = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoadFactorMonth

    SystemPurchasers_MaxLoadFactorYear = plx_enums.PropertyIDEnum.SystemPurchasers_MaxLoadFactorYear

    SystemPurchasers_MinLoadFactor = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoadFactor

    SystemPurchasers_MinLoadFactorHour = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoadFactorHour

    SystemPurchasers_MinLoadFactorDay = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoadFactorDay

    SystemPurchasers_MinLoadFactorWeek = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoadFactorWeek

    SystemPurchasers_MinLoadFactorMonth = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoadFactorMonth

    SystemPurchasers_MinLoadFactorYear = plx_enums.PropertyIDEnum.SystemPurchasers_MinLoadFactorYear

    SystemPurchasers_MaxEnergyPenalty = plx_enums.PropertyIDEnum.SystemPurchasers_MaxEnergyPenalty

    SystemPurchasers_MinEnergyPenalty = plx_enums.PropertyIDEnum.SystemPurchasers_MinEnergyPenalty

    SystemPurchasers_MarginalLossFactor = plx_enums.PropertyIDEnum.SystemPurchasers_MarginalLossFactor

    SystemPurchasers_BidQuantity = plx_enums.PropertyIDEnum.SystemPurchasers_BidQuantity

    SystemPurchasers_BidPrice = plx_enums.PropertyIDEnum.SystemPurchasers_BidPrice

    SystemPurchasers_Tariff = plx_enums.PropertyIDEnum.SystemPurchasers_Tariff

    SystemPurchasers_DemandFnSlope = plx_enums.PropertyIDEnum.SystemPurchasers_DemandFnSlope

    SystemPurchasers_DemandFnIntercept = plx_enums.PropertyIDEnum.SystemPurchasers_DemandFnIntercept

    SystemPurchasers_LoadObligation = plx_enums.PropertyIDEnum.SystemPurchasers_LoadObligation

    SystemPurchasers_x = plx_enums.PropertyIDEnum.SystemPurchasers_x

    SystemPurchasers_y = plx_enums.PropertyIDEnum.SystemPurchasers_y

    SystemPurchasers_z = plx_enums.PropertyIDEnum.SystemPurchasers_z

    SystemReserves_Type = plx_enums.PropertyIDEnum.SystemReserves_Type

    SystemReserves_MutuallyExclusive = plx_enums.PropertyIDEnum.SystemReserves_MutuallyExclusive

    SystemReserves_DynamicRisk = plx_enums.PropertyIDEnum.SystemReserves_DynamicRisk

    SystemReserves_CostAllocationModel = plx_enums.PropertyIDEnum.SystemReserves_CostAllocationModel

    SystemReserves_IsEnabled = plx_enums.PropertyIDEnum.SystemReserves_IsEnabled

    SystemReserves_IncludeinLTPlan = plx_enums.PropertyIDEnum.SystemReserves_IncludeinLTPlan

    SystemReserves_IncludeinMTSchedule = plx_enums.PropertyIDEnum.SystemReserves_IncludeinMTSchedule

    SystemReserves_IncludeinSTSchedule = plx_enums.PropertyIDEnum.SystemReserves_IncludeinSTSchedule

    SystemReserves_UnitCommitment = plx_enums.PropertyIDEnum.SystemReserves_UnitCommitment

    SystemReserves_SharingEnabled = plx_enums.PropertyIDEnum.SystemReserves_SharingEnabled

    SystemReserves_SharingLossesEnabled = plx_enums.PropertyIDEnum.SystemReserves_SharingLossesEnabled

    SystemReserves_MinProvision = plx_enums.PropertyIDEnum.SystemReserves_MinProvision

    SystemReserves_StaticRisk = plx_enums.PropertyIDEnum.SystemReserves_StaticRisk

    SystemReserves_Timeframe = plx_enums.PropertyIDEnum.SystemReserves_Timeframe

    SystemReserves_Duration = plx_enums.PropertyIDEnum.SystemReserves_Duration

    SystemReserves_MaxProvision = plx_enums.PropertyIDEnum.SystemReserves_MaxProvision

    SystemReserves_RiskAdjustmentFactor = plx_enums.PropertyIDEnum.SystemReserves_RiskAdjustmentFactor

    SystemReserves_EnergyUsage = plx_enums.PropertyIDEnum.SystemReserves_EnergyUsage

    SystemReserves_VoRS = plx_enums.PropertyIDEnum.SystemReserves_VoRS

    SystemReserves_PriceCap = plx_enums.PropertyIDEnum.SystemReserves_PriceCap

    SystemReserves_PriceFloor = plx_enums.PropertyIDEnum.SystemReserves_PriceFloor

    SystemReserves_CutoffSize = plx_enums.PropertyIDEnum.SystemReserves_CutoffSize

    SystemReserves_Price = plx_enums.PropertyIDEnum.SystemReserves_Price

    SystemReserves_x = plx_enums.PropertyIDEnum.SystemReserves_x

    SystemReserves_y = plx_enums.PropertyIDEnum.SystemReserves_y

    SystemReserves_z = plx_enums.PropertyIDEnum.SystemReserves_z

    SystemBatteries_RandomNumberSeed = plx_enums.PropertyIDEnum.SystemBatteries_RandomNumberSeed

    SystemBatteries_RepairTimeDistribution = plx_enums.PropertyIDEnum.SystemBatteries_RepairTimeDistribution

    SystemBatteries_EndEffectsMethod = plx_enums.PropertyIDEnum.SystemBatteries_EndEffectsMethod

    SystemBatteries_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemBatteries_ExpansionOptimality

    SystemBatteries_Units = plx_enums.PropertyIDEnum.SystemBatteries_Units

    SystemBatteries_Capacity = plx_enums.PropertyIDEnum.SystemBatteries_Capacity

    SystemBatteries_MaxPower = plx_enums.PropertyIDEnum.SystemBatteries_MaxPower

    SystemBatteries_MaxLoad = plx_enums.PropertyIDEnum.SystemBatteries_MaxLoad

    SystemBatteries_MaxSoC = plx_enums.PropertyIDEnum.SystemBatteries_MaxSoC

    SystemBatteries_MinSoC = plx_enums.PropertyIDEnum.SystemBatteries_MinSoC

    SystemBatteries_InitialSoC = plx_enums.PropertyIDEnum.SystemBatteries_InitialSoC

    SystemBatteries_ChargeEfficiency = plx_enums.PropertyIDEnum.SystemBatteries_ChargeEfficiency

    SystemBatteries_DischargeEfficiency = plx_enums.PropertyIDEnum.SystemBatteries_DischargeEfficiency

    SystemBatteries_VOMCharge = plx_enums.PropertyIDEnum.SystemBatteries_VOMCharge

    SystemBatteries_UoSCharge = plx_enums.PropertyIDEnum.SystemBatteries_UoSCharge

    SystemBatteries_MaxRampUp = plx_enums.PropertyIDEnum.SystemBatteries_MaxRampUp

    SystemBatteries_MaxRampUpPenalty = plx_enums.PropertyIDEnum.SystemBatteries_MaxRampUpPenalty

    SystemBatteries_MaxRampDown = plx_enums.PropertyIDEnum.SystemBatteries_MaxRampDown

    SystemBatteries_MaxRampDownPenalty = plx_enums.PropertyIDEnum.SystemBatteries_MaxRampDownPenalty

    SystemBatteries_MaxCycles = plx_enums.PropertyIDEnum.SystemBatteries_MaxCycles

    SystemBatteries_MaxCyclesHour = plx_enums.PropertyIDEnum.SystemBatteries_MaxCyclesHour

    SystemBatteries_MaxCyclesDay = plx_enums.PropertyIDEnum.SystemBatteries_MaxCyclesDay

    SystemBatteries_MaxCyclesWeek = plx_enums.PropertyIDEnum.SystemBatteries_MaxCyclesWeek

    SystemBatteries_MaxCyclesMonth = plx_enums.PropertyIDEnum.SystemBatteries_MaxCyclesMonth

    SystemBatteries_MaxCyclesYear = plx_enums.PropertyIDEnum.SystemBatteries_MaxCyclesYear

    SystemBatteries_EnergyTarget = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTarget

    SystemBatteries_EnergyTargetHour = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTargetHour

    SystemBatteries_EnergyTargetDay = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTargetDay

    SystemBatteries_EnergyTargetWeek = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTargetWeek

    SystemBatteries_EnergyTargetMonth = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTargetMonth

    SystemBatteries_EnergyTargetYear = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTargetYear

    SystemBatteries_EnergyTargetPenalty = plx_enums.PropertyIDEnum.SystemBatteries_EnergyTargetPenalty

    SystemBatteries_Nonanticipativity = plx_enums.PropertyIDEnum.SystemBatteries_Nonanticipativity

    SystemBatteries_NonanticipativityTime = plx_enums.PropertyIDEnum.SystemBatteries_NonanticipativityTime

    SystemBatteries_InitialAge = plx_enums.PropertyIDEnum.SystemBatteries_InitialAge

    SystemBatteries_PowerDegradation = plx_enums.PropertyIDEnum.SystemBatteries_PowerDegradation

    SystemBatteries_CapacityDegradation = plx_enums.PropertyIDEnum.SystemBatteries_CapacityDegradation

    SystemBatteries_FirmCapacity = plx_enums.PropertyIDEnum.SystemBatteries_FirmCapacity

    SystemBatteries_FOMCharge = plx_enums.PropertyIDEnum.SystemBatteries_FOMCharge

    SystemBatteries_MaintenanceRate = plx_enums.PropertyIDEnum.SystemBatteries_MaintenanceRate

    SystemBatteries_MaintenanceFrequency = plx_enums.PropertyIDEnum.SystemBatteries_MaintenanceFrequency

    SystemBatteries_ForcedOutageRate = plx_enums.PropertyIDEnum.SystemBatteries_ForcedOutageRate

    SystemBatteries_MeanTimetoRepair = plx_enums.PropertyIDEnum.SystemBatteries_MeanTimetoRepair

    SystemBatteries_MinTimeToRepair = plx_enums.PropertyIDEnum.SystemBatteries_MinTimeToRepair

    SystemBatteries_MaxTimeToRepair = plx_enums.PropertyIDEnum.SystemBatteries_MaxTimeToRepair

    SystemBatteries_RepairTimeShape = plx_enums.PropertyIDEnum.SystemBatteries_RepairTimeShape

    SystemBatteries_RepairTimeScale = plx_enums.PropertyIDEnum.SystemBatteries_RepairTimeScale

    SystemBatteries_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemBatteries_MaxUnitsBuilt

    SystemBatteries_LeadTime = plx_enums.PropertyIDEnum.SystemBatteries_LeadTime

    SystemBatteries_ProjectStartDate = plx_enums.PropertyIDEnum.SystemBatteries_ProjectStartDate

    SystemBatteries_TechnicalLife = plx_enums.PropertyIDEnum.SystemBatteries_TechnicalLife

    SystemBatteries_BuildCost = plx_enums.PropertyIDEnum.SystemBatteries_BuildCost

    SystemBatteries_WACC = plx_enums.PropertyIDEnum.SystemBatteries_WACC

    SystemBatteries_EconomicLife = plx_enums.PropertyIDEnum.SystemBatteries_EconomicLife

    SystemBatteries_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemBatteries_MinUnitsBuilt

    SystemBatteries_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemBatteries_MaxUnitsBuiltinYear

    SystemBatteries_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemBatteries_MinUnitsBuiltinYear

    SystemBatteries_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemBatteries_MaxUnitsRetired

    SystemBatteries_RetirementCost = plx_enums.PropertyIDEnum.SystemBatteries_RetirementCost

    SystemBatteries_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemBatteries_MinUnitsRetired

    SystemBatteries_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemBatteries_MaxUnitsRetiredinYear

    SystemBatteries_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemBatteries_MinUnitsRetiredinYear

    SystemBatteries_BuildNonanticipativity = plx_enums.PropertyIDEnum.SystemBatteries_BuildNonanticipativity

    SystemBatteries_RetireNonanticipativity = plx_enums.PropertyIDEnum.SystemBatteries_RetireNonanticipativity

    SystemBatteries_x = plx_enums.PropertyIDEnum.SystemBatteries_x

    SystemBatteries_y = plx_enums.PropertyIDEnum.SystemBatteries_y

    SystemBatteries_z = plx_enums.PropertyIDEnum.SystemBatteries_z

    SystemMaintenances_Duration = plx_enums.PropertyIDEnum.SystemMaintenances_Duration

    SystemMaintenances_Window = plx_enums.PropertyIDEnum.SystemMaintenances_Window

    SystemMaintenances_StartWindow = plx_enums.PropertyIDEnum.SystemMaintenances_StartWindow

    SystemMaintenances_EndWindow = plx_enums.PropertyIDEnum.SystemMaintenances_EndWindow

    SystemMaintenances_Cost = plx_enums.PropertyIDEnum.SystemMaintenances_Cost

    SystemMaintenances_Crew = plx_enums.PropertyIDEnum.SystemMaintenances_Crew

    SystemMaintenances_Equipment = plx_enums.PropertyIDEnum.SystemMaintenances_Equipment

    SystemMaintenances_LeadTime = plx_enums.PropertyIDEnum.SystemMaintenances_LeadTime

    SystemMaintenances_MutuallyExclusive = plx_enums.PropertyIDEnum.SystemMaintenances_MutuallyExclusive

    SystemMaintenances_PenaltyCost = plx_enums.PropertyIDEnum.SystemMaintenances_PenaltyCost

    SystemMaintenances_MinOccurrence = plx_enums.PropertyIDEnum.SystemMaintenances_MinOccurrence

    SystemMaintenances_MinOccurrenceHour = plx_enums.PropertyIDEnum.SystemMaintenances_MinOccurrenceHour

    SystemMaintenances_MinOccurrenceDay = plx_enums.PropertyIDEnum.SystemMaintenances_MinOccurrenceDay

    SystemMaintenances_MinOccurrenceWeek = plx_enums.PropertyIDEnum.SystemMaintenances_MinOccurrenceWeek

    SystemMaintenances_MinOccurrenceMonth = plx_enums.PropertyIDEnum.SystemMaintenances_MinOccurrenceMonth

    SystemMaintenances_MinOccurrenceYear = plx_enums.PropertyIDEnum.SystemMaintenances_MinOccurrenceYear

    SystemMaintenances_Nonanticipativity = plx_enums.PropertyIDEnum.SystemMaintenances_Nonanticipativity

    SystemMaintenances_x = plx_enums.PropertyIDEnum.SystemMaintenances_x

    SystemMaintenances_y = plx_enums.PropertyIDEnum.SystemMaintenances_y

    SystemMaintenances_z = plx_enums.PropertyIDEnum.SystemMaintenances_z

    SystemHeatNodes_AllowDumpHeat = plx_enums.PropertyIDEnum.SystemHeatNodes_AllowDumpHeat

    SystemHeatNodes_Units = plx_enums.PropertyIDEnum.SystemHeatNodes_Units

    SystemHeatNodes_HeatDemand = plx_enums.PropertyIDEnum.SystemHeatNodes_HeatDemand

    SystemHeatNodes_x = plx_enums.PropertyIDEnum.SystemHeatNodes_x

    SystemHeatNodes_y = plx_enums.PropertyIDEnum.SystemHeatNodes_y

    SystemHeatNodes_z = plx_enums.PropertyIDEnum.SystemHeatNodes_z

    SystemHeatPlants_UnitCommitmentOptimality = plx_enums.PropertyIDEnum.SystemHeatPlants_UnitCommitmentOptimality

    SystemHeatPlants_Units = plx_enums.PropertyIDEnum.SystemHeatPlants_Units

    SystemHeatPlants_MaxCapacity = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxCapacity

    SystemHeatPlants_EfficiencyBase = plx_enums.PropertyIDEnum.SystemHeatPlants_EfficiencyBase

    SystemHeatPlants_EfficiencyIncr = plx_enums.PropertyIDEnum.SystemHeatPlants_EfficiencyIncr

    SystemHeatPlants_VOMCharge = plx_enums.PropertyIDEnum.SystemHeatPlants_VOMCharge

    SystemHeatPlants_LoadPoint = plx_enums.PropertyIDEnum.SystemHeatPlants_LoadPoint

    SystemHeatPlants_HeatRate = plx_enums.PropertyIDEnum.SystemHeatPlants_HeatRate

    SystemHeatPlants_HeatRateBase = plx_enums.PropertyIDEnum.SystemHeatPlants_HeatRateBase

    SystemHeatPlants_HeatRateIncr = plx_enums.PropertyIDEnum.SystemHeatPlants_HeatRateIncr

    SystemHeatPlants_StartCost = plx_enums.PropertyIDEnum.SystemHeatPlants_StartCost

    SystemHeatPlants_StartCostTime = plx_enums.PropertyIDEnum.SystemHeatPlants_StartCostTime

    SystemHeatPlants_RunUpRate = plx_enums.PropertyIDEnum.SystemHeatPlants_RunUpRate

    SystemHeatPlants_StartProfile = plx_enums.PropertyIDEnum.SystemHeatPlants_StartProfile

    SystemHeatPlants_MinUpTime = plx_enums.PropertyIDEnum.SystemHeatPlants_MinUpTime

    SystemHeatPlants_MinDownTime = plx_enums.PropertyIDEnum.SystemHeatPlants_MinDownTime

    SystemHeatPlants_MaxUpTime = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxUpTime

    SystemHeatPlants_MaxDownTime = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxDownTime

    SystemHeatPlants_MaxRampUp = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxRampUp

    SystemHeatPlants_MaxRampDown = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxRampDown

    SystemHeatPlants_MinStableLevel = plx_enums.PropertyIDEnum.SystemHeatPlants_MinStableLevel

    SystemHeatPlants_FOMCharge = plx_enums.PropertyIDEnum.SystemHeatPlants_FOMCharge

    SystemHeatPlants_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxUnitsBuilt

    SystemHeatPlants_LeadTime = plx_enums.PropertyIDEnum.SystemHeatPlants_LeadTime

    SystemHeatPlants_ProjectStartDate = plx_enums.PropertyIDEnum.SystemHeatPlants_ProjectStartDate

    SystemHeatPlants_TechnicalLife = plx_enums.PropertyIDEnum.SystemHeatPlants_TechnicalLife

    SystemHeatPlants_BuildCost = plx_enums.PropertyIDEnum.SystemHeatPlants_BuildCost

    SystemHeatPlants_WACC = plx_enums.PropertyIDEnum.SystemHeatPlants_WACC

    SystemHeatPlants_EconomicLife = plx_enums.PropertyIDEnum.SystemHeatPlants_EconomicLife

    SystemHeatPlants_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemHeatPlants_MinUnitsBuilt

    SystemHeatPlants_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxUnitsBuiltinYear

    SystemHeatPlants_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemHeatPlants_MinUnitsBuiltinYear

    SystemHeatPlants_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxUnitsRetired

    SystemHeatPlants_RetirementCost = plx_enums.PropertyIDEnum.SystemHeatPlants_RetirementCost

    SystemHeatPlants_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemHeatPlants_MinUnitsRetired

    SystemHeatPlants_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemHeatPlants_MaxUnitsRetiredinYear

    SystemHeatPlants_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemHeatPlants_MinUnitsRetiredinYear

    SystemHeatPlants_x = plx_enums.PropertyIDEnum.SystemHeatPlants_x

    SystemHeatPlants_y = plx_enums.PropertyIDEnum.SystemHeatPlants_y

    SystemHeatPlants_z = plx_enums.PropertyIDEnum.SystemHeatPlants_z

    SystemGasFields_BalancePeriod = plx_enums.PropertyIDEnum.SystemGasFields_BalancePeriod

    SystemGasFields_InternalVolumeScalar = plx_enums.PropertyIDEnum.SystemGasFields_InternalVolumeScalar

    SystemGasFields_EndEffectsMethod = plx_enums.PropertyIDEnum.SystemGasFields_EndEffectsMethod

    SystemGasFields_RecyclePenalty = plx_enums.PropertyIDEnum.SystemGasFields_RecyclePenalty

    SystemGasFields_DecompositionMethod = plx_enums.PropertyIDEnum.SystemGasFields_DecompositionMethod

    SystemGasFields_DecompositionPenaltya = plx_enums.PropertyIDEnum.SystemGasFields_DecompositionPenaltya

    SystemGasFields_DecompositionPenaltyb = plx_enums.PropertyIDEnum.SystemGasFields_DecompositionPenaltyb

    SystemGasFields_DecompositionPenaltyc = plx_enums.PropertyIDEnum.SystemGasFields_DecompositionPenaltyc

    SystemGasFields_DecompositionPenaltyx = plx_enums.PropertyIDEnum.SystemGasFields_DecompositionPenaltyx

    SystemGasFields_DecompositionBoundPenalty = plx_enums.PropertyIDEnum.SystemGasFields_DecompositionBoundPenalty

    SystemGasFields_EnforceBounds = plx_enums.PropertyIDEnum.SystemGasFields_EnforceBounds

    SystemGasFields_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemGasFields_ExpansionOptimality

    SystemGasFields_Units = plx_enums.PropertyIDEnum.SystemGasFields_Units

    SystemGasFields_InitialVolume = plx_enums.PropertyIDEnum.SystemGasFields_InitialVolume

    SystemGasFields_ProductionCost = plx_enums.PropertyIDEnum.SystemGasFields_ProductionCost

    SystemGasFields_ProductionVolume = plx_enums.PropertyIDEnum.SystemGasFields_ProductionVolume

    SystemGasFields_MaxRamp = plx_enums.PropertyIDEnum.SystemGasFields_MaxRamp

    SystemGasFields_MaxRampHour = plx_enums.PropertyIDEnum.SystemGasFields_MaxRampHour

    SystemGasFields_MaxRampDay = plx_enums.PropertyIDEnum.SystemGasFields_MaxRampDay

    SystemGasFields_MaxRampWeek = plx_enums.PropertyIDEnum.SystemGasFields_MaxRampWeek

    SystemGasFields_MaxRampMonth = plx_enums.PropertyIDEnum.SystemGasFields_MaxRampMonth

    SystemGasFields_MaxRampYear = plx_enums.PropertyIDEnum.SystemGasFields_MaxRampYear

    SystemGasFields_MaxProduction = plx_enums.PropertyIDEnum.SystemGasFields_MaxProduction

    SystemGasFields_MaxProductionHour = plx_enums.PropertyIDEnum.SystemGasFields_MaxProductionHour

    SystemGasFields_MaxProductionDay = plx_enums.PropertyIDEnum.SystemGasFields_MaxProductionDay

    SystemGasFields_MaxProductionWeek = plx_enums.PropertyIDEnum.SystemGasFields_MaxProductionWeek

    SystemGasFields_MaxProductionMonth = plx_enums.PropertyIDEnum.SystemGasFields_MaxProductionMonth

    SystemGasFields_MaxProductionYear = plx_enums.PropertyIDEnum.SystemGasFields_MaxProductionYear

    SystemGasFields_MinProduction = plx_enums.PropertyIDEnum.SystemGasFields_MinProduction

    SystemGasFields_MinProductionHour = plx_enums.PropertyIDEnum.SystemGasFields_MinProductionHour

    SystemGasFields_MinProductionDay = plx_enums.PropertyIDEnum.SystemGasFields_MinProductionDay

    SystemGasFields_MinProductionWeek = plx_enums.PropertyIDEnum.SystemGasFields_MinProductionWeek

    SystemGasFields_MinProductionMonth = plx_enums.PropertyIDEnum.SystemGasFields_MinProductionMonth

    SystemGasFields_MinProductionYear = plx_enums.PropertyIDEnum.SystemGasFields_MinProductionYear

    SystemGasFields_Target = plx_enums.PropertyIDEnum.SystemGasFields_Target

    SystemGasFields_TargetHour = plx_enums.PropertyIDEnum.SystemGasFields_TargetHour

    SystemGasFields_TargetDay = plx_enums.PropertyIDEnum.SystemGasFields_TargetDay

    SystemGasFields_TargetWeek = plx_enums.PropertyIDEnum.SystemGasFields_TargetWeek

    SystemGasFields_TargetMonth = plx_enums.PropertyIDEnum.SystemGasFields_TargetMonth

    SystemGasFields_TargetYear = plx_enums.PropertyIDEnum.SystemGasFields_TargetYear

    SystemGasFields_TargetPenalty = plx_enums.PropertyIDEnum.SystemGasFields_TargetPenalty

    SystemGasFields_ExternalInjection = plx_enums.PropertyIDEnum.SystemGasFields_ExternalInjection

    SystemGasFields_FOMCharge = plx_enums.PropertyIDEnum.SystemGasFields_FOMCharge

    SystemGasFields_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasFields_MaxUnitsBuilt

    SystemGasFields_LeadTime = plx_enums.PropertyIDEnum.SystemGasFields_LeadTime

    SystemGasFields_ProjectStartDate = plx_enums.PropertyIDEnum.SystemGasFields_ProjectStartDate

    SystemGasFields_TechnicalLife = plx_enums.PropertyIDEnum.SystemGasFields_TechnicalLife

    SystemGasFields_BuildCost = plx_enums.PropertyIDEnum.SystemGasFields_BuildCost

    SystemGasFields_WACC = plx_enums.PropertyIDEnum.SystemGasFields_WACC

    SystemGasFields_EconomicLife = plx_enums.PropertyIDEnum.SystemGasFields_EconomicLife

    SystemGasFields_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasFields_MaxUnitsBuiltinYear

    SystemGasFields_x = plx_enums.PropertyIDEnum.SystemGasFields_x

    SystemGasFields_y = plx_enums.PropertyIDEnum.SystemGasFields_y

    SystemGasFields_z = plx_enums.PropertyIDEnum.SystemGasFields_z

    SystemGasPlants_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemGasPlants_ExpansionOptimality

    SystemGasPlants_Units = plx_enums.PropertyIDEnum.SystemGasPlants_Units

    SystemGasPlants_MaxProduction = plx_enums.PropertyIDEnum.SystemGasPlants_MaxProduction

    SystemGasPlants_MinProduction = plx_enums.PropertyIDEnum.SystemGasPlants_MinProduction

    SystemGasPlants_ProcessingRate = plx_enums.PropertyIDEnum.SystemGasPlants_ProcessingRate

    SystemGasPlants_ProcessingCharge = plx_enums.PropertyIDEnum.SystemGasPlants_ProcessingCharge

    SystemGasPlants_Consumption = plx_enums.PropertyIDEnum.SystemGasPlants_Consumption

    SystemGasPlants_EnergyUsage = plx_enums.PropertyIDEnum.SystemGasPlants_EnergyUsage

    SystemGasPlants_VOMCharge = plx_enums.PropertyIDEnum.SystemGasPlants_VOMCharge

    SystemGasPlants_FOMCharge = plx_enums.PropertyIDEnum.SystemGasPlants_FOMCharge

    SystemGasPlants_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasPlants_MaxUnitsBuilt

    SystemGasPlants_LeadTime = plx_enums.PropertyIDEnum.SystemGasPlants_LeadTime

    SystemGasPlants_ProjectStartDate = plx_enums.PropertyIDEnum.SystemGasPlants_ProjectStartDate

    SystemGasPlants_TechnicalLife = plx_enums.PropertyIDEnum.SystemGasPlants_TechnicalLife

    SystemGasPlants_BuildCost = plx_enums.PropertyIDEnum.SystemGasPlants_BuildCost

    SystemGasPlants_WACC = plx_enums.PropertyIDEnum.SystemGasPlants_WACC

    SystemGasPlants_EconomicLife = plx_enums.PropertyIDEnum.SystemGasPlants_EconomicLife

    SystemGasPlants_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasPlants_MinUnitsBuilt

    SystemGasPlants_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasPlants_MaxUnitsBuiltinYear

    SystemGasPlants_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasPlants_MinUnitsBuiltinYear

    SystemGasPlants_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemGasPlants_MaxUnitsRetired

    SystemGasPlants_RetirementCost = plx_enums.PropertyIDEnum.SystemGasPlants_RetirementCost

    SystemGasPlants_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemGasPlants_MinUnitsRetired

    SystemGasPlants_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasPlants_MaxUnitsRetiredinYear

    SystemGasPlants_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasPlants_MinUnitsRetiredinYear

    SystemGasPlants_x = plx_enums.PropertyIDEnum.SystemGasPlants_x

    SystemGasPlants_y = plx_enums.PropertyIDEnum.SystemGasPlants_y

    SystemGasPlants_z = plx_enums.PropertyIDEnum.SystemGasPlants_z

    SystemGasPipelines_RandomNumberSeed = plx_enums.PropertyIDEnum.SystemGasPipelines_RandomNumberSeed

    SystemGasPipelines_BalancePeriod = plx_enums.PropertyIDEnum.SystemGasPipelines_BalancePeriod

    SystemGasPipelines_InternalVolumeScalar = plx_enums.PropertyIDEnum.SystemGasPipelines_InternalVolumeScalar

    SystemGasPipelines_EndEffectsMethod = plx_enums.PropertyIDEnum.SystemGasPipelines_EndEffectsMethod

    SystemGasPipelines_RecyclePenalty = plx_enums.PropertyIDEnum.SystemGasPipelines_RecyclePenalty

    SystemGasPipelines_DecompositionMethod = plx_enums.PropertyIDEnum.SystemGasPipelines_DecompositionMethod

    SystemGasPipelines_DecompositionPenaltya = plx_enums.PropertyIDEnum.SystemGasPipelines_DecompositionPenaltya

    SystemGasPipelines_DecompositionPenaltyb = plx_enums.PropertyIDEnum.SystemGasPipelines_DecompositionPenaltyb

    SystemGasPipelines_DecompositionPenaltyc = plx_enums.PropertyIDEnum.SystemGasPipelines_DecompositionPenaltyc

    SystemGasPipelines_DecompositionPenaltyx = plx_enums.PropertyIDEnum.SystemGasPipelines_DecompositionPenaltyx

    SystemGasPipelines_DecompositionBoundPenalty = plx_enums.PropertyIDEnum.SystemGasPipelines_DecompositionBoundPenalty

    SystemGasPipelines_EnforceBounds = plx_enums.PropertyIDEnum.SystemGasPipelines_EnforceBounds

    SystemGasPipelines_RepairTimeDistribution = plx_enums.PropertyIDEnum.SystemGasPipelines_RepairTimeDistribution

    SystemGasPipelines_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemGasPipelines_ExpansionOptimality

    SystemGasPipelines_Units = plx_enums.PropertyIDEnum.SystemGasPipelines_Units

    SystemGasPipelines_MaxFlow = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlow

    SystemGasPipelines_MaxFlowHour = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowHour

    SystemGasPipelines_MaxFlowDay = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowDay

    SystemGasPipelines_MaxFlowWeek = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowWeek

    SystemGasPipelines_MaxFlowMonth = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowMonth

    SystemGasPipelines_MaxFlowYear = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowYear

    SystemGasPipelines_MaxFlowBack = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowBack

    SystemGasPipelines_MaxFlowBackHour = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowBackHour

    SystemGasPipelines_MaxFlowBackDay = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowBackDay

    SystemGasPipelines_MaxFlowBackWeek = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowBackWeek

    SystemGasPipelines_MaxFlowBackMonth = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowBackMonth

    SystemGasPipelines_MaxFlowBackYear = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxFlowBackYear

    SystemGasPipelines_Diameter = plx_enums.PropertyIDEnum.SystemGasPipelines_Diameter

    SystemGasPipelines_Roughness = plx_enums.PropertyIDEnum.SystemGasPipelines_Roughness

    SystemGasPipelines_Length = plx_enums.PropertyIDEnum.SystemGasPipelines_Length

    SystemGasPipelines_PumpEfficiency = plx_enums.PropertyIDEnum.SystemGasPipelines_PumpEfficiency

    SystemGasPipelines_FlowCharge = plx_enums.PropertyIDEnum.SystemGasPipelines_FlowCharge

    SystemGasPipelines_FlowChargeBack = plx_enums.PropertyIDEnum.SystemGasPipelines_FlowChargeBack

    SystemGasPipelines_InitialVolume = plx_enums.PropertyIDEnum.SystemGasPipelines_InitialVolume

    SystemGasPipelines_MaxVolume = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxVolume

    SystemGasPipelines_MinVolume = plx_enums.PropertyIDEnum.SystemGasPipelines_MinVolume

    SystemGasPipelines_VolumeImbalance = plx_enums.PropertyIDEnum.SystemGasPipelines_VolumeImbalance

    SystemGasPipelines_ImbalanceCharge = plx_enums.PropertyIDEnum.SystemGasPipelines_ImbalanceCharge

    SystemGasPipelines_FOMCharge = plx_enums.PropertyIDEnum.SystemGasPipelines_FOMCharge

    SystemGasPipelines_ConsumptionAllocation = plx_enums.PropertyIDEnum.SystemGasPipelines_ConsumptionAllocation

    SystemGasPipelines_UnitsOut = plx_enums.PropertyIDEnum.SystemGasPipelines_UnitsOut

    SystemGasPipelines_MaintenanceRate = plx_enums.PropertyIDEnum.SystemGasPipelines_MaintenanceRate

    SystemGasPipelines_MaintenanceFrequency = plx_enums.PropertyIDEnum.SystemGasPipelines_MaintenanceFrequency

    SystemGasPipelines_ForcedOutageRate = plx_enums.PropertyIDEnum.SystemGasPipelines_ForcedOutageRate

    SystemGasPipelines_OutageMaxFlow = plx_enums.PropertyIDEnum.SystemGasPipelines_OutageMaxFlow

    SystemGasPipelines_OutageMaxFlowBack = plx_enums.PropertyIDEnum.SystemGasPipelines_OutageMaxFlowBack

    SystemGasPipelines_MeanTimetoRepair = plx_enums.PropertyIDEnum.SystemGasPipelines_MeanTimetoRepair

    SystemGasPipelines_MinTimeToRepair = plx_enums.PropertyIDEnum.SystemGasPipelines_MinTimeToRepair

    SystemGasPipelines_MaxTimeToRepair = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxTimeToRepair

    SystemGasPipelines_RepairTimeShape = plx_enums.PropertyIDEnum.SystemGasPipelines_RepairTimeShape

    SystemGasPipelines_RepairTimeScale = plx_enums.PropertyIDEnum.SystemGasPipelines_RepairTimeScale

    SystemGasPipelines_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxUnitsBuilt

    SystemGasPipelines_LeadTime = plx_enums.PropertyIDEnum.SystemGasPipelines_LeadTime

    SystemGasPipelines_ProjectStartDate = plx_enums.PropertyIDEnum.SystemGasPipelines_ProjectStartDate

    SystemGasPipelines_TechnicalLife = plx_enums.PropertyIDEnum.SystemGasPipelines_TechnicalLife

    SystemGasPipelines_BuildCost = plx_enums.PropertyIDEnum.SystemGasPipelines_BuildCost

    SystemGasPipelines_WACC = plx_enums.PropertyIDEnum.SystemGasPipelines_WACC

    SystemGasPipelines_EconomicLife = plx_enums.PropertyIDEnum.SystemGasPipelines_EconomicLife

    SystemGasPipelines_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasPipelines_MinUnitsBuilt

    SystemGasPipelines_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxUnitsBuiltinYear

    SystemGasPipelines_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasPipelines_MinUnitsBuiltinYear

    SystemGasPipelines_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxUnitsRetired

    SystemGasPipelines_RetirementCost = plx_enums.PropertyIDEnum.SystemGasPipelines_RetirementCost

    SystemGasPipelines_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemGasPipelines_MinUnitsRetired

    SystemGasPipelines_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasPipelines_MaxUnitsRetiredinYear

    SystemGasPipelines_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasPipelines_MinUnitsRetiredinYear

    SystemGasPipelines_x = plx_enums.PropertyIDEnum.SystemGasPipelines_x

    SystemGasPipelines_y = plx_enums.PropertyIDEnum.SystemGasPipelines_y

    SystemGasPipelines_z = plx_enums.PropertyIDEnum.SystemGasPipelines_z

    SystemGasNodes_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemGasNodes_ExpansionOptimality

    SystemGasNodes_Units = plx_enums.PropertyIDEnum.SystemGasNodes_Units

    SystemGasNodes_FlowCharge = plx_enums.PropertyIDEnum.SystemGasNodes_FlowCharge

    SystemGasNodes_MaxFlow = plx_enums.PropertyIDEnum.SystemGasNodes_MaxFlow

    SystemGasNodes_MaxFlowHour = plx_enums.PropertyIDEnum.SystemGasNodes_MaxFlowHour

    SystemGasNodes_MaxFlowDay = plx_enums.PropertyIDEnum.SystemGasNodes_MaxFlowDay

    SystemGasNodes_MaxFlowWeek = plx_enums.PropertyIDEnum.SystemGasNodes_MaxFlowWeek

    SystemGasNodes_MaxFlowMonth = plx_enums.PropertyIDEnum.SystemGasNodes_MaxFlowMonth

    SystemGasNodes_MaxFlowYear = plx_enums.PropertyIDEnum.SystemGasNodes_MaxFlowYear

    SystemGasNodes_GasSecurity = plx_enums.PropertyIDEnum.SystemGasNodes_GasSecurity

    SystemGasNodes_FOMCharge = plx_enums.PropertyIDEnum.SystemGasNodes_FOMCharge

    SystemGasNodes_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasNodes_MaxUnitsBuilt

    SystemGasNodes_LeadTime = plx_enums.PropertyIDEnum.SystemGasNodes_LeadTime

    SystemGasNodes_ProjectStartDate = plx_enums.PropertyIDEnum.SystemGasNodes_ProjectStartDate

    SystemGasNodes_TechnicalLife = plx_enums.PropertyIDEnum.SystemGasNodes_TechnicalLife

    SystemGasNodes_BuildCost = plx_enums.PropertyIDEnum.SystemGasNodes_BuildCost

    SystemGasNodes_WACC = plx_enums.PropertyIDEnum.SystemGasNodes_WACC

    SystemGasNodes_EconomicLife = plx_enums.PropertyIDEnum.SystemGasNodes_EconomicLife

    SystemGasNodes_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasNodes_MinUnitsBuilt

    SystemGasNodes_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasNodes_MaxUnitsBuiltinYear

    SystemGasNodes_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasNodes_MinUnitsBuiltinYear

    SystemGasNodes_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemGasNodes_MaxUnitsRetired

    SystemGasNodes_RetirementCost = plx_enums.PropertyIDEnum.SystemGasNodes_RetirementCost

    SystemGasNodes_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemGasNodes_MinUnitsRetired

    SystemGasNodes_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasNodes_MaxUnitsRetiredinYear

    SystemGasNodes_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasNodes_MinUnitsRetiredinYear

    SystemGasNodes_x = plx_enums.PropertyIDEnum.SystemGasNodes_x

    SystemGasNodes_y = plx_enums.PropertyIDEnum.SystemGasNodes_y

    SystemGasNodes_z = plx_enums.PropertyIDEnum.SystemGasNodes_z

    SystemGasStorages_BalancePeriod = plx_enums.PropertyIDEnum.SystemGasStorages_BalancePeriod

    SystemGasStorages_InternalVolumeScalar = plx_enums.PropertyIDEnum.SystemGasStorages_InternalVolumeScalar

    SystemGasStorages_EndEffectsMethod = plx_enums.PropertyIDEnum.SystemGasStorages_EndEffectsMethod

    SystemGasStorages_RecyclePenalty = plx_enums.PropertyIDEnum.SystemGasStorages_RecyclePenalty

    SystemGasStorages_DecompositionMethod = plx_enums.PropertyIDEnum.SystemGasStorages_DecompositionMethod

    SystemGasStorages_DecompositionPenaltya = plx_enums.PropertyIDEnum.SystemGasStorages_DecompositionPenaltya

    SystemGasStorages_DecompositionPenaltyb = plx_enums.PropertyIDEnum.SystemGasStorages_DecompositionPenaltyb

    SystemGasStorages_DecompositionPenaltyc = plx_enums.PropertyIDEnum.SystemGasStorages_DecompositionPenaltyc

    SystemGasStorages_DecompositionPenaltyx = plx_enums.PropertyIDEnum.SystemGasStorages_DecompositionPenaltyx

    SystemGasStorages_DecompositionBoundPenalty = plx_enums.PropertyIDEnum.SystemGasStorages_DecompositionBoundPenalty

    SystemGasStorages_EnforceBounds = plx_enums.PropertyIDEnum.SystemGasStorages_EnforceBounds

    SystemGasStorages_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemGasStorages_ExpansionOptimality

    SystemGasStorages_Units = plx_enums.PropertyIDEnum.SystemGasStorages_Units

    SystemGasStorages_MaxVolume = plx_enums.PropertyIDEnum.SystemGasStorages_MaxVolume

    SystemGasStorages_MinVolume = plx_enums.PropertyIDEnum.SystemGasStorages_MinVolume

    SystemGasStorages_InitialVolume = plx_enums.PropertyIDEnum.SystemGasStorages_InitialVolume

    SystemGasStorages_WithdrawalCharge = plx_enums.PropertyIDEnum.SystemGasStorages_WithdrawalCharge

    SystemGasStorages_InjectionCharge = plx_enums.PropertyIDEnum.SystemGasStorages_InjectionCharge

    SystemGasStorages_InjectionRatchet = plx_enums.PropertyIDEnum.SystemGasStorages_InjectionRatchet

    SystemGasStorages_WithdrawalRatchet = plx_enums.PropertyIDEnum.SystemGasStorages_WithdrawalRatchet

    SystemGasStorages_MaxWithdrawal = plx_enums.PropertyIDEnum.SystemGasStorages_MaxWithdrawal

    SystemGasStorages_MaxWithdrawalHour = plx_enums.PropertyIDEnum.SystemGasStorages_MaxWithdrawalHour

    SystemGasStorages_MaxWithdrawalDay = plx_enums.PropertyIDEnum.SystemGasStorages_MaxWithdrawalDay

    SystemGasStorages_MaxWithdrawalWeek = plx_enums.PropertyIDEnum.SystemGasStorages_MaxWithdrawalWeek

    SystemGasStorages_MaxWithdrawalMonth = plx_enums.PropertyIDEnum.SystemGasStorages_MaxWithdrawalMonth

    SystemGasStorages_MaxWithdrawalYear = plx_enums.PropertyIDEnum.SystemGasStorages_MaxWithdrawalYear

    SystemGasStorages_MaxInjection = plx_enums.PropertyIDEnum.SystemGasStorages_MaxInjection

    SystemGasStorages_MaxInjectionHour = plx_enums.PropertyIDEnum.SystemGasStorages_MaxInjectionHour

    SystemGasStorages_MaxInjectionDay = plx_enums.PropertyIDEnum.SystemGasStorages_MaxInjectionDay

    SystemGasStorages_MaxInjectionWeek = plx_enums.PropertyIDEnum.SystemGasStorages_MaxInjectionWeek

    SystemGasStorages_MaxInjectionMonth = plx_enums.PropertyIDEnum.SystemGasStorages_MaxInjectionMonth

    SystemGasStorages_MaxInjectionYear = plx_enums.PropertyIDEnum.SystemGasStorages_MaxInjectionYear

    SystemGasStorages_MinWithdrawal = plx_enums.PropertyIDEnum.SystemGasStorages_MinWithdrawal

    SystemGasStorages_MinWithdrawalHour = plx_enums.PropertyIDEnum.SystemGasStorages_MinWithdrawalHour

    SystemGasStorages_MinWithdrawalDay = plx_enums.PropertyIDEnum.SystemGasStorages_MinWithdrawalDay

    SystemGasStorages_MinWithdrawalWeek = plx_enums.PropertyIDEnum.SystemGasStorages_MinWithdrawalWeek

    SystemGasStorages_MinWithdrawalMonth = plx_enums.PropertyIDEnum.SystemGasStorages_MinWithdrawalMonth

    SystemGasStorages_MinWithdrawalYear = plx_enums.PropertyIDEnum.SystemGasStorages_MinWithdrawalYear

    SystemGasStorages_MinInjection = plx_enums.PropertyIDEnum.SystemGasStorages_MinInjection

    SystemGasStorages_MinInjectionHour = plx_enums.PropertyIDEnum.SystemGasStorages_MinInjectionHour

    SystemGasStorages_MinInjectionDay = plx_enums.PropertyIDEnum.SystemGasStorages_MinInjectionDay

    SystemGasStorages_MinInjectionWeek = plx_enums.PropertyIDEnum.SystemGasStorages_MinInjectionWeek

    SystemGasStorages_MinInjectionMonth = plx_enums.PropertyIDEnum.SystemGasStorages_MinInjectionMonth

    SystemGasStorages_MinInjectionYear = plx_enums.PropertyIDEnum.SystemGasStorages_MinInjectionYear

    SystemGasStorages_MaxRamp = plx_enums.PropertyIDEnum.SystemGasStorages_MaxRamp

    SystemGasStorages_MaxRampHour = plx_enums.PropertyIDEnum.SystemGasStorages_MaxRampHour

    SystemGasStorages_MaxRampDay = plx_enums.PropertyIDEnum.SystemGasStorages_MaxRampDay

    SystemGasStorages_MaxRampWeek = plx_enums.PropertyIDEnum.SystemGasStorages_MaxRampWeek

    SystemGasStorages_MaxRampMonth = plx_enums.PropertyIDEnum.SystemGasStorages_MaxRampMonth

    SystemGasStorages_MaxRampYear = plx_enums.PropertyIDEnum.SystemGasStorages_MaxRampYear

    SystemGasStorages_Target = plx_enums.PropertyIDEnum.SystemGasStorages_Target

    SystemGasStorages_TargetHour = plx_enums.PropertyIDEnum.SystemGasStorages_TargetHour

    SystemGasStorages_TargetDay = plx_enums.PropertyIDEnum.SystemGasStorages_TargetDay

    SystemGasStorages_TargetWeek = plx_enums.PropertyIDEnum.SystemGasStorages_TargetWeek

    SystemGasStorages_TargetMonth = plx_enums.PropertyIDEnum.SystemGasStorages_TargetMonth

    SystemGasStorages_TargetYear = plx_enums.PropertyIDEnum.SystemGasStorages_TargetYear

    SystemGasStorages_TargetPenalty = plx_enums.PropertyIDEnum.SystemGasStorages_TargetPenalty

    SystemGasStorages_EnergyUsage = plx_enums.PropertyIDEnum.SystemGasStorages_EnergyUsage

    SystemGasStorages_LossRate = plx_enums.PropertyIDEnum.SystemGasStorages_LossRate

    SystemGasStorages_WithdrawalRateScalar = plx_enums.PropertyIDEnum.SystemGasStorages_WithdrawalRateScalar

    SystemGasStorages_WithdrawalVolume = plx_enums.PropertyIDEnum.SystemGasStorages_WithdrawalVolume

    SystemGasStorages_InjectionRateScalar = plx_enums.PropertyIDEnum.SystemGasStorages_InjectionRateScalar

    SystemGasStorages_InjectionVolume = plx_enums.PropertyIDEnum.SystemGasStorages_InjectionVolume

    SystemGasStorages_ExternalInjection = plx_enums.PropertyIDEnum.SystemGasStorages_ExternalInjection

    SystemGasStorages_FOMCharge = plx_enums.PropertyIDEnum.SystemGasStorages_FOMCharge

    SystemGasStorages_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasStorages_MaxUnitsBuilt

    SystemGasStorages_LeadTime = plx_enums.PropertyIDEnum.SystemGasStorages_LeadTime

    SystemGasStorages_ProjectStartDate = plx_enums.PropertyIDEnum.SystemGasStorages_ProjectStartDate

    SystemGasStorages_TechnicalLife = plx_enums.PropertyIDEnum.SystemGasStorages_TechnicalLife

    SystemGasStorages_BuildCost = plx_enums.PropertyIDEnum.SystemGasStorages_BuildCost

    SystemGasStorages_WACC = plx_enums.PropertyIDEnum.SystemGasStorages_WACC

    SystemGasStorages_EconomicLife = plx_enums.PropertyIDEnum.SystemGasStorages_EconomicLife

    SystemGasStorages_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemGasStorages_MinUnitsBuilt

    SystemGasStorages_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasStorages_MaxUnitsBuiltinYear

    SystemGasStorages_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemGasStorages_MinUnitsBuiltinYear

    SystemGasStorages_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemGasStorages_MaxUnitsRetired

    SystemGasStorages_RetirementCost = plx_enums.PropertyIDEnum.SystemGasStorages_RetirementCost

    SystemGasStorages_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemGasStorages_MinUnitsRetired

    SystemGasStorages_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasStorages_MaxUnitsRetiredinYear

    SystemGasStorages_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemGasStorages_MinUnitsRetiredinYear

    SystemGasStorages_TrajectoryNonanticipativity = plx_enums.PropertyIDEnum.SystemGasStorages_TrajectoryNonanticipativity

    SystemGasStorages_TrajectoryNonanticipativityVolume = plx_enums.PropertyIDEnum.SystemGasStorages_TrajectoryNonanticipativityVolume

    SystemGasStorages_TrajectoryNonanticipativityTime = plx_enums.PropertyIDEnum.SystemGasStorages_TrajectoryNonanticipativityTime

    SystemGasStorages_x = plx_enums.PropertyIDEnum.SystemGasStorages_x

    SystemGasStorages_y = plx_enums.PropertyIDEnum.SystemGasStorages_y

    SystemGasStorages_z = plx_enums.PropertyIDEnum.SystemGasStorages_z

    SystemGasDemands_Demand = plx_enums.PropertyIDEnum.SystemGasDemands_Demand

    SystemGasDemands_ShortagePrice = plx_enums.PropertyIDEnum.SystemGasDemands_ShortagePrice

    SystemGasDemands_ExcessPrice = plx_enums.PropertyIDEnum.SystemGasDemands_ExcessPrice

    SystemGasDemands_BidQuantity = plx_enums.PropertyIDEnum.SystemGasDemands_BidQuantity

    SystemGasDemands_BidPrice = plx_enums.PropertyIDEnum.SystemGasDemands_BidPrice

    SystemGasDemands_x = plx_enums.PropertyIDEnum.SystemGasDemands_x

    SystemGasDemands_y = plx_enums.PropertyIDEnum.SystemGasDemands_y

    SystemGasDemands_z = plx_enums.PropertyIDEnum.SystemGasDemands_z

    SystemGasBasins_MaxProduction = plx_enums.PropertyIDEnum.SystemGasBasins_MaxProduction

    SystemGasBasins_MaxProductionHour = plx_enums.PropertyIDEnum.SystemGasBasins_MaxProductionHour

    SystemGasBasins_MaxProductionDay = plx_enums.PropertyIDEnum.SystemGasBasins_MaxProductionDay

    SystemGasBasins_MaxProductionWeek = plx_enums.PropertyIDEnum.SystemGasBasins_MaxProductionWeek

    SystemGasBasins_MaxProductionMonth = plx_enums.PropertyIDEnum.SystemGasBasins_MaxProductionMonth

    SystemGasBasins_MaxProductionYear = plx_enums.PropertyIDEnum.SystemGasBasins_MaxProductionYear

    SystemGasBasins_MinProduction = plx_enums.PropertyIDEnum.SystemGasBasins_MinProduction

    SystemGasBasins_MinProductionHour = plx_enums.PropertyIDEnum.SystemGasBasins_MinProductionHour

    SystemGasBasins_MinProductionDay = plx_enums.PropertyIDEnum.SystemGasBasins_MinProductionDay

    SystemGasBasins_MinProductionWeek = plx_enums.PropertyIDEnum.SystemGasBasins_MinProductionWeek

    SystemGasBasins_MinProductionMonth = plx_enums.PropertyIDEnum.SystemGasBasins_MinProductionMonth

    SystemGasBasins_MinProductionYear = plx_enums.PropertyIDEnum.SystemGasBasins_MinProductionYear

    SystemGasBasins_x = plx_enums.PropertyIDEnum.SystemGasBasins_x

    SystemGasBasins_y = plx_enums.PropertyIDEnum.SystemGasBasins_y

    SystemGasBasins_z = plx_enums.PropertyIDEnum.SystemGasBasins_z

    SystemGasZones_x = plx_enums.PropertyIDEnum.SystemGasZones_x

    SystemGasZones_y = plx_enums.PropertyIDEnum.SystemGasZones_y

    SystemGasZones_z = plx_enums.PropertyIDEnum.SystemGasZones_z

    SystemGasContracts_PriceSetting = plx_enums.PropertyIDEnum.SystemGasContracts_PriceSetting

    SystemGasContracts_Quantity = plx_enums.PropertyIDEnum.SystemGasContracts_Quantity

    SystemGasContracts_QuantityHour = plx_enums.PropertyIDEnum.SystemGasContracts_QuantityHour

    SystemGasContracts_QuantityDay = plx_enums.PropertyIDEnum.SystemGasContracts_QuantityDay

    SystemGasContracts_QuantityWeek = plx_enums.PropertyIDEnum.SystemGasContracts_QuantityWeek

    SystemGasContracts_QuantityMonth = plx_enums.PropertyIDEnum.SystemGasContracts_QuantityMonth

    SystemGasContracts_QuantityYear = plx_enums.PropertyIDEnum.SystemGasContracts_QuantityYear

    SystemGasContracts_TakeorPayQuantity = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayQuantity

    SystemGasContracts_TakeorPayQuantityHour = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayQuantityHour

    SystemGasContracts_TakeorPayQuantityDay = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayQuantityDay

    SystemGasContracts_TakeorPayQuantityWeek = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayQuantityWeek

    SystemGasContracts_TakeorPayQuantityMonth = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayQuantityMonth

    SystemGasContracts_TakeorPayQuantityYear = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayQuantityYear

    SystemGasContracts_TakeorPayPrice = plx_enums.PropertyIDEnum.SystemGasContracts_TakeorPayPrice

    SystemGasContracts_Price = plx_enums.PropertyIDEnum.SystemGasContracts_Price

    SystemGasContracts_x = plx_enums.PropertyIDEnum.SystemGasContracts_x

    SystemGasContracts_y = plx_enums.PropertyIDEnum.SystemGasContracts_y

    SystemGasContracts_z = plx_enums.PropertyIDEnum.SystemGasContracts_z

    SystemGasTransports_VoyageTime = plx_enums.PropertyIDEnum.SystemGasTransports_VoyageTime

    SystemGasTransports_LoadingTime = plx_enums.PropertyIDEnum.SystemGasTransports_LoadingTime

    SystemGasTransports_DischargeTime = plx_enums.PropertyIDEnum.SystemGasTransports_DischargeTime

    SystemGasTransports_MinVolume = plx_enums.PropertyIDEnum.SystemGasTransports_MinVolume

    SystemGasTransports_MaxVolume = plx_enums.PropertyIDEnum.SystemGasTransports_MaxVolume

    SystemGasTransports_ShippingCharge = plx_enums.PropertyIDEnum.SystemGasTransports_ShippingCharge

    SystemGasTransports_BoiloffRate = plx_enums.PropertyIDEnum.SystemGasTransports_BoiloffRate

    SystemGasTransports_Imports = plx_enums.PropertyIDEnum.SystemGasTransports_Imports

    SystemGasTransports_Exports = plx_enums.PropertyIDEnum.SystemGasTransports_Exports

    SystemGasTransports_MaxShipments = plx_enums.PropertyIDEnum.SystemGasTransports_MaxShipments

    SystemGasTransports_MaxShipmentsHour = plx_enums.PropertyIDEnum.SystemGasTransports_MaxShipmentsHour

    SystemGasTransports_MaxShipmentsDay = plx_enums.PropertyIDEnum.SystemGasTransports_MaxShipmentsDay

    SystemGasTransports_MaxShipmentsWeek = plx_enums.PropertyIDEnum.SystemGasTransports_MaxShipmentsWeek

    SystemGasTransports_MaxShipmentsMonth = plx_enums.PropertyIDEnum.SystemGasTransports_MaxShipmentsMonth

    SystemGasTransports_MaxShipmentsYear = plx_enums.PropertyIDEnum.SystemGasTransports_MaxShipmentsYear

    SystemGasTransports_x = plx_enums.PropertyIDEnum.SystemGasTransports_x

    SystemGasTransports_y = plx_enums.PropertyIDEnum.SystemGasTransports_y

    SystemGasTransports_z = plx_enums.PropertyIDEnum.SystemGasTransports_z

    SystemWaterPlants_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemWaterPlants_ExpansionOptimality

    SystemWaterPlants_Units = plx_enums.PropertyIDEnum.SystemWaterPlants_Units

    SystemWaterPlants_MaxCapacity = plx_enums.PropertyIDEnum.SystemWaterPlants_MaxCapacity

    SystemWaterPlants_MinStableProduction = plx_enums.PropertyIDEnum.SystemWaterPlants_MinStableProduction

    SystemWaterPlants_AuxFixed = plx_enums.PropertyIDEnum.SystemWaterPlants_AuxFixed

    SystemWaterPlants_AuxBase = plx_enums.PropertyIDEnum.SystemWaterPlants_AuxBase

    SystemWaterPlants_AuxIncr = plx_enums.PropertyIDEnum.SystemWaterPlants_AuxIncr

    SystemWaterPlants_HeatUsage = plx_enums.PropertyIDEnum.SystemWaterPlants_HeatUsage

    SystemWaterPlants_WaterYield = plx_enums.PropertyIDEnum.SystemWaterPlants_WaterYield

    SystemWaterPlants_EnergyUsage = plx_enums.PropertyIDEnum.SystemWaterPlants_EnergyUsage

    SystemWaterPlants_VOMCharge = plx_enums.PropertyIDEnum.SystemWaterPlants_VOMCharge

    SystemWaterPlants_FOMCharge = plx_enums.PropertyIDEnum.SystemWaterPlants_FOMCharge

    SystemWaterPlants_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterPlants_MaxUnitsBuilt

    SystemWaterPlants_LeadTime = plx_enums.PropertyIDEnum.SystemWaterPlants_LeadTime

    SystemWaterPlants_ProjectStartDate = plx_enums.PropertyIDEnum.SystemWaterPlants_ProjectStartDate

    SystemWaterPlants_TechnicalLife = plx_enums.PropertyIDEnum.SystemWaterPlants_TechnicalLife

    SystemWaterPlants_BuildCost = plx_enums.PropertyIDEnum.SystemWaterPlants_BuildCost

    SystemWaterPlants_WACC = plx_enums.PropertyIDEnum.SystemWaterPlants_WACC

    SystemWaterPlants_EconomicLife = plx_enums.PropertyIDEnum.SystemWaterPlants_EconomicLife

    SystemWaterPlants_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterPlants_MinUnitsBuilt

    SystemWaterPlants_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterPlants_MaxUnitsBuiltinYear

    SystemWaterPlants_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterPlants_MinUnitsBuiltinYear

    SystemWaterPlants_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterPlants_MaxUnitsRetired

    SystemWaterPlants_RetirementCost = plx_enums.PropertyIDEnum.SystemWaterPlants_RetirementCost

    SystemWaterPlants_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterPlants_MinUnitsRetired

    SystemWaterPlants_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterPlants_MaxUnitsRetiredinYear

    SystemWaterPlants_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterPlants_MinUnitsRetiredinYear

    SystemWaterPlants_x = plx_enums.PropertyIDEnum.SystemWaterPlants_x

    SystemWaterPlants_y = plx_enums.PropertyIDEnum.SystemWaterPlants_y

    SystemWaterPlants_z = plx_enums.PropertyIDEnum.SystemWaterPlants_z

    SystemWaterPipelines_RandomNumberSeed = plx_enums.PropertyIDEnum.SystemWaterPipelines_RandomNumberSeed

    SystemWaterPipelines_RepairTimeDistribution = plx_enums.PropertyIDEnum.SystemWaterPipelines_RepairTimeDistribution

    SystemWaterPipelines_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemWaterPipelines_ExpansionOptimality

    SystemWaterPipelines_Units = plx_enums.PropertyIDEnum.SystemWaterPipelines_Units

    SystemWaterPipelines_MaxCapacity = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaxCapacity

    SystemWaterPipelines_Diameter = plx_enums.PropertyIDEnum.SystemWaterPipelines_Diameter

    SystemWaterPipelines_Roughness = plx_enums.PropertyIDEnum.SystemWaterPipelines_Roughness

    SystemWaterPipelines_Length = plx_enums.PropertyIDEnum.SystemWaterPipelines_Length

    SystemWaterPipelines_PumpEfficiency = plx_enums.PropertyIDEnum.SystemWaterPipelines_PumpEfficiency

    SystemWaterPipelines_VOMCharge = plx_enums.PropertyIDEnum.SystemWaterPipelines_VOMCharge

    SystemWaterPipelines_FOMCharge = plx_enums.PropertyIDEnum.SystemWaterPipelines_FOMCharge

    SystemWaterPipelines_ConsumptionAllocation = plx_enums.PropertyIDEnum.SystemWaterPipelines_ConsumptionAllocation

    SystemWaterPipelines_UnitsOut = plx_enums.PropertyIDEnum.SystemWaterPipelines_UnitsOut

    SystemWaterPipelines_MaintenanceRate = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaintenanceRate

    SystemWaterPipelines_MaintenanceFrequency = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaintenanceFrequency

    SystemWaterPipelines_ForcedOutageRate = plx_enums.PropertyIDEnum.SystemWaterPipelines_ForcedOutageRate

    SystemWaterPipelines_OutageRating = plx_enums.PropertyIDEnum.SystemWaterPipelines_OutageRating

    SystemWaterPipelines_MeanTimetoRepair = plx_enums.PropertyIDEnum.SystemWaterPipelines_MeanTimetoRepair

    SystemWaterPipelines_MinTimeToRepair = plx_enums.PropertyIDEnum.SystemWaterPipelines_MinTimeToRepair

    SystemWaterPipelines_MaxTimeToRepair = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaxTimeToRepair

    SystemWaterPipelines_RepairTimeShape = plx_enums.PropertyIDEnum.SystemWaterPipelines_RepairTimeShape

    SystemWaterPipelines_RepairTimeScale = plx_enums.PropertyIDEnum.SystemWaterPipelines_RepairTimeScale

    SystemWaterPipelines_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaxUnitsBuilt

    SystemWaterPipelines_LeadTime = plx_enums.PropertyIDEnum.SystemWaterPipelines_LeadTime

    SystemWaterPipelines_ProjectStartDate = plx_enums.PropertyIDEnum.SystemWaterPipelines_ProjectStartDate

    SystemWaterPipelines_TechnicalLife = plx_enums.PropertyIDEnum.SystemWaterPipelines_TechnicalLife

    SystemWaterPipelines_BuildCost = plx_enums.PropertyIDEnum.SystemWaterPipelines_BuildCost

    SystemWaterPipelines_WACC = plx_enums.PropertyIDEnum.SystemWaterPipelines_WACC

    SystemWaterPipelines_EconomicLife = plx_enums.PropertyIDEnum.SystemWaterPipelines_EconomicLife

    SystemWaterPipelines_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterPipelines_MinUnitsBuilt

    SystemWaterPipelines_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaxUnitsBuiltinYear

    SystemWaterPipelines_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterPipelines_MinUnitsBuiltinYear

    SystemWaterPipelines_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaxUnitsRetired

    SystemWaterPipelines_RetirementCost = plx_enums.PropertyIDEnum.SystemWaterPipelines_RetirementCost

    SystemWaterPipelines_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterPipelines_MinUnitsRetired

    SystemWaterPipelines_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterPipelines_MaxUnitsRetiredinYear

    SystemWaterPipelines_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterPipelines_MinUnitsRetiredinYear

    SystemWaterPipelines_x = plx_enums.PropertyIDEnum.SystemWaterPipelines_x

    SystemWaterPipelines_y = plx_enums.PropertyIDEnum.SystemWaterPipelines_y

    SystemWaterPipelines_z = plx_enums.PropertyIDEnum.SystemWaterPipelines_z

    SystemWaterNodes_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemWaterNodes_ExpansionOptimality

    SystemWaterNodes_Units = plx_enums.PropertyIDEnum.SystemWaterNodes_Units

    SystemWaterNodes_WaterSecurity = plx_enums.PropertyIDEnum.SystemWaterNodes_WaterSecurity

    SystemWaterNodes_FOMCharge = plx_enums.PropertyIDEnum.SystemWaterNodes_FOMCharge

    SystemWaterNodes_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterNodes_MaxUnitsBuilt

    SystemWaterNodes_LeadTime = plx_enums.PropertyIDEnum.SystemWaterNodes_LeadTime

    SystemWaterNodes_ProjectStartDate = plx_enums.PropertyIDEnum.SystemWaterNodes_ProjectStartDate

    SystemWaterNodes_TechnicalLife = plx_enums.PropertyIDEnum.SystemWaterNodes_TechnicalLife

    SystemWaterNodes_BuildCost = plx_enums.PropertyIDEnum.SystemWaterNodes_BuildCost

    SystemWaterNodes_WACC = plx_enums.PropertyIDEnum.SystemWaterNodes_WACC

    SystemWaterNodes_EconomicLife = plx_enums.PropertyIDEnum.SystemWaterNodes_EconomicLife

    SystemWaterNodes_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterNodes_MinUnitsBuilt

    SystemWaterNodes_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterNodes_MaxUnitsBuiltinYear

    SystemWaterNodes_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterNodes_MinUnitsBuiltinYear

    SystemWaterNodes_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterNodes_MaxUnitsRetired

    SystemWaterNodes_RetirementCost = plx_enums.PropertyIDEnum.SystemWaterNodes_RetirementCost

    SystemWaterNodes_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterNodes_MinUnitsRetired

    SystemWaterNodes_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterNodes_MaxUnitsRetiredinYear

    SystemWaterNodes_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterNodes_MinUnitsRetiredinYear

    SystemWaterNodes_x = plx_enums.PropertyIDEnum.SystemWaterNodes_x

    SystemWaterNodes_y = plx_enums.PropertyIDEnum.SystemWaterNodes_y

    SystemWaterNodes_z = plx_enums.PropertyIDEnum.SystemWaterNodes_z

    SystemWaterStorages_EnforceBounds = plx_enums.PropertyIDEnum.SystemWaterStorages_EnforceBounds

    SystemWaterStorages_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemWaterStorages_ExpansionOptimality

    SystemWaterStorages_Units = plx_enums.PropertyIDEnum.SystemWaterStorages_Units

    SystemWaterStorages_MaxVolume = plx_enums.PropertyIDEnum.SystemWaterStorages_MaxVolume

    SystemWaterStorages_MinVolume = plx_enums.PropertyIDEnum.SystemWaterStorages_MinVolume

    SystemWaterStorages_InitialVolume = plx_enums.PropertyIDEnum.SystemWaterStorages_InitialVolume

    SystemWaterStorages_Target = plx_enums.PropertyIDEnum.SystemWaterStorages_Target

    SystemWaterStorages_TargetHour = plx_enums.PropertyIDEnum.SystemWaterStorages_TargetHour

    SystemWaterStorages_TargetDay = plx_enums.PropertyIDEnum.SystemWaterStorages_TargetDay

    SystemWaterStorages_TargetWeek = plx_enums.PropertyIDEnum.SystemWaterStorages_TargetWeek

    SystemWaterStorages_TargetMonth = plx_enums.PropertyIDEnum.SystemWaterStorages_TargetMonth

    SystemWaterStorages_TargetYear = plx_enums.PropertyIDEnum.SystemWaterStorages_TargetYear

    SystemWaterStorages_TargetPenalty = plx_enums.PropertyIDEnum.SystemWaterStorages_TargetPenalty

    SystemWaterStorages_EnergyUsage = plx_enums.PropertyIDEnum.SystemWaterStorages_EnergyUsage

    SystemWaterStorages_NaturalInflow = plx_enums.PropertyIDEnum.SystemWaterStorages_NaturalInflow

    SystemWaterStorages_LossRate = plx_enums.PropertyIDEnum.SystemWaterStorages_LossRate

    SystemWaterStorages_FOMCharge = plx_enums.PropertyIDEnum.SystemWaterStorages_FOMCharge

    SystemWaterStorages_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterStorages_MaxUnitsBuilt

    SystemWaterStorages_LeadTime = plx_enums.PropertyIDEnum.SystemWaterStorages_LeadTime

    SystemWaterStorages_ProjectStartDate = plx_enums.PropertyIDEnum.SystemWaterStorages_ProjectStartDate

    SystemWaterStorages_TechnicalLife = plx_enums.PropertyIDEnum.SystemWaterStorages_TechnicalLife

    SystemWaterStorages_BuildCost = plx_enums.PropertyIDEnum.SystemWaterStorages_BuildCost

    SystemWaterStorages_WACC = plx_enums.PropertyIDEnum.SystemWaterStorages_WACC

    SystemWaterStorages_EconomicLife = plx_enums.PropertyIDEnum.SystemWaterStorages_EconomicLife

    SystemWaterStorages_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemWaterStorages_MinUnitsBuilt

    SystemWaterStorages_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterStorages_MaxUnitsBuiltinYear

    SystemWaterStorages_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemWaterStorages_MinUnitsBuiltinYear

    SystemWaterStorages_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterStorages_MaxUnitsRetired

    SystemWaterStorages_RetirementCost = plx_enums.PropertyIDEnum.SystemWaterStorages_RetirementCost

    SystemWaterStorages_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemWaterStorages_MinUnitsRetired

    SystemWaterStorages_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterStorages_MaxUnitsRetiredinYear

    SystemWaterStorages_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemWaterStorages_MinUnitsRetiredinYear

    SystemWaterStorages_TrajectoryNonanticipativity = plx_enums.PropertyIDEnum.SystemWaterStorages_TrajectoryNonanticipativity

    SystemWaterStorages_TrajectoryNonanticipativityVolume = plx_enums.PropertyIDEnum.SystemWaterStorages_TrajectoryNonanticipativityVolume

    SystemWaterStorages_TrajectoryNonanticipativityTime = plx_enums.PropertyIDEnum.SystemWaterStorages_TrajectoryNonanticipativityTime

    SystemWaterStorages_x = plx_enums.PropertyIDEnum.SystemWaterStorages_x

    SystemWaterStorages_y = plx_enums.PropertyIDEnum.SystemWaterStorages_y

    SystemWaterStorages_z = plx_enums.PropertyIDEnum.SystemWaterStorages_z

    SystemWaterDemands_Demand = plx_enums.PropertyIDEnum.SystemWaterDemands_Demand

    SystemWaterDemands_ShortagePrice = plx_enums.PropertyIDEnum.SystemWaterDemands_ShortagePrice

    SystemWaterDemands_ExcessPrice = plx_enums.PropertyIDEnum.SystemWaterDemands_ExcessPrice

    SystemWaterDemands_BidQuantity = plx_enums.PropertyIDEnum.SystemWaterDemands_BidQuantity

    SystemWaterDemands_BidPrice = plx_enums.PropertyIDEnum.SystemWaterDemands_BidPrice

    SystemWaterDemands_x = plx_enums.PropertyIDEnum.SystemWaterDemands_x

    SystemWaterDemands_y = plx_enums.PropertyIDEnum.SystemWaterDemands_y

    SystemWaterDemands_z = plx_enums.PropertyIDEnum.SystemWaterDemands_z

    SystemWaterZones_x = plx_enums.PropertyIDEnum.SystemWaterZones_x

    SystemWaterZones_y = plx_enums.PropertyIDEnum.SystemWaterZones_y

    SystemWaterZones_z = plx_enums.PropertyIDEnum.SystemWaterZones_z

    SystemRegions_GeneratorSettlementModel = plx_enums.PropertyIDEnum.SystemRegions_GeneratorSettlementModel

    SystemRegions_LoadSettlementModel = plx_enums.PropertyIDEnum.SystemRegions_LoadSettlementModel

    SystemRegions_UniformPricingPumpedStoragePriceSetting = plx_enums.PropertyIDEnum.SystemRegions_UniformPricingPumpedStoragePriceSetting

    SystemRegions_UniformPricingRelaxTransmissionLimits = plx_enums.PropertyIDEnum.SystemRegions_UniformPricingRelaxTransmissionLimits

    SystemRegions_UniformPricingRelaxGenericConstraints = plx_enums.PropertyIDEnum.SystemRegions_UniformPricingRelaxGenericConstraints

    SystemRegions_UniformPricingRelaxGeneratorConstraints = plx_enums.PropertyIDEnum.SystemRegions_UniformPricingRelaxGeneratorConstraints

    SystemRegions_UniformPricingRelaxAncillaryServices = plx_enums.PropertyIDEnum.SystemRegions_UniformPricingRelaxAncillaryServices

    SystemRegions_UpliftEnabled = plx_enums.PropertyIDEnum.SystemRegions_UpliftEnabled

    SystemRegions_UpliftCostBasis = plx_enums.PropertyIDEnum.SystemRegions_UpliftCostBasis

    SystemRegions_UpliftCompatibility = plx_enums.PropertyIDEnum.SystemRegions_UpliftCompatibility

    SystemRegions_UpliftAlpha = plx_enums.PropertyIDEnum.SystemRegions_UpliftAlpha

    SystemRegions_UpliftBeta = plx_enums.PropertyIDEnum.SystemRegions_UpliftBeta

    SystemRegions_UpliftDelta = plx_enums.PropertyIDEnum.SystemRegions_UpliftDelta

    SystemRegions_UpliftIncludeStartCost = plx_enums.PropertyIDEnum.SystemRegions_UpliftIncludeStartCost

    SystemRegions_UpliftIncludeNoLoadCost = plx_enums.PropertyIDEnum.SystemRegions_UpliftIncludeNoLoadCost

    SystemRegions_UpliftDetectActiveMinStableLevelConstraints = plx_enums.PropertyIDEnum.SystemRegions_UpliftDetectActiveMinStableLevelConstraints

    SystemRegions_UpliftDetectActiveRampConstraints = plx_enums.PropertyIDEnum.SystemRegions_UpliftDetectActiveRampConstraints

    SystemRegions_IncludeinMarginalUnit = plx_enums.PropertyIDEnum.SystemRegions_IncludeinMarginalUnit

    SystemRegions_IncludeinUplift = plx_enums.PropertyIDEnum.SystemRegions_IncludeinUplift

    SystemRegions_ConstraintPaymentsEnabled = plx_enums.PropertyIDEnum.SystemRegions_ConstraintPaymentsEnabled

    SystemRegions_ConstraintPaymentsCompatibility = plx_enums.PropertyIDEnum.SystemRegions_ConstraintPaymentsCompatibility

    SystemRegions_LoadMeteringPoint = plx_enums.PropertyIDEnum.SystemRegions_LoadMeteringPoint

    SystemRegions_LoadIncludesLosses = plx_enums.PropertyIDEnum.SystemRegions_LoadIncludesLosses

    SystemRegions_AggregateTransmission = plx_enums.PropertyIDEnum.SystemRegions_AggregateTransmission

    SystemRegions_PoolType = plx_enums.PropertyIDEnum.SystemRegions_PoolType

    SystemRegions_MLFAdjustsOfferPrice = plx_enums.PropertyIDEnum.SystemRegions_MLFAdjustsOfferPrice

    SystemRegions_MLFAdjustsBidPrice = plx_enums.PropertyIDEnum.SystemRegions_MLFAdjustsBidPrice

    SystemRegions_MLFAdjustsNoLoadCost = plx_enums.PropertyIDEnum.SystemRegions_MLFAdjustsNoLoadCost

    SystemRegions_MLFAdjustsStartCost = plx_enums.PropertyIDEnum.SystemRegions_MLFAdjustsStartCost

    SystemRegions_IncludeinRegionSupply = plx_enums.PropertyIDEnum.SystemRegions_IncludeinRegionSupply

    SystemRegions_TransmissionConstraintsEnabled = plx_enums.PropertyIDEnum.SystemRegions_TransmissionConstraintsEnabled

    SystemRegions_TransmissionConstraintVoltageThreshold = plx_enums.PropertyIDEnum.SystemRegions_TransmissionConstraintVoltageThreshold

    SystemRegions_TransmissionInterfaceConstraintsEnabled = plx_enums.PropertyIDEnum.SystemRegions_TransmissionInterfaceConstraintsEnabled

    SystemRegions_EnforceTransmissionLimitsOnLinesInInterfaces = plx_enums.PropertyIDEnum.SystemRegions_EnforceTransmissionLimitsOnLinesInInterfaces

    SystemRegions_TransmissionReportEnabled = plx_enums.PropertyIDEnum.SystemRegions_TransmissionReportEnabled

    SystemRegions_TransmissionReportVoltageThreshold = plx_enums.PropertyIDEnum.SystemRegions_TransmissionReportVoltageThreshold

    SystemRegions_TransmissionReportLinesInInterfaces = plx_enums.PropertyIDEnum.SystemRegions_TransmissionReportLinesInInterfaces

    SystemRegions_TransmissionReportInjectionandLoadNodes = plx_enums.PropertyIDEnum.SystemRegions_TransmissionReportInjectionandLoadNodes

    SystemRegions_ReportObjectsinRegion = plx_enums.PropertyIDEnum.SystemRegions_ReportObjectsinRegion

    SystemRegions_WheelingMethod = plx_enums.PropertyIDEnum.SystemRegions_WheelingMethod

    SystemRegions_Units = plx_enums.PropertyIDEnum.SystemRegions_Units

    SystemRegions_Load = plx_enums.PropertyIDEnum.SystemRegions_Load

    SystemRegions_LoadScalar = plx_enums.PropertyIDEnum.SystemRegions_LoadScalar

    SystemRegions_FixedLoad = plx_enums.PropertyIDEnum.SystemRegions_FixedLoad

    SystemRegions_FixedGeneration = plx_enums.PropertyIDEnum.SystemRegions_FixedGeneration

    SystemRegions_VoLL = plx_enums.PropertyIDEnum.SystemRegions_VoLL

    SystemRegions_PriceofDumpEnergy = plx_enums.PropertyIDEnum.SystemRegions_PriceofDumpEnergy

    SystemRegions_PriceCap = plx_enums.PropertyIDEnum.SystemRegions_PriceCap

    SystemRegions_PriceFloor = plx_enums.PropertyIDEnum.SystemRegions_PriceFloor

    SystemRegions_Price = plx_enums.PropertyIDEnum.SystemRegions_Price

    SystemRegions_WheelingCharge = plx_enums.PropertyIDEnum.SystemRegions_WheelingCharge

    SystemRegions_FixedCostScalar = plx_enums.PropertyIDEnum.SystemRegions_FixedCostScalar

    SystemRegions_Elasticity = plx_enums.PropertyIDEnum.SystemRegions_Elasticity

    SystemRegions_ReferenceLoad = plx_enums.PropertyIDEnum.SystemRegions_ReferenceLoad

    SystemRegions_DSPBidQuantity = plx_enums.PropertyIDEnum.SystemRegions_DSPBidQuantity

    SystemRegions_DSPBidPrice = plx_enums.PropertyIDEnum.SystemRegions_DSPBidPrice

    SystemRegions_IsStrategic = plx_enums.PropertyIDEnum.SystemRegions_IsStrategic

    SystemRegions_MaxMaintenance = plx_enums.PropertyIDEnum.SystemRegions_MaxMaintenance

    SystemRegions_MaintenanceFactor = plx_enums.PropertyIDEnum.SystemRegions_MaintenanceFactor

    SystemRegions_PeakPeriod = plx_enums.PropertyIDEnum.SystemRegions_PeakPeriod

    SystemRegions_FirmCapacityIncr = plx_enums.PropertyIDEnum.SystemRegions_FirmCapacityIncr

    SystemRegions_MinCapacityReserves = plx_enums.PropertyIDEnum.SystemRegions_MinCapacityReserves

    SystemRegions_MaxCapacityReserves = plx_enums.PropertyIDEnum.SystemRegions_MaxCapacityReserves

    SystemRegions_MinCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemRegions_MinCapacityReserveMargin

    SystemRegions_MaxCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemRegions_MaxCapacityReserveMargin

    SystemRegions_MinNativeCapacityReserves = plx_enums.PropertyIDEnum.SystemRegions_MinNativeCapacityReserves

    SystemRegions_MinNativeCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemRegions_MinNativeCapacityReserveMargin

    SystemRegions_CapacityShortagePrice = plx_enums.PropertyIDEnum.SystemRegions_CapacityShortagePrice

    SystemRegions_CapacityExcessPrice = plx_enums.PropertyIDEnum.SystemRegions_CapacityExcessPrice

    SystemRegions_CapacityPriceCap = plx_enums.PropertyIDEnum.SystemRegions_CapacityPriceCap

    SystemRegions_CapacityPriceFloor = plx_enums.PropertyIDEnum.SystemRegions_CapacityPriceFloor

    SystemRegions_LOLPTarget = plx_enums.PropertyIDEnum.SystemRegions_LOLPTarget

    SystemRegions_x = plx_enums.PropertyIDEnum.SystemRegions_x

    SystemRegions_y = plx_enums.PropertyIDEnum.SystemRegions_y

    SystemRegions_z = plx_enums.PropertyIDEnum.SystemRegions_z

    SystemZones_LoadSettlementModel = plx_enums.PropertyIDEnum.SystemZones_LoadSettlementModel

    SystemZones_WheelingMethod = plx_enums.PropertyIDEnum.SystemZones_WheelingMethod

    SystemZones_Units = plx_enums.PropertyIDEnum.SystemZones_Units

    SystemZones_Load = plx_enums.PropertyIDEnum.SystemZones_Load

    SystemZones_LoadParticipationFactor = plx_enums.PropertyIDEnum.SystemZones_LoadParticipationFactor

    SystemZones_LoadScalar = plx_enums.PropertyIDEnum.SystemZones_LoadScalar

    SystemZones_WheelingCharge = plx_enums.PropertyIDEnum.SystemZones_WheelingCharge

    SystemZones_MaxMaintenance = plx_enums.PropertyIDEnum.SystemZones_MaxMaintenance

    SystemZones_MaintenanceFactor = plx_enums.PropertyIDEnum.SystemZones_MaintenanceFactor

    SystemZones_PeakPeriod = plx_enums.PropertyIDEnum.SystemZones_PeakPeriod

    SystemZones_FirmCapacityIncr = plx_enums.PropertyIDEnum.SystemZones_FirmCapacityIncr

    SystemZones_MinCapacityReserves = plx_enums.PropertyIDEnum.SystemZones_MinCapacityReserves

    SystemZones_MaxCapacityReserves = plx_enums.PropertyIDEnum.SystemZones_MaxCapacityReserves

    SystemZones_MinCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemZones_MinCapacityReserveMargin

    SystemZones_MaxCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemZones_MaxCapacityReserveMargin

    SystemZones_MinNativeCapacityReserves = plx_enums.PropertyIDEnum.SystemZones_MinNativeCapacityReserves

    SystemZones_MinNativeCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemZones_MinNativeCapacityReserveMargin

    SystemZones_CapacityShortagePrice = plx_enums.PropertyIDEnum.SystemZones_CapacityShortagePrice

    SystemZones_CapacityExcessPrice = plx_enums.PropertyIDEnum.SystemZones_CapacityExcessPrice

    SystemZones_CapacityPriceCap = plx_enums.PropertyIDEnum.SystemZones_CapacityPriceCap

    SystemZones_CapacityPriceFloor = plx_enums.PropertyIDEnum.SystemZones_CapacityPriceFloor

    SystemZones_LOLPTarget = plx_enums.PropertyIDEnum.SystemZones_LOLPTarget

    SystemZones_x = plx_enums.PropertyIDEnum.SystemZones_x

    SystemZones_y = plx_enums.PropertyIDEnum.SystemZones_y

    SystemZones_z = plx_enums.PropertyIDEnum.SystemZones_z

    SystemNodes_MustReport = plx_enums.PropertyIDEnum.SystemNodes_MustReport

    SystemNodes_IsSlackBus = plx_enums.PropertyIDEnum.SystemNodes_IsSlackBus

    SystemNodes_AllowDumpEnergy = plx_enums.PropertyIDEnum.SystemNodes_AllowDumpEnergy

    SystemNodes_AllowUnservedEnergy = plx_enums.PropertyIDEnum.SystemNodes_AllowUnservedEnergy

    SystemNodes_ReferenceLoad = plx_enums.PropertyIDEnum.SystemNodes_ReferenceLoad

    SystemNodes_Voltage = plx_enums.PropertyIDEnum.SystemNodes_Voltage

    SystemNodes_Units = plx_enums.PropertyIDEnum.SystemNodes_Units

    SystemNodes_LoadParticipationFactor = plx_enums.PropertyIDEnum.SystemNodes_LoadParticipationFactor

    SystemNodes_Load = plx_enums.PropertyIDEnum.SystemNodes_Load

    SystemNodes_FixedLoad = plx_enums.PropertyIDEnum.SystemNodes_FixedLoad

    SystemNodes_FixedGeneration = plx_enums.PropertyIDEnum.SystemNodes_FixedGeneration

    SystemNodes_MaxNetInjection = plx_enums.PropertyIDEnum.SystemNodes_MaxNetInjection

    SystemNodes_MaxNetOfftake = plx_enums.PropertyIDEnum.SystemNodes_MaxNetOfftake

    SystemNodes_Rating = plx_enums.PropertyIDEnum.SystemNodes_Rating

    SystemNodes_DSPBidQuantity = plx_enums.PropertyIDEnum.SystemNodes_DSPBidQuantity

    SystemNodes_DSPBidRatio = plx_enums.PropertyIDEnum.SystemNodes_DSPBidRatio

    SystemNodes_DSPBidPrice = plx_enums.PropertyIDEnum.SystemNodes_DSPBidPrice

    SystemNodes_Price = plx_enums.PropertyIDEnum.SystemNodes_Price

    SystemNodes_MaxMaintenance = plx_enums.PropertyIDEnum.SystemNodes_MaxMaintenance

    SystemNodes_MaintenanceFactor = plx_enums.PropertyIDEnum.SystemNodes_MaintenanceFactor

    SystemNodes_MinCapacityReserves = plx_enums.PropertyIDEnum.SystemNodes_MinCapacityReserves

    SystemNodes_MinCapacityReserveMargin = plx_enums.PropertyIDEnum.SystemNodes_MinCapacityReserveMargin

    SystemNodes_x = plx_enums.PropertyIDEnum.SystemNodes_x

    SystemNodes_y = plx_enums.PropertyIDEnum.SystemNodes_y

    SystemNodes_z = plx_enums.PropertyIDEnum.SystemNodes_z

    SystemLines_MustReport = plx_enums.PropertyIDEnum.SystemLines_MustReport

    SystemLines_RandomNumberSeed = plx_enums.PropertyIDEnum.SystemLines_RandomNumberSeed

    SystemLines_RepairTimeDistribution = plx_enums.PropertyIDEnum.SystemLines_RepairTimeDistribution

    SystemLines_EnforceLimits = plx_enums.PropertyIDEnum.SystemLines_EnforceLimits

    SystemLines_FormulateUpfront = plx_enums.PropertyIDEnum.SystemLines_FormulateUpfront

    SystemLines_FormulateNPLUpfront = plx_enums.PropertyIDEnum.SystemLines_FormulateNPLUpfront

    SystemLines_MaxLossTranches = plx_enums.PropertyIDEnum.SystemLines_MaxLossTranches

    SystemLines_PriceSetting = plx_enums.PropertyIDEnum.SystemLines_PriceSetting

    SystemLines_OfferQuantityFormat = plx_enums.PropertyIDEnum.SystemLines_OfferQuantityFormat

    SystemLines_FixedFlowMethod = plx_enums.PropertyIDEnum.SystemLines_FixedFlowMethod

    SystemLines_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemLines_ExpansionOptimality

    SystemLines_Units = plx_enums.PropertyIDEnum.SystemLines_Units

    SystemLines_MaxFlow = plx_enums.PropertyIDEnum.SystemLines_MaxFlow

    SystemLines_MinFlow = plx_enums.PropertyIDEnum.SystemLines_MinFlow

    SystemLines_MaxRating = plx_enums.PropertyIDEnum.SystemLines_MaxRating

    SystemLines_MinRating = plx_enums.PropertyIDEnum.SystemLines_MinRating

    SystemLines_OverloadMaxRating = plx_enums.PropertyIDEnum.SystemLines_OverloadMaxRating

    SystemLines_OverloadMinRating = plx_enums.PropertyIDEnum.SystemLines_OverloadMinRating

    SystemLines_LimitPenalty = plx_enums.PropertyIDEnum.SystemLines_LimitPenalty

    SystemLines_Resistance = plx_enums.PropertyIDEnum.SystemLines_Resistance

    SystemLines_Reactance = plx_enums.PropertyIDEnum.SystemLines_Reactance

    SystemLines_Susceptance = plx_enums.PropertyIDEnum.SystemLines_Susceptance

    SystemLines_MaxRampUp = plx_enums.PropertyIDEnum.SystemLines_MaxRampUp

    SystemLines_MaxRampDown = plx_enums.PropertyIDEnum.SystemLines_MaxRampDown

    SystemLines_RampPenalty = plx_enums.PropertyIDEnum.SystemLines_RampPenalty

    SystemLines_LossBase = plx_enums.PropertyIDEnum.SystemLines_LossBase

    SystemLines_LossIncr = plx_enums.PropertyIDEnum.SystemLines_LossIncr

    SystemLines_LossIncr2 = plx_enums.PropertyIDEnum.SystemLines_LossIncr2

    SystemLines_LossBaseBack = plx_enums.PropertyIDEnum.SystemLines_LossBaseBack

    SystemLines_LossIncrBack = plx_enums.PropertyIDEnum.SystemLines_LossIncrBack

    SystemLines_LossIncr2Back = plx_enums.PropertyIDEnum.SystemLines_LossIncr2Back

    SystemLines_LossAllocation = plx_enums.PropertyIDEnum.SystemLines_LossAllocation

    SystemLines_FixedFlow = plx_enums.PropertyIDEnum.SystemLines_FixedFlow

    SystemLines_FixedFlowPenalty = plx_enums.PropertyIDEnum.SystemLines_FixedFlowPenalty

    SystemLines_FixedLoss = plx_enums.PropertyIDEnum.SystemLines_FixedLoss

    SystemLines_WheelingCharge = plx_enums.PropertyIDEnum.SystemLines_WheelingCharge

    SystemLines_WheelingChargeBack = plx_enums.PropertyIDEnum.SystemLines_WheelingChargeBack

    SystemLines_OfferBase = plx_enums.PropertyIDEnum.SystemLines_OfferBase

    SystemLines_OfferQuantity = plx_enums.PropertyIDEnum.SystemLines_OfferQuantity

    SystemLines_OfferPrice = plx_enums.PropertyIDEnum.SystemLines_OfferPrice

    SystemLines_OfferQuantityBack = plx_enums.PropertyIDEnum.SystemLines_OfferQuantityBack

    SystemLines_OfferPriceBack = plx_enums.PropertyIDEnum.SystemLines_OfferPriceBack

    SystemLines_MarginalLossFactor = plx_enums.PropertyIDEnum.SystemLines_MarginalLossFactor

    SystemLines_MarginalLossFactorBack = plx_enums.PropertyIDEnum.SystemLines_MarginalLossFactorBack

    SystemLines_FlowNonanticipativity = plx_enums.PropertyIDEnum.SystemLines_FlowNonanticipativity

    SystemLines_FlowNonanticipativityTime = plx_enums.PropertyIDEnum.SystemLines_FlowNonanticipativityTime

    SystemLines_FixedCharge = plx_enums.PropertyIDEnum.SystemLines_FixedCharge

    SystemLines_FOMCharge = plx_enums.PropertyIDEnum.SystemLines_FOMCharge

    SystemLines_EquityCharge = plx_enums.PropertyIDEnum.SystemLines_EquityCharge

    SystemLines_DebtCharge = plx_enums.PropertyIDEnum.SystemLines_DebtCharge

    SystemLines_Circuits = plx_enums.PropertyIDEnum.SystemLines_Circuits

    SystemLines_UnitsOut = plx_enums.PropertyIDEnum.SystemLines_UnitsOut

    SystemLines_MaintenanceRate = plx_enums.PropertyIDEnum.SystemLines_MaintenanceRate

    SystemLines_MaintenanceFrequency = plx_enums.PropertyIDEnum.SystemLines_MaintenanceFrequency

    SystemLines_ForcedOutageRate = plx_enums.PropertyIDEnum.SystemLines_ForcedOutageRate

    SystemLines_OutageMaxRating = plx_enums.PropertyIDEnum.SystemLines_OutageMaxRating

    SystemLines_OutageMinRating = plx_enums.PropertyIDEnum.SystemLines_OutageMinRating

    SystemLines_MeanTimetoRepair = plx_enums.PropertyIDEnum.SystemLines_MeanTimetoRepair

    SystemLines_MinTimeToRepair = plx_enums.PropertyIDEnum.SystemLines_MinTimeToRepair

    SystemLines_MaxTimeToRepair = plx_enums.PropertyIDEnum.SystemLines_MaxTimeToRepair

    SystemLines_RepairTimeShape = plx_enums.PropertyIDEnum.SystemLines_RepairTimeShape

    SystemLines_RepairTimeScale = plx_enums.PropertyIDEnum.SystemLines_RepairTimeScale

    SystemLines_MaxCapacityReserves = plx_enums.PropertyIDEnum.SystemLines_MaxCapacityReserves

    SystemLines_MinCapacityReserves = plx_enums.PropertyIDEnum.SystemLines_MinCapacityReserves

    SystemLines_FirmCapacity = plx_enums.PropertyIDEnum.SystemLines_FirmCapacity

    SystemLines_Type = plx_enums.PropertyIDEnum.SystemLines_Type

    SystemLines_BuildCost = plx_enums.PropertyIDEnum.SystemLines_BuildCost

    SystemLines_RetirementCost = plx_enums.PropertyIDEnum.SystemLines_RetirementCost

    SystemLines_LeadTime = plx_enums.PropertyIDEnum.SystemLines_LeadTime

    SystemLines_ProjectStartDate = plx_enums.PropertyIDEnum.SystemLines_ProjectStartDate

    SystemLines_CommissionDate = plx_enums.PropertyIDEnum.SystemLines_CommissionDate

    SystemLines_TechnicalLife = plx_enums.PropertyIDEnum.SystemLines_TechnicalLife

    SystemLines_WACC = plx_enums.PropertyIDEnum.SystemLines_WACC

    SystemLines_EconomicLife = plx_enums.PropertyIDEnum.SystemLines_EconomicLife

    SystemLines_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemLines_MaxUnitsBuilt

    SystemLines_MaxUnitsRetired = plx_enums.PropertyIDEnum.SystemLines_MaxUnitsRetired

    SystemLines_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemLines_MinUnitsBuilt

    SystemLines_MinUnitsRetired = plx_enums.PropertyIDEnum.SystemLines_MinUnitsRetired

    SystemLines_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemLines_MaxUnitsBuiltinYear

    SystemLines_MaxUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemLines_MaxUnitsRetiredinYear

    SystemLines_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemLines_MinUnitsBuiltinYear

    SystemLines_MinUnitsRetiredinYear = plx_enums.PropertyIDEnum.SystemLines_MinUnitsRetiredinYear

    SystemLines_BuildNonanticipativity = plx_enums.PropertyIDEnum.SystemLines_BuildNonanticipativity

    SystemLines_RetireNonanticipativity = plx_enums.PropertyIDEnum.SystemLines_RetireNonanticipativity

    SystemLines_x = plx_enums.PropertyIDEnum.SystemLines_x

    SystemLines_y = plx_enums.PropertyIDEnum.SystemLines_y

    SystemLines_z = plx_enums.PropertyIDEnum.SystemLines_z

    SystemMLFs_Intercept = plx_enums.PropertyIDEnum.SystemMLFs_Intercept

    SystemMLFs_FlowCoefficient = plx_enums.PropertyIDEnum.SystemMLFs_FlowCoefficient

    SystemTransformers_MustReport = plx_enums.PropertyIDEnum.SystemTransformers_MustReport

    SystemTransformers_EnforceLimits = plx_enums.PropertyIDEnum.SystemTransformers_EnforceLimits

    SystemTransformers_FormulateUpfront = plx_enums.PropertyIDEnum.SystemTransformers_FormulateUpfront

    SystemTransformers_Units = plx_enums.PropertyIDEnum.SystemTransformers_Units

    SystemTransformers_Rating = plx_enums.PropertyIDEnum.SystemTransformers_Rating

    SystemTransformers_OverloadRating = plx_enums.PropertyIDEnum.SystemTransformers_OverloadRating

    SystemTransformers_LimitPenalty = plx_enums.PropertyIDEnum.SystemTransformers_LimitPenalty

    SystemTransformers_Resistance = plx_enums.PropertyIDEnum.SystemTransformers_Resistance

    SystemTransformers_Reactance = plx_enums.PropertyIDEnum.SystemTransformers_Reactance

    SystemTransformers_Susceptance = plx_enums.PropertyIDEnum.SystemTransformers_Susceptance

    SystemTransformers_LossAllocation = plx_enums.PropertyIDEnum.SystemTransformers_LossAllocation

    SystemTransformers_FixedLoss = plx_enums.PropertyIDEnum.SystemTransformers_FixedLoss

    SystemTransformers_UnitsOut = plx_enums.PropertyIDEnum.SystemTransformers_UnitsOut

    SystemTransformers_x = plx_enums.PropertyIDEnum.SystemTransformers_x

    SystemTransformers_y = plx_enums.PropertyIDEnum.SystemTransformers_y

    SystemTransformers_z = plx_enums.PropertyIDEnum.SystemTransformers_z

    SystemFlowControls_PriceSetting = plx_enums.PropertyIDEnum.SystemFlowControls_PriceSetting

    SystemFlowControls_ExpansionOptimality = plx_enums.PropertyIDEnum.SystemFlowControls_ExpansionOptimality

    SystemFlowControls_Type = plx_enums.PropertyIDEnum.SystemFlowControls_Type

    SystemFlowControls_Units = plx_enums.PropertyIDEnum.SystemFlowControls_Units

    SystemFlowControls_MinAngle = plx_enums.PropertyIDEnum.SystemFlowControls_MinAngle

    SystemFlowControls_MaxAngle = plx_enums.PropertyIDEnum.SystemFlowControls_MaxAngle

    SystemFlowControls_MinImpedance = plx_enums.PropertyIDEnum.SystemFlowControls_MinImpedance

    SystemFlowControls_MaxImpedance = plx_enums.PropertyIDEnum.SystemFlowControls_MaxImpedance

    SystemFlowControls_MinVoltage = plx_enums.PropertyIDEnum.SystemFlowControls_MinVoltage

    SystemFlowControls_MaxVoltage = plx_enums.PropertyIDEnum.SystemFlowControls_MaxVoltage

    SystemFlowControls_Penalty = plx_enums.PropertyIDEnum.SystemFlowControls_Penalty

    SystemFlowControls_Angle = plx_enums.PropertyIDEnum.SystemFlowControls_Angle

    SystemFlowControls_AnglePoints = plx_enums.PropertyIDEnum.SystemFlowControls_AnglePoints

    SystemFlowControls_FlowLoadingPoints = plx_enums.PropertyIDEnum.SystemFlowControls_FlowLoadingPoints

    SystemFlowControls_FOMCharge = plx_enums.PropertyIDEnum.SystemFlowControls_FOMCharge

    SystemFlowControls_BuildCost = plx_enums.PropertyIDEnum.SystemFlowControls_BuildCost

    SystemFlowControls_LeadTime = plx_enums.PropertyIDEnum.SystemFlowControls_LeadTime

    SystemFlowControls_ProjectStartDate = plx_enums.PropertyIDEnum.SystemFlowControls_ProjectStartDate

    SystemFlowControls_CommissionDate = plx_enums.PropertyIDEnum.SystemFlowControls_CommissionDate

    SystemFlowControls_TechnicalLife = plx_enums.PropertyIDEnum.SystemFlowControls_TechnicalLife

    SystemFlowControls_WACC = plx_enums.PropertyIDEnum.SystemFlowControls_WACC

    SystemFlowControls_EconomicLife = plx_enums.PropertyIDEnum.SystemFlowControls_EconomicLife

    SystemFlowControls_MaxUnitsBuilt = plx_enums.PropertyIDEnum.SystemFlowControls_MaxUnitsBuilt

    SystemFlowControls_MinUnitsBuilt = plx_enums.PropertyIDEnum.SystemFlowControls_MinUnitsBuilt

    SystemFlowControls_MaxUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemFlowControls_MaxUnitsBuiltinYear

    SystemFlowControls_MinUnitsBuiltinYear = plx_enums.PropertyIDEnum.SystemFlowControls_MinUnitsBuiltinYear

    SystemFlowControls_BuildNonanticipativity = plx_enums.PropertyIDEnum.SystemFlowControls_BuildNonanticipativity

    SystemFlowControls_x = plx_enums.PropertyIDEnum.SystemFlowControls_x

    SystemFlowControls_y = plx_enums.PropertyIDEnum.SystemFlowControls_y

    SystemFlowControls_z = plx_enums.PropertyIDEnum.SystemFlowControls_z

    SystemInterfaces_FormulateUpfront = plx_enums.PropertyIDEnum.SystemInterfaces_FormulateUpfront

    SystemInterfaces_OfferQuantityFormat = plx_enums.PropertyIDEnum.SystemInterfaces_OfferQuantityFormat

    SystemInterfaces_Units = plx_enums.PropertyIDEnum.SystemInterfaces_Units

    SystemInterfaces_MinFlow = plx_enums.PropertyIDEnum.SystemInterfaces_MinFlow

    SystemInterfaces_MaxFlow = plx_enums.PropertyIDEnum.SystemInterfaces_MaxFlow

    SystemInterfaces_OverloadMaxRating = plx_enums.PropertyIDEnum.SystemInterfaces_OverloadMaxRating

    SystemInterfaces_OverloadMinRating = plx_enums.PropertyIDEnum.SystemInterfaces_OverloadMinRating

    SystemInterfaces_LimitPenalty = plx_enums.PropertyIDEnum.SystemInterfaces_LimitPenalty

    SystemInterfaces_MaxRampUp = plx_enums.PropertyIDEnum.SystemInterfaces_MaxRampUp

    SystemInterfaces_MaxRampDown = plx_enums.PropertyIDEnum.SystemInterfaces_MaxRampDown

    SystemInterfaces_RampPenalty = plx_enums.PropertyIDEnum.SystemInterfaces_RampPenalty

    SystemInterfaces_FixedFlow = plx_enums.PropertyIDEnum.SystemInterfaces_FixedFlow

    SystemInterfaces_FixedFlowPenalty = plx_enums.PropertyIDEnum.SystemInterfaces_FixedFlowPenalty

    SystemInterfaces_OfferBase = plx_enums.PropertyIDEnum.SystemInterfaces_OfferBase

    SystemInterfaces_OfferQuantity = plx_enums.PropertyIDEnum.SystemInterfaces_OfferQuantity

    SystemInterfaces_OfferPrice = plx_enums.PropertyIDEnum.SystemInterfaces_OfferPrice

    SystemInterfaces_OfferQuantityBack = plx_enums.PropertyIDEnum.SystemInterfaces_OfferQuantityBack

    SystemInterfaces_OfferPriceBack = plx_enums.PropertyIDEnum.SystemInterfaces_OfferPriceBack

    SystemInterfaces_FlowNonanticipativity = plx_enums.PropertyIDEnum.SystemInterfaces_FlowNonanticipativity

    SystemInterfaces_FlowNonanticipativityTime = plx_enums.PropertyIDEnum.SystemInterfaces_FlowNonanticipativityTime

    SystemInterfaces_FirmCapacity = plx_enums.PropertyIDEnum.SystemInterfaces_FirmCapacity

    SystemInterfaces_ExpansionCost = plx_enums.PropertyIDEnum.SystemInterfaces_ExpansionCost

    SystemInterfaces_MaxExpansion = plx_enums.PropertyIDEnum.SystemInterfaces_MaxExpansion

    SystemInterfaces_WACC = plx_enums.PropertyIDEnum.SystemInterfaces_WACC

    SystemInterfaces_EconomicLife = plx_enums.PropertyIDEnum.SystemInterfaces_EconomicLife

    SystemInterfaces_BuildNonanticipativity = plx_enums.PropertyIDEnum.SystemInterfaces_BuildNonanticipativity

    SystemInterfaces_x = plx_enums.PropertyIDEnum.SystemInterfaces_x

    SystemInterfaces_y = plx_enums.PropertyIDEnum.SystemInterfaces_y

    SystemInterfaces_z = plx_enums.PropertyIDEnum.SystemInterfaces_z

    SystemContingencies_IsEnabled = plx_enums.PropertyIDEnum.SystemContingencies_IsEnabled

    SystemContingencies_MonitoringThreshold = plx_enums.PropertyIDEnum.SystemContingencies_MonitoringThreshold

    SystemContingencies_x = plx_enums.PropertyIDEnum.SystemContingencies_x

    SystemContingencies_y = plx_enums.PropertyIDEnum.SystemContingencies_y

    SystemContingencies_z = plx_enums.PropertyIDEnum.SystemContingencies_z

    SystemCompanies_Strategic = plx_enums.PropertyIDEnum.SystemCompanies_Strategic

    SystemCompanies_MarkupBias = plx_enums.PropertyIDEnum.SystemCompanies_MarkupBias

    SystemCompanies_FormulateRisk = plx_enums.PropertyIDEnum.SystemCompanies_FormulateRisk

    SystemCompanies_RiskLevel = plx_enums.PropertyIDEnum.SystemCompanies_RiskLevel

    SystemCompanies_AcceptableRisk = plx_enums.PropertyIDEnum.SystemCompanies_AcceptableRisk

    SystemCompanies_MaxMaintenance = plx_enums.PropertyIDEnum.SystemCompanies_MaxMaintenance

    SystemCompanies_MinMaintenance = plx_enums.PropertyIDEnum.SystemCompanies_MinMaintenance

    SystemCompanies_MaxMaintenanceFactor = plx_enums.PropertyIDEnum.SystemCompanies_MaxMaintenanceFactor

    SystemCompanies_MinMaintenanceFactor = plx_enums.PropertyIDEnum.SystemCompanies_MinMaintenanceFactor

    SystemCompanies_x = plx_enums.PropertyIDEnum.SystemCompanies_x

    SystemCompanies_y = plx_enums.PropertyIDEnum.SystemCompanies_y

    SystemCompanies_z = plx_enums.PropertyIDEnum.SystemCompanies_z

    SystemFinancialContracts_IsPhysical = plx_enums.PropertyIDEnum.SystemFinancialContracts_IsPhysical

    SystemFinancialContracts_Quantity = plx_enums.PropertyIDEnum.SystemFinancialContracts_Quantity

    SystemFinancialContracts_FloorPrice = plx_enums.PropertyIDEnum.SystemFinancialContracts_FloorPrice

    SystemFinancialContracts_CapPrice = plx_enums.PropertyIDEnum.SystemFinancialContracts_CapPrice

    SystemHubs_PricingMethod = plx_enums.PropertyIDEnum.SystemHubs_PricingMethod

    SystemHubs_Units = plx_enums.PropertyIDEnum.SystemHubs_Units

    SystemHubs_x = plx_enums.PropertyIDEnum.SystemHubs_x

    SystemHubs_y = plx_enums.PropertyIDEnum.SystemHubs_y

    SystemHubs_z = plx_enums.PropertyIDEnum.SystemHubs_z

    SystemTransmissionRights_Type = plx_enums.PropertyIDEnum.SystemTransmissionRights_Type

    SystemTransmissionRights_SettlementModel = plx_enums.PropertyIDEnum.SystemTransmissionRights_SettlementModel

    SystemTransmissionRights_PricingMethod = plx_enums.PropertyIDEnum.SystemTransmissionRights_PricingMethod

    SystemTransmissionRights_Units = plx_enums.PropertyIDEnum.SystemTransmissionRights_Units

    SystemTransmissionRights_Quantity = plx_enums.PropertyIDEnum.SystemTransmissionRights_Quantity

    SystemTransmissionRights_RentalShare = plx_enums.PropertyIDEnum.SystemTransmissionRights_RentalShare

    SystemTransmissionRights_RentalBackShare = plx_enums.PropertyIDEnum.SystemTransmissionRights_RentalBackShare

    SystemTransmissionRights_Price = plx_enums.PropertyIDEnum.SystemTransmissionRights_Price

    SystemCournots_DemandIntercept = plx_enums.PropertyIDEnum.SystemCournots_DemandIntercept

    SystemCournots_DemandSlope = plx_enums.PropertyIDEnum.SystemCournots_DemandSlope

    SystemRSIs_AllowNegativeMarkups = plx_enums.PropertyIDEnum.SystemRSIs_AllowNegativeMarkups

    SystemRSIs_RSI = plx_enums.PropertyIDEnum.SystemRSIs_RSI

    SystemRSIs_LernerIndex = plx_enums.PropertyIDEnum.SystemRSIs_LernerIndex

    SystemRSIs_BoundedLernerIndex = plx_enums.PropertyIDEnum.SystemRSIs_BoundedLernerIndex

    SystemRSIs_Intercept = plx_enums.PropertyIDEnum.SystemRSIs_Intercept

    SystemRSIs_RSICoefficient = plx_enums.PropertyIDEnum.SystemRSIs_RSICoefficient

    SystemRSIs_RSIsquaredCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_RSIsquaredCoefficient

    SystemRSIs_LoadUnhedgedCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_LoadUnhedgedCoefficient

    SystemRSIs_RSIInverseCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_RSIInverseCoefficient

    SystemRSIs_LoadCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_LoadCoefficient

    SystemRSIs_LoadCapacityRatioCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_LoadCapacityRatioCoefficient

    SystemRSIs_CapacityFactorCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_CapacityFactorCoefficient

    SystemRSIs_LoadVariationCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_LoadVariationCoefficient

    SystemRSIs_SummerPeriodCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_SummerPeriodCoefficient

    SystemRSIs_PeakPeriodCoefficient = plx_enums.PropertyIDEnum.SystemRSIs_PeakPeriodCoefficient

    SystemRSIs_AverageLoad = plx_enums.PropertyIDEnum.SystemRSIs_AverageLoad

    SystemRSIs_LernerIndextstatistic = plx_enums.PropertyIDEnum.SystemRSIs_LernerIndextstatistic

    SystemRSIs_LernerIndexStdDev = plx_enums.PropertyIDEnum.SystemRSIs_LernerIndexStdDev

    SystemRSIs_LernerIndexCalibrationFactor = plx_enums.PropertyIDEnum.SystemRSIs_LernerIndexCalibrationFactor

    SystemRSIs_MinLernerIndex = plx_enums.PropertyIDEnum.SystemRSIs_MinLernerIndex

    SystemRSIs_MaxLernerIndex = plx_enums.PropertyIDEnum.SystemRSIs_MaxLernerIndex

    SystemMarkets_IsForward = plx_enums.PropertyIDEnum.SystemMarkets_IsForward

    SystemMarkets_IsMarginal = plx_enums.PropertyIDEnum.SystemMarkets_IsMarginal

    SystemMarkets_DemandCurve = plx_enums.PropertyIDEnum.SystemMarkets_DemandCurve

    SystemMarkets_PriceSetting = plx_enums.PropertyIDEnum.SystemMarkets_PriceSetting

    SystemMarkets_SupplySettlementModel = plx_enums.PropertyIDEnum.SystemMarkets_SupplySettlementModel

    SystemMarkets_DemandSettlementModel = plx_enums.PropertyIDEnum.SystemMarkets_DemandSettlementModel

    SystemMarkets_Units = plx_enums.PropertyIDEnum.SystemMarkets_Units

    SystemMarkets_Price = plx_enums.PropertyIDEnum.SystemMarkets_Price

    SystemMarkets_PriceScalar = plx_enums.PropertyIDEnum.SystemMarkets_PriceScalar

    SystemMarkets_PriceIncr = plx_enums.PropertyIDEnum.SystemMarkets_PriceIncr

    SystemMarkets_Quantity = plx_enums.PropertyIDEnum.SystemMarkets_Quantity

    SystemMarkets_BaseQuantity = plx_enums.PropertyIDEnum.SystemMarkets_BaseQuantity

    SystemMarkets_SellUnit = plx_enums.PropertyIDEnum.SystemMarkets_SellUnit

    SystemMarkets_SellBlock = plx_enums.PropertyIDEnum.SystemMarkets_SellBlock

    SystemMarkets_SellBlockHour = plx_enums.PropertyIDEnum.SystemMarkets_SellBlockHour

    SystemMarkets_SellBlockDay = plx_enums.PropertyIDEnum.SystemMarkets_SellBlockDay

    SystemMarkets_SellBlockWeek = plx_enums.PropertyIDEnum.SystemMarkets_SellBlockWeek

    SystemMarkets_SellBlockMonth = plx_enums.PropertyIDEnum.SystemMarkets_SellBlockMonth

    SystemMarkets_SellBlockYear = plx_enums.PropertyIDEnum.SystemMarkets_SellBlockYear

    SystemMarkets_SellBlockFixedCharge = plx_enums.PropertyIDEnum.SystemMarkets_SellBlockFixedCharge

    SystemMarkets_BuyUnit = plx_enums.PropertyIDEnum.SystemMarkets_BuyUnit

    SystemMarkets_BuyBlock = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlock

    SystemMarkets_BuyBlockHour = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlockHour

    SystemMarkets_BuyBlockDay = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlockDay

    SystemMarkets_BuyBlockWeek = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlockWeek

    SystemMarkets_BuyBlockMonth = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlockMonth

    SystemMarkets_BuyBlockYear = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlockYear

    SystemMarkets_BuyBlockFixedCharge = plx_enums.PropertyIDEnum.SystemMarkets_BuyBlockFixedCharge

    SystemMarkets_MinSales = plx_enums.PropertyIDEnum.SystemMarkets_MinSales

    SystemMarkets_MaxSales = plx_enums.PropertyIDEnum.SystemMarkets_MaxSales

    SystemMarkets_MinPurchases = plx_enums.PropertyIDEnum.SystemMarkets_MinPurchases

    SystemMarkets_MaxPurchases = plx_enums.PropertyIDEnum.SystemMarkets_MaxPurchases

    SystemMarkets_BidAskSpread = plx_enums.PropertyIDEnum.SystemMarkets_BidAskSpread

    SystemMarkets_BidSpread = plx_enums.PropertyIDEnum.SystemMarkets_BidSpread

    SystemMarkets_AskSpread = plx_enums.PropertyIDEnum.SystemMarkets_AskSpread

    SystemMarkets_FirmCapacity = plx_enums.PropertyIDEnum.SystemMarkets_FirmCapacity

    SystemMarkets_LoadObligation = plx_enums.PropertyIDEnum.SystemMarkets_LoadObligation

    SystemMarkets_x = plx_enums.PropertyIDEnum.SystemMarkets_x

    SystemMarkets_y = plx_enums.PropertyIDEnum.SystemMarkets_y

    SystemMarkets_z = plx_enums.PropertyIDEnum.SystemMarkets_z

    SystemConstraints_Sense = plx_enums.PropertyIDEnum.SystemConstraints_Sense

    SystemConstraints_LHSType = plx_enums.PropertyIDEnum.SystemConstraints_LHSType

    SystemConstraints_FormulateUpfront = plx_enums.PropertyIDEnum.SystemConstraints_FormulateUpfront

    SystemConstraints_ConditionLogic = plx_enums.PropertyIDEnum.SystemConstraints_ConditionLogic

    SystemConstraints_IncludeinLTPlan = plx_enums.PropertyIDEnum.SystemConstraints_IncludeinLTPlan

    SystemConstraints_IncludeinPASA = plx_enums.PropertyIDEnum.SystemConstraints_IncludeinPASA

    SystemConstraints_IncludeinMTSchedule = plx_enums.PropertyIDEnum.SystemConstraints_IncludeinMTSchedule

    SystemConstraints_IncludeinSTSchedule = plx_enums.PropertyIDEnum.SystemConstraints_IncludeinSTSchedule

    SystemConstraints_IncludeinUniformPricing = plx_enums.PropertyIDEnum.SystemConstraints_IncludeinUniformPricing

    SystemConstraints_DecompositionMethod = plx_enums.PropertyIDEnum.SystemConstraints_DecompositionMethod

    SystemConstraints_FeasibilityRepairWeight = plx_enums.PropertyIDEnum.SystemConstraints_FeasibilityRepairWeight

    SystemConstraints_WildcardMode = plx_enums.PropertyIDEnum.SystemConstraints_WildcardMode

    SystemConstraints_RHS = plx_enums.PropertyIDEnum.SystemConstraints_RHS

    SystemConstraints_RHSHour = plx_enums.PropertyIDEnum.SystemConstraints_RHSHour

    SystemConstraints_RHSDay = plx_enums.PropertyIDEnum.SystemConstraints_RHSDay

    SystemConstraints_RHSWeek = plx_enums.PropertyIDEnum.SystemConstraints_RHSWeek

    SystemConstraints_RHSMonth = plx_enums.PropertyIDEnum.SystemConstraints_RHSMonth

    SystemConstraints_RHSYear = plx_enums.PropertyIDEnum.SystemConstraints_RHSYear

    SystemConstraints_RHSCustom = plx_enums.PropertyIDEnum.SystemConstraints_RHSCustom

    SystemConstraints_PenaltyQuantity = plx_enums.PropertyIDEnum.SystemConstraints_PenaltyQuantity

    SystemConstraints_PenaltyPrice = plx_enums.PropertyIDEnum.SystemConstraints_PenaltyPrice

    SystemConstraints_MinRHS = plx_enums.PropertyIDEnum.SystemConstraints_MinRHS

    SystemConstraints_MaxRHS = plx_enums.PropertyIDEnum.SystemConstraints_MaxRHS

    SystemConstraints_x = plx_enums.PropertyIDEnum.SystemConstraints_x

    SystemConstraints_y = plx_enums.PropertyIDEnum.SystemConstraints_y

    SystemConstraints_z = plx_enums.PropertyIDEnum.SystemConstraints_z

    SystemDecisionVariables_IncludeinLTPlan = plx_enums.PropertyIDEnum.SystemDecisionVariables_IncludeinLTPlan

    SystemDecisionVariables_IncludeinPASA = plx_enums.PropertyIDEnum.SystemDecisionVariables_IncludeinPASA

    SystemDecisionVariables_IncludeinMTSchedule = plx_enums.PropertyIDEnum.SystemDecisionVariables_IncludeinMTSchedule

    SystemDecisionVariables_IncludeinSTSchedule = plx_enums.PropertyIDEnum.SystemDecisionVariables_IncludeinSTSchedule

    SystemDecisionVariables_ObjectiveFunctionCoefficient = plx_enums.PropertyIDEnum.SystemDecisionVariables_ObjectiveFunctionCoefficient

    SystemDecisionVariables_ObjectiveFunctionCoefficientHour = plx_enums.PropertyIDEnum.SystemDecisionVariables_ObjectiveFunctionCoefficientHour

    SystemDecisionVariables_ObjectiveFunctionCoefficientDay = plx_enums.PropertyIDEnum.SystemDecisionVariables_ObjectiveFunctionCoefficientDay

    SystemDecisionVariables_ObjectiveFunctionCoefficientWeek = plx_enums.PropertyIDEnum.SystemDecisionVariables_ObjectiveFunctionCoefficientWeek

    SystemDecisionVariables_ObjectiveFunctionCoefficientMonth = plx_enums.PropertyIDEnum.SystemDecisionVariables_ObjectiveFunctionCoefficientMonth

    SystemDecisionVariables_ObjectiveFunctionCoefficientYear = plx_enums.PropertyIDEnum.SystemDecisionVariables_ObjectiveFunctionCoefficientYear

    SystemDecisionVariables_LowerBound = plx_enums.PropertyIDEnum.SystemDecisionVariables_LowerBound

    SystemDecisionVariables_UpperBound = plx_enums.PropertyIDEnum.SystemDecisionVariables_UpperBound

    SystemDecisionVariables_Nonanticipativity = plx_enums.PropertyIDEnum.SystemDecisionVariables_Nonanticipativity

    SystemDecisionVariables_NonanticipativityTime = plx_enums.PropertyIDEnum.SystemDecisionVariables_NonanticipativityTime

    SystemDecisionVariables_x = plx_enums.PropertyIDEnum.SystemDecisionVariables_x

    SystemDecisionVariables_y = plx_enums.PropertyIDEnum.SystemDecisionVariables_y

    SystemDecisionVariables_z = plx_enums.PropertyIDEnum.SystemDecisionVariables_z

    SystemDataFiles_Filename = plx_enums.PropertyIDEnum.SystemDataFiles_Filename

    SystemDataFiles_BaseProfile = plx_enums.PropertyIDEnum.SystemDataFiles_BaseProfile

    SystemDataFiles_Energy = plx_enums.PropertyIDEnum.SystemDataFiles_Energy

    SystemDataFiles_Maximum = plx_enums.PropertyIDEnum.SystemDataFiles_Maximum

    SystemDataFiles_Minimum = plx_enums.PropertyIDEnum.SystemDataFiles_Minimum

    SystemDataFiles_Holiday = plx_enums.PropertyIDEnum.SystemDataFiles_Holiday

    SystemDataFiles_MinValue = plx_enums.PropertyIDEnum.SystemDataFiles_MinValue

    SystemDataFiles_MaxValue = plx_enums.PropertyIDEnum.SystemDataFiles_MaxValue

    SystemVariables_RandomNumberSeed = plx_enums.PropertyIDEnum.SystemVariables_RandomNumberSeed

    SystemVariables_SamplingMethod = plx_enums.PropertyIDEnum.SystemVariables_SamplingMethod

    SystemVariables_SamplingFrequency = plx_enums.PropertyIDEnum.SystemVariables_SamplingFrequency

    SystemVariables_SamplingPeriodType = plx_enums.PropertyIDEnum.SystemVariables_SamplingPeriodType

    SystemVariables_DistributionType = plx_enums.PropertyIDEnum.SystemVariables_DistributionType

    SystemVariables_Condition = plx_enums.PropertyIDEnum.SystemVariables_Condition

    SystemVariables_ConditionLogic = plx_enums.PropertyIDEnum.SystemVariables_ConditionLogic

    SystemVariables_IncludeinLTPlan = plx_enums.PropertyIDEnum.SystemVariables_IncludeinLTPlan

    SystemVariables_IncludeinPASA = plx_enums.PropertyIDEnum.SystemVariables_IncludeinPASA

    SystemVariables_IncludeinMTSchedule = plx_enums.PropertyIDEnum.SystemVariables_IncludeinMTSchedule

    SystemVariables_IncludeinSTSchedule = plx_enums.PropertyIDEnum.SystemVariables_IncludeinSTSchedule

    SystemVariables_Profile = plx_enums.PropertyIDEnum.SystemVariables_Profile

    SystemVariables_ProfileHour = plx_enums.PropertyIDEnum.SystemVariables_ProfileHour

    SystemVariables_ProfileDay = plx_enums.PropertyIDEnum.SystemVariables_ProfileDay

    SystemVariables_ProfileWeek = plx_enums.PropertyIDEnum.SystemVariables_ProfileWeek

    SystemVariables_ProfileMonth = plx_enums.PropertyIDEnum.SystemVariables_ProfileMonth

    SystemVariables_ProfileYear = plx_enums.PropertyIDEnum.SystemVariables_ProfileYear

    SystemVariables_MinValue = plx_enums.PropertyIDEnum.SystemVariables_MinValue

    SystemVariables_MaxValue = plx_enums.PropertyIDEnum.SystemVariables_MaxValue

    SystemVariables_Probability = plx_enums.PropertyIDEnum.SystemVariables_Probability

    SystemVariables_ErrorStdDev = plx_enums.PropertyIDEnum.SystemVariables_ErrorStdDev

    SystemVariables_AbsErrorStdDev = plx_enums.PropertyIDEnum.SystemVariables_AbsErrorStdDev

    SystemVariables_MinValueStdDev = plx_enums.PropertyIDEnum.SystemVariables_MinValueStdDev

    SystemVariables_MaxValueStdDev = plx_enums.PropertyIDEnum.SystemVariables_MaxValueStdDev

    SystemVariables_AutoCorrelation = plx_enums.PropertyIDEnum.SystemVariables_AutoCorrelation

    SystemVariables_MeanReversion = plx_enums.PropertyIDEnum.SystemVariables_MeanReversion

    SystemVariables_ARIMAalpha = plx_enums.PropertyIDEnum.SystemVariables_ARIMAalpha

    SystemVariables_ARIMAbeta = plx_enums.PropertyIDEnum.SystemVariables_ARIMAbeta

    SystemVariables_ARIMAd = plx_enums.PropertyIDEnum.SystemVariables_ARIMAd

    SystemVariables_JumpFrequency = plx_enums.PropertyIDEnum.SystemVariables_JumpFrequency

    SystemVariables_JumpMagnitude = plx_enums.PropertyIDEnum.SystemVariables_JumpMagnitude

    SystemVariables_JumpErrorStdDev = plx_enums.PropertyIDEnum.SystemVariables_JumpErrorStdDev

    SystemVariables_GARCHalpha = plx_enums.PropertyIDEnum.SystemVariables_GARCHalpha

    SystemVariables_GARCHbeta = plx_enums.PropertyIDEnum.SystemVariables_GARCHbeta

    SystemVariables_GARCHomega = plx_enums.PropertyIDEnum.SystemVariables_GARCHomega

    SystemVariables_Lookupx = plx_enums.PropertyIDEnum.SystemVariables_Lookupx

    SystemVariables_Lookupy = plx_enums.PropertyIDEnum.SystemVariables_Lookupy

    SystemVariables_LookupUnit = plx_enums.PropertyIDEnum.SystemVariables_LookupUnit

    SystemVariables_Sampling = plx_enums.PropertyIDEnum.SystemVariables_Sampling

    SystemVariables_StepHourActiveFrom = plx_enums.PropertyIDEnum.SystemVariables_StepHourActiveFrom

    SystemVariables_StepHoursActive = plx_enums.PropertyIDEnum.SystemVariables_StepHoursActive

    SystemVariables_CompoundIndex = plx_enums.PropertyIDEnum.SystemVariables_CompoundIndex

    SystemVariables_CompoundIndexHour = plx_enums.PropertyIDEnum.SystemVariables_CompoundIndexHour

    SystemVariables_CompoundIndexDay = plx_enums.PropertyIDEnum.SystemVariables_CompoundIndexDay

    SystemVariables_CompoundIndexWeek = plx_enums.PropertyIDEnum.SystemVariables_CompoundIndexWeek

    SystemVariables_CompoundIndexMonth = plx_enums.PropertyIDEnum.SystemVariables_CompoundIndexMonth

    SystemVariables_CompoundIndexYear = plx_enums.PropertyIDEnum.SystemVariables_CompoundIndexYear

    SystemTimeslices_Include = plx_enums.PropertyIDEnum.SystemTimeslices_Include

    SystemGlobals_FCFConstant = plx_enums.PropertyIDEnum.SystemGlobals_FCFConstant

    SystemGlobals_SampleWeight = plx_enums.PropertyIDEnum.SystemGlobals_SampleWeight

    SystemGlobals_TreeStageCount = plx_enums.PropertyIDEnum.SystemGlobals_TreeStageCount

    SystemGlobals_TreePeriodType = plx_enums.PropertyIDEnum.SystemGlobals_TreePeriodType

    SystemGlobals_TreePositionExpFactor = plx_enums.PropertyIDEnum.SystemGlobals_TreePositionExpFactor

    SystemGlobals_TreeLeavesExpFactor = plx_enums.PropertyIDEnum.SystemGlobals_TreeLeavesExpFactor

    SystemGlobals_TreeStagesPosition = plx_enums.PropertyIDEnum.SystemGlobals_TreeStagesPosition

    SystemGlobals_TreeStagesLeaves = plx_enums.PropertyIDEnum.SystemGlobals_TreeStagesLeaves

    SystemGlobals_TreeStagesHangingBranches = plx_enums.PropertyIDEnum.SystemGlobals_TreeStagesHangingBranches

    SystemGlobals_DeterministicStages = plx_enums.PropertyIDEnum.SystemGlobals_DeterministicStages

    SystemGlobals_HangingBranchesHistoricalYearStart = plx_enums.PropertyIDEnum.SystemGlobals_HangingBranchesHistoricalYearStart

    SystemGlobals_HangingBranchesWeight = plx_enums.PropertyIDEnum.SystemGlobals_HangingBranchesWeight

    SystemGlobals_HangingBranchesBlockCount = plx_enums.PropertyIDEnum.SystemGlobals_HangingBranchesBlockCount

    SystemGlobals_SlicingBlock = plx_enums.PropertyIDEnum.SystemGlobals_SlicingBlock

    GeneratorCompanies_Share = plx_enums.PropertyIDEnum.GeneratorCompanies_Share

    GeneratorNodes_GenerationParticipationFactor = plx_enums.PropertyIDEnum.GeneratorNodes_GenerationParticipationFactor

    GeneratorNodes_LoadParticipationFactor = plx_enums.PropertyIDEnum.GeneratorNodes_LoadParticipationFactor

    GeneratorFuels_TransportCharge = plx_enums.PropertyIDEnum.GeneratorFuels_TransportCharge

    GeneratorFuels_MutuallyExclusive = plx_enums.PropertyIDEnum.GeneratorFuels_MutuallyExclusive

    GeneratorFuels_Ratio = plx_enums.PropertyIDEnum.GeneratorFuels_Ratio

    GeneratorFuels_MinRatio = plx_enums.PropertyIDEnum.GeneratorFuels_MinRatio

    GeneratorFuels_MaxRatio = plx_enums.PropertyIDEnum.GeneratorFuels_MaxRatio

    GeneratorFuels_MaxInput = plx_enums.PropertyIDEnum.GeneratorFuels_MaxInput

    GeneratorFuels_Rating = plx_enums.PropertyIDEnum.GeneratorFuels_Rating

    GeneratorFuels_IsAvailable = plx_enums.PropertyIDEnum.GeneratorFuels_IsAvailable

    GeneratorFuels_HeatRateScalar = plx_enums.PropertyIDEnum.GeneratorFuels_HeatRateScalar

    GeneratorFuels_HeatRateBase = plx_enums.PropertyIDEnum.GeneratorFuels_HeatRateBase

    GeneratorFuels_HeatRate = plx_enums.PropertyIDEnum.GeneratorFuels_HeatRate

    GeneratorFuels_HeatRateIncr = plx_enums.PropertyIDEnum.GeneratorFuels_HeatRateIncr

    GeneratorFuels_HeatRateIncr2 = plx_enums.PropertyIDEnum.GeneratorFuels_HeatRateIncr2

    GeneratorFuels_HeatRateIncr3 = plx_enums.PropertyIDEnum.GeneratorFuels_HeatRateIncr3

    GeneratorFuels_TransitionCostDown = plx_enums.PropertyIDEnum.GeneratorFuels_TransitionCostDown

    GeneratorFuels_TransitionCostUp = plx_enums.PropertyIDEnum.GeneratorFuels_TransitionCostUp

    GeneratorFuels_DecouplingTime = plx_enums.PropertyIDEnum.GeneratorFuels_DecouplingTime

    GeneratorFuels_CouplingTime = plx_enums.PropertyIDEnum.GeneratorFuels_CouplingTime

    GeneratorFuels_EmissionScalar = plx_enums.PropertyIDEnum.GeneratorFuels_EmissionScalar

    GeneratorFuels_OfferQuantity = plx_enums.PropertyIDEnum.GeneratorFuels_OfferQuantity

    GeneratorFuels_OfferPrice = plx_enums.PropertyIDEnum.GeneratorFuels_OfferPrice

    GeneratorStartFuels_OfftakeatStart = plx_enums.PropertyIDEnum.GeneratorStartFuels_OfftakeatStart

    GeneratorStartFuels_TransportCharge = plx_enums.PropertyIDEnum.GeneratorStartFuels_TransportCharge

    GeneratorStartFuels_EmissionScalar = plx_enums.PropertyIDEnum.GeneratorStartFuels_EmissionScalar

    GeneratorHeadStorage_FlowFactor = plx_enums.PropertyIDEnum.GeneratorHeadStorage_FlowFactor

    GeneratorHeadStorage_FlowatStart = plx_enums.PropertyIDEnum.GeneratorHeadStorage_FlowatStart

    GeneratorHeadStorage_EfficiencyPoint = plx_enums.PropertyIDEnum.GeneratorHeadStorage_EfficiencyPoint

    GeneratorHeadStorage_EfficiencyScalar = plx_enums.PropertyIDEnum.GeneratorHeadStorage_EfficiencyScalar

    GeneratorTailStorage_FlowFactor = plx_enums.PropertyIDEnum.GeneratorTailStorage_FlowFactor

    GeneratorTransition_TransitionCost = plx_enums.PropertyIDEnum.GeneratorTransition_TransitionCost

    FuelCompanies_Share = plx_enums.PropertyIDEnum.FuelCompanies_Share

    EmissionFuels_ProductionRate = plx_enums.PropertyIDEnum.EmissionFuels_ProductionRate

    EmissionGenerators_ProductionRate = plx_enums.PropertyIDEnum.EmissionGenerators_ProductionRate

    EmissionGenerators_RemovalRate = plx_enums.PropertyIDEnum.EmissionGenerators_RemovalRate

    EmissionGenerators_RemovalCost = plx_enums.PropertyIDEnum.EmissionGenerators_RemovalCost

    EmissionGenerators_ProductionatStart = plx_enums.PropertyIDEnum.EmissionGenerators_ProductionatStart

    EmissionGenerators_ShadowPriceScalar = plx_enums.PropertyIDEnum.EmissionGenerators_ShadowPriceScalar

    EmissionGenerators_PriceScalar = plx_enums.PropertyIDEnum.EmissionGenerators_PriceScalar

    EmissionGenerators_Allocation = plx_enums.PropertyIDEnum.EmissionGenerators_Allocation

    EmissionGenerators_AllocationHour = plx_enums.PropertyIDEnum.EmissionGenerators_AllocationHour

    EmissionGenerators_AllocationDay = plx_enums.PropertyIDEnum.EmissionGenerators_AllocationDay

    EmissionGenerators_AllocationWeek = plx_enums.PropertyIDEnum.EmissionGenerators_AllocationWeek

    EmissionGenerators_AllocationMonth = plx_enums.PropertyIDEnum.EmissionGenerators_AllocationMonth

    EmissionGenerators_AllocationYear = plx_enums.PropertyIDEnum.EmissionGenerators_AllocationYear

    EmissionGasNodes_ProductionRate = plx_enums.PropertyIDEnum.EmissionGasNodes_ProductionRate

    EmissionGasPlants_ProductionRate = plx_enums.PropertyIDEnum.EmissionGasPlants_ProductionRate

    EmissionWaterPlants_ProductionRate = plx_enums.PropertyIDEnum.EmissionWaterPlants_ProductionRate

    AbatementGenerators_GenerationParticipationFactor = plx_enums.PropertyIDEnum.AbatementGenerators_GenerationParticipationFactor

    AbatementEmissions_AbatementCost = plx_enums.PropertyIDEnum.AbatementEmissions_AbatementCost

    AbatementEmissions_Efficiency = plx_enums.PropertyIDEnum.AbatementEmissions_Efficiency

    AbatementEmissions_MaxAbatement = plx_enums.PropertyIDEnum.AbatementEmissions_MaxAbatement

    AbatementConsumables_ConsumptionBase = plx_enums.PropertyIDEnum.AbatementConsumables_ConsumptionBase

    AbatementConsumables_ConsumptionIncr = plx_enums.PropertyIDEnum.AbatementConsumables_ConsumptionIncr

    PowerStationNodes_GenerationParticipationFactor = plx_enums.PropertyIDEnum.PowerStationNodes_GenerationParticipationFactor

    FuelContractCompanies_Share = plx_enums.PropertyIDEnum.FuelContractCompanies_Share

    PhysicalContractCompanies_Share = plx_enums.PropertyIDEnum.PhysicalContractCompanies_Share

    PurchaserCompanies_Share = plx_enums.PropertyIDEnum.PurchaserCompanies_Share

    PurchaserNodes_LoadParticipationFactor = plx_enums.PropertyIDEnum.PurchaserNodes_LoadParticipationFactor

    ReserveRegions_LoadRisk = plx_enums.PropertyIDEnum.ReserveRegions_LoadRisk

    ReserveRegions_LOLPTarget = plx_enums.PropertyIDEnum.ReserveRegions_LOLPTarget

    ReserveGenerators_InitialPumpLoadRaiseProvision = plx_enums.PropertyIDEnum.ReserveGenerators_InitialPumpLoadRaiseProvision

    ReserveGenerators_InitialRaiseProvision = plx_enums.PropertyIDEnum.ReserveGenerators_InitialRaiseProvision

    ReserveGenerators_MaxResponse = plx_enums.PropertyIDEnum.ReserveGenerators_MaxResponse

    ReserveGenerators_MaxSyncCondResponse = plx_enums.PropertyIDEnum.ReserveGenerators_MaxSyncCondResponse

    ReserveGenerators_MaxPumpResponse = plx_enums.PropertyIDEnum.ReserveGenerators_MaxPumpResponse

    ReserveGenerators_MaxReplacement = plx_enums.PropertyIDEnum.ReserveGenerators_MaxReplacement

    ReserveGenerators_MaxResponseFactor = plx_enums.PropertyIDEnum.ReserveGenerators_MaxResponseFactor

    ReserveGenerators_MaxSyncCondResponseFactor = plx_enums.PropertyIDEnum.ReserveGenerators_MaxSyncCondResponseFactor

    ReserveGenerators_MaxPumpResponseFactor = plx_enums.PropertyIDEnum.ReserveGenerators_MaxPumpResponseFactor

    ReserveGenerators_MaxReplacementFactor = plx_enums.PropertyIDEnum.ReserveGenerators_MaxReplacementFactor

    ReserveGenerators_MinProvision = plx_enums.PropertyIDEnum.ReserveGenerators_MinProvision

    ReserveGenerators_MinSpinningProvision = plx_enums.PropertyIDEnum.ReserveGenerators_MinSpinningProvision

    ReserveGenerators_MinRegulationProvision = plx_enums.PropertyIDEnum.ReserveGenerators_MinRegulationProvision

    ReserveGenerators_MinReplacementProvision = plx_enums.PropertyIDEnum.ReserveGenerators_MinReplacementProvision

    ReserveGenerators_Effectiveness = plx_enums.PropertyIDEnum.ReserveGenerators_Effectiveness

    ReserveGenerators_ResponseRatio = plx_enums.PropertyIDEnum.ReserveGenerators_ResponseRatio

    ReserveGenerators_OfferQuantity = plx_enums.PropertyIDEnum.ReserveGenerators_OfferQuantity

    ReserveGenerators_OfferPrice = plx_enums.PropertyIDEnum.ReserveGenerators_OfferPrice

    ReserveGenerators_SyncCondOfferPrice = plx_enums.PropertyIDEnum.ReserveGenerators_SyncCondOfferPrice

    ReserveGenerators_PumpOfferPrice = plx_enums.PropertyIDEnum.ReserveGenerators_PumpOfferPrice

    ReserveGenerators_ReplacementOfferQuantity = plx_enums.PropertyIDEnum.ReserveGenerators_ReplacementOfferQuantity

    ReserveGenerators_ReplacementOfferPrice = plx_enums.PropertyIDEnum.ReserveGenerators_ReplacementOfferPrice

    ReservePurchasers_OfferQuantity = plx_enums.PropertyIDEnum.ReservePurchasers_OfferQuantity

    ReservePurchasers_OfferPrice = plx_enums.PropertyIDEnum.ReservePurchasers_OfferPrice

    ReserveBatteries_OfferQuantity = plx_enums.PropertyIDEnum.ReserveBatteries_OfferQuantity

    ReserveBatteries_OfferPrice = plx_enums.PropertyIDEnum.ReserveBatteries_OfferPrice

    ReserveLineContingencies_FlowForwardCoefficient = plx_enums.PropertyIDEnum.ReserveLineContingencies_FlowForwardCoefficient

    ReserveLineContingencies_FlowBackCoefficient = plx_enums.PropertyIDEnum.ReserveLineContingencies_FlowBackCoefficient

    MaintenanceGenerators_OutageRating = plx_enums.PropertyIDEnum.MaintenanceGenerators_OutageRating

    MaintenanceGenerators_OutageRatingFactor = plx_enums.PropertyIDEnum.MaintenanceGenerators_OutageRatingFactor

    MaintenanceGenerators_OutageFirmCapacity = plx_enums.PropertyIDEnum.MaintenanceGenerators_OutageFirmCapacity

    MaintenanceGenerators_OutageFirmCapacityFactor = plx_enums.PropertyIDEnum.MaintenanceGenerators_OutageFirmCapacityFactor

    MaintenanceGasPipelines_OutageMaxFlow = plx_enums.PropertyIDEnum.MaintenanceGasPipelines_OutageMaxFlow

    MaintenanceGasPipelines_OutageMaxFlowBack = plx_enums.PropertyIDEnum.MaintenanceGasPipelines_OutageMaxFlowBack

    MaintenanceLines_OutageMaxRating = plx_enums.PropertyIDEnum.MaintenanceLines_OutageMaxRating

    MaintenanceLines_OutageMinRating = plx_enums.PropertyIDEnum.MaintenanceLines_OutageMinRating

    GeneratorHeatOutputNodes_ParticipationFactor = plx_enums.PropertyIDEnum.GeneratorHeatOutputNodes_ParticipationFactor

    HeatPlantFuels_MutuallyExclusive = plx_enums.PropertyIDEnum.HeatPlantFuels_MutuallyExclusive

    HeatPlantFuels_Ratio = plx_enums.PropertyIDEnum.HeatPlantFuels_Ratio

    HeatPlantFuels_MinRatio = plx_enums.PropertyIDEnum.HeatPlantFuels_MinRatio

    HeatPlantFuels_MaxRatio = plx_enums.PropertyIDEnum.HeatPlantFuels_MaxRatio

    HeatPlantFuels_MaxInput = plx_enums.PropertyIDEnum.HeatPlantFuels_MaxInput

    HeatPlantFuels_IsAvailable = plx_enums.PropertyIDEnum.HeatPlantFuels_IsAvailable

    HeatPlantFuels_HeatRateScalar = plx_enums.PropertyIDEnum.HeatPlantFuels_HeatRateScalar

    HeatPlantFuels_HeatRateBase = plx_enums.PropertyIDEnum.HeatPlantFuels_HeatRateBase

    HeatPlantFuels_HeatRate = plx_enums.PropertyIDEnum.HeatPlantFuels_HeatRate

    HeatPlantFuels_HeatRateIncr = plx_enums.PropertyIDEnum.HeatPlantFuels_HeatRateIncr

    HeatPlantHeatOutputNodes_ParticipationFactor = plx_enums.PropertyIDEnum.HeatPlantHeatOutputNodes_ParticipationFactor

    HeatPlantStartFuels_OfftakeatStart = plx_enums.PropertyIDEnum.HeatPlantStartFuels_OfftakeatStart

    HeatNodeHeatExportNodes_ParticipationFactor = plx_enums.PropertyIDEnum.HeatNodeHeatExportNodes_ParticipationFactor

    HeatNodeWaterPlants_ParticipationFactor = plx_enums.PropertyIDEnum.HeatNodeWaterPlants_ParticipationFactor

    MarketCompanies_Share = plx_enums.PropertyIDEnum.MarketCompanies_Share

    MarketHeatGenerators_ConversionRate = plx_enums.PropertyIDEnum.MarketHeatGenerators_ConversionRate

    MarketCapacityGenerators_OfferQuantity = plx_enums.PropertyIDEnum.MarketCapacityGenerators_OfferQuantity

    MarketCapacityGenerators_OfferPrice = plx_enums.PropertyIDEnum.MarketCapacityGenerators_OfferPrice

    GasFieldCompanies_Share = plx_enums.PropertyIDEnum.GasFieldCompanies_Share

    GasDemandGasNodes_DemandParticipationFactor = plx_enums.PropertyIDEnum.GasDemandGasNodes_DemandParticipationFactor

    RegionRegions_WheelingCharge = plx_enums.PropertyIDEnum.RegionRegions_WheelingCharge

    RegionRegions_MaxFlow = plx_enums.PropertyIDEnum.RegionRegions_MaxFlow

    ZoneZones_WheelingCharge = plx_enums.PropertyIDEnum.ZoneZones_WheelingCharge

    ZoneZones_MaxFlow = plx_enums.PropertyIDEnum.ZoneZones_MaxFlow

    NodeHubs_PricingWeight = plx_enums.PropertyIDEnum.NodeHubs_PricingWeight

    LineCompanies_Share = plx_enums.PropertyIDEnum.LineCompanies_Share

    MLFRegions_LoadCoefficient = plx_enums.PropertyIDEnum.MLFRegions_LoadCoefficient

    InterfaceLines_FlowCoefficient = plx_enums.PropertyIDEnum.InterfaceLines_FlowCoefficient

    InterfaceLines_FlowForwardCoefficient = plx_enums.PropertyIDEnum.InterfaceLines_FlowForwardCoefficient

    InterfaceLines_FlowBackCoefficient = plx_enums.PropertyIDEnum.InterfaceLines_FlowBackCoefficient

    InterfaceTransformers_FlowCoefficient = plx_enums.PropertyIDEnum.InterfaceTransformers_FlowCoefficient

    CompanyRegions_LoadParticipationFactor = plx_enums.PropertyIDEnum.CompanyRegions_LoadParticipationFactor

    CompanyEmissions_Allocation = plx_enums.PropertyIDEnum.CompanyEmissions_Allocation

    CompanyEmissions_AllocationHour = plx_enums.PropertyIDEnum.CompanyEmissions_AllocationHour

    CompanyEmissions_AllocationDay = plx_enums.PropertyIDEnum.CompanyEmissions_AllocationDay

    CompanyEmissions_AllocationWeek = plx_enums.PropertyIDEnum.CompanyEmissions_AllocationWeek

    CompanyEmissions_AllocationMonth = plx_enums.PropertyIDEnum.CompanyEmissions_AllocationMonth

    CompanyEmissions_AllocationYear = plx_enums.PropertyIDEnum.CompanyEmissions_AllocationYear

    FinancialContractGeneratingCompanies_Share = plx_enums.PropertyIDEnum.FinancialContractGeneratingCompanies_Share

    FinancialContractPurchasingCompanies_Share = plx_enums.PropertyIDEnum.FinancialContractPurchasingCompanies_Share

    FinancialContractRegion_LoadParticipationFactor = plx_enums.PropertyIDEnum.FinancialContractRegion_LoadParticipationFactor

    FinancialContractGenerators_GenerationParticipationFactor = plx_enums.PropertyIDEnum.FinancialContractGenerators_GenerationParticipationFactor

    TransmissionRightCompanies_Share = plx_enums.PropertyIDEnum.TransmissionRightCompanies_Share

    GasDemandCompanies_Share = plx_enums.PropertyIDEnum.GasDemandCompanies_Share

    ConstraintGenerators_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_GenerationCoefficient

    ConstraintGenerators_GenerationSquaredCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_GenerationSquaredCoefficient

    ConstraintGenerators_GenerationSUMSquaredCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_GenerationSUMSquaredCoefficient

    ConstraintGenerators_GenerationSentOutCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_GenerationSentOutCoefficient

    ConstraintGenerators_CapacityFactorCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_CapacityFactorCoefficient

    ConstraintGenerators_OperatingHoursCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_OperatingHoursCoefficient

    ConstraintGenerators_UnitsGeneratingCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsGeneratingCoefficient

    ConstraintGenerators_UnitsStartedCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsStartedCoefficient

    ConstraintGenerators_UnitsShutdownCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsShutdownCoefficient

    ConstraintGenerators_HoursDownCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_HoursDownCoefficient

    ConstraintGenerators_AvailableCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_AvailableCapacityCoefficient

    ConstraintGenerators_CommittedCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_CommittedCapacityCoefficient

    ConstraintGenerators_FuelOfftakeCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_FuelOfftakeCoefficient

    ConstraintGenerators_WasteHeatCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_WasteHeatCoefficient

    ConstraintGenerators_EmissionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_EmissionCoefficient

    ConstraintGenerators_HeatProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_HeatProductionCoefficient

    ConstraintGenerators_PumpLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_PumpLoadCoefficient

    ConstraintGenerators_PumpOperatingHoursCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_PumpOperatingHoursCoefficient

    ConstraintGenerators_UnitsPumpingCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsPumpingCoefficient

    ConstraintGenerators_PumpUnitsStartedCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_PumpUnitsStartedCoefficient

    ConstraintGenerators_SyncCondLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_SyncCondLoadCoefficient

    ConstraintGenerators_UnitsSyncCondCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsSyncCondCoefficient

    ConstraintGenerators_SyncCondOperatingHoursCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_SyncCondOperatingHoursCoefficient

    ConstraintGenerators_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampCoefficient

    ConstraintGenerators_RampUpCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampUpCoefficient

    ConstraintGenerators_RampDownCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampDownCoefficient

    ConstraintGenerators_RampUpViolationCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampUpViolationCoefficient

    ConstraintGenerators_RampDownViolationCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampDownViolationCoefficient

    ConstraintGenerators_ReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_ReserveProvisionCoefficient

    ConstraintGenerators_SpinningReserveCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_SpinningReserveCoefficient

    ConstraintGenerators_SyncCondReserveCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_SyncCondReserveCoefficient

    ConstraintGenerators_PumpDispatchableLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_PumpDispatchableLoadCoefficient

    ConstraintGenerators_RaiseReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RaiseReserveProvisionCoefficient

    ConstraintGenerators_LowerReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_LowerReserveProvisionCoefficient

    ConstraintGenerators_RegulationRaiseReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RegulationRaiseReserveProvisionCoefficient

    ConstraintGenerators_RegulationLowerReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RegulationLowerReserveProvisionCoefficient

    ConstraintGenerators_ReplacementReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_ReplacementReserveProvisionCoefficient

    ConstraintGenerators_ReserveUnitsCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_ReserveUnitsCoefficient

    ConstraintGenerators_OperatingReserveUnitsCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_OperatingReserveUnitsCoefficient

    ConstraintGenerators_FlexibilityUpCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_FlexibilityUpCoefficient

    ConstraintGenerators_FlexibilityDownCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_FlexibilityDownCoefficient

    ConstraintGenerators_RampFlexibilityUpCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampFlexibilityUpCoefficient

    ConstraintGenerators_RampFlexibilityDownCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RampFlexibilityDownCoefficient

    ConstraintGenerators_WithdrawalCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_WithdrawalCoefficient

    ConstraintGenerators_InjectionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_InjectionCoefficient

    ConstraintGenerators_WaterOfftakeCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_WaterOfftakeCoefficient

    ConstraintGenerators_WaterConsumptionCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_WaterConsumptionCoefficient

    ConstraintGenerators_NetProfitCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_NetProfitCoefficient

    ConstraintGenerators_PoolRevenueCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_PoolRevenueCoefficient

    ConstraintGenerators_NetRevenueCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_NetRevenueCoefficient

    ConstraintGenerators_StartShutdownCostCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_StartShutdownCostCoefficient

    ConstraintGenerators_FixedCostsCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_FixedCostsCoefficient

    ConstraintGenerators_InstalledCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_InstalledCapacityCoefficient

    ConstraintGenerators_RatedCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_RatedCapacityCoefficient

    ConstraintGenerators_UnitsOutCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsOutCoefficient

    ConstraintGenerators_MaintenanceCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_MaintenanceCoefficient

    ConstraintGenerators_FirmCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_FirmCapacityCoefficient

    ConstraintGenerators_AgeCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_AgeCoefficient

    ConstraintGenerators_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsBuiltCoefficient

    ConstraintGenerators_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsRetiredCoefficient

    ConstraintGenerators_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsBuiltinYearCoefficient

    ConstraintGenerators_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_UnitsRetiredinYearCoefficient

    ConstraintGenerators_CapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_CapacityBuiltCoefficient

    ConstraintGenerators_CapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_CapacityRetiredCoefficient

    ConstraintGenerators_CapacityReservesCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_CapacityReservesCoefficient

    ConstraintGenerators_BuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_BuildCostCoefficient

    ConstraintGenerators_BuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_BuiltCoefficient

    ConstraintGenerators_BuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGenerators_BuiltinYearCoefficient

    ConstraintFuels_OfftakeCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_OfftakeCoefficient

    ConstraintFuels_EmissionCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_EmissionCoefficient

    ConstraintFuels_InUseCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_InUseCoefficient

    ConstraintFuels_ClosingInventoryCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_ClosingInventoryCoefficient

    ConstraintFuels_InventoryChangeCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_InventoryChangeCoefficient

    ConstraintFuels_DeliveryCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_DeliveryCoefficient

    ConstraintFuels_WithdrawalCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_WithdrawalCoefficient

    ConstraintFuels_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintFuels_GenerationCoefficient

    ConstraintFuelContracts_OfftakeCoefficient = plx_enums.PropertyIDEnum.ConstraintFuelContracts_OfftakeCoefficient

    ConstraintEmissions_ProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintEmissions_ProductionCoefficient

    ConstraintEmissions_AbatementCoefficient = plx_enums.PropertyIDEnum.ConstraintEmissions_AbatementCoefficient

    ConstraintAbatements_AbatementCoefficient = plx_enums.PropertyIDEnum.ConstraintAbatements_AbatementCoefficient

    ConstraintAbatements_OperatingHoursCoefficient = plx_enums.PropertyIDEnum.ConstraintAbatements_OperatingHoursCoefficient

    ConstraintStorages_EndVolumeCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_EndVolumeCoefficient

    ConstraintStorages_EndLevelCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_EndLevelCoefficient

    ConstraintStorages_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_RampCoefficient

    ConstraintStorages_NaturalInflowCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_NaturalInflowCoefficient

    ConstraintStorages_InflowCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_InflowCoefficient

    ConstraintStorages_ReleaseCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_ReleaseCoefficient

    ConstraintStorages_GeneratorReleaseCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_GeneratorReleaseCoefficient

    ConstraintStorages_SpillCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_SpillCoefficient

    ConstraintStorages_HoursFullCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_HoursFullCoefficient

    ConstraintStorages_LossCoefficient = plx_enums.PropertyIDEnum.ConstraintStorages_LossCoefficient

    ConstraintWaterways_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterways_FlowCoefficient

    ConstraintWaterways_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterways_RampCoefficient

    ConstraintWaterways_HoursFlowingCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterways_HoursFlowingCoefficient

    ConstraintPhysicalContracts_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_LoadCoefficient

    ConstraintPhysicalContracts_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_GenerationCoefficient

    ConstraintPhysicalContracts_UnitsGeneratingCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_UnitsGeneratingCoefficient

    ConstraintPhysicalContracts_UnitsLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_UnitsLoadCoefficient

    ConstraintPhysicalContracts_GenerationCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_GenerationCapacityCoefficient

    ConstraintPhysicalContracts_LoadObligationCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_LoadObligationCoefficient

    ConstraintPhysicalContracts_BuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintPhysicalContracts_BuildCostCoefficient

    ConstraintPurchasers_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintPurchasers_LoadCoefficient

    ConstraintPurchasers_LoadObligationCoefficient = plx_enums.PropertyIDEnum.ConstraintPurchasers_LoadObligationCoefficient

    ConstraintPurchasers_ReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintPurchasers_ReserveProvisionCoefficient

    ConstraintReserves_ProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintReserves_ProvisionCoefficient

    ConstraintReserves_RiskCoefficient = plx_enums.PropertyIDEnum.ConstraintReserves_RiskCoefficient

    ConstraintReserves_ShortageCoefficient = plx_enums.PropertyIDEnum.ConstraintReserves_ShortageCoefficient

    ConstraintMarkets_SalesCoefficient = plx_enums.PropertyIDEnum.ConstraintMarkets_SalesCoefficient

    ConstraintMarkets_PurchasesCoefficient = plx_enums.PropertyIDEnum.ConstraintMarkets_PurchasesCoefficient

    ConstraintMarkets_RevenueCoefficient = plx_enums.PropertyIDEnum.ConstraintMarkets_RevenueCoefficient

    ConstraintMarkets_CostCoefficient = plx_enums.PropertyIDEnum.ConstraintMarkets_CostCoefficient

    ConstraintBatteries_EnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_EnergyCoefficient

    ConstraintBatteries_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_GenerationCoefficient

    ConstraintBatteries_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_LoadCoefficient

    ConstraintBatteries_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RampCoefficient

    ConstraintBatteries_RampUpCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RampUpCoefficient

    ConstraintBatteries_RampDownCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RampDownCoefficient

    ConstraintBatteries_RampUpViolationCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RampUpViolationCoefficient

    ConstraintBatteries_RampDownViolationCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RampDownViolationCoefficient

    ConstraintBatteries_ReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_ReserveProvisionCoefficient

    ConstraintBatteries_SpinningReserveCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_SpinningReserveCoefficient

    ConstraintBatteries_PumpDispatchableLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_PumpDispatchableLoadCoefficient

    ConstraintBatteries_RaiseReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RaiseReserveProvisionCoefficient

    ConstraintBatteries_LowerReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_LowerReserveProvisionCoefficient

    ConstraintBatteries_RegulationRaiseReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RegulationRaiseReserveProvisionCoefficient

    ConstraintBatteries_RegulationLowerReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_RegulationLowerReserveProvisionCoefficient

    ConstraintBatteries_ReplacementReserveProvisionCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_ReplacementReserveProvisionCoefficient

    ConstraintBatteries_ReserveUnitsCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_ReserveUnitsCoefficient

    ConstraintBatteries_OperatingReserveUnitsCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_OperatingReserveUnitsCoefficient

    ConstraintBatteries_CyclesCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_CyclesCoefficient

    ConstraintBatteries_AgeCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_AgeCoefficient

    ConstraintBatteries_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_UnitsBuiltCoefficient

    ConstraintBatteries_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_UnitsRetiredCoefficient

    ConstraintBatteries_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_UnitsBuiltinYearCoefficient

    ConstraintBatteries_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_UnitsRetiredinYearCoefficient

    ConstraintBatteries_CapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_CapacityBuiltCoefficient

    ConstraintBatteries_CapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_CapacityRetiredCoefficient

    ConstraintBatteries_CapacityReservesCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_CapacityReservesCoefficient

    ConstraintBatteries_BuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_BuildCostCoefficient

    ConstraintBatteries_BuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_BuiltCoefficient

    ConstraintBatteries_BuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintBatteries_BuiltinYearCoefficient

    ConstraintMaintenances_HoursActiveCoefficient = plx_enums.PropertyIDEnum.ConstraintMaintenances_HoursActiveCoefficient

    ConstraintMaintenances_CostCoefficient = plx_enums.PropertyIDEnum.ConstraintMaintenances_CostCoefficient

    ConstraintMaintenances_CrewCoefficient = plx_enums.PropertyIDEnum.ConstraintMaintenances_CrewCoefficient

    ConstraintMaintenances_EquipmentCoefficient = plx_enums.PropertyIDEnum.ConstraintMaintenances_EquipmentCoefficient

    ConstraintMaintenances_StartHourCoefficient = plx_enums.PropertyIDEnum.ConstraintMaintenances_StartHourCoefficient

    ConstraintMaintenances_StartCoefficient = plx_enums.PropertyIDEnum.ConstraintMaintenances_StartCoefficient

    ConstraintHeatNodes_HeatFlowCoefficient = plx_enums.PropertyIDEnum.ConstraintHeatNodes_HeatFlowCoefficient

    ConstraintHeatPlants_UnitsGeneratingCoefficient = plx_enums.PropertyIDEnum.ConstraintHeatPlants_UnitsGeneratingCoefficient

    ConstraintHeatPlants_FuelOfftakeCoefficient = plx_enums.PropertyIDEnum.ConstraintHeatPlants_FuelOfftakeCoefficient

    ConstraintHeatPlants_HeatProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintHeatPlants_HeatProductionCoefficient

    ConstraintGasFields_EndVolumeCoefficient = plx_enums.PropertyIDEnum.ConstraintGasFields_EndVolumeCoefficient

    ConstraintGasFields_ProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintGasFields_ProductionCoefficient

    ConstraintGasFields_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintGasFields_RampCoefficient

    ConstraintGasFields_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasFields_UnitsBuiltCoefficient

    ConstraintGasFields_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasFields_UnitsBuiltinYearCoefficient

    ConstraintGasPlants_ProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_ProductionCoefficient

    ConstraintGasPlants_CapacityFactorCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_CapacityFactorCoefficient

    ConstraintGasPlants_OperatingHoursCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_OperatingHoursCoefficient

    ConstraintGasPlants_EnergyUsageCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_EnergyUsageCoefficient

    ConstraintGasPlants_InstalledCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_InstalledCapacityCoefficient

    ConstraintGasPlants_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_UnitsBuiltCoefficient

    ConstraintGasPlants_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_UnitsRetiredCoefficient

    ConstraintGasPlants_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_UnitsBuiltinYearCoefficient

    ConstraintGasPlants_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_UnitsRetiredinYearCoefficient

    ConstraintGasPlants_CapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_CapacityBuiltCoefficient

    ConstraintGasPlants_CapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_CapacityRetiredCoefficient

    ConstraintGasPlants_BuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_BuildCostCoefficient

    ConstraintGasPlants_BuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_BuiltCoefficient

    ConstraintGasPlants_BuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPlants_BuiltinYearCoefficient

    ConstraintGasPipelines_EndVolumeCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_EndVolumeCoefficient

    ConstraintGasPipelines_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_FlowCoefficient

    ConstraintGasPipelines_FlowForwardCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_FlowForwardCoefficient

    ConstraintGasPipelines_FlowBackCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_FlowBackCoefficient

    ConstraintGasPipelines_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_UnitsBuiltCoefficient

    ConstraintGasPipelines_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_UnitsRetiredCoefficient

    ConstraintGasPipelines_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_UnitsBuiltinYearCoefficient

    ConstraintGasPipelines_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasPipelines_UnitsRetiredinYearCoefficient

    ConstraintGasNodes_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintGasNodes_FlowCoefficient

    ConstraintGasNodes_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasNodes_UnitsBuiltCoefficient

    ConstraintGasNodes_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGasNodes_UnitsRetiredCoefficient

    ConstraintGasNodes_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasNodes_UnitsBuiltinYearCoefficient

    ConstraintGasNodes_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasNodes_UnitsRetiredinYearCoefficient

    ConstraintGasStorages_EndVolumeCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_EndVolumeCoefficient

    ConstraintGasStorages_WithdrawalCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_WithdrawalCoefficient

    ConstraintGasStorages_InjectionCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_InjectionCoefficient

    ConstraintGasStorages_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_RampCoefficient

    ConstraintGasStorages_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_UnitsBuiltCoefficient

    ConstraintGasStorages_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_UnitsRetiredCoefficient

    ConstraintGasStorages_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_UnitsBuiltinYearCoefficient

    ConstraintGasStorages_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasStorages_UnitsRetiredinYearCoefficient

    ConstraintGasBasins_ProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintGasBasins_ProductionCoefficient

    ConstraintGasBasins_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintGasBasins_UnitsBuiltCoefficient

    ConstraintGasBasins_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintGasBasins_UnitsBuiltinYearCoefficient

    ConstraintGasTransports_ShipmentsCoefficient = plx_enums.PropertyIDEnum.ConstraintGasTransports_ShipmentsCoefficient

    ConstraintGasContracts_ProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintGasContracts_ProductionCoefficient

    ConstraintWaterPlants_ProductionCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_ProductionCoefficient

    ConstraintWaterPlants_CapacityFactorCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_CapacityFactorCoefficient

    ConstraintWaterPlants_OperatingHoursCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_OperatingHoursCoefficient

    ConstraintWaterPlants_EnergyUsageCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_EnergyUsageCoefficient

    ConstraintWaterPlants_InstalledCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_InstalledCapacityCoefficient

    ConstraintWaterPlants_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_UnitsBuiltCoefficient

    ConstraintWaterPlants_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_UnitsRetiredCoefficient

    ConstraintWaterPlants_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_UnitsBuiltinYearCoefficient

    ConstraintWaterPlants_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_UnitsRetiredinYearCoefficient

    ConstraintWaterPlants_CapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_CapacityBuiltCoefficient

    ConstraintWaterPlants_CapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_CapacityRetiredCoefficient

    ConstraintWaterPlants_BuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_BuildCostCoefficient

    ConstraintWaterPlants_BuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_BuiltCoefficient

    ConstraintWaterPlants_BuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPlants_BuiltinYearCoefficient

    ConstraintWaterPipelines_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_FlowCoefficient

    ConstraintWaterPipelines_FlowForwardCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_FlowForwardCoefficient

    ConstraintWaterPipelines_FlowBackCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_FlowBackCoefficient

    ConstraintWaterPipelines_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_UnitsBuiltCoefficient

    ConstraintWaterPipelines_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_UnitsRetiredCoefficient

    ConstraintWaterPipelines_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_UnitsBuiltinYearCoefficient

    ConstraintWaterPipelines_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterPipelines_UnitsRetiredinYearCoefficient

    ConstraintWaterNodes_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterNodes_FlowCoefficient

    ConstraintWaterNodes_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterNodes_UnitsBuiltCoefficient

    ConstraintWaterNodes_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterNodes_UnitsRetiredCoefficient

    ConstraintWaterNodes_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterNodes_UnitsBuiltinYearCoefficient

    ConstraintWaterNodes_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterNodes_UnitsRetiredinYearCoefficient

    ConstraintWaterStorages_NaturalInflowCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_NaturalInflowCoefficient

    ConstraintWaterStorages_EndVolumeCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_EndVolumeCoefficient

    ConstraintWaterStorages_ReleaseCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_ReleaseCoefficient

    ConstraintWaterStorages_InflowCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_InflowCoefficient

    ConstraintWaterStorages_RampCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_RampCoefficient

    ConstraintWaterStorages_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_UnitsBuiltCoefficient

    ConstraintWaterStorages_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_UnitsRetiredCoefficient

    ConstraintWaterStorages_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_UnitsBuiltinYearCoefficient

    ConstraintWaterStorages_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintWaterStorages_UnitsRetiredinYearCoefficient

    ConstraintRegions_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_LoadCoefficient

    ConstraintRegions_LoadSquaredCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_LoadSquaredCoefficient

    ConstraintRegions_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GenerationCoefficient

    ConstraintRegions_CommittedCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_CommittedCapacityCoefficient

    ConstraintRegions_UnservedEnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_UnservedEnergyCoefficient

    ConstraintRegions_DumpEnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_DumpEnergyCoefficient

    ConstraintRegions_NetLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_NetLoadCoefficient

    ConstraintRegions_FirmCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_FirmCapacityCoefficient

    ConstraintRegions_GenerationCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GenerationCapacityCoefficient

    ConstraintRegions_PeakLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_PeakLoadCoefficient

    ConstraintRegions_CapacityReservesCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_CapacityReservesCoefficient

    ConstraintRegions_GenerationCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GenerationCapacityBuiltCoefficient

    ConstraintRegions_GenerationCapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GenerationCapacityRetiredCoefficient

    ConstraintRegions_GeneratorBuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GeneratorBuildCostCoefficient

    ConstraintRegions_GeneratorsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GeneratorsBuiltCoefficient

    ConstraintRegions_GeneratorsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_GeneratorsBuiltinYearCoefficient

    ConstraintRegions_ImportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_ImportCapacityCoefficient

    ConstraintRegions_ExportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_ExportCapacityCoefficient

    ConstraintRegions_ImportCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_ImportCapacityBuiltCoefficient

    ConstraintRegions_ExportCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintRegions_ExportCapacityBuiltCoefficient

    ConstraintZones_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_LoadCoefficient

    ConstraintZones_LoadSquaredCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_LoadSquaredCoefficient

    ConstraintZones_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GenerationCoefficient

    ConstraintZones_CommittedCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_CommittedCapacityCoefficient

    ConstraintZones_UnservedEnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_UnservedEnergyCoefficient

    ConstraintZones_DumpEnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_DumpEnergyCoefficient

    ConstraintZones_NetLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_NetLoadCoefficient

    ConstraintZones_FirmCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_FirmCapacityCoefficient

    ConstraintZones_GenerationCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GenerationCapacityCoefficient

    ConstraintZones_PeakLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_PeakLoadCoefficient

    ConstraintZones_CapacityReservesCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_CapacityReservesCoefficient

    ConstraintZones_GenerationCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GenerationCapacityBuiltCoefficient

    ConstraintZones_GenerationCapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GenerationCapacityRetiredCoefficient

    ConstraintZones_GeneratorBuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GeneratorBuildCostCoefficient

    ConstraintZones_GeneratorsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GeneratorsBuiltCoefficient

    ConstraintZones_GeneratorsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_GeneratorsBuiltinYearCoefficient

    ConstraintZones_ImportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_ImportCapacityCoefficient

    ConstraintZones_ExportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_ExportCapacityCoefficient

    ConstraintZones_ImportCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_ImportCapacityBuiltCoefficient

    ConstraintZones_ExportCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintZones_ExportCapacityBuiltCoefficient

    ConstraintNodes_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_LoadCoefficient

    ConstraintNodes_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_GenerationCoefficient

    ConstraintNodes_UnservedEnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_UnservedEnergyCoefficient

    ConstraintNodes_DumpEnergyCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_DumpEnergyCoefficient

    ConstraintNodes_NetLoadCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_NetLoadCoefficient

    ConstraintNodes_NetInjectionCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_NetInjectionCoefficient

    ConstraintNodes_PhaseAngleCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_PhaseAngleCoefficient

    ConstraintNodes_MLFCoefficient = plx_enums.PropertyIDEnum.ConstraintNodes_MLFCoefficient

    ConstraintLines_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_FlowCoefficient

    ConstraintLines_FlowForwardCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_FlowForwardCoefficient

    ConstraintLines_FlowBackCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_FlowBackCoefficient

    ConstraintLines_FlowSquaredCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_FlowSquaredCoefficient

    ConstraintLines_FlowingForwardCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_FlowingForwardCoefficient

    ConstraintLines_FlowingBackCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_FlowingBackCoefficient

    ConstraintLines_SpareExportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_SpareExportCapacityCoefficient

    ConstraintLines_SpareImportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_SpareImportCapacityCoefficient

    ConstraintLines_UnitsOutCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_UnitsOutCoefficient

    ConstraintLines_ExportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_ExportCapacityCoefficient

    ConstraintLines_ImportCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_ImportCapacityCoefficient

    ConstraintLines_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_UnitsBuiltCoefficient

    ConstraintLines_UnitsRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_UnitsRetiredCoefficient

    ConstraintLines_UnitsBuiltinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_UnitsBuiltinYearCoefficient

    ConstraintLines_UnitsRetiredinYearCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_UnitsRetiredinYearCoefficient

    ConstraintLines_ExportCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_ExportCapacityBuiltCoefficient

    ConstraintLines_ImportCapacityBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_ImportCapacityBuiltCoefficient

    ConstraintLines_ExportCapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_ExportCapacityRetiredCoefficient

    ConstraintLines_ImportCapacityRetiredCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_ImportCapacityRetiredCoefficient

    ConstraintLines_BuildCostCoefficient = plx_enums.PropertyIDEnum.ConstraintLines_BuildCostCoefficient

    ConstraintTransformers_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintTransformers_FlowCoefficient

    ConstraintFlowControls_AngleCoefficient = plx_enums.PropertyIDEnum.ConstraintFlowControls_AngleCoefficient

    ConstraintFlowControls_PositiveAngleCoefficient = plx_enums.PropertyIDEnum.ConstraintFlowControls_PositiveAngleCoefficient

    ConstraintFlowControls_NegativeAngleCoefficient = plx_enums.PropertyIDEnum.ConstraintFlowControls_NegativeAngleCoefficient

    ConstraintFlowControls_UnitsBuiltCoefficient = plx_enums.PropertyIDEnum.ConstraintFlowControls_UnitsBuiltCoefficient

    ConstraintInterfaces_FlowCoefficient = plx_enums.PropertyIDEnum.ConstraintInterfaces_FlowCoefficient

    ConstraintInterfaces_FlowForwardCoefficient = plx_enums.PropertyIDEnum.ConstraintInterfaces_FlowForwardCoefficient

    ConstraintInterfaces_FlowBackCoefficient = plx_enums.PropertyIDEnum.ConstraintInterfaces_FlowBackCoefficient

    ConstraintInterfaces_ExpansionCostCoefficient = plx_enums.PropertyIDEnum.ConstraintInterfaces_ExpansionCostCoefficient

    ConstraintHubs_LoadCoefficient = plx_enums.PropertyIDEnum.ConstraintHubs_LoadCoefficient

    ConstraintHubs_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintHubs_GenerationCoefficient

    ConstraintCompanies_GenerationCoefficient = plx_enums.PropertyIDEnum.ConstraintCompanies_GenerationCoefficient

    ConstraintCompanies_CommittedCapacityCoefficient = plx_enums.PropertyIDEnum.ConstraintCompanies_CommittedCapacityCoefficient

    ConstraintCompanies_ContractVolumeCoefficient = plx_enums.PropertyIDEnum.ConstraintCompanies_ContractVolumeCoefficient

    ConstraintConditions_RHSCoefficient = plx_enums.PropertyIDEnum.ConstraintConditions_RHSCoefficient

    ConstraintDecisionVariables_ValueCoefficient = plx_enums.PropertyIDEnum.ConstraintDecisionVariables_ValueCoefficient

    ConstraintDecisionVariables_ValueSquaredCoefficient = plx_enums.PropertyIDEnum.ConstraintDecisionVariables_ValueSquaredCoefficient

    ConstraintVariables_ExpectedValueCoefficient = plx_enums.PropertyIDEnum.ConstraintVariables_ExpectedValueCoefficient

    ConstraintVariables_ValueCoefficient = plx_enums.PropertyIDEnum.ConstraintVariables_ValueCoefficient

    ConstraintVariables_ErrorCoefficient = plx_enums.PropertyIDEnum.ConstraintVariables_ErrorCoefficient

    ConstraintVariables_PositiveErrorCoefficient = plx_enums.PropertyIDEnum.ConstraintVariables_PositiveErrorCoefficient

    ConstraintVariables_NegativeErrorCoefficient = plx_enums.PropertyIDEnum.ConstraintVariables_NegativeErrorCoefficient

    DecisionVariableGenerators_HeatInputDefinitionCoefficient = plx_enums.PropertyIDEnum.DecisionVariableGenerators_HeatInputDefinitionCoefficient

    DecisionVariableNodes_NetInjectionDefinitionCoefficient = plx_enums.PropertyIDEnum.DecisionVariableNodes_NetInjectionDefinitionCoefficient

    DecisionVariableGasPlants_EnergyUsageDefinitionCoefficient = plx_enums.PropertyIDEnum.DecisionVariableGasPlants_EnergyUsageDefinitionCoefficient

    DecisionVariableWaterPlants_EnergyUsageDefinitionCoefficient = plx_enums.PropertyIDEnum.DecisionVariableWaterPlants_EnergyUsageDefinitionCoefficient

    DecisionVariableDefinition_ValueCoefficient = plx_enums.PropertyIDEnum.DecisionVariableDefinition_ValueCoefficient

    VariableGenerators_GenerationCoefficient = plx_enums.PropertyIDEnum.VariableGenerators_GenerationCoefficient

    VariableGenerators_UnitsGeneratingCoefficient = plx_enums.PropertyIDEnum.VariableGenerators_UnitsGeneratingCoefficient

    VariableGenerators_UnitsStartedCoefficient = plx_enums.PropertyIDEnum.VariableGenerators_UnitsStartedCoefficient

    VariableGenerators_UnitsSyncCondCoefficient = plx_enums.PropertyIDEnum.VariableGenerators_UnitsSyncCondCoefficient

    VariableGenerators_FuelOfftakeCoefficient = plx_enums.PropertyIDEnum.VariableGenerators_FuelOfftakeCoefficient

    VariableGenerators_UnitsOutCoefficient = plx_enums.PropertyIDEnum.VariableGenerators_UnitsOutCoefficient

    VariableFuels_OfftakeCoefficient = plx_enums.PropertyIDEnum.VariableFuels_OfftakeCoefficient

    VariableHeatNodes_HeatFlowCoefficient = plx_enums.PropertyIDEnum.VariableHeatNodes_HeatFlowCoefficient

    VariableHeatPlants_FuelOfftakeCoefficient = plx_enums.PropertyIDEnum.VariableHeatPlants_FuelOfftakeCoefficient

    VariableReserves_ProvisionCoefficient = plx_enums.PropertyIDEnum.VariableReserves_ProvisionCoefficient

    VariableReserves_RiskCoefficient = plx_enums.PropertyIDEnum.VariableReserves_RiskCoefficient

    VariableReserves_ShortageCoefficient = plx_enums.PropertyIDEnum.VariableReserves_ShortageCoefficient

    VariableRegions_LoadCoefficient = plx_enums.PropertyIDEnum.VariableRegions_LoadCoefficient

    VariableRegions_CapacityReservesCoefficient = plx_enums.PropertyIDEnum.VariableRegions_CapacityReservesCoefficient

    VariableRegions_PriceCoefficient = plx_enums.PropertyIDEnum.VariableRegions_PriceCoefficient

    VariableZones_LoadCoefficient = plx_enums.PropertyIDEnum.VariableZones_LoadCoefficient

    VariableZones_CapacityReservesCoefficient = plx_enums.PropertyIDEnum.VariableZones_CapacityReservesCoefficient

    VariableNodes_LoadCoefficient = plx_enums.PropertyIDEnum.VariableNodes_LoadCoefficient

    VariableLines_FlowCoefficient = plx_enums.PropertyIDEnum.VariableLines_FlowCoefficient

    VariableLines_FlowForwardCoefficient = plx_enums.PropertyIDEnum.VariableLines_FlowForwardCoefficient

    VariableLines_FlowBackCoefficient = plx_enums.PropertyIDEnum.VariableLines_FlowBackCoefficient

    VariableLines_FlowingForwardCoefficient = plx_enums.PropertyIDEnum.VariableLines_FlowingForwardCoefficient

    VariableLines_FlowingBackCoefficient = plx_enums.PropertyIDEnum.VariableLines_FlowingBackCoefficient

    VariableInterfaces_FlowCoefficient = plx_enums.PropertyIDEnum.VariableInterfaces_FlowCoefficient

    VariableStorages_EndVolumeCoefficient = plx_enums.PropertyIDEnum.VariableStorages_EndVolumeCoefficient

    VariableStorages_InflowCoefficient = plx_enums.PropertyIDEnum.VariableStorages_InflowCoefficient

    VariableStorages_ReleaseCoefficient = plx_enums.PropertyIDEnum.VariableStorages_ReleaseCoefficient

    VariableStorages_SpillCoefficient = plx_enums.PropertyIDEnum.VariableStorages_SpillCoefficient

    VariableVariables_Correlation = plx_enums.PropertyIDEnum.VariableVariables_Correlation

    VariableVariables_ValueCoefficient = plx_enums.PropertyIDEnum.VariableVariables_ValueCoefficient

    GlobalStorages_FCFShadowPrice = plx_enums.PropertyIDEnum.GlobalStorages_FCFShadowPrice

    ModelScenarios_ReadOrder = plx_enums.PropertyIDEnum.ModelScenarios_ReadOrder


class PropertyStatusEnum(Enum):
    Undefined = plx_enums.PropertyStatusEnum.Undefined

    Static1 = plx_enums.PropertyStatusEnum.Static1

    Dynamic = plx_enums.PropertyStatusEnum.Dynamic

    Series = plx_enums.PropertyStatusEnum.Series

    Cached = plx_enums.PropertyStatusEnum.Cached

    CachedCompressed = plx_enums.PropertyStatusEnum.CachedCompressed

    Interleaved = plx_enums.PropertyStatusEnum.Interleaved


class PumpedStorageModeEnum(Enum):
    None_ = 0

    Optimize = plx_enums.PumpedStorageModeEnum.Optimize

    Fixed = plx_enums.PumpedStorageModeEnum.Fixed


class PurchaserCompaniesEnum(Enum):
    Share = plx_enums.PurchaserCompaniesEnum.Share


class PurchaserNodesEnum(Enum):
    LoadParticipationFactor = plx_enums.PurchaserNodesEnum.LoadParticipationFactor


class QueriedColumnCountEnum(Enum):
    Properties = plx_enums.QueriedColumnCountEnum.Properties

    Periods = plx_enums.QueriedColumnCountEnum.Periods

    Names = plx_enums.QueriedColumnCountEnum.Names

    Values = plx_enums.QueriedColumnCountEnum.Values

    Statistics = plx_enums.QueriedColumnCountEnum.Statistics

    Samples = plx_enums.QueriedColumnCountEnum.Samples

    Timeslices = plx_enums.QueriedColumnCountEnum.Timeslices

    Bands = plx_enums.QueriedColumnCountEnum.Bands

    Models = plx_enums.QueriedColumnCountEnum.Models


class RegionRegionsEnum(Enum):
    WheelingCharge = plx_enums.RegionRegionsEnum.WheelingCharge

    MaxFlow = plx_enums.RegionRegionsEnum.MaxFlow


class RepairTimeDistributionEnum(Enum):
    Constant = plx_enums.RepairTimeDistributionEnum.Constant

    Uniform = plx_enums.RepairTimeDistributionEnum.Uniform

    Triangular = plx_enums.RepairTimeDistributionEnum.Triangular

    Exponential = plx_enums.RepairTimeDistributionEnum.Exponential

    Weibull = plx_enums.RepairTimeDistributionEnum.Weibull

    Lognormal = plx_enums.RepairTimeDistributionEnum.Lognormal

    SEV = plx_enums.RepairTimeDistributionEnum.SEV

    LEV = plx_enums.RepairTimeDistributionEnum.LEV

    None_ = -1


class ReportAttributeEnum(Enum):
    WriteDatabase = plx_enums.ReportAttributeEnum.WriteDatabase

    WriteFlatFiles = plx_enums.ReportAttributeEnum.WriteFlatFiles

    WriteXMLFiles = plx_enums.ReportAttributeEnum.WriteXMLFiles

    XMLContent = plx_enums.ReportAttributeEnum.XMLContent

    OutputResultsbyPeriod = plx_enums.ReportAttributeEnum.OutputResultsbyPeriod

    OutputResultsbyHour = plx_enums.ReportAttributeEnum.OutputResultsbyHour

    OutputResultsbyDay = plx_enums.ReportAttributeEnum.OutputResultsbyDay

    OutputResultsbyWeek = plx_enums.ReportAttributeEnum.OutputResultsbyWeek

    OutputResultsbyMonth = plx_enums.ReportAttributeEnum.OutputResultsbyMonth

    OutputResultsbyQuarter = plx_enums.ReportAttributeEnum.OutputResultsbyQuarter

    OutputResultsbyFiscalYear = plx_enums.ReportAttributeEnum.OutputResultsbyFiscalYear

    OutputStatistics = plx_enums.ReportAttributeEnum.OutputStatistics

    OutputResultsbySample = plx_enums.ReportAttributeEnum.OutputResultsbySample

    FilterObjectsByInterval = plx_enums.ReportAttributeEnum.FilterObjectsByInterval

    FilterObjectsInSummary = plx_enums.ReportAttributeEnum.FilterObjectsInSummary

    WholeYearsOnly = plx_enums.ReportAttributeEnum.WholeYearsOnly

    DatetimeConvention = plx_enums.ReportAttributeEnum.DatetimeConvention

    Locale = plx_enums.ReportAttributeEnum.Locale

    FlatFileFormat = plx_enums.ReportAttributeEnum.FlatFileFormat


class ReserveBatteriesEnum(Enum):
    OfferQuantity = plx_enums.ReserveBatteriesEnum.OfferQuantity

    OfferPrice = plx_enums.ReserveBatteriesEnum.OfferPrice


class ReserveGeneratorsEnum(Enum):
    InitialPumpLoadRaiseProvision = plx_enums.ReserveGeneratorsEnum.InitialPumpLoadRaiseProvision

    InitialRaiseProvision = plx_enums.ReserveGeneratorsEnum.InitialRaiseProvision

    MaxResponse = plx_enums.ReserveGeneratorsEnum.MaxResponse

    MaxSyncCondResponse = plx_enums.ReserveGeneratorsEnum.MaxSyncCondResponse

    MaxPumpResponse = plx_enums.ReserveGeneratorsEnum.MaxPumpResponse

    MaxReplacement = plx_enums.ReserveGeneratorsEnum.MaxReplacement

    MaxResponseFactor = plx_enums.ReserveGeneratorsEnum.MaxResponseFactor

    MaxSyncCondResponseFactor = plx_enums.ReserveGeneratorsEnum.MaxSyncCondResponseFactor

    MaxPumpResponseFactor = plx_enums.ReserveGeneratorsEnum.MaxPumpResponseFactor

    MaxReplacementFactor = plx_enums.ReserveGeneratorsEnum.MaxReplacementFactor

    MinProvision = plx_enums.ReserveGeneratorsEnum.MinProvision

    MinSpinningProvision = plx_enums.ReserveGeneratorsEnum.MinSpinningProvision

    MinRegulationProvision = plx_enums.ReserveGeneratorsEnum.MinRegulationProvision

    MinReplacementProvision = plx_enums.ReserveGeneratorsEnum.MinReplacementProvision

    Effectiveness = plx_enums.ReserveGeneratorsEnum.Effectiveness

    ResponseRatio = plx_enums.ReserveGeneratorsEnum.ResponseRatio

    OfferQuantity = plx_enums.ReserveGeneratorsEnum.OfferQuantity

    OfferPrice = plx_enums.ReserveGeneratorsEnum.OfferPrice

    SyncCondOfferPrice = plx_enums.ReserveGeneratorsEnum.SyncCondOfferPrice

    PumpOfferPrice = plx_enums.ReserveGeneratorsEnum.PumpOfferPrice

    ReplacementOfferQuantity = plx_enums.ReserveGeneratorsEnum.ReplacementOfferQuantity

    ReplacementOfferPrice = plx_enums.ReserveGeneratorsEnum.ReplacementOfferPrice


class ReserveLineContingenciesEnum(Enum):
    FlowForwardCoefficient = plx_enums.ReserveLineContingenciesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.ReserveLineContingenciesEnum.FlowBackCoefficient


class ReserveMutuallyExclusiveEnum(Enum):
    Auto = plx_enums.ReserveMutuallyExclusiveEnum.Auto

    Yes = plx_enums.ReserveMutuallyExclusiveEnum.Yes

    No = plx_enums.ReserveMutuallyExclusiveEnum.No


class ReservePurchasersEnum(Enum):
    OfferQuantity = plx_enums.ReservePurchasersEnum.OfferQuantity

    OfferPrice = plx_enums.ReservePurchasersEnum.OfferPrice


class ReserveRegionsEnum(Enum):
    LoadRisk = plx_enums.ReserveRegionsEnum.LoadRisk

    LOLPTarget = plx_enums.ReserveRegionsEnum.LOLPTarget


class ReserveTypeEnum(Enum):
    Raise = plx_enums.ReserveTypeEnum.Raise

    Lower = plx_enums.ReserveTypeEnum.Lower

    RegulationRaise = plx_enums.ReserveTypeEnum.RegulationRaise

    RegulationLower = plx_enums.ReserveTypeEnum.RegulationLower

    Replacement = plx_enums.ReserveTypeEnum.Replacement

    Operational = plx_enums.ReserveTypeEnum.Operational

    Regulation = plx_enums.ReserveTypeEnum.Regulation


class STScheduleAttributeEnum(Enum):
    DiscountRate = plx_enums.STScheduleAttributeEnum.DiscountRate

    DiscountPeriodType = plx_enums.STScheduleAttributeEnum.DiscountPeriodType

    EndEffectsMethod = plx_enums.STScheduleAttributeEnum.EndEffectsMethod

    HeatRateDetail = plx_enums.STScheduleAttributeEnum.HeatRateDetail

    TransmissionDetail = plx_enums.STScheduleAttributeEnum.TransmissionDetail

    StochasticMethod = plx_enums.STScheduleAttributeEnum.StochasticMethod


class ScenarioAttributeEnum(Enum):
    ReadOrder = plx_enums.ScenarioAttributeEnum.ReadOrder

    Locked = plx_enums.ScenarioAttributeEnum.Locked


class SenseEnum(Enum):
    FX = plx_enums.SenseEnum.FX

    LO = plx_enums.SenseEnum.LO

    UP = plx_enums.SenseEnum.UP


class SeriesTypeEnum(Enum):
    Values = plx_enums.SeriesTypeEnum.Values

    Properties = plx_enums.SeriesTypeEnum.Properties

    Names = plx_enums.SeriesTypeEnum.Names

    Periods = plx_enums.SeriesTypeEnum.Periods

    Bands = plx_enums.SeriesTypeEnum.Bands

    Statistics = plx_enums.SeriesTypeEnum.Statistics

    Samples = plx_enums.SeriesTypeEnum.Samples

    Models = plx_enums.SeriesTypeEnum.Models

    Timeslices = plx_enums.SeriesTypeEnum.Timeslices


class SimulationPhaseEnum(Enum):
    LTPlan = plx_enums.SimulationPhaseEnum.LTPlan

    PASA = plx_enums.SimulationPhaseEnum.PASA

    MTSchedule = plx_enums.SimulationPhaseEnum.MTSchedule

    STSchedule = plx_enums.SimulationPhaseEnum.STSchedule


class SolutionPeriodEnum(Enum):
    Period = plx_enums.SolutionPeriodEnum.Period

    Summary = plx_enums.SolutionPeriodEnum.Summary


class StartCostFunctionEnum(Enum):
    Interpolate = plx_enums.StartCostFunctionEnum.Interpolate

    StepFunction = plx_enums.StartCostFunctionEnum.StepFunction


class StatisticsEnum(Enum):
    Mean = plx_enums.StatisticsEnum.Mean

    Max = plx_enums.StatisticsEnum.Max

    Min = plx_enums.StatisticsEnum.Min

    StdDev = plx_enums.StatisticsEnum.StdDev


class StochasticAttributeEnum(Enum):
    OutagePatternCount = plx_enums.StochasticAttributeEnum.OutagePatternCount

    MonteCarloMethod = plx_enums.StochasticAttributeEnum.MonteCarloMethod

    WeibullShape = plx_enums.StochasticAttributeEnum.WeibullShape

    ConvergentSmoothing = plx_enums.StochasticAttributeEnum.ConvergentSmoothing

    OutageScope = plx_enums.StochasticAttributeEnum.OutageScope

    ConvergencePeriodType = plx_enums.StochasticAttributeEnum.ConvergencePeriodType

    RiskSampleCount = plx_enums.StochasticAttributeEnum.RiskSampleCount

    ReducedOutagePatternCount = plx_enums.StochasticAttributeEnum.ReducedOutagePatternCount

    ReducedSampleCount = plx_enums.StochasticAttributeEnum.ReducedSampleCount

    ReductionRelativeAccuracy = plx_enums.StochasticAttributeEnum.ReductionRelativeAccuracy

    ForcedOutagesinLookahead = plx_enums.StochasticAttributeEnum.ForcedOutagesinLookahead

    EFORMaintenanceAdjust = plx_enums.StochasticAttributeEnum.EFORMaintenanceAdjust


class StochasticMethodEnum(Enum):
    Deterministic = plx_enums.StochasticMethodEnum.Deterministic

    IndependentSamples = plx_enums.StochasticMethodEnum.IndependentSamples

    ScenariowiseDecomposition = plx_enums.StochasticMethodEnum.ScenariowiseDecomposition

    Parallel = plx_enums.StochasticMethodEnum.Parallel


class StorageAttributeEnum(Enum):
    Latitude = plx_enums.StorageAttributeEnum.Latitude

    Longitude = plx_enums.StorageAttributeEnum.Longitude


class StorageBridgeEnum(Enum):
    InitialVolume = plx_enums.StorageBridgeEnum.InitialVolume

    EndVolume = plx_enums.StorageBridgeEnum.EndVolume

    ShadowPrice = plx_enums.StorageBridgeEnum.ShadowPrice


class StorageDecompositionMethodEnum(Enum):
    None_ = 0

    Target = plx_enums.StorageDecompositionMethodEnum.Target

    WaterValue = plx_enums.StorageDecompositionMethodEnum.WaterValue


class StorageEndEffectsMethodEnum(Enum):
    Automatic = plx_enums.StorageEndEffectsMethodEnum.Automatic

    Free = plx_enums.StorageEndEffectsMethodEnum.Free

    Recyle = plx_enums.StorageEndEffectsMethodEnum.Recyle


class SummaryTypeEnum(Enum):
    None_ = 0

    Sum = plx_enums.SummaryTypeEnum.Sum

    Avg = plx_enums.SummaryTypeEnum.Avg

    Min = plx_enums.SummaryTypeEnum.Min

    Max = plx_enums.SummaryTypeEnum.Max

    MaxAbs = plx_enums.SummaryTypeEnum.MaxAbs

    ZeroBoundedDifference = plx_enums.SummaryTypeEnum.ZeroBoundedDifference

    AtExactInterval = plx_enums.SummaryTypeEnum.AtExactInterval

    AtExactIntervalSum = plx_enums.SummaryTypeEnum.AtExactIntervalSum

    AtExactIntervalLast = plx_enums.SummaryTypeEnum.AtExactIntervalLast

    First = plx_enums.SummaryTypeEnum.First

    Last = plx_enums.SummaryTypeEnum.Last


class SystemAbatementsEnum(Enum):
    Units = plx_enums.SystemAbatementsEnum.Units

    AbatementCost = plx_enums.SystemAbatementsEnum.AbatementCost

    RunningCost = plx_enums.SystemAbatementsEnum.RunningCost

    VOMCharge = plx_enums.SystemAbatementsEnum.VOMCharge

    Efficiency = plx_enums.SystemAbatementsEnum.Efficiency

    MaxAbatement = plx_enums.SystemAbatementsEnum.MaxAbatement

    FOMCharge = plx_enums.SystemAbatementsEnum.FOMCharge

    UnitsOut = plx_enums.SystemAbatementsEnum.UnitsOut

    x = plx_enums.SystemAbatementsEnum.x

    y = plx_enums.SystemAbatementsEnum.y

    z = plx_enums.SystemAbatementsEnum.z


class SystemBatteriesEnum(Enum):
    RandomNumberSeed = plx_enums.SystemBatteriesEnum.RandomNumberSeed

    RepairTimeDistribution = plx_enums.SystemBatteriesEnum.RepairTimeDistribution

    EndEffectsMethod = plx_enums.SystemBatteriesEnum.EndEffectsMethod

    ExpansionOptimality = plx_enums.SystemBatteriesEnum.ExpansionOptimality

    Units = plx_enums.SystemBatteriesEnum.Units

    Capacity = plx_enums.SystemBatteriesEnum.Capacity

    MaxPower = plx_enums.SystemBatteriesEnum.MaxPower

    MaxLoad = plx_enums.SystemBatteriesEnum.MaxLoad

    MaxSoC = plx_enums.SystemBatteriesEnum.MaxSoC

    MinSoC = plx_enums.SystemBatteriesEnum.MinSoC

    InitialSoC = plx_enums.SystemBatteriesEnum.InitialSoC

    ChargeEfficiency = plx_enums.SystemBatteriesEnum.ChargeEfficiency

    DischargeEfficiency = plx_enums.SystemBatteriesEnum.DischargeEfficiency

    VOMCharge = plx_enums.SystemBatteriesEnum.VOMCharge

    UoSCharge = plx_enums.SystemBatteriesEnum.UoSCharge

    MaxRampUp = plx_enums.SystemBatteriesEnum.MaxRampUp

    MaxRampUpPenalty = plx_enums.SystemBatteriesEnum.MaxRampUpPenalty

    MaxRampDown = plx_enums.SystemBatteriesEnum.MaxRampDown

    MaxRampDownPenalty = plx_enums.SystemBatteriesEnum.MaxRampDownPenalty

    MaxCycles = plx_enums.SystemBatteriesEnum.MaxCycles

    EnergyTarget = plx_enums.SystemBatteriesEnum.EnergyTarget

    EnergyTargetPenalty = plx_enums.SystemBatteriesEnum.EnergyTargetPenalty

    Nonanticipativity = plx_enums.SystemBatteriesEnum.Nonanticipativity

    NonanticipativityTime = plx_enums.SystemBatteriesEnum.NonanticipativityTime

    InitialAge = plx_enums.SystemBatteriesEnum.InitialAge

    PowerDegradation = plx_enums.SystemBatteriesEnum.PowerDegradation

    CapacityDegradation = plx_enums.SystemBatteriesEnum.CapacityDegradation

    FirmCapacity = plx_enums.SystemBatteriesEnum.FirmCapacity

    FOMCharge = plx_enums.SystemBatteriesEnum.FOMCharge

    MaintenanceRate = plx_enums.SystemBatteriesEnum.MaintenanceRate

    MaintenanceFrequency = plx_enums.SystemBatteriesEnum.MaintenanceFrequency

    ForcedOutageRate = plx_enums.SystemBatteriesEnum.ForcedOutageRate

    MeanTimetoRepair = plx_enums.SystemBatteriesEnum.MeanTimetoRepair

    MinTimeToRepair = plx_enums.SystemBatteriesEnum.MinTimeToRepair

    MaxTimeToRepair = plx_enums.SystemBatteriesEnum.MaxTimeToRepair

    RepairTimeShape = plx_enums.SystemBatteriesEnum.RepairTimeShape

    RepairTimeScale = plx_enums.SystemBatteriesEnum.RepairTimeScale

    MaxUnitsBuilt = plx_enums.SystemBatteriesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemBatteriesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemBatteriesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemBatteriesEnum.TechnicalLife

    BuildCost = plx_enums.SystemBatteriesEnum.BuildCost

    WACC = plx_enums.SystemBatteriesEnum.WACC

    EconomicLife = plx_enums.SystemBatteriesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemBatteriesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemBatteriesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemBatteriesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemBatteriesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemBatteriesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemBatteriesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemBatteriesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemBatteriesEnum.MinUnitsRetiredinYear

    BuildNonanticipativity = plx_enums.SystemBatteriesEnum.BuildNonanticipativity

    RetireNonanticipativity = plx_enums.SystemBatteriesEnum.RetireNonanticipativity

    x = plx_enums.SystemBatteriesEnum.x

    y = plx_enums.SystemBatteriesEnum.y

    z = plx_enums.SystemBatteriesEnum.z


class SystemCompaniesEnum(Enum):
    Strategic = plx_enums.SystemCompaniesEnum.Strategic

    MarkupBias = plx_enums.SystemCompaniesEnum.MarkupBias

    FormulateRisk = plx_enums.SystemCompaniesEnum.FormulateRisk

    RiskLevel = plx_enums.SystemCompaniesEnum.RiskLevel

    AcceptableRisk = plx_enums.SystemCompaniesEnum.AcceptableRisk

    MaxMaintenance = plx_enums.SystemCompaniesEnum.MaxMaintenance

    MinMaintenance = plx_enums.SystemCompaniesEnum.MinMaintenance

    MaxMaintenanceFactor = plx_enums.SystemCompaniesEnum.MaxMaintenanceFactor

    MinMaintenanceFactor = plx_enums.SystemCompaniesEnum.MinMaintenanceFactor

    x = plx_enums.SystemCompaniesEnum.x

    y = plx_enums.SystemCompaniesEnum.y

    z = plx_enums.SystemCompaniesEnum.z


class SystemConstraintsEnum(Enum):
    Sense = plx_enums.SystemConstraintsEnum.Sense

    LHSType = plx_enums.SystemConstraintsEnum.LHSType

    FormulateUpfront = plx_enums.SystemConstraintsEnum.FormulateUpfront

    ConditionLogic = plx_enums.SystemConstraintsEnum.ConditionLogic

    IncludeinLTPlan = plx_enums.SystemConstraintsEnum.IncludeinLTPlan

    IncludeinPASA = plx_enums.SystemConstraintsEnum.IncludeinPASA

    IncludeinMTSchedule = plx_enums.SystemConstraintsEnum.IncludeinMTSchedule

    IncludeinSTSchedule = plx_enums.SystemConstraintsEnum.IncludeinSTSchedule

    IncludeinUniformPricing = plx_enums.SystemConstraintsEnum.IncludeinUniformPricing

    DecompositionMethod = plx_enums.SystemConstraintsEnum.DecompositionMethod

    FeasibilityRepairWeight = plx_enums.SystemConstraintsEnum.FeasibilityRepairWeight

    WildcardMode = plx_enums.SystemConstraintsEnum.WildcardMode

    RHS = plx_enums.SystemConstraintsEnum.RHS

    PenaltyQuantity = plx_enums.SystemConstraintsEnum.PenaltyQuantity

    PenaltyPrice = plx_enums.SystemConstraintsEnum.PenaltyPrice

    MinRHS = plx_enums.SystemConstraintsEnum.MinRHS

    MaxRHS = plx_enums.SystemConstraintsEnum.MaxRHS

    x = plx_enums.SystemConstraintsEnum.x

    y = plx_enums.SystemConstraintsEnum.y

    z = plx_enums.SystemConstraintsEnum.z


class SystemContingenciesEnum(Enum):
    IsEnabled = plx_enums.SystemContingenciesEnum.IsEnabled

    MonitoringThreshold = plx_enums.SystemContingenciesEnum.MonitoringThreshold

    x = plx_enums.SystemContingenciesEnum.x

    y = plx_enums.SystemContingenciesEnum.y

    z = plx_enums.SystemContingenciesEnum.z


class SystemCournotsEnum(Enum):
    DemandIntercept = plx_enums.SystemCournotsEnum.DemandIntercept

    DemandSlope = plx_enums.SystemCournotsEnum.DemandSlope


class SystemDataFilesEnum(Enum):
    Filename = plx_enums.SystemDataFilesEnum.Filename

    BaseProfile = plx_enums.SystemDataFilesEnum.BaseProfile

    Energy = plx_enums.SystemDataFilesEnum.Energy

    Maximum = plx_enums.SystemDataFilesEnum.Maximum

    Minimum = plx_enums.SystemDataFilesEnum.Minimum

    Holiday = plx_enums.SystemDataFilesEnum.Holiday

    MinValue = plx_enums.SystemDataFilesEnum.MinValue

    MaxValue = plx_enums.SystemDataFilesEnum.MaxValue


class SystemDecisionVariablesEnum(Enum):
    IncludeinLTPlan = plx_enums.SystemDecisionVariablesEnum.IncludeinLTPlan

    IncludeinPASA = plx_enums.SystemDecisionVariablesEnum.IncludeinPASA

    IncludeinMTSchedule = plx_enums.SystemDecisionVariablesEnum.IncludeinMTSchedule

    IncludeinSTSchedule = plx_enums.SystemDecisionVariablesEnum.IncludeinSTSchedule

    ObjectiveFunctionCoefficient = plx_enums.SystemDecisionVariablesEnum.ObjectiveFunctionCoefficient

    LowerBound = plx_enums.SystemDecisionVariablesEnum.LowerBound

    UpperBound = plx_enums.SystemDecisionVariablesEnum.UpperBound

    Nonanticipativity = plx_enums.SystemDecisionVariablesEnum.Nonanticipativity

    NonanticipativityTime = plx_enums.SystemDecisionVariablesEnum.NonanticipativityTime

    x = plx_enums.SystemDecisionVariablesEnum.x

    y = plx_enums.SystemDecisionVariablesEnum.y

    z = plx_enums.SystemDecisionVariablesEnum.z


class SystemEmissionsEnum(Enum):
    Price = plx_enums.SystemEmissionsEnum.Price

    MaxProduction = plx_enums.SystemEmissionsEnum.MaxProduction

    MaxProductionPenalty = plx_enums.SystemEmissionsEnum.MaxProductionPenalty

    ShadowPrice = plx_enums.SystemEmissionsEnum.ShadowPrice

    x = plx_enums.SystemEmissionsEnum.x

    y = plx_enums.SystemEmissionsEnum.y

    z = plx_enums.SystemEmissionsEnum.z


class SystemFinancialContractsEnum(Enum):
    IsPhysical = plx_enums.SystemFinancialContractsEnum.IsPhysical

    Quantity = plx_enums.SystemFinancialContractsEnum.Quantity

    FloorPrice = plx_enums.SystemFinancialContractsEnum.FloorPrice

    CapPrice = plx_enums.SystemFinancialContractsEnum.CapPrice


class SystemFlowControlsEnum(Enum):
    PriceSetting = plx_enums.SystemFlowControlsEnum.PriceSetting

    ExpansionOptimality = plx_enums.SystemFlowControlsEnum.ExpansionOptimality

    Type = plx_enums.SystemFlowControlsEnum.Type

    Units = plx_enums.SystemFlowControlsEnum.Units

    MinAngle = plx_enums.SystemFlowControlsEnum.MinAngle

    MaxAngle = plx_enums.SystemFlowControlsEnum.MaxAngle

    MinImpedance = plx_enums.SystemFlowControlsEnum.MinImpedance

    MaxImpedance = plx_enums.SystemFlowControlsEnum.MaxImpedance

    MinVoltage = plx_enums.SystemFlowControlsEnum.MinVoltage

    MaxVoltage = plx_enums.SystemFlowControlsEnum.MaxVoltage

    Penalty = plx_enums.SystemFlowControlsEnum.Penalty

    Angle = plx_enums.SystemFlowControlsEnum.Angle

    AnglePoints = plx_enums.SystemFlowControlsEnum.AnglePoints

    FlowLoadingPoints = plx_enums.SystemFlowControlsEnum.FlowLoadingPoints

    FOMCharge = plx_enums.SystemFlowControlsEnum.FOMCharge

    BuildCost = plx_enums.SystemFlowControlsEnum.BuildCost

    LeadTime = plx_enums.SystemFlowControlsEnum.LeadTime

    ProjectStartDate = plx_enums.SystemFlowControlsEnum.ProjectStartDate

    CommissionDate = plx_enums.SystemFlowControlsEnum.CommissionDate

    TechnicalLife = plx_enums.SystemFlowControlsEnum.TechnicalLife

    WACC = plx_enums.SystemFlowControlsEnum.WACC

    EconomicLife = plx_enums.SystemFlowControlsEnum.EconomicLife

    MaxUnitsBuilt = plx_enums.SystemFlowControlsEnum.MaxUnitsBuilt

    MinUnitsBuilt = plx_enums.SystemFlowControlsEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemFlowControlsEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemFlowControlsEnum.MinUnitsBuiltinYear

    BuildNonanticipativity = plx_enums.SystemFlowControlsEnum.BuildNonanticipativity

    x = plx_enums.SystemFlowControlsEnum.x

    y = plx_enums.SystemFlowControlsEnum.y

    z = plx_enums.SystemFlowControlsEnum.z


class SystemFuelContractsEnum(Enum):
    Quantity = plx_enums.SystemFuelContractsEnum.Quantity

    Price = plx_enums.SystemFuelContractsEnum.Price

    PriceIncr = plx_enums.SystemFuelContractsEnum.PriceIncr

    PriceScalar = plx_enums.SystemFuelContractsEnum.PriceScalar

    TakeorPayQuantity = plx_enums.SystemFuelContractsEnum.TakeorPayQuantity

    TakeorPayPrice = plx_enums.SystemFuelContractsEnum.TakeorPayPrice

    FOMCharge = plx_enums.SystemFuelContractsEnum.FOMCharge

    x = plx_enums.SystemFuelContractsEnum.x

    y = plx_enums.SystemFuelContractsEnum.y

    z = plx_enums.SystemFuelContractsEnum.z


class SystemFuelsEnum(Enum):
    BalancePeriod = plx_enums.SystemFuelsEnum.BalancePeriod

    DecompositionMethod = plx_enums.SystemFuelsEnum.DecompositionMethod

    DecompositionPenaltya = plx_enums.SystemFuelsEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.SystemFuelsEnum.DecompositionPenaltyb

    DecompositionPenaltyc = plx_enums.SystemFuelsEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.SystemFuelsEnum.DecompositionPenaltyx

    DecompositionBoundPenalty = plx_enums.SystemFuelsEnum.DecompositionBoundPenalty

    Units = plx_enums.SystemFuelsEnum.Units

    Price = plx_enums.SystemFuelsEnum.Price

    Tax = plx_enums.SystemFuelsEnum.Tax

    PriceIncr = plx_enums.SystemFuelsEnum.PriceIncr

    PriceScalar = plx_enums.SystemFuelsEnum.PriceScalar

    HeatValue = plx_enums.SystemFuelsEnum.HeatValue

    MaxOfftake = plx_enums.SystemFuelsEnum.MaxOfftake

    MinOfftake = plx_enums.SystemFuelsEnum.MinOfftake

    ShadowPrice = plx_enums.SystemFuelsEnum.ShadowPrice

    ShadowPriceIncr = plx_enums.SystemFuelsEnum.ShadowPriceIncr

    ShadowPriceScalar = plx_enums.SystemFuelsEnum.ShadowPriceScalar

    MaxInventory = plx_enums.SystemFuelsEnum.MaxInventory

    MinInventory = plx_enums.SystemFuelsEnum.MinInventory

    OpeningInventory = plx_enums.SystemFuelsEnum.OpeningInventory

    Delivery = plx_enums.SystemFuelsEnum.Delivery

    DeliveryCharge = plx_enums.SystemFuelsEnum.DeliveryCharge

    InventoryCharge = plx_enums.SystemFuelsEnum.InventoryCharge

    ReservationCharge = plx_enums.SystemFuelsEnum.ReservationCharge

    WithdrawalCharge = plx_enums.SystemFuelsEnum.WithdrawalCharge

    MaxWithdrawal = plx_enums.SystemFuelsEnum.MaxWithdrawal

    MinWithdrawal = plx_enums.SystemFuelsEnum.MinWithdrawal

    FOMCharge = plx_enums.SystemFuelsEnum.FOMCharge

    x = plx_enums.SystemFuelsEnum.x

    y = plx_enums.SystemFuelsEnum.y

    z = plx_enums.SystemFuelsEnum.z


class SystemGasBasinsEnum(Enum):
    MaxProduction = plx_enums.SystemGasBasinsEnum.MaxProduction

    MinProduction = plx_enums.SystemGasBasinsEnum.MinProduction

    x = plx_enums.SystemGasBasinsEnum.x

    y = plx_enums.SystemGasBasinsEnum.y

    z = plx_enums.SystemGasBasinsEnum.z


class SystemGasContractsEnum(Enum):
    PriceSetting = plx_enums.SystemGasContractsEnum.PriceSetting

    Quantity = plx_enums.SystemGasContractsEnum.Quantity

    TakeorPayQuantity = plx_enums.SystemGasContractsEnum.TakeorPayQuantity

    TakeorPayPrice = plx_enums.SystemGasContractsEnum.TakeorPayPrice

    Price = plx_enums.SystemGasContractsEnum.Price

    x = plx_enums.SystemGasContractsEnum.x

    y = plx_enums.SystemGasContractsEnum.y

    z = plx_enums.SystemGasContractsEnum.z


class SystemGasDemandsEnum(Enum):
    Demand = plx_enums.SystemGasDemandsEnum.Demand

    ShortagePrice = plx_enums.SystemGasDemandsEnum.ShortagePrice

    ExcessPrice = plx_enums.SystemGasDemandsEnum.ExcessPrice

    BidQuantity = plx_enums.SystemGasDemandsEnum.BidQuantity

    BidPrice = plx_enums.SystemGasDemandsEnum.BidPrice

    x = plx_enums.SystemGasDemandsEnum.x

    y = plx_enums.SystemGasDemandsEnum.y

    z = plx_enums.SystemGasDemandsEnum.z


class SystemGasFieldsEnum(Enum):
    BalancePeriod = plx_enums.SystemGasFieldsEnum.BalancePeriod

    InternalVolumeScalar = plx_enums.SystemGasFieldsEnum.InternalVolumeScalar

    EndEffectsMethod = plx_enums.SystemGasFieldsEnum.EndEffectsMethod

    RecyclePenalty = plx_enums.SystemGasFieldsEnum.RecyclePenalty

    DecompositionMethod = plx_enums.SystemGasFieldsEnum.DecompositionMethod

    DecompositionPenaltya = plx_enums.SystemGasFieldsEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.SystemGasFieldsEnum.DecompositionPenaltyb

    DecompositionPenaltyc = plx_enums.SystemGasFieldsEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.SystemGasFieldsEnum.DecompositionPenaltyx

    DecompositionBoundPenalty = plx_enums.SystemGasFieldsEnum.DecompositionBoundPenalty

    EnforceBounds = plx_enums.SystemGasFieldsEnum.EnforceBounds

    ExpansionOptimality = plx_enums.SystemGasFieldsEnum.ExpansionOptimality

    Units = plx_enums.SystemGasFieldsEnum.Units

    InitialVolume = plx_enums.SystemGasFieldsEnum.InitialVolume

    ProductionCost = plx_enums.SystemGasFieldsEnum.ProductionCost

    ProductionVolume = plx_enums.SystemGasFieldsEnum.ProductionVolume

    MaxRamp = plx_enums.SystemGasFieldsEnum.MaxRamp

    MaxProduction = plx_enums.SystemGasFieldsEnum.MaxProduction

    MinProduction = plx_enums.SystemGasFieldsEnum.MinProduction

    Target = plx_enums.SystemGasFieldsEnum.Target

    TargetPenalty = plx_enums.SystemGasFieldsEnum.TargetPenalty

    ExternalInjection = plx_enums.SystemGasFieldsEnum.ExternalInjection

    FOMCharge = plx_enums.SystemGasFieldsEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemGasFieldsEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemGasFieldsEnum.LeadTime

    ProjectStartDate = plx_enums.SystemGasFieldsEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemGasFieldsEnum.TechnicalLife

    BuildCost = plx_enums.SystemGasFieldsEnum.BuildCost

    WACC = plx_enums.SystemGasFieldsEnum.WACC

    EconomicLife = plx_enums.SystemGasFieldsEnum.EconomicLife

    MaxUnitsBuiltinYear = plx_enums.SystemGasFieldsEnum.MaxUnitsBuiltinYear

    x = plx_enums.SystemGasFieldsEnum.x

    y = plx_enums.SystemGasFieldsEnum.y

    z = plx_enums.SystemGasFieldsEnum.z


class SystemGasNodesEnum(Enum):
    ExpansionOptimality = plx_enums.SystemGasNodesEnum.ExpansionOptimality

    Units = plx_enums.SystemGasNodesEnum.Units

    FlowCharge = plx_enums.SystemGasNodesEnum.FlowCharge

    MaxFlow = plx_enums.SystemGasNodesEnum.MaxFlow

    GasSecurity = plx_enums.SystemGasNodesEnum.GasSecurity

    FOMCharge = plx_enums.SystemGasNodesEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemGasNodesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemGasNodesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemGasNodesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemGasNodesEnum.TechnicalLife

    BuildCost = plx_enums.SystemGasNodesEnum.BuildCost

    WACC = plx_enums.SystemGasNodesEnum.WACC

    EconomicLife = plx_enums.SystemGasNodesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemGasNodesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemGasNodesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemGasNodesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemGasNodesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemGasNodesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemGasNodesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemGasNodesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemGasNodesEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemGasNodesEnum.x

    y = plx_enums.SystemGasNodesEnum.y

    z = plx_enums.SystemGasNodesEnum.z


class SystemGasPipelinesEnum(Enum):
    RandomNumberSeed = plx_enums.SystemGasPipelinesEnum.RandomNumberSeed

    BalancePeriod = plx_enums.SystemGasPipelinesEnum.BalancePeriod

    InternalVolumeScalar = plx_enums.SystemGasPipelinesEnum.InternalVolumeScalar

    EndEffectsMethod = plx_enums.SystemGasPipelinesEnum.EndEffectsMethod

    RecyclePenalty = plx_enums.SystemGasPipelinesEnum.RecyclePenalty

    DecompositionMethod = plx_enums.SystemGasPipelinesEnum.DecompositionMethod

    DecompositionPenaltya = plx_enums.SystemGasPipelinesEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.SystemGasPipelinesEnum.DecompositionPenaltyb

    DecompositionPenaltyc = plx_enums.SystemGasPipelinesEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.SystemGasPipelinesEnum.DecompositionPenaltyx

    DecompositionBoundPenalty = plx_enums.SystemGasPipelinesEnum.DecompositionBoundPenalty

    EnforceBounds = plx_enums.SystemGasPipelinesEnum.EnforceBounds

    RepairTimeDistribution = plx_enums.SystemGasPipelinesEnum.RepairTimeDistribution

    ExpansionOptimality = plx_enums.SystemGasPipelinesEnum.ExpansionOptimality

    Units = plx_enums.SystemGasPipelinesEnum.Units

    MaxFlow = plx_enums.SystemGasPipelinesEnum.MaxFlow

    MaxFlowBack = plx_enums.SystemGasPipelinesEnum.MaxFlowBack

    Diameter = plx_enums.SystemGasPipelinesEnum.Diameter

    Roughness = plx_enums.SystemGasPipelinesEnum.Roughness

    Length = plx_enums.SystemGasPipelinesEnum.Length

    PumpEfficiency = plx_enums.SystemGasPipelinesEnum.PumpEfficiency

    FlowCharge = plx_enums.SystemGasPipelinesEnum.FlowCharge

    FlowChargeBack = plx_enums.SystemGasPipelinesEnum.FlowChargeBack

    InitialVolume = plx_enums.SystemGasPipelinesEnum.InitialVolume

    MaxVolume = plx_enums.SystemGasPipelinesEnum.MaxVolume

    MinVolume = plx_enums.SystemGasPipelinesEnum.MinVolume

    VolumeImbalance = plx_enums.SystemGasPipelinesEnum.VolumeImbalance

    ImbalanceCharge = plx_enums.SystemGasPipelinesEnum.ImbalanceCharge

    FOMCharge = plx_enums.SystemGasPipelinesEnum.FOMCharge

    ConsumptionAllocation = plx_enums.SystemGasPipelinesEnum.ConsumptionAllocation

    UnitsOut = plx_enums.SystemGasPipelinesEnum.UnitsOut

    MaintenanceRate = plx_enums.SystemGasPipelinesEnum.MaintenanceRate

    MaintenanceFrequency = plx_enums.SystemGasPipelinesEnum.MaintenanceFrequency

    ForcedOutageRate = plx_enums.SystemGasPipelinesEnum.ForcedOutageRate

    OutageMaxFlow = plx_enums.SystemGasPipelinesEnum.OutageMaxFlow

    OutageMaxFlowBack = plx_enums.SystemGasPipelinesEnum.OutageMaxFlowBack

    MeanTimetoRepair = plx_enums.SystemGasPipelinesEnum.MeanTimetoRepair

    MinTimeToRepair = plx_enums.SystemGasPipelinesEnum.MinTimeToRepair

    MaxTimeToRepair = plx_enums.SystemGasPipelinesEnum.MaxTimeToRepair

    RepairTimeShape = plx_enums.SystemGasPipelinesEnum.RepairTimeShape

    RepairTimeScale = plx_enums.SystemGasPipelinesEnum.RepairTimeScale

    MaxUnitsBuilt = plx_enums.SystemGasPipelinesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemGasPipelinesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemGasPipelinesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemGasPipelinesEnum.TechnicalLife

    BuildCost = plx_enums.SystemGasPipelinesEnum.BuildCost

    WACC = plx_enums.SystemGasPipelinesEnum.WACC

    EconomicLife = plx_enums.SystemGasPipelinesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemGasPipelinesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemGasPipelinesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemGasPipelinesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemGasPipelinesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemGasPipelinesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemGasPipelinesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemGasPipelinesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemGasPipelinesEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemGasPipelinesEnum.x

    y = plx_enums.SystemGasPipelinesEnum.y

    z = plx_enums.SystemGasPipelinesEnum.z


class SystemGasPlantsEnum(Enum):
    ExpansionOptimality = plx_enums.SystemGasPlantsEnum.ExpansionOptimality

    Units = plx_enums.SystemGasPlantsEnum.Units

    MaxProduction = plx_enums.SystemGasPlantsEnum.MaxProduction

    MinProduction = plx_enums.SystemGasPlantsEnum.MinProduction

    ProcessingRate = plx_enums.SystemGasPlantsEnum.ProcessingRate

    ProcessingCharge = plx_enums.SystemGasPlantsEnum.ProcessingCharge

    Consumption = plx_enums.SystemGasPlantsEnum.Consumption

    EnergyUsage = plx_enums.SystemGasPlantsEnum.EnergyUsage

    VOMCharge = plx_enums.SystemGasPlantsEnum.VOMCharge

    FOMCharge = plx_enums.SystemGasPlantsEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemGasPlantsEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemGasPlantsEnum.LeadTime

    ProjectStartDate = plx_enums.SystemGasPlantsEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemGasPlantsEnum.TechnicalLife

    BuildCost = plx_enums.SystemGasPlantsEnum.BuildCost

    WACC = plx_enums.SystemGasPlantsEnum.WACC

    EconomicLife = plx_enums.SystemGasPlantsEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemGasPlantsEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemGasPlantsEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemGasPlantsEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemGasPlantsEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemGasPlantsEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemGasPlantsEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemGasPlantsEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemGasPlantsEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemGasPlantsEnum.x

    y = plx_enums.SystemGasPlantsEnum.y

    z = plx_enums.SystemGasPlantsEnum.z


class SystemGasStoragesEnum(Enum):
    BalancePeriod = plx_enums.SystemGasStoragesEnum.BalancePeriod

    InternalVolumeScalar = plx_enums.SystemGasStoragesEnum.InternalVolumeScalar

    EndEffectsMethod = plx_enums.SystemGasStoragesEnum.EndEffectsMethod

    RecyclePenalty = plx_enums.SystemGasStoragesEnum.RecyclePenalty

    DecompositionMethod = plx_enums.SystemGasStoragesEnum.DecompositionMethod

    DecompositionPenaltya = plx_enums.SystemGasStoragesEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.SystemGasStoragesEnum.DecompositionPenaltyb

    DecompositionPenaltyc = plx_enums.SystemGasStoragesEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.SystemGasStoragesEnum.DecompositionPenaltyx

    DecompositionBoundPenalty = plx_enums.SystemGasStoragesEnum.DecompositionBoundPenalty

    EnforceBounds = plx_enums.SystemGasStoragesEnum.EnforceBounds

    ExpansionOptimality = plx_enums.SystemGasStoragesEnum.ExpansionOptimality

    Units = plx_enums.SystemGasStoragesEnum.Units

    MaxVolume = plx_enums.SystemGasStoragesEnum.MaxVolume

    MinVolume = plx_enums.SystemGasStoragesEnum.MinVolume

    InitialVolume = plx_enums.SystemGasStoragesEnum.InitialVolume

    WithdrawalCharge = plx_enums.SystemGasStoragesEnum.WithdrawalCharge

    InjectionCharge = plx_enums.SystemGasStoragesEnum.InjectionCharge

    InjectionRatchet = plx_enums.SystemGasStoragesEnum.InjectionRatchet

    WithdrawalRatchet = plx_enums.SystemGasStoragesEnum.WithdrawalRatchet

    MaxWithdrawal = plx_enums.SystemGasStoragesEnum.MaxWithdrawal

    MaxInjection = plx_enums.SystemGasStoragesEnum.MaxInjection

    MinWithdrawal = plx_enums.SystemGasStoragesEnum.MinWithdrawal

    MinInjection = plx_enums.SystemGasStoragesEnum.MinInjection

    MaxRamp = plx_enums.SystemGasStoragesEnum.MaxRamp

    Target = plx_enums.SystemGasStoragesEnum.Target

    TargetPenalty = plx_enums.SystemGasStoragesEnum.TargetPenalty

    EnergyUsage = plx_enums.SystemGasStoragesEnum.EnergyUsage

    LossRate = plx_enums.SystemGasStoragesEnum.LossRate

    WithdrawalRateScalar = plx_enums.SystemGasStoragesEnum.WithdrawalRateScalar

    WithdrawalVolume = plx_enums.SystemGasStoragesEnum.WithdrawalVolume

    InjectionRateScalar = plx_enums.SystemGasStoragesEnum.InjectionRateScalar

    InjectionVolume = plx_enums.SystemGasStoragesEnum.InjectionVolume

    ExternalInjection = plx_enums.SystemGasStoragesEnum.ExternalInjection

    FOMCharge = plx_enums.SystemGasStoragesEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemGasStoragesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemGasStoragesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemGasStoragesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemGasStoragesEnum.TechnicalLife

    BuildCost = plx_enums.SystemGasStoragesEnum.BuildCost

    WACC = plx_enums.SystemGasStoragesEnum.WACC

    EconomicLife = plx_enums.SystemGasStoragesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemGasStoragesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemGasStoragesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemGasStoragesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemGasStoragesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemGasStoragesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemGasStoragesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemGasStoragesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemGasStoragesEnum.MinUnitsRetiredinYear

    TrajectoryNonanticipativity = plx_enums.SystemGasStoragesEnum.TrajectoryNonanticipativity

    TrajectoryNonanticipativityVolume = plx_enums.SystemGasStoragesEnum.TrajectoryNonanticipativityVolume

    TrajectoryNonanticipativityTime = plx_enums.SystemGasStoragesEnum.TrajectoryNonanticipativityTime

    x = plx_enums.SystemGasStoragesEnum.x

    y = plx_enums.SystemGasStoragesEnum.y

    z = plx_enums.SystemGasStoragesEnum.z


class SystemGasTransportsEnum(Enum):
    VoyageTime = plx_enums.SystemGasTransportsEnum.VoyageTime

    LoadingTime = plx_enums.SystemGasTransportsEnum.LoadingTime

    DischargeTime = plx_enums.SystemGasTransportsEnum.DischargeTime

    MinVolume = plx_enums.SystemGasTransportsEnum.MinVolume

    MaxVolume = plx_enums.SystemGasTransportsEnum.MaxVolume

    ShippingCharge = plx_enums.SystemGasTransportsEnum.ShippingCharge

    BoiloffRate = plx_enums.SystemGasTransportsEnum.BoiloffRate

    Imports = plx_enums.SystemGasTransportsEnum.Imports

    Exports = plx_enums.SystemGasTransportsEnum.Exports

    MaxShipments = plx_enums.SystemGasTransportsEnum.MaxShipments

    x = plx_enums.SystemGasTransportsEnum.x

    y = plx_enums.SystemGasTransportsEnum.y

    z = plx_enums.SystemGasTransportsEnum.z


class SystemGasZonesEnum(Enum):
    x = plx_enums.SystemGasZonesEnum.x

    y = plx_enums.SystemGasZonesEnum.y

    z = plx_enums.SystemGasZonesEnum.z


class SystemGeneratorsEnum(Enum):
    MustReport = plx_enums.SystemGeneratorsEnum.MustReport

    RandomNumberSeed = plx_enums.SystemGeneratorsEnum.RandomNumberSeed

    DispatchPeriod = plx_enums.SystemGeneratorsEnum.DispatchPeriod

    MaxHeatRateTranches = plx_enums.SystemGeneratorsEnum.MaxHeatRateTranches

    FormulateNonconvex = plx_enums.SystemGeneratorsEnum.FormulateNonconvex

    HeadEffectsMethod = plx_enums.SystemGeneratorsEnum.HeadEffectsMethod

    MinDownTimeMode = plx_enums.SystemGeneratorsEnum.MinDownTimeMode

    ForcedOutageRateDenominator = plx_enums.SystemGeneratorsEnum.ForcedOutageRateDenominator

    RepairTimeDistribution = plx_enums.SystemGeneratorsEnum.RepairTimeDistribution

    FixedLoadMethod = plx_enums.SystemGeneratorsEnum.FixedLoadMethod

    PriceSetting = plx_enums.SystemGeneratorsEnum.PriceSetting

    OfferQuantityFormat = plx_enums.SystemGeneratorsEnum.OfferQuantityFormat

    OffersMustClearinOrder = plx_enums.SystemGeneratorsEnum.OffersMustClearinOrder

    UnitCommitmentOptimality = plx_enums.SystemGeneratorsEnum.UnitCommitmentOptimality

    RoundingUpThreshold = plx_enums.SystemGeneratorsEnum.RoundingUpThreshold

    IncludeinRoundedRelaxationMeritOrder = plx_enums.SystemGeneratorsEnum.IncludeinRoundedRelaxationMeritOrder

    StartProfileRange = plx_enums.SystemGeneratorsEnum.StartProfileRange

    ExpansionOptimality = plx_enums.SystemGeneratorsEnum.ExpansionOptimality

    DecliningDepreciationBalance = plx_enums.SystemGeneratorsEnum.DecliningDepreciationBalance

    EnergyLimitDecompositionMethod = plx_enums.SystemGeneratorsEnum.EnergyLimitDecompositionMethod

    IncludeinUplift = plx_enums.SystemGeneratorsEnum.IncludeinUplift

    IncludeinCapacityPayments = plx_enums.SystemGeneratorsEnum.IncludeinCapacityPayments

    BalancePeriod = plx_enums.SystemGeneratorsEnum.BalancePeriod

    InternalVolumeScalar = plx_enums.SystemGeneratorsEnum.InternalVolumeScalar

    EndEffectsMethod = plx_enums.SystemGeneratorsEnum.EndEffectsMethod

    RecyclePenalty = plx_enums.SystemGeneratorsEnum.RecyclePenalty

    DecompositionMethod = plx_enums.SystemGeneratorsEnum.DecompositionMethod

    DecompositionPenaltya = plx_enums.SystemGeneratorsEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.SystemGeneratorsEnum.DecompositionPenaltyb

    DecompositionPenaltyc = plx_enums.SystemGeneratorsEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.SystemGeneratorsEnum.DecompositionPenaltyx

    DecompositionBoundPenalty = plx_enums.SystemGeneratorsEnum.DecompositionBoundPenalty

    EnforceBounds = plx_enums.SystemGeneratorsEnum.EnforceBounds

    IsStrategic = plx_enums.SystemGeneratorsEnum.IsStrategic

    TransitionType = plx_enums.SystemGeneratorsEnum.TransitionType

    Units = plx_enums.SystemGeneratorsEnum.Units

    MaxCapacity = plx_enums.SystemGeneratorsEnum.MaxCapacity

    MinStableLevel = plx_enums.SystemGeneratorsEnum.MinStableLevel

    MinStableFactor = plx_enums.SystemGeneratorsEnum.MinStableFactor

    FuelPrice = plx_enums.SystemGeneratorsEnum.FuelPrice

    LoadPoint = plx_enums.SystemGeneratorsEnum.LoadPoint

    HeatRate = plx_enums.SystemGeneratorsEnum.HeatRate

    HeatRateBase = plx_enums.SystemGeneratorsEnum.HeatRateBase

    HeatRateIncr = plx_enums.SystemGeneratorsEnum.HeatRateIncr

    HeatRateIncr2 = plx_enums.SystemGeneratorsEnum.HeatRateIncr2

    HeatRateIncr3 = plx_enums.SystemGeneratorsEnum.HeatRateIncr3

    VOMCharge = plx_enums.SystemGeneratorsEnum.VOMCharge

    UoSCharge = plx_enums.SystemGeneratorsEnum.UoSCharge

    RunningCost = plx_enums.SystemGeneratorsEnum.RunningCost

    StartCost = plx_enums.SystemGeneratorsEnum.StartCost

    StartCostTime = plx_enums.SystemGeneratorsEnum.StartCostTime

    RunUpRate = plx_enums.SystemGeneratorsEnum.RunUpRate

    StartProfile = plx_enums.SystemGeneratorsEnum.StartProfile

    StartPenalty = plx_enums.SystemGeneratorsEnum.StartPenalty

    ShutdownCost = plx_enums.SystemGeneratorsEnum.ShutdownCost

    RunDownRate = plx_enums.SystemGeneratorsEnum.RunDownRate

    ShutdownProfile = plx_enums.SystemGeneratorsEnum.ShutdownProfile

    ShutdownPenalty = plx_enums.SystemGeneratorsEnum.ShutdownPenalty

    Rating = plx_enums.SystemGeneratorsEnum.Rating

    RatingFactor = plx_enums.SystemGeneratorsEnum.RatingFactor

    MinUpTime = plx_enums.SystemGeneratorsEnum.MinUpTime

    MinDownTime = plx_enums.SystemGeneratorsEnum.MinDownTime

    MaxUpTime = plx_enums.SystemGeneratorsEnum.MaxUpTime

    MaxDownTime = plx_enums.SystemGeneratorsEnum.MaxDownTime

    MustRunUnits = plx_enums.SystemGeneratorsEnum.MustRunUnits

    FixedLoad = plx_enums.SystemGeneratorsEnum.FixedLoad

    FixedLoadPenalty = plx_enums.SystemGeneratorsEnum.FixedLoadPenalty

    MinLoad = plx_enums.SystemGeneratorsEnum.MinLoad

    MinLoadPenalty = plx_enums.SystemGeneratorsEnum.MinLoadPenalty

    MaxLoad = plx_enums.SystemGeneratorsEnum.MaxLoad

    Commit = plx_enums.SystemGeneratorsEnum.Commit

    FuelMixPenalty = plx_enums.SystemGeneratorsEnum.FuelMixPenalty

    RampUpCharge = plx_enums.SystemGeneratorsEnum.RampUpCharge

    RampDownCharge = plx_enums.SystemGeneratorsEnum.RampDownCharge

    MaxRampUp = plx_enums.SystemGeneratorsEnum.MaxRampUp

    MaxRampUpPenalty = plx_enums.SystemGeneratorsEnum.MaxRampUpPenalty

    MaxRampDown = plx_enums.SystemGeneratorsEnum.MaxRampDown

    MaxRampDownPenalty = plx_enums.SystemGeneratorsEnum.MaxRampDownPenalty

    RoughRunningPoint = plx_enums.SystemGeneratorsEnum.RoughRunningPoint

    RoughRunningRange = plx_enums.SystemGeneratorsEnum.RoughRunningRange

    RegulationPoint = plx_enums.SystemGeneratorsEnum.RegulationPoint

    RegulationRange = plx_enums.SystemGeneratorsEnum.RegulationRange

    AuxFixed = plx_enums.SystemGeneratorsEnum.AuxFixed

    AuxBase = plx_enums.SystemGeneratorsEnum.AuxBase

    AuxIncr = plx_enums.SystemGeneratorsEnum.AuxIncr

    MarginalLossFactor = plx_enums.SystemGeneratorsEnum.MarginalLossFactor

    EfficiencyBase = plx_enums.SystemGeneratorsEnum.EfficiencyBase

    EfficiencyIncr = plx_enums.SystemGeneratorsEnum.EfficiencyIncr

    PumpEfficiency = plx_enums.SystemGeneratorsEnum.PumpEfficiency

    PumpLoad = plx_enums.SystemGeneratorsEnum.PumpLoad

    PumpUnits = plx_enums.SystemGeneratorsEnum.PumpUnits

    MinPumpLoad = plx_enums.SystemGeneratorsEnum.MinPumpLoad

    MustPumpUnits = plx_enums.SystemGeneratorsEnum.MustPumpUnits

    MaxUnitsPumping = plx_enums.SystemGeneratorsEnum.MaxUnitsPumping

    FixedPumpLoad = plx_enums.SystemGeneratorsEnum.FixedPumpLoad

    FixedPumpLoadPenalty = plx_enums.SystemGeneratorsEnum.FixedPumpLoadPenalty

    PumpUoSCharge = plx_enums.SystemGeneratorsEnum.PumpUoSCharge

    MinPumpTime = plx_enums.SystemGeneratorsEnum.MinPumpTime

    MinPumpDownTime = plx_enums.SystemGeneratorsEnum.MinPumpDownTime

    ReservesVOMCharge = plx_enums.SystemGeneratorsEnum.ReservesVOMCharge

    SyncCondUnits = plx_enums.SystemGeneratorsEnum.SyncCondUnits

    MustrunSyncCondUnits = plx_enums.SystemGeneratorsEnum.MustrunSyncCondUnits

    SyncCondLoad = plx_enums.SystemGeneratorsEnum.SyncCondLoad

    SyncCondVOMCharge = plx_enums.SystemGeneratorsEnum.SyncCondVOMCharge

    ReserveShare = plx_enums.SystemGeneratorsEnum.ReserveShare

    InitialGeneration = plx_enums.SystemGeneratorsEnum.InitialGeneration

    InitialUnitsGenerating = plx_enums.SystemGeneratorsEnum.InitialUnitsGenerating

    InitialHoursUp = plx_enums.SystemGeneratorsEnum.InitialHoursUp

    InitialHoursDown = plx_enums.SystemGeneratorsEnum.InitialHoursDown

    InitialPumping = plx_enums.SystemGeneratorsEnum.InitialPumping

    InitialUnitsPumping = plx_enums.SystemGeneratorsEnum.InitialUnitsPumping

    InitialHoursPumping = plx_enums.SystemGeneratorsEnum.InitialHoursPumping

    GeneratortoPumpSwitchTime = plx_enums.SystemGeneratorsEnum.GeneratortoPumpSwitchTime

    PumptoGeneratorSwitchTime = plx_enums.SystemGeneratorsEnum.PumptoGeneratorSwitchTime

    EfficiencyDegradation = plx_enums.SystemGeneratorsEnum.EfficiencyDegradation

    LastStartState = plx_enums.SystemGeneratorsEnum.LastStartState

    ReferenceGeneration = plx_enums.SystemGeneratorsEnum.ReferenceGeneration

    LoadSubtracter = plx_enums.SystemGeneratorsEnum.LoadSubtracter

    PriceFollowing = plx_enums.SystemGeneratorsEnum.PriceFollowing

    LoadFollowingProfile = plx_enums.SystemGeneratorsEnum.LoadFollowingProfile

    LoadFollowingFactor = plx_enums.SystemGeneratorsEnum.LoadFollowingFactor

    BoilerEfficiency = plx_enums.SystemGeneratorsEnum.BoilerEfficiency

    HeatLoad = plx_enums.SystemGeneratorsEnum.HeatLoad

    PowertoHeatRatio = plx_enums.SystemGeneratorsEnum.PowertoHeatRatio

    CHPElectricHeatRateIncr = plx_enums.SystemGeneratorsEnum.CHPElectricHeatRateIncr

    CHPHeatSurrogateRateIncr = plx_enums.SystemGeneratorsEnum.CHPHeatSurrogateRateIncr

    BoilerHeatRateIncr = plx_enums.SystemGeneratorsEnum.BoilerHeatRateIncr

    MaxBoilerHeat = plx_enums.SystemGeneratorsEnum.MaxBoilerHeat

    MaxHeat = plx_enums.SystemGeneratorsEnum.MaxHeat

    MinHeat = plx_enums.SystemGeneratorsEnum.MinHeat

    OpeningHeat = plx_enums.SystemGeneratorsEnum.OpeningHeat

    HeatWithdrawalCharge = plx_enums.SystemGeneratorsEnum.HeatWithdrawalCharge

    HeatInjectionCharge = plx_enums.SystemGeneratorsEnum.HeatInjectionCharge

    FixedCharge = plx_enums.SystemGeneratorsEnum.FixedCharge

    HeatLoss = plx_enums.SystemGeneratorsEnum.HeatLoss

    WaterOfftake = plx_enums.SystemGeneratorsEnum.WaterOfftake

    WaterConsumption = plx_enums.SystemGeneratorsEnum.WaterConsumption

    MaxRelease = plx_enums.SystemGeneratorsEnum.MaxRelease

    MaxEnergy = plx_enums.SystemGeneratorsEnum.MaxEnergy

    MinEnergy = plx_enums.SystemGeneratorsEnum.MinEnergy

    MaxCapacityFactor = plx_enums.SystemGeneratorsEnum.MaxCapacityFactor

    MinCapacityFactor = plx_enums.SystemGeneratorsEnum.MinCapacityFactor

    MaxEnergyPenalty = plx_enums.SystemGeneratorsEnum.MaxEnergyPenalty

    MinEnergyPenalty = plx_enums.SystemGeneratorsEnum.MinEnergyPenalty

    MaxStarts = plx_enums.SystemGeneratorsEnum.MaxStarts

    MaxStartsPenalty = plx_enums.SystemGeneratorsEnum.MaxStartsPenalty

    EnergyScalar = plx_enums.SystemGeneratorsEnum.EnergyScalar

    MaxHeatWithdrawal = plx_enums.SystemGeneratorsEnum.MaxHeatWithdrawal

    MaxHeatInjection = plx_enums.SystemGeneratorsEnum.MaxHeatInjection

    MinHeatWithdrawal = plx_enums.SystemGeneratorsEnum.MinHeatWithdrawal

    MinHeatInjection = plx_enums.SystemGeneratorsEnum.MinHeatInjection

    OfferBase = plx_enums.SystemGeneratorsEnum.OfferBase

    OfferNoLoadCost = plx_enums.SystemGeneratorsEnum.OfferNoLoadCost

    OfferQuantity = plx_enums.SystemGeneratorsEnum.OfferQuantity

    OfferPrice = plx_enums.SystemGeneratorsEnum.OfferPrice

    OfferQuantityScalar = plx_enums.SystemGeneratorsEnum.OfferQuantityScalar

    OfferPriceIncr = plx_enums.SystemGeneratorsEnum.OfferPriceIncr

    OfferPriceScalar = plx_enums.SystemGeneratorsEnum.OfferPriceScalar

    Markup = plx_enums.SystemGeneratorsEnum.Markup

    BidCostMarkup = plx_enums.SystemGeneratorsEnum.BidCostMarkup

    MarkupPoint = plx_enums.SystemGeneratorsEnum.MarkupPoint

    PumpBidBase = plx_enums.SystemGeneratorsEnum.PumpBidBase

    PumpBidQuantity = plx_enums.SystemGeneratorsEnum.PumpBidQuantity

    PumpBidPrice = plx_enums.SystemGeneratorsEnum.PumpBidPrice

    PumpBidQuantityScalar = plx_enums.SystemGeneratorsEnum.PumpBidQuantityScalar

    PumpBidPriceIncr = plx_enums.SystemGeneratorsEnum.PumpBidPriceIncr

    PumpBidPriceScalar = plx_enums.SystemGeneratorsEnum.PumpBidPriceScalar

    StrategicRating = plx_enums.SystemGeneratorsEnum.StrategicRating

    StrategicReferencePrice = plx_enums.SystemGeneratorsEnum.StrategicReferencePrice

    InitialAge = plx_enums.SystemGeneratorsEnum.InitialAge

    PowerDegradation = plx_enums.SystemGeneratorsEnum.PowerDegradation

    CapacityDegradation = plx_enums.SystemGeneratorsEnum.CapacityDegradation

    FOMCharge = plx_enums.SystemGeneratorsEnum.FOMCharge

    EquityCharge = plx_enums.SystemGeneratorsEnum.EquityCharge

    DebtCharge = plx_enums.SystemGeneratorsEnum.DebtCharge

    FirmCapacity = plx_enums.SystemGeneratorsEnum.FirmCapacity

    UnitsOut = plx_enums.SystemGeneratorsEnum.UnitsOut

    Maintenance = plx_enums.SystemGeneratorsEnum.Maintenance

    ForcedOutage = plx_enums.SystemGeneratorsEnum.ForcedOutage

    MaintenanceRate = plx_enums.SystemGeneratorsEnum.MaintenanceRate

    MaintenanceFrequency = plx_enums.SystemGeneratorsEnum.MaintenanceFrequency

    ForcedOutageRate = plx_enums.SystemGeneratorsEnum.ForcedOutageRate

    OutageFactor = plx_enums.SystemGeneratorsEnum.OutageFactor

    OutageRating = plx_enums.SystemGeneratorsEnum.OutageRating

    OutagePumpLoad = plx_enums.SystemGeneratorsEnum.OutagePumpLoad

    InitialOperatingHours = plx_enums.SystemGeneratorsEnum.InitialOperatingHours

    MeanTimetoRepair = plx_enums.SystemGeneratorsEnum.MeanTimetoRepair

    MinTimeToRepair = plx_enums.SystemGeneratorsEnum.MinTimeToRepair

    MaxTimeToRepair = plx_enums.SystemGeneratorsEnum.MaxTimeToRepair

    RepairTimeShape = plx_enums.SystemGeneratorsEnum.RepairTimeShape

    RepairTimeScale = plx_enums.SystemGeneratorsEnum.RepairTimeScale

    BuildCost = plx_enums.SystemGeneratorsEnum.BuildCost

    RetirementCost = plx_enums.SystemGeneratorsEnum.RetirementCost

    OnetimeCost = plx_enums.SystemGeneratorsEnum.OnetimeCost

    LeadTime = plx_enums.SystemGeneratorsEnum.LeadTime

    ProjectStartDate = plx_enums.SystemGeneratorsEnum.ProjectStartDate

    CommissionDate = plx_enums.SystemGeneratorsEnum.CommissionDate

    TechnicalLife = plx_enums.SystemGeneratorsEnum.TechnicalLife

    WACC = plx_enums.SystemGeneratorsEnum.WACC

    EconomicLife = plx_enums.SystemGeneratorsEnum.EconomicLife

    MaxUnitsBuilt = plx_enums.SystemGeneratorsEnum.MaxUnitsBuilt

    MaxUnitsRetired = plx_enums.SystemGeneratorsEnum.MaxUnitsRetired

    MinUnitsBuilt = plx_enums.SystemGeneratorsEnum.MinUnitsBuilt

    MinUnitsRetired = plx_enums.SystemGeneratorsEnum.MinUnitsRetired

    MaxUnitsBuiltinYear = plx_enums.SystemGeneratorsEnum.MaxUnitsBuiltinYear

    MaxUnitsRetiredinYear = plx_enums.SystemGeneratorsEnum.MaxUnitsRetiredinYear

    MinUnitsBuiltinYear = plx_enums.SystemGeneratorsEnum.MinUnitsBuiltinYear

    MinUnitsRetiredinYear = plx_enums.SystemGeneratorsEnum.MinUnitsRetiredinYear

    BuildSetSize = plx_enums.SystemGeneratorsEnum.BuildSetSize

    CapacityPrice = plx_enums.SystemGeneratorsEnum.CapacityPrice

    UnitCommitmentNonanticipativity = plx_enums.SystemGeneratorsEnum.UnitCommitmentNonanticipativity

    UnitCommitmentNonanticipativityTime = plx_enums.SystemGeneratorsEnum.UnitCommitmentNonanticipativityTime

    PumpUnitCommitmentNonanticipativity = plx_enums.SystemGeneratorsEnum.PumpUnitCommitmentNonanticipativity

    PumpUnitCommitmentNonanticipativityTime = plx_enums.SystemGeneratorsEnum.PumpUnitCommitmentNonanticipativityTime

    GenerationNonanticipativity = plx_enums.SystemGeneratorsEnum.GenerationNonanticipativity

    GenerationNonanticipativityTime = plx_enums.SystemGeneratorsEnum.GenerationNonanticipativityTime

    PumpLoadNonanticipativity = plx_enums.SystemGeneratorsEnum.PumpLoadNonanticipativity

    PumpLoadNonanticipativityTime = plx_enums.SystemGeneratorsEnum.PumpLoadNonanticipativityTime

    BuildNonanticipativity = plx_enums.SystemGeneratorsEnum.BuildNonanticipativity

    RetireNonanticipativity = plx_enums.SystemGeneratorsEnum.RetireNonanticipativity

    x = plx_enums.SystemGeneratorsEnum.x

    y = plx_enums.SystemGeneratorsEnum.y

    z = plx_enums.SystemGeneratorsEnum.z


class SystemGlobalsEnum(Enum):
    FCFConstant = plx_enums.SystemGlobalsEnum.FCFConstant

    SampleWeight = plx_enums.SystemGlobalsEnum.SampleWeight

    TreeStageCount = plx_enums.SystemGlobalsEnum.TreeStageCount

    TreePeriodType = plx_enums.SystemGlobalsEnum.TreePeriodType

    TreePositionExpFactor = plx_enums.SystemGlobalsEnum.TreePositionExpFactor

    TreeLeavesExpFactor = plx_enums.SystemGlobalsEnum.TreeLeavesExpFactor

    TreeStagesPosition = plx_enums.SystemGlobalsEnum.TreeStagesPosition

    TreeStagesLeaves = plx_enums.SystemGlobalsEnum.TreeStagesLeaves

    TreeStagesHangingBranches = plx_enums.SystemGlobalsEnum.TreeStagesHangingBranches

    DeterministicStages = plx_enums.SystemGlobalsEnum.DeterministicStages

    HangingBranchesHistoricalYearStart = plx_enums.SystemGlobalsEnum.HangingBranchesHistoricalYearStart

    HangingBranchesWeight = plx_enums.SystemGlobalsEnum.HangingBranchesWeight

    HangingBranchesBlockCount = plx_enums.SystemGlobalsEnum.HangingBranchesBlockCount

    SlicingBlock = plx_enums.SystemGlobalsEnum.SlicingBlock


class SystemHeatNodesEnum(Enum):
    AllowDumpHeat = plx_enums.SystemHeatNodesEnum.AllowDumpHeat

    Units = plx_enums.SystemHeatNodesEnum.Units

    HeatDemand = plx_enums.SystemHeatNodesEnum.HeatDemand

    x = plx_enums.SystemHeatNodesEnum.x

    y = plx_enums.SystemHeatNodesEnum.y

    z = plx_enums.SystemHeatNodesEnum.z


class SystemHeatPlantsEnum(Enum):
    UnitCommitmentOptimality = plx_enums.SystemHeatPlantsEnum.UnitCommitmentOptimality

    Units = plx_enums.SystemHeatPlantsEnum.Units

    MaxCapacity = plx_enums.SystemHeatPlantsEnum.MaxCapacity

    EfficiencyBase = plx_enums.SystemHeatPlantsEnum.EfficiencyBase

    EfficiencyIncr = plx_enums.SystemHeatPlantsEnum.EfficiencyIncr

    VOMCharge = plx_enums.SystemHeatPlantsEnum.VOMCharge

    LoadPoint = plx_enums.SystemHeatPlantsEnum.LoadPoint

    HeatRate = plx_enums.SystemHeatPlantsEnum.HeatRate

    HeatRateBase = plx_enums.SystemHeatPlantsEnum.HeatRateBase

    HeatRateIncr = plx_enums.SystemHeatPlantsEnum.HeatRateIncr

    StartCost = plx_enums.SystemHeatPlantsEnum.StartCost

    StartCostTime = plx_enums.SystemHeatPlantsEnum.StartCostTime

    RunUpRate = plx_enums.SystemHeatPlantsEnum.RunUpRate

    StartProfile = plx_enums.SystemHeatPlantsEnum.StartProfile

    MinUpTime = plx_enums.SystemHeatPlantsEnum.MinUpTime

    MinDownTime = plx_enums.SystemHeatPlantsEnum.MinDownTime

    MaxUpTime = plx_enums.SystemHeatPlantsEnum.MaxUpTime

    MaxDownTime = plx_enums.SystemHeatPlantsEnum.MaxDownTime

    MaxRampUp = plx_enums.SystemHeatPlantsEnum.MaxRampUp

    MaxRampDown = plx_enums.SystemHeatPlantsEnum.MaxRampDown

    MinStableLevel = plx_enums.SystemHeatPlantsEnum.MinStableLevel

    FOMCharge = plx_enums.SystemHeatPlantsEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemHeatPlantsEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemHeatPlantsEnum.LeadTime

    ProjectStartDate = plx_enums.SystemHeatPlantsEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemHeatPlantsEnum.TechnicalLife

    BuildCost = plx_enums.SystemHeatPlantsEnum.BuildCost

    WACC = plx_enums.SystemHeatPlantsEnum.WACC

    EconomicLife = plx_enums.SystemHeatPlantsEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemHeatPlantsEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemHeatPlantsEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemHeatPlantsEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemHeatPlantsEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemHeatPlantsEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemHeatPlantsEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemHeatPlantsEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemHeatPlantsEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemHeatPlantsEnum.x

    y = plx_enums.SystemHeatPlantsEnum.y

    z = plx_enums.SystemHeatPlantsEnum.z


class SystemHubsEnum(Enum):
    PricingMethod = plx_enums.SystemHubsEnum.PricingMethod

    Units = plx_enums.SystemHubsEnum.Units

    x = plx_enums.SystemHubsEnum.x

    y = plx_enums.SystemHubsEnum.y

    z = plx_enums.SystemHubsEnum.z


class SystemInterfacesEnum(Enum):
    FormulateUpfront = plx_enums.SystemInterfacesEnum.FormulateUpfront

    OfferQuantityFormat = plx_enums.SystemInterfacesEnum.OfferQuantityFormat

    Units = plx_enums.SystemInterfacesEnum.Units

    MinFlow = plx_enums.SystemInterfacesEnum.MinFlow

    MaxFlow = plx_enums.SystemInterfacesEnum.MaxFlow

    OverloadMaxRating = plx_enums.SystemInterfacesEnum.OverloadMaxRating

    OverloadMinRating = plx_enums.SystemInterfacesEnum.OverloadMinRating

    LimitPenalty = plx_enums.SystemInterfacesEnum.LimitPenalty

    MaxRampUp = plx_enums.SystemInterfacesEnum.MaxRampUp

    MaxRampDown = plx_enums.SystemInterfacesEnum.MaxRampDown

    RampPenalty = plx_enums.SystemInterfacesEnum.RampPenalty

    FixedFlow = plx_enums.SystemInterfacesEnum.FixedFlow

    FixedFlowPenalty = plx_enums.SystemInterfacesEnum.FixedFlowPenalty

    OfferBase = plx_enums.SystemInterfacesEnum.OfferBase

    OfferQuantity = plx_enums.SystemInterfacesEnum.OfferQuantity

    OfferPrice = plx_enums.SystemInterfacesEnum.OfferPrice

    OfferQuantityBack = plx_enums.SystemInterfacesEnum.OfferQuantityBack

    OfferPriceBack = plx_enums.SystemInterfacesEnum.OfferPriceBack

    FlowNonanticipativity = plx_enums.SystemInterfacesEnum.FlowNonanticipativity

    FlowNonanticipativityTime = plx_enums.SystemInterfacesEnum.FlowNonanticipativityTime

    FirmCapacity = plx_enums.SystemInterfacesEnum.FirmCapacity

    ExpansionCost = plx_enums.SystemInterfacesEnum.ExpansionCost

    MaxExpansion = plx_enums.SystemInterfacesEnum.MaxExpansion

    WACC = plx_enums.SystemInterfacesEnum.WACC

    EconomicLife = plx_enums.SystemInterfacesEnum.EconomicLife

    BuildNonanticipativity = plx_enums.SystemInterfacesEnum.BuildNonanticipativity

    x = plx_enums.SystemInterfacesEnum.x

    y = plx_enums.SystemInterfacesEnum.y

    z = plx_enums.SystemInterfacesEnum.z


class SystemLinesEnum(Enum):
    MustReport = plx_enums.SystemLinesEnum.MustReport

    RandomNumberSeed = plx_enums.SystemLinesEnum.RandomNumberSeed

    RepairTimeDistribution = plx_enums.SystemLinesEnum.RepairTimeDistribution

    EnforceLimits = plx_enums.SystemLinesEnum.EnforceLimits

    FormulateUpfront = plx_enums.SystemLinesEnum.FormulateUpfront

    FormulateNPLUpfront = plx_enums.SystemLinesEnum.FormulateNPLUpfront

    MaxLossTranches = plx_enums.SystemLinesEnum.MaxLossTranches

    PriceSetting = plx_enums.SystemLinesEnum.PriceSetting

    OfferQuantityFormat = plx_enums.SystemLinesEnum.OfferQuantityFormat

    FixedFlowMethod = plx_enums.SystemLinesEnum.FixedFlowMethod

    ExpansionOptimality = plx_enums.SystemLinesEnum.ExpansionOptimality

    Units = plx_enums.SystemLinesEnum.Units

    MaxFlow = plx_enums.SystemLinesEnum.MaxFlow

    MinFlow = plx_enums.SystemLinesEnum.MinFlow

    MaxRating = plx_enums.SystemLinesEnum.MaxRating

    MinRating = plx_enums.SystemLinesEnum.MinRating

    OverloadMaxRating = plx_enums.SystemLinesEnum.OverloadMaxRating

    OverloadMinRating = plx_enums.SystemLinesEnum.OverloadMinRating

    LimitPenalty = plx_enums.SystemLinesEnum.LimitPenalty

    Resistance = plx_enums.SystemLinesEnum.Resistance

    Reactance = plx_enums.SystemLinesEnum.Reactance

    Susceptance = plx_enums.SystemLinesEnum.Susceptance

    MaxRampUp = plx_enums.SystemLinesEnum.MaxRampUp

    MaxRampDown = plx_enums.SystemLinesEnum.MaxRampDown

    RampPenalty = plx_enums.SystemLinesEnum.RampPenalty

    LossBase = plx_enums.SystemLinesEnum.LossBase

    LossIncr = plx_enums.SystemLinesEnum.LossIncr

    LossIncr2 = plx_enums.SystemLinesEnum.LossIncr2

    LossBaseBack = plx_enums.SystemLinesEnum.LossBaseBack

    LossIncrBack = plx_enums.SystemLinesEnum.LossIncrBack

    LossIncr2Back = plx_enums.SystemLinesEnum.LossIncr2Back

    LossAllocation = plx_enums.SystemLinesEnum.LossAllocation

    FixedFlow = plx_enums.SystemLinesEnum.FixedFlow

    FixedFlowPenalty = plx_enums.SystemLinesEnum.FixedFlowPenalty

    FixedLoss = plx_enums.SystemLinesEnum.FixedLoss

    WheelingCharge = plx_enums.SystemLinesEnum.WheelingCharge

    WheelingChargeBack = plx_enums.SystemLinesEnum.WheelingChargeBack

    OfferBase = plx_enums.SystemLinesEnum.OfferBase

    OfferQuantity = plx_enums.SystemLinesEnum.OfferQuantity

    OfferPrice = plx_enums.SystemLinesEnum.OfferPrice

    OfferQuantityBack = plx_enums.SystemLinesEnum.OfferQuantityBack

    OfferPriceBack = plx_enums.SystemLinesEnum.OfferPriceBack

    MarginalLossFactor = plx_enums.SystemLinesEnum.MarginalLossFactor

    MarginalLossFactorBack = plx_enums.SystemLinesEnum.MarginalLossFactorBack

    FlowNonanticipativity = plx_enums.SystemLinesEnum.FlowNonanticipativity

    FlowNonanticipativityTime = plx_enums.SystemLinesEnum.FlowNonanticipativityTime

    FixedCharge = plx_enums.SystemLinesEnum.FixedCharge

    FOMCharge = plx_enums.SystemLinesEnum.FOMCharge

    EquityCharge = plx_enums.SystemLinesEnum.EquityCharge

    DebtCharge = plx_enums.SystemLinesEnum.DebtCharge

    Circuits = plx_enums.SystemLinesEnum.Circuits

    UnitsOut = plx_enums.SystemLinesEnum.UnitsOut

    MaintenanceRate = plx_enums.SystemLinesEnum.MaintenanceRate

    MaintenanceFrequency = plx_enums.SystemLinesEnum.MaintenanceFrequency

    ForcedOutageRate = plx_enums.SystemLinesEnum.ForcedOutageRate

    OutageMaxRating = plx_enums.SystemLinesEnum.OutageMaxRating

    OutageMinRating = plx_enums.SystemLinesEnum.OutageMinRating

    MeanTimetoRepair = plx_enums.SystemLinesEnum.MeanTimetoRepair

    MinTimeToRepair = plx_enums.SystemLinesEnum.MinTimeToRepair

    MaxTimeToRepair = plx_enums.SystemLinesEnum.MaxTimeToRepair

    RepairTimeShape = plx_enums.SystemLinesEnum.RepairTimeShape

    RepairTimeScale = plx_enums.SystemLinesEnum.RepairTimeScale

    MaxCapacityReserves = plx_enums.SystemLinesEnum.MaxCapacityReserves

    MinCapacityReserves = plx_enums.SystemLinesEnum.MinCapacityReserves

    FirmCapacity = plx_enums.SystemLinesEnum.FirmCapacity

    Type = plx_enums.SystemLinesEnum.Type

    BuildCost = plx_enums.SystemLinesEnum.BuildCost

    RetirementCost = plx_enums.SystemLinesEnum.RetirementCost

    LeadTime = plx_enums.SystemLinesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemLinesEnum.ProjectStartDate

    CommissionDate = plx_enums.SystemLinesEnum.CommissionDate

    TechnicalLife = plx_enums.SystemLinesEnum.TechnicalLife

    WACC = plx_enums.SystemLinesEnum.WACC

    EconomicLife = plx_enums.SystemLinesEnum.EconomicLife

    MaxUnitsBuilt = plx_enums.SystemLinesEnum.MaxUnitsBuilt

    MaxUnitsRetired = plx_enums.SystemLinesEnum.MaxUnitsRetired

    MinUnitsBuilt = plx_enums.SystemLinesEnum.MinUnitsBuilt

    MinUnitsRetired = plx_enums.SystemLinesEnum.MinUnitsRetired

    MaxUnitsBuiltinYear = plx_enums.SystemLinesEnum.MaxUnitsBuiltinYear

    MaxUnitsRetiredinYear = plx_enums.SystemLinesEnum.MaxUnitsRetiredinYear

    MinUnitsBuiltinYear = plx_enums.SystemLinesEnum.MinUnitsBuiltinYear

    MinUnitsRetiredinYear = plx_enums.SystemLinesEnum.MinUnitsRetiredinYear

    BuildNonanticipativity = plx_enums.SystemLinesEnum.BuildNonanticipativity

    RetireNonanticipativity = plx_enums.SystemLinesEnum.RetireNonanticipativity

    x = plx_enums.SystemLinesEnum.x

    y = plx_enums.SystemLinesEnum.y

    z = plx_enums.SystemLinesEnum.z


class SystemMLFsEnum(Enum):
    Intercept = plx_enums.SystemMLFsEnum.Intercept

    FlowCoefficient = plx_enums.SystemMLFsEnum.FlowCoefficient


class SystemMaintenancesEnum(Enum):
    Duration = plx_enums.SystemMaintenancesEnum.Duration

    Window = plx_enums.SystemMaintenancesEnum.Window

    StartWindow = plx_enums.SystemMaintenancesEnum.StartWindow

    EndWindow = plx_enums.SystemMaintenancesEnum.EndWindow

    Cost = plx_enums.SystemMaintenancesEnum.Cost

    Crew = plx_enums.SystemMaintenancesEnum.Crew

    Equipment = plx_enums.SystemMaintenancesEnum.Equipment

    LeadTime = plx_enums.SystemMaintenancesEnum.LeadTime

    MutuallyExclusive = plx_enums.SystemMaintenancesEnum.MutuallyExclusive

    PenaltyCost = plx_enums.SystemMaintenancesEnum.PenaltyCost

    MinOccurrence = plx_enums.SystemMaintenancesEnum.MinOccurrence

    Nonanticipativity = plx_enums.SystemMaintenancesEnum.Nonanticipativity

    x = plx_enums.SystemMaintenancesEnum.x

    y = plx_enums.SystemMaintenancesEnum.y

    z = plx_enums.SystemMaintenancesEnum.z


class SystemMarketsEnum(Enum):
    IsForward = plx_enums.SystemMarketsEnum.IsForward

    IsMarginal = plx_enums.SystemMarketsEnum.IsMarginal

    DemandCurve = plx_enums.SystemMarketsEnum.DemandCurve

    PriceSetting = plx_enums.SystemMarketsEnum.PriceSetting

    SupplySettlementModel = plx_enums.SystemMarketsEnum.SupplySettlementModel

    DemandSettlementModel = plx_enums.SystemMarketsEnum.DemandSettlementModel

    Units = plx_enums.SystemMarketsEnum.Units

    Price = plx_enums.SystemMarketsEnum.Price

    PriceScalar = plx_enums.SystemMarketsEnum.PriceScalar

    PriceIncr = plx_enums.SystemMarketsEnum.PriceIncr

    Quantity = plx_enums.SystemMarketsEnum.Quantity

    BaseQuantity = plx_enums.SystemMarketsEnum.BaseQuantity

    SellUnit = plx_enums.SystemMarketsEnum.SellUnit

    SellBlock = plx_enums.SystemMarketsEnum.SellBlock

    SellBlockFixedCharge = plx_enums.SystemMarketsEnum.SellBlockFixedCharge

    BuyUnit = plx_enums.SystemMarketsEnum.BuyUnit

    BuyBlock = plx_enums.SystemMarketsEnum.BuyBlock

    BuyBlockFixedCharge = plx_enums.SystemMarketsEnum.BuyBlockFixedCharge

    MinSales = plx_enums.SystemMarketsEnum.MinSales

    MaxSales = plx_enums.SystemMarketsEnum.MaxSales

    MinPurchases = plx_enums.SystemMarketsEnum.MinPurchases

    MaxPurchases = plx_enums.SystemMarketsEnum.MaxPurchases

    BidAskSpread = plx_enums.SystemMarketsEnum.BidAskSpread

    BidSpread = plx_enums.SystemMarketsEnum.BidSpread

    AskSpread = plx_enums.SystemMarketsEnum.AskSpread

    FirmCapacity = plx_enums.SystemMarketsEnum.FirmCapacity

    LoadObligation = plx_enums.SystemMarketsEnum.LoadObligation

    x = plx_enums.SystemMarketsEnum.x

    y = plx_enums.SystemMarketsEnum.y

    z = plx_enums.SystemMarketsEnum.z


class SystemNodesEnum(Enum):
    MustReport = plx_enums.SystemNodesEnum.MustReport

    IsSlackBus = plx_enums.SystemNodesEnum.IsSlackBus

    AllowDumpEnergy = plx_enums.SystemNodesEnum.AllowDumpEnergy

    AllowUnservedEnergy = plx_enums.SystemNodesEnum.AllowUnservedEnergy

    ReferenceLoad = plx_enums.SystemNodesEnum.ReferenceLoad

    Voltage = plx_enums.SystemNodesEnum.Voltage

    Units = plx_enums.SystemNodesEnum.Units

    LoadParticipationFactor = plx_enums.SystemNodesEnum.LoadParticipationFactor

    Load = plx_enums.SystemNodesEnum.Load

    FixedLoad = plx_enums.SystemNodesEnum.FixedLoad

    FixedGeneration = plx_enums.SystemNodesEnum.FixedGeneration

    MaxNetInjection = plx_enums.SystemNodesEnum.MaxNetInjection

    MaxNetOfftake = plx_enums.SystemNodesEnum.MaxNetOfftake

    Rating = plx_enums.SystemNodesEnum.Rating

    DSPBidQuantity = plx_enums.SystemNodesEnum.DSPBidQuantity

    DSPBidRatio = plx_enums.SystemNodesEnum.DSPBidRatio

    DSPBidPrice = plx_enums.SystemNodesEnum.DSPBidPrice

    Price = plx_enums.SystemNodesEnum.Price

    MaxMaintenance = plx_enums.SystemNodesEnum.MaxMaintenance

    MaintenanceFactor = plx_enums.SystemNodesEnum.MaintenanceFactor

    MinCapacityReserves = plx_enums.SystemNodesEnum.MinCapacityReserves

    MinCapacityReserveMargin = plx_enums.SystemNodesEnum.MinCapacityReserveMargin

    x = plx_enums.SystemNodesEnum.x

    y = plx_enums.SystemNodesEnum.y

    z = plx_enums.SystemNodesEnum.z


class SystemOutAbatementsEnum(Enum):
    Units = plx_enums.SystemOutAbatementsEnum.Units

    OperatingHours = plx_enums.SystemOutAbatementsEnum.OperatingHours

    GrossEmissions = plx_enums.SystemOutAbatementsEnum.GrossEmissions

    Abatement = plx_enums.SystemOutAbatementsEnum.Abatement

    NetEmissions = plx_enums.SystemOutAbatementsEnum.NetEmissions

    Efficiency = plx_enums.SystemOutAbatementsEnum.Efficiency

    AbatementCost = plx_enums.SystemOutAbatementsEnum.AbatementCost

    RunningCost = plx_enums.SystemOutAbatementsEnum.RunningCost

    VOMCost = plx_enums.SystemOutAbatementsEnum.VOMCost

    ConsumablesCost = plx_enums.SystemOutAbatementsEnum.ConsumablesCost

    FOMCost = plx_enums.SystemOutAbatementsEnum.FOMCost

    TotalCost = plx_enums.SystemOutAbatementsEnum.TotalCost

    AbatementValue = plx_enums.SystemOutAbatementsEnum.AbatementValue

    AbatementNetCost = plx_enums.SystemOutAbatementsEnum.AbatementNetCost

    UnitsOut = plx_enums.SystemOutAbatementsEnum.UnitsOut

    x = plx_enums.SystemOutAbatementsEnum.x

    y = plx_enums.SystemOutAbatementsEnum.y

    z = plx_enums.SystemOutAbatementsEnum.z


class SystemOutBatteriesEnum(Enum):
    Units = plx_enums.SystemOutBatteriesEnum.Units

    Energy = plx_enums.SystemOutBatteriesEnum.Energy

    SoC = plx_enums.SystemOutBatteriesEnum.SoC

    AvailableSoC = plx_enums.SystemOutBatteriesEnum.AvailableSoC

    Generation = plx_enums.SystemOutBatteriesEnum.Generation

    Load = plx_enums.SystemOutBatteriesEnum.Load

    NetGeneration = plx_enums.SystemOutBatteriesEnum.NetGeneration

    Losses = plx_enums.SystemOutBatteriesEnum.Losses

    HoursCharging = plx_enums.SystemOutBatteriesEnum.HoursCharging

    HoursDischarging = plx_enums.SystemOutBatteriesEnum.HoursDischarging

    HoursIdle = plx_enums.SystemOutBatteriesEnum.HoursIdle

    RaiseReserve = plx_enums.SystemOutBatteriesEnum.RaiseReserve

    LowerReserve = plx_enums.SystemOutBatteriesEnum.LowerReserve

    RegulationRaiseReserve = plx_enums.SystemOutBatteriesEnum.RegulationRaiseReserve

    RegulationLowerReserve = plx_enums.SystemOutBatteriesEnum.RegulationLowerReserve

    ReplacementReserve = plx_enums.SystemOutBatteriesEnum.ReplacementReserve

    VOMCost = plx_enums.SystemOutBatteriesEnum.VOMCost

    UoSCost = plx_enums.SystemOutBatteriesEnum.UoSCost

    CapacityFactor = plx_enums.SystemOutBatteriesEnum.CapacityFactor

    LoadFactor = plx_enums.SystemOutBatteriesEnum.LoadFactor

    PriceReceived = plx_enums.SystemOutBatteriesEnum.PriceReceived

    PricePaid = plx_enums.SystemOutBatteriesEnum.PricePaid

    GenerationRevenue = plx_enums.SystemOutBatteriesEnum.GenerationRevenue

    CosttoLoad = plx_enums.SystemOutBatteriesEnum.CosttoLoad

    NetGenerationRevenue = plx_enums.SystemOutBatteriesEnum.NetGenerationRevenue

    ReservesRevenue = plx_enums.SystemOutBatteriesEnum.ReservesRevenue

    ClearedReserveOfferCost = plx_enums.SystemOutBatteriesEnum.ClearedReserveOfferCost

    NetProfit = plx_enums.SystemOutBatteriesEnum.NetProfit

    InstalledCapacity = plx_enums.SystemOutBatteriesEnum.InstalledCapacity

    FirmCapacity = plx_enums.SystemOutBatteriesEnum.FirmCapacity

    FOMCost = plx_enums.SystemOutBatteriesEnum.FOMCost

    Age = plx_enums.SystemOutBatteriesEnum.Age

    UnitsBuilt = plx_enums.SystemOutBatteriesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutBatteriesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutBatteriesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutBatteriesEnum.RetirementCost

    x = plx_enums.SystemOutBatteriesEnum.x

    y = plx_enums.SystemOutBatteriesEnum.y

    z = plx_enums.SystemOutBatteriesEnum.z


class SystemOutCompaniesEnum(Enum):
    Generation = plx_enums.SystemOutCompaniesEnum.Generation

    FuelOfftake = plx_enums.SystemOutCompaniesEnum.FuelOfftake

    WasteHeat = plx_enums.SystemOutCompaniesEnum.WasteHeat

    StartFuelOfftake = plx_enums.SystemOutCompaniesEnum.StartFuelOfftake

    DispatchableCapacity = plx_enums.SystemOutCompaniesEnum.DispatchableCapacity

    UndispatchedCapacity = plx_enums.SystemOutCompaniesEnum.UndispatchedCapacity

    NoCostCapacity = plx_enums.SystemOutCompaniesEnum.NoCostCapacity

    CapacityCurtailed = plx_enums.SystemOutCompaniesEnum.CapacityCurtailed

    FixedLoadGeneration = plx_enums.SystemOutCompaniesEnum.FixedLoadGeneration

    MinLoadGeneration = plx_enums.SystemOutCompaniesEnum.MinLoadGeneration

    RaiseReserve = plx_enums.SystemOutCompaniesEnum.RaiseReserve

    LowerReserve = plx_enums.SystemOutCompaniesEnum.LowerReserve

    RegulationRaiseReserve = plx_enums.SystemOutCompaniesEnum.RegulationRaiseReserve

    RegulationLowerReserve = plx_enums.SystemOutCompaniesEnum.RegulationLowerReserve

    ReplacementReserve = plx_enums.SystemOutCompaniesEnum.ReplacementReserve

    AuxiliaryUse = plx_enums.SystemOutCompaniesEnum.AuxiliaryUse

    PumpLoad = plx_enums.SystemOutCompaniesEnum.PumpLoad

    Load = plx_enums.SystemOutCompaniesEnum.Load

    PurchaserLoad = plx_enums.SystemOutCompaniesEnum.PurchaserLoad

    NetGeneration = plx_enums.SystemOutCompaniesEnum.NetGeneration

    NetLoad = plx_enums.SystemOutCompaniesEnum.NetLoad

    FuelPrice = plx_enums.SystemOutCompaniesEnum.FuelPrice

    FuelCost = plx_enums.SystemOutCompaniesEnum.FuelCost

    FuelTransportCost = plx_enums.SystemOutCompaniesEnum.FuelTransportCost

    FuelTransitionCost = plx_enums.SystemOutCompaniesEnum.FuelTransitionCost

    FuelInventoryCost = plx_enums.SystemOutCompaniesEnum.FuelInventoryCost

    VOMCost = plx_enums.SystemOutCompaniesEnum.VOMCost

    UoSCost = plx_enums.SystemOutCompaniesEnum.UoSCost

    PumpCost = plx_enums.SystemOutCompaniesEnum.PumpCost

    ReservesVOMCost = plx_enums.SystemOutCompaniesEnum.ReservesVOMCost

    ReservesCost = plx_enums.SystemOutCompaniesEnum.ReservesCost

    GenerationCost = plx_enums.SystemOutCompaniesEnum.GenerationCost

    GeneratorStartShutdownCost = plx_enums.SystemOutCompaniesEnum.GeneratorStartShutdownCost

    StartFuelCost = plx_enums.SystemOutCompaniesEnum.StartFuelCost

    EmissionsCost = plx_enums.SystemOutCompaniesEnum.EmissionsCost

    AbatementCost = plx_enums.SystemOutCompaniesEnum.AbatementCost

    TotalGenerationCost = plx_enums.SystemOutCompaniesEnum.TotalGenerationCost

    TotalSystemCost = plx_enums.SystemOutCompaniesEnum.TotalSystemCost

    FuelContractCost = plx_enums.SystemOutCompaniesEnum.FuelContractCost

    FOMCost = plx_enums.SystemOutCompaniesEnum.FOMCost

    EquityCost = plx_enums.SystemOutCompaniesEnum.EquityCost

    DebtCost = plx_enums.SystemOutCompaniesEnum.DebtCost

    FixedCosts = plx_enums.SystemOutCompaniesEnum.FixedCosts

    CosttoLoad = plx_enums.SystemOutCompaniesEnum.CosttoLoad

    SRMC = plx_enums.SystemOutCompaniesEnum.SRMC

    PriceReceived = plx_enums.SystemOutCompaniesEnum.PriceReceived

    PricePaid = plx_enums.SystemOutCompaniesEnum.PricePaid

    PoolRevenue = plx_enums.SystemOutCompaniesEnum.PoolRevenue

    ReservesRevenue = plx_enums.SystemOutCompaniesEnum.ReservesRevenue

    GasMarketRevenue = plx_enums.SystemOutCompaniesEnum.GasMarketRevenue

    HeatMarketRevenue = plx_enums.SystemOutCompaniesEnum.HeatMarketRevenue

    FuelMarketRevenue = plx_enums.SystemOutCompaniesEnum.FuelMarketRevenue

    TransmissionRental = plx_enums.SystemOutCompaniesEnum.TransmissionRental

    NetGenerationRevenue = plx_enums.SystemOutCompaniesEnum.NetGenerationRevenue

    NetCosttoLoad = plx_enums.SystemOutCompaniesEnum.NetCosttoLoad

    NetReservesRevenue = plx_enums.SystemOutCompaniesEnum.NetReservesRevenue

    NetRevenue = plx_enums.SystemOutCompaniesEnum.NetRevenue

    NetProfit = plx_enums.SystemOutCompaniesEnum.NetProfit

    GenerationatRRN = plx_enums.SystemOutCompaniesEnum.GenerationatRRN

    ContractVolume = plx_enums.SystemOutCompaniesEnum.ContractVolume

    NetContractVolume = plx_enums.SystemOutCompaniesEnum.NetContractVolume

    ContractSettlement = plx_enums.SystemOutCompaniesEnum.ContractSettlement

    NetContractSettlement = plx_enums.SystemOutCompaniesEnum.NetContractSettlement

    NetPoolRevenue = plx_enums.SystemOutCompaniesEnum.NetPoolRevenue

    ContractGeneration = plx_enums.SystemOutCompaniesEnum.ContractGeneration

    ContractLoad = plx_enums.SystemOutCompaniesEnum.ContractLoad

    ContractCost = plx_enums.SystemOutCompaniesEnum.ContractCost

    ContractRevenue = plx_enums.SystemOutCompaniesEnum.ContractRevenue

    NetContractRevenue = plx_enums.SystemOutCompaniesEnum.NetContractRevenue

    ShadowGeneration = plx_enums.SystemOutCompaniesEnum.ShadowGeneration

    GeneratorMonopolyRent = plx_enums.SystemOutCompaniesEnum.GeneratorMonopolyRent

    StrategicShadowPrice = plx_enums.SystemOutCompaniesEnum.StrategicShadowPrice

    ConstrainedOnRevenue = plx_enums.SystemOutCompaniesEnum.ConstrainedOnRevenue

    ConstrainedOffRevenue = plx_enums.SystemOutCompaniesEnum.ConstrainedOffRevenue

    InstalledCapacity = plx_enums.SystemOutCompaniesEnum.InstalledCapacity

    AvailableCapacity = plx_enums.SystemOutCompaniesEnum.AvailableCapacity

    GeneratorFirmCapacity = plx_enums.SystemOutCompaniesEnum.GeneratorFirmCapacity

    CapacityBuilt = plx_enums.SystemOutCompaniesEnum.CapacityBuilt

    CapacityRetired = plx_enums.SystemOutCompaniesEnum.CapacityRetired

    NetNewCapacity = plx_enums.SystemOutCompaniesEnum.NetNewCapacity

    CapacityRevenue = plx_enums.SystemOutCompaniesEnum.CapacityRevenue

    CapacityPrice = plx_enums.SystemOutCompaniesEnum.CapacityPrice

    BuildCost = plx_enums.SystemOutCompaniesEnum.BuildCost

    RetirementCost = plx_enums.SystemOutCompaniesEnum.RetirementCost

    AnnualizedBuildCost = plx_enums.SystemOutCompaniesEnum.AnnualizedBuildCost

    TotalCost = plx_enums.SystemOutCompaniesEnum.TotalCost

    LevelizedCost = plx_enums.SystemOutCompaniesEnum.LevelizedCost

    ShadowCapacityBuilt = plx_enums.SystemOutCompaniesEnum.ShadowCapacityBuilt

    x = plx_enums.SystemOutCompaniesEnum.x

    y = plx_enums.SystemOutCompaniesEnum.y

    z = plx_enums.SystemOutCompaniesEnum.z


class SystemOutConstraintsEnum(Enum):
    Activity = plx_enums.SystemOutConstraintsEnum.Activity

    Slack = plx_enums.SystemOutConstraintsEnum.Slack

    Violation = plx_enums.SystemOutConstraintsEnum.Violation

    HoursBinding = plx_enums.SystemOutConstraintsEnum.HoursBinding

    RHS = plx_enums.SystemOutConstraintsEnum.RHS

    Price = plx_enums.SystemOutConstraintsEnum.Price

    HoursActive = plx_enums.SystemOutConstraintsEnum.HoursActive

    PenaltyCost = plx_enums.SystemOutConstraintsEnum.PenaltyCost

    Rental = plx_enums.SystemOutConstraintsEnum.Rental

    x = plx_enums.SystemOutConstraintsEnum.x

    y = plx_enums.SystemOutConstraintsEnum.y

    z = plx_enums.SystemOutConstraintsEnum.z


class SystemOutContingenciesEnum(Enum):
    HoursBinding = plx_enums.SystemOutContingenciesEnum.HoursBinding

    ShadowPrice = plx_enums.SystemOutContingenciesEnum.ShadowPrice

    x = plx_enums.SystemOutContingenciesEnum.x

    y = plx_enums.SystemOutContingenciesEnum.y

    z = plx_enums.SystemOutContingenciesEnum.z


class SystemOutCournotsEnum(Enum):
    Elasticity = plx_enums.SystemOutCournotsEnum.Elasticity

    DemandIntercept = plx_enums.SystemOutCournotsEnum.DemandIntercept

    DemandSlope = plx_enums.SystemOutCournotsEnum.DemandSlope

    PerfectCompetitionDemand = plx_enums.SystemOutCournotsEnum.PerfectCompetitionDemand

    PerfectCompetitionProduction = plx_enums.SystemOutCournotsEnum.PerfectCompetitionProduction

    PerfectCompetitionNetImport = plx_enums.SystemOutCournotsEnum.PerfectCompetitionNetImport

    PerfectCompetitionPrice = plx_enums.SystemOutCournotsEnum.PerfectCompetitionPrice

    PerfectCompetitionProducerRevenue = plx_enums.SystemOutCournotsEnum.PerfectCompetitionProducerRevenue

    PerfectCompetitionConsumerSurplus = plx_enums.SystemOutCournotsEnum.PerfectCompetitionConsumerSurplus

    PerfectCompetitionProducerSurplus = plx_enums.SystemOutCournotsEnum.PerfectCompetitionProducerSurplus

    Demand = plx_enums.SystemOutCournotsEnum.Demand

    Production = plx_enums.SystemOutCournotsEnum.Production

    NetImport = plx_enums.SystemOutCournotsEnum.NetImport

    Price = plx_enums.SystemOutCournotsEnum.Price

    ProducerRevenue = plx_enums.SystemOutCournotsEnum.ProducerRevenue

    ConsumerSurplus = plx_enums.SystemOutCournotsEnum.ConsumerSurplus

    ProducerSurplus = plx_enums.SystemOutCournotsEnum.ProducerSurplus


class SystemOutDecisionVariablesEnum(Enum):
    Value = plx_enums.SystemOutDecisionVariablesEnum.Value

    ReducedCost = plx_enums.SystemOutDecisionVariablesEnum.ReducedCost

    Cost = plx_enums.SystemOutDecisionVariablesEnum.Cost

    ObjectiveFunctionCoefficient = plx_enums.SystemOutDecisionVariablesEnum.ObjectiveFunctionCoefficient

    LowerBound = plx_enums.SystemOutDecisionVariablesEnum.LowerBound

    UpperBound = plx_enums.SystemOutDecisionVariablesEnum.UpperBound

    MinValue = plx_enums.SystemOutDecisionVariablesEnum.MinValue

    MaxValue = plx_enums.SystemOutDecisionVariablesEnum.MaxValue

    x = plx_enums.SystemOutDecisionVariablesEnum.x

    y = plx_enums.SystemOutDecisionVariablesEnum.y

    z = plx_enums.SystemOutDecisionVariablesEnum.z


class SystemOutEmissionsEnum(Enum):
    Production = plx_enums.SystemOutEmissionsEnum.Production

    GrossProduction = plx_enums.SystemOutEmissionsEnum.GrossProduction

    Removal = plx_enums.SystemOutEmissionsEnum.Removal

    RemovalCost = plx_enums.SystemOutEmissionsEnum.RemovalCost

    Abatement = plx_enums.SystemOutEmissionsEnum.Abatement

    AbatementCost = plx_enums.SystemOutEmissionsEnum.AbatementCost

    Generation = plx_enums.SystemOutEmissionsEnum.Generation

    Intensity = plx_enums.SystemOutEmissionsEnum.Intensity

    Price = plx_enums.SystemOutEmissionsEnum.Price

    ShadowPrice = plx_enums.SystemOutEmissionsEnum.ShadowPrice

    Cost = plx_enums.SystemOutEmissionsEnum.Cost

    MaxProductionViolation = plx_enums.SystemOutEmissionsEnum.MaxProductionViolation

    MaxProductionViolationCost = plx_enums.SystemOutEmissionsEnum.MaxProductionViolationCost

    x = plx_enums.SystemOutEmissionsEnum.x

    y = plx_enums.SystemOutEmissionsEnum.y

    z = plx_enums.SystemOutEmissionsEnum.z


class SystemOutFinancialContractsEnum(Enum):
    Quantity = plx_enums.SystemOutFinancialContractsEnum.Quantity

    FloorPrice = plx_enums.SystemOutFinancialContractsEnum.FloorPrice

    CapPrice = plx_enums.SystemOutFinancialContractsEnum.CapPrice

    SettlementPrice = plx_enums.SystemOutFinancialContractsEnum.SettlementPrice

    Shortfall = plx_enums.SystemOutFinancialContractsEnum.Shortfall

    SettlementQuantity = plx_enums.SystemOutFinancialContractsEnum.SettlementQuantity

    Settlement = plx_enums.SystemOutFinancialContractsEnum.Settlement

    HoursActive = plx_enums.SystemOutFinancialContractsEnum.HoursActive


class SystemOutFlowControlsEnum(Enum):
    Angle = plx_enums.SystemOutFlowControlsEnum.Angle

    MinAngle = plx_enums.SystemOutFlowControlsEnum.MinAngle

    MaxAngle = plx_enums.SystemOutFlowControlsEnum.MaxAngle

    Flow = plx_enums.SystemOutFlowControlsEnum.Flow

    FlowBack = plx_enums.SystemOutFlowControlsEnum.FlowBack

    Impedance = plx_enums.SystemOutFlowControlsEnum.Impedance

    HoursBinding = plx_enums.SystemOutFlowControlsEnum.HoursBinding

    ShadowPrice = plx_enums.SystemOutFlowControlsEnum.ShadowPrice

    Rental = plx_enums.SystemOutFlowControlsEnum.Rental

    Penalty = plx_enums.SystemOutFlowControlsEnum.Penalty

    UnitsBuilt = plx_enums.SystemOutFlowControlsEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutFlowControlsEnum.BuildCost

    x = plx_enums.SystemOutFlowControlsEnum.x

    y = plx_enums.SystemOutFlowControlsEnum.y

    z = plx_enums.SystemOutFlowControlsEnum.z


class SystemOutFuelContractsEnum(Enum):
    Offtake = plx_enums.SystemOutFuelContractsEnum.Offtake

    Cost = plx_enums.SystemOutFuelContractsEnum.Cost

    Price = plx_enums.SystemOutFuelContractsEnum.Price

    TakeorPayPrice = plx_enums.SystemOutFuelContractsEnum.TakeorPayPrice

    ShadowPrice = plx_enums.SystemOutFuelContractsEnum.ShadowPrice

    TakeorPayShadowPrice = plx_enums.SystemOutFuelContractsEnum.TakeorPayShadowPrice

    TakeorPayViolation = plx_enums.SystemOutFuelContractsEnum.TakeorPayViolation

    TakeorPayViolationCost = plx_enums.SystemOutFuelContractsEnum.TakeorPayViolationCost

    FOMCost = plx_enums.SystemOutFuelContractsEnum.FOMCost

    TotalCost = plx_enums.SystemOutFuelContractsEnum.TotalCost

    x = plx_enums.SystemOutFuelContractsEnum.x

    y = plx_enums.SystemOutFuelContractsEnum.y

    z = plx_enums.SystemOutFuelContractsEnum.z


class SystemOutFuelsEnum(Enum):
    Price = plx_enums.SystemOutFuelsEnum.Price

    Tax = plx_enums.SystemOutFuelsEnum.Tax

    TotalPrice = plx_enums.SystemOutFuelsEnum.TotalPrice

    TimeweightedPrice = plx_enums.SystemOutFuelsEnum.TimeweightedPrice

    Offtake = plx_enums.SystemOutFuelsEnum.Offtake

    MaxOfftake = plx_enums.SystemOutFuelsEnum.MaxOfftake

    MinOfftake = plx_enums.SystemOutFuelsEnum.MinOfftake

    MaxInventory = plx_enums.SystemOutFuelsEnum.MaxInventory

    MinInventory = plx_enums.SystemOutFuelsEnum.MinInventory

    OpeningInventory = plx_enums.SystemOutFuelsEnum.OpeningInventory

    ClosingInventory = plx_enums.SystemOutFuelsEnum.ClosingInventory

    Delivery = plx_enums.SystemOutFuelsEnum.Delivery

    Withdrawal = plx_enums.SystemOutFuelsEnum.Withdrawal

    NetWithdrawal = plx_enums.SystemOutFuelsEnum.NetWithdrawal

    Cost = plx_enums.SystemOutFuelsEnum.Cost

    TaxCost = plx_enums.SystemOutFuelsEnum.TaxCost

    DeliveryCost = plx_enums.SystemOutFuelsEnum.DeliveryCost

    InventoryCost = plx_enums.SystemOutFuelsEnum.InventoryCost

    ReservationCost = plx_enums.SystemOutFuelsEnum.ReservationCost

    WithdrawalCost = plx_enums.SystemOutFuelsEnum.WithdrawalCost

    TotalCost = plx_enums.SystemOutFuelsEnum.TotalCost

    ShadowPrice = plx_enums.SystemOutFuelsEnum.ShadowPrice

    Generation = plx_enums.SystemOutFuelsEnum.Generation

    AverageHeatRate = plx_enums.SystemOutFuelsEnum.AverageHeatRate

    InstalledCapacity = plx_enums.SystemOutFuelsEnum.InstalledCapacity

    FOMCost = plx_enums.SystemOutFuelsEnum.FOMCost

    x = plx_enums.SystemOutFuelsEnum.x

    y = plx_enums.SystemOutFuelsEnum.y

    z = plx_enums.SystemOutFuelsEnum.z


class SystemOutGasBasinsEnum(Enum):
    InitialVolume = plx_enums.SystemOutGasBasinsEnum.InitialVolume

    EndVolume = plx_enums.SystemOutGasBasinsEnum.EndVolume

    Production = plx_enums.SystemOutGasBasinsEnum.Production

    ProductionCost = plx_enums.SystemOutGasBasinsEnum.ProductionCost

    FOMCost = plx_enums.SystemOutGasBasinsEnum.FOMCost

    FixedCosts = plx_enums.SystemOutGasBasinsEnum.FixedCosts

    ShadowPrice = plx_enums.SystemOutGasBasinsEnum.ShadowPrice

    Units = plx_enums.SystemOutGasBasinsEnum.Units

    UnitsBuilt = plx_enums.SystemOutGasBasinsEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutGasBasinsEnum.BuildCost

    x = plx_enums.SystemOutGasBasinsEnum.x

    y = plx_enums.SystemOutGasBasinsEnum.y

    z = plx_enums.SystemOutGasBasinsEnum.z


class SystemOutGasContractsEnum(Enum):
    Production = plx_enums.SystemOutGasContractsEnum.Production

    Cost = plx_enums.SystemOutGasContractsEnum.Cost

    Price = plx_enums.SystemOutGasContractsEnum.Price

    ShadowPrice = plx_enums.SystemOutGasContractsEnum.ShadowPrice

    TotalCost = plx_enums.SystemOutGasContractsEnum.TotalCost

    TakeorPayPrice = plx_enums.SystemOutGasContractsEnum.TakeorPayPrice

    TakeorPayShadowPrice = plx_enums.SystemOutGasContractsEnum.TakeorPayShadowPrice

    TakeorPayViolation = plx_enums.SystemOutGasContractsEnum.TakeorPayViolation

    TakeorPayViolationCost = plx_enums.SystemOutGasContractsEnum.TakeorPayViolationCost

    x = plx_enums.SystemOutGasContractsEnum.x

    y = plx_enums.SystemOutGasContractsEnum.y

    z = plx_enums.SystemOutGasContractsEnum.z


class SystemOutGasDemandsEnum(Enum):
    Demand = plx_enums.SystemOutGasDemandsEnum.Demand

    ShortageHours = plx_enums.SystemOutGasDemandsEnum.ShortageHours

    Shortage = plx_enums.SystemOutGasDemandsEnum.Shortage

    ShortageCost = plx_enums.SystemOutGasDemandsEnum.ShortageCost

    ExcessHours = plx_enums.SystemOutGasDemandsEnum.ExcessHours

    Excess = plx_enums.SystemOutGasDemandsEnum.Excess

    ExcessCost = plx_enums.SystemOutGasDemandsEnum.ExcessCost

    NetDemand = plx_enums.SystemOutGasDemandsEnum.NetDemand

    Cost = plx_enums.SystemOutGasDemandsEnum.Cost

    PricePaid = plx_enums.SystemOutGasDemandsEnum.PricePaid

    BidQuantity = plx_enums.SystemOutGasDemandsEnum.BidQuantity

    BidPrice = plx_enums.SystemOutGasDemandsEnum.BidPrice

    BidCleared = plx_enums.SystemOutGasDemandsEnum.BidCleared

    ClearedBidPrice = plx_enums.SystemOutGasDemandsEnum.ClearedBidPrice

    ClearedBidValue = plx_enums.SystemOutGasDemandsEnum.ClearedBidValue

    x = plx_enums.SystemOutGasDemandsEnum.x

    y = plx_enums.SystemOutGasDemandsEnum.y

    z = plx_enums.SystemOutGasDemandsEnum.z


class SystemOutGasFieldsEnum(Enum):
    InitialVolume = plx_enums.SystemOutGasFieldsEnum.InitialVolume

    EndVolume = plx_enums.SystemOutGasFieldsEnum.EndVolume

    Production = plx_enums.SystemOutGasFieldsEnum.Production

    ProductionCost = plx_enums.SystemOutGasFieldsEnum.ProductionCost

    FOMCost = plx_enums.SystemOutGasFieldsEnum.FOMCost

    FixedCosts = plx_enums.SystemOutGasFieldsEnum.FixedCosts

    ShadowPrice = plx_enums.SystemOutGasFieldsEnum.ShadowPrice

    Units = plx_enums.SystemOutGasFieldsEnum.Units

    UnitsBuilt = plx_enums.SystemOutGasFieldsEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutGasFieldsEnum.BuildCost

    x = plx_enums.SystemOutGasFieldsEnum.x

    y = plx_enums.SystemOutGasFieldsEnum.y

    z = plx_enums.SystemOutGasFieldsEnum.z


class SystemOutGasNodesEnum(Enum):
    Production = plx_enums.SystemOutGasNodesEnum.Production

    Demand = plx_enums.SystemOutGasNodesEnum.Demand

    Flow = plx_enums.SystemOutGasNodesEnum.Flow

    Imports = plx_enums.SystemOutGasNodesEnum.Imports

    Exports = plx_enums.SystemOutGasNodesEnum.Exports

    NetInterchange = plx_enums.SystemOutGasNodesEnum.NetInterchange

    NetMarketSales = plx_enums.SystemOutGasNodesEnum.NetMarketSales

    InitialVolume = plx_enums.SystemOutGasNodesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutGasNodesEnum.EndVolume

    ProductionCost = plx_enums.SystemOutGasNodesEnum.ProductionCost

    ShortageHours = plx_enums.SystemOutGasNodesEnum.ShortageHours

    Shortage = plx_enums.SystemOutGasNodesEnum.Shortage

    ShortageCost = plx_enums.SystemOutGasNodesEnum.ShortageCost

    ExcessHours = plx_enums.SystemOutGasNodesEnum.ExcessHours

    Excess = plx_enums.SystemOutGasNodesEnum.Excess

    ExcessCost = plx_enums.SystemOutGasNodesEnum.ExcessCost

    ShadowPrice = plx_enums.SystemOutGasNodesEnum.ShadowPrice

    Price = plx_enums.SystemOutGasNodesEnum.Price

    FOMCost = plx_enums.SystemOutGasNodesEnum.FOMCost

    FixedCosts = plx_enums.SystemOutGasNodesEnum.FixedCosts

    Units = plx_enums.SystemOutGasNodesEnum.Units

    UnitsBuilt = plx_enums.SystemOutGasNodesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutGasNodesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutGasNodesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutGasNodesEnum.RetirementCost

    x = plx_enums.SystemOutGasNodesEnum.x

    y = plx_enums.SystemOutGasNodesEnum.y

    z = plx_enums.SystemOutGasNodesEnum.z


class SystemOutGasPipelinesEnum(Enum):
    Flow = plx_enums.SystemOutGasPipelinesEnum.Flow

    HoursCongested = plx_enums.SystemOutGasPipelinesEnum.HoursCongested

    HoursCongestedBack = plx_enums.SystemOutGasPipelinesEnum.HoursCongestedBack

    MaxVolume = plx_enums.SystemOutGasPipelinesEnum.MaxVolume

    MinVolume = plx_enums.SystemOutGasPipelinesEnum.MinVolume

    InitialVolume = plx_enums.SystemOutGasPipelinesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutGasPipelinesEnum.EndVolume

    VolumeImbalance = plx_enums.SystemOutGasPipelinesEnum.VolumeImbalance

    ImbalanceCost = plx_enums.SystemOutGasPipelinesEnum.ImbalanceCost

    ProductionCost = plx_enums.SystemOutGasPipelinesEnum.ProductionCost

    FOMCost = plx_enums.SystemOutGasPipelinesEnum.FOMCost

    FixedCosts = plx_enums.SystemOutGasPipelinesEnum.FixedCosts

    UnitsOut = plx_enums.SystemOutGasPipelinesEnum.UnitsOut

    MaintenanceHours = plx_enums.SystemOutGasPipelinesEnum.MaintenanceHours

    ForcedOutageHours = plx_enums.SystemOutGasPipelinesEnum.ForcedOutageHours

    ServiceFactor = plx_enums.SystemOutGasPipelinesEnum.ServiceFactor

    Units = plx_enums.SystemOutGasPipelinesEnum.Units

    UnitsBuilt = plx_enums.SystemOutGasPipelinesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutGasPipelinesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutGasPipelinesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutGasPipelinesEnum.RetirementCost

    x = plx_enums.SystemOutGasPipelinesEnum.x

    y = plx_enums.SystemOutGasPipelinesEnum.y

    z = plx_enums.SystemOutGasPipelinesEnum.z


class SystemOutGasPlantsEnum(Enum):
    RawGas = plx_enums.SystemOutGasPlantsEnum.RawGas

    Production = plx_enums.SystemOutGasPlantsEnum.Production

    ProductionCost = plx_enums.SystemOutGasPlantsEnum.ProductionCost

    Consumption = plx_enums.SystemOutGasPlantsEnum.Consumption

    EnergyConsumption = plx_enums.SystemOutGasPlantsEnum.EnergyConsumption

    VOMCost = plx_enums.SystemOutGasPlantsEnum.VOMCost

    FOMCost = plx_enums.SystemOutGasPlantsEnum.FOMCost

    FixedCosts = plx_enums.SystemOutGasPlantsEnum.FixedCosts

    SRMC = plx_enums.SystemOutGasPlantsEnum.SRMC

    Units = plx_enums.SystemOutGasPlantsEnum.Units

    UnitsBuilt = plx_enums.SystemOutGasPlantsEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutGasPlantsEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutGasPlantsEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutGasPlantsEnum.RetirementCost

    x = plx_enums.SystemOutGasPlantsEnum.x

    y = plx_enums.SystemOutGasPlantsEnum.y

    z = plx_enums.SystemOutGasPlantsEnum.z


class SystemOutGasStoragesEnum(Enum):
    MaxVolume = plx_enums.SystemOutGasStoragesEnum.MaxVolume

    MinVolume = plx_enums.SystemOutGasStoragesEnum.MinVolume

    InitialVolume = plx_enums.SystemOutGasStoragesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutGasStoragesEnum.EndVolume

    WorkingVolume = plx_enums.SystemOutGasStoragesEnum.WorkingVolume

    Utilization = plx_enums.SystemOutGasStoragesEnum.Utilization

    WorkingUtilization = plx_enums.SystemOutGasStoragesEnum.WorkingUtilization

    AverageUtilization = plx_enums.SystemOutGasStoragesEnum.AverageUtilization

    AverageWorkingUtilization = plx_enums.SystemOutGasStoragesEnum.AverageWorkingUtilization

    Withdrawal = plx_enums.SystemOutGasStoragesEnum.Withdrawal

    Injection = plx_enums.SystemOutGasStoragesEnum.Injection

    NetWithdrawal = plx_enums.SystemOutGasStoragesEnum.NetWithdrawal

    WithdrawalCost = plx_enums.SystemOutGasStoragesEnum.WithdrawalCost

    InjectionCost = plx_enums.SystemOutGasStoragesEnum.InjectionCost

    ProductionCost = plx_enums.SystemOutGasStoragesEnum.ProductionCost

    ShadowPrice = plx_enums.SystemOutGasStoragesEnum.ShadowPrice

    FOMCost = plx_enums.SystemOutGasStoragesEnum.FOMCost

    FixedCosts = plx_enums.SystemOutGasStoragesEnum.FixedCosts

    Units = plx_enums.SystemOutGasStoragesEnum.Units

    UnitsBuilt = plx_enums.SystemOutGasStoragesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutGasStoragesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutGasStoragesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutGasStoragesEnum.RetirementCost

    x = plx_enums.SystemOutGasStoragesEnum.x

    y = plx_enums.SystemOutGasStoragesEnum.y

    z = plx_enums.SystemOutGasStoragesEnum.z


class SystemOutGasTransportsEnum(Enum):
    Imports = plx_enums.SystemOutGasTransportsEnum.Imports

    Exports = plx_enums.SystemOutGasTransportsEnum.Exports

    Losses = plx_enums.SystemOutGasTransportsEnum.Losses

    ContractImports = plx_enums.SystemOutGasTransportsEnum.ContractImports

    SpotImports = plx_enums.SystemOutGasTransportsEnum.SpotImports

    ShippingCost = plx_enums.SystemOutGasTransportsEnum.ShippingCost

    x = plx_enums.SystemOutGasTransportsEnum.x

    y = plx_enums.SystemOutGasTransportsEnum.y

    z = plx_enums.SystemOutGasTransportsEnum.z


class SystemOutGasZonesEnum(Enum):
    Production = plx_enums.SystemOutGasZonesEnum.Production

    Demand = plx_enums.SystemOutGasZonesEnum.Demand

    Imports = plx_enums.SystemOutGasZonesEnum.Imports

    Exports = plx_enums.SystemOutGasZonesEnum.Exports

    NetInterchange = plx_enums.SystemOutGasZonesEnum.NetInterchange

    InitialVolume = plx_enums.SystemOutGasZonesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutGasZonesEnum.EndVolume

    ShortageHours = plx_enums.SystemOutGasZonesEnum.ShortageHours

    Shortage = plx_enums.SystemOutGasZonesEnum.Shortage

    ShortageCost = plx_enums.SystemOutGasZonesEnum.ShortageCost

    ExcessHours = plx_enums.SystemOutGasZonesEnum.ExcessHours

    Excess = plx_enums.SystemOutGasZonesEnum.Excess

    ExcessCost = plx_enums.SystemOutGasZonesEnum.ExcessCost

    NetDemand = plx_enums.SystemOutGasZonesEnum.NetDemand

    Cost = plx_enums.SystemOutGasZonesEnum.Cost

    PricePaid = plx_enums.SystemOutGasZonesEnum.PricePaid

    x = plx_enums.SystemOutGasZonesEnum.x

    y = plx_enums.SystemOutGasZonesEnum.y

    z = plx_enums.SystemOutGasZonesEnum.z


class SystemOutGeneratorsEnum(Enum):
    Generation = plx_enums.SystemOutGeneratorsEnum.Generation

    MinGeneration = plx_enums.SystemOutGeneratorsEnum.MinGeneration

    MaxGeneration = plx_enums.SystemOutGeneratorsEnum.MaxGeneration

    UnitsGenerating = plx_enums.SystemOutGeneratorsEnum.UnitsGenerating

    UnitsStarted = plx_enums.SystemOutGeneratorsEnum.UnitsStarted

    UnitsShutdown = plx_enums.SystemOutGeneratorsEnum.UnitsShutdown

    DispatchableCapacity = plx_enums.SystemOutGeneratorsEnum.DispatchableCapacity

    UndispatchedCapacity = plx_enums.SystemOutGeneratorsEnum.UndispatchedCapacity

    OperatingHours = plx_enums.SystemOutGeneratorsEnum.OperatingHours

    HoursUp = plx_enums.SystemOutGeneratorsEnum.HoursUp

    HoursDown = plx_enums.SystemOutGeneratorsEnum.HoursDown

    CapacityFactor = plx_enums.SystemOutGeneratorsEnum.CapacityFactor

    FuelOfftake = plx_enums.SystemOutGeneratorsEnum.FuelOfftake

    StartFuelOfftake = plx_enums.SystemOutGeneratorsEnum.StartFuelOfftake

    WasteHeat = plx_enums.SystemOutGeneratorsEnum.WasteHeat

    NoCostCapacity = plx_enums.SystemOutGeneratorsEnum.NoCostCapacity

    HoursCurtailed = plx_enums.SystemOutGeneratorsEnum.HoursCurtailed

    CapacityCurtailed = plx_enums.SystemOutGeneratorsEnum.CapacityCurtailed

    CurtailmentFactor = plx_enums.SystemOutGeneratorsEnum.CurtailmentFactor

    Ramp = plx_enums.SystemOutGeneratorsEnum.Ramp

    RampUp = plx_enums.SystemOutGeneratorsEnum.RampUp

    MinutesofRampUp = plx_enums.SystemOutGeneratorsEnum.MinutesofRampUp

    RampUpCost = plx_enums.SystemOutGeneratorsEnum.RampUpCost

    RampUpPrice = plx_enums.SystemOutGeneratorsEnum.RampUpPrice

    RampDown = plx_enums.SystemOutGeneratorsEnum.RampDown

    MinutesofRampDown = plx_enums.SystemOutGeneratorsEnum.MinutesofRampDown

    RampDownCost = plx_enums.SystemOutGeneratorsEnum.RampDownCost

    RampDownPrice = plx_enums.SystemOutGeneratorsEnum.RampDownPrice

    RampUpViolationHours = plx_enums.SystemOutGeneratorsEnum.RampUpViolationHours

    RampDownViolationHours = plx_enums.SystemOutGeneratorsEnum.RampDownViolationHours

    RampUpViolation = plx_enums.SystemOutGeneratorsEnum.RampUpViolation

    RampDownViolation = plx_enums.SystemOutGeneratorsEnum.RampDownViolation

    RampUpViolationCost = plx_enums.SystemOutGeneratorsEnum.RampUpViolationCost

    RampDownViolationCost = plx_enums.SystemOutGeneratorsEnum.RampDownViolationCost

    FixedLoadGeneration = plx_enums.SystemOutGeneratorsEnum.FixedLoadGeneration

    FixedLoadViolation = plx_enums.SystemOutGeneratorsEnum.FixedLoadViolation

    FixedLoadViolationHours = plx_enums.SystemOutGeneratorsEnum.FixedLoadViolationHours

    FixedLoadViolationCost = plx_enums.SystemOutGeneratorsEnum.FixedLoadViolationCost

    MinLoadGeneration = plx_enums.SystemOutGeneratorsEnum.MinLoadGeneration

    MinLoadViolation = plx_enums.SystemOutGeneratorsEnum.MinLoadViolation

    MinLoadViolationHours = plx_enums.SystemOutGeneratorsEnum.MinLoadViolationHours

    MinLoadViolationCost = plx_enums.SystemOutGeneratorsEnum.MinLoadViolationCost

    MaxEnergyViolation = plx_enums.SystemOutGeneratorsEnum.MaxEnergyViolation

    MaxEnergyViolationCost = plx_enums.SystemOutGeneratorsEnum.MaxEnergyViolationCost

    MinEnergyViolation = plx_enums.SystemOutGeneratorsEnum.MinEnergyViolation

    MinEnergyViolationCost = plx_enums.SystemOutGeneratorsEnum.MinEnergyViolationCost

    MaxStartsViolation = plx_enums.SystemOutGeneratorsEnum.MaxStartsViolation

    MaxStartsViolationCost = plx_enums.SystemOutGeneratorsEnum.MaxStartsViolationCost

    RaiseReserve = plx_enums.SystemOutGeneratorsEnum.RaiseReserve

    LowerReserve = plx_enums.SystemOutGeneratorsEnum.LowerReserve

    RegulationRaiseReserve = plx_enums.SystemOutGeneratorsEnum.RegulationRaiseReserve

    RegulationLowerReserve = plx_enums.SystemOutGeneratorsEnum.RegulationLowerReserve

    ReplacementReserve = plx_enums.SystemOutGeneratorsEnum.ReplacementReserve

    FlexibilityUp = plx_enums.SystemOutGeneratorsEnum.FlexibilityUp

    FlexibilityDown = plx_enums.SystemOutGeneratorsEnum.FlexibilityDown

    RampFlexibilityUp = plx_enums.SystemOutGeneratorsEnum.RampFlexibilityUp

    RampFlexibilityDown = plx_enums.SystemOutGeneratorsEnum.RampFlexibilityDown

    HoursatMinimum = plx_enums.SystemOutGeneratorsEnum.HoursatMinimum

    InflexibleGeneration = plx_enums.SystemOutGeneratorsEnum.InflexibleGeneration

    AuxiliaryUse = plx_enums.SystemOutGeneratorsEnum.AuxiliaryUse

    GenerationSentOut = plx_enums.SystemOutGeneratorsEnum.GenerationSentOut

    UnitsPumping = plx_enums.SystemOutGeneratorsEnum.UnitsPumping

    PumpUnitsStarted = plx_enums.SystemOutGeneratorsEnum.PumpUnitsStarted

    PumpLoad = plx_enums.SystemOutGeneratorsEnum.PumpLoad

    PumpOperatingHours = plx_enums.SystemOutGeneratorsEnum.PumpOperatingHours

    NetGeneration = plx_enums.SystemOutGeneratorsEnum.NetGeneration

    FixedPumpLoad = plx_enums.SystemOutGeneratorsEnum.FixedPumpLoad

    FixedPumpLoadViolation = plx_enums.SystemOutGeneratorsEnum.FixedPumpLoadViolation

    FixedPumpLoadViolationHours = plx_enums.SystemOutGeneratorsEnum.FixedPumpLoadViolationHours

    FixedPumpLoadViolationCost = plx_enums.SystemOutGeneratorsEnum.FixedPumpLoadViolationCost

    WaterRelease = plx_enums.SystemOutGeneratorsEnum.WaterRelease

    WaterPumped = plx_enums.SystemOutGeneratorsEnum.WaterPumped

    UnitsSyncCond = plx_enums.SystemOutGeneratorsEnum.UnitsSyncCond

    SyncCondLoad = plx_enums.SystemOutGeneratorsEnum.SyncCondLoad

    SyncCondOperatingHours = plx_enums.SystemOutGeneratorsEnum.SyncCondOperatingHours

    FuelPrice = plx_enums.SystemOutGeneratorsEnum.FuelPrice

    FuelCost = plx_enums.SystemOutGeneratorsEnum.FuelCost

    FuelTransportCost = plx_enums.SystemOutGeneratorsEnum.FuelTransportCost

    FuelTransitionCost = plx_enums.SystemOutGeneratorsEnum.FuelTransitionCost

    VOMCharge = plx_enums.SystemOutGeneratorsEnum.VOMCharge

    VOMCost = plx_enums.SystemOutGeneratorsEnum.VOMCost

    UoSCost = plx_enums.SystemOutGeneratorsEnum.UoSCost

    PumpCost = plx_enums.SystemOutGeneratorsEnum.PumpCost

    SyncCondCost = plx_enums.SystemOutGeneratorsEnum.SyncCondCost

    ReservesVOMCost = plx_enums.SystemOutGeneratorsEnum.ReservesVOMCost

    ReservesCost = plx_enums.SystemOutGeneratorsEnum.ReservesCost

    GenerationCost = plx_enums.SystemOutGeneratorsEnum.GenerationCost

    StartShutdownCost = plx_enums.SystemOutGeneratorsEnum.StartShutdownCost

    StartShutdownPenaltyCost = plx_enums.SystemOutGeneratorsEnum.StartShutdownPenaltyCost

    StartFuelCost = plx_enums.SystemOutGeneratorsEnum.StartFuelCost

    EmissionsCost = plx_enums.SystemOutGeneratorsEnum.EmissionsCost

    AbatementCost = plx_enums.SystemOutGeneratorsEnum.AbatementCost

    TotalGenerationCost = plx_enums.SystemOutGeneratorsEnum.TotalGenerationCost

    TotalSystemCost = plx_enums.SystemOutGeneratorsEnum.TotalSystemCost

    FOMCost = plx_enums.SystemOutGeneratorsEnum.FOMCost

    EquityCost = plx_enums.SystemOutGeneratorsEnum.EquityCost

    DebtCost = plx_enums.SystemOutGeneratorsEnum.DebtCost

    FixedCosts = plx_enums.SystemOutGeneratorsEnum.FixedCosts

    HeatRate = plx_enums.SystemOutGeneratorsEnum.HeatRate

    MarginalHeatRate = plx_enums.SystemOutGeneratorsEnum.MarginalHeatRate

    AverageHeatRate = plx_enums.SystemOutGeneratorsEnum.AverageHeatRate

    Efficiency = plx_enums.SystemOutGeneratorsEnum.Efficiency

    MarginalFuelCost = plx_enums.SystemOutGeneratorsEnum.MarginalFuelCost

    SRMC = plx_enums.SystemOutGeneratorsEnum.SRMC

    AverageCost = plx_enums.SystemOutGeneratorsEnum.AverageCost

    AverageTotalCost = plx_enums.SystemOutGeneratorsEnum.AverageTotalCost

    OfferBase = plx_enums.SystemOutGeneratorsEnum.OfferBase

    OfferNoLoadCost = plx_enums.SystemOutGeneratorsEnum.OfferNoLoadCost

    OfferQuantity = plx_enums.SystemOutGeneratorsEnum.OfferQuantity

    OfferPrice = plx_enums.SystemOutGeneratorsEnum.OfferPrice

    CostPrice = plx_enums.SystemOutGeneratorsEnum.CostPrice

    Markup = plx_enums.SystemOutGeneratorsEnum.Markup

    BidCostMarkup = plx_enums.SystemOutGeneratorsEnum.BidCostMarkup

    OfferCleared = plx_enums.SystemOutGeneratorsEnum.OfferCleared

    ClearedOfferPrice = plx_enums.SystemOutGeneratorsEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.SystemOutGeneratorsEnum.ClearedOfferCost

    PriceReceived = plx_enums.SystemOutGeneratorsEnum.PriceReceived

    PumpBidBase = plx_enums.SystemOutGeneratorsEnum.PumpBidBase

    PumpBidQuantity = plx_enums.SystemOutGeneratorsEnum.PumpBidQuantity

    PumpBidPrice = plx_enums.SystemOutGeneratorsEnum.PumpBidPrice

    PumpBidCleared = plx_enums.SystemOutGeneratorsEnum.PumpBidCleared

    ClearedPumpBidPrice = plx_enums.SystemOutGeneratorsEnum.ClearedPumpBidPrice

    ClearedPumpBidCost = plx_enums.SystemOutGeneratorsEnum.ClearedPumpBidCost

    PumpPricePaid = plx_enums.SystemOutGeneratorsEnum.PumpPricePaid

    SyncCondPricePaid = plx_enums.SystemOutGeneratorsEnum.SyncCondPricePaid

    ClearedReserveOfferCost = plx_enums.SystemOutGeneratorsEnum.ClearedReserveOfferCost

    SparkSpread = plx_enums.SystemOutGeneratorsEnum.SparkSpread

    CleanSparkSpread = plx_enums.SystemOutGeneratorsEnum.CleanSparkSpread

    PoolRevenue = plx_enums.SystemOutGeneratorsEnum.PoolRevenue

    ReservesRevenue = plx_enums.SystemOutGeneratorsEnum.ReservesRevenue

    NetReservesRevenue = plx_enums.SystemOutGeneratorsEnum.NetReservesRevenue

    HeatMarketRevenue = plx_enums.SystemOutGeneratorsEnum.HeatMarketRevenue

    NetRevenue = plx_enums.SystemOutGeneratorsEnum.NetRevenue

    NetProfit = plx_enums.SystemOutGeneratorsEnum.NetProfit

    ShadowGeneration = plx_enums.SystemOutGeneratorsEnum.ShadowGeneration

    ShadowPoolRevenue = plx_enums.SystemOutGeneratorsEnum.ShadowPoolRevenue

    ShadowPriceReceived = plx_enums.SystemOutGeneratorsEnum.ShadowPriceReceived

    MonopolyRent = plx_enums.SystemOutGeneratorsEnum.MonopolyRent

    StrategicShadowPrice = plx_enums.SystemOutGeneratorsEnum.StrategicShadowPrice

    ScheduledGeneration = plx_enums.SystemOutGeneratorsEnum.ScheduledGeneration

    ScheduledRevenue = plx_enums.SystemOutGeneratorsEnum.ScheduledRevenue

    ConstrainedOnRevenue = plx_enums.SystemOutGeneratorsEnum.ConstrainedOnRevenue

    ConstrainedOffRevenue = plx_enums.SystemOutGeneratorsEnum.ConstrainedOffRevenue

    ScheduledGenerationCost = plx_enums.SystemOutGeneratorsEnum.ScheduledGenerationCost

    ScheduledOfferCost = plx_enums.SystemOutGeneratorsEnum.ScheduledOfferCost

    ScheduledStartShutdownCost = plx_enums.SystemOutGeneratorsEnum.ScheduledStartShutdownCost

    CHPGeneration = plx_enums.SystemOutGeneratorsEnum.CHPGeneration

    CondenseModeGeneration = plx_enums.SystemOutGeneratorsEnum.CondenseModeGeneration

    HeatProduction = plx_enums.SystemOutGeneratorsEnum.HeatProduction

    CHPHeatProduction = plx_enums.SystemOutGeneratorsEnum.CHPHeatProduction

    BoilerHeatProduction = plx_enums.SystemOutGeneratorsEnum.BoilerHeatProduction

    HeatFuelOfftake = plx_enums.SystemOutGeneratorsEnum.HeatFuelOfftake

    CHPPowerFuelOfftake = plx_enums.SystemOutGeneratorsEnum.CHPPowerFuelOfftake

    CHPHeatFuelOfftake = plx_enums.SystemOutGeneratorsEnum.CHPHeatFuelOfftake

    CHPHeatSurrogateFuelOfftake = plx_enums.SystemOutGeneratorsEnum.CHPHeatSurrogateFuelOfftake

    BoilerFuelOfftake = plx_enums.SystemOutGeneratorsEnum.BoilerFuelOfftake

    HeatProductionCost = plx_enums.SystemOutGeneratorsEnum.HeatProductionCost

    HeatRevenue = plx_enums.SystemOutGeneratorsEnum.HeatRevenue

    MaxHeat = plx_enums.SystemOutGeneratorsEnum.MaxHeat

    MinHeat = plx_enums.SystemOutGeneratorsEnum.MinHeat

    OpeningHeat = plx_enums.SystemOutGeneratorsEnum.OpeningHeat

    ClosingHeat = plx_enums.SystemOutGeneratorsEnum.ClosingHeat

    HeatWithdrawal = plx_enums.SystemOutGeneratorsEnum.HeatWithdrawal

    HeatInjection = plx_enums.SystemOutGeneratorsEnum.HeatInjection

    NetHeatWithdrawal = plx_enums.SystemOutGeneratorsEnum.NetHeatWithdrawal

    HeatLoss = plx_enums.SystemOutGeneratorsEnum.HeatLoss

    HeatWithdrawalCost = plx_enums.SystemOutGeneratorsEnum.HeatWithdrawalCost

    HeatInjectionCost = plx_enums.SystemOutGeneratorsEnum.HeatInjectionCost

    HeatShadowPrice = plx_enums.SystemOutGeneratorsEnum.HeatShadowPrice

    WaterOfftake = plx_enums.SystemOutGeneratorsEnum.WaterOfftake

    WaterConsumption = plx_enums.SystemOutGeneratorsEnum.WaterConsumption

    WaterCost = plx_enums.SystemOutGeneratorsEnum.WaterCost

    WaterPricePaid = plx_enums.SystemOutGeneratorsEnum.WaterPricePaid

    Units = plx_enums.SystemOutGeneratorsEnum.Units

    MaxCapacity = plx_enums.SystemOutGeneratorsEnum.MaxCapacity

    InstalledCapacity = plx_enums.SystemOutGeneratorsEnum.InstalledCapacity

    Rating = plx_enums.SystemOutGeneratorsEnum.Rating

    RawRating = plx_enums.SystemOutGeneratorsEnum.RawRating

    RatedCapacity = plx_enums.SystemOutGeneratorsEnum.RatedCapacity

    FirmCapacity = plx_enums.SystemOutGeneratorsEnum.FirmCapacity

    CapacityReserves = plx_enums.SystemOutGeneratorsEnum.CapacityReserves

    UnitsOut = plx_enums.SystemOutGeneratorsEnum.UnitsOut

    Maintenance = plx_enums.SystemOutGeneratorsEnum.Maintenance

    DiscreteMaintenance = plx_enums.SystemOutGeneratorsEnum.DiscreteMaintenance

    DistributedMaintenance = plx_enums.SystemOutGeneratorsEnum.DistributedMaintenance

    MaintenanceHours = plx_enums.SystemOutGeneratorsEnum.MaintenanceHours

    MaintenanceRate = plx_enums.SystemOutGeneratorsEnum.MaintenanceRate

    ForcedOutage = plx_enums.SystemOutGeneratorsEnum.ForcedOutage

    ForcedOutageHours = plx_enums.SystemOutGeneratorsEnum.ForcedOutageHours

    ForcedOutageRate = plx_enums.SystemOutGeneratorsEnum.ForcedOutageRate

    OperatingorForcedOutageHours = plx_enums.SystemOutGeneratorsEnum.OperatingorForcedOutageHours

    AvailableCapacity = plx_enums.SystemOutGeneratorsEnum.AvailableCapacity

    ServiceFactor = plx_enums.SystemOutGeneratorsEnum.ServiceFactor

    UnitsBuilt = plx_enums.SystemOutGeneratorsEnum.UnitsBuilt

    UnitsRetired = plx_enums.SystemOutGeneratorsEnum.UnitsRetired

    CapacityBuilt = plx_enums.SystemOutGeneratorsEnum.CapacityBuilt

    CapacityRetired = plx_enums.SystemOutGeneratorsEnum.CapacityRetired

    NetNewCapacity = plx_enums.SystemOutGeneratorsEnum.NetNewCapacity

    CapacityPrice = plx_enums.SystemOutGeneratorsEnum.CapacityPrice

    CapacityRevenue = plx_enums.SystemOutGeneratorsEnum.CapacityRevenue

    BuildCost = plx_enums.SystemOutGeneratorsEnum.BuildCost

    AnnualizedBuildCost = plx_enums.SystemOutGeneratorsEnum.AnnualizedBuildCost

    TotalCost = plx_enums.SystemOutGeneratorsEnum.TotalCost

    LevelizedCost = plx_enums.SystemOutGeneratorsEnum.LevelizedCost

    Age = plx_enums.SystemOutGeneratorsEnum.Age

    RetirementCost = plx_enums.SystemOutGeneratorsEnum.RetirementCost

    ShadowCapacityBuilt = plx_enums.SystemOutGeneratorsEnum.ShadowCapacityBuilt

    x = plx_enums.SystemOutGeneratorsEnum.x

    y = plx_enums.SystemOutGeneratorsEnum.y

    z = plx_enums.SystemOutGeneratorsEnum.z


class SystemOutHeatNodesEnum(Enum):
    HeatWithdrawal = plx_enums.SystemOutHeatNodesEnum.HeatWithdrawal

    HeatInjection = plx_enums.SystemOutHeatNodesEnum.HeatInjection

    x = plx_enums.SystemOutHeatNodesEnum.x

    y = plx_enums.SystemOutHeatNodesEnum.y

    z = plx_enums.SystemOutHeatNodesEnum.z


class SystemOutHeatPlantsEnum(Enum):
    HeatProduction = plx_enums.SystemOutHeatPlantsEnum.HeatProduction

    HeatProductionCost = plx_enums.SystemOutHeatPlantsEnum.HeatProductionCost

    VOMCost = plx_enums.SystemOutHeatPlantsEnum.VOMCost

    StartShutdownCost = plx_enums.SystemOutHeatPlantsEnum.StartShutdownCost

    StartFuelCost = plx_enums.SystemOutHeatPlantsEnum.StartFuelCost

    FuelOfftake = plx_enums.SystemOutHeatPlantsEnum.FuelOfftake

    StartFuelOfftake = plx_enums.SystemOutHeatPlantsEnum.StartFuelOfftake

    ElectricalUsage = plx_enums.SystemOutHeatPlantsEnum.ElectricalUsage

    UnitsProducingHeat = plx_enums.SystemOutHeatPlantsEnum.UnitsProducingHeat

    Ramp = plx_enums.SystemOutHeatPlantsEnum.Ramp

    RampUp = plx_enums.SystemOutHeatPlantsEnum.RampUp

    RampDown = plx_enums.SystemOutHeatPlantsEnum.RampDown

    OperatingHours = plx_enums.SystemOutHeatPlantsEnum.OperatingHours

    Efficiency = plx_enums.SystemOutHeatPlantsEnum.Efficiency

    MarginalHeatRate = plx_enums.SystemOutHeatPlantsEnum.MarginalHeatRate

    AverageHeatRate = plx_enums.SystemOutHeatPlantsEnum.AverageHeatRate

    SRMC = plx_enums.SystemOutHeatPlantsEnum.SRMC

    FOMCost = plx_enums.SystemOutHeatPlantsEnum.FOMCost

    InstalledCapacity = plx_enums.SystemOutHeatPlantsEnum.InstalledCapacity

    UnitsBuilt = plx_enums.SystemOutHeatPlantsEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutHeatPlantsEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutHeatPlantsEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutHeatPlantsEnum.RetirementCost

    x = plx_enums.SystemOutHeatPlantsEnum.x

    y = plx_enums.SystemOutHeatPlantsEnum.y

    z = plx_enums.SystemOutHeatPlantsEnum.z


class SystemOutHubsEnum(Enum):
    Price = plx_enums.SystemOutHubsEnum.Price

    CustomerLoad = plx_enums.SystemOutHubsEnum.CustomerLoad

    NetGeneration = plx_enums.SystemOutHubsEnum.NetGeneration

    CosttoLoad = plx_enums.SystemOutHubsEnum.CosttoLoad

    GeneratorPoolRevenue = plx_enums.SystemOutHubsEnum.GeneratorPoolRevenue

    LoadweightedPrice = plx_enums.SystemOutHubsEnum.LoadweightedPrice

    GenerationweightedPrice = plx_enums.SystemOutHubsEnum.GenerationweightedPrice

    MarginalLossCharge = plx_enums.SystemOutHubsEnum.MarginalLossCharge

    EnergyCharge = plx_enums.SystemOutHubsEnum.EnergyCharge

    CongestionCharge = plx_enums.SystemOutHubsEnum.CongestionCharge

    x = plx_enums.SystemOutHubsEnum.x

    y = plx_enums.SystemOutHubsEnum.y

    z = plx_enums.SystemOutHubsEnum.z


class SystemOutInterfacesEnum(Enum):
    Flow = plx_enums.SystemOutInterfacesEnum.Flow

    FlowBack = plx_enums.SystemOutInterfacesEnum.FlowBack

    NetFlow = plx_enums.SystemOutInterfacesEnum.NetFlow

    ExportLimit = plx_enums.SystemOutInterfacesEnum.ExportLimit

    ImportLimit = plx_enums.SystemOutInterfacesEnum.ImportLimit

    Loading = plx_enums.SystemOutInterfacesEnum.Loading

    LoadingBack = plx_enums.SystemOutInterfacesEnum.LoadingBack

    HoursCongested = plx_enums.SystemOutInterfacesEnum.HoursCongested

    HoursCongestedBack = plx_enums.SystemOutInterfacesEnum.HoursCongestedBack

    ShadowPrice = plx_enums.SystemOutInterfacesEnum.ShadowPrice

    ShadowPriceBack = plx_enums.SystemOutInterfacesEnum.ShadowPriceBack

    Rental = plx_enums.SystemOutInterfacesEnum.Rental

    Violation = plx_enums.SystemOutInterfacesEnum.Violation

    ViolationBack = plx_enums.SystemOutInterfacesEnum.ViolationBack

    Ramp = plx_enums.SystemOutInterfacesEnum.Ramp

    RampCost = plx_enums.SystemOutInterfacesEnum.RampCost

    MaxFlow = plx_enums.SystemOutInterfacesEnum.MaxFlow

    MinFlow = plx_enums.SystemOutInterfacesEnum.MinFlow

    FixedFlow = plx_enums.SystemOutInterfacesEnum.FixedFlow

    FixedFlowViolation = plx_enums.SystemOutInterfacesEnum.FixedFlowViolation

    FixedFlowViolationHours = plx_enums.SystemOutInterfacesEnum.FixedFlowViolationHours

    FixedFlowViolationCost = plx_enums.SystemOutInterfacesEnum.FixedFlowViolationCost

    OfferBase = plx_enums.SystemOutInterfacesEnum.OfferBase

    OfferQuantity = plx_enums.SystemOutInterfacesEnum.OfferQuantity

    OfferPrice = plx_enums.SystemOutInterfacesEnum.OfferPrice

    OfferQuantityBack = plx_enums.SystemOutInterfacesEnum.OfferQuantityBack

    OfferPriceBack = plx_enums.SystemOutInterfacesEnum.OfferPriceBack

    OfferCleared = plx_enums.SystemOutInterfacesEnum.OfferCleared

    OfferClearedBack = plx_enums.SystemOutInterfacesEnum.OfferClearedBack

    ClearedOfferPrice = plx_enums.SystemOutInterfacesEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.SystemOutInterfacesEnum.ClearedOfferCost

    AvailableTransferCapability = plx_enums.SystemOutInterfacesEnum.AvailableTransferCapability

    AvailableTransferCapabilityBack = plx_enums.SystemOutInterfacesEnum.AvailableTransferCapabilityBack

    FirmCapacity = plx_enums.SystemOutInterfacesEnum.FirmCapacity

    CapacityReserves = plx_enums.SystemOutInterfacesEnum.CapacityReserves

    CapacityBuilt = plx_enums.SystemOutInterfacesEnum.CapacityBuilt

    ExpansionCost = plx_enums.SystemOutInterfacesEnum.ExpansionCost

    x = plx_enums.SystemOutInterfacesEnum.x

    y = plx_enums.SystemOutInterfacesEnum.y

    z = plx_enums.SystemOutInterfacesEnum.z


class SystemOutLinesEnum(Enum):
    Flow = plx_enums.SystemOutLinesEnum.Flow

    FlowBack = plx_enums.SystemOutLinesEnum.FlowBack

    NetFlow = plx_enums.SystemOutLinesEnum.NetFlow

    ExportLimit = plx_enums.SystemOutLinesEnum.ExportLimit

    ImportLimit = plx_enums.SystemOutLinesEnum.ImportLimit

    Loading = plx_enums.SystemOutLinesEnum.Loading

    LoadingBack = plx_enums.SystemOutLinesEnum.LoadingBack

    HoursCongested = plx_enums.SystemOutLinesEnum.HoursCongested

    HoursCongestedBack = plx_enums.SystemOutLinesEnum.HoursCongestedBack

    ShadowPrice = plx_enums.SystemOutLinesEnum.ShadowPrice

    ShadowPriceBack = plx_enums.SystemOutLinesEnum.ShadowPriceBack

    ViolationHours = plx_enums.SystemOutLinesEnum.ViolationHours

    ViolationBackHours = plx_enums.SystemOutLinesEnum.ViolationBackHours

    Violation = plx_enums.SystemOutLinesEnum.Violation

    ViolationBack = plx_enums.SystemOutLinesEnum.ViolationBack

    ViolationCost = plx_enums.SystemOutLinesEnum.ViolationCost

    ViolationCostBack = plx_enums.SystemOutLinesEnum.ViolationCostBack

    Ramp = plx_enums.SystemOutLinesEnum.Ramp

    RampCost = plx_enums.SystemOutLinesEnum.RampCost

    MaxFlow = plx_enums.SystemOutLinesEnum.MaxFlow

    MinFlow = plx_enums.SystemOutLinesEnum.MinFlow

    FixedFlow = plx_enums.SystemOutLinesEnum.FixedFlow

    FixedFlowViolation = plx_enums.SystemOutLinesEnum.FixedFlowViolation

    FixedFlowViolationHours = plx_enums.SystemOutLinesEnum.FixedFlowViolationHours

    FixedFlowViolationCost = plx_enums.SystemOutLinesEnum.FixedFlowViolationCost

    ExportCost = plx_enums.SystemOutLinesEnum.ExportCost

    ImportCost = plx_enums.SystemOutLinesEnum.ImportCost

    ExportRevenue = plx_enums.SystemOutLinesEnum.ExportRevenue

    ImportRevenue = plx_enums.SystemOutLinesEnum.ImportRevenue

    Rental = plx_enums.SystemOutLinesEnum.Rental

    RentalBack = plx_enums.SystemOutLinesEnum.RentalBack

    WheelingCost = plx_enums.SystemOutLinesEnum.WheelingCost

    WheelingCostBack = plx_enums.SystemOutLinesEnum.WheelingCostBack

    Loss = plx_enums.SystemOutLinesEnum.Loss

    LossBack = plx_enums.SystemOutLinesEnum.LossBack

    MarginalLoss = plx_enums.SystemOutLinesEnum.MarginalLoss

    MarginalLossFactor = plx_enums.SystemOutLinesEnum.MarginalLossFactor

    Voltage = plx_enums.SystemOutLinesEnum.Voltage

    OfferBase = plx_enums.SystemOutLinesEnum.OfferBase

    OfferQuantity = plx_enums.SystemOutLinesEnum.OfferQuantity

    OfferPrice = plx_enums.SystemOutLinesEnum.OfferPrice

    OfferQuantityBack = plx_enums.SystemOutLinesEnum.OfferQuantityBack

    OfferPriceBack = plx_enums.SystemOutLinesEnum.OfferPriceBack

    OfferCleared = plx_enums.SystemOutLinesEnum.OfferCleared

    OfferClearedBack = plx_enums.SystemOutLinesEnum.OfferClearedBack

    ClearedOfferPrice = plx_enums.SystemOutLinesEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.SystemOutLinesEnum.ClearedOfferCost

    FOMCost = plx_enums.SystemOutLinesEnum.FOMCost

    EquityCost = plx_enums.SystemOutLinesEnum.EquityCost

    DebtCost = plx_enums.SystemOutLinesEnum.DebtCost

    NetProfit = plx_enums.SystemOutLinesEnum.NetProfit

    Units = plx_enums.SystemOutLinesEnum.Units

    FirmCapacity = plx_enums.SystemOutLinesEnum.FirmCapacity

    CapacityReserves = plx_enums.SystemOutLinesEnum.CapacityReserves

    UnitsOut = plx_enums.SystemOutLinesEnum.UnitsOut

    Maintenance = plx_enums.SystemOutLinesEnum.Maintenance

    MaintenanceBack = plx_enums.SystemOutLinesEnum.MaintenanceBack

    DiscreteMaintenance = plx_enums.SystemOutLinesEnum.DiscreteMaintenance

    DiscreteMaintenanceBack = plx_enums.SystemOutLinesEnum.DiscreteMaintenanceBack

    DistributedMaintenance = plx_enums.SystemOutLinesEnum.DistributedMaintenance

    DistributedMaintenanceBack = plx_enums.SystemOutLinesEnum.DistributedMaintenanceBack

    MaintenanceRate = plx_enums.SystemOutLinesEnum.MaintenanceRate

    ForcedOutage = plx_enums.SystemOutLinesEnum.ForcedOutage

    ForcedOutageRate = plx_enums.SystemOutLinesEnum.ForcedOutageRate

    ServiceFactor = plx_enums.SystemOutLinesEnum.ServiceFactor

    AvailableTransferCapability = plx_enums.SystemOutLinesEnum.AvailableTransferCapability

    AvailableTransferCapabilityBack = plx_enums.SystemOutLinesEnum.AvailableTransferCapabilityBack

    UnitsBuilt = plx_enums.SystemOutLinesEnum.UnitsBuilt

    UnitsRetired = plx_enums.SystemOutLinesEnum.UnitsRetired

    ExportCapacityBuilt = plx_enums.SystemOutLinesEnum.ExportCapacityBuilt

    ImportCapacityBuilt = plx_enums.SystemOutLinesEnum.ImportCapacityBuilt

    ExportCapacityRetired = plx_enums.SystemOutLinesEnum.ExportCapacityRetired

    ImportCapacityRetired = plx_enums.SystemOutLinesEnum.ImportCapacityRetired

    BuildCost = plx_enums.SystemOutLinesEnum.BuildCost

    RetirementCost = plx_enums.SystemOutLinesEnum.RetirementCost

    x = plx_enums.SystemOutLinesEnum.x

    y = plx_enums.SystemOutLinesEnum.y

    z = plx_enums.SystemOutLinesEnum.z


class SystemOutMaintenancesEnum(Enum):
    StartDate = plx_enums.SystemOutMaintenancesEnum.StartDate

    HoursActive = plx_enums.SystemOutMaintenancesEnum.HoursActive

    Duration = plx_enums.SystemOutMaintenancesEnum.Duration

    Cost = plx_enums.SystemOutMaintenancesEnum.Cost

    Crew = plx_enums.SystemOutMaintenancesEnum.Crew

    Equipment = plx_enums.SystemOutMaintenancesEnum.Equipment

    Outage = plx_enums.SystemOutMaintenancesEnum.Outage

    PenaltyCost = plx_enums.SystemOutMaintenancesEnum.PenaltyCost

    x = plx_enums.SystemOutMaintenancesEnum.x

    y = plx_enums.SystemOutMaintenancesEnum.y

    z = plx_enums.SystemOutMaintenancesEnum.z


class SystemOutMarketsEnum(Enum):
    Sales = plx_enums.SystemOutMarketsEnum.Sales

    Purchases = plx_enums.SystemOutMarketsEnum.Purchases

    NetSales = plx_enums.SystemOutMarketsEnum.NetSales

    NetPurchases = plx_enums.SystemOutMarketsEnum.NetPurchases

    Price = plx_enums.SystemOutMarketsEnum.Price

    Revenue = plx_enums.SystemOutMarketsEnum.Revenue

    Cost = plx_enums.SystemOutMarketsEnum.Cost

    NetRevenue = plx_enums.SystemOutMarketsEnum.NetRevenue

    NetCost = plx_enums.SystemOutMarketsEnum.NetCost

    TotalCost = plx_enums.SystemOutMarketsEnum.TotalCost

    PriceReceived = plx_enums.SystemOutMarketsEnum.PriceReceived

    PricePaid = plx_enums.SystemOutMarketsEnum.PricePaid

    NaturalRevenue = plx_enums.SystemOutMarketsEnum.NaturalRevenue

    NaturalCost = plx_enums.SystemOutMarketsEnum.NaturalCost

    FirmCapacity = plx_enums.SystemOutMarketsEnum.FirmCapacity

    LoadObligation = plx_enums.SystemOutMarketsEnum.LoadObligation

    x = plx_enums.SystemOutMarketsEnum.x

    y = plx_enums.SystemOutMarketsEnum.y

    z = plx_enums.SystemOutMarketsEnum.z


class SystemOutNodesEnum(Enum):
    Load = plx_enums.SystemOutNodesEnum.Load

    NativeLoad = plx_enums.SystemOutNodesEnum.NativeLoad

    FixedLoad = plx_enums.SystemOutNodesEnum.FixedLoad

    FixedGeneration = plx_enums.SystemOutNodesEnum.FixedGeneration

    Generation = plx_enums.SystemOutNodesEnum.Generation

    GeneratorAuxiliaryUse = plx_enums.SystemOutNodesEnum.GeneratorAuxiliaryUse

    GenerationSentOut = plx_enums.SystemOutNodesEnum.GenerationSentOut

    PumpLoad = plx_enums.SystemOutNodesEnum.PumpLoad

    PurchaserLoad = plx_enums.SystemOutNodesEnum.PurchaserLoad

    NetContractLoad = plx_enums.SystemOutNodesEnum.NetContractLoad

    NetMarketSales = plx_enums.SystemOutNodesEnum.NetMarketSales

    DemandCurtailed = plx_enums.SystemOutNodesEnum.DemandCurtailed

    DSPBidQuantity = plx_enums.SystemOutNodesEnum.DSPBidQuantity

    DSPBidPrice = plx_enums.SystemOutNodesEnum.DSPBidPrice

    DSPBidCleared = plx_enums.SystemOutNodesEnum.DSPBidCleared

    ClearedDSPBidPrice = plx_enums.SystemOutNodesEnum.ClearedDSPBidPrice

    ClearedDSPBidCost = plx_enums.SystemOutNodesEnum.ClearedDSPBidCost

    CustomerLoad = plx_enums.SystemOutNodesEnum.CustomerLoad

    Imports = plx_enums.SystemOutNodesEnum.Imports

    Exports = plx_enums.SystemOutNodesEnum.Exports

    NetDCExport = plx_enums.SystemOutNodesEnum.NetDCExport

    NetInjection = plx_enums.SystemOutNodesEnum.NetInjection

    UnservedEnergy = plx_enums.SystemOutNodesEnum.UnservedEnergy

    DumpEnergy = plx_enums.SystemOutNodesEnum.DumpEnergy

    Losses = plx_enums.SystemOutNodesEnum.Losses

    Flow = plx_enums.SystemOutNodesEnum.Flow

    Price = plx_enums.SystemOutNodesEnum.Price

    EnergyCharge = plx_enums.SystemOutNodesEnum.EnergyCharge

    CongestionCharge = plx_enums.SystemOutNodesEnum.CongestionCharge

    MarginalLossCharge = plx_enums.SystemOutNodesEnum.MarginalLossCharge

    MarginalLossFactor = plx_enums.SystemOutNodesEnum.MarginalLossFactor

    Voltage = plx_enums.SystemOutNodesEnum.Voltage

    PhaseAngle = plx_enums.SystemOutNodesEnum.PhaseAngle

    PeakLoad = plx_enums.SystemOutNodesEnum.PeakLoad

    GenerationCapacity = plx_enums.SystemOutNodesEnum.GenerationCapacity

    FirmGenerationCapacity = plx_enums.SystemOutNodesEnum.FirmGenerationCapacity

    CurtailableLoad = plx_enums.SystemOutNodesEnum.CurtailableLoad

    ContractGenerationCapacity = plx_enums.SystemOutNodesEnum.ContractGenerationCapacity

    ContractLoadObligation = plx_enums.SystemOutNodesEnum.ContractLoadObligation

    ImportCapacity = plx_enums.SystemOutNodesEnum.ImportCapacity

    ExportCapacity = plx_enums.SystemOutNodesEnum.ExportCapacity

    NetCapacityInterchange = plx_enums.SystemOutNodesEnum.NetCapacityInterchange

    MinCapacityReserves = plx_enums.SystemOutNodesEnum.MinCapacityReserves

    CapacityReserves = plx_enums.SystemOutNodesEnum.CapacityReserves

    MinLoad = plx_enums.SystemOutNodesEnum.MinLoad

    DiscreteMaintenance = plx_enums.SystemOutNodesEnum.DiscreteMaintenance

    DistributedMaintenance = plx_enums.SystemOutNodesEnum.DistributedMaintenance

    MaintenanceFactor = plx_enums.SystemOutNodesEnum.MaintenanceFactor

    EENS = plx_enums.SystemOutNodesEnum.EENS

    EDNS = plx_enums.SystemOutNodesEnum.EDNS

    LOLE = plx_enums.SystemOutNodesEnum.LOLE

    LOLP = plx_enums.SystemOutNodesEnum.LOLP

    x = plx_enums.SystemOutNodesEnum.x

    y = plx_enums.SystemOutNodesEnum.y

    z = plx_enums.SystemOutNodesEnum.z


class SystemOutPhysicalContractsEnum(Enum):
    Generation = plx_enums.SystemOutPhysicalContractsEnum.Generation

    Load = plx_enums.SystemOutPhysicalContractsEnum.Load

    NetGeneration = plx_enums.SystemOutPhysicalContractsEnum.NetGeneration

    CapacityFactor = plx_enums.SystemOutPhysicalContractsEnum.CapacityFactor

    LoadFactor = plx_enums.SystemOutPhysicalContractsEnum.LoadFactor

    PriceReceived = plx_enums.SystemOutPhysicalContractsEnum.PriceReceived

    PricePaid = plx_enums.SystemOutPhysicalContractsEnum.PricePaid

    GenerationCost = plx_enums.SystemOutPhysicalContractsEnum.GenerationCost

    LoadRevenue = plx_enums.SystemOutPhysicalContractsEnum.LoadRevenue

    NetGenerationCost = plx_enums.SystemOutPhysicalContractsEnum.NetGenerationCost

    GenerationRevenue = plx_enums.SystemOutPhysicalContractsEnum.GenerationRevenue

    CosttoLoad = plx_enums.SystemOutPhysicalContractsEnum.CosttoLoad

    NetGenerationRevenue = plx_enums.SystemOutPhysicalContractsEnum.NetGenerationRevenue

    FixedCost = plx_enums.SystemOutPhysicalContractsEnum.FixedCost

    GenerationCapacity = plx_enums.SystemOutPhysicalContractsEnum.GenerationCapacity

    LoadObligation = plx_enums.SystemOutPhysicalContractsEnum.LoadObligation

    x = plx_enums.SystemOutPhysicalContractsEnum.x

    y = plx_enums.SystemOutPhysicalContractsEnum.y

    z = plx_enums.SystemOutPhysicalContractsEnum.z


class SystemOutPurchasersEnum(Enum):
    Load = plx_enums.SystemOutPurchasersEnum.Load

    PricePaid = plx_enums.SystemOutPurchasersEnum.PricePaid

    CosttoLoad = plx_enums.SystemOutPurchasersEnum.CosttoLoad

    BidQuantity = plx_enums.SystemOutPurchasersEnum.BidQuantity

    BidPrice = plx_enums.SystemOutPurchasersEnum.BidPrice

    BidCleared = plx_enums.SystemOutPurchasersEnum.BidCleared

    ClearedBidPrice = plx_enums.SystemOutPurchasersEnum.ClearedBidPrice

    ClearedBidValue = plx_enums.SystemOutPurchasersEnum.ClearedBidValue

    LoadFactor = plx_enums.SystemOutPurchasersEnum.LoadFactor

    MaxEnergyViolation = plx_enums.SystemOutPurchasersEnum.MaxEnergyViolation

    MaxEnergyViolationCost = plx_enums.SystemOutPurchasersEnum.MaxEnergyViolationCost

    MinEnergyViolation = plx_enums.SystemOutPurchasersEnum.MinEnergyViolation

    MinEnergyViolationCost = plx_enums.SystemOutPurchasersEnum.MinEnergyViolationCost

    ClearedReserveOfferCost = plx_enums.SystemOutPurchasersEnum.ClearedReserveOfferCost

    ReservesRevenue = plx_enums.SystemOutPurchasersEnum.ReservesRevenue

    LoadObligation = plx_enums.SystemOutPurchasersEnum.LoadObligation

    x = plx_enums.SystemOutPurchasersEnum.x

    y = plx_enums.SystemOutPurchasersEnum.y

    z = plx_enums.SystemOutPurchasersEnum.z


class SystemOutRSIsEnum(Enum):
    RSI = plx_enums.SystemOutRSIsEnum.RSI

    UtilityGeneration = plx_enums.SystemOutRSIsEnum.UtilityGeneration

    UtilityAvailableCapacity = plx_enums.SystemOutRSIsEnum.UtilityAvailableCapacity

    NonUtilityGeneration = plx_enums.SystemOutRSIsEnum.NonUtilityGeneration

    NonUtilityAvailableCapacity = plx_enums.SystemOutRSIsEnum.NonUtilityAvailableCapacity

    NonUtilityContractVolume = plx_enums.SystemOutRSIsEnum.NonUtilityContractVolume

    TotalInternalCapacity = plx_enums.SystemOutRSIsEnum.TotalInternalCapacity

    TotalImportCapacity = plx_enums.SystemOutRSIsEnum.TotalImportCapacity

    TotalSupplyCapacity = plx_enums.SystemOutRSIsEnum.TotalSupplyCapacity

    LargestSuppliersCapacity = plx_enums.SystemOutRSIsEnum.LargestSuppliersCapacity

    ImportCapacity = plx_enums.SystemOutRSIsEnum.ImportCapacity

    Demand = plx_enums.SystemOutRSIsEnum.Demand

    LernerIndex = plx_enums.SystemOutRSIsEnum.LernerIndex

    BoundedLernerIndex = plx_enums.SystemOutRSIsEnum.BoundedLernerIndex

    BidCostMarkup = plx_enums.SystemOutRSIsEnum.BidCostMarkup

    PriceCostMarkup = plx_enums.SystemOutRSIsEnum.PriceCostMarkup

    LoadUnhedged = plx_enums.SystemOutRSIsEnum.LoadUnhedged

    LoadCapacityRatio = plx_enums.SystemOutRSIsEnum.LoadCapacityRatio

    CapacityFactor = plx_enums.SystemOutRSIsEnum.CapacityFactor

    LoadVariation = plx_enums.SystemOutRSIsEnum.LoadVariation

    SummerPeriod = plx_enums.SystemOutRSIsEnum.SummerPeriod

    PeakPeriod = plx_enums.SystemOutRSIsEnum.PeakPeriod


class SystemOutRegionsEnum(Enum):
    Load = plx_enums.SystemOutRegionsEnum.Load

    NativeLoad = plx_enums.SystemOutRegionsEnum.NativeLoad

    FixedLoad = plx_enums.SystemOutRegionsEnum.FixedLoad

    FixedGeneration = plx_enums.SystemOutRegionsEnum.FixedGeneration

    Generation = plx_enums.SystemOutRegionsEnum.Generation

    GeneratorAuxiliaryUse = plx_enums.SystemOutRegionsEnum.GeneratorAuxiliaryUse

    GenerationSentOut = plx_enums.SystemOutRegionsEnum.GenerationSentOut

    ContractGeneration = plx_enums.SystemOutRegionsEnum.ContractGeneration

    ContractLoad = plx_enums.SystemOutRegionsEnum.ContractLoad

    NetContractLoad = plx_enums.SystemOutRegionsEnum.NetContractLoad

    NetMarketSales = plx_enums.SystemOutRegionsEnum.NetMarketSales

    PumpLoad = plx_enums.SystemOutRegionsEnum.PumpLoad

    NetGeneration = plx_enums.SystemOutRegionsEnum.NetGeneration

    PurchaserLoad = plx_enums.SystemOutRegionsEnum.PurchaserLoad

    CustomerLoad = plx_enums.SystemOutRegionsEnum.CustomerLoad

    Imports = plx_enums.SystemOutRegionsEnum.Imports

    Exports = plx_enums.SystemOutRegionsEnum.Exports

    NetInterchange = plx_enums.SystemOutRegionsEnum.NetInterchange

    TransmissionLosses = plx_enums.SystemOutRegionsEnum.TransmissionLosses

    DemandCurtailed = plx_enums.SystemOutRegionsEnum.DemandCurtailed

    UnservedEnergyHours = plx_enums.SystemOutRegionsEnum.UnservedEnergyHours

    UnservedEnergy = plx_enums.SystemOutRegionsEnum.UnservedEnergy

    CostofUnservedEnergy = plx_enums.SystemOutRegionsEnum.CostofUnservedEnergy

    DumpEnergyHours = plx_enums.SystemOutRegionsEnum.DumpEnergyHours

    DumpEnergy = plx_enums.SystemOutRegionsEnum.DumpEnergy

    CostofDumpEnergy = plx_enums.SystemOutRegionsEnum.CostofDumpEnergy

    NoCostGenerationCapacity = plx_enums.SystemOutRegionsEnum.NoCostGenerationCapacity

    HoursGenerationCurtailed = plx_enums.SystemOutRegionsEnum.HoursGenerationCurtailed

    GenerationCapacityCurtailed = plx_enums.SystemOutRegionsEnum.GenerationCapacityCurtailed

    FlexibilityUp = plx_enums.SystemOutRegionsEnum.FlexibilityUp

    FlexibilityDown = plx_enums.SystemOutRegionsEnum.FlexibilityDown

    RampFlexibilityUp = plx_enums.SystemOutRegionsEnum.RampFlexibilityUp

    RampFlexibilityDown = plx_enums.SystemOutRegionsEnum.RampFlexibilityDown

    HoursatMinimum = plx_enums.SystemOutRegionsEnum.HoursatMinimum

    InflexibleGeneration = plx_enums.SystemOutRegionsEnum.InflexibleGeneration

    GenerationCost = plx_enums.SystemOutRegionsEnum.GenerationCost

    GeneratorPumpCost = plx_enums.SystemOutRegionsEnum.GeneratorPumpCost

    GeneratorStartShutdownCost = plx_enums.SystemOutRegionsEnum.GeneratorStartShutdownCost

    EmissionsCost = plx_enums.SystemOutRegionsEnum.EmissionsCost

    AbatementCost = plx_enums.SystemOutRegionsEnum.AbatementCost

    TotalGenerationCost = plx_enums.SystemOutRegionsEnum.TotalGenerationCost

    TotalSystemCost = plx_enums.SystemOutRegionsEnum.TotalSystemCost

    GeneratorFOMCost = plx_enums.SystemOutRegionsEnum.GeneratorFOMCost

    TotalFixedCosts = plx_enums.SystemOutRegionsEnum.TotalFixedCosts

    SRMC = plx_enums.SystemOutRegionsEnum.SRMC

    Price = plx_enums.SystemOutRegionsEnum.Price

    Uplift = plx_enums.SystemOutRegionsEnum.Uplift

    PriceCostMarkup = plx_enums.SystemOutRegionsEnum.PriceCostMarkup

    TimeweightedPrice = plx_enums.SystemOutRegionsEnum.TimeweightedPrice

    LoadweightedPrice = plx_enums.SystemOutRegionsEnum.LoadweightedPrice

    GenerationweightedPrice = plx_enums.SystemOutRegionsEnum.GenerationweightedPrice

    CosttoLoad = plx_enums.SystemOutRegionsEnum.CosttoLoad

    GeneratorPoolRevenue = plx_enums.SystemOutRegionsEnum.GeneratorPoolRevenue

    TransmissionRental = plx_enums.SystemOutRegionsEnum.TransmissionRental

    SettlementSurplus = plx_enums.SystemOutRegionsEnum.SettlementSurplus

    InterregionalTransmissionLosses = plx_enums.SystemOutRegionsEnum.InterregionalTransmissionLosses

    IntraregionalTransmissionLosses = plx_enums.SystemOutRegionsEnum.IntraregionalTransmissionLosses

    ContractVolume = plx_enums.SystemOutRegionsEnum.ContractVolume

    ContractSettlement = plx_enums.SystemOutRegionsEnum.ContractSettlement

    NetCosttoLoad = plx_enums.SystemOutRegionsEnum.NetCosttoLoad

    DSPBidQuantity = plx_enums.SystemOutRegionsEnum.DSPBidQuantity

    DSPBidPrice = plx_enums.SystemOutRegionsEnum.DSPBidPrice

    DSPBidCleared = plx_enums.SystemOutRegionsEnum.DSPBidCleared

    ClearedDSPBidPrice = plx_enums.SystemOutRegionsEnum.ClearedDSPBidPrice

    ClearedDSPBidCost = plx_enums.SystemOutRegionsEnum.ClearedDSPBidCost

    CostofCurtailment = plx_enums.SystemOutRegionsEnum.CostofCurtailment

    GeneratorNetPoolRevenue = plx_enums.SystemOutRegionsEnum.GeneratorNetPoolRevenue

    ClearedOfferCost = plx_enums.SystemOutRegionsEnum.ClearedOfferCost

    ClearedReserveOfferCost = plx_enums.SystemOutRegionsEnum.ClearedReserveOfferCost

    GeneratorNetRevenue = plx_enums.SystemOutRegionsEnum.GeneratorNetRevenue

    ShadowLoad = plx_enums.SystemOutRegionsEnum.ShadowLoad

    ShadowGeneration = plx_enums.SystemOutRegionsEnum.ShadowGeneration

    ShadowPrice = plx_enums.SystemOutRegionsEnum.ShadowPrice

    ShadowCosttoLoad = plx_enums.SystemOutRegionsEnum.ShadowCosttoLoad

    GeneratorMonopolyRent = plx_enums.SystemOutRegionsEnum.GeneratorMonopolyRent

    UtilityMonopolyRent = plx_enums.SystemOutRegionsEnum.UtilityMonopolyRent

    NonUtilityMonopolyRent = plx_enums.SystemOutRegionsEnum.NonUtilityMonopolyRent

    UtilityContractSettlement = plx_enums.SystemOutRegionsEnum.UtilityContractSettlement

    NonUtilityContractSettlement = plx_enums.SystemOutRegionsEnum.NonUtilityContractSettlement

    UtilityNetRevenue = plx_enums.SystemOutRegionsEnum.UtilityNetRevenue

    NonUtilityNetRevenue = plx_enums.SystemOutRegionsEnum.NonUtilityNetRevenue

    ConstrainedOnCost = plx_enums.SystemOutRegionsEnum.ConstrainedOnCost

    ConstrainedOffCost = plx_enums.SystemOutRegionsEnum.ConstrainedOffCost

    GeneratorNetProfit = plx_enums.SystemOutRegionsEnum.GeneratorNetProfit

    NetMarketProfit = plx_enums.SystemOutRegionsEnum.NetMarketProfit

    ExportCost = plx_enums.SystemOutRegionsEnum.ExportCost

    ImportRevenue = plx_enums.SystemOutRegionsEnum.ImportRevenue

    NetCostofExports = plx_enums.SystemOutRegionsEnum.NetCostofExports

    WheelingRevenue = plx_enums.SystemOutRegionsEnum.WheelingRevenue

    WheelingCost = plx_enums.SystemOutRegionsEnum.WheelingCost

    IntraregionalTransmissionRental = plx_enums.SystemOutRegionsEnum.IntraregionalTransmissionRental

    InterregionalTransmissionRental = plx_enums.SystemOutRegionsEnum.InterregionalTransmissionRental

    TransmissionControlRental = plx_enums.SystemOutRegionsEnum.TransmissionControlRental

    PeakLoad = plx_enums.SystemOutRegionsEnum.PeakLoad

    GenerationCapacity = plx_enums.SystemOutRegionsEnum.GenerationCapacity

    FirmGenerationCapacity = plx_enums.SystemOutRegionsEnum.FirmGenerationCapacity

    CurtailableLoad = plx_enums.SystemOutRegionsEnum.CurtailableLoad

    ContractGenerationCapacity = plx_enums.SystemOutRegionsEnum.ContractGenerationCapacity

    ContractLoadObligation = plx_enums.SystemOutRegionsEnum.ContractLoadObligation

    ImportCapacity = plx_enums.SystemOutRegionsEnum.ImportCapacity

    ExportCapacity = plx_enums.SystemOutRegionsEnum.ExportCapacity

    NetCapacityInterchange = plx_enums.SystemOutRegionsEnum.NetCapacityInterchange

    MinCapacityReserves = plx_enums.SystemOutRegionsEnum.MinCapacityReserves

    MaxCapacityReserves = plx_enums.SystemOutRegionsEnum.MaxCapacityReserves

    CapacityReserves = plx_enums.SystemOutRegionsEnum.CapacityReserves

    MaxCapacityReserveMargin = plx_enums.SystemOutRegionsEnum.MaxCapacityReserveMargin

    MinCapacityReserveMargin = plx_enums.SystemOutRegionsEnum.MinCapacityReserveMargin

    CapacityReserveMargin = plx_enums.SystemOutRegionsEnum.CapacityReserveMargin

    MinLoad = plx_enums.SystemOutRegionsEnum.MinLoad

    Maintenance = plx_enums.SystemOutRegionsEnum.Maintenance

    ForcedOutage = plx_enums.SystemOutRegionsEnum.ForcedOutage

    AvailableCapacity = plx_enums.SystemOutRegionsEnum.AvailableCapacity

    AvailableCapacityReserves = plx_enums.SystemOutRegionsEnum.AvailableCapacityReserves

    AvailableCapacityMargin = plx_enums.SystemOutRegionsEnum.AvailableCapacityMargin

    DispatchableCapacity = plx_enums.SystemOutRegionsEnum.DispatchableCapacity

    UndispatchedCapacity = plx_enums.SystemOutRegionsEnum.UndispatchedCapacity

    DiscreteMaintenance = plx_enums.SystemOutRegionsEnum.DiscreteMaintenance

    DistributedMaintenance = plx_enums.SystemOutRegionsEnum.DistributedMaintenance

    MaintenanceFactor = plx_enums.SystemOutRegionsEnum.MaintenanceFactor

    EENS = plx_enums.SystemOutRegionsEnum.EENS

    EDNS = plx_enums.SystemOutRegionsEnum.EDNS

    LOLE = plx_enums.SystemOutRegionsEnum.LOLE

    LOLP = plx_enums.SystemOutRegionsEnum.LOLP

    MultiareaLOLE = plx_enums.SystemOutRegionsEnum.MultiareaLOLE

    MultiareaLOLP = plx_enums.SystemOutRegionsEnum.MultiareaLOLP

    PlanningPeakLoad = plx_enums.SystemOutRegionsEnum.PlanningPeakLoad

    GenerationCapacityBuilt = plx_enums.SystemOutRegionsEnum.GenerationCapacityBuilt

    GenerationCapacityRetired = plx_enums.SystemOutRegionsEnum.GenerationCapacityRetired

    ImportCapacityBuilt = plx_enums.SystemOutRegionsEnum.ImportCapacityBuilt

    ImportCapacityRetired = plx_enums.SystemOutRegionsEnum.ImportCapacityRetired

    ExportCapacityBuilt = plx_enums.SystemOutRegionsEnum.ExportCapacityBuilt

    ExportCapacityRetired = plx_enums.SystemOutRegionsEnum.ExportCapacityRetired

    CapacityShortage = plx_enums.SystemOutRegionsEnum.CapacityShortage

    CapacityExcess = plx_enums.SystemOutRegionsEnum.CapacityExcess

    CapacityShadowPrice = plx_enums.SystemOutRegionsEnum.CapacityShadowPrice

    LRMC = plx_enums.SystemOutRegionsEnum.LRMC

    CapacityPayments = plx_enums.SystemOutRegionsEnum.CapacityPayments

    CapacityPrice = plx_enums.SystemOutRegionsEnum.CapacityPrice

    CapacityShortageCost = plx_enums.SystemOutRegionsEnum.CapacityShortageCost

    CapacityExcessCost = plx_enums.SystemOutRegionsEnum.CapacityExcessCost

    TotalGeneratorRevenue = plx_enums.SystemOutRegionsEnum.TotalGeneratorRevenue

    GeneratorBuildCost = plx_enums.SystemOutRegionsEnum.GeneratorBuildCost

    GeneratorRetirementCost = plx_enums.SystemOutRegionsEnum.GeneratorRetirementCost

    TransmissionBuildCost = plx_enums.SystemOutRegionsEnum.TransmissionBuildCost

    TransmissionRetirementCost = plx_enums.SystemOutRegionsEnum.TransmissionRetirementCost

    AnnualizedBuildCost = plx_enums.SystemOutRegionsEnum.AnnualizedBuildCost

    TotalCost = plx_enums.SystemOutRegionsEnum.TotalCost

    LevelizedCost = plx_enums.SystemOutRegionsEnum.LevelizedCost

    ShadowGenerationCapacityBuilt = plx_enums.SystemOutRegionsEnum.ShadowGenerationCapacityBuilt

    x = plx_enums.SystemOutRegionsEnum.x

    y = plx_enums.SystemOutRegionsEnum.y

    z = plx_enums.SystemOutRegionsEnum.z


class SystemOutReservesEnum(Enum):
    Provision = plx_enums.SystemOutReservesEnum.Provision

    Risk = plx_enums.SystemOutReservesEnum.Risk

    Shortage = plx_enums.SystemOutReservesEnum.Shortage

    ShortageHours = plx_enums.SystemOutReservesEnum.ShortageHours

    ShortageCost = plx_enums.SystemOutReservesEnum.ShortageCost

    ClearedOfferPrice = plx_enums.SystemOutReservesEnum.ClearedOfferPrice

    ClearedOfferCost = plx_enums.SystemOutReservesEnum.ClearedOfferCost

    Cost = plx_enums.SystemOutReservesEnum.Cost

    Price = plx_enums.SystemOutReservesEnum.Price

    TimeweightedPrice = plx_enums.SystemOutReservesEnum.TimeweightedPrice

    AvailableResponse = plx_enums.SystemOutReservesEnum.AvailableResponse

    x = plx_enums.SystemOutReservesEnum.x

    y = plx_enums.SystemOutReservesEnum.y

    z = plx_enums.SystemOutReservesEnum.z


class SystemOutStoragesEnum(Enum):
    MaxVolume = plx_enums.SystemOutStoragesEnum.MaxVolume

    MinVolume = plx_enums.SystemOutStoragesEnum.MinVolume

    InitialVolume = plx_enums.SystemOutStoragesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutStoragesEnum.EndVolume

    InitialLevel = plx_enums.SystemOutStoragesEnum.InitialLevel

    EndLevel = plx_enums.SystemOutStoragesEnum.EndLevel

    HoursFull = plx_enums.SystemOutStoragesEnum.HoursFull

    WorkingVolume = plx_enums.SystemOutStoragesEnum.WorkingVolume

    Utilization = plx_enums.SystemOutStoragesEnum.Utilization

    WorkingUtilization = plx_enums.SystemOutStoragesEnum.WorkingUtilization

    AverageUtilization = plx_enums.SystemOutStoragesEnum.AverageUtilization

    AverageWorkingUtilization = plx_enums.SystemOutStoragesEnum.AverageWorkingUtilization

    Inflow = plx_enums.SystemOutStoragesEnum.Inflow

    Release = plx_enums.SystemOutStoragesEnum.Release

    NaturalInflow = plx_enums.SystemOutStoragesEnum.NaturalInflow

    GeneratorRelease = plx_enums.SystemOutStoragesEnum.GeneratorRelease

    DownstreamRelease = plx_enums.SystemOutStoragesEnum.DownstreamRelease

    Spill = plx_enums.SystemOutStoragesEnum.Spill

    InflowRate = plx_enums.SystemOutStoragesEnum.InflowRate

    ReleaseRate = plx_enums.SystemOutStoragesEnum.ReleaseRate

    NaturalInflowRate = plx_enums.SystemOutStoragesEnum.NaturalInflowRate

    GeneratorReleaseRate = plx_enums.SystemOutStoragesEnum.GeneratorReleaseRate

    DownstreamReleaseRate = plx_enums.SystemOutStoragesEnum.DownstreamReleaseRate

    SpillRate = plx_enums.SystemOutStoragesEnum.SpillRate

    Loss = plx_enums.SystemOutStoragesEnum.Loss

    ShadowPrice = plx_enums.SystemOutStoragesEnum.ShadowPrice

    MarginalValue = plx_enums.SystemOutStoragesEnum.MarginalValue

    MarginalCost = plx_enums.SystemOutStoragesEnum.MarginalCost

    PotentialEnergy = plx_enums.SystemOutStoragesEnum.PotentialEnergy

    Generation = plx_enums.SystemOutStoragesEnum.Generation

    PumpLoad = plx_enums.SystemOutStoragesEnum.PumpLoad

    Efficiency = plx_enums.SystemOutStoragesEnum.Efficiency

    MinReleaseViolation = plx_enums.SystemOutStoragesEnum.MinReleaseViolation

    MinReleaseViolationHours = plx_enums.SystemOutStoragesEnum.MinReleaseViolationHours

    MinReleaseViolationCost = plx_enums.SystemOutStoragesEnum.MinReleaseViolationCost

    MaxReleaseViolation = plx_enums.SystemOutStoragesEnum.MaxReleaseViolation

    MaxReleaseViolationHours = plx_enums.SystemOutStoragesEnum.MaxReleaseViolationHours

    MaxReleaseViolationCost = plx_enums.SystemOutStoragesEnum.MaxReleaseViolationCost

    Ramp = plx_enums.SystemOutStoragesEnum.Ramp

    RampPrice = plx_enums.SystemOutStoragesEnum.RampPrice

    RampViolation = plx_enums.SystemOutStoragesEnum.RampViolation

    RampViolationHours = plx_enums.SystemOutStoragesEnum.RampViolationHours

    RampViolationCost = plx_enums.SystemOutStoragesEnum.RampViolationCost

    TargetViolation = plx_enums.SystemOutStoragesEnum.TargetViolation

    TargetViolationCost = plx_enums.SystemOutStoragesEnum.TargetViolationCost

    NonphysicalInflow = plx_enums.SystemOutStoragesEnum.NonphysicalInflow

    NonphysicalSpill = plx_enums.SystemOutStoragesEnum.NonphysicalSpill

    x = plx_enums.SystemOutStoragesEnum.x

    y = plx_enums.SystemOutStoragesEnum.y

    z = plx_enums.SystemOutStoragesEnum.z


class SystemOutTimeslicesEnum(Enum):
    HoursIncluded = plx_enums.SystemOutTimeslicesEnum.HoursIncluded


class SystemOutTransformersEnum(Enum):
    Flow = plx_enums.SystemOutTransformersEnum.Flow

    FlowBack = plx_enums.SystemOutTransformersEnum.FlowBack

    ExportLimit = plx_enums.SystemOutTransformersEnum.ExportLimit

    ImportLimit = plx_enums.SystemOutTransformersEnum.ImportLimit

    Loading = plx_enums.SystemOutTransformersEnum.Loading

    LoadingBack = plx_enums.SystemOutTransformersEnum.LoadingBack

    Loss = plx_enums.SystemOutTransformersEnum.Loss

    LossBack = plx_enums.SystemOutTransformersEnum.LossBack

    Voltage = plx_enums.SystemOutTransformersEnum.Voltage

    HoursCongested = plx_enums.SystemOutTransformersEnum.HoursCongested

    ShadowPrice = plx_enums.SystemOutTransformersEnum.ShadowPrice

    ViolationHours = plx_enums.SystemOutTransformersEnum.ViolationHours

    ViolationBackHours = plx_enums.SystemOutTransformersEnum.ViolationBackHours

    Violation = plx_enums.SystemOutTransformersEnum.Violation

    ViolationBack = plx_enums.SystemOutTransformersEnum.ViolationBack

    ViolationCost = plx_enums.SystemOutTransformersEnum.ViolationCost

    ViolationCostBack = plx_enums.SystemOutTransformersEnum.ViolationCostBack

    MaxFlow = plx_enums.SystemOutTransformersEnum.MaxFlow

    MinFlow = plx_enums.SystemOutTransformersEnum.MinFlow

    ExportCost = plx_enums.SystemOutTransformersEnum.ExportCost

    ImportCost = plx_enums.SystemOutTransformersEnum.ImportCost

    ExportRevenue = plx_enums.SystemOutTransformersEnum.ExportRevenue

    ImportRevenue = plx_enums.SystemOutTransformersEnum.ImportRevenue

    Rental = plx_enums.SystemOutTransformersEnum.Rental

    RentalBack = plx_enums.SystemOutTransformersEnum.RentalBack

    AvailableTransferCapability = plx_enums.SystemOutTransformersEnum.AvailableTransferCapability

    AvailableTransferCapabilityBack = plx_enums.SystemOutTransformersEnum.AvailableTransferCapabilityBack

    x = plx_enums.SystemOutTransformersEnum.x

    y = plx_enums.SystemOutTransformersEnum.y

    z = plx_enums.SystemOutTransformersEnum.z


class SystemOutTransmissionRightsEnum(Enum):
    Quantity = plx_enums.SystemOutTransmissionRightsEnum.Quantity

    Settlement = plx_enums.SystemOutTransmissionRightsEnum.Settlement

    NetProfit = plx_enums.SystemOutTransmissionRightsEnum.NetProfit

    SourcePrice = plx_enums.SystemOutTransmissionRightsEnum.SourcePrice

    SourceEnergyCharge = plx_enums.SystemOutTransmissionRightsEnum.SourceEnergyCharge

    SourceCongestionCharge = plx_enums.SystemOutTransmissionRightsEnum.SourceCongestionCharge

    SourceLossCharge = plx_enums.SystemOutTransmissionRightsEnum.SourceLossCharge

    SinkPrice = plx_enums.SystemOutTransmissionRightsEnum.SinkPrice

    SinkEnergyCharge = plx_enums.SystemOutTransmissionRightsEnum.SinkEnergyCharge

    SinkCongestionCharge = plx_enums.SystemOutTransmissionRightsEnum.SinkCongestionCharge

    SinkLossCharge = plx_enums.SystemOutTransmissionRightsEnum.SinkLossCharge

    PriceDelta = plx_enums.SystemOutTransmissionRightsEnum.PriceDelta


class SystemOutVariablesEnum(Enum):
    ExpectedValue = plx_enums.SystemOutVariablesEnum.ExpectedValue

    RawValue = plx_enums.SystemOutVariablesEnum.RawValue

    Value = plx_enums.SystemOutVariablesEnum.Value

    Error = plx_enums.SystemOutVariablesEnum.Error

    Volatility = plx_enums.SystemOutVariablesEnum.Volatility


class SystemOutWaterDemandsEnum(Enum):
    Demand = plx_enums.SystemOutWaterDemandsEnum.Demand

    ShortageHours = plx_enums.SystemOutWaterDemandsEnum.ShortageHours

    Shortage = plx_enums.SystemOutWaterDemandsEnum.Shortage

    ShortageCost = plx_enums.SystemOutWaterDemandsEnum.ShortageCost

    ExcessHours = plx_enums.SystemOutWaterDemandsEnum.ExcessHours

    Excess = plx_enums.SystemOutWaterDemandsEnum.Excess

    ExcessCost = plx_enums.SystemOutWaterDemandsEnum.ExcessCost

    NetDemand = plx_enums.SystemOutWaterDemandsEnum.NetDemand

    Cost = plx_enums.SystemOutWaterDemandsEnum.Cost

    PricePaid = plx_enums.SystemOutWaterDemandsEnum.PricePaid

    BidQuantity = plx_enums.SystemOutWaterDemandsEnum.BidQuantity

    BidPrice = plx_enums.SystemOutWaterDemandsEnum.BidPrice

    BidCleared = plx_enums.SystemOutWaterDemandsEnum.BidCleared

    ClearedBidPrice = plx_enums.SystemOutWaterDemandsEnum.ClearedBidPrice

    ClearedBidValue = plx_enums.SystemOutWaterDemandsEnum.ClearedBidValue

    x = plx_enums.SystemOutWaterDemandsEnum.x

    y = plx_enums.SystemOutWaterDemandsEnum.y

    z = plx_enums.SystemOutWaterDemandsEnum.z


class SystemOutWaterNodesEnum(Enum):
    Production = plx_enums.SystemOutWaterNodesEnum.Production

    Demand = plx_enums.SystemOutWaterNodesEnum.Demand

    Flow = plx_enums.SystemOutWaterNodesEnum.Flow

    Imports = plx_enums.SystemOutWaterNodesEnum.Imports

    Exports = plx_enums.SystemOutWaterNodesEnum.Exports

    NetInterchange = plx_enums.SystemOutWaterNodesEnum.NetInterchange

    InitialVolume = plx_enums.SystemOutWaterNodesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutWaterNodesEnum.EndVolume

    ProductionCost = plx_enums.SystemOutWaterNodesEnum.ProductionCost

    ShortageHours = plx_enums.SystemOutWaterNodesEnum.ShortageHours

    Shortage = plx_enums.SystemOutWaterNodesEnum.Shortage

    ShortageCost = plx_enums.SystemOutWaterNodesEnum.ShortageCost

    ExcessHours = plx_enums.SystemOutWaterNodesEnum.ExcessHours

    Excess = plx_enums.SystemOutWaterNodesEnum.Excess

    ExcessCost = plx_enums.SystemOutWaterNodesEnum.ExcessCost

    ShadowPrice = plx_enums.SystemOutWaterNodesEnum.ShadowPrice

    FOMCost = plx_enums.SystemOutWaterNodesEnum.FOMCost

    FixedCosts = plx_enums.SystemOutWaterNodesEnum.FixedCosts

    EnergyConsumption = plx_enums.SystemOutWaterNodesEnum.EnergyConsumption

    Units = plx_enums.SystemOutWaterNodesEnum.Units

    UnitsBuilt = plx_enums.SystemOutWaterNodesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutWaterNodesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutWaterNodesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutWaterNodesEnum.RetirementCost

    x = plx_enums.SystemOutWaterNodesEnum.x

    y = plx_enums.SystemOutWaterNodesEnum.y

    z = plx_enums.SystemOutWaterNodesEnum.z


class SystemOutWaterPipelinesEnum(Enum):
    Flow = plx_enums.SystemOutWaterPipelinesEnum.Flow

    HoursCongested = plx_enums.SystemOutWaterPipelinesEnum.HoursCongested

    HoursCongestedBack = plx_enums.SystemOutWaterPipelinesEnum.HoursCongestedBack

    ProductionCost = plx_enums.SystemOutWaterPipelinesEnum.ProductionCost

    FOMCost = plx_enums.SystemOutWaterPipelinesEnum.FOMCost

    FixedCosts = plx_enums.SystemOutWaterPipelinesEnum.FixedCosts

    EnergyConsumption = plx_enums.SystemOutWaterPipelinesEnum.EnergyConsumption

    UnitsOut = plx_enums.SystemOutWaterPipelinesEnum.UnitsOut

    MaintenanceHours = plx_enums.SystemOutWaterPipelinesEnum.MaintenanceHours

    ForcedOutageHours = plx_enums.SystemOutWaterPipelinesEnum.ForcedOutageHours

    ServiceFactor = plx_enums.SystemOutWaterPipelinesEnum.ServiceFactor

    Units = plx_enums.SystemOutWaterPipelinesEnum.Units

    UnitsBuilt = plx_enums.SystemOutWaterPipelinesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutWaterPipelinesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutWaterPipelinesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutWaterPipelinesEnum.RetirementCost

    x = plx_enums.SystemOutWaterPipelinesEnum.x

    y = plx_enums.SystemOutWaterPipelinesEnum.y

    z = plx_enums.SystemOutWaterPipelinesEnum.z


class SystemOutWaterPlantsEnum(Enum):
    RawWater = plx_enums.SystemOutWaterPlantsEnum.RawWater

    Production = plx_enums.SystemOutWaterPlantsEnum.Production

    ProductionCost = plx_enums.SystemOutWaterPlantsEnum.ProductionCost

    VOMCost = plx_enums.SystemOutWaterPlantsEnum.VOMCost

    FOMCost = plx_enums.SystemOutWaterPlantsEnum.FOMCost

    FixedCosts = plx_enums.SystemOutWaterPlantsEnum.FixedCosts

    SRMC = plx_enums.SystemOutWaterPlantsEnum.SRMC

    EnergyConsumption = plx_enums.SystemOutWaterPlantsEnum.EnergyConsumption

    ElectricLoad = plx_enums.SystemOutWaterPlantsEnum.ElectricLoad

    HeatLoad = plx_enums.SystemOutWaterPlantsEnum.HeatLoad

    AuxiliaryUse = plx_enums.SystemOutWaterPlantsEnum.AuxiliaryUse

    Units = plx_enums.SystemOutWaterPlantsEnum.Units

    UnitsBuilt = plx_enums.SystemOutWaterPlantsEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutWaterPlantsEnum.BuildCost

    x = plx_enums.SystemOutWaterPlantsEnum.x

    y = plx_enums.SystemOutWaterPlantsEnum.y

    z = plx_enums.SystemOutWaterPlantsEnum.z


class SystemOutWaterStoragesEnum(Enum):
    MaxVolume = plx_enums.SystemOutWaterStoragesEnum.MaxVolume

    MinVolume = plx_enums.SystemOutWaterStoragesEnum.MinVolume

    InitialVolume = plx_enums.SystemOutWaterStoragesEnum.InitialVolume

    EndVolume = plx_enums.SystemOutWaterStoragesEnum.EndVolume

    WorkingVolume = plx_enums.SystemOutWaterStoragesEnum.WorkingVolume

    Utilization = plx_enums.SystemOutWaterStoragesEnum.Utilization

    WorkingUtilization = plx_enums.SystemOutWaterStoragesEnum.WorkingUtilization

    AverageUtilization = plx_enums.SystemOutWaterStoragesEnum.AverageUtilization

    AverageWorkingUtilization = plx_enums.SystemOutWaterStoragesEnum.AverageWorkingUtilization

    Withdrawal = plx_enums.SystemOutWaterStoragesEnum.Withdrawal

    Injection = plx_enums.SystemOutWaterStoragesEnum.Injection

    NetWithdrawal = plx_enums.SystemOutWaterStoragesEnum.NetWithdrawal

    ShadowPrice = plx_enums.SystemOutWaterStoragesEnum.ShadowPrice

    FOMCost = plx_enums.SystemOutWaterStoragesEnum.FOMCost

    FixedCosts = plx_enums.SystemOutWaterStoragesEnum.FixedCosts

    Units = plx_enums.SystemOutWaterStoragesEnum.Units

    UnitsBuilt = plx_enums.SystemOutWaterStoragesEnum.UnitsBuilt

    BuildCost = plx_enums.SystemOutWaterStoragesEnum.BuildCost

    UnitsRetired = plx_enums.SystemOutWaterStoragesEnum.UnitsRetired

    RetirementCost = plx_enums.SystemOutWaterStoragesEnum.RetirementCost

    x = plx_enums.SystemOutWaterStoragesEnum.x

    y = plx_enums.SystemOutWaterStoragesEnum.y

    z = plx_enums.SystemOutWaterStoragesEnum.z


class SystemOutWaterZonesEnum(Enum):
    Production = plx_enums.SystemOutWaterZonesEnum.Production

    Demand = plx_enums.SystemOutWaterZonesEnum.Demand

    Imports = plx_enums.SystemOutWaterZonesEnum.Imports

    Exports = plx_enums.SystemOutWaterZonesEnum.Exports

    NetInterchange = plx_enums.SystemOutWaterZonesEnum.NetInterchange

    ShortageHours = plx_enums.SystemOutWaterZonesEnum.ShortageHours

    Shortage = plx_enums.SystemOutWaterZonesEnum.Shortage

    ShortageCost = plx_enums.SystemOutWaterZonesEnum.ShortageCost

    ExcessHours = plx_enums.SystemOutWaterZonesEnum.ExcessHours

    Excess = plx_enums.SystemOutWaterZonesEnum.Excess

    ExcessCost = plx_enums.SystemOutWaterZonesEnum.ExcessCost

    NetDemand = plx_enums.SystemOutWaterZonesEnum.NetDemand

    Cost = plx_enums.SystemOutWaterZonesEnum.Cost

    PricePaid = plx_enums.SystemOutWaterZonesEnum.PricePaid

    x = plx_enums.SystemOutWaterZonesEnum.x

    y = plx_enums.SystemOutWaterZonesEnum.y

    z = plx_enums.SystemOutWaterZonesEnum.z


class SystemOutWaterwaysEnum(Enum):
    Flow = plx_enums.SystemOutWaterwaysEnum.Flow

    MaxFlow = plx_enums.SystemOutWaterwaysEnum.MaxFlow

    MinFlow = plx_enums.SystemOutWaterwaysEnum.MinFlow

    HoursFlowing = plx_enums.SystemOutWaterwaysEnum.HoursFlowing

    ShadowPrice = plx_enums.SystemOutWaterwaysEnum.ShadowPrice

    MaxFlowViolationHours = plx_enums.SystemOutWaterwaysEnum.MaxFlowViolationHours

    MaxFlowViolation = plx_enums.SystemOutWaterwaysEnum.MaxFlowViolation

    MaxFlowViolationCost = plx_enums.SystemOutWaterwaysEnum.MaxFlowViolationCost

    MinFlowViolationHours = plx_enums.SystemOutWaterwaysEnum.MinFlowViolationHours

    MinFlowViolation = plx_enums.SystemOutWaterwaysEnum.MinFlowViolation

    MinFlowViolationCost = plx_enums.SystemOutWaterwaysEnum.MinFlowViolationCost

    Ramp = plx_enums.SystemOutWaterwaysEnum.Ramp

    MaxRamp = plx_enums.SystemOutWaterwaysEnum.MaxRamp

    RampViolationHours = plx_enums.SystemOutWaterwaysEnum.RampViolationHours

    RampViolation = plx_enums.SystemOutWaterwaysEnum.RampViolation

    RampViolationCost = plx_enums.SystemOutWaterwaysEnum.RampViolationCost

    x = plx_enums.SystemOutWaterwaysEnum.x

    y = plx_enums.SystemOutWaterwaysEnum.y

    z = plx_enums.SystemOutWaterwaysEnum.z


class SystemOutZonesEnum(Enum):
    Load = plx_enums.SystemOutZonesEnum.Load

    NativeLoad = plx_enums.SystemOutZonesEnum.NativeLoad

    FixedLoad = plx_enums.SystemOutZonesEnum.FixedLoad

    FixedGeneration = plx_enums.SystemOutZonesEnum.FixedGeneration

    Generation = plx_enums.SystemOutZonesEnum.Generation

    GeneratorAuxiliaryUse = plx_enums.SystemOutZonesEnum.GeneratorAuxiliaryUse

    GenerationSentOut = plx_enums.SystemOutZonesEnum.GenerationSentOut

    DemandCurtailed = plx_enums.SystemOutZonesEnum.DemandCurtailed

    ContractGeneration = plx_enums.SystemOutZonesEnum.ContractGeneration

    ContractLoad = plx_enums.SystemOutZonesEnum.ContractLoad

    NetContractLoad = plx_enums.SystemOutZonesEnum.NetContractLoad

    NetMarketSales = plx_enums.SystemOutZonesEnum.NetMarketSales

    PumpLoad = plx_enums.SystemOutZonesEnum.PumpLoad

    NetGeneration = plx_enums.SystemOutZonesEnum.NetGeneration

    PurchaserLoad = plx_enums.SystemOutZonesEnum.PurchaserLoad

    CustomerLoad = plx_enums.SystemOutZonesEnum.CustomerLoad

    Imports = plx_enums.SystemOutZonesEnum.Imports

    Exports = plx_enums.SystemOutZonesEnum.Exports

    NetInterchange = plx_enums.SystemOutZonesEnum.NetInterchange

    TransmissionLosses = plx_enums.SystemOutZonesEnum.TransmissionLosses

    UnservedEnergyHours = plx_enums.SystemOutZonesEnum.UnservedEnergyHours

    UnservedEnergy = plx_enums.SystemOutZonesEnum.UnservedEnergy

    CostofUnservedEnergy = plx_enums.SystemOutZonesEnum.CostofUnservedEnergy

    DumpEnergyHours = plx_enums.SystemOutZonesEnum.DumpEnergyHours

    DumpEnergy = plx_enums.SystemOutZonesEnum.DumpEnergy

    CostofDumpEnergy = plx_enums.SystemOutZonesEnum.CostofDumpEnergy

    NoCostGenerationCapacity = plx_enums.SystemOutZonesEnum.NoCostGenerationCapacity

    HoursGenerationCurtailed = plx_enums.SystemOutZonesEnum.HoursGenerationCurtailed

    GenerationCapacityCurtailed = plx_enums.SystemOutZonesEnum.GenerationCapacityCurtailed

    FlexibilityUp = plx_enums.SystemOutZonesEnum.FlexibilityUp

    FlexibilityDown = plx_enums.SystemOutZonesEnum.FlexibilityDown

    RampFlexibilityUp = plx_enums.SystemOutZonesEnum.RampFlexibilityUp

    RampFlexibilityDown = plx_enums.SystemOutZonesEnum.RampFlexibilityDown

    HoursatMinimum = plx_enums.SystemOutZonesEnum.HoursatMinimum

    InflexibleGeneration = plx_enums.SystemOutZonesEnum.InflexibleGeneration

    GenerationCost = plx_enums.SystemOutZonesEnum.GenerationCost

    GeneratorPumpCost = plx_enums.SystemOutZonesEnum.GeneratorPumpCost

    GeneratorStartShutdownCost = plx_enums.SystemOutZonesEnum.GeneratorStartShutdownCost

    EmissionsCost = plx_enums.SystemOutZonesEnum.EmissionsCost

    AbatementCost = plx_enums.SystemOutZonesEnum.AbatementCost

    TotalGenerationCost = plx_enums.SystemOutZonesEnum.TotalGenerationCost

    TotalSystemCost = plx_enums.SystemOutZonesEnum.TotalSystemCost

    GeneratorFOMCost = plx_enums.SystemOutZonesEnum.GeneratorFOMCost

    TotalFixedCosts = plx_enums.SystemOutZonesEnum.TotalFixedCosts

    SRMC = plx_enums.SystemOutZonesEnum.SRMC

    Price = plx_enums.SystemOutZonesEnum.Price

    TimeweightedPrice = plx_enums.SystemOutZonesEnum.TimeweightedPrice

    LoadweightedPrice = plx_enums.SystemOutZonesEnum.LoadweightedPrice

    GenerationweightedPrice = plx_enums.SystemOutZonesEnum.GenerationweightedPrice

    EnergyCharge = plx_enums.SystemOutZonesEnum.EnergyCharge

    CongestionCharge = plx_enums.SystemOutZonesEnum.CongestionCharge

    MarginalLossCharge = plx_enums.SystemOutZonesEnum.MarginalLossCharge

    MarginalLossFactor = plx_enums.SystemOutZonesEnum.MarginalLossFactor

    CosttoLoad = plx_enums.SystemOutZonesEnum.CosttoLoad

    GeneratorPoolRevenue = plx_enums.SystemOutZonesEnum.GeneratorPoolRevenue

    TransmissionRental = plx_enums.SystemOutZonesEnum.TransmissionRental

    SettlementSurplus = plx_enums.SystemOutZonesEnum.SettlementSurplus

    CostofCurtailment = plx_enums.SystemOutZonesEnum.CostofCurtailment

    ClearedOfferCost = plx_enums.SystemOutZonesEnum.ClearedOfferCost

    ClearedReserveOfferCost = plx_enums.SystemOutZonesEnum.ClearedReserveOfferCost

    GeneratorNetRevenue = plx_enums.SystemOutZonesEnum.GeneratorNetRevenue

    GeneratorNetProfit = plx_enums.SystemOutZonesEnum.GeneratorNetProfit

    NetMarketProfit = plx_enums.SystemOutZonesEnum.NetMarketProfit

    ExportCost = plx_enums.SystemOutZonesEnum.ExportCost

    ImportRevenue = plx_enums.SystemOutZonesEnum.ImportRevenue

    NetCostofExports = plx_enums.SystemOutZonesEnum.NetCostofExports

    WheelingRevenue = plx_enums.SystemOutZonesEnum.WheelingRevenue

    WheelingCost = plx_enums.SystemOutZonesEnum.WheelingCost

    PeakLoad = plx_enums.SystemOutZonesEnum.PeakLoad

    GenerationCapacity = plx_enums.SystemOutZonesEnum.GenerationCapacity

    FirmGenerationCapacity = plx_enums.SystemOutZonesEnum.FirmGenerationCapacity

    CurtailableLoad = plx_enums.SystemOutZonesEnum.CurtailableLoad

    ContractGenerationCapacity = plx_enums.SystemOutZonesEnum.ContractGenerationCapacity

    ContractLoadObligation = plx_enums.SystemOutZonesEnum.ContractLoadObligation

    ImportCapacity = plx_enums.SystemOutZonesEnum.ImportCapacity

    ExportCapacity = plx_enums.SystemOutZonesEnum.ExportCapacity

    NetCapacityInterchange = plx_enums.SystemOutZonesEnum.NetCapacityInterchange

    MinCapacityReserves = plx_enums.SystemOutZonesEnum.MinCapacityReserves

    MaxCapacityReserves = plx_enums.SystemOutZonesEnum.MaxCapacityReserves

    CapacityReserves = plx_enums.SystemOutZonesEnum.CapacityReserves

    MaxCapacityReserveMargin = plx_enums.SystemOutZonesEnum.MaxCapacityReserveMargin

    MinCapacityReserveMargin = plx_enums.SystemOutZonesEnum.MinCapacityReserveMargin

    CapacityReserveMargin = plx_enums.SystemOutZonesEnum.CapacityReserveMargin

    MinLoad = plx_enums.SystemOutZonesEnum.MinLoad

    AvailableCapacity = plx_enums.SystemOutZonesEnum.AvailableCapacity

    AvailableCapacityReserves = plx_enums.SystemOutZonesEnum.AvailableCapacityReserves

    AvailableCapacityMargin = plx_enums.SystemOutZonesEnum.AvailableCapacityMargin

    DispatchableCapacity = plx_enums.SystemOutZonesEnum.DispatchableCapacity

    UndispatchedCapacity = plx_enums.SystemOutZonesEnum.UndispatchedCapacity

    DiscreteMaintenance = plx_enums.SystemOutZonesEnum.DiscreteMaintenance

    DistributedMaintenance = plx_enums.SystemOutZonesEnum.DistributedMaintenance

    MaintenanceFactor = plx_enums.SystemOutZonesEnum.MaintenanceFactor

    EENS = plx_enums.SystemOutZonesEnum.EENS

    EDNS = plx_enums.SystemOutZonesEnum.EDNS

    LOLE = plx_enums.SystemOutZonesEnum.LOLE

    LOLP = plx_enums.SystemOutZonesEnum.LOLP

    MultiareaLOLE = plx_enums.SystemOutZonesEnum.MultiareaLOLE

    MultiareaLOLP = plx_enums.SystemOutZonesEnum.MultiareaLOLP

    PlanningPeakLoad = plx_enums.SystemOutZonesEnum.PlanningPeakLoad

    GenerationCapacityBuilt = plx_enums.SystemOutZonesEnum.GenerationCapacityBuilt

    GenerationCapacityRetired = plx_enums.SystemOutZonesEnum.GenerationCapacityRetired

    ImportCapacityBuilt = plx_enums.SystemOutZonesEnum.ImportCapacityBuilt

    ImportCapacityRetired = plx_enums.SystemOutZonesEnum.ImportCapacityRetired

    ExportCapacityBuilt = plx_enums.SystemOutZonesEnum.ExportCapacityBuilt

    ExportCapacityRetired = plx_enums.SystemOutZonesEnum.ExportCapacityRetired

    CapacityShortage = plx_enums.SystemOutZonesEnum.CapacityShortage

    CapacityExcess = plx_enums.SystemOutZonesEnum.CapacityExcess

    CapacityShadowPrice = plx_enums.SystemOutZonesEnum.CapacityShadowPrice

    LRMC = plx_enums.SystemOutZonesEnum.LRMC

    CapacityPayments = plx_enums.SystemOutZonesEnum.CapacityPayments

    CapacityPrice = plx_enums.SystemOutZonesEnum.CapacityPrice

    CapacityShortageCost = plx_enums.SystemOutZonesEnum.CapacityShortageCost

    CapacityExcessCost = plx_enums.SystemOutZonesEnum.CapacityExcessCost

    TotalGeneratorRevenue = plx_enums.SystemOutZonesEnum.TotalGeneratorRevenue

    GeneratorBuildCost = plx_enums.SystemOutZonesEnum.GeneratorBuildCost

    GeneratorRetirementCost = plx_enums.SystemOutZonesEnum.GeneratorRetirementCost

    TransmissionBuildCost = plx_enums.SystemOutZonesEnum.TransmissionBuildCost

    TransmissionRetirementCost = plx_enums.SystemOutZonesEnum.TransmissionRetirementCost

    AnnualizedBuildCost = plx_enums.SystemOutZonesEnum.AnnualizedBuildCost

    TotalCost = plx_enums.SystemOutZonesEnum.TotalCost

    LevelizedCost = plx_enums.SystemOutZonesEnum.LevelizedCost

    x = plx_enums.SystemOutZonesEnum.x

    y = plx_enums.SystemOutZonesEnum.y

    z = plx_enums.SystemOutZonesEnum.z


class SystemPhysicalContractsEnum(Enum):
    OfferQuantityFormat = plx_enums.SystemPhysicalContractsEnum.OfferQuantityFormat

    PriceSetting = plx_enums.SystemPhysicalContractsEnum.PriceSetting

    Units = plx_enums.SystemPhysicalContractsEnum.Units

    MaxGeneration = plx_enums.SystemPhysicalContractsEnum.MaxGeneration

    MaxLoad = plx_enums.SystemPhysicalContractsEnum.MaxLoad

    MinGeneration = plx_enums.SystemPhysicalContractsEnum.MinGeneration

    MinLoad = plx_enums.SystemPhysicalContractsEnum.MinLoad

    OfferQuantity = plx_enums.SystemPhysicalContractsEnum.OfferQuantity

    OfferPrice = plx_enums.SystemPhysicalContractsEnum.OfferPrice

    BidQuantity = plx_enums.SystemPhysicalContractsEnum.BidQuantity

    BidPrice = plx_enums.SystemPhysicalContractsEnum.BidPrice

    FirmCapacity = plx_enums.SystemPhysicalContractsEnum.FirmCapacity

    LoadObligation = plx_enums.SystemPhysicalContractsEnum.LoadObligation

    CapacityCharge = plx_enums.SystemPhysicalContractsEnum.CapacityCharge

    MaxGenerationUnits = plx_enums.SystemPhysicalContractsEnum.MaxGenerationUnits

    MaxLoadUnits = plx_enums.SystemPhysicalContractsEnum.MaxLoadUnits

    MinGenerationUnits = plx_enums.SystemPhysicalContractsEnum.MinGenerationUnits

    MinLoadUnits = plx_enums.SystemPhysicalContractsEnum.MinLoadUnits

    BuildNonanticipativity = plx_enums.SystemPhysicalContractsEnum.BuildNonanticipativity

    x = plx_enums.SystemPhysicalContractsEnum.x

    y = plx_enums.SystemPhysicalContractsEnum.y

    z = plx_enums.SystemPhysicalContractsEnum.z


class SystemPowerStationsEnum(Enum):
    IsEnabled = plx_enums.SystemPowerStationsEnum.IsEnabled


class SystemPurchasersEnum(Enum):
    BenefitFunctionShape = plx_enums.SystemPurchasersEnum.BenefitFunctionShape

    MaxBenefitFunctionTranches = plx_enums.SystemPurchasersEnum.MaxBenefitFunctionTranches

    InterruptibleLoadLogic = plx_enums.SystemPurchasersEnum.InterruptibleLoadLogic

    PriceSetting = plx_enums.SystemPurchasersEnum.PriceSetting

    Units = plx_enums.SystemPurchasersEnum.Units

    MinLoad = plx_enums.SystemPurchasersEnum.MinLoad

    MaxLoad = plx_enums.SystemPurchasersEnum.MaxLoad

    FixedLoad = plx_enums.SystemPurchasersEnum.FixedLoad

    MaxRampDown = plx_enums.SystemPurchasersEnum.MaxRampDown

    MaxRampUp = plx_enums.SystemPurchasersEnum.MaxRampUp

    MaxEnergy = plx_enums.SystemPurchasersEnum.MaxEnergy

    MinEnergy = plx_enums.SystemPurchasersEnum.MinEnergy

    MaxLoadFactor = plx_enums.SystemPurchasersEnum.MaxLoadFactor

    MinLoadFactor = plx_enums.SystemPurchasersEnum.MinLoadFactor

    MaxEnergyPenalty = plx_enums.SystemPurchasersEnum.MaxEnergyPenalty

    MinEnergyPenalty = plx_enums.SystemPurchasersEnum.MinEnergyPenalty

    MarginalLossFactor = plx_enums.SystemPurchasersEnum.MarginalLossFactor

    BidQuantity = plx_enums.SystemPurchasersEnum.BidQuantity

    BidPrice = plx_enums.SystemPurchasersEnum.BidPrice

    Tariff = plx_enums.SystemPurchasersEnum.Tariff

    DemandFnSlope = plx_enums.SystemPurchasersEnum.DemandFnSlope

    DemandFnIntercept = plx_enums.SystemPurchasersEnum.DemandFnIntercept

    LoadObligation = plx_enums.SystemPurchasersEnum.LoadObligation

    x = plx_enums.SystemPurchasersEnum.x

    y = plx_enums.SystemPurchasersEnum.y

    z = plx_enums.SystemPurchasersEnum.z


class SystemRSIsEnum(Enum):
    AllowNegativeMarkups = plx_enums.SystemRSIsEnum.AllowNegativeMarkups

    RSI = plx_enums.SystemRSIsEnum.RSI

    LernerIndex = plx_enums.SystemRSIsEnum.LernerIndex

    BoundedLernerIndex = plx_enums.SystemRSIsEnum.BoundedLernerIndex

    Intercept = plx_enums.SystemRSIsEnum.Intercept

    RSICoefficient = plx_enums.SystemRSIsEnum.RSICoefficient

    RSIsquaredCoefficient = plx_enums.SystemRSIsEnum.RSIsquaredCoefficient

    LoadUnhedgedCoefficient = plx_enums.SystemRSIsEnum.LoadUnhedgedCoefficient

    RSIInverseCoefficient = plx_enums.SystemRSIsEnum.RSIInverseCoefficient

    LoadCoefficient = plx_enums.SystemRSIsEnum.LoadCoefficient

    LoadCapacityRatioCoefficient = plx_enums.SystemRSIsEnum.LoadCapacityRatioCoefficient

    CapacityFactorCoefficient = plx_enums.SystemRSIsEnum.CapacityFactorCoefficient

    LoadVariationCoefficient = plx_enums.SystemRSIsEnum.LoadVariationCoefficient

    SummerPeriodCoefficient = plx_enums.SystemRSIsEnum.SummerPeriodCoefficient

    PeakPeriodCoefficient = plx_enums.SystemRSIsEnum.PeakPeriodCoefficient

    AverageLoad = plx_enums.SystemRSIsEnum.AverageLoad

    LernerIndextstatistic = plx_enums.SystemRSIsEnum.LernerIndextstatistic

    LernerIndexStdDev = plx_enums.SystemRSIsEnum.LernerIndexStdDev

    LernerIndexCalibrationFactor = plx_enums.SystemRSIsEnum.LernerIndexCalibrationFactor

    MinLernerIndex = plx_enums.SystemRSIsEnum.MinLernerIndex

    MaxLernerIndex = plx_enums.SystemRSIsEnum.MaxLernerIndex


class SystemRegionsEnum(Enum):
    GeneratorSettlementModel = plx_enums.SystemRegionsEnum.GeneratorSettlementModel

    LoadSettlementModel = plx_enums.SystemRegionsEnum.LoadSettlementModel

    UniformPricingPumpedStoragePriceSetting = plx_enums.SystemRegionsEnum.UniformPricingPumpedStoragePriceSetting

    UniformPricingRelaxTransmissionLimits = plx_enums.SystemRegionsEnum.UniformPricingRelaxTransmissionLimits

    UniformPricingRelaxGenericConstraints = plx_enums.SystemRegionsEnum.UniformPricingRelaxGenericConstraints

    UniformPricingRelaxGeneratorConstraints = plx_enums.SystemRegionsEnum.UniformPricingRelaxGeneratorConstraints

    UniformPricingRelaxAncillaryServices = plx_enums.SystemRegionsEnum.UniformPricingRelaxAncillaryServices

    UpliftEnabled = plx_enums.SystemRegionsEnum.UpliftEnabled

    UpliftCostBasis = plx_enums.SystemRegionsEnum.UpliftCostBasis

    UpliftCompatibility = plx_enums.SystemRegionsEnum.UpliftCompatibility

    UpliftAlpha = plx_enums.SystemRegionsEnum.UpliftAlpha

    UpliftBeta = plx_enums.SystemRegionsEnum.UpliftBeta

    UpliftDelta = plx_enums.SystemRegionsEnum.UpliftDelta

    UpliftIncludeStartCost = plx_enums.SystemRegionsEnum.UpliftIncludeStartCost

    UpliftIncludeNoLoadCost = plx_enums.SystemRegionsEnum.UpliftIncludeNoLoadCost

    UpliftDetectActiveMinStableLevelConstraints = plx_enums.SystemRegionsEnum.UpliftDetectActiveMinStableLevelConstraints

    UpliftDetectActiveRampConstraints = plx_enums.SystemRegionsEnum.UpliftDetectActiveRampConstraints

    IncludeinMarginalUnit = plx_enums.SystemRegionsEnum.IncludeinMarginalUnit

    IncludeinUplift = plx_enums.SystemRegionsEnum.IncludeinUplift

    ConstraintPaymentsEnabled = plx_enums.SystemRegionsEnum.ConstraintPaymentsEnabled

    ConstraintPaymentsCompatibility = plx_enums.SystemRegionsEnum.ConstraintPaymentsCompatibility

    LoadMeteringPoint = plx_enums.SystemRegionsEnum.LoadMeteringPoint

    LoadIncludesLosses = plx_enums.SystemRegionsEnum.LoadIncludesLosses

    AggregateTransmission = plx_enums.SystemRegionsEnum.AggregateTransmission

    PoolType = plx_enums.SystemRegionsEnum.PoolType

    MLFAdjustsOfferPrice = plx_enums.SystemRegionsEnum.MLFAdjustsOfferPrice

    MLFAdjustsBidPrice = plx_enums.SystemRegionsEnum.MLFAdjustsBidPrice

    MLFAdjustsNoLoadCost = plx_enums.SystemRegionsEnum.MLFAdjustsNoLoadCost

    MLFAdjustsStartCost = plx_enums.SystemRegionsEnum.MLFAdjustsStartCost

    IncludeinRegionSupply = plx_enums.SystemRegionsEnum.IncludeinRegionSupply

    TransmissionConstraintsEnabled = plx_enums.SystemRegionsEnum.TransmissionConstraintsEnabled

    TransmissionConstraintVoltageThreshold = plx_enums.SystemRegionsEnum.TransmissionConstraintVoltageThreshold

    TransmissionInterfaceConstraintsEnabled = plx_enums.SystemRegionsEnum.TransmissionInterfaceConstraintsEnabled

    EnforceTransmissionLimitsOnLinesInInterfaces = plx_enums.SystemRegionsEnum.EnforceTransmissionLimitsOnLinesInInterfaces

    TransmissionReportEnabled = plx_enums.SystemRegionsEnum.TransmissionReportEnabled

    TransmissionReportVoltageThreshold = plx_enums.SystemRegionsEnum.TransmissionReportVoltageThreshold

    TransmissionReportLinesInInterfaces = plx_enums.SystemRegionsEnum.TransmissionReportLinesInInterfaces

    TransmissionReportInjectionandLoadNodes = plx_enums.SystemRegionsEnum.TransmissionReportInjectionandLoadNodes

    ReportObjectsinRegion = plx_enums.SystemRegionsEnum.ReportObjectsinRegion

    WheelingMethod = plx_enums.SystemRegionsEnum.WheelingMethod

    Units = plx_enums.SystemRegionsEnum.Units

    Load = plx_enums.SystemRegionsEnum.Load

    LoadScalar = plx_enums.SystemRegionsEnum.LoadScalar

    FixedLoad = plx_enums.SystemRegionsEnum.FixedLoad

    FixedGeneration = plx_enums.SystemRegionsEnum.FixedGeneration

    VoLL = plx_enums.SystemRegionsEnum.VoLL

    PriceofDumpEnergy = plx_enums.SystemRegionsEnum.PriceofDumpEnergy

    PriceCap = plx_enums.SystemRegionsEnum.PriceCap

    PriceFloor = plx_enums.SystemRegionsEnum.PriceFloor

    Price = plx_enums.SystemRegionsEnum.Price

    WheelingCharge = plx_enums.SystemRegionsEnum.WheelingCharge

    FixedCostScalar = plx_enums.SystemRegionsEnum.FixedCostScalar

    Elasticity = plx_enums.SystemRegionsEnum.Elasticity

    ReferenceLoad = plx_enums.SystemRegionsEnum.ReferenceLoad

    DSPBidQuantity = plx_enums.SystemRegionsEnum.DSPBidQuantity

    DSPBidPrice = plx_enums.SystemRegionsEnum.DSPBidPrice

    IsStrategic = plx_enums.SystemRegionsEnum.IsStrategic

    MaxMaintenance = plx_enums.SystemRegionsEnum.MaxMaintenance

    MaintenanceFactor = plx_enums.SystemRegionsEnum.MaintenanceFactor

    PeakPeriod = plx_enums.SystemRegionsEnum.PeakPeriod

    FirmCapacityIncr = plx_enums.SystemRegionsEnum.FirmCapacityIncr

    MinCapacityReserves = plx_enums.SystemRegionsEnum.MinCapacityReserves

    MaxCapacityReserves = plx_enums.SystemRegionsEnum.MaxCapacityReserves

    MinCapacityReserveMargin = plx_enums.SystemRegionsEnum.MinCapacityReserveMargin

    MaxCapacityReserveMargin = plx_enums.SystemRegionsEnum.MaxCapacityReserveMargin

    MinNativeCapacityReserves = plx_enums.SystemRegionsEnum.MinNativeCapacityReserves

    MinNativeCapacityReserveMargin = plx_enums.SystemRegionsEnum.MinNativeCapacityReserveMargin

    CapacityShortagePrice = plx_enums.SystemRegionsEnum.CapacityShortagePrice

    CapacityExcessPrice = plx_enums.SystemRegionsEnum.CapacityExcessPrice

    CapacityPriceCap = plx_enums.SystemRegionsEnum.CapacityPriceCap

    CapacityPriceFloor = plx_enums.SystemRegionsEnum.CapacityPriceFloor

    LOLPTarget = plx_enums.SystemRegionsEnum.LOLPTarget

    x = plx_enums.SystemRegionsEnum.x

    y = plx_enums.SystemRegionsEnum.y

    z = plx_enums.SystemRegionsEnum.z


class SystemReservesEnum(Enum):
    Type = plx_enums.SystemReservesEnum.Type

    MutuallyExclusive = plx_enums.SystemReservesEnum.MutuallyExclusive

    DynamicRisk = plx_enums.SystemReservesEnum.DynamicRisk

    CostAllocationModel = plx_enums.SystemReservesEnum.CostAllocationModel

    IsEnabled = plx_enums.SystemReservesEnum.IsEnabled

    IncludeinLTPlan = plx_enums.SystemReservesEnum.IncludeinLTPlan

    IncludeinMTSchedule = plx_enums.SystemReservesEnum.IncludeinMTSchedule

    IncludeinSTSchedule = plx_enums.SystemReservesEnum.IncludeinSTSchedule

    UnitCommitment = plx_enums.SystemReservesEnum.UnitCommitment

    SharingEnabled = plx_enums.SystemReservesEnum.SharingEnabled

    SharingLossesEnabled = plx_enums.SystemReservesEnum.SharingLossesEnabled

    MinProvision = plx_enums.SystemReservesEnum.MinProvision

    StaticRisk = plx_enums.SystemReservesEnum.StaticRisk

    Timeframe = plx_enums.SystemReservesEnum.Timeframe

    Duration = plx_enums.SystemReservesEnum.Duration

    MaxProvision = plx_enums.SystemReservesEnum.MaxProvision

    RiskAdjustmentFactor = plx_enums.SystemReservesEnum.RiskAdjustmentFactor

    EnergyUsage = plx_enums.SystemReservesEnum.EnergyUsage

    VoRS = plx_enums.SystemReservesEnum.VoRS

    PriceCap = plx_enums.SystemReservesEnum.PriceCap

    PriceFloor = plx_enums.SystemReservesEnum.PriceFloor

    CutoffSize = plx_enums.SystemReservesEnum.CutoffSize

    Price = plx_enums.SystemReservesEnum.Price

    x = plx_enums.SystemReservesEnum.x

    y = plx_enums.SystemReservesEnum.y

    z = plx_enums.SystemReservesEnum.z


class SystemStoragesEnum(Enum):

    Model = plx_enums.SystemStoragesEnum.Model

    BalancePeriod = plx_enums.SystemStoragesEnum.BalancePeriod

    InternalVolumeScalar = plx_enums.SystemStoragesEnum.InternalVolumeScalar

    EndEffectsMethod = plx_enums.SystemStoragesEnum.EndEffectsMethod

    RecyclePenalty = plx_enums.SystemStoragesEnum.RecyclePenalty

    DecompositionMethod = plx_enums.SystemStoragesEnum.DecompositionMethod

    DecompositionPenaltya = plx_enums.SystemStoragesEnum.DecompositionPenaltya

    DecompositionPenaltyb = plx_enums.SystemStoragesEnum.DecompositionPenaltyb

    DecompositionPenaltyc = plx_enums.SystemStoragesEnum.DecompositionPenaltyc

    DecompositionPenaltyx = plx_enums.SystemStoragesEnum.DecompositionPenaltyx

    DecompositionBoundPenalty = plx_enums.SystemStoragesEnum.DecompositionBoundPenalty

    EnforceBounds = plx_enums.SystemStoragesEnum.EnforceBounds

    SpillPenalty = plx_enums.SystemStoragesEnum.SpillPenalty

    NonphysicalInflowPenalty = plx_enums.SystemStoragesEnum.NonphysicalInflowPenalty

    NonphysicalSpillPenalty = plx_enums.SystemStoragesEnum.NonphysicalSpillPenalty

    Units = plx_enums.SystemStoragesEnum.Units

    MaxVolume = plx_enums.SystemStoragesEnum.MaxVolume

    InitialVolume = plx_enums.SystemStoragesEnum.InitialVolume

    MinVolume = plx_enums.SystemStoragesEnum.MinVolume

    MaxLevel = plx_enums.SystemStoragesEnum.MaxLevel

    InitialLevel = plx_enums.SystemStoragesEnum.InitialLevel

    MinLevel = plx_enums.SystemStoragesEnum.MinLevel

    LowRefLevel = plx_enums.SystemStoragesEnum.LowRefLevel

    LowRefArea = plx_enums.SystemStoragesEnum.LowRefArea

    HighRefLevel = plx_enums.SystemStoragesEnum.HighRefLevel

    HighRefArea = plx_enums.SystemStoragesEnum.HighRefArea

    NaturalInflow = plx_enums.SystemStoragesEnum.NaturalInflow

    NaturalInflowIncr = plx_enums.SystemStoragesEnum.NaturalInflowIncr

    NaturalInflowScalar = plx_enums.SystemStoragesEnum.NaturalInflowScalar

    WaterValue = plx_enums.SystemStoragesEnum.WaterValue

    EnergyValue = plx_enums.SystemStoragesEnum.EnergyValue

    WaterValuePoint = plx_enums.SystemStoragesEnum.WaterValuePoint

    DownstreamEfficiency = plx_enums.SystemStoragesEnum.DownstreamEfficiency

    LossRate = plx_enums.SystemStoragesEnum.LossRate

    MinRelease = plx_enums.SystemStoragesEnum.MinRelease

    MaxRelease = plx_enums.SystemStoragesEnum.MaxRelease

    MaxGeneratorRelease = plx_enums.SystemStoragesEnum.MaxGeneratorRelease

    MinReleasePenalty = plx_enums.SystemStoragesEnum.MinReleasePenalty

    MaxReleasePenalty = plx_enums.SystemStoragesEnum.MaxReleasePenalty

    MaxSpill = plx_enums.SystemStoragesEnum.MaxSpill

    MaxRamp = plx_enums.SystemStoragesEnum.MaxRamp

    MaxRampPenalty = plx_enums.SystemStoragesEnum.MaxRampPenalty

    Target = plx_enums.SystemStoragesEnum.Target

    TargetLevel = plx_enums.SystemStoragesEnum.TargetLevel

    TargetPenalty = plx_enums.SystemStoragesEnum.TargetPenalty

    TrajectoryNonanticipativity = plx_enums.SystemStoragesEnum.TrajectoryNonanticipativity

    TrajectoryNonanticipativityVolume = plx_enums.SystemStoragesEnum.TrajectoryNonanticipativityVolume

    TrajectoryNonanticipativityTime = plx_enums.SystemStoragesEnum.TrajectoryNonanticipativityTime

    x = plx_enums.SystemStoragesEnum.x

    y = plx_enums.SystemStoragesEnum.y

    z = plx_enums.SystemStoragesEnum.z


class SystemTimeslicesEnum(Enum):
    Include = plx_enums.SystemTimeslicesEnum.Include


class SystemTransformersEnum(Enum):
    MustReport = plx_enums.SystemTransformersEnum.MustReport

    EnforceLimits = plx_enums.SystemTransformersEnum.EnforceLimits

    FormulateUpfront = plx_enums.SystemTransformersEnum.FormulateUpfront

    Units = plx_enums.SystemTransformersEnum.Units

    Rating = plx_enums.SystemTransformersEnum.Rating

    OverloadRating = plx_enums.SystemTransformersEnum.OverloadRating

    LimitPenalty = plx_enums.SystemTransformersEnum.LimitPenalty

    Resistance = plx_enums.SystemTransformersEnum.Resistance

    Reactance = plx_enums.SystemTransformersEnum.Reactance

    Susceptance = plx_enums.SystemTransformersEnum.Susceptance

    LossAllocation = plx_enums.SystemTransformersEnum.LossAllocation

    FixedLoss = plx_enums.SystemTransformersEnum.FixedLoss

    UnitsOut = plx_enums.SystemTransformersEnum.UnitsOut

    x = plx_enums.SystemTransformersEnum.x

    y = plx_enums.SystemTransformersEnum.y

    z = plx_enums.SystemTransformersEnum.z


class SystemTransmissionRightsEnum(Enum):
    Type = plx_enums.SystemTransmissionRightsEnum.Type

    SettlementModel = plx_enums.SystemTransmissionRightsEnum.SettlementModel

    PricingMethod = plx_enums.SystemTransmissionRightsEnum.PricingMethod

    Units = plx_enums.SystemTransmissionRightsEnum.Units

    Quantity = plx_enums.SystemTransmissionRightsEnum.Quantity

    RentalShare = plx_enums.SystemTransmissionRightsEnum.RentalShare

    RentalBackShare = plx_enums.SystemTransmissionRightsEnum.RentalBackShare

    Price = plx_enums.SystemTransmissionRightsEnum.Price


class SystemVariablesEnum(Enum):
    RandomNumberSeed = plx_enums.SystemVariablesEnum.RandomNumberSeed

    SamplingMethod = plx_enums.SystemVariablesEnum.SamplingMethod

    SamplingFrequency = plx_enums.SystemVariablesEnum.SamplingFrequency

    SamplingPeriodType = plx_enums.SystemVariablesEnum.SamplingPeriodType

    DistributionType = plx_enums.SystemVariablesEnum.DistributionType

    Condition = plx_enums.SystemVariablesEnum.Condition

    ConditionLogic = plx_enums.SystemVariablesEnum.ConditionLogic

    IncludeinLTPlan = plx_enums.SystemVariablesEnum.IncludeinLTPlan

    IncludeinPASA = plx_enums.SystemVariablesEnum.IncludeinPASA

    IncludeinMTSchedule = plx_enums.SystemVariablesEnum.IncludeinMTSchedule

    IncludeinSTSchedule = plx_enums.SystemVariablesEnum.IncludeinSTSchedule

    Profile = plx_enums.SystemVariablesEnum.Profile

    MinValue = plx_enums.SystemVariablesEnum.MinValue

    MaxValue = plx_enums.SystemVariablesEnum.MaxValue

    Probability = plx_enums.SystemVariablesEnum.Probability

    ErrorStdDev = plx_enums.SystemVariablesEnum.ErrorStdDev

    AbsErrorStdDev = plx_enums.SystemVariablesEnum.AbsErrorStdDev

    MinValueStdDev = plx_enums.SystemVariablesEnum.MinValueStdDev

    MaxValueStdDev = plx_enums.SystemVariablesEnum.MaxValueStdDev

    AutoCorrelation = plx_enums.SystemVariablesEnum.AutoCorrelation

    MeanReversion = plx_enums.SystemVariablesEnum.MeanReversion

    ARIMAalpha = plx_enums.SystemVariablesEnum.ARIMAalpha

    ARIMAbeta = plx_enums.SystemVariablesEnum.ARIMAbeta

    ARIMAd = plx_enums.SystemVariablesEnum.ARIMAd

    JumpFrequency = plx_enums.SystemVariablesEnum.JumpFrequency

    JumpMagnitude = plx_enums.SystemVariablesEnum.JumpMagnitude

    JumpErrorStdDev = plx_enums.SystemVariablesEnum.JumpErrorStdDev

    GARCHalpha = plx_enums.SystemVariablesEnum.GARCHalpha

    GARCHbeta = plx_enums.SystemVariablesEnum.GARCHbeta

    GARCHomega = plx_enums.SystemVariablesEnum.GARCHomega

    Lookupx = plx_enums.SystemVariablesEnum.Lookupx

    Lookupy = plx_enums.SystemVariablesEnum.Lookupy

    LookupUnit = plx_enums.SystemVariablesEnum.LookupUnit

    Sampling = plx_enums.SystemVariablesEnum.Sampling

    StepHourActiveFrom = plx_enums.SystemVariablesEnum.StepHourActiveFrom

    StepHoursActive = plx_enums.SystemVariablesEnum.StepHoursActive

    CompoundIndex = plx_enums.SystemVariablesEnum.CompoundIndex


class SystemWaterDemandsEnum(Enum):
    Demand = plx_enums.SystemWaterDemandsEnum.Demand

    ShortagePrice = plx_enums.SystemWaterDemandsEnum.ShortagePrice

    ExcessPrice = plx_enums.SystemWaterDemandsEnum.ExcessPrice

    BidQuantity = plx_enums.SystemWaterDemandsEnum.BidQuantity

    BidPrice = plx_enums.SystemWaterDemandsEnum.BidPrice

    x = plx_enums.SystemWaterDemandsEnum.x

    y = plx_enums.SystemWaterDemandsEnum.y

    z = plx_enums.SystemWaterDemandsEnum.z


class SystemWaterNodesEnum(Enum):
    ExpansionOptimality = plx_enums.SystemWaterNodesEnum.ExpansionOptimality

    Units = plx_enums.SystemWaterNodesEnum.Units

    WaterSecurity = plx_enums.SystemWaterNodesEnum.WaterSecurity

    FOMCharge = plx_enums.SystemWaterNodesEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemWaterNodesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemWaterNodesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemWaterNodesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemWaterNodesEnum.TechnicalLife

    BuildCost = plx_enums.SystemWaterNodesEnum.BuildCost

    WACC = plx_enums.SystemWaterNodesEnum.WACC

    EconomicLife = plx_enums.SystemWaterNodesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemWaterNodesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemWaterNodesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemWaterNodesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemWaterNodesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemWaterNodesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemWaterNodesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemWaterNodesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemWaterNodesEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemWaterNodesEnum.x

    y = plx_enums.SystemWaterNodesEnum.y

    z = plx_enums.SystemWaterNodesEnum.z


class SystemWaterPipelinesEnum(Enum):
    RandomNumberSeed = plx_enums.SystemWaterPipelinesEnum.RandomNumberSeed

    RepairTimeDistribution = plx_enums.SystemWaterPipelinesEnum.RepairTimeDistribution

    ExpansionOptimality = plx_enums.SystemWaterPipelinesEnum.ExpansionOptimality

    Units = plx_enums.SystemWaterPipelinesEnum.Units

    MaxCapacity = plx_enums.SystemWaterPipelinesEnum.MaxCapacity

    Diameter = plx_enums.SystemWaterPipelinesEnum.Diameter

    Roughness = plx_enums.SystemWaterPipelinesEnum.Roughness

    Length = plx_enums.SystemWaterPipelinesEnum.Length

    PumpEfficiency = plx_enums.SystemWaterPipelinesEnum.PumpEfficiency

    VOMCharge = plx_enums.SystemWaterPipelinesEnum.VOMCharge

    FOMCharge = plx_enums.SystemWaterPipelinesEnum.FOMCharge

    ConsumptionAllocation = plx_enums.SystemWaterPipelinesEnum.ConsumptionAllocation

    UnitsOut = plx_enums.SystemWaterPipelinesEnum.UnitsOut

    MaintenanceRate = plx_enums.SystemWaterPipelinesEnum.MaintenanceRate

    MaintenanceFrequency = plx_enums.SystemWaterPipelinesEnum.MaintenanceFrequency

    ForcedOutageRate = plx_enums.SystemWaterPipelinesEnum.ForcedOutageRate

    OutageRating = plx_enums.SystemWaterPipelinesEnum.OutageRating

    MeanTimetoRepair = plx_enums.SystemWaterPipelinesEnum.MeanTimetoRepair

    MinTimeToRepair = plx_enums.SystemWaterPipelinesEnum.MinTimeToRepair

    MaxTimeToRepair = plx_enums.SystemWaterPipelinesEnum.MaxTimeToRepair

    RepairTimeShape = plx_enums.SystemWaterPipelinesEnum.RepairTimeShape

    RepairTimeScale = plx_enums.SystemWaterPipelinesEnum.RepairTimeScale

    MaxUnitsBuilt = plx_enums.SystemWaterPipelinesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemWaterPipelinesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemWaterPipelinesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemWaterPipelinesEnum.TechnicalLife

    BuildCost = plx_enums.SystemWaterPipelinesEnum.BuildCost

    WACC = plx_enums.SystemWaterPipelinesEnum.WACC

    EconomicLife = plx_enums.SystemWaterPipelinesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemWaterPipelinesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemWaterPipelinesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemWaterPipelinesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemWaterPipelinesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemWaterPipelinesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemWaterPipelinesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemWaterPipelinesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemWaterPipelinesEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemWaterPipelinesEnum.x

    y = plx_enums.SystemWaterPipelinesEnum.y

    z = plx_enums.SystemWaterPipelinesEnum.z


class SystemWaterPlantsEnum(Enum):
    ExpansionOptimality = plx_enums.SystemWaterPlantsEnum.ExpansionOptimality

    Units = plx_enums.SystemWaterPlantsEnum.Units

    MaxCapacity = plx_enums.SystemWaterPlantsEnum.MaxCapacity

    MinStableProduction = plx_enums.SystemWaterPlantsEnum.MinStableProduction

    AuxFixed = plx_enums.SystemWaterPlantsEnum.AuxFixed

    AuxBase = plx_enums.SystemWaterPlantsEnum.AuxBase

    AuxIncr = plx_enums.SystemWaterPlantsEnum.AuxIncr

    HeatUsage = plx_enums.SystemWaterPlantsEnum.HeatUsage

    WaterYield = plx_enums.SystemWaterPlantsEnum.WaterYield

    EnergyUsage = plx_enums.SystemWaterPlantsEnum.EnergyUsage

    VOMCharge = plx_enums.SystemWaterPlantsEnum.VOMCharge

    FOMCharge = plx_enums.SystemWaterPlantsEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemWaterPlantsEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemWaterPlantsEnum.LeadTime

    ProjectStartDate = plx_enums.SystemWaterPlantsEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemWaterPlantsEnum.TechnicalLife

    BuildCost = plx_enums.SystemWaterPlantsEnum.BuildCost

    WACC = plx_enums.SystemWaterPlantsEnum.WACC

    EconomicLife = plx_enums.SystemWaterPlantsEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemWaterPlantsEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemWaterPlantsEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemWaterPlantsEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemWaterPlantsEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemWaterPlantsEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemWaterPlantsEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemWaterPlantsEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemWaterPlantsEnum.MinUnitsRetiredinYear

    x = plx_enums.SystemWaterPlantsEnum.x

    y = plx_enums.SystemWaterPlantsEnum.y

    z = plx_enums.SystemWaterPlantsEnum.z


class SystemWaterStoragesEnum(Enum):
    EnforceBounds = plx_enums.SystemWaterStoragesEnum.EnforceBounds

    ExpansionOptimality = plx_enums.SystemWaterStoragesEnum.ExpansionOptimality

    Units = plx_enums.SystemWaterStoragesEnum.Units

    MaxVolume = plx_enums.SystemWaterStoragesEnum.MaxVolume

    MinVolume = plx_enums.SystemWaterStoragesEnum.MinVolume

    InitialVolume = plx_enums.SystemWaterStoragesEnum.InitialVolume

    Target = plx_enums.SystemWaterStoragesEnum.Target

    TargetPenalty = plx_enums.SystemWaterStoragesEnum.TargetPenalty

    EnergyUsage = plx_enums.SystemWaterStoragesEnum.EnergyUsage

    NaturalInflow = plx_enums.SystemWaterStoragesEnum.NaturalInflow

    LossRate = plx_enums.SystemWaterStoragesEnum.LossRate

    FOMCharge = plx_enums.SystemWaterStoragesEnum.FOMCharge

    MaxUnitsBuilt = plx_enums.SystemWaterStoragesEnum.MaxUnitsBuilt

    LeadTime = plx_enums.SystemWaterStoragesEnum.LeadTime

    ProjectStartDate = plx_enums.SystemWaterStoragesEnum.ProjectStartDate

    TechnicalLife = plx_enums.SystemWaterStoragesEnum.TechnicalLife

    BuildCost = plx_enums.SystemWaterStoragesEnum.BuildCost

    WACC = plx_enums.SystemWaterStoragesEnum.WACC

    EconomicLife = plx_enums.SystemWaterStoragesEnum.EconomicLife

    MinUnitsBuilt = plx_enums.SystemWaterStoragesEnum.MinUnitsBuilt

    MaxUnitsBuiltinYear = plx_enums.SystemWaterStoragesEnum.MaxUnitsBuiltinYear

    MinUnitsBuiltinYear = plx_enums.SystemWaterStoragesEnum.MinUnitsBuiltinYear

    MaxUnitsRetired = plx_enums.SystemWaterStoragesEnum.MaxUnitsRetired

    RetirementCost = plx_enums.SystemWaterStoragesEnum.RetirementCost

    MinUnitsRetired = plx_enums.SystemWaterStoragesEnum.MinUnitsRetired

    MaxUnitsRetiredinYear = plx_enums.SystemWaterStoragesEnum.MaxUnitsRetiredinYear

    MinUnitsRetiredinYear = plx_enums.SystemWaterStoragesEnum.MinUnitsRetiredinYear

    TrajectoryNonanticipativity = plx_enums.SystemWaterStoragesEnum.TrajectoryNonanticipativity

    TrajectoryNonanticipativityVolume = plx_enums.SystemWaterStoragesEnum.TrajectoryNonanticipativityVolume

    TrajectoryNonanticipativityTime = plx_enums.SystemWaterStoragesEnum.TrajectoryNonanticipativityTime

    x = plx_enums.SystemWaterStoragesEnum.x

    y = plx_enums.SystemWaterStoragesEnum.y

    z = plx_enums.SystemWaterStoragesEnum.z


class SystemWaterZonesEnum(Enum):
    x = plx_enums.SystemWaterZonesEnum.x

    y = plx_enums.SystemWaterZonesEnum.y

    z = plx_enums.SystemWaterZonesEnum.z


class SystemWaterwaysEnum(Enum):
    TraversalTime = plx_enums.SystemWaterwaysEnum.TraversalTime

    FlowControl = plx_enums.SystemWaterwaysEnum.FlowControl

    MaxFlow = plx_enums.SystemWaterwaysEnum.MaxFlow

    MinFlow = plx_enums.SystemWaterwaysEnum.MinFlow

    InitialFlow = plx_enums.SystemWaterwaysEnum.InitialFlow

    MaxRamp = plx_enums.SystemWaterwaysEnum.MaxRamp

    MaxFlowPenalty = plx_enums.SystemWaterwaysEnum.MaxFlowPenalty

    MinFlowPenalty = plx_enums.SystemWaterwaysEnum.MinFlowPenalty

    MaxRampPenalty = plx_enums.SystemWaterwaysEnum.MaxRampPenalty

    InputScalar = plx_enums.SystemWaterwaysEnum.InputScalar

    OutputScalar = plx_enums.SystemWaterwaysEnum.OutputScalar

    x = plx_enums.SystemWaterwaysEnum.x

    y = plx_enums.SystemWaterwaysEnum.y

    z = plx_enums.SystemWaterwaysEnum.z


class SystemZonesEnum(Enum):
    LoadSettlementModel = plx_enums.SystemZonesEnum.LoadSettlementModel

    WheelingMethod = plx_enums.SystemZonesEnum.WheelingMethod

    Units = plx_enums.SystemZonesEnum.Units

    Load = plx_enums.SystemZonesEnum.Load

    LoadParticipationFactor = plx_enums.SystemZonesEnum.LoadParticipationFactor

    LoadScalar = plx_enums.SystemZonesEnum.LoadScalar

    WheelingCharge = plx_enums.SystemZonesEnum.WheelingCharge

    MaxMaintenance = plx_enums.SystemZonesEnum.MaxMaintenance

    MaintenanceFactor = plx_enums.SystemZonesEnum.MaintenanceFactor

    PeakPeriod = plx_enums.SystemZonesEnum.PeakPeriod

    FirmCapacityIncr = plx_enums.SystemZonesEnum.FirmCapacityIncr

    MinCapacityReserves = plx_enums.SystemZonesEnum.MinCapacityReserves

    MaxCapacityReserves = plx_enums.SystemZonesEnum.MaxCapacityReserves

    MinCapacityReserveMargin = plx_enums.SystemZonesEnum.MinCapacityReserveMargin

    MaxCapacityReserveMargin = plx_enums.SystemZonesEnum.MaxCapacityReserveMargin

    MinNativeCapacityReserves = plx_enums.SystemZonesEnum.MinNativeCapacityReserves

    MinNativeCapacityReserveMargin = plx_enums.SystemZonesEnum.MinNativeCapacityReserveMargin

    CapacityShortagePrice = plx_enums.SystemZonesEnum.CapacityShortagePrice

    CapacityExcessPrice = plx_enums.SystemZonesEnum.CapacityExcessPrice

    CapacityPriceCap = plx_enums.SystemZonesEnum.CapacityPriceCap

    CapacityPriceFloor = plx_enums.SystemZonesEnum.CapacityPriceFloor

    LOLPTarget = plx_enums.SystemZonesEnum.LOLPTarget

    x = plx_enums.SystemZonesEnum.x

    y = plx_enums.SystemZonesEnum.y

    z = plx_enums.SystemZonesEnum.z


class TransformerEnforceLimitsEnum(Enum):
    Never = plx_enums.TransformerEnforceLimitsEnum.Never

    Voltage = plx_enums.TransformerEnforceLimitsEnum.Voltage

    Always = plx_enums.TransformerEnforceLimitsEnum.Always

    Contingency = plx_enums.TransformerEnforceLimitsEnum.Contingency


class TransmissionAttributeEnum(Enum):
    MVABase = plx_enums.TransmissionAttributeEnum.MVABase

    OPFMethod = plx_enums.TransmissionAttributeEnum.OPFMethod

    ConstraintsEnabled = plx_enums.TransmissionAttributeEnum.ConstraintsEnabled

    FormulateUpfront = plx_enums.TransmissionAttributeEnum.FormulateUpfront

    ConstraintVoltageThreshold = plx_enums.TransmissionAttributeEnum.ConstraintVoltageThreshold

    InterfaceConstraintsEnabled = plx_enums.TransmissionAttributeEnum.InterfaceConstraintsEnabled

    EnforceLimitsOnLinesInInterfaces = plx_enums.TransmissionAttributeEnum.EnforceLimitsOnLinesInInterfaces

    LossesEnabled = plx_enums.TransmissionAttributeEnum.LossesEnabled

    LossVoltageThreshold = plx_enums.TransmissionAttributeEnum.LossVoltageThreshold

    LossMethod = plx_enums.TransmissionAttributeEnum.LossMethod

    MaxLossRelativeError = plx_enums.TransmissionAttributeEnum.MaxLossRelativeError

    MaxLossAbsoluteError = plx_enums.TransmissionAttributeEnum.MaxLossAbsoluteError

    MaxLossTranches = plx_enums.TransmissionAttributeEnum.MaxLossTranches

    LossTolerance = plx_enums.TransmissionAttributeEnum.LossTolerance

    MaxLossIterations = plx_enums.TransmissionAttributeEnum.MaxLossIterations

    MaxEmbeddedLossIterations = plx_enums.TransmissionAttributeEnum.MaxEmbeddedLossIterations

    DetectNonphysicalLosses = plx_enums.TransmissionAttributeEnum.DetectNonphysicalLosses

    PTDFMethod = plx_enums.TransmissionAttributeEnum.PTDFMethod

    FlowPTDFThreshold = plx_enums.TransmissionAttributeEnum.FlowPTDFThreshold

    WheelingPTDFThreshold = plx_enums.TransmissionAttributeEnum.WheelingPTDFThreshold

    CacheTransmissionMatrices = plx_enums.TransmissionAttributeEnum.CacheTransmissionMatrices

    ReactanceCutoff = plx_enums.TransmissionAttributeEnum.ReactanceCutoff

    AllowDumpEnergy = plx_enums.TransmissionAttributeEnum.AllowDumpEnergy

    AllowUnservedEnergy = plx_enums.TransmissionAttributeEnum.AllowUnservedEnergy

    BoundNodePhaseAngles = plx_enums.TransmissionAttributeEnum.BoundNodePhaseAngles

    MaxAbsolutePhaseAngle = plx_enums.TransmissionAttributeEnum.MaxAbsolutePhaseAngle

    InternalVoLL = plx_enums.TransmissionAttributeEnum.InternalVoLL

    USEThreshold = plx_enums.TransmissionAttributeEnum.USEThreshold

    RentalMethod = plx_enums.TransmissionAttributeEnum.RentalMethod

    InterruptionSharing = plx_enums.TransmissionAttributeEnum.InterruptionSharing

    ReportEnabled = plx_enums.TransmissionAttributeEnum.ReportEnabled

    ReportVoltageThreshold = plx_enums.TransmissionAttributeEnum.ReportVoltageThreshold

    ReportLinesInInterfaces = plx_enums.TransmissionAttributeEnum.ReportLinesInInterfaces

    ReportAllInterregionalFlows = plx_enums.TransmissionAttributeEnum.ReportAllInterregionalFlows

    ReportAllInterzonalFlows = plx_enums.TransmissionAttributeEnum.ReportAllInterzonalFlows

    ReportInjectionandLoadNodes = plx_enums.TransmissionAttributeEnum.ReportInjectionandLoadNodes

    ConvergenceReportLevel = plx_enums.TransmissionAttributeEnum.ConvergenceReportLevel

    SCUCEnabled = plx_enums.TransmissionAttributeEnum.SCUCEnabled

    SCUCConstraintVoltageThreshold = plx_enums.TransmissionAttributeEnum.SCUCConstraintVoltageThreshold

    SCUCInterfaceConstraintsEnabled = plx_enums.TransmissionAttributeEnum.SCUCInterfaceConstraintsEnabled

    EnforceN1Contingencies = plx_enums.TransmissionAttributeEnum.EnforceN1Contingencies

    N1ContingencyVoltageThreshold = plx_enums.TransmissionAttributeEnum.N1ContingencyVoltageThreshold

    ContingencyMonitoringThreshold = plx_enums.TransmissionAttributeEnum.ContingencyMonitoringThreshold

    LimitThreshold = plx_enums.TransmissionAttributeEnum.LimitThreshold

    LimitBootstrapInitialThreshold = plx_enums.TransmissionAttributeEnum.LimitBootstrapInitialThreshold

    LimitBootstrapThresholdDecrement = plx_enums.TransmissionAttributeEnum.LimitBootstrapThresholdDecrement

    MaxLimitIterations = plx_enums.TransmissionAttributeEnum.MaxLimitIterations

    NetworkReduction = plx_enums.TransmissionAttributeEnum.NetworkReduction


class TransmissionConvergenceReportLevelEnum(Enum):
    None_ = 0

    Normal = plx_enums.TransmissionConvergenceReportLevelEnum.Normal

    Verbose = plx_enums.TransmissionConvergenceReportLevelEnum.Verbose


class TransmissionDetailEnum(Enum):
    Regional = plx_enums.TransmissionDetailEnum.Regional

    Nodal = plx_enums.TransmissionDetailEnum.Nodal

    Zonal = plx_enums.TransmissionDetailEnum.Zonal


class TransmissionOPFMethodEnum(Enum):
    Standard = plx_enums.TransmissionOPFMethodEnum.Standard

    LargeScale = plx_enums.TransmissionOPFMethodEnum.LargeScale


class TransmissionPTDFMethodEnum(Enum):
    SlackBus = plx_enums.TransmissionPTDFMethodEnum.SlackBus

    DistributedLoadSlackReference = plx_enums.TransmissionPTDFMethodEnum.DistributedLoadSlackReference

    DistributedGenerationSlackCapacity = plx_enums.TransmissionPTDFMethodEnum.DistributedGenerationSlackCapacity

    DistributedGenerationSlackReference = plx_enums.TransmissionPTDFMethodEnum.DistributedGenerationSlackReference


class TransmissionPTDFResolutionEnum(Enum):
    Nodal = plx_enums.TransmissionPTDFResolutionEnum.Nodal

    Zonal = plx_enums.TransmissionPTDFResolutionEnum.Zonal

    Regional = plx_enums.TransmissionPTDFResolutionEnum.Regional


class TransmissionRentalMethodEnum(Enum):
    PointToPoint = plx_enums.TransmissionRentalMethodEnum.PointToPoint

    FlowGate = plx_enums.TransmissionRentalMethodEnum.FlowGate


class TransmissionRightCompaniesEnum(Enum):
    Share = plx_enums.TransmissionRightCompaniesEnum.Share


class TransmissionRightsPricingMethodEnum(Enum):
    LMP = plx_enums.TransmissionRightsPricingMethodEnum.LMP

    CongestionCharge = plx_enums.TransmissionRightsPricingMethodEnum.CongestionCharge


class TransmissionRightsSettlementModelEnum(Enum):
    Buy = plx_enums.TransmissionRightsSettlementModelEnum.Buy

    Sell = plx_enums.TransmissionRightsSettlementModelEnum.Sell


class TransmissionRightsTypeEnum(Enum):
    SRA = plx_enums.TransmissionRightsTypeEnum.SRA

    FTR = plx_enums.TransmissionRightsTypeEnum.FTR


class TransmissionWheelingMethodEnum(Enum):
    Net = plx_enums.TransmissionWheelingMethodEnum.Net

    Gross = plx_enums.TransmissionWheelingMethodEnum.Gross


class UnitCommitmentEnum(Enum):
    Off = plx_enums.UnitCommitmentEnum.Off

    On = plx_enums.UnitCommitmentEnum.On

    Free = plx_enums.UnitCommitmentEnum.Free


class UnitsofDataEnum(Enum):
    Metric = plx_enums.UnitsofDataEnum.Metric

    Imperial = plx_enums.UnitsofDataEnum.Imperial


class UpliftCompatibilityEnum(Enum):
    Korea = plx_enums.UpliftCompatibilityEnum.Korea

    Ireland = plx_enums.UpliftCompatibilityEnum.Ireland

    Custom = plx_enums.UpliftCompatibilityEnum.Custom


class UpliftCostBasisEnum(Enum):
    CostBased = plx_enums.UpliftCostBasisEnum.CostBased

    BidBased = plx_enums.UpliftCostBasisEnum.BidBased


class VariableAttributeEnum(Enum):
    CompoundType = plx_enums.VariableAttributeEnum.CompoundType

    CompoundStartDate = plx_enums.VariableAttributeEnum.CompoundStartDate


class VariableCompoundTypeEnum(Enum):
    Nominal = plx_enums.VariableCompoundTypeEnum.Nominal

    Annual = plx_enums.VariableCompoundTypeEnum.Annual


class VariableConditionEnum(Enum):
    EQ = plx_enums.VariableConditionEnum.EQ

    GE = plx_enums.VariableConditionEnum.GE

    GT = plx_enums.VariableConditionEnum.GT

    None_ = 4

    LT = plx_enums.VariableConditionEnum.LT

    LE = plx_enums.VariableConditionEnum.LE


class VariableDistributionTypeEnum(Enum):
    Normal = plx_enums.VariableDistributionTypeEnum.Normal

    Lognormal = plx_enums.VariableDistributionTypeEnum.Lognormal


class VariableFuelsEnum(Enum):
    OfftakeCoefficient = plx_enums.VariableFuelsEnum.OfftakeCoefficient


class VariableGeneratorsEnum(Enum):
    GenerationCoefficient = plx_enums.VariableGeneratorsEnum.GenerationCoefficient

    UnitsGeneratingCoefficient = plx_enums.VariableGeneratorsEnum.UnitsGeneratingCoefficient

    UnitsStartedCoefficient = plx_enums.VariableGeneratorsEnum.UnitsStartedCoefficient

    UnitsSyncCondCoefficient = plx_enums.VariableGeneratorsEnum.UnitsSyncCondCoefficient

    FuelOfftakeCoefficient = plx_enums.VariableGeneratorsEnum.FuelOfftakeCoefficient

    UnitsOutCoefficient = plx_enums.VariableGeneratorsEnum.UnitsOutCoefficient


class VariableHeatNodesEnum(Enum):
    HeatFlowCoefficient = plx_enums.VariableHeatNodesEnum.HeatFlowCoefficient


class VariableHeatPlantsEnum(Enum):
    FuelOfftakeCoefficient = plx_enums.VariableHeatPlantsEnum.FuelOfftakeCoefficient


class VariableInterfacesEnum(Enum):
    FlowCoefficient = plx_enums.VariableInterfacesEnum.FlowCoefficient


class VariableLinesEnum(Enum):
    FlowCoefficient = plx_enums.VariableLinesEnum.FlowCoefficient

    FlowForwardCoefficient = plx_enums.VariableLinesEnum.FlowForwardCoefficient

    FlowBackCoefficient = plx_enums.VariableLinesEnum.FlowBackCoefficient

    FlowingForwardCoefficient = plx_enums.VariableLinesEnum.FlowingForwardCoefficient

    FlowingBackCoefficient = plx_enums.VariableLinesEnum.FlowingBackCoefficient


class VariableNodesEnum(Enum):
    LoadCoefficient = plx_enums.VariableNodesEnum.LoadCoefficient


class VariableRegionsEnum(Enum):
    LoadCoefficient = plx_enums.VariableRegionsEnum.LoadCoefficient

    CapacityReservesCoefficient = plx_enums.VariableRegionsEnum.CapacityReservesCoefficient

    PriceCoefficient = plx_enums.VariableRegionsEnum.PriceCoefficient


class VariableReservesEnum(Enum):
    ProvisionCoefficient = plx_enums.VariableReservesEnum.ProvisionCoefficient

    RiskCoefficient = plx_enums.VariableReservesEnum.RiskCoefficient

    ShortageCoefficient = plx_enums.VariableReservesEnum.ShortageCoefficient


class VariableSampleSourceEnum(Enum):
    AutoCorrelation = plx_enums.VariableSampleSourceEnum.AutoCorrelation

    MeanReversion = plx_enums.VariableSampleSourceEnum.MeanReversion

    ARIMA = plx_enums.VariableSampleSourceEnum.ARIMA

    RandomFromProfiles = plx_enums.VariableSampleSourceEnum.RandomFromProfiles

    InSequenceFromProfiles = plx_enums.VariableSampleSourceEnum.InSequenceFromProfiles

    Variable = plx_enums.VariableSampleSourceEnum.Variable

    TransformedARIMA = plx_enums.VariableSampleSourceEnum.TransformedARIMA

    None_ = -1


class VariableSamplingMethodEnum(Enum):
    None_ = 0

    Auto = plx_enums.VariableSamplingMethodEnum.Auto

    User = plx_enums.VariableSamplingMethodEnum.User


class VariableStoragesEnum(Enum):
    EndVolumeCoefficient = plx_enums.VariableStoragesEnum.EndVolumeCoefficient

    InflowCoefficient = plx_enums.VariableStoragesEnum.InflowCoefficient

    ReleaseCoefficient = plx_enums.VariableStoragesEnum.ReleaseCoefficient

    SpillCoefficient = plx_enums.VariableStoragesEnum.SpillCoefficient


class VariableVariablesEnum(Enum):
    Correlation = plx_enums.VariableVariablesEnum.Correlation

    ValueCoefficient = plx_enums.VariableVariablesEnum.ValueCoefficient


class VariableZonesEnum(Enum):
    LoadCoefficient = plx_enums.VariableZonesEnum.LoadCoefficient

    CapacityReservesCoefficient = plx_enums.VariableZonesEnum.CapacityReservesCoefficient


class WaterNodeAttributeEnum(Enum):
    Latitude = plx_enums.WaterNodeAttributeEnum.Latitude

    Longitude = plx_enums.WaterNodeAttributeEnum.Longitude


class WaterStorageAttributeEnum(Enum):
    Latitude = plx_enums.WaterStorageAttributeEnum.Latitude

    Longitude = plx_enums.WaterStorageAttributeEnum.Longitude


class WaterwayFlowControlEnum(Enum):
    Economic = plx_enums.WaterwayFlowControlEnum.Economic

    SpillOnly = plx_enums.WaterwayFlowControlEnum.SpillOnly


class ZoneZonesEnum(Enum):
    WheelingCharge = plx_enums.ZoneZonesEnum.WheelingCharge

    MaxFlow = plx_enums.ZoneZonesEnum.MaxFlow


class MessageActionEnum(Enum):
    Error = plx_enums.MessageActionEnum.Error

    Warn = plx_enums.MessageActionEnum.Warn

    WarnOnce = plx_enums.MessageActionEnum.WarnOnce

    Ignore = plx_enums.MessageActionEnum.Ignore


class Elements(Enum):
    COMPUTER = plx_enums.Elements.COMPUTER

    USERNAME = plx_enums.Elements.USERNAME

    PHYSICAL_MEMORY = plx_enums.Elements.PHYSICAL_MEMORY

    CPU_TYPE = plx_enums.Elements.CPU_TYPE

    CORE_COUNT = plx_enums.Elements.CORE_COUNT

    VERSION = plx_enums.Elements.VERSION

    SIMULATION_DATE = plx_enums.Elements.SIMULATION_DATE

    MODEL_NAME = plx_enums.Elements.MODEL_NAME

    MODEL_DESCRIPTION = plx_enums.Elements.MODEL_DESCRIPTION

    PHASES = plx_enums.Elements.PHASES

    CLASS_COUNT = plx_enums.Elements.CLASS_COUNT

    SOLVER = plx_enums.Elements.SOLVER

    PHASE_STEP_COUNT = plx_enums.Elements.PHASE_STEP_COUNT

    PHASE_DATE_RANGE = plx_enums.Elements.PHASE_DATE_RANGE

    PHASE_STEP_PERIOD_COUNT = plx_enums.Elements.PHASE_STEP_PERIOD_COUNT

    PERIODS_PER_DAY = plx_enums.Elements.PERIODS_PER_DAY

    PHASE_TIME = plx_enums.Elements.PHASE_TIME

    PHASE_PEAK_MEMORY = plx_enums.Elements.PHASE_PEAK_MEMORY

    PHASE_TASK_SIZE = plx_enums.Elements.PHASE_TASK_SIZE

    HARDWARE_ID = plx_enums.Elements.HARDWARE_ID

    EMAIL_ADDRESS = plx_enums.Elements.EMAIL_ADDRESS

    LICENSE_USERNAME = plx_enums.Elements.LICENSE_USERNAME

    MODEL_PROPERTIES = plx_enums.Elements.MODEL_PROPERTIES

    MODEL_REPORT = plx_enums.Elements.MODEL_REPORT

    MODEL_ERROR = plx_enums.Elements.MODEL_ERROR

    MODEL_COMPLETED_TIME = plx_enums.Elements.MODEL_COMPLETED_TIME

    COMPANY = plx_enums.Elements.COMPANY

