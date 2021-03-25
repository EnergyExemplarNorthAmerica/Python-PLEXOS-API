from enum import Enum


class AbatementConsumablesEnum(Enum):
    ConsumptionBase = 1
    ConsumptionIncr = 2


class AbatementEmissionsEnum(Enum):
    AbatementCost = 1
    Efficiency = 2
    MaxAbatement = 3


class AbatementGeneratorsEnum(Enum):
    GenerationParticipationFactor = 1


class ActionEnum(Enum):
    Equal = 0
    Multiply = 1
    Divide = 2
    Add = 3
    Subtract = 4
    RaisetoPower = 5
    Test = 6


class AggregationEnum(Enum):
    None_ = 0
    Category = 1
    All = 2


class AncillaryServicesCostAllocationModelEnum(Enum):
    None_ = 0
    Runway = 1
    ModifiedRunway = 2
    Prorata = 3


class AttributeIDEnum(Enum):
    Generator_Latitude = 1
    Generator_Longitude = 2
    Storage_Latitude = 3
    Storage_Longitude = 4
    Node_Latitude = 5
    Node_Longitude = 6
    Battery_Latitude = 7
    Battery_Longitude = 8
    GasStorage_Latitude = 9
    GasStorage_Longitude = 10
    GasNode_Latitude = 11
    GasNode_Longitude = 12
    WaterStorage_Latitude = 13
    WaterStorage_Longitude = 14
    WaterNode_Latitude = 15
    WaterNode_Longitude = 16
    Market_UnitCommitment = 17
    DecisionVariable_Type = 18
    DecisionVariable_TimeLag = 19
    DecisionVariable_TimeInvariant = 20
    List_Report = 21
    List_Filter = 22
    List_InclusiveEmpty = 23
    List_Transient = 24
    DataFile_Enabled = 25
    DataFile_GrowthPeriod = 26
    DataFile_Method = 27
    DataFile_RelativeGrowthatMin = 28
    DataFile_ShapeDistortion = 29
    DataFile_DecimalPlaces = 30
    DataFile_MissingValueMethod = 31
    DataFile_PeriodsperDay = 32
    DataFile_UpscalingMethod = 33
    DataFile_DownscalingMethod = 34
    DataFile_DatetimeConvention = 35
    DataFile_Locale = 36
    DataFile_TimeShift = 37
    DataFile_WeekBeginning = 38
    DataFile_HistoricalSampling = 39
    DataFile_HistoricalYearFrom = 40
    DataFile_HistoricalYearTo = 41
    DataFile_HistoricalYearStart = 42
    DataFile_HistoricalYearEnding = 43
    DataFile_HistoricalPeriodType = 44
    DataFile_BaseYear = 45
    Variable_CompoundType = 46
    Variable_CompoundStartDate = 47
    Horizon_PeriodsperDay = 48
    Horizon_DateFrom = 49
    Horizon_StepType = 50
    Horizon_StepCount = 51
    Horizon_DayBeginning = 52
    Horizon_WeekBeginning = 53
    Horizon_YearEnding = 54
    Horizon_Chronology = 55
    Horizon_TypicalWeek = 56
    Horizon_ChronoDateFrom = 57
    Horizon_ChronoPeriodFrom = 58
    Horizon_ChronoPeriodTo = 59
    Horizon_ChronoStepType = 60
    Horizon_ChronoAtaTime = 61
    Horizon_ChronoStepCount = 62
    Horizon_LookaheadIndicator = 63
    Horizon_LookaheadType = 64
    Horizon_LookaheadAtaTime = 65
    Horizon_LookaheadPeriodsperDay = 66
    Report_WriteDatabase = 67
    Report_WriteFlatFiles = 68
    Report_WriteXMLFiles = 69
    Report_XMLContent = 70
    Report_OutputResultsbyPeriod = 71
    Report_OutputResultsbyHour = 72
    Report_OutputResultsbyDay = 73
    Report_OutputResultsbyWeek = 74
    Report_OutputResultsbyMonth = 75
    Report_OutputResultsbyQuarter = 76
    Report_OutputResultsbyFiscalYear = 77
    Report_OutputStatistics = 78
    Report_OutputResultsbySample = 79
    Report_FilterObjectsByInterval = 80
    Report_FilterObjectsInSummary = 81
    Report_WholeYearsOnly = 82
    Report_DatetimeConvention = 83
    Report_Locale = 84
    Report_FlatFileFormat = 85
    Model_Enabled = 86
    Model_ExecutionOrder = 87
    Model_RandomNumberSeed = 88
    Model_OutputtoFolder = 89
    Model_MakeUniqueName = 90
    Model_WriteInput = 91
    Model_LoadCustomAssemblies = 92
    Model_RunMode = 93
    LTPlan_DiscountRate = 94
    LTPlan_DiscountPeriodType = 95
    LTPlan_AtaTime = 96
    LTPlan_Overlap = 97
    LTPlan_Chronology = 98
    LTPlan_LDCType = 99
    LTPlan_BlockCount = 100
    LTPlan_LastBlockCount = 101
    LTPlan_LDCSlicingMethod = 102
    LTPlan_LDCWeighta = 103
    LTPlan_LDCWeightb = 104
    LTPlan_LDCWeightc = 105
    LTPlan_LDCWeightd = 106
    LTPlan_LDCPinTop = 107
    LTPlan_LDCPinBottom = 108
    LTPlan_SampleType = 109
    LTPlan_SamplingInterval = 110
    LTPlan_ReducedSampleCount = 111
    LTPlan_ReductionRelativeAccuracy = 112
    LTPlan_Optimality = 113
    LTPlan_IntegerizationHorizon = 114
    LTPlan_EndEffectsMethod = 115
    LTPlan_SolutionCount = 116
    LTPlan_SolutionQuality = 117
    LTPlan_AlwaysAnnualizeBuildCost = 118
    LTPlan_DepreciationMethod = 119
    LTPlan_TaxRate = 120
    LTPlan_InflationRate = 121
    LTPlan_HeatRateDetail = 122
    LTPlan_OutageIncrement = 123
    LTPlan_UseEffectiveLoadApproach = 124
    LTPlan_MaintenanceSculpting = 125
    LTPlan_PricingMethod = 126
    LTPlan_TransmissionDetail = 127
    LTPlan_AllowCapacitySharing = 128
    LTPlan_CapacityPaymentsEnabled = 129
    LTPlan_StartCostAmortizationPeriod = 130
    LTPlan_ComputeReliabilityIndices = 131
    LTPlan_ComputeMultiareaReliabilityIndices = 132
    LTPlan_StochasticMethod = 133
    LTPlan_WriteExpansionPlanTextFiles = 134
    PASA_StepType = 135
    PASA_TransmissionDetail = 136
    PASA_IncludeDSP = 137
    PASA_IncludeDemandBids = 138
    PASA_IncludeContractGeneration = 139
    PASA_IncludeContractLoad = 140
    PASA_IncludeMarketPurchases = 141
    PASA_ConstraintsEnabled = 142
    PASA_InterfaceConstraintsEnabled = 143
    PASA_MaintenanceSculpting = 144
    PASA_ComputeReliabilityIndices = 145
    PASA_ComputeMultiareaReliabilityIndices = 146
    PASA_WriteOutageTextFiles = 147
    PASA_StochasticMethod = 148
    MTSchedule_DiscountRate = 149
    MTSchedule_DiscountPeriodType = 150
    MTSchedule_EndEffectsMethod = 151
    MTSchedule_StepType = 152
    MTSchedule_AtaTime = 153
    MTSchedule_Chronology = 154
    MTSchedule_LDCType = 155
    MTSchedule_BlockCount = 156
    MTSchedule_LastBlockCount = 157
    MTSchedule_LDCSlicingMethod = 158
    MTSchedule_LDCWeighta = 159
    MTSchedule_LDCWeightb = 160
    MTSchedule_LDCWeightc = 161
    MTSchedule_LDCWeightd = 162
    MTSchedule_LDCPinTop = 163
    MTSchedule_LDCPinBottom = 164
    MTSchedule_SampleType = 165
    MTSchedule_SamplingInterval = 166
    MTSchedule_ReducedSampleCount = 167
    MTSchedule_ReductionRelativeAccuracy = 168
    MTSchedule_HeatRateDetail = 169
    MTSchedule_UseEffectiveLoadApproach = 170
    MTSchedule_OutageIncrement = 171
    MTSchedule_PricingMethod = 172
    MTSchedule_TransmissionDetail = 173
    MTSchedule_NewEntryDriver = 174
    MTSchedule_NewEntryCapacityMechanism = 175
    MTSchedule_NewEntryTimeLag = 176
    MTSchedule_StartCostAmortizationPeriod = 177
    MTSchedule_StochasticMethod = 178
    MTSchedule_WriteBridgeTextFiles = 179
    STSchedule_DiscountRate = 180
    STSchedule_DiscountPeriodType = 181
    STSchedule_EndEffectsMethod = 182
    STSchedule_HeatRateDetail = 183
    STSchedule_TransmissionDetail = 184
    STSchedule_StochasticMethod = 185
    Transmission_MVABase = 186
    Transmission_OPFMethod = 187
    Transmission_ConstraintsEnabled = 188
    Transmission_FormulateUpfront = 189
    Transmission_ConstraintVoltageThreshold = 190
    Transmission_InterfaceConstraintsEnabled = 191
    Transmission_EnforceLimitsOnLinesInInterfaces = 192
    Transmission_LossesEnabled = 193
    Transmission_LossVoltageThreshold = 194
    Transmission_LossMethod = 195
    Transmission_MaxLossRelativeError = 196
    Transmission_MaxLossAbsoluteError = 197
    Transmission_MaxLossTranches = 198
    Transmission_LossTolerance = 199
    Transmission_MaxLossIterations = 200
    Transmission_MaxEmbeddedLossIterations = 201
    Transmission_DetectNonphysicalLosses = 202
    Transmission_PTDFMethod = 203
    Transmission_FlowPTDFThreshold = 204
    Transmission_WheelingPTDFThreshold = 205
    Transmission_CacheTransmissionMatrices = 206
    Transmission_ReactanceCutoff = 207
    Transmission_AllowDumpEnergy = 208
    Transmission_AllowUnservedEnergy = 209
    Transmission_BoundNodePhaseAngles = 210
    Transmission_MaxAbsolutePhaseAngle = 211
    Transmission_InternalVoLL = 212
    Transmission_USEThreshold = 213
    Transmission_RentalMethod = 214
    Transmission_InterruptionSharing = 215
    Transmission_ReportEnabled = 216
    Transmission_ReportVoltageThreshold = 217
    Transmission_ReportLinesInInterfaces = 218
    Transmission_ReportAllInterregionalFlows = 219
    Transmission_ReportAllInterzonalFlows = 220
    Transmission_ReportInjectionandLoadNodes = 221
    Transmission_ConvergenceReportLevel = 222
    Transmission_SCUCEnabled = 223
    Transmission_SCUCConstraintVoltageThreshold = 224
    Transmission_SCUCInterfaceConstraintsEnabled = 225
    Transmission_EnforceN1Contingencies = 226
    Transmission_N1ContingencyVoltageThreshold = 227
    Transmission_ContingencyMonitoringThreshold = 228
    Transmission_LimitThreshold = 229
    Transmission_LimitBootstrapInitialThreshold = 230
    Transmission_LimitBootstrapThresholdDecrement = 231
    Transmission_MaxLimitIterations = 232
    Transmission_NetworkReduction = 233
    Production_DispatchbyPowerStation = 234
    Production_UnitCommitmentOptimality = 235
    Production_RoundingUpThreshold = 236
    Production_RoundedRelaxationCommitmentModel = 237
    Production_RoundedRelaxationTuning = 238
    Production_RoundedRelaxationStartThreshold = 239
    Production_RoundedRelaxationEndThreshold = 240
    Production_RoundedRelaxationThresholdIncrement = 241
    Production_DPCapacityFactorThreshold = 242
    Production_DPCapacityFactorErrorThreshold = 243
    Production_FuelUseFunctionPrecision = 244
    Production_MaxHeatRateTranches = 245
    Production_HeatRateErrorMethod = 246
    Production_StartCostMethod = 247
    Production_CapacityFactorConstraintBasis = 248
    Production_FormulateUpfront = 249
    Production_FormulateRampUpfront = 250
    Production_IntegersinLookahead = 251
    Production_ForcedOutageRelaxesMinDownTime = 252
    Production_PumpandGenerate = 253
    Competition_EquilibriumModel = 254
    Competition_DefaultElasticity = 255
    Competition_DemandScaling = 256
    Competition_RevenueTargetingMethod = 257
    Competition_RevenueTargetingIterations = 258
    Competition_PricingStrategy = 259
    Competition_BertrandDetectActiveRampConstraints = 260
    Competition_BertrandOOMODEnabled = 261
    Competition_Epsilon = 262
    Competition_RSIEnabled = 263
    Competition_RSIBidCostMarkupMethod = 264
    Competition_NoLoadCostMarkup = 265
    Competition_MarkupMinStableLevel = 266
    Competition_StartCostMarkup = 267
    Competition_StartCostMarkupProductionBands = 268
    Competition_StartCostMarkupWindow = 269
    Competition_ContractsOptimizeOffers = 270
    Competition_ContractsSettlementMethod = 271
    Competition_ContractsHandoffPoint = 272
    Competition_MarketTradingFormat = 273
    Stochastic_OutagePatternCount = 274
    Stochastic_MonteCarloMethod = 275
    Stochastic_WeibullShape = 276
    Stochastic_ConvergentSmoothing = 277
    Stochastic_OutageScope = 278
    Stochastic_ConvergencePeriodType = 279
    Stochastic_RiskSampleCount = 280
    Stochastic_ReducedOutagePatternCount = 281
    Stochastic_ReducedSampleCount = 282
    Stochastic_ReductionRelativeAccuracy = 283
    Stochastic_ForcedOutagesinLookahead = 284
    Stochastic_EFORMaintenanceAdjust = 285
    Scenario_ReadOrder = 286
    Scenario_Locked = 287
    Performance_SOLVER = 288
    Performance_SmallLPOptimizer = 289
    Performance_SmallLPNonzeroCount = 290
    Performance_ColdStartOptimizer1 = 291
    Performance_ColdStartOptimizer2 = 292
    Performance_ColdStartOptimizer3 = 293
    Performance_HotStartOptimizer1 = 294
    Performance_HotStartOptimizer2 = 295
    Performance_HotStartOptimizer3 = 296
    Performance_MaximumThreads = 297
    Performance_MIPRootOptimizer = 298
    Performance_MIPNodeOptimizer = 299
    Performance_SmallMIPRelativeGap = 300
    Performance_SmallMIPImproveStartGap = 301
    Performance_SmallMIPMaxTime = 302
    Performance_SmallMIPIntegerCount = 303
    Performance_MIPRelativeGap = 304
    Performance_MIPImproveStartGap = 305
    Performance_MIPMaxTime = 306
    Performance_MIPMaxRelaxationRepairTime = 307
    Performance_MIPMaximumThreads = 308
    Performance_MaximumParallelTasks = 309
    Performance_MIPStartSolution = 310
    Project_Enabled = 311
    Diagnostic_ClearExisting = 312
    Diagnostic_TaskSize = 313
    Diagnostic_TaskComponents = 314
    Diagnostic_LPProgress = 315
    Diagnostic_MIPProgress = 316
    Diagnostic_SolverSummary = 317
    Diagnostic_SolutionStatus = 318
    Diagnostic_Times = 319
    Diagnostic_SampleSummary = 320
    Diagnostic_StepSummary = 321
    Diagnostic_PerformanceSummary = 322
    Diagnostic_StepFrom = 323
    Diagnostic_StepTo = 324
    Diagnostic_SampleFrom = 325
    Diagnostic_SampleTo = 326
    Diagnostic_LPFiles = 327
    Diagnostic_MPSFiles = 328
    Diagnostic_SolutionFiles = 329
    Diagnostic_GenericNames = 330
    Diagnostic_BinaryFiles = 331
    Diagnostic_UseGenericWriter = 332
    Diagnostic_SortRowColumnNames = 333
    Diagnostic_StandardizeNames = 334
    Diagnostic_StripModelName = 335
    Diagnostic_Algebraic = 336
    Diagnostic_SkipZeroValues = 337
    Diagnostic_ZeroToleranceLP = 338
    Diagnostic_ZeroToleranceSOL = 339
    Diagnostic_DecimalPlacesLP = 340
    Diagnostic_DecimalPlacesSOL = 341
    Diagnostic_Infeasibilities = 342
    Diagnostic_MaxInfeasibilityLogLines = 343
    Diagnostic_FeasibilityRepairWeight = 344
    Diagnostic_DatabaseLoad = 345
    Diagnostic_Licensing = 346
    Diagnostic_ComputerInformation = 347
    Diagnostic_DataFileRead = 348
    Diagnostic_BertrandPricing = 349
    Diagnostic_RevenueRecovery = 350
    Diagnostic_BidCostMarkup = 351
    Diagnostic_NewEntry = 352
    Diagnostic_ShiftFactors = 353
    Diagnostic_UnservedEnergy = 354
    Diagnostic_InterruptionSharing = 355
    Diagnostic_NetworkTraversal = 356
    Diagnostic_TransmissionTopology = 357
    Diagnostic_TransmissionLosses = 358
    Diagnostic_CongestionCharges = 359
    Diagnostic_MarginalLossCharges = 360
    Diagnostic_BindingContingencies = 361
    Diagnostic_UnitCommitment = 362
    Diagnostic_ConstraintDecomposition = 363
    Diagnostic_ConstraintRollover = 364
    Diagnostic_StorageDecomposition = 365
    Diagnostic_UniformPricing = 366
    Diagnostic_MarginalUnit = 367
    Diagnostic_MarginalUnitTransmissionDetail = 368
    Diagnostic_MarginalUnitIncrement = 369
    Diagnostic_MarginalExpansionUnit = 370
    Diagnostic_MarginalExpansionIncrement = 371
    Diagnostic_RegionSupply = 372
    Diagnostic_Annuities = 373
    Diagnostic_NPV = 374
    Diagnostic_EmbeddedLosses = 375
    Diagnostic_Outages = 376
    Diagnostic_RandomNumberSeed = 377
    Diagnostic_Interleaved = 378
    Diagnostic_HeatRate = 379
    Diagnostic_ObjectiveFunction = 380
    Diagnostic_FutureCostFunction = 381
    Diagnostic_HistoricalSampling = 382
    Diagnostic_ScenarioTree = 383
    Diagnostic_SampleWeights = 384


class BatteryAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class ChronoStepTypeEnum(Enum):
    Minute = 0
    Hour = 1
    Day = 2
    Week = 3
    Second = -1


class ChronologyEnum(Enum):
    Full = 0
    TypicalWeek = 1
    Partial = 2
    Fitted = 3
    Sampled = 4


class ClassEnum(Enum):
    System = 1
    Generator = 2
    Fuel = 3
    FuelContract = 4
    Emission = 5
    Abatement = 6
    Storage = 7
    Waterway = 8
    PowerStation = 9
    PhysicalContract = 10
    Purchaser = 11
    Reserve = 12
    Battery = 13
    Maintenance = 14
    HeatPlant = 15
    HeatNode = 16
    GasField = 17
    GasPlant = 18
    GasPipeline = 19
    GasNode = 20
    GasStorage = 21
    GasDemand = 22
    GasBasin = 23
    GasZone = 24
    GasContract = 25
    GasTransport = 26
    WaterPlant = 27
    WaterPipeline = 28
    WaterNode = 29
    WaterStorage = 30
    WaterDemand = 31
    WaterZone = 32
    Region = 33
    Zone = 34
    Node = 35
    Line = 36
    MLF = 37
    Transformer = 38
    FlowControl = 39
    Interface = 40
    Contingency = 41
    Company = 42
    FinancialContract = 43
    Hub = 44
    TransmissionRight = 45
    Cournot = 46
    RSI = 47
    Market = 48
    Constraint = 49
    DecisionVariable = 50
    DataFile = 51
    Variable = 52
    Timeslice = 53
    Global = 54
    Scenario = 55
    Model = 56
    Project = 57
    Horizon = 58
    Report = 59
    LTPlan = 60
    PASA = 61
    MTSchedule = 62
    STSchedule = 63
    Transmission = 64
    Production = 65
    Competition = 66
    Stochastic = 67
    Performance = 68
    Diagnostic = 69
    List = 70


class ClassGroupEnum(Enum):
    Electric = 2
    Heat = 3
    Gas = 4
    Water = 5
    Transmission = 6
    Financial = 7
    Generic = 8
    Data = 9
    Execute = 10
    Simulation = 11
    Settings = 12
    List = 13


class CollectionEnum(Enum):
    SystemGenerators = 1
    SystemFuels = 2
    SystemFuelContracts = 3
    SystemEmissions = 4
    SystemAbatements = 5
    SystemStorages = 6
    SystemWaterways = 7
    SystemPowerStations = 8
    SystemPhysicalContracts = 9
    SystemPurchasers = 10
    SystemReserves = 11
    SystemBatteries = 12
    SystemMaintenances = 13
    SystemHeatPlants = 14
    SystemHeatNodes = 15
    SystemGasFields = 16
    SystemGasPlants = 17
    SystemGasPipelines = 18
    SystemGasNodes = 19
    SystemGasStorages = 20
    SystemGasDemands = 21
    SystemGasBasins = 22
    SystemGasZones = 23
    SystemGasContracts = 24
    SystemGasTransports = 25
    SystemWaterPlants = 26
    SystemWaterPipelines = 27
    SystemWaterNodes = 28
    SystemWaterStorages = 29
    SystemWaterDemands = 30
    SystemWaterZones = 31
    SystemRegions = 32
    SystemZones = 33
    SystemNodes = 34
    SystemLines = 35
    SystemMLFs = 36
    SystemTransformers = 37
    SystemFlowControls = 38
    SystemInterfaces = 39
    SystemContingencies = 40
    SystemCompanies = 41
    SystemFinancialContracts = 42
    SystemHubs = 43
    SystemTransmissionRights = 44
    SystemCournots = 45
    SystemRSIs = 46
    SystemMarkets = 47
    SystemConstraints = 48
    SystemDecisionVariables = 49
    SystemLists = 50
    SystemDataFiles = 51
    SystemVariables = 52
    SystemTimeslices = 53
    SystemGlobals = 54
    SystemScenarios = 55
    SystemModels = 56
    SystemProjects = 57
    SystemHorizons = 58
    SystemReports = 59
    SystemLTPlan = 60
    SystemPASA = 61
    SystemMTSchedule = 62
    SystemSTSchedule = 63
    SystemTransmission = 64
    SystemProduction = 65
    SystemCompetition = 66
    SystemStochastic = 67
    SystemPerformance = 68
    SystemDiagnostics = 69
    GeneratorTemplate = 70
    FuelTemplate = 71
    FuelContractTemplate = 72
    EmissionTemplate = 73
    AbatementTemplate = 74
    StorageTemplate = 75
    WaterwayTemplate = 76
    PowerStationTemplate = 77
    PhysicalContractTemplate = 78
    PurchaserTemplate = 79
    ReserveTemplate = 80
    BatteryTemplate = 81
    MaintenanceTemplate = 82
    HeatPlantTemplate = 83
    HeatNodeTemplate = 84
    GasFieldTemplate = 85
    GasPlantTemplate = 86
    GasPipelineTemplate = 87
    GasNodeTemplate = 88
    GasStorageTemplate = 89
    GasDemandTemplate = 90
    GasBasinTemplate = 91
    GasZoneTemplate = 92
    GasContractTemplate = 93
    WaterPlantTemplate = 94
    WaterPipelineTemplate = 95
    WaterNodeTemplate = 96
    WaterStorageTemplate = 97
    WaterDemandTemplate = 98
    WaterZoneTemplate = 99
    RegionTemplate = 100
    ZoneTemplate = 101
    NodeTemplate = 102
    LineTemplate = 103
    MLFTemplate = 104
    TransformerTemplate = 105
    FlowControlTemplate = 106
    InterfaceTemplate = 107
    ContingencyTemplate = 108
    CompanyTemplate = 109
    FinancialContractTemplate = 110
    HubTemplate = 111
    TransmissionRightTemplate = 112
    CournotTemplate = 113
    RSITemplate = 114
    MarketTemplate = 115
    ConstraintTemplate = 116
    DecisionVariableTemplate = 117
    GeneratorHeatInput = 118
    GeneratorTransition = 119
    GeneratorFuels = 120
    GeneratorStartFuels = 121
    GeneratorHeadStorage = 122
    GeneratorTailStorage = 123
    GeneratorPowerStation = 124
    GeneratorMarktoMarkets = 125
    GeneratorGasNode = 126
    GeneratorWaterNode = 127
    GeneratorNodes = 128
    GeneratorNodes_star_ = 129
    GeneratorCompanies = 130
    FuelGasNodes = 131
    FuelCompanies = 132
    FuelContractGenerators = 133
    FuelContractFuel = 134
    FuelContractCompanies = 135
    FuelContractConstraints = 136
    EmissionGenerators = 137
    EmissionFuels = 138
    EmissionGasNodes = 139
    EmissionGasPlants = 140
    EmissionWaterPlants = 141
    AbatementGenerators = 142
    AbatementEmissions = 143
    AbatementConsumables = 144
    StorageWaterNodes = 145
    WaterwayStorageFrom = 146
    WaterwayStorageTo = 147
    PowerStationNodes = 148
    PhysicalContractGenerationNode = 149
    PhysicalContractLoadNode = 150
    PhysicalContractCompanies = 151
    PurchaserNodes = 152
    PurchaserNodes_star_ = 153
    PurchaserCompanies = 154
    ReserveGenerators = 155
    ReservePurchasers = 156
    ReserveGeneratorContingencies = 157
    ReserveGeneratorCostAllocation = 158
    ReserveBatteries = 159
    ReserveNestedReserves = 160
    ReserveRegions = 161
    ReserveLineContingencies = 162
    BatteryNode = 163
    BatteryNodes_star_ = 164
    BatteryCompanies = 165
    MaintenanceGenerators = 166
    MaintenanceGasPipelines = 167
    MaintenanceLines = 168
    MaintenancePrerequisites = 169
    GeneratorHeatInputNodes = 170
    GeneratorHeatOutputNodes = 171
    HeatPlantFuels = 172
    HeatPlantNodes = 173
    HeatPlantHeatInputNodes = 174
    HeatPlantHeatOutputNodes = 175
    HeatPlantStartFuels = 176
    HeatNodeHeatExportNodes = 177
    HeatNodeWaterPlants = 178
    GasFieldCompanies = 179
    GasFieldGasNode = 180
    GasFieldGasBasin = 181
    GasPlantInputNode = 182
    GasPlantOutputNode = 183
    GasPlantNode = 184
    GasPipelineGasNodeFrom = 185
    GasPipelineGasNodeTo = 186
    GasNodeGasZones = 187
    GasStorageGasNode = 188
    GasDemandGasNodes = 189
    GasDemandCompanies = 190
    GasZoneGenerators = 191
    GasZoneGasFields = 192
    GasZoneGasPlants = 193
    GasZoneExportingGasPipelines = 194
    GasZoneImportingGasPipelines = 195
    GasZoneInterzonalGasPipelines = 196
    GasZoneIntrazonalGasPipelines = 197
    GasZoneGasStorages = 198
    GasZoneGasDemands = 199
    GasZoneExportingGasTransports = 200
    GasZoneImportingGasTransports = 201
    GasZoneInterzonalGasTransports = 202
    GasZoneIntrazonalGasTransports = 203
    GasContractGasFields = 204
    GasContractGasPipelines = 205
    GasContractGasTransports = 206
    GasTransportExportNode = 207
    GasTransportImportNode = 208
    WaterPlantInputNode = 209
    WaterPlantOutputNode = 210
    WaterPlantNode = 211
    WaterPipelineWaterNodeFrom = 212
    WaterPipelineWaterNodeTo = 213
    WaterNodeWaterZones = 214
    WaterNodeNode = 215
    WaterStorageWaterNode = 216
    WaterDemandWaterNodes = 217
    WaterZoneWaterPlants = 218
    WaterZoneWaterStorages = 219
    WaterZoneExportingWaterPipelines = 220
    WaterZoneImportingWaterPipelines = 221
    WaterZoneInterzonalWaterPipelines = 222
    WaterZoneIntrazonalWaterPipelines = 223
    WaterZoneWaterDemands = 224
    RegionGenerators = 225
    RegionEmissions = 226
    RegionGenerationContracts = 227
    RegionLoadContracts = 228
    RegionPurchasers = 229
    RegionMarkets = 230
    RegionBatteries = 231
    RegionRegions = 232
    RegionReferenceNode = 233
    RegionExportingLines = 234
    RegionImportingLines = 235
    RegionInterregionalLines = 236
    RegionIntraregionalLines = 237
    RegionExportingTransformers = 238
    RegionImportingTransformers = 239
    RegionInterregionalTransformers = 240
    RegionIntraregionalTransformers = 241
    RegionUtilities = 242
    ZoneCapacityGenerators = 243
    ZoneGenerators = 244
    ZoneEmissions = 245
    ZoneCapacityGenerationContracts = 246
    ZoneCapacityLoadContracts = 247
    ZoneGenerationContracts = 248
    ZoneLoadContracts = 249
    ZoneCapacityPurchasers = 250
    ZonePurchasers = 251
    ZoneMarkets = 252
    ZoneCapacityMarkets = 253
    ZoneCapacityBatteries = 254
    ZoneBatteries = 255
    ZoneRegion = 256
    ZoneZones = 257
    ZoneReferenceNode = 258
    ZoneExportingCapacityLines = 259
    ZoneExportingLines = 260
    ZoneImportingCapacityLines = 261
    ZoneImportingLines = 262
    ZoneInterzonalLines = 263
    ZoneIntrazonalLines = 264
    ZoneExportingCapacityTransformers = 265
    ZoneExportingTransformers = 266
    ZoneImportingCapacityTransformers = 267
    ZoneImportingTransformers = 268
    ZoneInterzonalTransformers = 269
    ZoneIntrazonalTransformers = 270
    NodeRegion = 271
    NodeCapacityZone = 272
    NodeZone = 273
    NodeHubs = 274
    LineNodeFrom = 275
    LineNodeTo = 276
    LineCompanies = 277
    MLFRegions = 278
    MLFNode = 279
    MLFLine = 280
    TransformerNodeFrom = 281
    TransformerNodeTo = 282
    FlowControlLine = 283
    FlowControlLines_star_ = 284
    InterfaceLines = 285
    InterfaceTransformers = 286
    ContingencyGenerators = 287
    ContingencyLines = 288
    ContingencyMonitoredLines = 289
    ContingencyMonitoredTransformers = 290
    ContingencyTransformers = 291
    ContingencyMonitoredInterfaces = 292
    CompanyFuels = 293
    CompanyEmissions = 294
    CompanyReserves = 295
    CompanyRegions = 296
    FinancialContractGenerators = 297
    FinancialContractRegion = 298
    FinancialContractRegions = 299
    FinancialContractGeneratingCompanies = 300
    FinancialContractPurchasingCompanies = 301
    FinancialContractConditions = 302
    TransmissionRightNodeFrom = 303
    TransmissionRightNodeTo = 304
    TransmissionRightZoneFrom = 305
    TransmissionRightZoneTo = 306
    TransmissionRightHubFrom = 307
    TransmissionRightHubTo = 308
    TransmissionRightLine = 309
    TransmissionRightCompanies = 310
    CournotRegion = 311
    RSIRegion = 312
    RSILines = 313
    RSIInterfaces = 314
    RSICompanies = 315
    MarketCapacityGenerators = 316
    MarketHeatGenerators = 317
    MarketFuels = 318
    MarketEmissions = 319
    MarketReserves = 320
    MarketGasNodes = 321
    MarketNodes = 322
    MarketCompanies = 323
    ConstraintGenerators = 324
    ConstraintFuels = 325
    ConstraintFuelContracts = 326
    ConstraintEmissions = 327
    ConstraintAbatements = 328
    ConstraintStorages = 329
    ConstraintWaterways = 330
    ConstraintPhysicalContracts = 331
    ConstraintPurchasers = 332
    ConstraintReserves = 333
    ConstraintBatteries = 334
    ConstraintMaintenances = 335
    ConstraintHeatPlants = 336
    ConstraintHeatNodes = 337
    ConstraintGasFields = 338
    ConstraintGasPlants = 339
    ConstraintGasPipelines = 340
    ConstraintGasNodes = 341
    ConstraintGasStorages = 342
    ConstraintGasBasins = 343
    ConstraintGasContracts = 344
    ConstraintGasTransports = 345
    ConstraintWaterPlants = 346
    ConstraintWaterPipelines = 347
    ConstraintWaterNodes = 348
    ConstraintWaterStorages = 349
    ConstraintRegions = 350
    ConstraintZones = 351
    ConstraintNodes = 352
    ConstraintLines = 353
    ConstraintTransformers = 354
    ConstraintFlowControls = 355
    ConstraintInterfaces = 356
    ConstraintCompanies = 357
    ConstraintHubs = 358
    ConstraintMarkets = 359
    ConstraintDecisionVariables = 360
    ConstraintVariables = 361
    ConstraintConditions = 362
    DecisionVariableGenerators = 363
    DecisionVariableNodes = 364
    DecisionVariableGasPlants = 365
    DecisionVariableWaterPlants = 366
    DecisionVariableDefinition = 367
    VariableGenerators = 368
    VariableFuels = 369
    VariableReserves = 370
    VariableRegions = 371
    VariableZones = 372
    VariableNodes = 373
    VariableLines = 374
    VariableInterfaces = 375
    VariableStorages = 376
    VariableHeatNodes = 377
    VariableHeatPlants = 378
    VariableConditions = 379
    VariableVariables = 380
    GlobalStorages = 381
    ModelScenarios = 382
    ModelHorizon = 383
    ModelReport = 384
    ModelLTPlan = 385
    ModelPASA = 386
    ModelMTSchedule = 387
    ModelSTSchedule = 388
    ModelTransmission = 389
    ModelProduction = 390
    ModelCompetition = 391
    ModelStochastic = 392
    ModelPerformance = 393
    ModelDiagnostic = 394
    ModelInterleaved = 395
    ProjectModels = 396
    ProjectHorizon = 397
    ProjectReport = 398
    ListGenerators = 399
    ListFuels = 400
    ListFuelContracts = 401
    ListEmissions = 402
    ListAbatements = 403
    ListStorages = 404
    ListWaterways = 405
    ListPowerStations = 406
    ListPhysicalContracts = 407
    ListPurchasers = 408
    ListReserves = 409
    ListBatteries = 410
    ListMaintenances = 411
    ListHeatPlants = 412
    ListHeatNodes = 413
    ListGasFields = 414
    ListGasPlants = 415
    ListGasPipelines = 416
    ListGasNodes = 417
    ListGasStorages = 418
    ListGasDemands = 419
    ListGasBasins = 420
    ListGasZones = 421
    ListGasContracts = 422
    ListGasTransports = 423
    ListWaterPlants = 424
    ListWaterPipelines = 425
    ListWaterNodes = 426
    ListWaterStorages = 427
    ListWaterDemands = 428
    ListWaterZones = 429
    ListRegions = 430
    ListZones = 431
    ListNodes = 432
    ListLines = 433
    ListMLFs = 434
    ListTransformers = 435
    ListFlowControls = 436
    ListInterfaces = 437
    ListContingencies = 438
    ListCompanies = 439
    ListFinancialContracts = 440
    ListHubs = 441
    ListTransmissionRights = 442
    ListCournots = 443
    ListRSIs = 444
    ListMarkets = 445
    ListConstraints = 446
    ListDecisionVariables = 447
    ListDataFiles = 448
    ListVariables = 449
    ListTimeslices = 450
    ListGlobals = 451
    ListScenarios = 452
    ListLists = 453
    ReportLists = 454


class CompanyBridgeEnum(Enum):
    Generation = 1
    PoolRevenue = 2
    Penalty = 3


class CompanyEmissionsEnum(Enum):
    Allocation = 1


class CompanyRegionsEnum(Enum):
    LoadParticipationFactor = 1


class CompetitionAttributeEnum(Enum):
    EquilibriumModel = 1
    DefaultElasticity = 2
    DemandScaling = 3
    RevenueTargetingMethod = 4
    RevenueTargetingIterations = 5
    PricingStrategy = 6
    BertrandDetectActiveRampConstraints = 7
    BertrandOOMODEnabled = 8
    Epsilon = 9
    RSIEnabled = 10
    RSIBidCostMarkupMethod = 11
    NoLoadCostMarkup = 12
    MarkupMinStableLevel = 13
    StartCostMarkup = 14
    StartCostMarkupProductionBands = 15
    StartCostMarkupWindow = 16
    ContractsOptimizeOffers = 17
    ContractsSettlementMethod = 18
    ContractsHandoffPoint = 19
    MarketTradingFormat = 20


class CompetitionEquilibriumModelEnum(Enum):
    PerfectCompetition = 0
    CostRecovery = 1
    Cournot = 2


class CompetitionPricingStrategyEnum(Enum):
    None__ = 0
    NoCongestion = 1
    Interregional = 2
    Intraregional = 3


class CompetitionRSIBidCostMarkupMethod(Enum):
    VariableByMeritOrder = 0
    VariableBySupplyCapacity = 1
    Uniform = 2


class CompetitionRSIScenario(Enum):
    Base = 0
    Low = 1
    High = 2


class CompetitionRevenueTargetingMethodEnum(Enum):
    IncrementOnly = 0
    DecrementOnly = 1
    IncrementandDecrement = 2


class ComplementEnum(Enum):
    GeneratorInheritors = 70
    FuelInheritors = 71
    FuelContractInheritors = 72
    EmissionInheritors = 73
    AbatementInheritors = 74
    StorageInheritors = 75
    WaterwayInheritors = 76
    PowerStationInheritors = 77
    PhysicalContractInheritors = 78
    PurchaserInheritors = 79
    ReserveInheritors = 80
    BatteryInheritors = 81
    MaintenanceInheritors = 82
    HeatPlantInheritors = 83
    HeatNodeInheritors = 84
    GasFieldInheritors = 85
    GasPlantInheritors = 86
    GasPipelineInheritors = 87
    GasNodeInheritors = 88
    GasStorageInheritors = 89
    GasDemandInheritors = 90
    GasBasinInheritors = 91
    GasZoneInheritors = 92
    GasContractInheritors = 93
    WaterPlantInheritors = 94
    WaterPipelineInheritors = 95
    WaterNodeInheritors = 96
    WaterStorageInheritors = 97
    WaterDemandInheritors = 98
    WaterZoneInheritors = 99
    RegionInheritors = 100
    ZoneInheritors = 101
    NodeInheritors = 102
    LineInheritors = 103
    MLFInheritors = 104
    TransformerInheritors = 105
    FlowControlInheritors = 106
    InterfaceInheritors = 107
    ContingencyInheritors = 108
    CompanyInheritors = 109
    FinancialContractInheritors = 110
    HubInheritors = 111
    TransmissionRightInheritors = 112
    CournotInheritors = 113
    RSIInheritors = 114
    MarketInheritors = 115
    ConstraintInheritors = 116
    DecisionVariableInheritors = 117
    GeneratorHeatOutput = 118
    FuelGenerators = 120
    FuelGeneratorsStarted = 121
    StorageExportingGenerators = 122
    StorageImportingGenerators = 123
    PowerStationGenerators = 124
    MarketGenerators = 125
    GasNodeGenerators = 126
    WaterNodeGenerators = 127
    NodeGenerators = 128
    NodeGenerators_star_ = 129
    CompanyGenerators = 130
    GasNodeFuels = 131
    CompanyFuels = 132
    GeneratorFuelContracts = 133
    FuelFuelContracts = 134
    CompanyFuelContracts = 135
    GeneratorEmissions = 137
    FuelEmissions = 138
    GasNodeEmissions = 139
    GasPlantEmissions = 140
    WaterPlantEmissions = 141
    GeneratorAbatements = 142
    EmissionAbatements = 143
    FuelAbatements = 144
    WaterNodeStorages = 145
    StorageExportingWaterways = 146
    StorageImportingWaterways = 147
    NodeGenerationContracts = 149
    NodeLoadContracts = 150
    CompanyPhysicalContracts = 151
    NodePurchasers = 152
    NodePurchasers_star_ = 153
    CompanyPurchasers = 154
    GeneratorReserves = 155
    PurchaserReserves = 156
    GeneratorContingencyReserves = 157
    GeneratorReserveCostsAllocated = 158
    BatteryReserves = 159
    ReserveMasterReserves = 160
    RegionContingencyReserves = 161
    LineContingencyReserves = 162
    NodeBatteries = 163
    NodeBatteries_star_ = 164
    CompanyBatteries = 165
    GeneratorMaintenances = 166
    GasPipelineMaintenances = 167
    LineMaintenances = 168
    MaintenanceDependencies = 169
    HeatNodeGeneratorsSupplied = 170
    HeatNodeSupplyingGenerators = 171
    FuelHeatPlants = 172
    NodeHeatPlants = 173
    HeatNodeInputHeatPlants = 174
    HeatNodeOutputHeatPlants = 175
    FuelHeatPlantsStarted = 176
    HeatNodeHeatImportNodes = 177
    WaterPlantHeatNodes = 178
    CompanyGasFields = 179
    GasNodeGasFields = 180
    GasBasinGasFields = 181
    GasNodeGasPlantsSupplied = 182
    GasNodeSupplyingGasPlants = 183
    NodeGasPlants = 184
    GasNodeExportingGasPipelines = 185
    GasNodeImportingGasPipelines = 186
    GasZoneGasNodes = 187
    GasNodeGasStorages = 188
    GasNodeGasDemands = 189
    CompanyGasDemands = 190
    GasFieldGasContracts = 204
    GasPipelineGasContracts = 205
    GasTransportGasContracts = 206
    GasNodeExportingGasTransports = 207
    GasNodeImportingGasTransports = 208
    WaterNodeWaterPlantSupplied = 209
    WaterNodeSupplyingWaterPlants = 210
    NodeWaterPlants = 211
    WaterNodeExportingWaterPipelines = 212
    WaterNodeImportingWaterPipelines = 213
    WaterZoneWaterNodes = 214
    NodeWaterNodes = 215
    WaterNodeWaterStorages = 216
    WaterNodeWaterDemands = 217
    GeneratorRegions = 225
    EmissionRegions = 226
    PurchaserRegions = 229
    BatteryRegions = 231
    GeneratorCapacityZones = 243
    GeneratorZones = 244
    EmissionZones = 245
    PurchaserCapacityZones = 250
    PurchaserZones = 251
    BatteryCapacityZones = 254
    BatteryZones = 255
    RegionZones = 256
    RegionNodes = 271
    ZoneCapacityNodes = 272
    ZoneNodes = 273
    HubNodes = 274
    NodeExportingLines = 275
    NodeImportingLines = 276
    CompanyLines = 277
    NodeExportingTransformers = 281
    NodeImportingTransformers = 282
    LineFlowControls = 283
    LineFlowControls_star_ = 284
    LineInterfaces = 285
    TransformerInterfaces = 286
    GeneratorContingencies = 287
    LineContingencies = 288
    LineMonitoringContingencies = 289
    TransformerMonitoringContingencies = 290
    TransformerContingencies = 291
    InterfaceMonitoringContingencies = 292
    EmissionCompanies = 294
    RegionCompanies = 296
    GeneratorFinancialContracts = 297
    RegionFinancialContracts = 298
    CompanyGenerationContracts = 300
    CompanyPurchaseContracts = 301
    VariableFinancialContracts = 302
    CompanyTransmissionRights = 310
    GeneratorCapacityMarkets = 316
    GeneratorHeatMarkets = 317
    FuelMarkets = 318
    EmissionMarkets = 319
    ReserveMarkets = 320
    GasNodeGasMarkets = 321
    NodeEnergyMarkets = 322
    CompanyMarkets = 323
    GeneratorConstraints = 324
    FuelConstraints = 325
    FuelContractConstraints = 326
    EmissionConstraints = 327
    AbatementConstraints = 328
    StorageConstraints = 329
    WaterwayConstraints = 330
    PhysicalContractConstraints = 331
    PurchaserConstraints = 332
    ReserveConstraints = 333
    BatteryConstraints = 334
    MaintenanceConstraints = 335
    HeatPlantConstraints = 336
    HeatNodeConstraints = 337
    GasFieldConstraints = 338
    GasPlantConstraints = 339
    GasPipelineConstraints = 340
    GasNodeConstraints = 341
    GasStorageConstraints = 342
    GasBasinConstraints = 343
    GasContractConstraints = 344
    GasTransportConstraints = 345
    WaterPlantConstraints = 346
    WaterPipelineConstraints = 347
    WaterNodeConstraints = 348
    WaterStorageConstraints = 349
    RegionConstraints = 350
    ZoneConstraints = 351
    NodeConstraints = 352
    LineConstraints = 353
    TransformerConstraints = 354
    FlowControlConstraints = 355
    InterfaceConstraints = 356
    CompanyConstraints = 357
    HubConstraints = 358
    MarketConstraints = 359
    DecisionVariableConstraints = 360
    VariableConstraints = 361
    VariableConditionalConstraints = 362
    GeneratorDecisionVariables = 363
    NodeDecisionVariables = 364
    GasPlantDecisionVariables = 365
    WaterPlantDecisionVariables = 366
    ConstraintDefinitions = 367
    GeneratorConditions = 368
    FuelConditions = 369
    ReserveConditions = 370
    RegionConditions = 371
    ZoneConditions = 372
    NodeConditions = 373
    LineConditions = 374
    InterfaceConditions = 375
    StorageConditions = 376
    HeatNodeConditions = 377
    HeatPlantConditions = 378
    StorageGlobals = 381
    ScenarioModels = 382
    HorizonModels = 383
    ReportModels = 384
    LTPlanModels = 385
    PASAModels = 386
    MTScheduleModels = 387
    STScheduleModels = 388
    TransmissionModels = 389
    ProductionModels = 390
    CompetitionModels = 391
    StochasticModels = 392
    PerformanceModels = 393
    DiagnosticModels = 394
    ModelProjects = 396
    HorizonProjects = 397
    ReportProjects = 398
    GeneratorLists = 399
    FuelLists = 400
    FuelContractLists = 401
    EmissionLists = 402
    AbatementLists = 403
    StorageLists = 404
    WaterwayLists = 405
    PowerStationLists = 406
    PhysicalContractLists = 407
    PurchaserLists = 408
    ReserveLists = 409
    BatteryLists = 410
    MaintenanceLists = 411
    HeatPlantLists = 412
    HeatNodeLists = 413
    GasFieldLists = 414
    GasPlantLists = 415
    GasPipelineLists = 416
    GasNodeLists = 417
    GasStorageLists = 418
    GasDemandLists = 419
    GasBasinLists = 420
    GasZoneLists = 421
    GasContractLists = 422
    GasTransportLists = 423
    WaterPlantLists = 424
    WaterPipelineLists = 425
    WaterNodeLists = 426
    WaterStorageLists = 427
    WaterDemandLists = 428
    WaterZoneLists = 429
    RegionLists = 430
    ZoneLists = 431
    NodeLists = 432
    LineLists = 433
    MLFLists = 434
    TransformerLists = 435
    FlowControlLists = 436
    InterfaceLists = 437
    ContingencyLists = 438
    CompanyLists = 439
    FinancialContractLists = 440
    HubLists = 441
    TransmissionRightLists = 442
    CournotLists = 443
    RSILists = 444
    MarketLists = 445
    ConstraintLists = 446
    DecisionVariableLists = 447
    DataFileLists = 448
    VariableLists = 449
    TimesliceLists = 450
    GlobalLists = 451
    ScenarioLists = 452
    ListReports = 454


class ConstraintAbatementsEnum(Enum):
    AbatementCoefficient = 1
    OperatingHoursCoefficient = 2


class ConstraintBatteriesEnum(Enum):
    EnergyCoefficient = 1
    GenerationCoefficient = 2
    LoadCoefficient = 3
    RampCoefficient = 4
    RampUpCoefficient = 5
    RampDownCoefficient = 6
    RampUpViolationCoefficient = 7
    RampDownViolationCoefficient = 8
    ReserveProvisionCoefficient = 9
    SpinningReserveCoefficient = 10
    PumpDispatchableLoadCoefficient = 11
    RaiseReserveProvisionCoefficient = 12
    LowerReserveProvisionCoefficient = 13
    RegulationRaiseReserveProvisionCoefficient = 14
    RegulationLowerReserveProvisionCoefficient = 15
    ReplacementReserveProvisionCoefficient = 16
    ReserveUnitsCoefficient = 17
    OperatingReserveUnitsCoefficient = 18
    CyclesCoefficient = 19
    AgeCoefficient = 20
    UnitsBuiltCoefficient = 21
    UnitsRetiredCoefficient = 22
    UnitsBuiltinYearCoefficient = 23
    UnitsRetiredinYearCoefficient = 24
    CapacityBuiltCoefficient = 25
    CapacityRetiredCoefficient = 26
    CapacityReservesCoefficient = 27
    BuildCostCoefficient = 28
    BuiltCoefficient = 29
    BuiltinYearCoefficient = 30


class ConstraintBridgeEnum(Enum):
    RHS = 1
    PenaltyQuantity = 2
    PenaltyPrice = 3
    Slack = 4
    Activity = 5
    Violation = 6
    Price = 7


class ConstraintCompaniesEnum(Enum):
    GenerationCoefficient = 1
    CommittedCapacityCoefficient = 2
    ContractVolumeCoefficient = 3


class ConstraintConditionLogicEnum(Enum):
    AND1 = 0
    OR1 = 1


class ConstraintConditionMethodEnum(Enum):
    Ignore = 0
    Iterate = 1
    Optimize = 2


class ConstraintConditionsEnum(Enum):
    RHSCoefficient = 1


class ConstraintDecisionVariablesEnum(Enum):
    ValueCoefficient = 1
    ValueSquaredCoefficient = 2


class ConstraintDecompositionMethodEnum(Enum):
    Quantity = 0
    Price = 1


class ConstraintEmissionsEnum(Enum):
    ProductionCoefficient = 1
    AbatementCoefficient = 2


class ConstraintFlowControlsEnum(Enum):
    AngleCoefficient = 1
    PositiveAngleCoefficient = 2
    NegativeAngleCoefficient = 3
    UnitsBuiltCoefficient = 4


class ConstraintFuelContractsEnum(Enum):
    OfftakeCoefficient = 1


class ConstraintFuelsEnum(Enum):
    OfftakeCoefficient = 1
    EmissionCoefficient = 2
    InUseCoefficient = 3
    ClosingInventoryCoefficient = 4
    InventoryChangeCoefficient = 5
    DeliveryCoefficient = 6
    WithdrawalCoefficient = 7
    GenerationCoefficient = 8


class ConstraintGasBasinsEnum(Enum):
    ProductionCoefficient = 1
    UnitsBuiltCoefficient = 2
    UnitsBuiltinYearCoefficient = 3


class ConstraintGasContractsEnum(Enum):
    ProductionCoefficient = 1


class ConstraintGasFieldsEnum(Enum):
    EndVolumeCoefficient = 1
    ProductionCoefficient = 2
    RampCoefficient = 3
    UnitsBuiltCoefficient = 4
    UnitsBuiltinYearCoefficient = 5


class ConstraintGasNodesEnum(Enum):
    FlowCoefficient = 1
    UnitsBuiltCoefficient = 2
    UnitsRetiredCoefficient = 3
    UnitsBuiltinYearCoefficient = 4
    UnitsRetiredinYearCoefficient = 5


class ConstraintGasPipelinesEnum(Enum):
    EndVolumeCoefficient = 1
    FlowCoefficient = 2
    FlowForwardCoefficient = 3
    FlowBackCoefficient = 4
    UnitsBuiltCoefficient = 5
    UnitsRetiredCoefficient = 6
    UnitsBuiltinYearCoefficient = 7
    UnitsRetiredinYearCoefficient = 8


class ConstraintGasPlantsEnum(Enum):
    ProductionCoefficient = 1
    CapacityFactorCoefficient = 2
    OperatingHoursCoefficient = 3
    EnergyUsageCoefficient = 4
    InstalledCapacityCoefficient = 5
    UnitsBuiltCoefficient = 6
    UnitsRetiredCoefficient = 7
    UnitsBuiltinYearCoefficient = 8
    UnitsRetiredinYearCoefficient = 9
    CapacityBuiltCoefficient = 10
    CapacityRetiredCoefficient = 11
    BuildCostCoefficient = 12
    BuiltCoefficient = 13
    BuiltinYearCoefficient = 14


class ConstraintGasStoragesEnum(Enum):
    EndVolumeCoefficient = 1
    WithdrawalCoefficient = 2
    InjectionCoefficient = 3
    RampCoefficient = 4
    UnitsBuiltCoefficient = 5
    UnitsRetiredCoefficient = 6
    UnitsBuiltinYearCoefficient = 7
    UnitsRetiredinYearCoefficient = 8


class ConstraintGasTransportsEnum(Enum):
    ShipmentsCoefficient = 1


class ConstraintGeneratorsEnum(Enum):
    GenerationCoefficient = 1
    GenerationSquaredCoefficient = 2
    GenerationSUMSquaredCoefficient = 3
    GenerationSentOutCoefficient = 4
    CapacityFactorCoefficient = 5
    OperatingHoursCoefficient = 6
    UnitsGeneratingCoefficient = 7
    UnitsStartedCoefficient = 8
    UnitsShutdownCoefficient = 9
    HoursDownCoefficient = 10
    AvailableCapacityCoefficient = 11
    CommittedCapacityCoefficient = 12
    FuelOfftakeCoefficient = 13
    WasteHeatCoefficient = 14
    EmissionCoefficient = 15
    HeatProductionCoefficient = 16
    PumpLoadCoefficient = 17
    PumpOperatingHoursCoefficient = 18
    UnitsPumpingCoefficient = 19
    PumpUnitsStartedCoefficient = 20
    SyncCondLoadCoefficient = 21
    UnitsSyncCondCoefficient = 22
    SyncCondOperatingHoursCoefficient = 23
    RampCoefficient = 24
    RampUpCoefficient = 25
    RampDownCoefficient = 26
    RampUpViolationCoefficient = 27
    RampDownViolationCoefficient = 28
    ReserveProvisionCoefficient = 29
    SpinningReserveCoefficient = 30
    SyncCondReserveCoefficient = 31
    PumpDispatchableLoadCoefficient = 32
    RaiseReserveProvisionCoefficient = 33
    LowerReserveProvisionCoefficient = 34
    RegulationRaiseReserveProvisionCoefficient = 35
    RegulationLowerReserveProvisionCoefficient = 36
    ReplacementReserveProvisionCoefficient = 37
    ReserveUnitsCoefficient = 38
    OperatingReserveUnitsCoefficient = 39
    FlexibilityUpCoefficient = 40
    FlexibilityDownCoefficient = 41
    RampFlexibilityUpCoefficient = 42
    RampFlexibilityDownCoefficient = 43
    WithdrawalCoefficient = 44
    InjectionCoefficient = 45
    WaterOfftakeCoefficient = 46
    WaterConsumptionCoefficient = 47
    NetProfitCoefficient = 48
    PoolRevenueCoefficient = 49
    NetRevenueCoefficient = 50
    StartShutdownCostCoefficient = 51
    FixedCostsCoefficient = 52
    InstalledCapacityCoefficient = 53
    RatedCapacityCoefficient = 54
    UnitsOutCoefficient = 55
    MaintenanceCoefficient = 56
    FirmCapacityCoefficient = 57
    AgeCoefficient = 58
    UnitsBuiltCoefficient = 59
    UnitsRetiredCoefficient = 60
    UnitsBuiltinYearCoefficient = 61
    UnitsRetiredinYearCoefficient = 62
    CapacityBuiltCoefficient = 63
    CapacityRetiredCoefficient = 64
    CapacityReservesCoefficient = 65
    BuildCostCoefficient = 66
    BuiltCoefficient = 67
    BuiltinYearCoefficient = 68


class ConstraintHeatNodesEnum(Enum):
    HeatFlowCoefficient = 1


class ConstraintHeatPlantsEnum(Enum):
    UnitsGeneratingCoefficient = 1
    FuelOfftakeCoefficient = 2
    HeatProductionCoefficient = 3


class ConstraintHubsEnum(Enum):
    LoadCoefficient = 1
    GenerationCoefficient = 2


class ConstraintInterfacesEnum(Enum):
    FlowCoefficient = 1
    FlowForwardCoefficient = 2
    FlowBackCoefficient = 3
    ExpansionCostCoefficient = 4


class ConstraintLHSTypeEnum(Enum):
    Sum = 0
    MaxSum = 1
    Max = 2


class ConstraintLinesEnum(Enum):
    FlowCoefficient = 1
    FlowForwardCoefficient = 2
    FlowBackCoefficient = 3
    FlowSquaredCoefficient = 4
    FlowingForwardCoefficient = 5
    FlowingBackCoefficient = 6
    SpareExportCapacityCoefficient = 7
    SpareImportCapacityCoefficient = 8
    UnitsOutCoefficient = 9
    ExportCapacityCoefficient = 10
    ImportCapacityCoefficient = 11
    UnitsBuiltCoefficient = 12
    UnitsRetiredCoefficient = 13
    UnitsBuiltinYearCoefficient = 14
    UnitsRetiredinYearCoefficient = 15
    ExportCapacityBuiltCoefficient = 16
    ImportCapacityBuiltCoefficient = 17
    ExportCapacityRetiredCoefficient = 18
    ImportCapacityRetiredCoefficient = 19
    BuildCostCoefficient = 20


class ConstraintMaintenancesEnum(Enum):
    HoursActiveCoefficient = 1
    CostCoefficient = 2
    CrewCoefficient = 3
    EquipmentCoefficient = 4
    StartHourCoefficient = 5
    StartCoefficient = 6


class ConstraintMarketsEnum(Enum):
    SalesCoefficient = 1
    PurchasesCoefficient = 2
    RevenueCoefficient = 3
    CostCoefficient = 4


class ConstraintNodesEnum(Enum):
    LoadCoefficient = 1
    GenerationCoefficient = 2
    UnservedEnergyCoefficient = 3
    DumpEnergyCoefficient = 4
    NetLoadCoefficient = 5
    NetInjectionCoefficient = 6
    PhaseAngleCoefficient = 7
    MLFCoefficient = 8


class ConstraintPaymentsCompatibilityEnum(Enum):
    Korea = 1
    Ireland = 2


class ConstraintPhysicalContractsEnum(Enum):
    LoadCoefficient = 1
    GenerationCoefficient = 2
    UnitsGeneratingCoefficient = 3
    UnitsLoadCoefficient = 4
    GenerationCapacityCoefficient = 5
    LoadObligationCoefficient = 6
    BuildCostCoefficient = 7


class ConstraintPurchasersEnum(Enum):
    LoadCoefficient = 1
    LoadObligationCoefficient = 2
    ReserveProvisionCoefficient = 3


class ConstraintRegionsEnum(Enum):
    LoadCoefficient = 1
    LoadSquaredCoefficient = 2
    GenerationCoefficient = 3
    CommittedCapacityCoefficient = 4
    UnservedEnergyCoefficient = 5
    DumpEnergyCoefficient = 6
    NetLoadCoefficient = 7
    FirmCapacityCoefficient = 8
    GenerationCapacityCoefficient = 9
    PeakLoadCoefficient = 10
    CapacityReservesCoefficient = 11
    GenerationCapacityBuiltCoefficient = 12
    GenerationCapacityRetiredCoefficient = 13
    GeneratorBuildCostCoefficient = 14
    GeneratorsBuiltCoefficient = 15
    GeneratorsBuiltinYearCoefficient = 16
    ImportCapacityCoefficient = 17
    ExportCapacityCoefficient = 18
    ImportCapacityBuiltCoefficient = 19
    ExportCapacityBuiltCoefficient = 20


class ConstraintReservesEnum(Enum):
    ProvisionCoefficient = 1
    RiskCoefficient = 2
    ShortageCoefficient = 3


class ConstraintStatusEnum(Enum):
    InActive = 0
    Active = 1


class ConstraintStoragesEnum(Enum):
    EndVolumeCoefficient = 1
    EndLevelCoefficient = 2
    RampCoefficient = 3
    NaturalInflowCoefficient = 4
    InflowCoefficient = 5
    ReleaseCoefficient = 6
    GeneratorReleaseCoefficient = 7
    SpillCoefficient = 8
    HoursFullCoefficient = 9
    LossCoefficient = 10


class ConstraintTransformersEnum(Enum):
    FlowCoefficient = 1


class ConstraintVariablesEnum(Enum):
    ExpectedValueCoefficient = 1
    ValueCoefficient = 2
    ErrorCoefficient = 3
    PositiveErrorCoefficient = 4
    NegativeErrorCoefficient = 5


class ConstraintWaterNodesEnum(Enum):
    FlowCoefficient = 1
    UnitsBuiltCoefficient = 2
    UnitsRetiredCoefficient = 3
    UnitsBuiltinYearCoefficient = 4
    UnitsRetiredinYearCoefficient = 5


class ConstraintWaterPipelinesEnum(Enum):
    FlowCoefficient = 1
    FlowForwardCoefficient = 2
    FlowBackCoefficient = 3
    UnitsBuiltCoefficient = 4
    UnitsRetiredCoefficient = 5
    UnitsBuiltinYearCoefficient = 6
    UnitsRetiredinYearCoefficient = 7


class ConstraintWaterPlantsEnum(Enum):
    ProductionCoefficient = 1
    CapacityFactorCoefficient = 2
    OperatingHoursCoefficient = 3
    EnergyUsageCoefficient = 4
    InstalledCapacityCoefficient = 5
    UnitsBuiltCoefficient = 6
    UnitsRetiredCoefficient = 7
    UnitsBuiltinYearCoefficient = 8
    UnitsRetiredinYearCoefficient = 9
    CapacityBuiltCoefficient = 10
    CapacityRetiredCoefficient = 11
    BuildCostCoefficient = 12
    BuiltCoefficient = 13
    BuiltinYearCoefficient = 14


class ConstraintWaterStoragesEnum(Enum):
    NaturalInflowCoefficient = 1
    EndVolumeCoefficient = 2
    ReleaseCoefficient = 3
    InflowCoefficient = 4
    RampCoefficient = 5
    UnitsBuiltCoefficient = 6
    UnitsRetiredCoefficient = 7
    UnitsBuiltinYearCoefficient = 8
    UnitsRetiredinYearCoefficient = 9


class ConstraintWaterwaysEnum(Enum):
    FlowCoefficient = 1
    RampCoefficient = 2
    HoursFlowingCoefficient = 3


class ConstraintZonesEnum(Enum):
    LoadCoefficient = 1
    LoadSquaredCoefficient = 2
    GenerationCoefficient = 3
    CommittedCapacityCoefficient = 4
    UnservedEnergyCoefficient = 5
    DumpEnergyCoefficient = 6
    NetLoadCoefficient = 7
    FirmCapacityCoefficient = 8
    GenerationCapacityCoefficient = 9
    PeakLoadCoefficient = 10
    CapacityReservesCoefficient = 11
    GenerationCapacityBuiltCoefficient = 12
    GenerationCapacityRetiredCoefficient = 13
    GeneratorBuildCostCoefficient = 14
    GeneratorsBuiltCoefficient = 15
    GeneratorsBuiltinYearCoefficient = 16
    ImportCapacityCoefficient = 17
    ExportCapacityCoefficient = 18
    ImportCapacityBuiltCoefficient = 19
    ExportCapacityBuiltCoefficient = 20


class ContractHandoffPointEnum(Enum):
    Purchaser = 0
    Generator = 1


class ContractSettlementMethodEnum(Enum):
    Fixed = 0
    Prorata = 1
    LeastCost = 2


class CycleTypeEnum(Enum):
    Day = 1
    Month = 3
    Year = 4
    Quarter = 7


class DataFileAttributeEnum(Enum):
    Enabled = 1
    GrowthPeriod = 2
    Method = 3
    RelativeGrowthatMin = 4
    ShapeDistortion = 5
    DecimalPlaces = 6
    MissingValueMethod = 7
    PeriodsperDay = 8
    UpscalingMethod = 9
    DownscalingMethod = 10
    DatetimeConvention = 11
    Locale = 12
    TimeShift = 13
    WeekBeginning = 14
    HistoricalSampling = 15
    HistoricalYearFrom = 16
    HistoricalYearTo = 17
    HistoricalYearStart = 18
    HistoricalYearEnding = 19
    HistoricalPeriodType = 20
    BaseYear = 21


class DataFileDownScalingMethodEnum(Enum):
    Average = 0
    First = 1
    Last = 2
    Auto = -1


class DataFileMissingValueMethodEnum(Enum):
    LastKnownValue = 0
    AssumeZero = 1
    AssumeDefault = 2


class DataFileUpScalingMethodEnum(Enum):
    Step = 0
    Interpolate = 1
    BoundaryInterpolate = 2
    Auto = -1


class DatetimeConventionEnum(Enum):
    BeginningofInterval = 0
    EndofInterval = 1


class DecisionVariableAttributeEnum(Enum):
    Type = 1
    TimeLag = 2
    TimeInvariant = 3


class DecisionVariableDefinitionEnum(Enum):
    ValueCoefficient = 1


class DecisionVariableGasPlantsEnum(Enum):
    EnergyUsageDefinitionCoefficient = 1


class DecisionVariableGeneratorsEnum(Enum):
    HeatInputDefinitionCoefficient = 1


class DecisionVariableNodesEnum(Enum):
    NetInjectionDefinitionCoefficient = 1


class DecisionVariableTypeEnum(Enum):
    Continuous = 0
    Integer = 1


class DecisionVariableWaterPlantsEnum(Enum):
    EnergyUsageDefinitionCoefficient = 1


class DepreciationMethodEnum(Enum):
    None_ = 0
    StraightLine = 1
    Declining = 2


class DesignBenefitFnShapeEnum(Enum):
    PiecewiseLinear = 0
    Quadratic = 1


class DesignOfferQuantityFormatEnum(Enum):
    Incremental = 0
    Cumulative = 1


class DesignPoolTypeEnum(Enum):
    Gross = 0
    Net = 1


class DesignSettlementModelEnum(Enum):
    Nodal = 0
    ReferenceNode = 1
    LoadWeightedAverage = 2
    PayAsBid = 3
    UniformPrice = 4
    None_ = 5
    Custom = 6
    MostExpensiveDispatched = 7


class DiagnosticAttributeEnum(Enum):
    ClearExisting = 1
    TaskSize = 2
    TaskComponents = 3
    LPProgress = 4
    MIPProgress = 5
    SolverSummary = 6
    SolutionStatus = 7
    Times = 8
    SampleSummary = 9
    StepSummary = 10
    PerformanceSummary = 11
    StepFrom = 12
    StepTo = 13
    SampleFrom = 14
    SampleTo = 15
    LPFiles = 16
    MPSFiles = 17
    SolutionFiles = 18
    GenericNames = 19
    BinaryFiles = 20
    UseGenericWriter = 21
    SortRowColumnNames = 22
    StandardizeNames = 23
    StripModelName = 24
    Algebraic = 25
    SkipZeroValues = 26
    ZeroToleranceLP = 27
    ZeroToleranceSOL = 28
    DecimalPlacesLP = 29
    DecimalPlacesSOL = 30
    Infeasibilities = 31
    MaxInfeasibilityLogLines = 32
    FeasibilityRepairWeight = 33
    DatabaseLoad = 34
    Licensing = 35
    ComputerInformation = 36
    DataFileRead = 37
    BertrandPricing = 38
    RevenueRecovery = 39
    BidCostMarkup = 40
    NewEntry = 41
    ShiftFactors = 42
    UnservedEnergy = 43
    InterruptionSharing = 44
    NetworkTraversal = 45
    TransmissionTopology = 46
    TransmissionLosses = 47
    CongestionCharges = 48
    MarginalLossCharges = 49
    BindingContingencies = 50
    UnitCommitment = 51
    ConstraintDecomposition = 52
    ConstraintRollover = 53
    StorageDecomposition = 54
    UniformPricing = 55
    MarginalUnit = 56
    MarginalUnitTransmissionDetail = 57
    MarginalUnitIncrement = 58
    MarginalExpansionUnit = 59
    MarginalExpansionIncrement = 60
    RegionSupply = 61
    Annuities = 62
    NPV = 63
    EmbeddedLosses = 64
    Outages = 65
    RandomNumberSeed = 66
    Interleaved = 67
    HeatRate = 68
    ObjectiveFunction = 69
    FutureCostFunction = 70
    HistoricalSampling = 71
    ScenarioTree = 72
    SampleWeights = 73


class DiscountEndEffectsMethodEnum(Enum):
    None_ = 0
    Perpetuity = 1


class EEIFormatEnum(Enum):
    TwoDigitYear = 0
    FourDigitYear = 1


class EmissionFuelsEnum(Enum):
    ProductionRate = 1


class EmissionGasNodesEnum(Enum):
    ProductionRate = 1


class EmissionGasPlantsEnum(Enum):
    ProductionRate = 1


class EmissionGeneratorsEnum(Enum):
    ProductionRate = 1
    RemovalRate = 2
    RemovalCost = 3
    ProductionatStart = 4
    ShadowPriceScalar = 5
    PriceScalar = 6
    Allocation = 7


class EmissionWaterPlantsEnum(Enum):
    ProductionRate = 1


class EnforceMinUpandDownTimesEnum(Enum):
    No = 0
    Yes = -1


class FileTypeEnum(Enum):
    FileTypeEnum_Input = 0
    FileTypeEnum_Output = 1


class FinancialContractGeneratingCompaniesEnum(Enum):
    Share = 1


class FinancialContractGeneratorsEnum(Enum):
    GenerationParticipationFactor = 1


class FinancialContractPurchasingCompaniesEnum(Enum):
    Share = 1


class FinancialContractRegionEnum(Enum):
    LoadParticipationFactor = 1


class FixedLoadTypeEnum(Enum):
    None_ = 0
    FixedLoad = 1
    MinLoad = 2


class FlatFileFormatEnum(Enum):
    PeriodsInColumns = 0
    NamedPeriodsInColumns = 1
    BandsInColumns = 2
    NamesInColumns = 3
    NamedBandsInColumns = 4
    Patterned = 5
    NamedPatterned = 6
    PatternedNamesInColumns = 7
    PatternsInColumns = 8
    NamedPatternsInColumns = 9
    Unknown = -1


class FlowControlAngleVariationEnum(Enum):
    Variable = 0
    Fixed = 1


class FlowControlTypeEnum(Enum):
    PST = 0
    DSR = 1
    DSSC = 2
    MSSR = 3
    TCSC = 4
    SSSC = 5


class FlowModelEnum(Enum):
    None_ = 0
    Net = 1
    Directed = 2


class FuelCompaniesEnum(Enum):
    Share = 1


class FuelContractCompaniesEnum(Enum):
    Share = 1


class GasDemandCompaniesEnum(Enum):
    Share = 1


class GasDemandGasNodesEnum(Enum):
    DemandParticipationFactor = 1


class GasFieldCompaniesEnum(Enum):
    Share = 1


class GasNodeAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class GasStorageAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class GeneratorAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class GeneratorCommitmentModelEnum(Enum):
    None_ = 0
    Aggregated = 1
    UnitbyUnit = 2


class GeneratorCompaniesEnum(Enum):
    Share = 1


class GeneratorFuelsEnum(Enum):
    TransportCharge = 1
    MutuallyExclusive = 2
    Ratio = 3
    MinRatio = 4
    MaxRatio = 5
    MaxInput = 6
    Rating = 7
    IsAvailable = 8
    HeatRateScalar = 9
    HeatRateBase = 10
    HeatRate = 11
    HeatRateIncr = 12
    HeatRateIncr2 = 13
    HeatRateIncr3 = 14
    TransitionCostDown = 15
    TransitionCostUp = 16
    DecouplingTime = 17
    CouplingTime = 18
    EmissionScalar = 19
    OfferQuantity = 20
    OfferPrice = 21


class GeneratorHeadStorageEnum(Enum):
    FlowFactor = 1
    FlowatStart = 2
    EfficiencyPoint = 3
    EfficiencyScalar = 4


class GeneratorHeatOutputNodesEnum(Enum):
    ParticipationFactor = 1


class GeneratorHeatRateDetailEnum(Enum):
    Detailed = 0
    Simple = 1
    Simplest = 2


class GeneratorHeatRateModelEnum(Enum):
    OfftakeFx = 0
    Constant = 1
    AvgAtPoints = 2
    IncrwithBase = 3
    IncrwithAvg = 4
    EfficiencyIncr = 5


class GeneratorNodesEnum(Enum):
    GenerationParticipationFactor = 1
    LoadParticipationFactor = 2


class GeneratorPricingMethodEnum(Enum):
    Average = 0
    Marginal = 1


class GeneratorReserveMethodEnum(Enum):
    Constant = 0
    Unbounded = 1
    Bounded = 2


class GeneratorStartFuelsEnum(Enum):
    OfftakeatStart = 1
    TransportCharge = 2
    EmissionScalar = 3


class GeneratorTailStorageEnum(Enum):
    FlowFactor = 1


class GeneratorTransitionEnum(Enum):
    TransitionCost = 1


class GeneratorTransitionTypeEnum(Enum):
    Individual = 0
    Group = 1


class GlobalStoragesEnum(Enum):
    FCFShadowPrice = 1


class GrowthMethodEnum(Enum):
    None_ = 0
    Linear = 1
    Quadratic = 2
    Custom = 3


class HeadEffectsMethodEnum(Enum):
    BackwardLooking = 0
    Dynamic = 1


class HeatNodeHeatExportNodesEnum(Enum):
    ParticipationFactor = 1


class HeatNodeWaterPlantsEnum(Enum):
    ParticipationFactor = 1


class HeatPlantFuelsEnum(Enum):
    MutuallyExclusive = 1
    Ratio = 2
    MinRatio = 3
    MaxRatio = 4
    MaxInput = 5
    IsAvailable = 6
    HeatRateScalar = 7
    HeatRateBase = 8
    HeatRate = 9
    HeatRateIncr = 10


class HeatPlantHeatOutputNodesEnum(Enum):
    ParticipationFactor = 1


class HeatPlantStartFuelsEnum(Enum):
    OfftakeatStart = 1


class HorizonAttributeEnum(Enum):
    PeriodsperDay = 1
    DateFrom = 2
    StepType = 3
    StepCount = 4
    DayBeginning = 5
    WeekBeginning = 6
    YearEnding = 7
    Chronology = 8
    TypicalWeek = 9
    ChronoDateFrom = 10
    ChronoPeriodFrom = 11
    ChronoPeriodTo = 12
    ChronoStepType = 13
    ChronoAtaTime = 14
    ChronoStepCount = 15
    LookaheadIndicator = 16
    LookaheadType = 17
    LookaheadAtaTime = 18
    LookaheadPeriodsperDay = 19


class HubPricingMethodEnum(Enum):
    LoadWeightedAverage = 0
    GenerationWeigthedAverage = 1
    WeightedAverage = 2


class HydroModelEnum(Enum):
    Auto = 0
    Energy = 1
    Level = 2
    Volume = 3


class ImageEnum(Enum):
    ImageEnum_Closed = 1
    ImageEnum_Open = 2
    ImageEnum_DatumInUse = 3
    ImageEnum_DatumNotInUse = 4


class IntegerOptimalityEnum(Enum):
    LinearRelaxation = 0
    RoundedLinearRelaxation = 1
    IntegerOptimal = 2
    DynamicProgram = 3
    Free = -1


class InterfaceLinesEnum(Enum):
    FlowCoefficient = 1
    FlowForwardCoefficient = 2
    FlowBackCoefficient = 3


class InterfaceTransformersEnum(Enum):
    FlowCoefficient = 1


class LDCSlicingMethodEnum(Enum):
    PeakOffpeakBias = 0
    WeightedLeastsquares = 1


class LTPlanAttributeEnum(Enum):
    DiscountRate = 1
    DiscountPeriodType = 2
    AtaTime = 3
    Overlap = 4
    Chronology = 5
    LDCType = 6
    BlockCount = 7
    LastBlockCount = 8
    LDCSlicingMethod = 9
    LDCWeighta = 10
    LDCWeightb = 11
    LDCWeightc = 12
    LDCWeightd = 13
    LDCPinTop = 14
    LDCPinBottom = 15
    SampleType = 16
    SamplingInterval = 17
    ReducedSampleCount = 18
    ReductionRelativeAccuracy = 19
    Optimality = 20
    IntegerizationHorizon = 21
    EndEffectsMethod = 22
    SolutionCount = 23
    SolutionQuality = 24
    AlwaysAnnualizeBuildCost = 25
    DepreciationMethod = 26
    TaxRate = 27
    InflationRate = 28
    HeatRateDetail = 29
    OutageIncrement = 30
    UseEffectiveLoadApproach = 31
    MaintenanceSculpting = 32
    PricingMethod = 33
    TransmissionDetail = 34
    AllowCapacitySharing = 35
    CapacityPaymentsEnabled = 36
    StartCostAmortizationPeriod = 37
    ComputeReliabilityIndices = 38
    ComputeMultiareaReliabilityIndices = 39
    StochasticMethod = 40
    WriteExpansionPlanTextFiles = 41


class LicenseFeaturesEnum(Enum):
    MASTER = 1
    MOSEKLicensed = 2
    PLEXOSSupportforMOSEK = 3
    MOSEKMixedInteger = 4
    PLEXOSInterface = 5
    PLEXOSDiagnostics = 6
    PLEXOSBaseProduct = 7
    PLEXOSModule1 = 8
    PLEXOSModule2 = 9
    PLEXOSModule3 = 10
    PLEXOSModule4 = 11
    LTPlan = 12
    PLEXOSConnect = 13
    PLEXOSSupportForGurobi = 14
    PLEXOSGasModel = 15
    PLEXOSSupportForGLPK = 16
    PLEXOSModule10 = 17
    PLEXOSModule11 = 18
    PLEXOSModule12 = 19
    PLEXOSVersion5 = 20
    PLEXOSSupportforCPLEX = 21
    PLEXOSSupportforXpressMP = 22
    MOSEKConic = 23
    PLEXOSVersion6 = 24
    XpressMPBaseProduct = 25
    XpressMPParallel = 26
    PLEXOSSupportforSoPlexSCIP = 27
    PLEXOSVersion7 = 29
    PLEXOSIntegratedEnergyModel = 100
    PLEXOSForPowerSystems = 101
    PLEXOSValuebasedReliability = 102
    PLEXOSRealtime = 103
    PLEXOSforGas = 104
    PLEXOSforWater = 105
    PLEXOSTrial = 106
    PLEXOSAPI = 1000


class LineCompaniesEnum(Enum):
    Share = 1


class LineDispatchTypeEnum(Enum):
    Regulated = 0
    Entrepreneurial = 1


class LineEnforceLimitsEnum(Enum):
    Never = 0
    Voltage = 1
    Always = 2
    Contingency = 3


class LineTypeEnum(Enum):
    AC = 0
    DC = 1


class ListAttributeEnum(Enum):
    Report = 1
    Filter = 2
    InclusiveEmpty = 3
    Transient = 4


class LoadMeteringPointEnum(Enum):
    GeneratorTerminal = 0
    SentOut = 1


class LossMethodEnum(Enum):
    Auto = 0
    PiecewiseLinear = 1
    Conic = 3
    SuccessiveMLF = 4
    SinglePassGPF = 5


class MLFRegionsEnum(Enum):
    LoadCoefficient = 1


class MTScheduleAttributeEnum(Enum):
    DiscountRate = 1
    DiscountPeriodType = 2
    EndEffectsMethod = 3
    StepType = 4
    AtaTime = 5
    Chronology = 6
    LDCType = 7
    BlockCount = 8
    LastBlockCount = 9
    LDCSlicingMethod = 10
    LDCWeighta = 11
    LDCWeightb = 12
    LDCWeightc = 13
    LDCWeightd = 14
    LDCPinTop = 15
    LDCPinBottom = 16
    SampleType = 17
    SamplingInterval = 18
    ReducedSampleCount = 19
    ReductionRelativeAccuracy = 20
    HeatRateDetail = 21
    UseEffectiveLoadApproach = 22
    OutageIncrement = 23
    PricingMethod = 24
    TransmissionDetail = 25
    NewEntryDriver = 26
    NewEntryCapacityMechanism = 27
    NewEntryTimeLag = 28
    StartCostAmortizationPeriod = 29
    StochasticMethod = 30
    WriteBridgeTextFiles = 31


class MaintenanceGasPipelinesEnum(Enum):
    OutageMaxFlow = 1
    OutageMaxFlowBack = 2


class MaintenanceGeneratorsEnum(Enum):
    OutageRating = 1
    OutageRatingFactor = 2
    OutageFirmCapacity = 3
    OutageFirmCapacityFactor = 4


class MaintenanceLinesEnum(Enum):
    OutageMaxRating = 1
    OutageMinRating = 2


class MarginalUnitTransmissionDetailEnum(Enum):
    Regional = 0
    System = 1


class MarketAttributeEnum(Enum):
    UnitCommitment = 1


class MarketCapacityGeneratorsEnum(Enum):
    OfferQuantity = 1
    OfferPrice = 2


class MarketCompaniesEnum(Enum):
    Share = 1


class MarketHeatGeneratorsEnum(Enum):
    ConversionRate = 1


class MarketSettlementModelEnum(Enum):
    Natural = 0
    Buy = 1
    Sell = 2


class MarketTimescaleEnum(Enum):
    RealTime = 0
    DayAhead = 1


class MarketTradingFormatEnum(Enum):
    Bilateral = 0
    POOLCO = 1


class MarketTypeEnum(Enum):
    None_ = 0
    Energy = 1
    AncillaryServices = 2
    Heat = 3
    Capacity = 4
    Fuel = 5
    Emission = 6
    Gas = 7


class MinDownTimeModeEnum(Enum):
    Relaxed = 0
    Enforced = 1


class ModelAttributeEnum(Enum):
    Enabled = 1
    ExecutionOrder = 2
    RandomNumberSeed = 3
    OutputtoFolder = 4
    MakeUniqueName = 5
    WriteInput = 6
    LoadCustomAssemblies = 7
    RunMode = 8


class ModelScenariosEnum(Enum):
    ReadOrder = 1


class MonteCarloMethodEnum(Enum):
    MonteCarlo = 0
    ConvergentMonteCarlo = 1


class MonteCarloOutageScopeEnum(Enum):
    All = 0
    ForcedOnly = 1
    MaintenanceOnly = 2
    None_ = 3


class NewEntryCapacityMechanismEnum(Enum):
    None_ = 0
    LOLPxVoLL = 1
    ReserveTrader = 2


class NewEntryContextEnum(Enum):
    Reliability = 0
    Entrepreneurial = 1


class NewEntryDriverEnum(Enum):
    None_ = 0
    ReliabilityOnly = 1
    ReliabilityAndEntrepreneurial = 2
    EntrepreurialOnly = 3


class NodeAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class NodeHubsEnum(Enum):
    PricingWeight = 1


class NodeTypeEnum(Enum):
    NodeTypeEnum_SystemObject = 0
    NodeTypeEnum_ClassGroup = 1
    NodeTypeEnum_CategoryInSystemCollection = 2
    NodeTypeEnum_SystemCollection = 3
    NodeTypeEnum_ObjectInSystemCollection = 4
    NodeTypeEnum_ObjectCollection = 5
    NodeTypeEnum_CategoryInObjectCollection = 6
    NodeTypeEnum_ObjectInObjectCollection = 7


class NonConvexModeEnum(Enum):
    Never = 0
    Auto = 1
    Always = 2


class OutAbatementConsumablesEnum(Enum):
    Consumption = 1
    Cost = 2


class OutAbatementEmissionsEnum(Enum):
    GrossEmissions = 1
    Abatement = 2
    NetEmissions = 3
    Efficiency = 4
    AbatementValue = 5


class OutCompanyEmissionsEnum(Enum):
    Production = 1
    GrossProduction = 2
    Removal = 3
    RemovalCost = 4
    Abatement = 5
    AbatementCost = 6
    Generation = 7
    Intensity = 8
    Allocation = 9
    Cost = 10


class OutCompanyFuelsEnum(Enum):
    Offtake = 1
    OfftakeRatio = 2
    InventoryCost = 3


class OutCompanyRegionsEnum(Enum):
    Load = 1
    InstalledCapacity = 2
    AvailableCapacity = 3
    Generation = 4
    MarginalCost = 5
    PriceReceived = 6
    PoolRevenue = 7
    GenerationatRRN = 8
    ContractVolume = 9
    NetContractVolume = 10
    ContractShortfall = 11
    ContractSettlement = 12
    NetContractSettlement = 13
    ShadowGeneration = 14


class OutCompanyReservesEnum(Enum):
    Provision = 1
    Revenue = 2


class OutEmissionFuelsEnum(Enum):
    Production = 1
    GrossProduction = 2
    Removal = 3
    RemovalCost = 4
    Abatement = 5
    AbatementCost = 6
    Generation = 7
    Intensity = 8
    Cost = 9


class OutEmissionGasNodesEnum(Enum):
    Production = 1
    Cost = 2


class OutEmissionGeneratorsEnum(Enum):
    GenerationProduction = 1
    UnitStartProduction = 2
    Production = 3
    GrossProduction = 4
    Removal = 5
    RemovalCost = 6
    Abatement = 7
    AbatementCost = 8
    Generation = 9
    Intensity = 10
    Cost = 11
    IncrementalProductionRate = 12
    IncrementalCost = 13
    SRMC = 14


class OutFinancialContractRegionsEnum(Enum):
    SettlementPrice = 1
    Shortfall = 2
    SettlementQuantity = 3
    Settlement = 4


class OutGasDemandCompaniesEnum(Enum):
    Demand = 1
    Shortage = 2
    ShortageCost = 3
    Excess = 4
    ExcessCost = 5
    NetDemand = 6
    Cost = 7


class OutGasFieldCompaniesEnum(Enum):
    Production = 1
    ProductionCost = 2
    FOMCost = 3
    FixedCosts = 4
    ShadowPrice = 5
    NetRevenue = 6
    NetProfit = 7


class OutGasPipelineGasNodeFromEnum(Enum):
    ParticipationFactor = 1


class OutGasPipelineGasNodeToEnum(Enum):
    ParticipationFactor = 1


class OutGeneratorCompaniesEnum(Enum):
    Generation = 1
    DispatchableCapacity = 2
    UndispatchedCapacity = 3
    FuelOfftake = 4
    StartFuelOfftake = 5
    HeatFuelOfftake = 6
    WasteHeat = 7
    NoCostCapacity = 8
    FixedLoadGeneration = 9
    MinLoadGeneration = 10
    AuxiliaryUse = 11
    PumpLoad = 12
    RaiseReserve = 13
    LowerReserve = 14
    RegulationRaiseReserve = 15
    RegulationLowerReserve = 16
    ReplacementReserve = 17
    HeatProduction = 18
    BoilerHeatProduction = 19
    FuelCost = 20
    FuelTransportCost = 21
    FuelTransitionCost = 22
    VOMCost = 23
    UoSCost = 24
    PumpCost = 25
    ReservesVOMCost = 26
    ReservesCost = 27
    HeatProductionCost = 28
    GenerationCost = 29
    StartShutdownCost = 30
    StartFuelCost = 31
    EmissionsCost = 32
    AbatementCost = 33
    TotalGenerationCost = 34
    FOMCost = 35
    EquityCost = 36
    DebtCost = 37
    ClearedOfferCost = 38
    PoolRevenue = 39
    ReservesRevenue = 40
    NetReservesRevenue = 41
    HeatRevenue = 42
    HeatMarketRevenue = 43
    FixedCosts = 44
    NetRevenue = 45
    NetProfit = 46
    MonopolyRent = 47
    ScheduledGeneration = 48
    ScheduledRevenue = 49
    ConstrainedOnRevenue = 50
    ConstrainedOffRevenue = 51
    ScheduledGenerationCost = 52
    ScheduledOfferCost = 53
    ScheduledStartShutdownCost = 54
    InstalledCapacity = 55
    RatedCapacity = 56
    Maintenance = 57
    ForcedOutage = 58
    AvailableCapacity = 59
    CapacityBuilt = 60
    CapacityRetired = 61
    NetNewCapacity = 62
    CapacityRevenue = 63
    BuildCost = 64
    RetirementCost = 65


class OutGeneratorFuelsEnum(Enum):
    Offtake = 1
    OfftakeRatio = 2
    Generation = 3
    Price = 4
    Cost = 5
    TransportCharge = 6
    TransportCost = 7
    TransitionCost = 8
    MarginalHeatRate = 9
    SRMC = 10
    HoursAvailable = 11
    OfferQuantity = 12
    OfferPrice = 13
    CostPrice = 14
    OfferCleared = 15
    HoursinUse = 16


class OutGeneratorStartFuelsEnum(Enum):
    Offtake = 1
    Price = 2
    Cost = 3
    TransportCost = 4


class OutGeneratorTransitionEnum(Enum):
    TransitionCost = 1
    TransitionCount = 2


class OutHeatPlantFuelsEnum(Enum):
    Offtake = 1
    OfftakeRatio = 2
    Price = 3
    Cost = 4
    MarginalHeatRate = 5
    SRMC = 6
    HoursinUse = 7


class OutHeatPlantStartFuelsEnum(Enum):
    Offtake = 1
    Price = 2
    Cost = 3


class OutMarketCapacityGeneratorsEnum(Enum):
    Sales = 1
    Revenue = 2
    ClearedOfferPrice = 3
    ClearedOfferCost = 4


class OutMarketFuelsEnum(Enum):
    Sales = 1
    Purchases = 2
    Revenue = 3
    Cost = 4


class OutMarketGasNodesEnum(Enum):
    Sales = 1
    Purchases = 2
    NetSales = 3
    NetPurchases = 4
    Revenue = 5
    Cost = 6
    NetRevenue = 7
    NetCost = 8


class OutMarketHeatGeneratorsEnum(Enum):
    Sales = 1
    Revenue = 2


class OutMarketNodesEnum(Enum):
    Sales = 1
    Purchases = 2
    NetSales = 3
    NetPurchases = 4
    Revenue = 5
    Cost = 6
    NetRevenue = 7
    NetCost = 8


class OutMarketReservesEnum(Enum):
    Sales = 1
    Purchases = 2
    NetSales = 3
    NetPurchases = 4
    Revenue = 5
    Cost = 6
    NetRevenue = 7
    NetCost = 8


class OutRSICompaniesEnum(Enum):
    SupplyCapacity = 1
    BidCostMarkup = 2


class OutRSIInterfacesEnum(Enum):
    SupplyCapacity = 1


class OutRSILinesEnum(Enum):
    SupplyCapacity = 1


class OutRegionEmissionsEnum(Enum):
    Production = 1
    GrossProduction = 2
    Removal = 3
    RemovalCost = 4
    Abatement = 5
    AbatementCost = 6
    Generation = 7
    Intensity = 8
    Cost = 9


class OutRegionRegionsEnum(Enum):
    AvailableTransferCapability = 1
    AvailableTransferCapabilityBack = 2
    Imports = 3
    Exports = 4
    NetInterchange = 5
    WheelingCost = 6


class OutReserveBatteriesEnum(Enum):
    AvailableResponse = 1
    Provision = 2
    ClearedOfferPrice = 3
    ClearedOfferCost = 4
    Revenue = 5


class OutReserveGeneratorContingenciesEnum(Enum):
    Risk = 1
    ShadowPrice = 2


class OutReserveGeneratorCostAllocationEnum(Enum):
    Cost = 1


class OutReserveGeneratorsEnum(Enum):
    AvailableResponse = 1
    Provision = 2
    SpinningReserveProvision = 3
    SyncCondReserveProvision = 4
    PumpDispatchableLoadProvision = 5
    NonspinningReserveProvision = 6
    ClearedOfferPrice = 7
    ClearedOfferCost = 8
    Revenue = 9


class OutReserveLineContingenciesEnum(Enum):
    Risk = 1
    ShadowPrice = 2


class OutReservePurchasersEnum(Enum):
    AvailableResponse = 1
    Provision = 2
    Revenue = 3
    ClearedOfferPrice = 4
    ClearedOfferCost = 5
    Cost = 6


class OutReserveRegionsEnum(Enum):
    Risk = 1


class OutZoneEmissionsEnum(Enum):
    Production = 1
    GrossProduction = 2
    Removal = 3
    RemovalCost = 4
    Abatement = 5
    AbatementCost = 6
    Generation = 7
    Intensity = 8
    Cost = 9


class OutZoneZonesEnum(Enum):
    AvailableTransferCapability = 1
    AvailableTransferCapabilityBack = 2
    WheelingCost = 3


class OutageDataEnum(Enum):
    UnitsOut = 1
    Maintenance = 2
    ForcedOutage = 3


class OutageRateDenominatorEnum(Enum):
    Time = 0
    OperatingTime = 1


class OutageTypeEnum(Enum):
    None_ = 0
    Maintenance = 1
    Forced = 2


class PASAAttributeEnum(Enum):
    StepType = 1
    TransmissionDetail = 2
    IncludeDSP = 3
    IncludeDemandBids = 4
    IncludeContractGeneration = 5
    IncludeContractLoad = 6
    IncludeMarketPurchases = 7
    ConstraintsEnabled = 8
    InterfaceConstraintsEnabled = 9
    MaintenanceSculpting = 10
    ComputeReliabilityIndices = 11
    ComputeMultiareaReliabilityIndices = 12
    WriteOutageTextFiles = 13
    StochasticMethod = 14


class PLEXOSVersionEnum(Enum):
    Minor = 0
    Major = 8


class PageEnum(Enum):
    PageEnum_Objects = 0
    PageEnum_Memberships = 1
    PageEnum_Properties = 2


class PerformanceAttributeEnum(Enum):
    SOLVER = 1
    SmallLPOptimizer = 2
    SmallLPNonzeroCount = 3
    ColdStartOptimizer1 = 4
    ColdStartOptimizer2 = 5
    ColdStartOptimizer3 = 6
    HotStartOptimizer1 = 7
    HotStartOptimizer2 = 8
    HotStartOptimizer3 = 9
    MaximumThreads = 10
    MIPRootOptimizer = 11
    MIPNodeOptimizer = 12
    SmallMIPRelativeGap = 13
    SmallMIPImproveStartGap = 14
    SmallMIPMaxTime = 15
    SmallMIPIntegerCount = 16
    MIPRelativeGap = 17
    MIPImproveStartGap = 18
    MIPMaxTime = 19
    MIPMaxRelaxationRepairTime = 20
    MIPMaximumThreads = 21
    MaximumParallelTasks = 22
    MIPStartSolution = 23


class PerformanceEnum(Enum):
    MaximizeSpeed = 0
    MinimizeMemoryUse = 1


class PeriodEnum(Enum):
    Interval = 0
    Day = 1
    Week = 2
    Month = 3
    FiscalYear = 4
    Custom = 5
    Hour = 6
    Quarter = 7
    Block = 8
    Undefined = -1


class PhysicalContractCompaniesEnum(Enum):
    Share = 1


class PowerStationNodesEnum(Enum):
    GenerationParticipationFactor = 1


class ProductionAttributeEnum(Enum):
    DispatchbyPowerStation = 1
    UnitCommitmentOptimality = 2
    RoundingUpThreshold = 3
    RoundedRelaxationCommitmentModel = 4
    RoundedRelaxationTuning = 5
    RoundedRelaxationStartThreshold = 6
    RoundedRelaxationEndThreshold = 7
    RoundedRelaxationThresholdIncrement = 8
    DPCapacityFactorThreshold = 9
    DPCapacityFactorErrorThreshold = 10
    FuelUseFunctionPrecision = 11
    MaxHeatRateTranches = 12
    HeatRateErrorMethod = 13
    StartCostMethod = 14
    CapacityFactorConstraintBasis = 15
    FormulateUpfront = 16
    FormulateRampUpfront = 17
    IntegersinLookahead = 18
    ForcedOutageRelaxesMinDownTime = 19
    PumpandGenerate = 20


class ProductionCapacityFactorConstraintBasisEnum(Enum):
    MaxCapacity = 0
    Rating = 1


class ProductionEnergyConstraintDecompositionEnum(Enum):
    ToConstraints = 0
    ToProfile = 1


class ProductionFixedLoadMethod(Enum):
    RelaxWhenZero = 0
    EnforceAllPeriods = 1


class ProductionHeatRateErrorMethod(Enum):
    ThrowError = 0
    WarnAndReportRawCurve = 1
    WarnAndReportAdjustedCurve = 2
    AdjustAndContinue = 3
    AllowNonconvex = 4


class ProductionIntegersinLookaheadEnum(Enum):
    Never = 0
    Auto = 1
    Always = 2


class ProductionRampConstraintMethodEnum(Enum):
    TwoPassHeuristic = 0
    Intertemporal = 1


class ProjectAttributeEnum(Enum):
    Enabled = 1


class PropertyIDEnum(Enum):
    SystemGenerators_MustReport = 1
    SystemGenerators_RandomNumberSeed = 2
    SystemGenerators_DispatchPeriod = 3
    SystemGenerators_MaxHeatRateTranches = 4
    SystemGenerators_FormulateNonconvex = 5
    SystemGenerators_HeadEffectsMethod = 6
    SystemGenerators_MinDownTimeMode = 7
    SystemGenerators_ForcedOutageRateDenominator = 8
    SystemGenerators_RepairTimeDistribution = 9
    SystemGenerators_FixedLoadMethod = 10
    SystemGenerators_PriceSetting = 11
    SystemGenerators_OfferQuantityFormat = 12
    SystemGenerators_OffersMustClearinOrder = 13
    SystemGenerators_UnitCommitmentOptimality = 14
    SystemGenerators_RoundingUpThreshold = 15
    SystemGenerators_IncludeinRoundedRelaxationMeritOrder = 16
    SystemGenerators_StartProfileRange = 17
    SystemGenerators_ExpansionOptimality = 18
    SystemGenerators_DecliningDepreciationBalance = 19
    SystemGenerators_EnergyLimitDecompositionMethod = 20
    SystemGenerators_IncludeinUplift = 21
    SystemGenerators_IncludeinCapacityPayments = 22
    SystemGenerators_BalancePeriod = 23
    SystemGenerators_InternalVolumeScalar = 24
    SystemGenerators_EndEffectsMethod = 25
    SystemGenerators_RecyclePenalty = 26
    SystemGenerators_DecompositionMethod = 27
    SystemGenerators_DecompositionPenaltya = 28
    SystemGenerators_DecompositionPenaltyb = 29
    SystemGenerators_DecompositionPenaltyc = 30
    SystemGenerators_DecompositionPenaltyx = 31
    SystemGenerators_DecompositionBoundPenalty = 32
    SystemGenerators_EnforceBounds = 33
    SystemGenerators_IsStrategic = 34
    SystemGenerators_TransitionType = 35
    SystemGenerators_Units = 36
    SystemGenerators_MaxCapacity = 37
    SystemGenerators_MinStableLevel = 38
    SystemGenerators_MinStableFactor = 39
    SystemGenerators_FuelPrice = 40
    SystemGenerators_LoadPoint = 41
    SystemGenerators_HeatRate = 42
    SystemGenerators_HeatRateBase = 43
    SystemGenerators_HeatRateIncr = 44
    SystemGenerators_HeatRateIncr2 = 45
    SystemGenerators_HeatRateIncr3 = 46
    SystemGenerators_VOMCharge = 47
    SystemGenerators_UoSCharge = 48
    SystemGenerators_RunningCost = 49
    SystemGenerators_StartCost = 50
    SystemGenerators_StartCostTime = 51
    SystemGenerators_RunUpRate = 52
    SystemGenerators_StartProfile = 53
    SystemGenerators_StartPenalty = 54
    SystemGenerators_ShutdownCost = 55
    SystemGenerators_RunDownRate = 56
    SystemGenerators_ShutdownProfile = 57
    SystemGenerators_ShutdownPenalty = 58
    SystemGenerators_Rating = 59
    SystemGenerators_RatingFactor = 60
    SystemGenerators_MinUpTime = 61
    SystemGenerators_MinDownTime = 62
    SystemGenerators_MaxUpTime = 63
    SystemGenerators_MaxDownTime = 64
    SystemGenerators_MustRunUnits = 65
    SystemGenerators_FixedLoad = 66
    SystemGenerators_FixedLoadPenalty = 67
    SystemGenerators_MinLoad = 68
    SystemGenerators_MinLoadPenalty = 69
    SystemGenerators_MaxLoad = 70
    SystemGenerators_Commit = 71
    SystemGenerators_FuelMixPenalty = 72
    SystemGenerators_RampUpCharge = 73
    SystemGenerators_RampDownCharge = 74
    SystemGenerators_MaxRampUp = 75
    SystemGenerators_MaxRampUpPenalty = 76
    SystemGenerators_MaxRampDown = 77
    SystemGenerators_MaxRampDownPenalty = 78
    SystemGenerators_RoughRunningPoint = 79
    SystemGenerators_RoughRunningRange = 80
    SystemGenerators_RegulationPoint = 81
    SystemGenerators_RegulationRange = 82
    SystemGenerators_AuxFixed = 83
    SystemGenerators_AuxBase = 84
    SystemGenerators_AuxIncr = 85
    SystemGenerators_MarginalLossFactor = 86
    SystemGenerators_EfficiencyBase = 87
    SystemGenerators_EfficiencyIncr = 88
    SystemGenerators_PumpEfficiency = 89
    SystemGenerators_PumpLoad = 90
    SystemGenerators_PumpUnits = 91
    SystemGenerators_MinPumpLoad = 92
    SystemGenerators_MustPumpUnits = 93
    SystemGenerators_MaxUnitsPumping = 94
    SystemGenerators_FixedPumpLoad = 95
    SystemGenerators_FixedPumpLoadPenalty = 96
    SystemGenerators_PumpUoSCharge = 97
    SystemGenerators_MinPumpTime = 98
    SystemGenerators_MinPumpDownTime = 99
    SystemGenerators_ReservesVOMCharge = 100
    SystemGenerators_SyncCondUnits = 101
    SystemGenerators_MustrunSyncCondUnits = 102
    SystemGenerators_SyncCondLoad = 103
    SystemGenerators_SyncCondVOMCharge = 104
    SystemGenerators_ReserveShare = 105
    SystemGenerators_InitialGeneration = 106
    SystemGenerators_InitialUnitsGenerating = 107
    SystemGenerators_InitialHoursUp = 108
    SystemGenerators_InitialHoursDown = 109
    SystemGenerators_InitialPumping = 110
    SystemGenerators_InitialUnitsPumping = 111
    SystemGenerators_InitialHoursPumping = 112
    SystemGenerators_GeneratortoPumpSwitchTime = 113
    SystemGenerators_PumptoGeneratorSwitchTime = 114
    SystemGenerators_EfficiencyDegradation = 115
    SystemGenerators_LastStartState = 116
    SystemGenerators_ReferenceGeneration = 117
    SystemGenerators_LoadSubtracter = 118
    SystemGenerators_PriceFollowing = 119
    SystemGenerators_LoadFollowingProfile = 120
    SystemGenerators_LoadFollowingFactor = 121
    SystemGenerators_BoilerEfficiency = 122
    SystemGenerators_HeatLoad = 123
    SystemGenerators_PowertoHeatRatio = 124
    SystemGenerators_CHPElectricHeatRateIncr = 125
    SystemGenerators_CHPHeatSurrogateRateIncr = 126
    SystemGenerators_BoilerHeatRateIncr = 127
    SystemGenerators_MaxBoilerHeat = 128
    SystemGenerators_MaxHeat = 129
    SystemGenerators_MinHeat = 130
    SystemGenerators_OpeningHeat = 131
    SystemGenerators_HeatWithdrawalCharge = 132
    SystemGenerators_HeatInjectionCharge = 133
    SystemGenerators_FixedCharge = 134
    SystemGenerators_HeatLoss = 135
    SystemGenerators_WaterOfftake = 136
    SystemGenerators_WaterConsumption = 137
    SystemGenerators_MaxRelease = 138
    SystemGenerators_MaxEnergy = 139
    SystemGenerators_MaxEnergyHour = 140
    SystemGenerators_MaxEnergyDay = 141
    SystemGenerators_MaxEnergyWeek = 142
    SystemGenerators_MaxEnergyMonth = 143
    SystemGenerators_MaxEnergyYear = 144
    SystemGenerators_MinEnergy = 145
    SystemGenerators_MinEnergyHour = 146
    SystemGenerators_MinEnergyDay = 147
    SystemGenerators_MinEnergyWeek = 148
    SystemGenerators_MinEnergyMonth = 149
    SystemGenerators_MinEnergyYear = 150
    SystemGenerators_MaxCapacityFactor = 151
    SystemGenerators_MaxCapacityFactorHour = 152
    SystemGenerators_MaxCapacityFactorDay = 153
    SystemGenerators_MaxCapacityFactorWeek = 154
    SystemGenerators_MaxCapacityFactorMonth = 155
    SystemGenerators_MaxCapacityFactorYear = 156
    SystemGenerators_MinCapacityFactor = 157
    SystemGenerators_MinCapacityFactorHour = 158
    SystemGenerators_MinCapacityFactorDay = 159
    SystemGenerators_MinCapacityFactorWeek = 160
    SystemGenerators_MinCapacityFactorMonth = 161
    SystemGenerators_MinCapacityFactorYear = 162
    SystemGenerators_MaxEnergyPenalty = 163
    SystemGenerators_MinEnergyPenalty = 164
    SystemGenerators_MaxStarts = 165
    SystemGenerators_MaxStartsHour = 166
    SystemGenerators_MaxStartsDay = 167
    SystemGenerators_MaxStartsWeek = 168
    SystemGenerators_MaxStartsMonth = 169
    SystemGenerators_MaxStartsYear = 170
    SystemGenerators_MaxStartsPenalty = 171
    SystemGenerators_EnergyScalar = 172
    SystemGenerators_MaxHeatWithdrawal = 173
    SystemGenerators_MaxHeatWithdrawalHour = 174
    SystemGenerators_MaxHeatWithdrawalDay = 175
    SystemGenerators_MaxHeatWithdrawalWeek = 176
    SystemGenerators_MaxHeatWithdrawalMonth = 177
    SystemGenerators_MaxHeatWithdrawalYear = 178
    SystemGenerators_MaxHeatInjection = 179
    SystemGenerators_MaxHeatInjectionHour = 180
    SystemGenerators_MaxHeatInjectionDay = 181
    SystemGenerators_MaxHeatInjectionWeek = 182
    SystemGenerators_MaxHeatInjectionMonth = 183
    SystemGenerators_MaxHeatInjectionYear = 184
    SystemGenerators_MinHeatWithdrawal = 185
    SystemGenerators_MinHeatWithdrawalHour = 186
    SystemGenerators_MinHeatWithdrawalDay = 187
    SystemGenerators_MinHeatWithdrawalWeek = 188
    SystemGenerators_MinHeatWithdrawalMonth = 189
    SystemGenerators_MinHeatWithdrawalYear = 190
    SystemGenerators_MinHeatInjection = 191
    SystemGenerators_MinHeatInjectionHour = 192
    SystemGenerators_MinHeatInjectionDay = 193
    SystemGenerators_MinHeatInjectionWeek = 194
    SystemGenerators_MinHeatInjectionMonth = 195
    SystemGenerators_MinHeatInjectionYear = 196
    SystemGenerators_OfferBase = 197
    SystemGenerators_OfferNoLoadCost = 198
    SystemGenerators_OfferQuantity = 199
    SystemGenerators_OfferPrice = 200
    SystemGenerators_OfferQuantityScalar = 201
    SystemGenerators_OfferPriceIncr = 202
    SystemGenerators_OfferPriceScalar = 203
    SystemGenerators_Markup = 204
    SystemGenerators_BidCostMarkup = 205
    SystemGenerators_MarkupPoint = 206
    SystemGenerators_PumpBidBase = 207
    SystemGenerators_PumpBidQuantity = 208
    SystemGenerators_PumpBidPrice = 209
    SystemGenerators_PumpBidQuantityScalar = 210
    SystemGenerators_PumpBidPriceIncr = 211
    SystemGenerators_PumpBidPriceScalar = 212
    SystemGenerators_StrategicRating = 213
    SystemGenerators_StrategicReferencePrice = 214
    SystemGenerators_InitialAge = 215
    SystemGenerators_PowerDegradation = 216
    SystemGenerators_CapacityDegradation = 217
    SystemGenerators_FOMCharge = 218
    SystemGenerators_EquityCharge = 219
    SystemGenerators_DebtCharge = 220
    SystemGenerators_FirmCapacity = 221
    SystemGenerators_UnitsOut = 222
    SystemGenerators_Maintenance = 223
    SystemGenerators_ForcedOutage = 224
    SystemGenerators_MaintenanceRate = 225
    SystemGenerators_MaintenanceFrequency = 226
    SystemGenerators_ForcedOutageRate = 227
    SystemGenerators_OutageFactor = 228
    SystemGenerators_OutageRating = 229
    SystemGenerators_OutagePumpLoad = 230
    SystemGenerators_InitialOperatingHours = 231
    SystemGenerators_MeanTimetoRepair = 232
    SystemGenerators_MinTimeToRepair = 233
    SystemGenerators_MaxTimeToRepair = 234
    SystemGenerators_RepairTimeShape = 235
    SystemGenerators_RepairTimeScale = 236
    SystemGenerators_BuildCost = 237
    SystemGenerators_RetirementCost = 238
    SystemGenerators_OnetimeCost = 239
    SystemGenerators_LeadTime = 240
    SystemGenerators_ProjectStartDate = 241
    SystemGenerators_CommissionDate = 242
    SystemGenerators_TechnicalLife = 243
    SystemGenerators_WACC = 244
    SystemGenerators_EconomicLife = 245
    SystemGenerators_MaxUnitsBuilt = 246
    SystemGenerators_MaxUnitsRetired = 247
    SystemGenerators_MinUnitsBuilt = 248
    SystemGenerators_MinUnitsRetired = 249
    SystemGenerators_MaxUnitsBuiltinYear = 250
    SystemGenerators_MaxUnitsRetiredinYear = 251
    SystemGenerators_MinUnitsBuiltinYear = 252
    SystemGenerators_MinUnitsRetiredinYear = 253
    SystemGenerators_BuildSetSize = 254
    SystemGenerators_CapacityPrice = 255
    SystemGenerators_UnitCommitmentNonanticipativity = 256
    SystemGenerators_UnitCommitmentNonanticipativityTime = 257
    SystemGenerators_PumpUnitCommitmentNonanticipativity = 258
    SystemGenerators_PumpUnitCommitmentNonanticipativityTime = 259
    SystemGenerators_GenerationNonanticipativity = 260
    SystemGenerators_GenerationNonanticipativityTime = 261
    SystemGenerators_PumpLoadNonanticipativity = 262
    SystemGenerators_PumpLoadNonanticipativityTime = 263
    SystemGenerators_BuildNonanticipativity = 264
    SystemGenerators_RetireNonanticipativity = 265
    SystemGenerators_x = 266
    SystemGenerators_y = 267
    SystemGenerators_z = 268
    SystemFuels_BalancePeriod = 269
    SystemFuels_DecompositionMethod = 270
    SystemFuels_DecompositionPenaltya = 271
    SystemFuels_DecompositionPenaltyb = 272
    SystemFuels_DecompositionPenaltyc = 273
    SystemFuels_DecompositionPenaltyx = 274
    SystemFuels_DecompositionBoundPenalty = 275
    SystemFuels_Units = 276
    SystemFuels_Price = 277
    SystemFuels_Tax = 278
    SystemFuels_PriceIncr = 279
    SystemFuels_PriceScalar = 280
    SystemFuels_HeatValue = 281
    SystemFuels_MaxOfftake = 282
    SystemFuels_MaxOfftakeHour = 283
    SystemFuels_MaxOfftakeDay = 284
    SystemFuels_MaxOfftakeWeek = 285
    SystemFuels_MaxOfftakeMonth = 286
    SystemFuels_MaxOfftakeYear = 287
    SystemFuels_MinOfftake = 288
    SystemFuels_MinOfftakeHour = 289
    SystemFuels_MinOfftakeDay = 290
    SystemFuels_MinOfftakeWeek = 291
    SystemFuels_MinOfftakeMonth = 292
    SystemFuels_MinOfftakeYear = 293
    SystemFuels_ShadowPrice = 294
    SystemFuels_ShadowPriceIncr = 295
    SystemFuels_ShadowPriceScalar = 296
    SystemFuels_MaxInventory = 297
    SystemFuels_MinInventory = 298
    SystemFuels_OpeningInventory = 299
    SystemFuels_Delivery = 300
    SystemFuels_DeliveryCharge = 301
    SystemFuels_InventoryCharge = 302
    SystemFuels_ReservationCharge = 303
    SystemFuels_WithdrawalCharge = 304
    SystemFuels_MaxWithdrawal = 305
    SystemFuels_MaxWithdrawalHour = 306
    SystemFuels_MaxWithdrawalDay = 307
    SystemFuels_MaxWithdrawalWeek = 308
    SystemFuels_MaxWithdrawalMonth = 309
    SystemFuels_MaxWithdrawalYear = 310
    SystemFuels_MinWithdrawal = 311
    SystemFuels_MinWithdrawalHour = 312
    SystemFuels_MinWithdrawalDay = 313
    SystemFuels_MinWithdrawalWeek = 314
    SystemFuels_MinWithdrawalMonth = 315
    SystemFuels_MinWithdrawalYear = 316
    SystemFuels_FOMCharge = 317
    SystemFuels_x = 318
    SystemFuels_y = 319
    SystemFuels_z = 320
    SystemFuelContracts_Quantity = 321
    SystemFuelContracts_QuantityHour = 322
    SystemFuelContracts_QuantityDay = 323
    SystemFuelContracts_QuantityWeek = 324
    SystemFuelContracts_QuantityMonth = 325
    SystemFuelContracts_QuantityYear = 326
    SystemFuelContracts_Price = 327
    SystemFuelContracts_PriceIncr = 328
    SystemFuelContracts_PriceScalar = 329
    SystemFuelContracts_TakeorPayQuantity = 330
    SystemFuelContracts_TakeorPayQuantityHour = 331
    SystemFuelContracts_TakeorPayQuantityDay = 332
    SystemFuelContracts_TakeorPayQuantityWeek = 333
    SystemFuelContracts_TakeorPayQuantityMonth = 334
    SystemFuelContracts_TakeorPayQuantityYear = 335
    SystemFuelContracts_TakeorPayPrice = 336
    SystemFuelContracts_FOMCharge = 337
    SystemFuelContracts_x = 338
    SystemFuelContracts_y = 339
    SystemFuelContracts_z = 340
    SystemEmissions_Price = 341
    SystemEmissions_MaxProduction = 342
    SystemEmissions_MaxProductionHour = 343
    SystemEmissions_MaxProductionDay = 344
    SystemEmissions_MaxProductionWeek = 345
    SystemEmissions_MaxProductionMonth = 346
    SystemEmissions_MaxProductionYear = 347
    SystemEmissions_MaxProductionPenalty = 348
    SystemEmissions_ShadowPrice = 349
    SystemEmissions_x = 350
    SystemEmissions_y = 351
    SystemEmissions_z = 352
    SystemAbatements_Units = 353
    SystemAbatements_AbatementCost = 354
    SystemAbatements_RunningCost = 355
    SystemAbatements_VOMCharge = 356
    SystemAbatements_Efficiency = 357
    SystemAbatements_MaxAbatement = 358
    SystemAbatements_FOMCharge = 359
    SystemAbatements_UnitsOut = 360
    SystemAbatements_x = 361
    SystemAbatements_y = 362
    SystemAbatements_z = 363
    SystemStorages_Model = 364
    SystemStorages_BalancePeriod = 365
    SystemStorages_InternalVolumeScalar = 366
    SystemStorages_EndEffectsMethod = 367
    SystemStorages_RecyclePenalty = 368
    SystemStorages_DecompositionMethod = 369
    SystemStorages_DecompositionPenaltya = 370
    SystemStorages_DecompositionPenaltyb = 371
    SystemStorages_DecompositionPenaltyc = 372
    SystemStorages_DecompositionPenaltyx = 373
    SystemStorages_DecompositionBoundPenalty = 374
    SystemStorages_EnforceBounds = 375
    SystemStorages_SpillPenalty = 376
    SystemStorages_NonphysicalInflowPenalty = 377
    SystemStorages_NonphysicalSpillPenalty = 378
    SystemStorages_Units = 379
    SystemStorages_MaxVolume = 380
    SystemStorages_InitialVolume = 381
    SystemStorages_MinVolume = 382
    SystemStorages_MaxLevel = 383
    SystemStorages_InitialLevel = 384
    SystemStorages_MinLevel = 385
    SystemStorages_LowRefLevel = 386
    SystemStorages_LowRefArea = 387
    SystemStorages_HighRefLevel = 388
    SystemStorages_HighRefArea = 389
    SystemStorages_NaturalInflow = 390
    SystemStorages_NaturalInflowIncr = 391
    SystemStorages_NaturalInflowScalar = 392
    SystemStorages_WaterValue = 393
    SystemStorages_EnergyValue = 394
    SystemStorages_WaterValuePoint = 395
    SystemStorages_DownstreamEfficiency = 396
    SystemStorages_LossRate = 397
    SystemStorages_MinRelease = 398
    SystemStorages_MaxRelease = 399
    SystemStorages_MaxGeneratorRelease = 400
    SystemStorages_MinReleasePenalty = 401
    SystemStorages_MaxReleasePenalty = 402
    SystemStorages_MaxSpill = 403
    SystemStorages_MaxRamp = 404
    SystemStorages_MaxRampHour = 405
    SystemStorages_MaxRampDay = 406
    SystemStorages_MaxRampWeek = 407
    SystemStorages_MaxRampMonth = 408
    SystemStorages_MaxRampYear = 409
    SystemStorages_MaxRampPenalty = 410
    SystemStorages_Target = 411
    SystemStorages_TargetHour = 412
    SystemStorages_TargetDay = 413
    SystemStorages_TargetWeek = 414
    SystemStorages_TargetMonth = 415
    SystemStorages_TargetYear = 416
    SystemStorages_TargetLevel = 417
    SystemStorages_TargetLevelHour = 418
    SystemStorages_TargetLevelDay = 419
    SystemStorages_TargetLevelWeek = 420
    SystemStorages_TargetLevelMonth = 421
    SystemStorages_TargetLevelYear = 422
    SystemStorages_TargetPenalty = 423
    SystemStorages_TrajectoryNonanticipativity = 424
    SystemStorages_TrajectoryNonanticipativityVolume = 425
    SystemStorages_TrajectoryNonanticipativityTime = 426
    SystemStorages_x = 427
    SystemStorages_y = 428
    SystemStorages_z = 429
    SystemWaterways_TraversalTime = 430
    SystemWaterways_FlowControl = 431
    SystemWaterways_MaxFlow = 432
    SystemWaterways_MinFlow = 433
    SystemWaterways_InitialFlow = 434
    SystemWaterways_MaxRamp = 435
    SystemWaterways_MaxFlowPenalty = 436
    SystemWaterways_MinFlowPenalty = 437
    SystemWaterways_MaxRampPenalty = 438
    SystemWaterways_InputScalar = 439
    SystemWaterways_OutputScalar = 440
    SystemWaterways_x = 441
    SystemWaterways_y = 442
    SystemWaterways_z = 443
    SystemPowerStations_IsEnabled = 444
    SystemPhysicalContracts_OfferQuantityFormat = 445
    SystemPhysicalContracts_PriceSetting = 446
    SystemPhysicalContracts_Units = 447
    SystemPhysicalContracts_MaxGeneration = 448
    SystemPhysicalContracts_MaxLoad = 449
    SystemPhysicalContracts_MinGeneration = 450
    SystemPhysicalContracts_MinLoad = 451
    SystemPhysicalContracts_OfferQuantity = 452
    SystemPhysicalContracts_OfferPrice = 453
    SystemPhysicalContracts_BidQuantity = 454
    SystemPhysicalContracts_BidPrice = 455
    SystemPhysicalContracts_FirmCapacity = 456
    SystemPhysicalContracts_LoadObligation = 457
    SystemPhysicalContracts_CapacityCharge = 458
    SystemPhysicalContracts_CapacityChargeHour = 459
    SystemPhysicalContracts_CapacityChargeDay = 460
    SystemPhysicalContracts_CapacityChargeWeek = 461
    SystemPhysicalContracts_CapacityChargeMonth = 462
    SystemPhysicalContracts_CapacityChargeYear = 463
    SystemPhysicalContracts_MaxGenerationUnits = 464
    SystemPhysicalContracts_MaxLoadUnits = 465
    SystemPhysicalContracts_MinGenerationUnits = 466
    SystemPhysicalContracts_MinLoadUnits = 467
    SystemPhysicalContracts_BuildNonanticipativity = 468
    SystemPhysicalContracts_x = 469
    SystemPhysicalContracts_y = 470
    SystemPhysicalContracts_z = 471
    SystemPurchasers_BenefitFunctionShape = 472
    SystemPurchasers_MaxBenefitFunctionTranches = 473
    SystemPurchasers_InterruptibleLoadLogic = 474
    SystemPurchasers_PriceSetting = 475
    SystemPurchasers_Units = 476
    SystemPurchasers_MinLoad = 477
    SystemPurchasers_MaxLoad = 478
    SystemPurchasers_FixedLoad = 479
    SystemPurchasers_MaxRampDown = 480
    SystemPurchasers_MaxRampUp = 481
    SystemPurchasers_MaxEnergy = 482
    SystemPurchasers_MaxEnergyHour = 483
    SystemPurchasers_MaxEnergyDay = 484
    SystemPurchasers_MaxEnergyWeek = 485
    SystemPurchasers_MaxEnergyMonth = 486
    SystemPurchasers_MaxEnergyYear = 487
    SystemPurchasers_MinEnergy = 488
    SystemPurchasers_MinEnergyHour = 489
    SystemPurchasers_MinEnergyDay = 490
    SystemPurchasers_MinEnergyWeek = 491
    SystemPurchasers_MinEnergyMonth = 492
    SystemPurchasers_MinEnergyYear = 493
    SystemPurchasers_MaxLoadFactor = 494
    SystemPurchasers_MaxLoadFactorHour = 495
    SystemPurchasers_MaxLoadFactorDay = 496
    SystemPurchasers_MaxLoadFactorWeek = 497
    SystemPurchasers_MaxLoadFactorMonth = 498
    SystemPurchasers_MaxLoadFactorYear = 499
    SystemPurchasers_MinLoadFactor = 500
    SystemPurchasers_MinLoadFactorHour = 501
    SystemPurchasers_MinLoadFactorDay = 502
    SystemPurchasers_MinLoadFactorWeek = 503
    SystemPurchasers_MinLoadFactorMonth = 504
    SystemPurchasers_MinLoadFactorYear = 505
    SystemPurchasers_MaxEnergyPenalty = 506
    SystemPurchasers_MinEnergyPenalty = 507
    SystemPurchasers_MarginalLossFactor = 508
    SystemPurchasers_BidQuantity = 509
    SystemPurchasers_BidPrice = 510
    SystemPurchasers_Tariff = 511
    SystemPurchasers_DemandFnSlope = 512
    SystemPurchasers_DemandFnIntercept = 513
    SystemPurchasers_LoadObligation = 514
    SystemPurchasers_x = 515
    SystemPurchasers_y = 516
    SystemPurchasers_z = 517
    SystemReserves_Type = 518
    SystemReserves_MutuallyExclusive = 519
    SystemReserves_DynamicRisk = 520
    SystemReserves_CostAllocationModel = 521
    SystemReserves_IsEnabled = 522
    SystemReserves_IncludeinLTPlan = 523
    SystemReserves_IncludeinMTSchedule = 524
    SystemReserves_IncludeinSTSchedule = 525
    SystemReserves_UnitCommitment = 526
    SystemReserves_SharingEnabled = 527
    SystemReserves_SharingLossesEnabled = 528
    SystemReserves_MinProvision = 529
    SystemReserves_StaticRisk = 530
    SystemReserves_Timeframe = 531
    SystemReserves_Duration = 532
    SystemReserves_MaxProvision = 533
    SystemReserves_RiskAdjustmentFactor = 534
    SystemReserves_EnergyUsage = 535
    SystemReserves_VoRS = 536
    SystemReserves_PriceCap = 537
    SystemReserves_PriceFloor = 538
    SystemReserves_CutoffSize = 539
    SystemReserves_Price = 540
    SystemReserves_x = 541
    SystemReserves_y = 542
    SystemReserves_z = 543
    SystemBatteries_RandomNumberSeed = 544
    SystemBatteries_RepairTimeDistribution = 545
    SystemBatteries_EndEffectsMethod = 546
    SystemBatteries_ExpansionOptimality = 547
    SystemBatteries_Units = 548
    SystemBatteries_Capacity = 549
    SystemBatteries_MaxPower = 550
    SystemBatteries_MaxLoad = 551
    SystemBatteries_MaxSoC = 552
    SystemBatteries_MinSoC = 553
    SystemBatteries_InitialSoC = 554
    SystemBatteries_ChargeEfficiency = 555
    SystemBatteries_DischargeEfficiency = 556
    SystemBatteries_VOMCharge = 557
    SystemBatteries_UoSCharge = 558
    SystemBatteries_MaxRampUp = 559
    SystemBatteries_MaxRampUpPenalty = 560
    SystemBatteries_MaxRampDown = 561
    SystemBatteries_MaxRampDownPenalty = 562
    SystemBatteries_MaxCycles = 563
    SystemBatteries_MaxCyclesHour = 564
    SystemBatteries_MaxCyclesDay = 565
    SystemBatteries_MaxCyclesWeek = 566
    SystemBatteries_MaxCyclesMonth = 567
    SystemBatteries_MaxCyclesYear = 568
    SystemBatteries_EnergyTarget = 569
    SystemBatteries_EnergyTargetHour = 570
    SystemBatteries_EnergyTargetDay = 571
    SystemBatteries_EnergyTargetWeek = 572
    SystemBatteries_EnergyTargetMonth = 573
    SystemBatteries_EnergyTargetYear = 574
    SystemBatteries_EnergyTargetPenalty = 575
    SystemBatteries_Nonanticipativity = 576
    SystemBatteries_NonanticipativityTime = 577
    SystemBatteries_InitialAge = 578
    SystemBatteries_PowerDegradation = 579
    SystemBatteries_CapacityDegradation = 580
    SystemBatteries_FirmCapacity = 581
    SystemBatteries_FOMCharge = 582
    SystemBatteries_MaintenanceRate = 583
    SystemBatteries_MaintenanceFrequency = 584
    SystemBatteries_ForcedOutageRate = 585
    SystemBatteries_MeanTimetoRepair = 586
    SystemBatteries_MinTimeToRepair = 587
    SystemBatteries_MaxTimeToRepair = 588
    SystemBatteries_RepairTimeShape = 589
    SystemBatteries_RepairTimeScale = 590
    SystemBatteries_MaxUnitsBuilt = 591
    SystemBatteries_LeadTime = 592
    SystemBatteries_ProjectStartDate = 593
    SystemBatteries_TechnicalLife = 594
    SystemBatteries_BuildCost = 595
    SystemBatteries_WACC = 596
    SystemBatteries_EconomicLife = 597
    SystemBatteries_MinUnitsBuilt = 598
    SystemBatteries_MaxUnitsBuiltinYear = 599
    SystemBatteries_MinUnitsBuiltinYear = 600
    SystemBatteries_MaxUnitsRetired = 601
    SystemBatteries_RetirementCost = 602
    SystemBatteries_MinUnitsRetired = 603
    SystemBatteries_MaxUnitsRetiredinYear = 604
    SystemBatteries_MinUnitsRetiredinYear = 605
    SystemBatteries_BuildNonanticipativity = 606
    SystemBatteries_RetireNonanticipativity = 607
    SystemBatteries_x = 608
    SystemBatteries_y = 609
    SystemBatteries_z = 610
    SystemMaintenances_Duration = 611
    SystemMaintenances_Window = 612
    SystemMaintenances_StartWindow = 613
    SystemMaintenances_EndWindow = 614
    SystemMaintenances_Cost = 615
    SystemMaintenances_Crew = 616
    SystemMaintenances_Equipment = 617
    SystemMaintenances_LeadTime = 618
    SystemMaintenances_MutuallyExclusive = 619
    SystemMaintenances_PenaltyCost = 620
    SystemMaintenances_MinOccurrence = 621
    SystemMaintenances_MinOccurrenceHour = 622
    SystemMaintenances_MinOccurrenceDay = 623
    SystemMaintenances_MinOccurrenceWeek = 624
    SystemMaintenances_MinOccurrenceMonth = 625
    SystemMaintenances_MinOccurrenceYear = 626
    SystemMaintenances_Nonanticipativity = 627
    SystemMaintenances_x = 628
    SystemMaintenances_y = 629
    SystemMaintenances_z = 630
    SystemHeatNodes_AllowDumpHeat = 631
    SystemHeatNodes_Units = 632
    SystemHeatNodes_HeatDemand = 633
    SystemHeatNodes_x = 634
    SystemHeatNodes_y = 635
    SystemHeatNodes_z = 636
    SystemHeatPlants_UnitCommitmentOptimality = 637
    SystemHeatPlants_Units = 638
    SystemHeatPlants_MaxCapacity = 639
    SystemHeatPlants_EfficiencyBase = 640
    SystemHeatPlants_EfficiencyIncr = 641
    SystemHeatPlants_VOMCharge = 642
    SystemHeatPlants_LoadPoint = 643
    SystemHeatPlants_HeatRate = 644
    SystemHeatPlants_HeatRateBase = 645
    SystemHeatPlants_HeatRateIncr = 646
    SystemHeatPlants_StartCost = 647
    SystemHeatPlants_StartCostTime = 648
    SystemHeatPlants_RunUpRate = 649
    SystemHeatPlants_StartProfile = 650
    SystemHeatPlants_MinUpTime = 651
    SystemHeatPlants_MinDownTime = 652
    SystemHeatPlants_MaxUpTime = 653
    SystemHeatPlants_MaxDownTime = 654
    SystemHeatPlants_MaxRampUp = 655
    SystemHeatPlants_MaxRampDown = 656
    SystemHeatPlants_MinStableLevel = 657
    SystemHeatPlants_FOMCharge = 658
    SystemHeatPlants_MaxUnitsBuilt = 659
    SystemHeatPlants_LeadTime = 660
    SystemHeatPlants_ProjectStartDate = 661
    SystemHeatPlants_TechnicalLife = 662
    SystemHeatPlants_BuildCost = 663
    SystemHeatPlants_WACC = 664
    SystemHeatPlants_EconomicLife = 665
    SystemHeatPlants_MinUnitsBuilt = 666
    SystemHeatPlants_MaxUnitsBuiltinYear = 667
    SystemHeatPlants_MinUnitsBuiltinYear = 668
    SystemHeatPlants_MaxUnitsRetired = 669
    SystemHeatPlants_RetirementCost = 670
    SystemHeatPlants_MinUnitsRetired = 671
    SystemHeatPlants_MaxUnitsRetiredinYear = 672
    SystemHeatPlants_MinUnitsRetiredinYear = 673
    SystemHeatPlants_x = 674
    SystemHeatPlants_y = 675
    SystemHeatPlants_z = 676
    SystemGasFields_BalancePeriod = 677
    SystemGasFields_InternalVolumeScalar = 678
    SystemGasFields_EndEffectsMethod = 679
    SystemGasFields_RecyclePenalty = 680
    SystemGasFields_DecompositionMethod = 681
    SystemGasFields_DecompositionPenaltya = 682
    SystemGasFields_DecompositionPenaltyb = 683
    SystemGasFields_DecompositionPenaltyc = 684
    SystemGasFields_DecompositionPenaltyx = 685
    SystemGasFields_DecompositionBoundPenalty = 686
    SystemGasFields_EnforceBounds = 687
    SystemGasFields_ExpansionOptimality = 688
    SystemGasFields_Units = 689
    SystemGasFields_InitialVolume = 690
    SystemGasFields_ProductionCost = 691
    SystemGasFields_ProductionVolume = 692
    SystemGasFields_MaxRamp = 693
    SystemGasFields_MaxRampHour = 694
    SystemGasFields_MaxRampDay = 695
    SystemGasFields_MaxRampWeek = 696
    SystemGasFields_MaxRampMonth = 697
    SystemGasFields_MaxRampYear = 698
    SystemGasFields_MaxProduction = 699
    SystemGasFields_MaxProductionHour = 700
    SystemGasFields_MaxProductionDay = 701
    SystemGasFields_MaxProductionWeek = 702
    SystemGasFields_MaxProductionMonth = 703
    SystemGasFields_MaxProductionYear = 704
    SystemGasFields_MinProduction = 705
    SystemGasFields_MinProductionHour = 706
    SystemGasFields_MinProductionDay = 707
    SystemGasFields_MinProductionWeek = 708
    SystemGasFields_MinProductionMonth = 709
    SystemGasFields_MinProductionYear = 710
    SystemGasFields_Target = 711
    SystemGasFields_TargetHour = 712
    SystemGasFields_TargetDay = 713
    SystemGasFields_TargetWeek = 714
    SystemGasFields_TargetMonth = 715
    SystemGasFields_TargetYear = 716
    SystemGasFields_TargetPenalty = 717
    SystemGasFields_ExternalInjection = 718
    SystemGasFields_FOMCharge = 719
    SystemGasFields_MaxUnitsBuilt = 720
    SystemGasFields_LeadTime = 721
    SystemGasFields_ProjectStartDate = 722
    SystemGasFields_TechnicalLife = 723
    SystemGasFields_BuildCost = 724
    SystemGasFields_WACC = 725
    SystemGasFields_EconomicLife = 726
    SystemGasFields_MaxUnitsBuiltinYear = 727
    SystemGasFields_x = 728
    SystemGasFields_y = 729
    SystemGasFields_z = 730
    SystemGasPlants_ExpansionOptimality = 731
    SystemGasPlants_Units = 732
    SystemGasPlants_MaxProduction = 733
    SystemGasPlants_MinProduction = 734
    SystemGasPlants_ProcessingRate = 735
    SystemGasPlants_ProcessingCharge = 736
    SystemGasPlants_Consumption = 737
    SystemGasPlants_EnergyUsage = 738
    SystemGasPlants_VOMCharge = 739
    SystemGasPlants_FOMCharge = 740
    SystemGasPlants_MaxUnitsBuilt = 741
    SystemGasPlants_LeadTime = 742
    SystemGasPlants_ProjectStartDate = 743
    SystemGasPlants_TechnicalLife = 744
    SystemGasPlants_BuildCost = 745
    SystemGasPlants_WACC = 746
    SystemGasPlants_EconomicLife = 747
    SystemGasPlants_MinUnitsBuilt = 748
    SystemGasPlants_MaxUnitsBuiltinYear = 749
    SystemGasPlants_MinUnitsBuiltinYear = 750
    SystemGasPlants_MaxUnitsRetired = 751
    SystemGasPlants_RetirementCost = 752
    SystemGasPlants_MinUnitsRetired = 753
    SystemGasPlants_MaxUnitsRetiredinYear = 754
    SystemGasPlants_MinUnitsRetiredinYear = 755
    SystemGasPlants_x = 756
    SystemGasPlants_y = 757
    SystemGasPlants_z = 758
    SystemGasPipelines_RandomNumberSeed = 759
    SystemGasPipelines_BalancePeriod = 760
    SystemGasPipelines_InternalVolumeScalar = 761
    SystemGasPipelines_EndEffectsMethod = 762
    SystemGasPipelines_RecyclePenalty = 763
    SystemGasPipelines_DecompositionMethod = 764
    SystemGasPipelines_DecompositionPenaltya = 765
    SystemGasPipelines_DecompositionPenaltyb = 766
    SystemGasPipelines_DecompositionPenaltyc = 767
    SystemGasPipelines_DecompositionPenaltyx = 768
    SystemGasPipelines_DecompositionBoundPenalty = 769
    SystemGasPipelines_EnforceBounds = 770
    SystemGasPipelines_RepairTimeDistribution = 771
    SystemGasPipelines_ExpansionOptimality = 772
    SystemGasPipelines_Units = 773
    SystemGasPipelines_MaxFlow = 774
    SystemGasPipelines_MaxFlowHour = 775
    SystemGasPipelines_MaxFlowDay = 776
    SystemGasPipelines_MaxFlowWeek = 777
    SystemGasPipelines_MaxFlowMonth = 778
    SystemGasPipelines_MaxFlowYear = 779
    SystemGasPipelines_MaxFlowBack = 780
    SystemGasPipelines_MaxFlowBackHour = 781
    SystemGasPipelines_MaxFlowBackDay = 782
    SystemGasPipelines_MaxFlowBackWeek = 783
    SystemGasPipelines_MaxFlowBackMonth = 784
    SystemGasPipelines_MaxFlowBackYear = 785
    SystemGasPipelines_Diameter = 786
    SystemGasPipelines_Roughness = 787
    SystemGasPipelines_Length = 788
    SystemGasPipelines_PumpEfficiency = 789
    SystemGasPipelines_FlowCharge = 790
    SystemGasPipelines_FlowChargeBack = 791
    SystemGasPipelines_InitialVolume = 792
    SystemGasPipelines_MaxVolume = 793
    SystemGasPipelines_MinVolume = 794
    SystemGasPipelines_VolumeImbalance = 795
    SystemGasPipelines_ImbalanceCharge = 796
    SystemGasPipelines_FOMCharge = 797
    SystemGasPipelines_ConsumptionAllocation = 798
    SystemGasPipelines_UnitsOut = 799
    SystemGasPipelines_MaintenanceRate = 800
    SystemGasPipelines_MaintenanceFrequency = 801
    SystemGasPipelines_ForcedOutageRate = 802
    SystemGasPipelines_OutageMaxFlow = 803
    SystemGasPipelines_OutageMaxFlowBack = 804
    SystemGasPipelines_MeanTimetoRepair = 805
    SystemGasPipelines_MinTimeToRepair = 806
    SystemGasPipelines_MaxTimeToRepair = 807
    SystemGasPipelines_RepairTimeShape = 808
    SystemGasPipelines_RepairTimeScale = 809
    SystemGasPipelines_MaxUnitsBuilt = 810
    SystemGasPipelines_LeadTime = 811
    SystemGasPipelines_ProjectStartDate = 812
    SystemGasPipelines_TechnicalLife = 813
    SystemGasPipelines_BuildCost = 814
    SystemGasPipelines_WACC = 815
    SystemGasPipelines_EconomicLife = 816
    SystemGasPipelines_MinUnitsBuilt = 817
    SystemGasPipelines_MaxUnitsBuiltinYear = 818
    SystemGasPipelines_MinUnitsBuiltinYear = 819
    SystemGasPipelines_MaxUnitsRetired = 820
    SystemGasPipelines_RetirementCost = 821
    SystemGasPipelines_MinUnitsRetired = 822
    SystemGasPipelines_MaxUnitsRetiredinYear = 823
    SystemGasPipelines_MinUnitsRetiredinYear = 824
    SystemGasPipelines_x = 825
    SystemGasPipelines_y = 826
    SystemGasPipelines_z = 827
    SystemGasNodes_ExpansionOptimality = 828
    SystemGasNodes_Units = 829
    SystemGasNodes_FlowCharge = 830
    SystemGasNodes_MaxFlow = 831
    SystemGasNodes_MaxFlowHour = 832
    SystemGasNodes_MaxFlowDay = 833
    SystemGasNodes_MaxFlowWeek = 834
    SystemGasNodes_MaxFlowMonth = 835
    SystemGasNodes_MaxFlowYear = 836
    SystemGasNodes_GasSecurity = 837
    SystemGasNodes_FOMCharge = 838
    SystemGasNodes_MaxUnitsBuilt = 839
    SystemGasNodes_LeadTime = 840
    SystemGasNodes_ProjectStartDate = 841
    SystemGasNodes_TechnicalLife = 842
    SystemGasNodes_BuildCost = 843
    SystemGasNodes_WACC = 844
    SystemGasNodes_EconomicLife = 845
    SystemGasNodes_MinUnitsBuilt = 846
    SystemGasNodes_MaxUnitsBuiltinYear = 847
    SystemGasNodes_MinUnitsBuiltinYear = 848
    SystemGasNodes_MaxUnitsRetired = 849
    SystemGasNodes_RetirementCost = 850
    SystemGasNodes_MinUnitsRetired = 851
    SystemGasNodes_MaxUnitsRetiredinYear = 852
    SystemGasNodes_MinUnitsRetiredinYear = 853
    SystemGasNodes_x = 854
    SystemGasNodes_y = 855
    SystemGasNodes_z = 856
    SystemGasStorages_BalancePeriod = 857
    SystemGasStorages_InternalVolumeScalar = 858
    SystemGasStorages_EndEffectsMethod = 859
    SystemGasStorages_RecyclePenalty = 860
    SystemGasStorages_DecompositionMethod = 861
    SystemGasStorages_DecompositionPenaltya = 862
    SystemGasStorages_DecompositionPenaltyb = 863
    SystemGasStorages_DecompositionPenaltyc = 864
    SystemGasStorages_DecompositionPenaltyx = 865
    SystemGasStorages_DecompositionBoundPenalty = 866
    SystemGasStorages_EnforceBounds = 867
    SystemGasStorages_ExpansionOptimality = 868
    SystemGasStorages_Units = 869
    SystemGasStorages_MaxVolume = 870
    SystemGasStorages_MinVolume = 871
    SystemGasStorages_InitialVolume = 872
    SystemGasStorages_WithdrawalCharge = 873
    SystemGasStorages_InjectionCharge = 874
    SystemGasStorages_InjectionRatchet = 875
    SystemGasStorages_WithdrawalRatchet = 876
    SystemGasStorages_MaxWithdrawal = 877
    SystemGasStorages_MaxWithdrawalHour = 878
    SystemGasStorages_MaxWithdrawalDay = 879
    SystemGasStorages_MaxWithdrawalWeek = 880
    SystemGasStorages_MaxWithdrawalMonth = 881
    SystemGasStorages_MaxWithdrawalYear = 882
    SystemGasStorages_MaxInjection = 883
    SystemGasStorages_MaxInjectionHour = 884
    SystemGasStorages_MaxInjectionDay = 885
    SystemGasStorages_MaxInjectionWeek = 886
    SystemGasStorages_MaxInjectionMonth = 887
    SystemGasStorages_MaxInjectionYear = 888
    SystemGasStorages_MinWithdrawal = 889
    SystemGasStorages_MinWithdrawalHour = 890
    SystemGasStorages_MinWithdrawalDay = 891
    SystemGasStorages_MinWithdrawalWeek = 892
    SystemGasStorages_MinWithdrawalMonth = 893
    SystemGasStorages_MinWithdrawalYear = 894
    SystemGasStorages_MinInjection = 895
    SystemGasStorages_MinInjectionHour = 896
    SystemGasStorages_MinInjectionDay = 897
    SystemGasStorages_MinInjectionWeek = 898
    SystemGasStorages_MinInjectionMonth = 899
    SystemGasStorages_MinInjectionYear = 900
    SystemGasStorages_MaxRamp = 901
    SystemGasStorages_MaxRampHour = 902
    SystemGasStorages_MaxRampDay = 903
    SystemGasStorages_MaxRampWeek = 904
    SystemGasStorages_MaxRampMonth = 905
    SystemGasStorages_MaxRampYear = 906
    SystemGasStorages_Target = 907
    SystemGasStorages_TargetHour = 908
    SystemGasStorages_TargetDay = 909
    SystemGasStorages_TargetWeek = 910
    SystemGasStorages_TargetMonth = 911
    SystemGasStorages_TargetYear = 912
    SystemGasStorages_TargetPenalty = 913
    SystemGasStorages_EnergyUsage = 914
    SystemGasStorages_LossRate = 915
    SystemGasStorages_WithdrawalRateScalar = 916
    SystemGasStorages_WithdrawalVolume = 917
    SystemGasStorages_InjectionRateScalar = 918
    SystemGasStorages_InjectionVolume = 919
    SystemGasStorages_ExternalInjection = 920
    SystemGasStorages_FOMCharge = 921
    SystemGasStorages_MaxUnitsBuilt = 922
    SystemGasStorages_LeadTime = 923
    SystemGasStorages_ProjectStartDate = 924
    SystemGasStorages_TechnicalLife = 925
    SystemGasStorages_BuildCost = 926
    SystemGasStorages_WACC = 927
    SystemGasStorages_EconomicLife = 928
    SystemGasStorages_MinUnitsBuilt = 929
    SystemGasStorages_MaxUnitsBuiltinYear = 930
    SystemGasStorages_MinUnitsBuiltinYear = 931
    SystemGasStorages_MaxUnitsRetired = 932
    SystemGasStorages_RetirementCost = 933
    SystemGasStorages_MinUnitsRetired = 934
    SystemGasStorages_MaxUnitsRetiredinYear = 935
    SystemGasStorages_MinUnitsRetiredinYear = 936
    SystemGasStorages_TrajectoryNonanticipativity = 937
    SystemGasStorages_TrajectoryNonanticipativityVolume = 938
    SystemGasStorages_TrajectoryNonanticipativityTime = 939
    SystemGasStorages_x = 940
    SystemGasStorages_y = 941
    SystemGasStorages_z = 942
    SystemGasDemands_Demand = 943
    SystemGasDemands_ShortagePrice = 944
    SystemGasDemands_ExcessPrice = 945
    SystemGasDemands_BidQuantity = 946
    SystemGasDemands_BidPrice = 947
    SystemGasDemands_x = 948
    SystemGasDemands_y = 949
    SystemGasDemands_z = 950
    SystemGasBasins_MaxProduction = 951
    SystemGasBasins_MaxProductionHour = 952
    SystemGasBasins_MaxProductionDay = 953
    SystemGasBasins_MaxProductionWeek = 954
    SystemGasBasins_MaxProductionMonth = 955
    SystemGasBasins_MaxProductionYear = 956
    SystemGasBasins_MinProduction = 957
    SystemGasBasins_MinProductionHour = 958
    SystemGasBasins_MinProductionDay = 959
    SystemGasBasins_MinProductionWeek = 960
    SystemGasBasins_MinProductionMonth = 961
    SystemGasBasins_MinProductionYear = 962
    SystemGasBasins_x = 963
    SystemGasBasins_y = 964
    SystemGasBasins_z = 965
    SystemGasZones_x = 966
    SystemGasZones_y = 967
    SystemGasZones_z = 968
    SystemGasContracts_PriceSetting = 969
    SystemGasContracts_Quantity = 970
    SystemGasContracts_QuantityHour = 971
    SystemGasContracts_QuantityDay = 972
    SystemGasContracts_QuantityWeek = 973
    SystemGasContracts_QuantityMonth = 974
    SystemGasContracts_QuantityYear = 975
    SystemGasContracts_TakeorPayQuantity = 976
    SystemGasContracts_TakeorPayQuantityHour = 977
    SystemGasContracts_TakeorPayQuantityDay = 978
    SystemGasContracts_TakeorPayQuantityWeek = 979
    SystemGasContracts_TakeorPayQuantityMonth = 980
    SystemGasContracts_TakeorPayQuantityYear = 981
    SystemGasContracts_TakeorPayPrice = 982
    SystemGasContracts_Price = 983
    SystemGasContracts_x = 984
    SystemGasContracts_y = 985
    SystemGasContracts_z = 986
    SystemGasTransports_VoyageTime = 987
    SystemGasTransports_LoadingTime = 988
    SystemGasTransports_DischargeTime = 989
    SystemGasTransports_MinVolume = 990
    SystemGasTransports_MaxVolume = 991
    SystemGasTransports_ShippingCharge = 992
    SystemGasTransports_BoiloffRate = 993
    SystemGasTransports_Imports = 994
    SystemGasTransports_Exports = 995
    SystemGasTransports_MaxShipments = 996
    SystemGasTransports_MaxShipmentsHour = 997
    SystemGasTransports_MaxShipmentsDay = 998
    SystemGasTransports_MaxShipmentsWeek = 999
    SystemGasTransports_MaxShipmentsMonth = 1000
    SystemGasTransports_MaxShipmentsYear = 1001
    SystemGasTransports_x = 1002
    SystemGasTransports_y = 1003
    SystemGasTransports_z = 1004
    SystemWaterPlants_ExpansionOptimality = 1005
    SystemWaterPlants_Units = 1006
    SystemWaterPlants_MaxCapacity = 1007
    SystemWaterPlants_MinStableProduction = 1008
    SystemWaterPlants_AuxFixed = 1009
    SystemWaterPlants_AuxBase = 1010
    SystemWaterPlants_AuxIncr = 1011
    SystemWaterPlants_HeatUsage = 1012
    SystemWaterPlants_WaterYield = 1013
    SystemWaterPlants_EnergyUsage = 1014
    SystemWaterPlants_VOMCharge = 1015
    SystemWaterPlants_FOMCharge = 1016
    SystemWaterPlants_MaxUnitsBuilt = 1017
    SystemWaterPlants_LeadTime = 1018
    SystemWaterPlants_ProjectStartDate = 1019
    SystemWaterPlants_TechnicalLife = 1020
    SystemWaterPlants_BuildCost = 1021
    SystemWaterPlants_WACC = 1022
    SystemWaterPlants_EconomicLife = 1023
    SystemWaterPlants_MinUnitsBuilt = 1024
    SystemWaterPlants_MaxUnitsBuiltinYear = 1025
    SystemWaterPlants_MinUnitsBuiltinYear = 1026
    SystemWaterPlants_MaxUnitsRetired = 1027
    SystemWaterPlants_RetirementCost = 1028
    SystemWaterPlants_MinUnitsRetired = 1029
    SystemWaterPlants_MaxUnitsRetiredinYear = 1030
    SystemWaterPlants_MinUnitsRetiredinYear = 1031
    SystemWaterPlants_x = 1032
    SystemWaterPlants_y = 1033
    SystemWaterPlants_z = 1034
    SystemWaterPipelines_RandomNumberSeed = 1035
    SystemWaterPipelines_RepairTimeDistribution = 1036
    SystemWaterPipelines_ExpansionOptimality = 1037
    SystemWaterPipelines_Units = 1038
    SystemWaterPipelines_MaxCapacity = 1039
    SystemWaterPipelines_Diameter = 1040
    SystemWaterPipelines_Roughness = 1041
    SystemWaterPipelines_Length = 1042
    SystemWaterPipelines_PumpEfficiency = 1043
    SystemWaterPipelines_VOMCharge = 1044
    SystemWaterPipelines_FOMCharge = 1045
    SystemWaterPipelines_ConsumptionAllocation = 1046
    SystemWaterPipelines_UnitsOut = 1047
    SystemWaterPipelines_MaintenanceRate = 1048
    SystemWaterPipelines_MaintenanceFrequency = 1049
    SystemWaterPipelines_ForcedOutageRate = 1050
    SystemWaterPipelines_OutageRating = 1051
    SystemWaterPipelines_MeanTimetoRepair = 1052
    SystemWaterPipelines_MinTimeToRepair = 1053
    SystemWaterPipelines_MaxTimeToRepair = 1054
    SystemWaterPipelines_RepairTimeShape = 1055
    SystemWaterPipelines_RepairTimeScale = 1056
    SystemWaterPipelines_MaxUnitsBuilt = 1057
    SystemWaterPipelines_LeadTime = 1058
    SystemWaterPipelines_ProjectStartDate = 1059
    SystemWaterPipelines_TechnicalLife = 1060
    SystemWaterPipelines_BuildCost = 1061
    SystemWaterPipelines_WACC = 1062
    SystemWaterPipelines_EconomicLife = 1063
    SystemWaterPipelines_MinUnitsBuilt = 1064
    SystemWaterPipelines_MaxUnitsBuiltinYear = 1065
    SystemWaterPipelines_MinUnitsBuiltinYear = 1066
    SystemWaterPipelines_MaxUnitsRetired = 1067
    SystemWaterPipelines_RetirementCost = 1068
    SystemWaterPipelines_MinUnitsRetired = 1069
    SystemWaterPipelines_MaxUnitsRetiredinYear = 1070
    SystemWaterPipelines_MinUnitsRetiredinYear = 1071
    SystemWaterPipelines_x = 1072
    SystemWaterPipelines_y = 1073
    SystemWaterPipelines_z = 1074
    SystemWaterNodes_ExpansionOptimality = 1075
    SystemWaterNodes_Units = 1076
    SystemWaterNodes_WaterSecurity = 1077
    SystemWaterNodes_FOMCharge = 1078
    SystemWaterNodes_MaxUnitsBuilt = 1079
    SystemWaterNodes_LeadTime = 1080
    SystemWaterNodes_ProjectStartDate = 1081
    SystemWaterNodes_TechnicalLife = 1082
    SystemWaterNodes_BuildCost = 1083
    SystemWaterNodes_WACC = 1084
    SystemWaterNodes_EconomicLife = 1085
    SystemWaterNodes_MinUnitsBuilt = 1086
    SystemWaterNodes_MaxUnitsBuiltinYear = 1087
    SystemWaterNodes_MinUnitsBuiltinYear = 1088
    SystemWaterNodes_MaxUnitsRetired = 1089
    SystemWaterNodes_RetirementCost = 1090
    SystemWaterNodes_MinUnitsRetired = 1091
    SystemWaterNodes_MaxUnitsRetiredinYear = 1092
    SystemWaterNodes_MinUnitsRetiredinYear = 1093
    SystemWaterNodes_x = 1094
    SystemWaterNodes_y = 1095
    SystemWaterNodes_z = 1096
    SystemWaterStorages_EnforceBounds = 1097
    SystemWaterStorages_ExpansionOptimality = 1098
    SystemWaterStorages_Units = 1099
    SystemWaterStorages_MaxVolume = 1100
    SystemWaterStorages_MinVolume = 1101
    SystemWaterStorages_InitialVolume = 1102
    SystemWaterStorages_Target = 1103
    SystemWaterStorages_TargetHour = 1104
    SystemWaterStorages_TargetDay = 1105
    SystemWaterStorages_TargetWeek = 1106
    SystemWaterStorages_TargetMonth = 1107
    SystemWaterStorages_TargetYear = 1108
    SystemWaterStorages_TargetPenalty = 1109
    SystemWaterStorages_EnergyUsage = 1110
    SystemWaterStorages_NaturalInflow = 1111
    SystemWaterStorages_LossRate = 1112
    SystemWaterStorages_FOMCharge = 1113
    SystemWaterStorages_MaxUnitsBuilt = 1114
    SystemWaterStorages_LeadTime = 1115
    SystemWaterStorages_ProjectStartDate = 1116
    SystemWaterStorages_TechnicalLife = 1117
    SystemWaterStorages_BuildCost = 1118
    SystemWaterStorages_WACC = 1119
    SystemWaterStorages_EconomicLife = 1120
    SystemWaterStorages_MinUnitsBuilt = 1121
    SystemWaterStorages_MaxUnitsBuiltinYear = 1122
    SystemWaterStorages_MinUnitsBuiltinYear = 1123
    SystemWaterStorages_MaxUnitsRetired = 1124
    SystemWaterStorages_RetirementCost = 1125
    SystemWaterStorages_MinUnitsRetired = 1126
    SystemWaterStorages_MaxUnitsRetiredinYear = 1127
    SystemWaterStorages_MinUnitsRetiredinYear = 1128
    SystemWaterStorages_TrajectoryNonanticipativity = 1129
    SystemWaterStorages_TrajectoryNonanticipativityVolume = 1130
    SystemWaterStorages_TrajectoryNonanticipativityTime = 1131
    SystemWaterStorages_x = 1132
    SystemWaterStorages_y = 1133
    SystemWaterStorages_z = 1134
    SystemWaterDemands_Demand = 1135
    SystemWaterDemands_ShortagePrice = 1136
    SystemWaterDemands_ExcessPrice = 1137
    SystemWaterDemands_BidQuantity = 1138
    SystemWaterDemands_BidPrice = 1139
    SystemWaterDemands_x = 1140
    SystemWaterDemands_y = 1141
    SystemWaterDemands_z = 1142
    SystemWaterZones_x = 1143
    SystemWaterZones_y = 1144
    SystemWaterZones_z = 1145
    SystemRegions_GeneratorSettlementModel = 1146
    SystemRegions_LoadSettlementModel = 1147
    SystemRegions_UniformPricingPumpedStoragePriceSetting = 1148
    SystemRegions_UniformPricingRelaxTransmissionLimits = 1149
    SystemRegions_UniformPricingRelaxGenericConstraints = 1150
    SystemRegions_UniformPricingRelaxGeneratorConstraints = 1151
    SystemRegions_UniformPricingRelaxAncillaryServices = 1152
    SystemRegions_UpliftEnabled = 1153
    SystemRegions_UpliftCostBasis = 1154
    SystemRegions_UpliftCompatibility = 1155
    SystemRegions_UpliftAlpha = 1156
    SystemRegions_UpliftBeta = 1157
    SystemRegions_UpliftDelta = 1158
    SystemRegions_UpliftIncludeStartCost = 1159
    SystemRegions_UpliftIncludeNoLoadCost = 1160
    SystemRegions_UpliftDetectActiveMinStableLevelConstraints = 1161
    SystemRegions_UpliftDetectActiveRampConstraints = 1162
    SystemRegions_IncludeinMarginalUnit = 1163
    SystemRegions_IncludeinUplift = 1164
    SystemRegions_ConstraintPaymentsEnabled = 1165
    SystemRegions_ConstraintPaymentsCompatibility = 1166
    SystemRegions_LoadMeteringPoint = 1167
    SystemRegions_LoadIncludesLosses = 1168
    SystemRegions_AggregateTransmission = 1169
    SystemRegions_PoolType = 1170
    SystemRegions_MLFAdjustsOfferPrice = 1171
    SystemRegions_MLFAdjustsBidPrice = 1172
    SystemRegions_MLFAdjustsNoLoadCost = 1173
    SystemRegions_MLFAdjustsStartCost = 1174
    SystemRegions_IncludeinRegionSupply = 1175
    SystemRegions_TransmissionConstraintsEnabled = 1176
    SystemRegions_TransmissionConstraintVoltageThreshold = 1177
    SystemRegions_TransmissionInterfaceConstraintsEnabled = 1178
    SystemRegions_EnforceTransmissionLimitsOnLinesInInterfaces = 1179
    SystemRegions_TransmissionReportEnabled = 1180
    SystemRegions_TransmissionReportVoltageThreshold = 1181
    SystemRegions_TransmissionReportLinesInInterfaces = 1182
    SystemRegions_TransmissionReportInjectionandLoadNodes = 1183
    SystemRegions_ReportObjectsinRegion = 1184
    SystemRegions_WheelingMethod = 1185
    SystemRegions_Units = 1186
    SystemRegions_Load = 1187
    SystemRegions_LoadScalar = 1188
    SystemRegions_FixedLoad = 1189
    SystemRegions_FixedGeneration = 1190
    SystemRegions_VoLL = 1191
    SystemRegions_PriceofDumpEnergy = 1192
    SystemRegions_PriceCap = 1193
    SystemRegions_PriceFloor = 1194
    SystemRegions_Price = 1195
    SystemRegions_WheelingCharge = 1196
    SystemRegions_FixedCostScalar = 1197
    SystemRegions_Elasticity = 1198
    SystemRegions_ReferenceLoad = 1199
    SystemRegions_DSPBidQuantity = 1200
    SystemRegions_DSPBidPrice = 1201
    SystemRegions_IsStrategic = 1202
    SystemRegions_MaxMaintenance = 1203
    SystemRegions_MaintenanceFactor = 1204
    SystemRegions_PeakPeriod = 1205
    SystemRegions_FirmCapacityIncr = 1206
    SystemRegions_MinCapacityReserves = 1207
    SystemRegions_MaxCapacityReserves = 1208
    SystemRegions_MinCapacityReserveMargin = 1209
    SystemRegions_MaxCapacityReserveMargin = 1210
    SystemRegions_MinNativeCapacityReserves = 1211
    SystemRegions_MinNativeCapacityReserveMargin = 1212
    SystemRegions_CapacityShortagePrice = 1213
    SystemRegions_CapacityExcessPrice = 1214
    SystemRegions_CapacityPriceCap = 1215
    SystemRegions_CapacityPriceFloor = 1216
    SystemRegions_LOLPTarget = 1217
    SystemRegions_x = 1218
    SystemRegions_y = 1219
    SystemRegions_z = 1220
    SystemZones_LoadSettlementModel = 1221
    SystemZones_WheelingMethod = 1222
    SystemZones_Units = 1223
    SystemZones_Load = 1224
    SystemZones_LoadParticipationFactor = 1225
    SystemZones_LoadScalar = 1226
    SystemZones_WheelingCharge = 1227
    SystemZones_MaxMaintenance = 1228
    SystemZones_MaintenanceFactor = 1229
    SystemZones_PeakPeriod = 1230
    SystemZones_FirmCapacityIncr = 1231
    SystemZones_MinCapacityReserves = 1232
    SystemZones_MaxCapacityReserves = 1233
    SystemZones_MinCapacityReserveMargin = 1234
    SystemZones_MaxCapacityReserveMargin = 1235
    SystemZones_MinNativeCapacityReserves = 1236
    SystemZones_MinNativeCapacityReserveMargin = 1237
    SystemZones_CapacityShortagePrice = 1238
    SystemZones_CapacityExcessPrice = 1239
    SystemZones_CapacityPriceCap = 1240
    SystemZones_CapacityPriceFloor = 1241
    SystemZones_LOLPTarget = 1242
    SystemZones_x = 1243
    SystemZones_y = 1244
    SystemZones_z = 1245
    SystemNodes_MustReport = 1246
    SystemNodes_IsSlackBus = 1247
    SystemNodes_AllowDumpEnergy = 1248
    SystemNodes_AllowUnservedEnergy = 1249
    SystemNodes_ReferenceLoad = 1250
    SystemNodes_Voltage = 1251
    SystemNodes_Units = 1252
    SystemNodes_LoadParticipationFactor = 1253
    SystemNodes_Load = 1254
    SystemNodes_FixedLoad = 1255
    SystemNodes_FixedGeneration = 1256
    SystemNodes_MaxNetInjection = 1257
    SystemNodes_MaxNetOfftake = 1258
    SystemNodes_Rating = 1259
    SystemNodes_DSPBidQuantity = 1260
    SystemNodes_DSPBidRatio = 1261
    SystemNodes_DSPBidPrice = 1262
    SystemNodes_Price = 1263
    SystemNodes_MaxMaintenance = 1264
    SystemNodes_MaintenanceFactor = 1265
    SystemNodes_MinCapacityReserves = 1266
    SystemNodes_MinCapacityReserveMargin = 1267
    SystemNodes_x = 1268
    SystemNodes_y = 1269
    SystemNodes_z = 1270
    SystemLines_MustReport = 1271
    SystemLines_RandomNumberSeed = 1272
    SystemLines_RepairTimeDistribution = 1273
    SystemLines_EnforceLimits = 1274
    SystemLines_FormulateUpfront = 1275
    SystemLines_FormulateNPLUpfront = 1276
    SystemLines_MaxLossTranches = 1277
    SystemLines_PriceSetting = 1278
    SystemLines_OfferQuantityFormat = 1279
    SystemLines_FixedFlowMethod = 1280
    SystemLines_ExpansionOptimality = 1281
    SystemLines_Units = 1282
    SystemLines_MaxFlow = 1283
    SystemLines_MinFlow = 1284
    SystemLines_MaxRating = 1285
    SystemLines_MinRating = 1286
    SystemLines_OverloadMaxRating = 1287
    SystemLines_OverloadMinRating = 1288
    SystemLines_LimitPenalty = 1289
    SystemLines_Resistance = 1290
    SystemLines_Reactance = 1291
    SystemLines_Susceptance = 1292
    SystemLines_MaxRampUp = 1293
    SystemLines_MaxRampDown = 1294
    SystemLines_RampPenalty = 1295
    SystemLines_LossBase = 1296
    SystemLines_LossIncr = 1297
    SystemLines_LossIncr2 = 1298
    SystemLines_LossBaseBack = 1299
    SystemLines_LossIncrBack = 1300
    SystemLines_LossIncr2Back = 1301
    SystemLines_LossAllocation = 1302
    SystemLines_FixedFlow = 1303
    SystemLines_FixedFlowPenalty = 1304
    SystemLines_FixedLoss = 1305
    SystemLines_WheelingCharge = 1306
    SystemLines_WheelingChargeBack = 1307
    SystemLines_OfferBase = 1308
    SystemLines_OfferQuantity = 1309
    SystemLines_OfferPrice = 1310
    SystemLines_OfferQuantityBack = 1311
    SystemLines_OfferPriceBack = 1312
    SystemLines_MarginalLossFactor = 1313
    SystemLines_MarginalLossFactorBack = 1314
    SystemLines_FlowNonanticipativity = 1315
    SystemLines_FlowNonanticipativityTime = 1316
    SystemLines_FixedCharge = 1317
    SystemLines_FOMCharge = 1318
    SystemLines_EquityCharge = 1319
    SystemLines_DebtCharge = 1320
    SystemLines_Circuits = 1321
    SystemLines_UnitsOut = 1322
    SystemLines_MaintenanceRate = 1323
    SystemLines_MaintenanceFrequency = 1324
    SystemLines_ForcedOutageRate = 1325
    SystemLines_OutageMaxRating = 1326
    SystemLines_OutageMinRating = 1327
    SystemLines_MeanTimetoRepair = 1328
    SystemLines_MinTimeToRepair = 1329
    SystemLines_MaxTimeToRepair = 1330
    SystemLines_RepairTimeShape = 1331
    SystemLines_RepairTimeScale = 1332
    SystemLines_MaxCapacityReserves = 1333
    SystemLines_MinCapacityReserves = 1334
    SystemLines_FirmCapacity = 1335
    SystemLines_Type = 1336
    SystemLines_BuildCost = 1337
    SystemLines_RetirementCost = 1338
    SystemLines_LeadTime = 1339
    SystemLines_ProjectStartDate = 1340
    SystemLines_CommissionDate = 1341
    SystemLines_TechnicalLife = 1342
    SystemLines_WACC = 1343
    SystemLines_EconomicLife = 1344
    SystemLines_MaxUnitsBuilt = 1345
    SystemLines_MaxUnitsRetired = 1346
    SystemLines_MinUnitsBuilt = 1347
    SystemLines_MinUnitsRetired = 1348
    SystemLines_MaxUnitsBuiltinYear = 1349
    SystemLines_MaxUnitsRetiredinYear = 1350
    SystemLines_MinUnitsBuiltinYear = 1351
    SystemLines_MinUnitsRetiredinYear = 1352
    SystemLines_BuildNonanticipativity = 1353
    SystemLines_RetireNonanticipativity = 1354
    SystemLines_x = 1355
    SystemLines_y = 1356
    SystemLines_z = 1357
    SystemMLFs_Intercept = 1358
    SystemMLFs_FlowCoefficient = 1359
    SystemTransformers_MustReport = 1360
    SystemTransformers_EnforceLimits = 1361
    SystemTransformers_FormulateUpfront = 1362
    SystemTransformers_Units = 1363
    SystemTransformers_Rating = 1364
    SystemTransformers_OverloadRating = 1365
    SystemTransformers_LimitPenalty = 1366
    SystemTransformers_Resistance = 1367
    SystemTransformers_Reactance = 1368
    SystemTransformers_Susceptance = 1369
    SystemTransformers_LossAllocation = 1370
    SystemTransformers_FixedLoss = 1371
    SystemTransformers_UnitsOut = 1372
    SystemTransformers_x = 1373
    SystemTransformers_y = 1374
    SystemTransformers_z = 1375
    SystemFlowControls_PriceSetting = 1376
    SystemFlowControls_ExpansionOptimality = 1377
    SystemFlowControls_Type = 1378
    SystemFlowControls_Units = 1379
    SystemFlowControls_MinAngle = 1380
    SystemFlowControls_MaxAngle = 1381
    SystemFlowControls_MinImpedance = 1382
    SystemFlowControls_MaxImpedance = 1383
    SystemFlowControls_MinVoltage = 1384
    SystemFlowControls_MaxVoltage = 1385
    SystemFlowControls_Penalty = 1386
    SystemFlowControls_Angle = 1387
    SystemFlowControls_AnglePoints = 1388
    SystemFlowControls_FlowLoadingPoints = 1389
    SystemFlowControls_FOMCharge = 1390
    SystemFlowControls_BuildCost = 1391
    SystemFlowControls_LeadTime = 1392
    SystemFlowControls_ProjectStartDate = 1393
    SystemFlowControls_CommissionDate = 1394
    SystemFlowControls_TechnicalLife = 1395
    SystemFlowControls_WACC = 1396
    SystemFlowControls_EconomicLife = 1397
    SystemFlowControls_MaxUnitsBuilt = 1398
    SystemFlowControls_MinUnitsBuilt = 1399
    SystemFlowControls_MaxUnitsBuiltinYear = 1400
    SystemFlowControls_MinUnitsBuiltinYear = 1401
    SystemFlowControls_BuildNonanticipativity = 1402
    SystemFlowControls_x = 1403
    SystemFlowControls_y = 1404
    SystemFlowControls_z = 1405
    SystemInterfaces_FormulateUpfront = 1406
    SystemInterfaces_OfferQuantityFormat = 1407
    SystemInterfaces_Units = 1408
    SystemInterfaces_MinFlow = 1409
    SystemInterfaces_MaxFlow = 1410
    SystemInterfaces_OverloadMaxRating = 1411
    SystemInterfaces_OverloadMinRating = 1412
    SystemInterfaces_LimitPenalty = 1413
    SystemInterfaces_MaxRampUp = 1414
    SystemInterfaces_MaxRampDown = 1415
    SystemInterfaces_RampPenalty = 1416
    SystemInterfaces_FixedFlow = 1417
    SystemInterfaces_FixedFlowPenalty = 1418
    SystemInterfaces_OfferBase = 1419
    SystemInterfaces_OfferQuantity = 1420
    SystemInterfaces_OfferPrice = 1421
    SystemInterfaces_OfferQuantityBack = 1422
    SystemInterfaces_OfferPriceBack = 1423
    SystemInterfaces_FlowNonanticipativity = 1424
    SystemInterfaces_FlowNonanticipativityTime = 1425
    SystemInterfaces_FirmCapacity = 1426
    SystemInterfaces_ExpansionCost = 1427
    SystemInterfaces_MaxExpansion = 1428
    SystemInterfaces_WACC = 1429
    SystemInterfaces_EconomicLife = 1430
    SystemInterfaces_BuildNonanticipativity = 1431
    SystemInterfaces_x = 1432
    SystemInterfaces_y = 1433
    SystemInterfaces_z = 1434
    SystemContingencies_IsEnabled = 1435
    SystemContingencies_MonitoringThreshold = 1436
    SystemContingencies_x = 1437
    SystemContingencies_y = 1438
    SystemContingencies_z = 1439
    SystemCompanies_Strategic = 1440
    SystemCompanies_MarkupBias = 1441
    SystemCompanies_FormulateRisk = 1442
    SystemCompanies_RiskLevel = 1443
    SystemCompanies_AcceptableRisk = 1444
    SystemCompanies_MaxMaintenance = 1445
    SystemCompanies_MinMaintenance = 1446
    SystemCompanies_MaxMaintenanceFactor = 1447
    SystemCompanies_MinMaintenanceFactor = 1448
    SystemCompanies_x = 1449
    SystemCompanies_y = 1450
    SystemCompanies_z = 1451
    SystemFinancialContracts_IsPhysical = 1452
    SystemFinancialContracts_Quantity = 1453
    SystemFinancialContracts_FloorPrice = 1454
    SystemFinancialContracts_CapPrice = 1455
    SystemHubs_PricingMethod = 1456
    SystemHubs_Units = 1457
    SystemHubs_x = 1458
    SystemHubs_y = 1459
    SystemHubs_z = 1460
    SystemTransmissionRights_Type = 1461
    SystemTransmissionRights_SettlementModel = 1462
    SystemTransmissionRights_PricingMethod = 1463
    SystemTransmissionRights_Units = 1464
    SystemTransmissionRights_Quantity = 1465
    SystemTransmissionRights_RentalShare = 1466
    SystemTransmissionRights_RentalBackShare = 1467
    SystemTransmissionRights_Price = 1468
    SystemCournots_DemandIntercept = 1469
    SystemCournots_DemandSlope = 1470
    SystemRSIs_AllowNegativeMarkups = 1471
    SystemRSIs_RSI = 1472
    SystemRSIs_LernerIndex = 1473
    SystemRSIs_BoundedLernerIndex = 1474
    SystemRSIs_Intercept = 1475
    SystemRSIs_RSICoefficient = 1476
    SystemRSIs_RSIsquaredCoefficient = 1477
    SystemRSIs_LoadUnhedgedCoefficient = 1478
    SystemRSIs_RSIInverseCoefficient = 1479
    SystemRSIs_LoadCoefficient = 1480
    SystemRSIs_LoadCapacityRatioCoefficient = 1481
    SystemRSIs_CapacityFactorCoefficient = 1482
    SystemRSIs_LoadVariationCoefficient = 1483
    SystemRSIs_SummerPeriodCoefficient = 1484
    SystemRSIs_PeakPeriodCoefficient = 1485
    SystemRSIs_AverageLoad = 1486
    SystemRSIs_LernerIndextstatistic = 1487
    SystemRSIs_LernerIndexStdDev = 1488
    SystemRSIs_LernerIndexCalibrationFactor = 1489
    SystemRSIs_MinLernerIndex = 1490
    SystemRSIs_MaxLernerIndex = 1491
    SystemMarkets_IsForward = 1492
    SystemMarkets_IsMarginal = 1493
    SystemMarkets_DemandCurve = 1494
    SystemMarkets_PriceSetting = 1495
    SystemMarkets_SupplySettlementModel = 1496
    SystemMarkets_DemandSettlementModel = 1497
    SystemMarkets_Units = 1498
    SystemMarkets_Price = 1499
    SystemMarkets_PriceScalar = 1500
    SystemMarkets_PriceIncr = 1501
    SystemMarkets_Quantity = 1502
    SystemMarkets_BaseQuantity = 1503
    SystemMarkets_SellUnit = 1504
    SystemMarkets_SellBlock = 1505
    SystemMarkets_SellBlockHour = 1506
    SystemMarkets_SellBlockDay = 1507
    SystemMarkets_SellBlockWeek = 1508
    SystemMarkets_SellBlockMonth = 1509
    SystemMarkets_SellBlockYear = 1510
    SystemMarkets_SellBlockFixedCharge = 1511
    SystemMarkets_BuyUnit = 1512
    SystemMarkets_BuyBlock = 1513
    SystemMarkets_BuyBlockHour = 1514
    SystemMarkets_BuyBlockDay = 1515
    SystemMarkets_BuyBlockWeek = 1516
    SystemMarkets_BuyBlockMonth = 1517
    SystemMarkets_BuyBlockYear = 1518
    SystemMarkets_BuyBlockFixedCharge = 1519
    SystemMarkets_MinSales = 1520
    SystemMarkets_MaxSales = 1521
    SystemMarkets_MinPurchases = 1522
    SystemMarkets_MaxPurchases = 1523
    SystemMarkets_BidAskSpread = 1524
    SystemMarkets_BidSpread = 1525
    SystemMarkets_AskSpread = 1526
    SystemMarkets_FirmCapacity = 1527
    SystemMarkets_LoadObligation = 1528
    SystemMarkets_x = 1529
    SystemMarkets_y = 1530
    SystemMarkets_z = 1531
    SystemConstraints_Sense = 1532
    SystemConstraints_LHSType = 1533
    SystemConstraints_FormulateUpfront = 1534
    SystemConstraints_ConditionLogic = 1535
    SystemConstraints_IncludeinLTPlan = 1536
    SystemConstraints_IncludeinPASA = 1537
    SystemConstraints_IncludeinMTSchedule = 1538
    SystemConstraints_IncludeinSTSchedule = 1539
    SystemConstraints_IncludeinUniformPricing = 1540
    SystemConstraints_DecompositionMethod = 1541
    SystemConstraints_FeasibilityRepairWeight = 1542
    SystemConstraints_WildcardMode = 1543
    SystemConstraints_RHS = 1544
    SystemConstraints_RHSHour = 1545
    SystemConstraints_RHSDay = 1546
    SystemConstraints_RHSWeek = 1547
    SystemConstraints_RHSMonth = 1548
    SystemConstraints_RHSYear = 1549
    SystemConstraints_RHSCustom = 1550
    SystemConstraints_PenaltyQuantity = 1551
    SystemConstraints_PenaltyPrice = 1552
    SystemConstraints_MinRHS = 1553
    SystemConstraints_MaxRHS = 1554
    SystemConstraints_x = 1555
    SystemConstraints_y = 1556
    SystemConstraints_z = 1557
    SystemDecisionVariables_IncludeinLTPlan = 1558
    SystemDecisionVariables_IncludeinPASA = 1559
    SystemDecisionVariables_IncludeinMTSchedule = 1560
    SystemDecisionVariables_IncludeinSTSchedule = 1561
    SystemDecisionVariables_ObjectiveFunctionCoefficient = 1562
    SystemDecisionVariables_ObjectiveFunctionCoefficientHour = 1563
    SystemDecisionVariables_ObjectiveFunctionCoefficientDay = 1564
    SystemDecisionVariables_ObjectiveFunctionCoefficientWeek = 1565
    SystemDecisionVariables_ObjectiveFunctionCoefficientMonth = 1566
    SystemDecisionVariables_ObjectiveFunctionCoefficientYear = 1567
    SystemDecisionVariables_LowerBound = 1568
    SystemDecisionVariables_UpperBound = 1569
    SystemDecisionVariables_Nonanticipativity = 1570
    SystemDecisionVariables_NonanticipativityTime = 1571
    SystemDecisionVariables_x = 1572
    SystemDecisionVariables_y = 1573
    SystemDecisionVariables_z = 1574
    SystemDataFiles_Filename = 1575
    SystemDataFiles_BaseProfile = 1576
    SystemDataFiles_Energy = 1577
    SystemDataFiles_Maximum = 1578
    SystemDataFiles_Minimum = 1579
    SystemDataFiles_Holiday = 1580
    SystemDataFiles_MinValue = 1581
    SystemDataFiles_MaxValue = 1582
    SystemVariables_RandomNumberSeed = 1583
    SystemVariables_SamplingMethod = 1584
    SystemVariables_SamplingFrequency = 1585
    SystemVariables_SamplingPeriodType = 1586
    SystemVariables_DistributionType = 1587
    SystemVariables_Condition = 1588
    SystemVariables_ConditionLogic = 1589
    SystemVariables_IncludeinLTPlan = 1590
    SystemVariables_IncludeinPASA = 1591
    SystemVariables_IncludeinMTSchedule = 1592
    SystemVariables_IncludeinSTSchedule = 1593
    SystemVariables_Profile = 1594
    SystemVariables_ProfileHour = 1595
    SystemVariables_ProfileDay = 1596
    SystemVariables_ProfileWeek = 1597
    SystemVariables_ProfileMonth = 1598
    SystemVariables_ProfileYear = 1599
    SystemVariables_MinValue = 1600
    SystemVariables_MaxValue = 1601
    SystemVariables_Probability = 1602
    SystemVariables_ErrorStdDev = 1603
    SystemVariables_AbsErrorStdDev = 1604
    SystemVariables_MinValueStdDev = 1605
    SystemVariables_MaxValueStdDev = 1606
    SystemVariables_AutoCorrelation = 1607
    SystemVariables_MeanReversion = 1608
    SystemVariables_ARIMAalpha = 1609
    SystemVariables_ARIMAbeta = 1610
    SystemVariables_ARIMAd = 1611
    SystemVariables_JumpFrequency = 1612
    SystemVariables_JumpMagnitude = 1613
    SystemVariables_JumpErrorStdDev = 1614
    SystemVariables_GARCHalpha = 1615
    SystemVariables_GARCHbeta = 1616
    SystemVariables_GARCHomega = 1617
    SystemVariables_Lookupx = 1618
    SystemVariables_Lookupy = 1619
    SystemVariables_LookupUnit = 1620
    SystemVariables_Sampling = 1621
    SystemVariables_StepHourActiveFrom = 1622
    SystemVariables_StepHoursActive = 1623
    SystemVariables_CompoundIndex = 1624
    SystemVariables_CompoundIndexHour = 1625
    SystemVariables_CompoundIndexDay = 1626
    SystemVariables_CompoundIndexWeek = 1627
    SystemVariables_CompoundIndexMonth = 1628
    SystemVariables_CompoundIndexYear = 1629
    SystemTimeslices_Include = 1630
    SystemGlobals_FCFConstant = 1631
    SystemGlobals_SampleWeight = 1632
    SystemGlobals_TreeStageCount = 1633
    SystemGlobals_TreePeriodType = 1634
    SystemGlobals_TreePositionExpFactor = 1635
    SystemGlobals_TreeLeavesExpFactor = 1636
    SystemGlobals_TreeStagesPosition = 1637
    SystemGlobals_TreeStagesLeaves = 1638
    SystemGlobals_TreeStagesHangingBranches = 1639
    SystemGlobals_DeterministicStages = 1640
    SystemGlobals_HangingBranchesHistoricalYearStart = 1641
    SystemGlobals_HangingBranchesWeight = 1642
    SystemGlobals_HangingBranchesBlockCount = 1643
    SystemGlobals_SlicingBlock = 1644
    GeneratorCompanies_Share = 1645
    GeneratorNodes_GenerationParticipationFactor = 1646
    GeneratorNodes_LoadParticipationFactor = 1647
    GeneratorFuels_TransportCharge = 1648
    GeneratorFuels_MutuallyExclusive = 1649
    GeneratorFuels_Ratio = 1650
    GeneratorFuels_MinRatio = 1651
    GeneratorFuels_MaxRatio = 1652
    GeneratorFuels_MaxInput = 1653
    GeneratorFuels_Rating = 1654
    GeneratorFuels_IsAvailable = 1655
    GeneratorFuels_HeatRateScalar = 1656
    GeneratorFuels_HeatRateBase = 1657
    GeneratorFuels_HeatRate = 1658
    GeneratorFuels_HeatRateIncr = 1659
    GeneratorFuels_HeatRateIncr2 = 1660
    GeneratorFuels_HeatRateIncr3 = 1661
    GeneratorFuels_TransitionCostDown = 1662
    GeneratorFuels_TransitionCostUp = 1663
    GeneratorFuels_DecouplingTime = 1664
    GeneratorFuels_CouplingTime = 1665
    GeneratorFuels_EmissionScalar = 1666
    GeneratorFuels_OfferQuantity = 1667
    GeneratorFuels_OfferPrice = 1668
    GeneratorStartFuels_OfftakeatStart = 1669
    GeneratorStartFuels_TransportCharge = 1670
    GeneratorStartFuels_EmissionScalar = 1671
    GeneratorHeadStorage_FlowFactor = 1672
    GeneratorHeadStorage_FlowatStart = 1673
    GeneratorHeadStorage_EfficiencyPoint = 1674
    GeneratorHeadStorage_EfficiencyScalar = 1675
    GeneratorTailStorage_FlowFactor = 1676
    GeneratorTransition_TransitionCost = 1677
    FuelCompanies_Share = 1678
    EmissionFuels_ProductionRate = 1679
    EmissionGenerators_ProductionRate = 1680
    EmissionGenerators_RemovalRate = 1681
    EmissionGenerators_RemovalCost = 1682
    EmissionGenerators_ProductionatStart = 1683
    EmissionGenerators_ShadowPriceScalar = 1684
    EmissionGenerators_PriceScalar = 1685
    EmissionGenerators_Allocation = 1686
    EmissionGenerators_AllocationHour = 1687
    EmissionGenerators_AllocationDay = 1688
    EmissionGenerators_AllocationWeek = 1689
    EmissionGenerators_AllocationMonth = 1690
    EmissionGenerators_AllocationYear = 1691
    EmissionGasNodes_ProductionRate = 1692
    EmissionGasPlants_ProductionRate = 1693
    EmissionWaterPlants_ProductionRate = 1694
    AbatementGenerators_GenerationParticipationFactor = 1695
    AbatementEmissions_AbatementCost = 1696
    AbatementEmissions_Efficiency = 1697
    AbatementEmissions_MaxAbatement = 1698
    AbatementConsumables_ConsumptionBase = 1699
    AbatementConsumables_ConsumptionIncr = 1700
    PowerStationNodes_GenerationParticipationFactor = 1701
    FuelContractCompanies_Share = 1702
    PhysicalContractCompanies_Share = 1703
    PurchaserCompanies_Share = 1704
    PurchaserNodes_LoadParticipationFactor = 1705
    ReserveRegions_LoadRisk = 1706
    ReserveRegions_LOLPTarget = 1707
    ReserveGenerators_InitialPumpLoadRaiseProvision = 1708
    ReserveGenerators_InitialRaiseProvision = 1709
    ReserveGenerators_MaxResponse = 1710
    ReserveGenerators_MaxSyncCondResponse = 1711
    ReserveGenerators_MaxPumpResponse = 1712
    ReserveGenerators_MaxReplacement = 1713
    ReserveGenerators_MaxResponseFactor = 1714
    ReserveGenerators_MaxSyncCondResponseFactor = 1715
    ReserveGenerators_MaxPumpResponseFactor = 1716
    ReserveGenerators_MaxReplacementFactor = 1717
    ReserveGenerators_MinProvision = 1718
    ReserveGenerators_MinSpinningProvision = 1719
    ReserveGenerators_MinRegulationProvision = 1720
    ReserveGenerators_MinReplacementProvision = 1721
    ReserveGenerators_Effectiveness = 1722
    ReserveGenerators_ResponseRatio = 1723
    ReserveGenerators_OfferQuantity = 1724
    ReserveGenerators_OfferPrice = 1725
    ReserveGenerators_SyncCondOfferPrice = 1726
    ReserveGenerators_PumpOfferPrice = 1727
    ReserveGenerators_ReplacementOfferQuantity = 1728
    ReserveGenerators_ReplacementOfferPrice = 1729
    ReservePurchasers_OfferQuantity = 1730
    ReservePurchasers_OfferPrice = 1731
    ReserveBatteries_OfferQuantity = 1732
    ReserveBatteries_OfferPrice = 1733
    ReserveLineContingencies_FlowForwardCoefficient = 1734
    ReserveLineContingencies_FlowBackCoefficient = 1735
    MaintenanceGenerators_OutageRating = 1736
    MaintenanceGenerators_OutageRatingFactor = 1737
    MaintenanceGenerators_OutageFirmCapacity = 1738
    MaintenanceGenerators_OutageFirmCapacityFactor = 1739
    MaintenanceGasPipelines_OutageMaxFlow = 1740
    MaintenanceGasPipelines_OutageMaxFlowBack = 1741
    MaintenanceLines_OutageMaxRating = 1742
    MaintenanceLines_OutageMinRating = 1743
    GeneratorHeatOutputNodes_ParticipationFactor = 1744
    HeatPlantFuels_MutuallyExclusive = 1745
    HeatPlantFuels_Ratio = 1746
    HeatPlantFuels_MinRatio = 1747
    HeatPlantFuels_MaxRatio = 1748
    HeatPlantFuels_MaxInput = 1749
    HeatPlantFuels_IsAvailable = 1750
    HeatPlantFuels_HeatRateScalar = 1751
    HeatPlantFuels_HeatRateBase = 1752
    HeatPlantFuels_HeatRate = 1753
    HeatPlantFuels_HeatRateIncr = 1754
    HeatPlantHeatOutputNodes_ParticipationFactor = 1755
    HeatPlantStartFuels_OfftakeatStart = 1756
    HeatNodeHeatExportNodes_ParticipationFactor = 1757
    HeatNodeWaterPlants_ParticipationFactor = 1758
    MarketCompanies_Share = 1759
    MarketHeatGenerators_ConversionRate = 1760
    MarketCapacityGenerators_OfferQuantity = 1761
    MarketCapacityGenerators_OfferPrice = 1762
    GasFieldCompanies_Share = 1763
    GasDemandGasNodes_DemandParticipationFactor = 1764
    RegionRegions_WheelingCharge = 1765
    RegionRegions_MaxFlow = 1766
    ZoneZones_WheelingCharge = 1767
    ZoneZones_MaxFlow = 1768
    NodeHubs_PricingWeight = 1769
    LineCompanies_Share = 1770
    MLFRegions_LoadCoefficient = 1771
    InterfaceLines_FlowCoefficient = 1772
    InterfaceLines_FlowForwardCoefficient = 1773
    InterfaceLines_FlowBackCoefficient = 1774
    InterfaceTransformers_FlowCoefficient = 1775
    CompanyRegions_LoadParticipationFactor = 1776
    CompanyEmissions_Allocation = 1777
    CompanyEmissions_AllocationHour = 1778
    CompanyEmissions_AllocationDay = 1779
    CompanyEmissions_AllocationWeek = 1780
    CompanyEmissions_AllocationMonth = 1781
    CompanyEmissions_AllocationYear = 1782
    FinancialContractGeneratingCompanies_Share = 1783
    FinancialContractPurchasingCompanies_Share = 1784
    FinancialContractRegion_LoadParticipationFactor = 1785
    FinancialContractGenerators_GenerationParticipationFactor = 1786
    TransmissionRightCompanies_Share = 1787
    GasDemandCompanies_Share = 1788
    ConstraintGenerators_GenerationCoefficient = 1789
    ConstraintGenerators_GenerationSquaredCoefficient = 1790
    ConstraintGenerators_GenerationSUMSquaredCoefficient = 1791
    ConstraintGenerators_GenerationSentOutCoefficient = 1792
    ConstraintGenerators_CapacityFactorCoefficient = 1793
    ConstraintGenerators_OperatingHoursCoefficient = 1794
    ConstraintGenerators_UnitsGeneratingCoefficient = 1795
    ConstraintGenerators_UnitsStartedCoefficient = 1796
    ConstraintGenerators_UnitsShutdownCoefficient = 1797
    ConstraintGenerators_HoursDownCoefficient = 1798
    ConstraintGenerators_AvailableCapacityCoefficient = 1799
    ConstraintGenerators_CommittedCapacityCoefficient = 1800
    ConstraintGenerators_FuelOfftakeCoefficient = 1801
    ConstraintGenerators_WasteHeatCoefficient = 1802
    ConstraintGenerators_EmissionCoefficient = 1803
    ConstraintGenerators_HeatProductionCoefficient = 1804
    ConstraintGenerators_PumpLoadCoefficient = 1805
    ConstraintGenerators_PumpOperatingHoursCoefficient = 1806
    ConstraintGenerators_UnitsPumpingCoefficient = 1807
    ConstraintGenerators_PumpUnitsStartedCoefficient = 1808
    ConstraintGenerators_SyncCondLoadCoefficient = 1809
    ConstraintGenerators_UnitsSyncCondCoefficient = 1810
    ConstraintGenerators_SyncCondOperatingHoursCoefficient = 1811
    ConstraintGenerators_RampCoefficient = 1812
    ConstraintGenerators_RampUpCoefficient = 1813
    ConstraintGenerators_RampDownCoefficient = 1814
    ConstraintGenerators_RampUpViolationCoefficient = 1815
    ConstraintGenerators_RampDownViolationCoefficient = 1816
    ConstraintGenerators_ReserveProvisionCoefficient = 1817
    ConstraintGenerators_SpinningReserveCoefficient = 1818
    ConstraintGenerators_SyncCondReserveCoefficient = 1819
    ConstraintGenerators_PumpDispatchableLoadCoefficient = 1820
    ConstraintGenerators_RaiseReserveProvisionCoefficient = 1821
    ConstraintGenerators_LowerReserveProvisionCoefficient = 1822
    ConstraintGenerators_RegulationRaiseReserveProvisionCoefficient = 1823
    ConstraintGenerators_RegulationLowerReserveProvisionCoefficient = 1824
    ConstraintGenerators_ReplacementReserveProvisionCoefficient = 1825
    ConstraintGenerators_ReserveUnitsCoefficient = 1826
    ConstraintGenerators_OperatingReserveUnitsCoefficient = 1827
    ConstraintGenerators_FlexibilityUpCoefficient = 1828
    ConstraintGenerators_FlexibilityDownCoefficient = 1829
    ConstraintGenerators_RampFlexibilityUpCoefficient = 1830
    ConstraintGenerators_RampFlexibilityDownCoefficient = 1831
    ConstraintGenerators_WithdrawalCoefficient = 1832
    ConstraintGenerators_InjectionCoefficient = 1833
    ConstraintGenerators_WaterOfftakeCoefficient = 1834
    ConstraintGenerators_WaterConsumptionCoefficient = 1835
    ConstraintGenerators_NetProfitCoefficient = 1836
    ConstraintGenerators_PoolRevenueCoefficient = 1837
    ConstraintGenerators_NetRevenueCoefficient = 1838
    ConstraintGenerators_StartShutdownCostCoefficient = 1839
    ConstraintGenerators_FixedCostsCoefficient = 1840
    ConstraintGenerators_InstalledCapacityCoefficient = 1841
    ConstraintGenerators_RatedCapacityCoefficient = 1842
    ConstraintGenerators_UnitsOutCoefficient = 1843
    ConstraintGenerators_MaintenanceCoefficient = 1844
    ConstraintGenerators_FirmCapacityCoefficient = 1845
    ConstraintGenerators_AgeCoefficient = 1846
    ConstraintGenerators_UnitsBuiltCoefficient = 1847
    ConstraintGenerators_UnitsRetiredCoefficient = 1848
    ConstraintGenerators_UnitsBuiltinYearCoefficient = 1849
    ConstraintGenerators_UnitsRetiredinYearCoefficient = 1850
    ConstraintGenerators_CapacityBuiltCoefficient = 1851
    ConstraintGenerators_CapacityRetiredCoefficient = 1852
    ConstraintGenerators_CapacityReservesCoefficient = 1853
    ConstraintGenerators_BuildCostCoefficient = 1854
    ConstraintGenerators_BuiltCoefficient = 1855
    ConstraintGenerators_BuiltinYearCoefficient = 1856
    ConstraintFuels_OfftakeCoefficient = 1857
    ConstraintFuels_EmissionCoefficient = 1858
    ConstraintFuels_InUseCoefficient = 1859
    ConstraintFuels_ClosingInventoryCoefficient = 1860
    ConstraintFuels_InventoryChangeCoefficient = 1861
    ConstraintFuels_DeliveryCoefficient = 1862
    ConstraintFuels_WithdrawalCoefficient = 1863
    ConstraintFuels_GenerationCoefficient = 1864
    ConstraintFuelContracts_OfftakeCoefficient = 1865
    ConstraintEmissions_ProductionCoefficient = 1866
    ConstraintEmissions_AbatementCoefficient = 1867
    ConstraintAbatements_AbatementCoefficient = 1868
    ConstraintAbatements_OperatingHoursCoefficient = 1869
    ConstraintStorages_EndVolumeCoefficient = 1870
    ConstraintStorages_EndLevelCoefficient = 1871
    ConstraintStorages_RampCoefficient = 1872
    ConstraintStorages_NaturalInflowCoefficient = 1873
    ConstraintStorages_InflowCoefficient = 1874
    ConstraintStorages_ReleaseCoefficient = 1875
    ConstraintStorages_GeneratorReleaseCoefficient = 1876
    ConstraintStorages_SpillCoefficient = 1877
    ConstraintStorages_HoursFullCoefficient = 1878
    ConstraintStorages_LossCoefficient = 1879
    ConstraintWaterways_FlowCoefficient = 1880
    ConstraintWaterways_RampCoefficient = 1881
    ConstraintWaterways_HoursFlowingCoefficient = 1882
    ConstraintPhysicalContracts_LoadCoefficient = 1883
    ConstraintPhysicalContracts_GenerationCoefficient = 1884
    ConstraintPhysicalContracts_UnitsGeneratingCoefficient = 1885
    ConstraintPhysicalContracts_UnitsLoadCoefficient = 1886
    ConstraintPhysicalContracts_GenerationCapacityCoefficient = 1887
    ConstraintPhysicalContracts_LoadObligationCoefficient = 1888
    ConstraintPhysicalContracts_BuildCostCoefficient = 1889
    ConstraintPurchasers_LoadCoefficient = 1890
    ConstraintPurchasers_LoadObligationCoefficient = 1891
    ConstraintPurchasers_ReserveProvisionCoefficient = 1892
    ConstraintReserves_ProvisionCoefficient = 1893
    ConstraintReserves_RiskCoefficient = 1894
    ConstraintReserves_ShortageCoefficient = 1895
    ConstraintMarkets_SalesCoefficient = 1896
    ConstraintMarkets_PurchasesCoefficient = 1897
    ConstraintMarkets_RevenueCoefficient = 1898
    ConstraintMarkets_CostCoefficient = 1899
    ConstraintBatteries_EnergyCoefficient = 1900
    ConstraintBatteries_GenerationCoefficient = 1901
    ConstraintBatteries_LoadCoefficient = 1902
    ConstraintBatteries_RampCoefficient = 1903
    ConstraintBatteries_RampUpCoefficient = 1904
    ConstraintBatteries_RampDownCoefficient = 1905
    ConstraintBatteries_RampUpViolationCoefficient = 1906
    ConstraintBatteries_RampDownViolationCoefficient = 1907
    ConstraintBatteries_ReserveProvisionCoefficient = 1908
    ConstraintBatteries_SpinningReserveCoefficient = 1909
    ConstraintBatteries_PumpDispatchableLoadCoefficient = 1910
    ConstraintBatteries_RaiseReserveProvisionCoefficient = 1911
    ConstraintBatteries_LowerReserveProvisionCoefficient = 1912
    ConstraintBatteries_RegulationRaiseReserveProvisionCoefficient = 1913
    ConstraintBatteries_RegulationLowerReserveProvisionCoefficient = 1914
    ConstraintBatteries_ReplacementReserveProvisionCoefficient = 1915
    ConstraintBatteries_ReserveUnitsCoefficient = 1916
    ConstraintBatteries_OperatingReserveUnitsCoefficient = 1917
    ConstraintBatteries_CyclesCoefficient = 1918
    ConstraintBatteries_AgeCoefficient = 1919
    ConstraintBatteries_UnitsBuiltCoefficient = 1920
    ConstraintBatteries_UnitsRetiredCoefficient = 1921
    ConstraintBatteries_UnitsBuiltinYearCoefficient = 1922
    ConstraintBatteries_UnitsRetiredinYearCoefficient = 1923
    ConstraintBatteries_CapacityBuiltCoefficient = 1924
    ConstraintBatteries_CapacityRetiredCoefficient = 1925
    ConstraintBatteries_CapacityReservesCoefficient = 1926
    ConstraintBatteries_BuildCostCoefficient = 1927
    ConstraintBatteries_BuiltCoefficient = 1928
    ConstraintBatteries_BuiltinYearCoefficient = 1929
    ConstraintMaintenances_HoursActiveCoefficient = 1930
    ConstraintMaintenances_CostCoefficient = 1931
    ConstraintMaintenances_CrewCoefficient = 1932
    ConstraintMaintenances_EquipmentCoefficient = 1933
    ConstraintMaintenances_StartHourCoefficient = 1934
    ConstraintMaintenances_StartCoefficient = 1935
    ConstraintHeatNodes_HeatFlowCoefficient = 1936
    ConstraintHeatPlants_UnitsGeneratingCoefficient = 1937
    ConstraintHeatPlants_FuelOfftakeCoefficient = 1938
    ConstraintHeatPlants_HeatProductionCoefficient = 1939
    ConstraintGasFields_EndVolumeCoefficient = 1940
    ConstraintGasFields_ProductionCoefficient = 1941
    ConstraintGasFields_RampCoefficient = 1942
    ConstraintGasFields_UnitsBuiltCoefficient = 1943
    ConstraintGasFields_UnitsBuiltinYearCoefficient = 1944
    ConstraintGasPlants_ProductionCoefficient = 1945
    ConstraintGasPlants_CapacityFactorCoefficient = 1946
    ConstraintGasPlants_OperatingHoursCoefficient = 1947
    ConstraintGasPlants_EnergyUsageCoefficient = 1948
    ConstraintGasPlants_InstalledCapacityCoefficient = 1949
    ConstraintGasPlants_UnitsBuiltCoefficient = 1950
    ConstraintGasPlants_UnitsRetiredCoefficient = 1951
    ConstraintGasPlants_UnitsBuiltinYearCoefficient = 1952
    ConstraintGasPlants_UnitsRetiredinYearCoefficient = 1953
    ConstraintGasPlants_CapacityBuiltCoefficient = 1954
    ConstraintGasPlants_CapacityRetiredCoefficient = 1955
    ConstraintGasPlants_BuildCostCoefficient = 1956
    ConstraintGasPlants_BuiltCoefficient = 1957
    ConstraintGasPlants_BuiltinYearCoefficient = 1958
    ConstraintGasPipelines_EndVolumeCoefficient = 1959
    ConstraintGasPipelines_FlowCoefficient = 1960
    ConstraintGasPipelines_FlowForwardCoefficient = 1961
    ConstraintGasPipelines_FlowBackCoefficient = 1962
    ConstraintGasPipelines_UnitsBuiltCoefficient = 1963
    ConstraintGasPipelines_UnitsRetiredCoefficient = 1964
    ConstraintGasPipelines_UnitsBuiltinYearCoefficient = 1965
    ConstraintGasPipelines_UnitsRetiredinYearCoefficient = 1966
    ConstraintGasNodes_FlowCoefficient = 1967
    ConstraintGasNodes_UnitsBuiltCoefficient = 1968
    ConstraintGasNodes_UnitsRetiredCoefficient = 1969
    ConstraintGasNodes_UnitsBuiltinYearCoefficient = 1970
    ConstraintGasNodes_UnitsRetiredinYearCoefficient = 1971
    ConstraintGasStorages_EndVolumeCoefficient = 1972
    ConstraintGasStorages_WithdrawalCoefficient = 1973
    ConstraintGasStorages_InjectionCoefficient = 1974
    ConstraintGasStorages_RampCoefficient = 1975
    ConstraintGasStorages_UnitsBuiltCoefficient = 1976
    ConstraintGasStorages_UnitsRetiredCoefficient = 1977
    ConstraintGasStorages_UnitsBuiltinYearCoefficient = 1978
    ConstraintGasStorages_UnitsRetiredinYearCoefficient = 1979
    ConstraintGasBasins_ProductionCoefficient = 1980
    ConstraintGasBasins_UnitsBuiltCoefficient = 1981
    ConstraintGasBasins_UnitsBuiltinYearCoefficient = 1982
    ConstraintGasTransports_ShipmentsCoefficient = 1983
    ConstraintGasContracts_ProductionCoefficient = 1984
    ConstraintWaterPlants_ProductionCoefficient = 1985
    ConstraintWaterPlants_CapacityFactorCoefficient = 1986
    ConstraintWaterPlants_OperatingHoursCoefficient = 1987
    ConstraintWaterPlants_EnergyUsageCoefficient = 1988
    ConstraintWaterPlants_InstalledCapacityCoefficient = 1989
    ConstraintWaterPlants_UnitsBuiltCoefficient = 1990
    ConstraintWaterPlants_UnitsRetiredCoefficient = 1991
    ConstraintWaterPlants_UnitsBuiltinYearCoefficient = 1992
    ConstraintWaterPlants_UnitsRetiredinYearCoefficient = 1993
    ConstraintWaterPlants_CapacityBuiltCoefficient = 1994
    ConstraintWaterPlants_CapacityRetiredCoefficient = 1995
    ConstraintWaterPlants_BuildCostCoefficient = 1996
    ConstraintWaterPlants_BuiltCoefficient = 1997
    ConstraintWaterPlants_BuiltinYearCoefficient = 1998
    ConstraintWaterPipelines_FlowCoefficient = 1999
    ConstraintWaterPipelines_FlowForwardCoefficient = 2000
    ConstraintWaterPipelines_FlowBackCoefficient = 2001
    ConstraintWaterPipelines_UnitsBuiltCoefficient = 2002
    ConstraintWaterPipelines_UnitsRetiredCoefficient = 2003
    ConstraintWaterPipelines_UnitsBuiltinYearCoefficient = 2004
    ConstraintWaterPipelines_UnitsRetiredinYearCoefficient = 2005
    ConstraintWaterNodes_FlowCoefficient = 2006
    ConstraintWaterNodes_UnitsBuiltCoefficient = 2007
    ConstraintWaterNodes_UnitsRetiredCoefficient = 2008
    ConstraintWaterNodes_UnitsBuiltinYearCoefficient = 2009
    ConstraintWaterNodes_UnitsRetiredinYearCoefficient = 2010
    ConstraintWaterStorages_NaturalInflowCoefficient = 2011
    ConstraintWaterStorages_EndVolumeCoefficient = 2012
    ConstraintWaterStorages_ReleaseCoefficient = 2013
    ConstraintWaterStorages_InflowCoefficient = 2014
    ConstraintWaterStorages_RampCoefficient = 2015
    ConstraintWaterStorages_UnitsBuiltCoefficient = 2016
    ConstraintWaterStorages_UnitsRetiredCoefficient = 2017
    ConstraintWaterStorages_UnitsBuiltinYearCoefficient = 2018
    ConstraintWaterStorages_UnitsRetiredinYearCoefficient = 2019
    ConstraintRegions_LoadCoefficient = 2020
    ConstraintRegions_LoadSquaredCoefficient = 2021
    ConstraintRegions_GenerationCoefficient = 2022
    ConstraintRegions_CommittedCapacityCoefficient = 2023
    ConstraintRegions_UnservedEnergyCoefficient = 2024
    ConstraintRegions_DumpEnergyCoefficient = 2025
    ConstraintRegions_NetLoadCoefficient = 2026
    ConstraintRegions_FirmCapacityCoefficient = 2027
    ConstraintRegions_GenerationCapacityCoefficient = 2028
    ConstraintRegions_PeakLoadCoefficient = 2029
    ConstraintRegions_CapacityReservesCoefficient = 2030
    ConstraintRegions_GenerationCapacityBuiltCoefficient = 2031
    ConstraintRegions_GenerationCapacityRetiredCoefficient = 2032
    ConstraintRegions_GeneratorBuildCostCoefficient = 2033
    ConstraintRegions_GeneratorsBuiltCoefficient = 2034
    ConstraintRegions_GeneratorsBuiltinYearCoefficient = 2035
    ConstraintRegions_ImportCapacityCoefficient = 2036
    ConstraintRegions_ExportCapacityCoefficient = 2037
    ConstraintRegions_ImportCapacityBuiltCoefficient = 2038
    ConstraintRegions_ExportCapacityBuiltCoefficient = 2039
    ConstraintZones_LoadCoefficient = 2040
    ConstraintZones_LoadSquaredCoefficient = 2041
    ConstraintZones_GenerationCoefficient = 2042
    ConstraintZones_CommittedCapacityCoefficient = 2043
    ConstraintZones_UnservedEnergyCoefficient = 2044
    ConstraintZones_DumpEnergyCoefficient = 2045
    ConstraintZones_NetLoadCoefficient = 2046
    ConstraintZones_FirmCapacityCoefficient = 2047
    ConstraintZones_GenerationCapacityCoefficient = 2048
    ConstraintZones_PeakLoadCoefficient = 2049
    ConstraintZones_CapacityReservesCoefficient = 2050
    ConstraintZones_GenerationCapacityBuiltCoefficient = 2051
    ConstraintZones_GenerationCapacityRetiredCoefficient = 2052
    ConstraintZones_GeneratorBuildCostCoefficient = 2053
    ConstraintZones_GeneratorsBuiltCoefficient = 2054
    ConstraintZones_GeneratorsBuiltinYearCoefficient = 2055
    ConstraintZones_ImportCapacityCoefficient = 2056
    ConstraintZones_ExportCapacityCoefficient = 2057
    ConstraintZones_ImportCapacityBuiltCoefficient = 2058
    ConstraintZones_ExportCapacityBuiltCoefficient = 2059
    ConstraintNodes_LoadCoefficient = 2060
    ConstraintNodes_GenerationCoefficient = 2061
    ConstraintNodes_UnservedEnergyCoefficient = 2062
    ConstraintNodes_DumpEnergyCoefficient = 2063
    ConstraintNodes_NetLoadCoefficient = 2064
    ConstraintNodes_NetInjectionCoefficient = 2065
    ConstraintNodes_PhaseAngleCoefficient = 2066
    ConstraintNodes_MLFCoefficient = 2067
    ConstraintLines_FlowCoefficient = 2068
    ConstraintLines_FlowForwardCoefficient = 2069
    ConstraintLines_FlowBackCoefficient = 2070
    ConstraintLines_FlowSquaredCoefficient = 2071
    ConstraintLines_FlowingForwardCoefficient = 2072
    ConstraintLines_FlowingBackCoefficient = 2073
    ConstraintLines_SpareExportCapacityCoefficient = 2074
    ConstraintLines_SpareImportCapacityCoefficient = 2075
    ConstraintLines_UnitsOutCoefficient = 2076
    ConstraintLines_ExportCapacityCoefficient = 2077
    ConstraintLines_ImportCapacityCoefficient = 2078
    ConstraintLines_UnitsBuiltCoefficient = 2079
    ConstraintLines_UnitsRetiredCoefficient = 2080
    ConstraintLines_UnitsBuiltinYearCoefficient = 2081
    ConstraintLines_UnitsRetiredinYearCoefficient = 2082
    ConstraintLines_ExportCapacityBuiltCoefficient = 2083
    ConstraintLines_ImportCapacityBuiltCoefficient = 2084
    ConstraintLines_ExportCapacityRetiredCoefficient = 2085
    ConstraintLines_ImportCapacityRetiredCoefficient = 2086
    ConstraintLines_BuildCostCoefficient = 2087
    ConstraintTransformers_FlowCoefficient = 2088
    ConstraintFlowControls_AngleCoefficient = 2089
    ConstraintFlowControls_PositiveAngleCoefficient = 2090
    ConstraintFlowControls_NegativeAngleCoefficient = 2091
    ConstraintFlowControls_UnitsBuiltCoefficient = 2092
    ConstraintInterfaces_FlowCoefficient = 2093
    ConstraintInterfaces_FlowForwardCoefficient = 2094
    ConstraintInterfaces_FlowBackCoefficient = 2095
    ConstraintInterfaces_ExpansionCostCoefficient = 2096
    ConstraintHubs_LoadCoefficient = 2097
    ConstraintHubs_GenerationCoefficient = 2098
    ConstraintCompanies_GenerationCoefficient = 2099
    ConstraintCompanies_CommittedCapacityCoefficient = 2100
    ConstraintCompanies_ContractVolumeCoefficient = 2101
    ConstraintConditions_RHSCoefficient = 2102
    ConstraintDecisionVariables_ValueCoefficient = 2103
    ConstraintDecisionVariables_ValueSquaredCoefficient = 2104
    ConstraintVariables_ExpectedValueCoefficient = 2105
    ConstraintVariables_ValueCoefficient = 2106
    ConstraintVariables_ErrorCoefficient = 2107
    ConstraintVariables_PositiveErrorCoefficient = 2108
    ConstraintVariables_NegativeErrorCoefficient = 2109
    DecisionVariableGenerators_HeatInputDefinitionCoefficient = 2110
    DecisionVariableNodes_NetInjectionDefinitionCoefficient = 2111
    DecisionVariableGasPlants_EnergyUsageDefinitionCoefficient = 2112
    DecisionVariableWaterPlants_EnergyUsageDefinitionCoefficient = 2113
    DecisionVariableDefinition_ValueCoefficient = 2114
    VariableGenerators_GenerationCoefficient = 2115
    VariableGenerators_UnitsGeneratingCoefficient = 2116
    VariableGenerators_UnitsStartedCoefficient = 2117
    VariableGenerators_UnitsSyncCondCoefficient = 2118
    VariableGenerators_FuelOfftakeCoefficient = 2119
    VariableGenerators_UnitsOutCoefficient = 2120
    VariableFuels_OfftakeCoefficient = 2121
    VariableHeatNodes_HeatFlowCoefficient = 2122
    VariableHeatPlants_FuelOfftakeCoefficient = 2123
    VariableReserves_ProvisionCoefficient = 2124
    VariableReserves_RiskCoefficient = 2125
    VariableReserves_ShortageCoefficient = 2126
    VariableRegions_LoadCoefficient = 2127
    VariableRegions_CapacityReservesCoefficient = 2128
    VariableRegions_PriceCoefficient = 2129
    VariableZones_LoadCoefficient = 2130
    VariableZones_CapacityReservesCoefficient = 2131
    VariableNodes_LoadCoefficient = 2132
    VariableLines_FlowCoefficient = 2133
    VariableLines_FlowForwardCoefficient = 2134
    VariableLines_FlowBackCoefficient = 2135
    VariableLines_FlowingForwardCoefficient = 2136
    VariableLines_FlowingBackCoefficient = 2137
    VariableInterfaces_FlowCoefficient = 2138
    VariableStorages_EndVolumeCoefficient = 2139
    VariableStorages_InflowCoefficient = 2140
    VariableStorages_ReleaseCoefficient = 2141
    VariableStorages_SpillCoefficient = 2142
    VariableVariables_Correlation = 2143
    VariableVariables_ValueCoefficient = 2144
    GlobalStorages_FCFShadowPrice = 2145
    ModelScenarios_ReadOrder = 2146


class PropertyStatusEnum(Enum):
    Undefined = 0
    Static1 = 1
    Dynamic = 2
    Series = 3
    Cached = 4
    CachedCompressed = 5
    Interleaved = 7


class PumpedStorageModeEnum(Enum):
    None_ = 0
    Optimize = 1
    Fixed = 2


class PurchaserCompaniesEnum(Enum):
    Share = 1


class PurchaserNodesEnum(Enum):
    LoadParticipationFactor = 1


class QueriedColumnCountEnum(Enum):
    Properties = 11
    Periods = 12
    Names = 12
    Values = 13
    Statistics = 13
    Samples = 13
    Timeslices = 13
    Bands = 13
    Models = 14


class RegionRegionsEnum(Enum):
    WheelingCharge = 1
    MaxFlow = 2


class RepairTimeDistributionEnum(Enum):
    Constant = 0
    Uniform = 1
    Triangular = 2
    Exponential = 3
    Weibull = 4
    Lognormal = 5
    SEV = 6
    LEV = 7
    None_ = -1


class ReportAttributeEnum(Enum):
    WriteDatabase = 1
    WriteFlatFiles = 2
    WriteXMLFiles = 3
    XMLContent = 4
    OutputResultsbyPeriod = 5
    OutputResultsbyHour = 6
    OutputResultsbyDay = 7
    OutputResultsbyWeek = 8
    OutputResultsbyMonth = 9
    OutputResultsbyQuarter = 10
    OutputResultsbyFiscalYear = 11
    OutputStatistics = 12
    OutputResultsbySample = 13
    FilterObjectsByInterval = 14
    FilterObjectsInSummary = 15
    WholeYearsOnly = 16
    DatetimeConvention = 17
    Locale = 18
    FlatFileFormat = 19


class ReserveBatteriesEnum(Enum):
    OfferQuantity = 1
    OfferPrice = 2


class ReserveGeneratorsEnum(Enum):
    InitialPumpLoadRaiseProvision = 1
    InitialRaiseProvision = 2
    MaxResponse = 3
    MaxSyncCondResponse = 4
    MaxPumpResponse = 5
    MaxReplacement = 6
    MaxResponseFactor = 7
    MaxSyncCondResponseFactor = 8
    MaxPumpResponseFactor = 9
    MaxReplacementFactor = 10
    MinProvision = 11
    MinSpinningProvision = 12
    MinRegulationProvision = 13
    MinReplacementProvision = 14
    Effectiveness = 15
    ResponseRatio = 16
    OfferQuantity = 17
    OfferPrice = 18
    SyncCondOfferPrice = 19
    PumpOfferPrice = 20
    ReplacementOfferQuantity = 21
    ReplacementOfferPrice = 22


class ReserveLineContingenciesEnum(Enum):
    FlowForwardCoefficient = 1
    FlowBackCoefficient = 2


class ReserveMutuallyExclusiveEnum(Enum):
    Auto = 0
    Yes = 1
    No = 2


class ReservePurchasersEnum(Enum):
    OfferQuantity = 1
    OfferPrice = 2


class ReserveRegionsEnum(Enum):
    LoadRisk = 1
    LOLPTarget = 2


class ReserveTypeEnum(Enum):
    Raise = 1
    Lower = 2
    RegulationRaise = 3
    RegulationLower = 4
    Replacement = 5
    Operational = 6
    Regulation = 7


class STScheduleAttributeEnum(Enum):
    DiscountRate = 1
    DiscountPeriodType = 2
    EndEffectsMethod = 3
    HeatRateDetail = 4
    TransmissionDetail = 5
    StochasticMethod = 6


class ScenarioAttributeEnum(Enum):
    ReadOrder = 1
    Locked = 2


class SenseEnum(Enum):
    FX = 0
    LO = 1
    UP = -1


class SeriesTypeEnum(Enum):
    Values = 0
    Properties = 1
    Names = 2
    Periods = 3
    Bands = 4
    Statistics = 5
    Samples = 6
    Models = 7
    Timeslices = 8


class SimulationPhaseEnum(Enum):
    LTPlan = 1
    PASA = 2
    MTSchedule = 3
    STSchedule = 4


class SolutionPeriodEnum(Enum):
    Period = 0
    Summary = 1


class StartCostFunctionEnum(Enum):
    Interpolate = 0
    StepFunction = 1


class StatisticsEnum(Enum):
    Mean = 0
    Max = -3
    Min = -2
    StdDev = -1


class StochasticAttributeEnum(Enum):
    OutagePatternCount = 1
    MonteCarloMethod = 2
    WeibullShape = 3
    ConvergentSmoothing = 4
    OutageScope = 5
    ConvergencePeriodType = 6
    RiskSampleCount = 7
    ReducedOutagePatternCount = 8
    ReducedSampleCount = 9
    ReductionRelativeAccuracy = 10
    ForcedOutagesinLookahead = 11
    EFORMaintenanceAdjust = 12


class StochasticMethodEnum(Enum):
    Deterministic = 0
    IndependentSamples = 1
    ScenariowiseDecomposition = 2
    Parallel = 3


class StorageAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class StorageBridgeEnum(Enum):
    InitialVolume = 1
    EndVolume = 2
    ShadowPrice = 3


class StorageDecompositionMethodEnum(Enum):
    None_ = 0
    Target = 1
    WaterValue = 2


class StorageEndEffectsMethodEnum(Enum):
    Automatic = 0
    Free = 1
    Recyle = 2


class SummaryTypeEnum(Enum):
    None_ = 0
    Sum = 1
    Avg = 2
    Min = 3
    Max = 4
    MaxAbs = 5
    ZeroBoundedDifference = 6
    AtExactInterval = 7
    AtExactIntervalSum = 8
    AtExactIntervalLast = 9
    First = 10
    Last = 11


class SystemAbatementsEnum(Enum):
    Units = 1
    AbatementCost = 2
    RunningCost = 3
    VOMCharge = 4
    Efficiency = 5
    MaxAbatement = 6
    FOMCharge = 7
    UnitsOut = 8
    x = 9
    y = 10
    z = 11


class SystemBatteriesEnum(Enum):
    RandomNumberSeed = 1
    RepairTimeDistribution = 2
    EndEffectsMethod = 3
    ExpansionOptimality = 4
    Units = 5
    Capacity = 6
    MaxPower = 7
    MaxLoad = 8
    MaxSoC = 9
    MinSoC = 10
    InitialSoC = 11
    ChargeEfficiency = 12
    DischargeEfficiency = 13
    VOMCharge = 14
    UoSCharge = 15
    MaxRampUp = 16
    MaxRampUpPenalty = 17
    MaxRampDown = 18
    MaxRampDownPenalty = 19
    MaxCycles = 20
    EnergyTarget = 21
    EnergyTargetPenalty = 22
    Nonanticipativity = 23
    NonanticipativityTime = 24
    InitialAge = 25
    PowerDegradation = 26
    CapacityDegradation = 27
    FirmCapacity = 28
    FOMCharge = 29
    MaintenanceRate = 30
    MaintenanceFrequency = 31
    ForcedOutageRate = 32
    MeanTimetoRepair = 33
    MinTimeToRepair = 34
    MaxTimeToRepair = 35
    RepairTimeShape = 36
    RepairTimeScale = 37
    MaxUnitsBuilt = 38
    LeadTime = 39
    ProjectStartDate = 40
    TechnicalLife = 41
    BuildCost = 42
    WACC = 43
    EconomicLife = 44
    MinUnitsBuilt = 45
    MaxUnitsBuiltinYear = 46
    MinUnitsBuiltinYear = 47
    MaxUnitsRetired = 48
    RetirementCost = 49
    MinUnitsRetired = 50
    MaxUnitsRetiredinYear = 51
    MinUnitsRetiredinYear = 52
    BuildNonanticipativity = 53
    RetireNonanticipativity = 54
    x = 55
    y = 56
    z = 57


class SystemCompaniesEnum(Enum):
    Strategic = 1
    MarkupBias = 2
    FormulateRisk = 3
    RiskLevel = 4
    AcceptableRisk = 5
    MaxMaintenance = 6
    MinMaintenance = 7
    MaxMaintenanceFactor = 8
    MinMaintenanceFactor = 9
    x = 10
    y = 11
    z = 12


class SystemConstraintsEnum(Enum):
    Sense = 1
    LHSType = 2
    FormulateUpfront = 3
    ConditionLogic = 4
    IncludeinLTPlan = 5
    IncludeinPASA = 6
    IncludeinMTSchedule = 7
    IncludeinSTSchedule = 8
    IncludeinUniformPricing = 9
    DecompositionMethod = 10
    FeasibilityRepairWeight = 11
    WildcardMode = 12
    RHS = 13
    PenaltyQuantity = 14
    PenaltyPrice = 15
    MinRHS = 16
    MaxRHS = 17
    x = 18
    y = 19
    z = 20


class SystemContingenciesEnum(Enum):
    IsEnabled = 1
    MonitoringThreshold = 2
    x = 3
    y = 4
    z = 5


class SystemCournotsEnum(Enum):
    DemandIntercept = 1
    DemandSlope = 2


class SystemDataFilesEnum(Enum):
    Filename = 1
    BaseProfile = 2
    Energy = 3
    Maximum = 4
    Minimum = 5
    Holiday = 6
    MinValue = 7
    MaxValue = 8


class SystemDecisionVariablesEnum(Enum):
    IncludeinLTPlan = 1
    IncludeinPASA = 2
    IncludeinMTSchedule = 3
    IncludeinSTSchedule = 4
    ObjectiveFunctionCoefficient = 5
    LowerBound = 6
    UpperBound = 7
    Nonanticipativity = 8
    NonanticipativityTime = 9
    x = 10
    y = 11
    z = 12


class SystemEmissionsEnum(Enum):
    Price = 1
    MaxProduction = 2
    MaxProductionPenalty = 3
    ShadowPrice = 4
    x = 5
    y = 6
    z = 7


class SystemFinancialContractsEnum(Enum):
    IsPhysical = 1
    Quantity = 2
    FloorPrice = 3
    CapPrice = 4


class SystemFlowControlsEnum(Enum):
    PriceSetting = 1
    ExpansionOptimality = 2
    Type = 3
    Units = 4
    MinAngle = 5
    MaxAngle = 6
    MinImpedance = 7
    MaxImpedance = 8
    MinVoltage = 9
    MaxVoltage = 10
    Penalty = 11
    Angle = 12
    AnglePoints = 13
    FlowLoadingPoints = 14
    FOMCharge = 15
    BuildCost = 16
    LeadTime = 17
    ProjectStartDate = 18
    CommissionDate = 19
    TechnicalLife = 20
    WACC = 21
    EconomicLife = 22
    MaxUnitsBuilt = 23
    MinUnitsBuilt = 24
    MaxUnitsBuiltinYear = 25
    MinUnitsBuiltinYear = 26
    BuildNonanticipativity = 27
    x = 28
    y = 29
    z = 30


class SystemFuelContractsEnum(Enum):
    Quantity = 1
    Price = 2
    PriceIncr = 3
    PriceScalar = 4
    TakeorPayQuantity = 5
    TakeorPayPrice = 6
    FOMCharge = 7
    x = 8
    y = 9
    z = 10


class SystemFuelsEnum(Enum):
    BalancePeriod = 1
    DecompositionMethod = 2
    DecompositionPenaltya = 3
    DecompositionPenaltyb = 4
    DecompositionPenaltyc = 5
    DecompositionPenaltyx = 6
    DecompositionBoundPenalty = 7
    Units = 8
    Price = 9
    Tax = 10
    PriceIncr = 11
    PriceScalar = 12
    HeatValue = 13
    MaxOfftake = 14
    MinOfftake = 15
    ShadowPrice = 16
    ShadowPriceIncr = 17
    ShadowPriceScalar = 18
    MaxInventory = 19
    MinInventory = 20
    OpeningInventory = 21
    Delivery = 22
    DeliveryCharge = 23
    InventoryCharge = 24
    ReservationCharge = 25
    WithdrawalCharge = 26
    MaxWithdrawal = 27
    MinWithdrawal = 28
    FOMCharge = 29
    x = 30
    y = 31
    z = 32


class SystemGasBasinsEnum(Enum):
    MaxProduction = 1
    MinProduction = 2
    x = 3
    y = 4
    z = 5


class SystemGasContractsEnum(Enum):
    PriceSetting = 1
    Quantity = 2
    TakeorPayQuantity = 3
    TakeorPayPrice = 4
    Price = 5
    x = 6
    y = 7
    z = 8


class SystemGasDemandsEnum(Enum):
    Demand = 1
    ShortagePrice = 2
    ExcessPrice = 3
    BidQuantity = 4
    BidPrice = 5
    x = 6
    y = 7
    z = 8


class SystemGasFieldsEnum(Enum):
    BalancePeriod = 1
    InternalVolumeScalar = 2
    EndEffectsMethod = 3
    RecyclePenalty = 4
    DecompositionMethod = 5
    DecompositionPenaltya = 6
    DecompositionPenaltyb = 7
    DecompositionPenaltyc = 8
    DecompositionPenaltyx = 9
    DecompositionBoundPenalty = 10
    EnforceBounds = 11
    ExpansionOptimality = 12
    Units = 13
    InitialVolume = 14
    ProductionCost = 15
    ProductionVolume = 16
    MaxRamp = 17
    MaxProduction = 18
    MinProduction = 19
    Target = 20
    TargetPenalty = 21
    ExternalInjection = 22
    FOMCharge = 23
    MaxUnitsBuilt = 24
    LeadTime = 25
    ProjectStartDate = 26
    TechnicalLife = 27
    BuildCost = 28
    WACC = 29
    EconomicLife = 30
    MaxUnitsBuiltinYear = 31
    x = 32
    y = 33
    z = 34


class SystemGasNodesEnum(Enum):
    ExpansionOptimality = 1
    Units = 2
    FlowCharge = 3
    MaxFlow = 4
    GasSecurity = 5
    FOMCharge = 6
    MaxUnitsBuilt = 7
    LeadTime = 8
    ProjectStartDate = 9
    TechnicalLife = 10
    BuildCost = 11
    WACC = 12
    EconomicLife = 13
    MinUnitsBuilt = 14
    MaxUnitsBuiltinYear = 15
    MinUnitsBuiltinYear = 16
    MaxUnitsRetired = 17
    RetirementCost = 18
    MinUnitsRetired = 19
    MaxUnitsRetiredinYear = 20
    MinUnitsRetiredinYear = 21
    x = 22
    y = 23
    z = 24


class SystemGasPipelinesEnum(Enum):
    RandomNumberSeed = 1
    BalancePeriod = 2
    InternalVolumeScalar = 3
    EndEffectsMethod = 4
    RecyclePenalty = 5
    DecompositionMethod = 6
    DecompositionPenaltya = 7
    DecompositionPenaltyb = 8
    DecompositionPenaltyc = 9
    DecompositionPenaltyx = 10
    DecompositionBoundPenalty = 11
    EnforceBounds = 12
    RepairTimeDistribution = 13
    ExpansionOptimality = 14
    Units = 15
    MaxFlow = 16
    MaxFlowBack = 17
    Diameter = 18
    Roughness = 19
    Length = 20
    PumpEfficiency = 21
    FlowCharge = 22
    FlowChargeBack = 23
    InitialVolume = 24
    MaxVolume = 25
    MinVolume = 26
    VolumeImbalance = 27
    ImbalanceCharge = 28
    FOMCharge = 29
    ConsumptionAllocation = 30
    UnitsOut = 31
    MaintenanceRate = 32
    MaintenanceFrequency = 33
    ForcedOutageRate = 34
    OutageMaxFlow = 35
    OutageMaxFlowBack = 36
    MeanTimetoRepair = 37
    MinTimeToRepair = 38
    MaxTimeToRepair = 39
    RepairTimeShape = 40
    RepairTimeScale = 41
    MaxUnitsBuilt = 42
    LeadTime = 43
    ProjectStartDate = 44
    TechnicalLife = 45
    BuildCost = 46
    WACC = 47
    EconomicLife = 48
    MinUnitsBuilt = 49
    MaxUnitsBuiltinYear = 50
    MinUnitsBuiltinYear = 51
    MaxUnitsRetired = 52
    RetirementCost = 53
    MinUnitsRetired = 54
    MaxUnitsRetiredinYear = 55
    MinUnitsRetiredinYear = 56
    x = 57
    y = 58
    z = 59


class SystemGasPlantsEnum(Enum):
    ExpansionOptimality = 1
    Units = 2
    MaxProduction = 3
    MinProduction = 4
    ProcessingRate = 5
    ProcessingCharge = 6
    Consumption = 7
    EnergyUsage = 8
    VOMCharge = 9
    FOMCharge = 10
    MaxUnitsBuilt = 11
    LeadTime = 12
    ProjectStartDate = 13
    TechnicalLife = 14
    BuildCost = 15
    WACC = 16
    EconomicLife = 17
    MinUnitsBuilt = 18
    MaxUnitsBuiltinYear = 19
    MinUnitsBuiltinYear = 20
    MaxUnitsRetired = 21
    RetirementCost = 22
    MinUnitsRetired = 23
    MaxUnitsRetiredinYear = 24
    MinUnitsRetiredinYear = 25
    x = 26
    y = 27
    z = 28


class SystemGasStoragesEnum(Enum):
    BalancePeriod = 1
    InternalVolumeScalar = 2
    EndEffectsMethod = 3
    RecyclePenalty = 4
    DecompositionMethod = 5
    DecompositionPenaltya = 6
    DecompositionPenaltyb = 7
    DecompositionPenaltyc = 8
    DecompositionPenaltyx = 9
    DecompositionBoundPenalty = 10
    EnforceBounds = 11
    ExpansionOptimality = 12
    Units = 13
    MaxVolume = 14
    MinVolume = 15
    InitialVolume = 16
    WithdrawalCharge = 17
    InjectionCharge = 18
    InjectionRatchet = 19
    WithdrawalRatchet = 20
    MaxWithdrawal = 21
    MaxInjection = 22
    MinWithdrawal = 23
    MinInjection = 24
    MaxRamp = 25
    Target = 26
    TargetPenalty = 27
    EnergyUsage = 28
    LossRate = 29
    WithdrawalRateScalar = 30
    WithdrawalVolume = 31
    InjectionRateScalar = 32
    InjectionVolume = 33
    ExternalInjection = 34
    FOMCharge = 35
    MaxUnitsBuilt = 36
    LeadTime = 37
    ProjectStartDate = 38
    TechnicalLife = 39
    BuildCost = 40
    WACC = 41
    EconomicLife = 42
    MinUnitsBuilt = 43
    MaxUnitsBuiltinYear = 44
    MinUnitsBuiltinYear = 45
    MaxUnitsRetired = 46
    RetirementCost = 47
    MinUnitsRetired = 48
    MaxUnitsRetiredinYear = 49
    MinUnitsRetiredinYear = 50
    TrajectoryNonanticipativity = 51
    TrajectoryNonanticipativityVolume = 52
    TrajectoryNonanticipativityTime = 53
    x = 54
    y = 55
    z = 56


class SystemGasTransportsEnum(Enum):
    VoyageTime = 1
    LoadingTime = 2
    DischargeTime = 3
    MinVolume = 4
    MaxVolume = 5
    ShippingCharge = 6
    BoiloffRate = 7
    Imports = 8
    Exports = 9
    MaxShipments = 10
    x = 11
    y = 12
    z = 13


class SystemGasZonesEnum(Enum):
    x = 1
    y = 2
    z = 3


class SystemGeneratorsEnum(Enum):
    MustReport = 1
    RandomNumberSeed = 2
    DispatchPeriod = 3
    MaxHeatRateTranches = 4
    FormulateNonconvex = 5
    HeadEffectsMethod = 6
    MinDownTimeMode = 7
    ForcedOutageRateDenominator = 8
    RepairTimeDistribution = 9
    FixedLoadMethod = 10
    PriceSetting = 11
    OfferQuantityFormat = 12
    OffersMustClearinOrder = 13
    UnitCommitmentOptimality = 14
    RoundingUpThreshold = 15
    IncludeinRoundedRelaxationMeritOrder = 16
    StartProfileRange = 17
    ExpansionOptimality = 18
    DecliningDepreciationBalance = 19
    EnergyLimitDecompositionMethod = 20
    IncludeinUplift = 21
    IncludeinCapacityPayments = 22
    BalancePeriod = 23
    InternalVolumeScalar = 24
    EndEffectsMethod = 25
    RecyclePenalty = 26
    DecompositionMethod = 27
    DecompositionPenaltya = 28
    DecompositionPenaltyb = 29
    DecompositionPenaltyc = 30
    DecompositionPenaltyx = 31
    DecompositionBoundPenalty = 32
    EnforceBounds = 33
    IsStrategic = 34
    TransitionType = 35
    Units = 36
    MaxCapacity = 37
    MinStableLevel = 38
    MinStableFactor = 39
    FuelPrice = 40
    LoadPoint = 41
    HeatRate = 42
    HeatRateBase = 43
    HeatRateIncr = 44
    HeatRateIncr2 = 45
    HeatRateIncr3 = 46
    VOMCharge = 47
    UoSCharge = 48
    RunningCost = 49
    StartCost = 50
    StartCostTime = 51
    RunUpRate = 52
    StartProfile = 53
    StartPenalty = 54
    ShutdownCost = 55
    RunDownRate = 56
    ShutdownProfile = 57
    ShutdownPenalty = 58
    Rating = 59
    RatingFactor = 60
    MinUpTime = 61
    MinDownTime = 62
    MaxUpTime = 63
    MaxDownTime = 64
    MustRunUnits = 65
    FixedLoad = 66
    FixedLoadPenalty = 67
    MinLoad = 68
    MinLoadPenalty = 69
    MaxLoad = 70
    Commit = 71
    FuelMixPenalty = 72
    RampUpCharge = 73
    RampDownCharge = 74
    MaxRampUp = 75
    MaxRampUpPenalty = 76
    MaxRampDown = 77
    MaxRampDownPenalty = 78
    RoughRunningPoint = 79
    RoughRunningRange = 80
    RegulationPoint = 81
    RegulationRange = 82
    AuxFixed = 83
    AuxBase = 84
    AuxIncr = 85
    MarginalLossFactor = 86
    EfficiencyBase = 87
    EfficiencyIncr = 88
    PumpEfficiency = 89
    PumpLoad = 90
    PumpUnits = 91
    MinPumpLoad = 92
    MustPumpUnits = 93
    MaxUnitsPumping = 94
    FixedPumpLoad = 95
    FixedPumpLoadPenalty = 96
    PumpUoSCharge = 97
    MinPumpTime = 98
    MinPumpDownTime = 99
    ReservesVOMCharge = 100
    SyncCondUnits = 101
    MustrunSyncCondUnits = 102
    SyncCondLoad = 103
    SyncCondVOMCharge = 104
    ReserveShare = 105
    InitialGeneration = 106
    InitialUnitsGenerating = 107
    InitialHoursUp = 108
    InitialHoursDown = 109
    InitialPumping = 110
    InitialUnitsPumping = 111
    InitialHoursPumping = 112
    GeneratortoPumpSwitchTime = 113
    PumptoGeneratorSwitchTime = 114
    EfficiencyDegradation = 115
    LastStartState = 116
    ReferenceGeneration = 117
    LoadSubtracter = 118
    PriceFollowing = 119
    LoadFollowingProfile = 120
    LoadFollowingFactor = 121
    BoilerEfficiency = 122
    HeatLoad = 123
    PowertoHeatRatio = 124
    CHPElectricHeatRateIncr = 125
    CHPHeatSurrogateRateIncr = 126
    BoilerHeatRateIncr = 127
    MaxBoilerHeat = 128
    MaxHeat = 129
    MinHeat = 130
    OpeningHeat = 131
    HeatWithdrawalCharge = 132
    HeatInjectionCharge = 133
    FixedCharge = 134
    HeatLoss = 135
    WaterOfftake = 136
    WaterConsumption = 137
    MaxRelease = 138
    MaxEnergy = 139
    MinEnergy = 140
    MaxCapacityFactor = 141
    MinCapacityFactor = 142
    MaxEnergyPenalty = 143
    MinEnergyPenalty = 144
    MaxStarts = 145
    MaxStartsPenalty = 146
    EnergyScalar = 147
    MaxHeatWithdrawal = 148
    MaxHeatInjection = 149
    MinHeatWithdrawal = 150
    MinHeatInjection = 151
    OfferBase = 152
    OfferNoLoadCost = 153
    OfferQuantity = 154
    OfferPrice = 155
    OfferQuantityScalar = 156
    OfferPriceIncr = 157
    OfferPriceScalar = 158
    Markup = 159
    BidCostMarkup = 160
    MarkupPoint = 161
    PumpBidBase = 162
    PumpBidQuantity = 163
    PumpBidPrice = 164
    PumpBidQuantityScalar = 165
    PumpBidPriceIncr = 166
    PumpBidPriceScalar = 167
    StrategicRating = 168
    StrategicReferencePrice = 169
    InitialAge = 170
    PowerDegradation = 171
    CapacityDegradation = 172
    FOMCharge = 173
    EquityCharge = 174
    DebtCharge = 175
    FirmCapacity = 176
    UnitsOut = 177
    Maintenance = 178
    ForcedOutage = 179
    MaintenanceRate = 180
    MaintenanceFrequency = 181
    ForcedOutageRate = 182
    OutageFactor = 183
    OutageRating = 184
    OutagePumpLoad = 185
    InitialOperatingHours = 186
    MeanTimetoRepair = 187
    MinTimeToRepair = 188
    MaxTimeToRepair = 189
    RepairTimeShape = 190
    RepairTimeScale = 191
    BuildCost = 192
    RetirementCost = 193
    OnetimeCost = 194
    LeadTime = 195
    ProjectStartDate = 196
    CommissionDate = 197
    TechnicalLife = 198
    WACC = 199
    EconomicLife = 200
    MaxUnitsBuilt = 201
    MaxUnitsRetired = 202
    MinUnitsBuilt = 203
    MinUnitsRetired = 204
    MaxUnitsBuiltinYear = 205
    MaxUnitsRetiredinYear = 206
    MinUnitsBuiltinYear = 207
    MinUnitsRetiredinYear = 208
    BuildSetSize = 209
    CapacityPrice = 210
    UnitCommitmentNonanticipativity = 211
    UnitCommitmentNonanticipativityTime = 212
    PumpUnitCommitmentNonanticipativity = 213
    PumpUnitCommitmentNonanticipativityTime = 214
    GenerationNonanticipativity = 215
    GenerationNonanticipativityTime = 216
    PumpLoadNonanticipativity = 217
    PumpLoadNonanticipativityTime = 218
    BuildNonanticipativity = 219
    RetireNonanticipativity = 220
    x = 221
    y = 222
    z = 223


class SystemGlobalsEnum(Enum):
    FCFConstant = 1
    SampleWeight = 2
    TreeStageCount = 3
    TreePeriodType = 4
    TreePositionExpFactor = 5
    TreeLeavesExpFactor = 6
    TreeStagesPosition = 7
    TreeStagesLeaves = 8
    TreeStagesHangingBranches = 9
    DeterministicStages = 10
    HangingBranchesHistoricalYearStart = 11
    HangingBranchesWeight = 12
    HangingBranchesBlockCount = 13
    SlicingBlock = 14


class SystemHeatNodesEnum(Enum):
    AllowDumpHeat = 1
    Units = 2
    HeatDemand = 3
    x = 4
    y = 5
    z = 6


class SystemHeatPlantsEnum(Enum):
    UnitCommitmentOptimality = 1
    Units = 2
    MaxCapacity = 3
    EfficiencyBase = 4
    EfficiencyIncr = 5
    VOMCharge = 6
    LoadPoint = 7
    HeatRate = 8
    HeatRateBase = 9
    HeatRateIncr = 10
    StartCost = 11
    StartCostTime = 12
    RunUpRate = 13
    StartProfile = 14
    MinUpTime = 15
    MinDownTime = 16
    MaxUpTime = 17
    MaxDownTime = 18
    MaxRampUp = 19
    MaxRampDown = 20
    MinStableLevel = 21
    FOMCharge = 22
    MaxUnitsBuilt = 23
    LeadTime = 24
    ProjectStartDate = 25
    TechnicalLife = 26
    BuildCost = 27
    WACC = 28
    EconomicLife = 29
    MinUnitsBuilt = 30
    MaxUnitsBuiltinYear = 31
    MinUnitsBuiltinYear = 32
    MaxUnitsRetired = 33
    RetirementCost = 34
    MinUnitsRetired = 35
    MaxUnitsRetiredinYear = 36
    MinUnitsRetiredinYear = 37
    x = 38
    y = 39
    z = 40


class SystemHubsEnum(Enum):
    PricingMethod = 1
    Units = 2
    x = 3
    y = 4
    z = 5


class SystemInterfacesEnum(Enum):
    FormulateUpfront = 1
    OfferQuantityFormat = 2
    Units = 3
    MinFlow = 4
    MaxFlow = 5
    OverloadMaxRating = 6
    OverloadMinRating = 7
    LimitPenalty = 8
    MaxRampUp = 9
    MaxRampDown = 10
    RampPenalty = 11
    FixedFlow = 12
    FixedFlowPenalty = 13
    OfferBase = 14
    OfferQuantity = 15
    OfferPrice = 16
    OfferQuantityBack = 17
    OfferPriceBack = 18
    FlowNonanticipativity = 19
    FlowNonanticipativityTime = 20
    FirmCapacity = 21
    ExpansionCost = 22
    MaxExpansion = 23
    WACC = 24
    EconomicLife = 25
    BuildNonanticipativity = 26
    x = 27
    y = 28
    z = 29


class SystemLinesEnum(Enum):
    MustReport = 1
    RandomNumberSeed = 2
    RepairTimeDistribution = 3
    EnforceLimits = 4
    FormulateUpfront = 5
    FormulateNPLUpfront = 6
    MaxLossTranches = 7
    PriceSetting = 8
    OfferQuantityFormat = 9
    FixedFlowMethod = 10
    ExpansionOptimality = 11
    Units = 12
    MaxFlow = 13
    MinFlow = 14
    MaxRating = 15
    MinRating = 16
    OverloadMaxRating = 17
    OverloadMinRating = 18
    LimitPenalty = 19
    Resistance = 20
    Reactance = 21
    Susceptance = 22
    MaxRampUp = 23
    MaxRampDown = 24
    RampPenalty = 25
    LossBase = 26
    LossIncr = 27
    LossIncr2 = 28
    LossBaseBack = 29
    LossIncrBack = 30
    LossIncr2Back = 31
    LossAllocation = 32
    FixedFlow = 33
    FixedFlowPenalty = 34
    FixedLoss = 35
    WheelingCharge = 36
    WheelingChargeBack = 37
    OfferBase = 38
    OfferQuantity = 39
    OfferPrice = 40
    OfferQuantityBack = 41
    OfferPriceBack = 42
    MarginalLossFactor = 43
    MarginalLossFactorBack = 44
    FlowNonanticipativity = 45
    FlowNonanticipativityTime = 46
    FixedCharge = 47
    FOMCharge = 48
    EquityCharge = 49
    DebtCharge = 50
    Circuits = 51
    UnitsOut = 52
    MaintenanceRate = 53
    MaintenanceFrequency = 54
    ForcedOutageRate = 55
    OutageMaxRating = 56
    OutageMinRating = 57
    MeanTimetoRepair = 58
    MinTimeToRepair = 59
    MaxTimeToRepair = 60
    RepairTimeShape = 61
    RepairTimeScale = 62
    MaxCapacityReserves = 63
    MinCapacityReserves = 64
    FirmCapacity = 65
    Type = 66
    BuildCost = 67
    RetirementCost = 68
    LeadTime = 69
    ProjectStartDate = 70
    CommissionDate = 71
    TechnicalLife = 72
    WACC = 73
    EconomicLife = 74
    MaxUnitsBuilt = 75
    MaxUnitsRetired = 76
    MinUnitsBuilt = 77
    MinUnitsRetired = 78
    MaxUnitsBuiltinYear = 79
    MaxUnitsRetiredinYear = 80
    MinUnitsBuiltinYear = 81
    MinUnitsRetiredinYear = 82
    BuildNonanticipativity = 83
    RetireNonanticipativity = 84
    x = 85
    y = 86
    z = 87


class SystemMLFsEnum(Enum):
    Intercept = 1
    FlowCoefficient = 2


class SystemMaintenancesEnum(Enum):
    Duration = 1
    Window = 2
    StartWindow = 3
    EndWindow = 4
    Cost = 5
    Crew = 6
    Equipment = 7
    LeadTime = 8
    MutuallyExclusive = 9
    PenaltyCost = 10
    MinOccurrence = 11
    Nonanticipativity = 12
    x = 13
    y = 14
    z = 15


class SystemMarketsEnum(Enum):
    IsForward = 1
    IsMarginal = 2
    DemandCurve = 3
    PriceSetting = 4
    SupplySettlementModel = 5
    DemandSettlementModel = 6
    Units = 7
    Price = 8
    PriceScalar = 9
    PriceIncr = 10
    Quantity = 11
    BaseQuantity = 12
    SellUnit = 13
    SellBlock = 14
    SellBlockFixedCharge = 15
    BuyUnit = 16
    BuyBlock = 17
    BuyBlockFixedCharge = 18
    MinSales = 19
    MaxSales = 20
    MinPurchases = 21
    MaxPurchases = 22
    BidAskSpread = 23
    BidSpread = 24
    AskSpread = 25
    FirmCapacity = 26
    LoadObligation = 27
    x = 28
    y = 29
    z = 30


class SystemNodesEnum(Enum):
    MustReport = 1
    IsSlackBus = 2
    AllowDumpEnergy = 3
    AllowUnservedEnergy = 4
    ReferenceLoad = 5
    Voltage = 6
    Units = 7
    LoadParticipationFactor = 8
    Load = 9
    FixedLoad = 10
    FixedGeneration = 11
    MaxNetInjection = 12
    MaxNetOfftake = 13
    Rating = 14
    DSPBidQuantity = 15
    DSPBidRatio = 16
    DSPBidPrice = 17
    Price = 18
    MaxMaintenance = 19
    MaintenanceFactor = 20
    MinCapacityReserves = 21
    MinCapacityReserveMargin = 22
    x = 23
    y = 24
    z = 25


class SystemOutAbatementsEnum(Enum):
    Units = 1
    OperatingHours = 2
    GrossEmissions = 3
    Abatement = 4
    NetEmissions = 5
    Efficiency = 6
    AbatementCost = 7
    RunningCost = 8
    VOMCost = 9
    ConsumablesCost = 10
    FOMCost = 11
    TotalCost = 12
    AbatementValue = 13
    AbatementNetCost = 14
    UnitsOut = 15
    x = 16
    y = 17
    z = 18


class SystemOutBatteriesEnum(Enum):
    Units = 1
    Energy = 2
    SoC = 3
    AvailableSoC = 4
    Generation = 5
    Load = 6
    NetGeneration = 7
    Losses = 8
    HoursCharging = 9
    HoursDischarging = 10
    HoursIdle = 11
    RaiseReserve = 12
    LowerReserve = 13
    RegulationRaiseReserve = 14
    RegulationLowerReserve = 15
    ReplacementReserve = 16
    VOMCost = 17
    UoSCost = 18
    CapacityFactor = 19
    LoadFactor = 20
    PriceReceived = 21
    PricePaid = 22
    GenerationRevenue = 23
    CosttoLoad = 24
    NetGenerationRevenue = 25
    ReservesRevenue = 26
    ClearedReserveOfferCost = 27
    NetProfit = 28
    InstalledCapacity = 29
    FirmCapacity = 30
    FOMCost = 31
    Age = 32
    UnitsBuilt = 33
    BuildCost = 34
    UnitsRetired = 35
    RetirementCost = 36
    x = 37
    y = 38
    z = 39


class SystemOutCompaniesEnum(Enum):
    Generation = 1
    FuelOfftake = 2
    WasteHeat = 3
    StartFuelOfftake = 4
    DispatchableCapacity = 5
    UndispatchedCapacity = 6
    NoCostCapacity = 7
    CapacityCurtailed = 8
    FixedLoadGeneration = 9
    MinLoadGeneration = 10
    RaiseReserve = 11
    LowerReserve = 12
    RegulationRaiseReserve = 13
    RegulationLowerReserve = 14
    ReplacementReserve = 15
    AuxiliaryUse = 16
    PumpLoad = 17
    Load = 18
    PurchaserLoad = 19
    NetGeneration = 20
    NetLoad = 21
    FuelPrice = 22
    FuelCost = 23
    FuelTransportCost = 24
    FuelTransitionCost = 25
    FuelInventoryCost = 26
    VOMCost = 27
    UoSCost = 28
    PumpCost = 29
    ReservesVOMCost = 30
    ReservesCost = 31
    GenerationCost = 32
    GeneratorStartShutdownCost = 33
    StartFuelCost = 34
    EmissionsCost = 35
    AbatementCost = 36
    TotalGenerationCost = 37
    TotalSystemCost = 38
    FuelContractCost = 39
    FOMCost = 40
    EquityCost = 41
    DebtCost = 42
    FixedCosts = 43
    CosttoLoad = 44
    SRMC = 45
    PriceReceived = 46
    PricePaid = 47
    PoolRevenue = 48
    ReservesRevenue = 49
    GasMarketRevenue = 50
    HeatMarketRevenue = 51
    FuelMarketRevenue = 52
    TransmissionRental = 53
    NetGenerationRevenue = 54
    NetCosttoLoad = 55
    NetReservesRevenue = 56
    NetRevenue = 57
    NetProfit = 58
    GenerationatRRN = 59
    ContractVolume = 60
    NetContractVolume = 61
    ContractSettlement = 62
    NetContractSettlement = 63
    NetPoolRevenue = 64
    ContractGeneration = 65
    ContractLoad = 66
    ContractCost = 67
    ContractRevenue = 68
    NetContractRevenue = 69
    ShadowGeneration = 70
    GeneratorMonopolyRent = 71
    StrategicShadowPrice = 72
    ConstrainedOnRevenue = 73
    ConstrainedOffRevenue = 74
    InstalledCapacity = 75
    AvailableCapacity = 76
    GeneratorFirmCapacity = 77
    CapacityBuilt = 78
    CapacityRetired = 79
    NetNewCapacity = 80
    CapacityRevenue = 81
    CapacityPrice = 82
    BuildCost = 83
    RetirementCost = 84
    AnnualizedBuildCost = 85
    TotalCost = 86
    LevelizedCost = 87
    ShadowCapacityBuilt = 88
    x = 89
    y = 90
    z = 91


class SystemOutConstraintsEnum(Enum):
    Activity = 1
    Slack = 2
    Violation = 3
    HoursBinding = 4
    RHS = 5
    Price = 6
    HoursActive = 7
    PenaltyCost = 8
    Rental = 9
    x = 10
    y = 11
    z = 12


class SystemOutContingenciesEnum(Enum):
    HoursBinding = 1
    ShadowPrice = 2
    x = 3
    y = 4
    z = 5


class SystemOutCournotsEnum(Enum):
    Elasticity = 1
    DemandIntercept = 2
    DemandSlope = 3
    PerfectCompetitionDemand = 4
    PerfectCompetitionProduction = 5
    PerfectCompetitionNetImport = 6
    PerfectCompetitionPrice = 7
    PerfectCompetitionProducerRevenue = 8
    PerfectCompetitionConsumerSurplus = 9
    PerfectCompetitionProducerSurplus = 10
    Demand = 11
    Production = 12
    NetImport = 13
    Price = 14
    ProducerRevenue = 15
    ConsumerSurplus = 16
    ProducerSurplus = 17


class SystemOutDecisionVariablesEnum(Enum):
    Value = 1
    ReducedCost = 2
    Cost = 3
    ObjectiveFunctionCoefficient = 4
    LowerBound = 5
    UpperBound = 6
    MinValue = 7
    MaxValue = 8
    x = 9
    y = 10
    z = 11


class SystemOutEmissionsEnum(Enum):
    Production = 1
    GrossProduction = 2
    Removal = 3
    RemovalCost = 4
    Abatement = 5
    AbatementCost = 6
    Generation = 7
    Intensity = 8
    Price = 9
    ShadowPrice = 10
    Cost = 11
    MaxProductionViolation = 12
    MaxProductionViolationCost = 13
    x = 14
    y = 15
    z = 16


class SystemOutFinancialContractsEnum(Enum):
    Quantity = 1
    FloorPrice = 2
    CapPrice = 3
    SettlementPrice = 4
    Shortfall = 5
    SettlementQuantity = 6
    Settlement = 7
    HoursActive = 8


class SystemOutFlowControlsEnum(Enum):
    Angle = 1
    MinAngle = 2
    MaxAngle = 3
    Flow = 4
    FlowBack = 5
    Impedance = 6
    HoursBinding = 7
    ShadowPrice = 8
    Rental = 9
    Penalty = 10
    UnitsBuilt = 11
    BuildCost = 12
    x = 13
    y = 14
    z = 15


class SystemOutFuelContractsEnum(Enum):
    Offtake = 1
    Cost = 2
    Price = 3
    TakeorPayPrice = 4
    ShadowPrice = 5
    TakeorPayShadowPrice = 6
    TakeorPayViolation = 7
    TakeorPayViolationCost = 8
    FOMCost = 9
    TotalCost = 10
    x = 11
    y = 12
    z = 13


class SystemOutFuelsEnum(Enum):
    Price = 1
    Tax = 2
    TotalPrice = 3
    TimeweightedPrice = 4
    Offtake = 5
    MaxOfftake = 6
    MinOfftake = 7
    MaxInventory = 8
    MinInventory = 9
    OpeningInventory = 10
    ClosingInventory = 11
    Delivery = 12
    Withdrawal = 13
    NetWithdrawal = 14
    Cost = 15
    TaxCost = 16
    DeliveryCost = 17
    InventoryCost = 18
    ReservationCost = 19
    WithdrawalCost = 20
    TotalCost = 21
    ShadowPrice = 22
    Generation = 23
    AverageHeatRate = 24
    InstalledCapacity = 25
    FOMCost = 26
    x = 27
    y = 28
    z = 29


class SystemOutGasBasinsEnum(Enum):
    InitialVolume = 1
    EndVolume = 2
    Production = 3
    ProductionCost = 4
    FOMCost = 5
    FixedCosts = 6
    ShadowPrice = 7
    Units = 8
    UnitsBuilt = 9
    BuildCost = 10
    x = 11
    y = 12
    z = 13


class SystemOutGasContractsEnum(Enum):
    Production = 1
    Cost = 2
    Price = 3
    ShadowPrice = 4
    TotalCost = 5
    TakeorPayPrice = 6
    TakeorPayShadowPrice = 7
    TakeorPayViolation = 8
    TakeorPayViolationCost = 9
    x = 10
    y = 11
    z = 12


class SystemOutGasDemandsEnum(Enum):
    Demand = 1
    ShortageHours = 2
    Shortage = 3
    ShortageCost = 4
    ExcessHours = 5
    Excess = 6
    ExcessCost = 7
    NetDemand = 8
    Cost = 9
    PricePaid = 10
    BidQuantity = 11
    BidPrice = 12
    BidCleared = 13
    ClearedBidPrice = 14
    ClearedBidValue = 15
    x = 16
    y = 17
    z = 18


class SystemOutGasFieldsEnum(Enum):
    InitialVolume = 1
    EndVolume = 2
    Production = 3
    ProductionCost = 4
    FOMCost = 5
    FixedCosts = 6
    ShadowPrice = 7
    Units = 8
    UnitsBuilt = 9
    BuildCost = 10
    x = 11
    y = 12
    z = 13


class SystemOutGasNodesEnum(Enum):
    Production = 1
    Demand = 2
    Flow = 3
    Imports = 4
    Exports = 5
    NetInterchange = 6
    NetMarketSales = 7
    InitialVolume = 8
    EndVolume = 9
    ProductionCost = 10
    ShortageHours = 11
    Shortage = 12
    ShortageCost = 13
    ExcessHours = 14
    Excess = 15
    ExcessCost = 16
    ShadowPrice = 17
    Price = 18
    FOMCost = 19
    FixedCosts = 20
    Units = 21
    UnitsBuilt = 22
    BuildCost = 23
    UnitsRetired = 24
    RetirementCost = 25
    x = 26
    y = 27
    z = 28


class SystemOutGasPipelinesEnum(Enum):
    Flow = 1
    HoursCongested = 2
    HoursCongestedBack = 3
    MaxVolume = 4
    MinVolume = 5
    InitialVolume = 6
    EndVolume = 7
    VolumeImbalance = 8
    ImbalanceCost = 9
    ProductionCost = 10
    FOMCost = 11
    FixedCosts = 12
    UnitsOut = 13
    MaintenanceHours = 14
    ForcedOutageHours = 15
    ServiceFactor = 16
    Units = 17
    UnitsBuilt = 18
    BuildCost = 19
    UnitsRetired = 20
    RetirementCost = 21
    x = 22
    y = 23
    z = 24


class SystemOutGasPlantsEnum(Enum):
    RawGas = 1
    Production = 2
    ProductionCost = 3
    Consumption = 4
    EnergyConsumption = 5
    VOMCost = 6
    FOMCost = 7
    FixedCosts = 8
    SRMC = 9
    Units = 10
    UnitsBuilt = 11
    BuildCost = 12
    UnitsRetired = 13
    RetirementCost = 14
    x = 15
    y = 16
    z = 17


class SystemOutGasStoragesEnum(Enum):
    MaxVolume = 1
    MinVolume = 2
    InitialVolume = 3
    EndVolume = 4
    WorkingVolume = 5
    Utilization = 6
    WorkingUtilization = 7
    AverageUtilization = 8
    AverageWorkingUtilization = 9
    Withdrawal = 10
    Injection = 11
    NetWithdrawal = 12
    WithdrawalCost = 13
    InjectionCost = 14
    ProductionCost = 15
    ShadowPrice = 16
    FOMCost = 17
    FixedCosts = 18
    Units = 19
    UnitsBuilt = 20
    BuildCost = 21
    UnitsRetired = 22
    RetirementCost = 23
    x = 24
    y = 25
    z = 26


class SystemOutGasTransportsEnum(Enum):
    Imports = 1
    Exports = 2
    Losses = 3
    ContractImports = 4
    SpotImports = 5
    ShippingCost = 6
    x = 7
    y = 8
    z = 9


class SystemOutGasZonesEnum(Enum):
    Production = 1
    Demand = 2
    Imports = 3
    Exports = 4
    NetInterchange = 5
    InitialVolume = 6
    EndVolume = 7
    ShortageHours = 8
    Shortage = 9
    ShortageCost = 10
    ExcessHours = 11
    Excess = 12
    ExcessCost = 13
    NetDemand = 14
    Cost = 15
    PricePaid = 16
    x = 17
    y = 18
    z = 19


class SystemOutGeneratorsEnum(Enum):
    Generation = 1
    MinGeneration = 2
    MaxGeneration = 3
    UnitsGenerating = 4
    UnitsStarted = 5
    UnitsShutdown = 6
    DispatchableCapacity = 7
    UndispatchedCapacity = 8
    OperatingHours = 9
    HoursUp = 10
    HoursDown = 11
    CapacityFactor = 12
    FuelOfftake = 13
    StartFuelOfftake = 14
    WasteHeat = 15
    NoCostCapacity = 16
    HoursCurtailed = 17
    CapacityCurtailed = 18
    CurtailmentFactor = 19
    Ramp = 20
    RampUp = 21
    MinutesofRampUp = 22
    RampUpCost = 23
    RampUpPrice = 24
    RampDown = 25
    MinutesofRampDown = 26
    RampDownCost = 27
    RampDownPrice = 28
    RampUpViolationHours = 29
    RampDownViolationHours = 30
    RampUpViolation = 31
    RampDownViolation = 32
    RampUpViolationCost = 33
    RampDownViolationCost = 34
    FixedLoadGeneration = 35
    FixedLoadViolation = 36
    FixedLoadViolationHours = 37
    FixedLoadViolationCost = 38
    MinLoadGeneration = 39
    MinLoadViolation = 40
    MinLoadViolationHours = 41
    MinLoadViolationCost = 42
    MaxEnergyViolation = 43
    MaxEnergyViolationCost = 44
    MinEnergyViolation = 45
    MinEnergyViolationCost = 46
    MaxStartsViolation = 47
    MaxStartsViolationCost = 48
    RaiseReserve = 49
    LowerReserve = 50
    RegulationRaiseReserve = 51
    RegulationLowerReserve = 52
    ReplacementReserve = 53
    FlexibilityUp = 54
    FlexibilityDown = 55
    RampFlexibilityUp = 56
    RampFlexibilityDown = 57
    HoursatMinimum = 58
    InflexibleGeneration = 59
    AuxiliaryUse = 60
    GenerationSentOut = 61
    UnitsPumping = 62
    PumpUnitsStarted = 63
    PumpLoad = 64
    PumpOperatingHours = 65
    NetGeneration = 66
    FixedPumpLoad = 67
    FixedPumpLoadViolation = 68
    FixedPumpLoadViolationHours = 69
    FixedPumpLoadViolationCost = 70
    WaterRelease = 71
    WaterPumped = 72
    UnitsSyncCond = 73
    SyncCondLoad = 74
    SyncCondOperatingHours = 75
    FuelPrice = 76
    FuelCost = 77
    FuelTransportCost = 78
    FuelTransitionCost = 79
    VOMCharge = 80
    VOMCost = 81
    UoSCost = 82
    PumpCost = 83
    SyncCondCost = 84
    ReservesVOMCost = 85
    ReservesCost = 86
    GenerationCost = 87
    StartShutdownCost = 88
    StartShutdownPenaltyCost = 89
    StartFuelCost = 90
    EmissionsCost = 91
    AbatementCost = 92
    TotalGenerationCost = 93
    TotalSystemCost = 94
    FOMCost = 95
    EquityCost = 96
    DebtCost = 97
    FixedCosts = 98
    HeatRate = 99
    MarginalHeatRate = 100
    AverageHeatRate = 101
    Efficiency = 102
    MarginalFuelCost = 103
    SRMC = 104
    AverageCost = 105
    AverageTotalCost = 106
    OfferBase = 107
    OfferNoLoadCost = 108
    OfferQuantity = 109
    OfferPrice = 110
    CostPrice = 111
    Markup = 112
    BidCostMarkup = 113
    OfferCleared = 114
    ClearedOfferPrice = 115
    ClearedOfferCost = 116
    PriceReceived = 117
    PumpBidBase = 118
    PumpBidQuantity = 119
    PumpBidPrice = 120
    PumpBidCleared = 121
    ClearedPumpBidPrice = 122
    ClearedPumpBidCost = 123
    PumpPricePaid = 124
    SyncCondPricePaid = 125
    ClearedReserveOfferCost = 126
    SparkSpread = 127
    CleanSparkSpread = 128
    PoolRevenue = 129
    ReservesRevenue = 130
    NetReservesRevenue = 131
    HeatMarketRevenue = 132
    NetRevenue = 133
    NetProfit = 134
    ShadowGeneration = 135
    ShadowPoolRevenue = 136
    ShadowPriceReceived = 137
    MonopolyRent = 138
    StrategicShadowPrice = 139
    ScheduledGeneration = 140
    ScheduledRevenue = 141
    ConstrainedOnRevenue = 142
    ConstrainedOffRevenue = 143
    ScheduledGenerationCost = 144
    ScheduledOfferCost = 145
    ScheduledStartShutdownCost = 146
    CHPGeneration = 147
    CondenseModeGeneration = 148
    HeatProduction = 149
    CHPHeatProduction = 150
    BoilerHeatProduction = 151
    HeatFuelOfftake = 152
    CHPPowerFuelOfftake = 153
    CHPHeatFuelOfftake = 154
    CHPHeatSurrogateFuelOfftake = 155
    BoilerFuelOfftake = 156
    HeatProductionCost = 157
    HeatRevenue = 158
    MaxHeat = 159
    MinHeat = 160
    OpeningHeat = 161
    ClosingHeat = 162
    HeatWithdrawal = 163
    HeatInjection = 164
    NetHeatWithdrawal = 165
    HeatLoss = 166
    HeatWithdrawalCost = 167
    HeatInjectionCost = 168
    HeatShadowPrice = 169
    WaterOfftake = 170
    WaterConsumption = 171
    WaterCost = 172
    WaterPricePaid = 173
    Units = 174
    MaxCapacity = 175
    InstalledCapacity = 176
    Rating = 177
    RawRating = 178
    RatedCapacity = 179
    FirmCapacity = 180
    CapacityReserves = 181
    UnitsOut = 182
    Maintenance = 183
    DiscreteMaintenance = 184
    DistributedMaintenance = 185
    MaintenanceHours = 186
    MaintenanceRate = 187
    ForcedOutage = 188
    ForcedOutageHours = 189
    ForcedOutageRate = 190
    OperatingorForcedOutageHours = 191
    AvailableCapacity = 192
    ServiceFactor = 193
    UnitsBuilt = 194
    UnitsRetired = 195
    CapacityBuilt = 196
    CapacityRetired = 197
    NetNewCapacity = 198
    CapacityPrice = 199
    CapacityRevenue = 200
    BuildCost = 201
    AnnualizedBuildCost = 202
    TotalCost = 203
    LevelizedCost = 204
    Age = 205
    RetirementCost = 206
    ShadowCapacityBuilt = 207
    x = 208
    y = 209
    z = 210


class SystemOutHeatNodesEnum(Enum):
    HeatWithdrawal = 1
    HeatInjection = 2
    x = 3
    y = 4
    z = 5


class SystemOutHeatPlantsEnum(Enum):
    HeatProduction = 1
    HeatProductionCost = 2
    VOMCost = 3
    StartShutdownCost = 4
    StartFuelCost = 5
    FuelOfftake = 6
    StartFuelOfftake = 7
    ElectricalUsage = 8
    UnitsProducingHeat = 9
    Ramp = 10
    RampUp = 11
    RampDown = 12
    OperatingHours = 13
    Efficiency = 14
    MarginalHeatRate = 15
    AverageHeatRate = 16
    SRMC = 17
    FOMCost = 18
    InstalledCapacity = 19
    UnitsBuilt = 20
    BuildCost = 21
    UnitsRetired = 22
    RetirementCost = 23
    x = 24
    y = 25
    z = 26


class SystemOutHubsEnum(Enum):
    Price = 1
    CustomerLoad = 2
    NetGeneration = 3
    CosttoLoad = 4
    GeneratorPoolRevenue = 5
    LoadweightedPrice = 6
    GenerationweightedPrice = 7
    MarginalLossCharge = 8
    EnergyCharge = 9
    CongestionCharge = 10
    x = 11
    y = 12
    z = 13


class SystemOutInterfacesEnum(Enum):
    Flow = 1
    FlowBack = 2
    NetFlow = 3
    ExportLimit = 4
    ImportLimit = 5
    Loading = 6
    LoadingBack = 7
    HoursCongested = 8
    HoursCongestedBack = 9
    ShadowPrice = 10
    ShadowPriceBack = 11
    Rental = 12
    Violation = 13
    ViolationBack = 14
    Ramp = 15
    RampCost = 16
    MaxFlow = 17
    MinFlow = 18
    FixedFlow = 19
    FixedFlowViolation = 20
    FixedFlowViolationHours = 21
    FixedFlowViolationCost = 22
    OfferBase = 23
    OfferQuantity = 24
    OfferPrice = 25
    OfferQuantityBack = 26
    OfferPriceBack = 27
    OfferCleared = 28
    OfferClearedBack = 29
    ClearedOfferPrice = 30
    ClearedOfferCost = 31
    AvailableTransferCapability = 32
    AvailableTransferCapabilityBack = 33
    FirmCapacity = 34
    CapacityReserves = 35
    CapacityBuilt = 36
    ExpansionCost = 37
    x = 38
    y = 39
    z = 40


class SystemOutLinesEnum(Enum):
    Flow = 1
    FlowBack = 2
    NetFlow = 3
    ExportLimit = 4
    ImportLimit = 5
    Loading = 6
    LoadingBack = 7
    HoursCongested = 8
    HoursCongestedBack = 9
    ShadowPrice = 10
    ShadowPriceBack = 11
    ViolationHours = 12
    ViolationBackHours = 13
    Violation = 14
    ViolationBack = 15
    ViolationCost = 16
    ViolationCostBack = 17
    Ramp = 18
    RampCost = 19
    MaxFlow = 20
    MinFlow = 21
    FixedFlow = 22
    FixedFlowViolation = 23
    FixedFlowViolationHours = 24
    FixedFlowViolationCost = 25
    ExportCost = 26
    ImportCost = 27
    ExportRevenue = 28
    ImportRevenue = 29
    Rental = 30
    RentalBack = 31
    WheelingCost = 32
    WheelingCostBack = 33
    Loss = 34
    LossBack = 35
    MarginalLoss = 36
    MarginalLossFactor = 37
    Voltage = 38
    OfferBase = 39
    OfferQuantity = 40
    OfferPrice = 41
    OfferQuantityBack = 42
    OfferPriceBack = 43
    OfferCleared = 44
    OfferClearedBack = 45
    ClearedOfferPrice = 46
    ClearedOfferCost = 47
    FOMCost = 48
    EquityCost = 49
    DebtCost = 50
    NetProfit = 51
    Units = 52
    FirmCapacity = 53
    CapacityReserves = 54
    UnitsOut = 55
    Maintenance = 56
    MaintenanceBack = 57
    DiscreteMaintenance = 58
    DiscreteMaintenanceBack = 59
    DistributedMaintenance = 60
    DistributedMaintenanceBack = 61
    MaintenanceRate = 62
    ForcedOutage = 63
    ForcedOutageRate = 64
    ServiceFactor = 65
    AvailableTransferCapability = 66
    AvailableTransferCapabilityBack = 67
    UnitsBuilt = 68
    UnitsRetired = 69
    ExportCapacityBuilt = 70
    ImportCapacityBuilt = 71
    ExportCapacityRetired = 72
    ImportCapacityRetired = 73
    BuildCost = 74
    RetirementCost = 75
    x = 76
    y = 77
    z = 78


class SystemOutMaintenancesEnum(Enum):
    StartDate = 1
    HoursActive = 2
    Duration = 3
    Cost = 4
    Crew = 5
    Equipment = 6
    Outage = 7
    PenaltyCost = 8
    x = 9
    y = 10
    z = 11


class SystemOutMarketsEnum(Enum):
    Sales = 1
    Purchases = 2
    NetSales = 3
    NetPurchases = 4
    Price = 5
    Revenue = 6
    Cost = 7
    NetRevenue = 8
    NetCost = 9
    TotalCost = 10
    PriceReceived = 11
    PricePaid = 12
    NaturalRevenue = 13
    NaturalCost = 14
    FirmCapacity = 15
    LoadObligation = 16
    x = 17
    y = 18
    z = 19


class SystemOutNodesEnum(Enum):
    Load = 1
    NativeLoad = 2
    FixedLoad = 3
    FixedGeneration = 4
    Generation = 5
    GeneratorAuxiliaryUse = 6
    GenerationSentOut = 7
    PumpLoad = 8
    PurchaserLoad = 9
    NetContractLoad = 10
    NetMarketSales = 11
    DemandCurtailed = 12
    DSPBidQuantity = 13
    DSPBidPrice = 14
    DSPBidCleared = 15
    ClearedDSPBidPrice = 16
    ClearedDSPBidCost = 17
    CustomerLoad = 18
    Imports = 19
    Exports = 20
    NetDCExport = 21
    NetInjection = 22
    UnservedEnergy = 23
    DumpEnergy = 24
    Losses = 25
    Flow = 26
    Price = 27
    EnergyCharge = 28
    CongestionCharge = 29
    MarginalLossCharge = 30
    MarginalLossFactor = 31
    Voltage = 32
    PhaseAngle = 33
    PeakLoad = 34
    GenerationCapacity = 35
    FirmGenerationCapacity = 36
    CurtailableLoad = 37
    ContractGenerationCapacity = 38
    ContractLoadObligation = 39
    ImportCapacity = 40
    ExportCapacity = 41
    NetCapacityInterchange = 42
    MinCapacityReserves = 43
    CapacityReserves = 44
    MinLoad = 45
    DiscreteMaintenance = 46
    DistributedMaintenance = 47
    MaintenanceFactor = 48
    EENS = 49
    EDNS = 50
    LOLE = 51
    LOLP = 52
    x = 53
    y = 54
    z = 55


class SystemOutPhysicalContractsEnum(Enum):
    Generation = 1
    Load = 2
    NetGeneration = 3
    CapacityFactor = 4
    LoadFactor = 5
    PriceReceived = 6
    PricePaid = 7
    GenerationCost = 8
    LoadRevenue = 9
    NetGenerationCost = 10
    GenerationRevenue = 11
    CosttoLoad = 12
    NetGenerationRevenue = 13
    FixedCost = 14
    GenerationCapacity = 15
    LoadObligation = 16
    x = 17
    y = 18
    z = 19


class SystemOutPurchasersEnum(Enum):
    Load = 1
    PricePaid = 2
    CosttoLoad = 3
    BidQuantity = 4
    BidPrice = 5
    BidCleared = 6
    ClearedBidPrice = 7
    ClearedBidValue = 8
    LoadFactor = 9
    MaxEnergyViolation = 10
    MaxEnergyViolationCost = 11
    MinEnergyViolation = 12
    MinEnergyViolationCost = 13
    ClearedReserveOfferCost = 14
    ReservesRevenue = 15
    LoadObligation = 16
    x = 17
    y = 18
    z = 19


class SystemOutRSIsEnum(Enum):
    RSI = 1
    UtilityGeneration = 2
    UtilityAvailableCapacity = 3
    NonUtilityGeneration = 4
    NonUtilityAvailableCapacity = 5
    NonUtilityContractVolume = 6
    TotalInternalCapacity = 7
    TotalImportCapacity = 8
    TotalSupplyCapacity = 9
    LargestSuppliersCapacity = 10
    ImportCapacity = 11
    Demand = 12
    LernerIndex = 13
    BoundedLernerIndex = 14
    BidCostMarkup = 15
    PriceCostMarkup = 16
    LoadUnhedged = 17
    LoadCapacityRatio = 18
    CapacityFactor = 19
    LoadVariation = 20
    SummerPeriod = 21
    PeakPeriod = 22


class SystemOutRegionsEnum(Enum):
    Load = 1
    NativeLoad = 2
    FixedLoad = 3
    FixedGeneration = 4
    Generation = 5
    GeneratorAuxiliaryUse = 6
    GenerationSentOut = 7
    ContractGeneration = 8
    ContractLoad = 9
    NetContractLoad = 10
    NetMarketSales = 11
    PumpLoad = 12
    NetGeneration = 13
    PurchaserLoad = 14
    CustomerLoad = 15
    Imports = 16
    Exports = 17
    NetInterchange = 18
    TransmissionLosses = 19
    DemandCurtailed = 20
    UnservedEnergyHours = 21
    UnservedEnergy = 22
    CostofUnservedEnergy = 23
    DumpEnergyHours = 24
    DumpEnergy = 25
    CostofDumpEnergy = 26
    NoCostGenerationCapacity = 27
    HoursGenerationCurtailed = 28
    GenerationCapacityCurtailed = 29
    FlexibilityUp = 30
    FlexibilityDown = 31
    RampFlexibilityUp = 32
    RampFlexibilityDown = 33
    HoursatMinimum = 34
    InflexibleGeneration = 35
    GenerationCost = 36
    GeneratorPumpCost = 37
    GeneratorStartShutdownCost = 38
    EmissionsCost = 39
    AbatementCost = 40
    TotalGenerationCost = 41
    TotalSystemCost = 42
    GeneratorFOMCost = 43
    TotalFixedCosts = 44
    SRMC = 45
    Price = 46
    Uplift = 47
    PriceCostMarkup = 48
    TimeweightedPrice = 49
    LoadweightedPrice = 50
    GenerationweightedPrice = 51
    CosttoLoad = 52
    GeneratorPoolRevenue = 53
    TransmissionRental = 54
    SettlementSurplus = 55
    InterregionalTransmissionLosses = 56
    IntraregionalTransmissionLosses = 57
    ContractVolume = 58
    ContractSettlement = 59
    NetCosttoLoad = 60
    DSPBidQuantity = 61
    DSPBidPrice = 62
    DSPBidCleared = 63
    ClearedDSPBidPrice = 64
    ClearedDSPBidCost = 65
    CostofCurtailment = 66
    GeneratorNetPoolRevenue = 67
    ClearedOfferCost = 68
    ClearedReserveOfferCost = 69
    GeneratorNetRevenue = 70
    ShadowLoad = 71
    ShadowGeneration = 72
    ShadowPrice = 73
    ShadowCosttoLoad = 74
    GeneratorMonopolyRent = 75
    UtilityMonopolyRent = 76
    NonUtilityMonopolyRent = 77
    UtilityContractSettlement = 78
    NonUtilityContractSettlement = 79
    UtilityNetRevenue = 80
    NonUtilityNetRevenue = 81
    ConstrainedOnCost = 82
    ConstrainedOffCost = 83
    GeneratorNetProfit = 84
    NetMarketProfit = 85
    ExportCost = 86
    ImportRevenue = 87
    NetCostofExports = 88
    WheelingRevenue = 89
    WheelingCost = 90
    IntraregionalTransmissionRental = 91
    InterregionalTransmissionRental = 92
    TransmissionControlRental = 93
    PeakLoad = 94
    GenerationCapacity = 95
    FirmGenerationCapacity = 96
    CurtailableLoad = 97
    ContractGenerationCapacity = 98
    ContractLoadObligation = 99
    ImportCapacity = 100
    ExportCapacity = 101
    NetCapacityInterchange = 102
    MinCapacityReserves = 103
    MaxCapacityReserves = 104
    CapacityReserves = 105
    MaxCapacityReserveMargin = 106
    MinCapacityReserveMargin = 107
    CapacityReserveMargin = 108
    MinLoad = 109
    Maintenance = 110
    ForcedOutage = 111
    AvailableCapacity = 112
    AvailableCapacityReserves = 113
    AvailableCapacityMargin = 114
    DispatchableCapacity = 115
    UndispatchedCapacity = 116
    DiscreteMaintenance = 117
    DistributedMaintenance = 118
    MaintenanceFactor = 119
    EENS = 120
    EDNS = 121
    LOLE = 122
    LOLP = 123
    MultiareaLOLE = 124
    MultiareaLOLP = 125
    PlanningPeakLoad = 126
    GenerationCapacityBuilt = 127
    GenerationCapacityRetired = 128
    ImportCapacityBuilt = 129
    ImportCapacityRetired = 130
    ExportCapacityBuilt = 131
    ExportCapacityRetired = 132
    CapacityShortage = 133
    CapacityExcess = 134
    CapacityShadowPrice = 135
    LRMC = 136
    CapacityPayments = 137
    CapacityPrice = 138
    CapacityShortageCost = 139
    CapacityExcessCost = 140
    TotalGeneratorRevenue = 141
    GeneratorBuildCost = 142
    GeneratorRetirementCost = 143
    TransmissionBuildCost = 144
    TransmissionRetirementCost = 145
    AnnualizedBuildCost = 146
    TotalCost = 147
    LevelizedCost = 148
    ShadowGenerationCapacityBuilt = 149
    x = 150
    y = 151
    z = 152


class SystemOutReservesEnum(Enum):
    Provision = 1
    Risk = 2
    Shortage = 3
    ShortageHours = 4
    ShortageCost = 5
    ClearedOfferPrice = 6
    ClearedOfferCost = 7
    Cost = 8
    Price = 9
    TimeweightedPrice = 10
    AvailableResponse = 11
    x = 12
    y = 13
    z = 14


class SystemOutStoragesEnum(Enum):
    MaxVolume = 1
    MinVolume = 2
    InitialVolume = 3
    EndVolume = 4
    InitialLevel = 5
    EndLevel = 6
    HoursFull = 7
    WorkingVolume = 8
    Utilization = 9
    WorkingUtilization = 10
    AverageUtilization = 11
    AverageWorkingUtilization = 12
    Inflow = 13
    Release = 14
    NaturalInflow = 15
    GeneratorRelease = 16
    DownstreamRelease = 17
    Spill = 18
    InflowRate = 19
    ReleaseRate = 20
    NaturalInflowRate = 21
    GeneratorReleaseRate = 22
    DownstreamReleaseRate = 23
    SpillRate = 24
    Loss = 25
    ShadowPrice = 26
    MarginalValue = 27
    MarginalCost = 28
    PotentialEnergy = 29
    Generation = 30
    PumpLoad = 31
    Efficiency = 32
    MinReleaseViolation = 33
    MinReleaseViolationHours = 34
    MinReleaseViolationCost = 35
    MaxReleaseViolation = 36
    MaxReleaseViolationHours = 37
    MaxReleaseViolationCost = 38
    Ramp = 39
    RampPrice = 40
    RampViolation = 41
    RampViolationHours = 42
    RampViolationCost = 43
    TargetViolation = 44
    TargetViolationCost = 45
    NonphysicalInflow = 46
    NonphysicalSpill = 47
    x = 48
    y = 49
    z = 50


class SystemOutTimeslicesEnum(Enum):
    HoursIncluded = 1


class SystemOutTransformersEnum(Enum):
    Flow = 1
    FlowBack = 2
    ExportLimit = 3
    ImportLimit = 4
    Loading = 5
    LoadingBack = 6
    Loss = 7
    LossBack = 8
    Voltage = 9
    HoursCongested = 10
    ShadowPrice = 11
    ViolationHours = 12
    ViolationBackHours = 13
    Violation = 14
    ViolationBack = 15
    ViolationCost = 16
    ViolationCostBack = 17
    MaxFlow = 18
    MinFlow = 19
    ExportCost = 20
    ImportCost = 21
    ExportRevenue = 22
    ImportRevenue = 23
    Rental = 24
    RentalBack = 25
    AvailableTransferCapability = 26
    AvailableTransferCapabilityBack = 27
    x = 28
    y = 29
    z = 30


class SystemOutTransmissionRightsEnum(Enum):
    Quantity = 1
    Settlement = 2
    NetProfit = 3
    SourcePrice = 4
    SourceEnergyCharge = 5
    SourceCongestionCharge = 6
    SourceLossCharge = 7
    SinkPrice = 8
    SinkEnergyCharge = 9
    SinkCongestionCharge = 10
    SinkLossCharge = 11
    PriceDelta = 12


class SystemOutVariablesEnum(Enum):
    ExpectedValue = 1
    RawValue = 2
    Value = 3
    Error = 4
    Volatility = 5


class SystemOutWaterDemandsEnum(Enum):
    Demand = 1
    ShortageHours = 2
    Shortage = 3
    ShortageCost = 4
    ExcessHours = 5
    Excess = 6
    ExcessCost = 7
    NetDemand = 8
    Cost = 9
    PricePaid = 10
    BidQuantity = 11
    BidPrice = 12
    BidCleared = 13
    ClearedBidPrice = 14
    ClearedBidValue = 15
    x = 16
    y = 17
    z = 18


class SystemOutWaterNodesEnum(Enum):
    Production = 1
    Demand = 2
    Flow = 3
    Imports = 4
    Exports = 5
    NetInterchange = 6
    InitialVolume = 7
    EndVolume = 8
    ProductionCost = 9
    ShortageHours = 10
    Shortage = 11
    ShortageCost = 12
    ExcessHours = 13
    Excess = 14
    ExcessCost = 15
    ShadowPrice = 16
    FOMCost = 17
    FixedCosts = 18
    EnergyConsumption = 19
    Units = 20
    UnitsBuilt = 21
    BuildCost = 22
    UnitsRetired = 23
    RetirementCost = 24
    x = 25
    y = 26
    z = 27


class SystemOutWaterPipelinesEnum(Enum):
    Flow = 1
    HoursCongested = 2
    HoursCongestedBack = 3
    ProductionCost = 4
    FOMCost = 5
    FixedCosts = 6
    EnergyConsumption = 7
    UnitsOut = 8
    MaintenanceHours = 9
    ForcedOutageHours = 10
    ServiceFactor = 11
    Units = 12
    UnitsBuilt = 13
    BuildCost = 14
    UnitsRetired = 15
    RetirementCost = 16
    x = 17
    y = 18
    z = 19


class SystemOutWaterPlantsEnum(Enum):
    RawWater = 1
    Production = 2
    ProductionCost = 3
    VOMCost = 4
    FOMCost = 5
    FixedCosts = 6
    SRMC = 7
    EnergyConsumption = 8
    ElectricLoad = 9
    HeatLoad = 10
    AuxiliaryUse = 11
    Units = 12
    UnitsBuilt = 13
    BuildCost = 14
    x = 15
    y = 16
    z = 17


class SystemOutWaterStoragesEnum(Enum):
    MaxVolume = 1
    MinVolume = 2
    InitialVolume = 3
    EndVolume = 4
    WorkingVolume = 5
    Utilization = 6
    WorkingUtilization = 7
    AverageUtilization = 8
    AverageWorkingUtilization = 9
    Withdrawal = 10
    Injection = 11
    NetWithdrawal = 12
    ShadowPrice = 13
    FOMCost = 14
    FixedCosts = 15
    Units = 16
    UnitsBuilt = 17
    BuildCost = 18
    UnitsRetired = 19
    RetirementCost = 20
    x = 21
    y = 22
    z = 23


class SystemOutWaterZonesEnum(Enum):
    Production = 1
    Demand = 2
    Imports = 3
    Exports = 4
    NetInterchange = 5
    ShortageHours = 6
    Shortage = 7
    ShortageCost = 8
    ExcessHours = 9
    Excess = 10
    ExcessCost = 11
    NetDemand = 12
    Cost = 13
    PricePaid = 14
    x = 15
    y = 16
    z = 17


class SystemOutWaterwaysEnum(Enum):
    Flow = 1
    MaxFlow = 2
    MinFlow = 3
    HoursFlowing = 4
    ShadowPrice = 5
    MaxFlowViolationHours = 6
    MaxFlowViolation = 7
    MaxFlowViolationCost = 8
    MinFlowViolationHours = 9
    MinFlowViolation = 10
    MinFlowViolationCost = 11
    Ramp = 12
    MaxRamp = 13
    RampViolationHours = 14
    RampViolation = 15
    RampViolationCost = 16
    x = 17
    y = 18
    z = 19


class SystemOutZonesEnum(Enum):
    Load = 1
    NativeLoad = 2
    FixedLoad = 3
    FixedGeneration = 4
    Generation = 5
    GeneratorAuxiliaryUse = 6
    GenerationSentOut = 7
    DemandCurtailed = 8
    ContractGeneration = 9
    ContractLoad = 10
    NetContractLoad = 11
    NetMarketSales = 12
    PumpLoad = 13
    NetGeneration = 14
    PurchaserLoad = 15
    CustomerLoad = 16
    Imports = 17
    Exports = 18
    NetInterchange = 19
    TransmissionLosses = 20
    UnservedEnergyHours = 21
    UnservedEnergy = 22
    CostofUnservedEnergy = 23
    DumpEnergyHours = 24
    DumpEnergy = 25
    CostofDumpEnergy = 26
    NoCostGenerationCapacity = 27
    HoursGenerationCurtailed = 28
    GenerationCapacityCurtailed = 29
    FlexibilityUp = 30
    FlexibilityDown = 31
    RampFlexibilityUp = 32
    RampFlexibilityDown = 33
    HoursatMinimum = 34
    InflexibleGeneration = 35
    GenerationCost = 36
    GeneratorPumpCost = 37
    GeneratorStartShutdownCost = 38
    EmissionsCost = 39
    AbatementCost = 40
    TotalGenerationCost = 41
    TotalSystemCost = 42
    GeneratorFOMCost = 43
    TotalFixedCosts = 44
    SRMC = 45
    Price = 46
    TimeweightedPrice = 47
    LoadweightedPrice = 48
    GenerationweightedPrice = 49
    EnergyCharge = 50
    CongestionCharge = 51
    MarginalLossCharge = 52
    MarginalLossFactor = 53
    CosttoLoad = 54
    GeneratorPoolRevenue = 55
    TransmissionRental = 56
    SettlementSurplus = 57
    CostofCurtailment = 58
    ClearedOfferCost = 59
    ClearedReserveOfferCost = 60
    GeneratorNetRevenue = 61
    GeneratorNetProfit = 62
    NetMarketProfit = 63
    ExportCost = 64
    ImportRevenue = 65
    NetCostofExports = 66
    WheelingRevenue = 67
    WheelingCost = 68
    PeakLoad = 69
    GenerationCapacity = 70
    FirmGenerationCapacity = 71
    CurtailableLoad = 72
    ContractGenerationCapacity = 73
    ContractLoadObligation = 74
    ImportCapacity = 75
    ExportCapacity = 76
    NetCapacityInterchange = 77
    MinCapacityReserves = 78
    MaxCapacityReserves = 79
    CapacityReserves = 80
    MaxCapacityReserveMargin = 81
    MinCapacityReserveMargin = 82
    CapacityReserveMargin = 83
    MinLoad = 84
    AvailableCapacity = 85
    AvailableCapacityReserves = 86
    AvailableCapacityMargin = 87
    DispatchableCapacity = 88
    UndispatchedCapacity = 89
    DiscreteMaintenance = 90
    DistributedMaintenance = 91
    MaintenanceFactor = 92
    EENS = 93
    EDNS = 94
    LOLE = 95
    LOLP = 96
    MultiareaLOLE = 97
    MultiareaLOLP = 98
    PlanningPeakLoad = 99
    GenerationCapacityBuilt = 100
    GenerationCapacityRetired = 101
    ImportCapacityBuilt = 102
    ImportCapacityRetired = 103
    ExportCapacityBuilt = 104
    ExportCapacityRetired = 105
    CapacityShortage = 106
    CapacityExcess = 107
    CapacityShadowPrice = 108
    LRMC = 109
    CapacityPayments = 110
    CapacityPrice = 111
    CapacityShortageCost = 112
    CapacityExcessCost = 113
    TotalGeneratorRevenue = 114
    GeneratorBuildCost = 115
    GeneratorRetirementCost = 116
    TransmissionBuildCost = 117
    TransmissionRetirementCost = 118
    AnnualizedBuildCost = 119
    TotalCost = 120
    LevelizedCost = 121
    x = 122
    y = 123
    z = 124


class SystemPhysicalContractsEnum(Enum):
    OfferQuantityFormat = 1
    PriceSetting = 2
    Units = 3
    MaxGeneration = 4
    MaxLoad = 5
    MinGeneration = 6
    MinLoad = 7
    OfferQuantity = 8
    OfferPrice = 9
    BidQuantity = 10
    BidPrice = 11
    FirmCapacity = 12
    LoadObligation = 13
    CapacityCharge = 14
    MaxGenerationUnits = 15
    MaxLoadUnits = 16
    MinGenerationUnits = 17
    MinLoadUnits = 18
    BuildNonanticipativity = 19
    x = 20
    y = 21
    z = 22


class SystemPowerStationsEnum(Enum):
    IsEnabled = 1


class SystemPurchasersEnum(Enum):
    BenefitFunctionShape = 1
    MaxBenefitFunctionTranches = 2
    InterruptibleLoadLogic = 3
    PriceSetting = 4
    Units = 5
    MinLoad = 6
    MaxLoad = 7
    FixedLoad = 8
    MaxRampDown = 9
    MaxRampUp = 10
    MaxEnergy = 11
    MinEnergy = 12
    MaxLoadFactor = 13
    MinLoadFactor = 14
    MaxEnergyPenalty = 15
    MinEnergyPenalty = 16
    MarginalLossFactor = 17
    BidQuantity = 18
    BidPrice = 19
    Tariff = 20
    DemandFnSlope = 21
    DemandFnIntercept = 22
    LoadObligation = 23
    x = 24
    y = 25
    z = 26


class SystemRSIsEnum(Enum):
    AllowNegativeMarkups = 1
    RSI = 2
    LernerIndex = 3
    BoundedLernerIndex = 4
    Intercept = 5
    RSICoefficient = 6
    RSIsquaredCoefficient = 7
    LoadUnhedgedCoefficient = 8
    RSIInverseCoefficient = 9
    LoadCoefficient = 10
    LoadCapacityRatioCoefficient = 11
    CapacityFactorCoefficient = 12
    LoadVariationCoefficient = 13
    SummerPeriodCoefficient = 14
    PeakPeriodCoefficient = 15
    AverageLoad = 16
    LernerIndextstatistic = 17
    LernerIndexStdDev = 18
    LernerIndexCalibrationFactor = 19
    MinLernerIndex = 20
    MaxLernerIndex = 21


class SystemRegionsEnum(Enum):
    GeneratorSettlementModel = 1
    LoadSettlementModel = 2
    UniformPricingPumpedStoragePriceSetting = 3
    UniformPricingRelaxTransmissionLimits = 4
    UniformPricingRelaxGenericConstraints = 5
    UniformPricingRelaxGeneratorConstraints = 6
    UniformPricingRelaxAncillaryServices = 7
    UpliftEnabled = 8
    UpliftCostBasis = 9
    UpliftCompatibility = 10
    UpliftAlpha = 11
    UpliftBeta = 12
    UpliftDelta = 13
    UpliftIncludeStartCost = 14
    UpliftIncludeNoLoadCost = 15
    UpliftDetectActiveMinStableLevelConstraints = 16
    UpliftDetectActiveRampConstraints = 17
    IncludeinMarginalUnit = 18
    IncludeinUplift = 19
    ConstraintPaymentsEnabled = 20
    ConstraintPaymentsCompatibility = 21
    LoadMeteringPoint = 22
    LoadIncludesLosses = 23
    AggregateTransmission = 24
    PoolType = 25
    MLFAdjustsOfferPrice = 26
    MLFAdjustsBidPrice = 27
    MLFAdjustsNoLoadCost = 28
    MLFAdjustsStartCost = 29
    IncludeinRegionSupply = 30
    TransmissionConstraintsEnabled = 31
    TransmissionConstraintVoltageThreshold = 32
    TransmissionInterfaceConstraintsEnabled = 33
    EnforceTransmissionLimitsOnLinesInInterfaces = 34
    TransmissionReportEnabled = 35
    TransmissionReportVoltageThreshold = 36
    TransmissionReportLinesInInterfaces = 37
    TransmissionReportInjectionandLoadNodes = 38
    ReportObjectsinRegion = 39
    WheelingMethod = 40
    Units = 41
    Load = 42
    LoadScalar = 43
    FixedLoad = 44
    FixedGeneration = 45
    VoLL = 46
    PriceofDumpEnergy = 47
    PriceCap = 48
    PriceFloor = 49
    Price = 50
    WheelingCharge = 51
    FixedCostScalar = 52
    Elasticity = 53
    ReferenceLoad = 54
    DSPBidQuantity = 55
    DSPBidPrice = 56
    IsStrategic = 57
    MaxMaintenance = 58
    MaintenanceFactor = 59
    PeakPeriod = 60
    FirmCapacityIncr = 61
    MinCapacityReserves = 62
    MaxCapacityReserves = 63
    MinCapacityReserveMargin = 64
    MaxCapacityReserveMargin = 65
    MinNativeCapacityReserves = 66
    MinNativeCapacityReserveMargin = 67
    CapacityShortagePrice = 68
    CapacityExcessPrice = 69
    CapacityPriceCap = 70
    CapacityPriceFloor = 71
    LOLPTarget = 72
    x = 73
    y = 74
    z = 75


class SystemReservesEnum(Enum):
    Type = 1
    MutuallyExclusive = 2
    DynamicRisk = 3
    CostAllocationModel = 4
    IsEnabled = 5
    IncludeinLTPlan = 6
    IncludeinMTSchedule = 7
    IncludeinSTSchedule = 8
    UnitCommitment = 9
    SharingEnabled = 10
    SharingLossesEnabled = 11
    MinProvision = 12
    StaticRisk = 13
    Timeframe = 14
    Duration = 15
    MaxProvision = 16
    RiskAdjustmentFactor = 17
    EnergyUsage = 18
    VoRS = 19
    PriceCap = 20
    PriceFloor = 21
    CutoffSize = 22
    Price = 23
    x = 24
    y = 25
    z = 26


class SystemStoragesEnum(Enum):
    Model = 1
    BalancePeriod = 2
    InternalVolumeScalar = 3
    EndEffectsMethod = 4
    RecyclePenalty = 5
    DecompositionMethod = 6
    DecompositionPenaltya = 7
    DecompositionPenaltyb = 8
    DecompositionPenaltyc = 9
    DecompositionPenaltyx = 10
    DecompositionBoundPenalty = 11
    EnforceBounds = 12
    SpillPenalty = 13
    NonphysicalInflowPenalty = 14
    NonphysicalSpillPenalty = 15
    Units = 16
    MaxVolume = 17
    InitialVolume = 18
    MinVolume = 19
    MaxLevel = 20
    InitialLevel = 21
    MinLevel = 22
    LowRefLevel = 23
    LowRefArea = 24
    HighRefLevel = 25
    HighRefArea = 26
    NaturalInflow = 27
    NaturalInflowIncr = 28
    NaturalInflowScalar = 29
    WaterValue = 30
    EnergyValue = 31
    WaterValuePoint = 32
    DownstreamEfficiency = 33
    LossRate = 34
    MinRelease = 35
    MaxRelease = 36
    MaxGeneratorRelease = 37
    MinReleasePenalty = 38
    MaxReleasePenalty = 39
    MaxSpill = 40
    MaxRamp = 41
    MaxRampPenalty = 42
    Target = 43
    TargetLevel = 44
    TargetPenalty = 45
    TrajectoryNonanticipativity = 46
    TrajectoryNonanticipativityVolume = 47
    TrajectoryNonanticipativityTime = 48
    x = 49
    y = 50
    z = 51


class SystemTimeslicesEnum(Enum):
    Include = 1


class SystemTransformersEnum(Enum):
    MustReport = 1
    EnforceLimits = 2
    FormulateUpfront = 3
    Units = 4
    Rating = 5
    OverloadRating = 6
    LimitPenalty = 7
    Resistance = 8
    Reactance = 9
    Susceptance = 10
    LossAllocation = 11
    FixedLoss = 12
    UnitsOut = 13
    x = 14
    y = 15
    z = 16


class SystemTransmissionRightsEnum(Enum):
    Type = 1
    SettlementModel = 2
    PricingMethod = 3
    Units = 4
    Quantity = 5
    RentalShare = 6
    RentalBackShare = 7
    Price = 8


class SystemVariablesEnum(Enum):
    RandomNumberSeed = 1
    SamplingMethod = 2
    SamplingFrequency = 3
    SamplingPeriodType = 4
    DistributionType = 5
    Condition = 6
    ConditionLogic = 7
    IncludeinLTPlan = 8
    IncludeinPASA = 9
    IncludeinMTSchedule = 10
    IncludeinSTSchedule = 11
    Profile = 12
    MinValue = 13
    MaxValue = 14
    Probability = 15
    ErrorStdDev = 16
    AbsErrorStdDev = 17
    MinValueStdDev = 18
    MaxValueStdDev = 19
    AutoCorrelation = 20
    MeanReversion = 21
    ARIMAalpha = 22
    ARIMAbeta = 23
    ARIMAd = 24
    JumpFrequency = 25
    JumpMagnitude = 26
    JumpErrorStdDev = 27
    GARCHalpha = 28
    GARCHbeta = 29
    GARCHomega = 30
    Lookupx = 31
    Lookupy = 32
    LookupUnit = 33
    Sampling = 34
    StepHourActiveFrom = 35
    StepHoursActive = 36
    CompoundIndex = 37


class SystemWaterDemandsEnum(Enum):
    Demand = 1
    ShortagePrice = 2
    ExcessPrice = 3
    BidQuantity = 4
    BidPrice = 5
    x = 6
    y = 7
    z = 8


class SystemWaterNodesEnum(Enum):
    ExpansionOptimality = 1
    Units = 2
    WaterSecurity = 3
    FOMCharge = 4
    MaxUnitsBuilt = 5
    LeadTime = 6
    ProjectStartDate = 7
    TechnicalLife = 8
    BuildCost = 9
    WACC = 10
    EconomicLife = 11
    MinUnitsBuilt = 12
    MaxUnitsBuiltinYear = 13
    MinUnitsBuiltinYear = 14
    MaxUnitsRetired = 15
    RetirementCost = 16
    MinUnitsRetired = 17
    MaxUnitsRetiredinYear = 18
    MinUnitsRetiredinYear = 19
    x = 20
    y = 21
    z = 22


class SystemWaterPipelinesEnum(Enum):
    RandomNumberSeed = 1
    RepairTimeDistribution = 2
    ExpansionOptimality = 3
    Units = 4
    MaxCapacity = 5
    Diameter = 6
    Roughness = 7
    Length = 8
    PumpEfficiency = 9
    VOMCharge = 10
    FOMCharge = 11
    ConsumptionAllocation = 12
    UnitsOut = 13
    MaintenanceRate = 14
    MaintenanceFrequency = 15
    ForcedOutageRate = 16
    OutageRating = 17
    MeanTimetoRepair = 18
    MinTimeToRepair = 19
    MaxTimeToRepair = 20
    RepairTimeShape = 21
    RepairTimeScale = 22
    MaxUnitsBuilt = 23
    LeadTime = 24
    ProjectStartDate = 25
    TechnicalLife = 26
    BuildCost = 27
    WACC = 28
    EconomicLife = 29
    MinUnitsBuilt = 30
    MaxUnitsBuiltinYear = 31
    MinUnitsBuiltinYear = 32
    MaxUnitsRetired = 33
    RetirementCost = 34
    MinUnitsRetired = 35
    MaxUnitsRetiredinYear = 36
    MinUnitsRetiredinYear = 37
    x = 38
    y = 39
    z = 40


class SystemWaterPlantsEnum(Enum):
    ExpansionOptimality = 1
    Units = 2
    MaxCapacity = 3
    MinStableProduction = 4
    AuxFixed = 5
    AuxBase = 6
    AuxIncr = 7
    HeatUsage = 8
    WaterYield = 9
    EnergyUsage = 10
    VOMCharge = 11
    FOMCharge = 12
    MaxUnitsBuilt = 13
    LeadTime = 14
    ProjectStartDate = 15
    TechnicalLife = 16
    BuildCost = 17
    WACC = 18
    EconomicLife = 19
    MinUnitsBuilt = 20
    MaxUnitsBuiltinYear = 21
    MinUnitsBuiltinYear = 22
    MaxUnitsRetired = 23
    RetirementCost = 24
    MinUnitsRetired = 25
    MaxUnitsRetiredinYear = 26
    MinUnitsRetiredinYear = 27
    x = 28
    y = 29
    z = 30


class SystemWaterStoragesEnum(Enum):
    EnforceBounds = 1
    ExpansionOptimality = 2
    Units = 3
    MaxVolume = 4
    MinVolume = 5
    InitialVolume = 6
    Target = 7
    TargetPenalty = 8
    EnergyUsage = 9
    NaturalInflow = 10
    LossRate = 11
    FOMCharge = 12
    MaxUnitsBuilt = 13
    LeadTime = 14
    ProjectStartDate = 15
    TechnicalLife = 16
    BuildCost = 17
    WACC = 18
    EconomicLife = 19
    MinUnitsBuilt = 20
    MaxUnitsBuiltinYear = 21
    MinUnitsBuiltinYear = 22
    MaxUnitsRetired = 23
    RetirementCost = 24
    MinUnitsRetired = 25
    MaxUnitsRetiredinYear = 26
    MinUnitsRetiredinYear = 27
    TrajectoryNonanticipativity = 28
    TrajectoryNonanticipativityVolume = 29
    TrajectoryNonanticipativityTime = 30
    x = 31
    y = 32
    z = 33


class SystemWaterZonesEnum(Enum):
    x = 1
    y = 2
    z = 3


class SystemWaterwaysEnum(Enum):
    TraversalTime = 1
    FlowControl = 2
    MaxFlow = 3
    MinFlow = 4
    InitialFlow = 5
    MaxRamp = 6
    MaxFlowPenalty = 7
    MinFlowPenalty = 8
    MaxRampPenalty = 9
    InputScalar = 10
    OutputScalar = 11
    x = 12
    y = 13
    z = 14


class SystemZonesEnum(Enum):
    LoadSettlementModel = 1
    WheelingMethod = 2
    Units = 3
    Load = 4
    LoadParticipationFactor = 5
    LoadScalar = 6
    WheelingCharge = 7
    MaxMaintenance = 8
    MaintenanceFactor = 9
    PeakPeriod = 10
    FirmCapacityIncr = 11
    MinCapacityReserves = 12
    MaxCapacityReserves = 13
    MinCapacityReserveMargin = 14
    MaxCapacityReserveMargin = 15
    MinNativeCapacityReserves = 16
    MinNativeCapacityReserveMargin = 17
    CapacityShortagePrice = 18
    CapacityExcessPrice = 19
    CapacityPriceCap = 20
    CapacityPriceFloor = 21
    LOLPTarget = 22
    x = 23
    y = 24
    z = 25


class TransformerEnforceLimitsEnum(Enum):
    Never = 0
    Voltage = 1
    Always = 2
    Contingency = 3


class TransmissionAttributeEnum(Enum):
    MVABase = 1
    OPFMethod = 2
    ConstraintsEnabled = 3
    FormulateUpfront = 4
    ConstraintVoltageThreshold = 5
    InterfaceConstraintsEnabled = 6
    EnforceLimitsOnLinesInInterfaces = 7
    LossesEnabled = 8
    LossVoltageThreshold = 9
    LossMethod = 10
    MaxLossRelativeError = 11
    MaxLossAbsoluteError = 12
    MaxLossTranches = 13
    LossTolerance = 14
    MaxLossIterations = 15
    MaxEmbeddedLossIterations = 16
    DetectNonphysicalLosses = 17
    PTDFMethod = 18
    FlowPTDFThreshold = 19
    WheelingPTDFThreshold = 20
    CacheTransmissionMatrices = 21
    ReactanceCutoff = 22
    AllowDumpEnergy = 23
    AllowUnservedEnergy = 24
    BoundNodePhaseAngles = 25
    MaxAbsolutePhaseAngle = 26
    InternalVoLL = 27
    USEThreshold = 28
    RentalMethod = 29
    InterruptionSharing = 30
    ReportEnabled = 31
    ReportVoltageThreshold = 32
    ReportLinesInInterfaces = 33
    ReportAllInterregionalFlows = 34
    ReportAllInterzonalFlows = 35
    ReportInjectionandLoadNodes = 36
    ConvergenceReportLevel = 37
    SCUCEnabled = 38
    SCUCConstraintVoltageThreshold = 39
    SCUCInterfaceConstraintsEnabled = 40
    EnforceN1Contingencies = 41
    N1ContingencyVoltageThreshold = 42
    ContingencyMonitoringThreshold = 43
    LimitThreshold = 44
    LimitBootstrapInitialThreshold = 45
    LimitBootstrapThresholdDecrement = 46
    MaxLimitIterations = 47
    NetworkReduction = 48


class TransmissionConvergenceReportLevelEnum(Enum):
    None_ = 0
    Normal = 1
    Verbose = 2


class TransmissionDetailEnum(Enum):
    Regional = 0
    Nodal = 1
    Zonal = 2


class TransmissionOPFMethodEnum(Enum):
    Standard = 0
    LargeScale = 1


class TransmissionPTDFMethodEnum(Enum):
    SlackBus = 0
    DistributedLoadSlackReference = 1
    DistributedGenerationSlackCapacity = 3
    DistributedGenerationSlackReference = 4


class TransmissionPTDFResolutionEnum(Enum):
    Nodal = 0
    Zonal = 1
    Regional = 2


class TransmissionRentalMethodEnum(Enum):
    PointToPoint = 0
    FlowGate = 1


class TransmissionRightCompaniesEnum(Enum):
    Share = 1


class TransmissionRightsPricingMethodEnum(Enum):
    LMP = 0
    CongestionCharge = 1


class TransmissionRightsSettlementModelEnum(Enum):
    Buy = 0
    Sell = 1


class TransmissionRightsTypeEnum(Enum):
    SRA = 0
    FTR = 1


class TransmissionWheelingMethodEnum(Enum):
    Net = 1
    Gross = 2


class UnitCommitmentEnum(Enum):
    Off = 0
    On = 1
    Free = -1


class UnitsofDataEnum(Enum):
    Metric = 0
    Imperial = 1


class UpliftCompatibilityEnum(Enum):
    Korea = 1
    Ireland = 2
    Custom = 3


class UpliftCostBasisEnum(Enum):
    CostBased = 1
    BidBased = 2


class VariableAttributeEnum(Enum):
    CompoundType = 1
    CompoundStartDate = 2


class VariableCompoundTypeEnum(Enum):
    Nominal = 0
    Annual = 1


class VariableConditionEnum(Enum):
    EQ = 0
    GE = 1
    GT = 2
    None_ = 4
    LT = -2
    LE = -1


class VariableDistributionTypeEnum(Enum):
    Normal = 0
    Lognormal = 1


class VariableFuelsEnum(Enum):
    OfftakeCoefficient = 1


class VariableGeneratorsEnum(Enum):
    GenerationCoefficient = 1
    UnitsGeneratingCoefficient = 2
    UnitsStartedCoefficient = 3
    UnitsSyncCondCoefficient = 4
    FuelOfftakeCoefficient = 5
    UnitsOutCoefficient = 6


class VariableHeatNodesEnum(Enum):
    HeatFlowCoefficient = 1


class VariableHeatPlantsEnum(Enum):
    FuelOfftakeCoefficient = 1


class VariableInterfacesEnum(Enum):
    FlowCoefficient = 1


class VariableLinesEnum(Enum):
    FlowCoefficient = 1
    FlowForwardCoefficient = 2
    FlowBackCoefficient = 3
    FlowingForwardCoefficient = 4
    FlowingBackCoefficient = 5


class VariableNodesEnum(Enum):
    LoadCoefficient = 1


class VariableRegionsEnum(Enum):
    LoadCoefficient = 1
    CapacityReservesCoefficient = 2
    PriceCoefficient = 3


class VariableReservesEnum(Enum):
    ProvisionCoefficient = 1
    RiskCoefficient = 2
    ShortageCoefficient = 3


class VariableSampleSourceEnum(Enum):
    AutoCorrelation = 0
    MeanReversion = 1
    ARIMA = 2
    RandomFromProfiles = 3
    InSequenceFromProfiles = 4
    Variable = 5
    TransformedARIMA = 6
    None_ = -1


class VariableSamplingMethodEnum(Enum):
    None_ = 0
    Auto = 1
    User = 2


class VariableStoragesEnum(Enum):
    EndVolumeCoefficient = 1
    InflowCoefficient = 2
    ReleaseCoefficient = 3
    SpillCoefficient = 4


class VariableVariablesEnum(Enum):
    Correlation = 1
    ValueCoefficient = 2


class VariableZonesEnum(Enum):
    LoadCoefficient = 1
    CapacityReservesCoefficient = 2


class WaterNodeAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class WaterStorageAttributeEnum(Enum):
    Latitude = 1
    Longitude = 2


class WaterwayFlowControlEnum(Enum):
    Economic = 0
    SpillOnly = 1


class ZoneZonesEnum(Enum):
    WheelingCharge = 1
    MaxFlow = 2
