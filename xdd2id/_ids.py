IDS_MAP = {
    '001000': 'DEVICE_TYPE',
    '001001': 'ERROR_REGISTER',
    '011003': 'ERROR_FIELD_1',
    '021003': 'ERROR_FIELD_2',
    '031003': 'ERROR_FIELD_3',
    '041003': 'ERROR_FIELD_4',
    '001005': 'COB_ID_SYNC',
    '001006': 'CYCLE_PERIOD',
    '001007': 'SYNC_WINDOWS_LENGTH',
    '001008': 'DEVICE_NAME',
    '001009': 'HW_VERSION',
    '00100a': 'SW_VERSION',
    '00100c': 'GUARD_TIME',
    '00100d': 'LIFE_TIME_FACTOR',
    '011010': 'STORE_ALL_PARAMS',
    '021010': 'STORE_COMM_PARAMS',
    '031010': 'STORE_APP_PARAMS',
    '011011': 'RESTORE_ALL_PARAMS',
    '021011': 'RESTORE_COMM_PARAMS',
    '031011': 'RESTORE_APP_PARAMS',
    '001014': 'COB_ID_EMERGENCY_MSG',
    '001017': 'PRODUCER_HEARTBEAT_TIME',
    '011018': 'ID_OBJ_VENDOR_ID',
    '021018': 'ID_OBJ_PRODUCT_CODE',
    '031018': 'ID_OBJ_REVISION_NUM',
    '041018': 'ID_OBJ_SERIAL_NUM',
    '011200': 'SSDO_COB_ID_CLIENT_SERVER',
    '021200': 'SSDO_COB_ID_SERVER_CLIENT',
    '011400': 'RPDO_1_COB_ID_USED',
    '021400': 'RPDO_1_TRANS_TYPE',
    '031400': 'RPDO_1_INHIBIT_TIME',
    '011401': 'RPDO_2_COB_ID_USED',
    '021401': 'RPDO_2_TRANS_TYPE',
    '031401': 'RPDO_2_INHIBIT_TIME',
    '011402': 'RPDO_3_COB_ID_USED',
    '021402': 'RPDO_3_TRANS_TYPE',
    '031402': 'RPDO_3_INHIBIT_TIME',
    '011403': 'RPDO_4_COB_ID_USED',
    '021403': 'RPDO_4_TRANS_TYPE',
    '031403': 'RPDO_4_INHIBIT_TIME',
    '011600': 'RPDO_1_MAPPING_PARAM_1',
    '021600': 'RPDO_1_MAPPING_PARAM_2',
    '031600': 'RPDO_1_MAPPING_PARAM_3',
    '041600': 'RPDO_1_MAPPING_PARAM_4',
    '051600': 'RPDO_1_MAPPING_PARAM_5',
    '061600': 'RPDO_1_MAPPING_PARAM_6',
    '071600': 'RPDO_1_MAPPING_PARAM_7',
    '081600': 'RPDO_1_MAPPING_PARAM_8',
    '011601': 'RPDO_2_MAPPING_PARAM_1',
    '021601': 'RPDO_2_MAPPING_PARAM_2',
    '031601': 'RPDO_2_MAPPING_PARAM_3',
    '041601': 'RPDO_2_MAPPING_PARAM_4',
    '051601': 'RPDO_2_MAPPING_PARAM_5',
    '061601': 'RPDO_2_MAPPING_PARAM_6',
    '071601': 'RPDO_2_MAPPING_PARAM_7',
    '081601': 'RPDO_2_MAPPING_PARAM_8',
    '011602': 'RPDO_3_MAPPING_PARAM_1',
    '021602': 'RPDO_3_MAPPING_PARAM_2',
    '031602': 'RPDO_3_MAPPING_PARAM_3',
    '041602': 'RPDO_3_MAPPING_PARAM_4',
    '051602': 'RPDO_3_MAPPING_PARAM_5',
    '061602': 'RPDO_3_MAPPING_PARAM_6',
    '071602': 'RPDO_3_MAPPING_PARAM_7',
    '081602': 'RPDO_3_MAPPING_PARAM_8',
    '011603': 'RPDO_4_MAPPING_PARAM_1',
    '021603': 'RPDO_4_MAPPING_PARAM_2',
    '031603': 'RPDO_4_MAPPING_PARAM_3',
    '041603': 'RPDO_4_MAPPING_PARAM_4',
    '051603': 'RPDO_4_MAPPING_PARAM_5',
    '061603': 'RPDO_4_MAPPING_PARAM_6',
    '071603': 'RPDO_4_MAPPING_PARAM_7',
    '081603': 'RPDO_4_MAPPING_PARAM_8',
    '011800': 'TPDO_1_COB_ID_USED',
    '021800': 'TPDO_1_TRANS_TYPE',
    '031800': 'TPDO_1_INHIBIT_TIME',
    '051800': 'TPDO_1_EVENT_TIMER',
    '011801': 'TPDO_2_COB_ID_USED',
    '021801': 'TPDO_2_TRANS_TYPE',
    '031801': 'TPDO_2_INHIBIT_TIME',
    '051801': 'TPDO_2_EVENT_TIMER',
    '011802': 'TPDO_3_COB_ID_USED',
    '021802': 'TPDO_3_TRANS_TYPE',
    '031802': 'TPDO_3_INHIBIT_TIME',
    '051802': 'TPDO_3_EVENT_TIMER',
    '011803': 'TPDO_4_COB_ID_USED',
    '021803': 'TPDO_4_TRANS_TYPE',
    '031803': 'TPDO_4_INHIBIT_TIME',
    '051803': 'TPDO_4_EVENT_TIMER',
    '011a00': 'TPDO_1_MAPPING_PARAM_1',
    '021a00': 'TPDO_1_MAPPING_PARAM_2',
    '031a00': 'TPDO_1_MAPPING_PARAM_3',
    '041a00': 'TPDO_1_MAPPING_PARAM_4',
    '051a00': 'TPDO_1_MAPPING_PARAM_5',
    '061a00': 'TPDO_1_MAPPING_PARAM_6',
    '071a00': 'TPDO_1_MAPPING_PARAM_7',
    '081a00': 'TPDO_1_MAPPING_PARAM_8',
    '011a01': 'TPDO_2_MAPPING_PARAM_1',
    '021a01': 'TPDO_2_MAPPING_PARAM_2',
    '031a01': 'TPDO_2_MAPPING_PARAM_3',
    '041a01': 'TPDO_2_MAPPING_PARAM_4',
    '051a01': 'TPDO_2_MAPPING_PARAM_5',
    '061a01': 'TPDO_2_MAPPING_PARAM_6',
    '071a01': 'TPDO_2_MAPPING_PARAM_7',
    '081a01': 'TPDO_2_MAPPING_PARAM_8',
    '011a02': 'TPDO_3_MAPPING_PARAM_1',
    '021a02': 'TPDO_3_MAPPING_PARAM_2',
    '031a02': 'TPDO_3_MAPPING_PARAM_3',
    '041a02': 'TPDO_3_MAPPING_PARAM_4',
    '051a02': 'TPDO_3_MAPPING_PARAM_5',
    '061a02': 'TPDO_3_MAPPING_PARAM_6',
    '071a02': 'TPDO_3_MAPPING_PARAM_7',
    '081a02': 'TPDO_3_MAPPING_PARAM_8',
    '011a03': 'TPDO_4_MAPPING_PARAM_1',
    '021a03': 'TPDO_4_MAPPING_PARAM_2',
    '031a03': 'TPDO_4_MAPPING_PARAM_3',
    '041a03': 'TPDO_4_MAPPING_PARAM_4',
    '051a03': 'TPDO_4_MAPPING_PARAM_5',
    '061a03': 'TPDO_4_MAPPING_PARAM_6',
    '071a03': 'TPDO_4_MAPPING_PARAM_7',
    '081a03': 'TPDO_4_MAPPING_PARAM_8',
    '012000': 'UART_CFG_NODE_ID',
    '022000': 'UART_CFG_BAUDRATE',
    '032000': 'UART_CFG_DAISY_CHAIN',
    '042000': 'UART_CFG_BASE_FORMAT',
    '052000': 'UART_CFG_STS_WORD_REQ',
    '062000': 'UART_CFG_CRC_ENABLE',
    '072000': 'UART_CFG_LIFEGUARD_MSG',
    '082000': 'UART_CFG_BINARY_MODE',
    '012001': 'CANOPEN_CFG_NODE_ID',
    '022001': 'CANOPEN_CFG_BAUDRATE',
    '032001': 'CANOPEN_CFG_DIAG_LVL',
    '01200f': 'COMM_PASSWORD_ALL',
    '02200f': 'COMM_PASSWORD_UART',
    '03200f': 'COMM_PASSWORD_CANOPEN',
    '002020': 'PWM_ALT_FREQ_EN',
    '0120c2': 'DRIVE_TEMPERATURE_ACT',
    '0220c2': 'DRIVE_TEMPERATURE_MAX',
    '0320c2': 'DRIVE_TEMPERATURE_MIN',
    '012101': 'BUS_VOLTAGE_DC_LINK',
    '022101': 'BUS_VOLTAGE_USER_MAX',
    '032101': 'BUS_VOLTAGE_USER_MIN',
    '012102': 'HOMING_EXTRA_TOTAL_TIMEOUT',
    '022102': 'HOMING_EXTRA_TORQUE_THRESHOLD',
    '032102': 'HOMING_EXTRA_STARTUP_SENSOR',
    '012103': 'SHUNT_CFG_AVAIL',
    '022103': 'SHUNT_CFG_DUTY_USED',
    '032103': 'SHUNT_CFG_HYSTERESIS',
    '042103': 'SHUNT_CFG_FREQ',
    '002290': 'DRIVE_SETUP_STATUS',
    '002301': 'MOTOR_PAIR_POLES',
    '012305': 'COMMUTATION_SENSOR',
    '022305': 'COMMUTATION_IANGLE_DET_METHOD',
    '032305': 'COMMUTATION_ACT_SYSTEM_ANGLE',
    '042305': 'COMMUTATION_REF_SENSOR',
    '052305': 'COMMUTATION_ANGLE_OFFSET',
    '012306': 'FORCED_ALIGN_METHOD_TIME',
    '022306': 'FORCED_ALIGN_METHOD_CURR',
    '032306': 'FORCED_ALIGN_METHOD_TOLERANCE',
    '012307': 'KNOWN_ALIGN_METHOD_INITIAL_ANGLE',
    '012308': 'NINCR_ALIGN_OFFSET_PHASE_A',
    '012310': 'FB_TORQUE_SENSOR',
    '022310': 'FB_VEL_SENSOR',
    '032310': 'FB_POS_SENSOR',
    '002311': 'DIG_ENC_SINCOS_SWAP',
    '002312': 'DIG_ENC_SINCOS_TYPE',
    '002313': 'DIG_ENC_SINCOS_GLITCH_FILTER',
    '002314': 'DIG_ENC_VAL',
    '012321': 'DIGITAL_HALLS_POLARITY',
    '022321': 'DIGITAL_HALLS_VAL',
    '032321': 'DIGITAL_HALLS_STEP_OFFSET',
    '012340': 'LINEAR_HALL_VALS_1',
    '022340': 'LINEAR_HALL_VALS_2',
    '032340': 'LINEAR_HALL_VALS_3',
    '012341': 'LINEAR_HALL_OFFSETS_1',
    '022341': 'LINEAR_HALL_OFFSETS_2',
    '032341': 'LINEAR_HALL_OFFSETS_3',
    '012342': 'LINEAR_HALL_GAINS_1',
    '022342': 'LINEAR_HALL_GAINS_2',
    '032342': 'LINEAR_HALL_GAINS_3',
    '012343': 'LINEAR_HALL_ROT_ALPHA',
    '022343': 'LINEAR_HALL_ROT_BETA',
    '032343': 'LINEAR_HALL_ROT_ZERO',
    '002344': 'LINEAR_HALL_EST_ANGLE',
    '002345': 'LINEAR_HALL_POLARITY',
    '012350': 'SINCOS_VALS_SINUS',
    '022350': 'SINCOS_VALS_COSINUS',
    '032350': 'SINCOS_VALS_REF_VAL',
    '012351': 'SINCOS_OFFSETS_SINUS',
    '022351': 'SINCOS_OFFSETS_COSINUS',
    '032351': 'SINCOS_OFFSETS_REF',
    '012352': 'SINCOS_GAINS_SINUS',
    '022352': 'SINCOS_GAINS_COSINUS',
    '032352': 'SINCOS_GAINS_REF',
    '002353': 'SINCOS_EST_ANGLE',
    '002354': 'SINCOS_MULT_FACTOR',
    '012360': 'SMO_PARAMS_LOCK_TIME',
    '022360': 'SMO_PARAMS_OLOOP_FINAL_SPEED',
    '032360': 'SMO_PARAMS_OLOOP_CURR',
    '042360': 'SMO_PARAMS_OLOOP_TIME',
    '052360': 'SMO_PARAMS_OPEN_CLOSE_TRANS_ENABLED',
    '062360': 'SMO_PARAMS_GAIN',
    '072360': 'SMO_PARAMS_LINEAR_ZONE',
    '012361': 'SMO_RESULTS_EST_I_ALPHA',
    '022361': 'SMO_RESULTS_EST_I_BETA',
    '032361': 'SMO_RESULTS_MEAS_I_ALPHA',
    '042361': 'SMO_RESULTS_MEAS_I_BETA',
    '052361': 'SMO_RESULTS_EST_BEMF_ALPHA',
    '062361': 'SMO_RESULTS_EST_BEMF_BETA',
    '072361': 'SMO_RESULTS_EST_THETA',
    '012370': 'RESOLVER_PARAMS_ANGLE',
    '022370': 'RESOLVER_PARAMS_TOLERANCE',
    '032370': 'RESOLVER_PARAMS_POLE_PAIRS',
    '042370': 'RESOLVER_PARAMS_POLARITY',
    '052370': 'RESOLVER_PARAMS_ADAPTED_ANGLE',
    '062370': 'RESOLVER_PARAMS_ERR_CODE',
    '072370': 'RESOLVER_PARAMS_ERR_FILTER',
    '012380': 'SSI_ABSENC_CFG_FRAME_TYPE',
    '022380': 'SSI_ABSENC_CFG_FRAME_SIZE',
    '032380': 'SSI_ABSENC_CFG_CODIFICATION',
    '042380': 'SSI_ABSENC_CFG_MAX_CLOCK_RATE',
    '052380': 'SSI_ABSENC_CFG_SINGLE_TURN_BITS',
    '062380': 'SSI_ABSENC_CFG_SINGLE_TURN_START_BIT',
    '072380': 'SSI_ABSENC_CFG_MULTI_TURN_BITS',
    '082380': 'SSI_ABSENC_CFG_MULTI_TURN_START_BIT',
    '092380': 'SSI_ABSENC_CFG_ENDIANNESS',
    '0a2380': 'SSI_ABSENC_CFG_ERR_FILTER',
    '002381': 'SSI_MULTI_TURN_VAL',
    '002382': 'SSI_SINGLE_TURN_VAL',
    '002383': 'SSI_POLARITY',
    '0123d0': 'AIN_FB_AIN_USED',
    '0223d0': 'AIN_FB_AIN_MOTION_OFFSET',
    '0323d0': 'AIN_FB_RESERVED',
    '0423d0': 'AIN_FB_AIN_MOTION_RANGE',
    '0523d0': 'AIN_FB_AIN_POLARITY',
    '0123d1': 'AIN_FB_CORR_ENABLED',
    '0223d1': 'AIN_FB_CORR_VAL_0',
    '0323d1': 'AIN_FB_CORR_VAL_1',
    '0423d1': 'AIN_FB_CORR_VAL_2',
    '0523d1': 'AIN_FB_CORR_VAL_3',
    '0623d1': 'AIN_FB_CORR_VAL_4',
    '0723d1': 'AIN_FB_CORR_VAL_5',
    '0823d1': 'AIN_FB_CORR_VAL_6',
    '0923d1': 'AIN_FB_CORR_VAL_7',
    '0a23d1': 'AIN_FB_CORR_VAL_8',
    '0b23d1': 'AIN_FB_CORR_VAL_9',
    '0c23d1': 'AIN_FB_CORR_VAL_10',
    '0d23d1': 'AIN_FB_CORR_VAL_11',
    '0e23d1': 'AIN_FB_CORR_VAL_12',
    '0f23d1': 'AIN_FB_CORR_VAL_13',
    '1023d1': 'AIN_FB_CORR_VAL_14',
    '1123d1': 'AIN_FB_CORR_VAL_15',
    '1223d1': 'AIN_FB_CORR_VAL_16',
    '1323d1': 'AIN_FB_CORR_VAL_17',
    '1423d1': 'AIN_FB_CORR_VAL_18',
    '1523d1': 'AIN_FB_CORR_VAL_19',
    '1623d1': 'AIN_FB_CORR_VAL_20',
    '1723d1': 'AIN_FB_CORR_VAL_21',
    '1823d1': 'AIN_FB_CORR_VAL_22',
    '1923d1': 'AIN_FB_CORR_VAL_23',
    '1a23d1': 'AIN_FB_CORR_VAL_24',
    '1b23d1': 'AIN_FB_CORR_VAL_25',
    '1c23d1': 'AIN_FB_CORR_VAL_26',
    '1d23d1': 'AIN_FB_CORR_VAL_27',
    '1e23d1': 'AIN_FB_CORR_VAL_28',
    '1f23d1': 'AIN_FB_CORR_VAL_29',
    '2023d1': 'AIN_FB_CORR_VAL_30',
    '2123d1': 'AIN_FB_CORR_VAL_31',
    '2223d1': 'AIN_FB_CORR_VAL_32',
    '2323d1': 'AIN_FB_CORR_VAL_33',
    '2423d1': 'AIN_FB_CORR_VAL_34',
    '2523d1': 'AIN_FB_CORR_VAL_35',
    '2623d1': 'AIN_FB_CORR_VAL_36',
    '2723d1': 'AIN_FB_CORR_VAL_37',
    '2823d1': 'AIN_FB_CORR_VAL_38',
    '2923d1': 'AIN_FB_CORR_VAL_39',
    '2a23d1': 'AIN_FB_CORR_VAL_40',
    '2b23d1': 'AIN_FB_CORR_VAL_41',
    '2c23d1': 'AIN_FB_CORR_VAL_42',
    '2d23d1': 'AIN_FB_CORR_VAL_43',
    '2e23d1': 'AIN_FB_CORR_VAL_44',
    '2f23d1': 'AIN_FB_CORR_VAL_45',
    '3023d1': 'AIN_FB_CORR_VAL_46',
    '3123d1': 'AIN_FB_CORR_VAL_47',
    '3223d1': 'AIN_FB_CORR_VAL_48',
    '3323d1': 'AIN_FB_CORR_VAL_49',
    '3423d1': 'AIN_FB_CORR_VAL_50',
    '3523d1': 'AIN_FB_CORR_VAL_51',
    '3623d1': 'AIN_FB_CORR_VAL_52',
    '3723d1': 'AIN_FB_CORR_VAL_53',
    '3823d1': 'AIN_FB_CORR_VAL_54',
    '3923d1': 'AIN_FB_CORR_VAL_55',
    '3a23d1': 'AIN_FB_CORR_VAL_56',
    '3b23d1': 'AIN_FB_CORR_VAL_57',
    '3c23d1': 'AIN_FB_CORR_VAL_58',
    '3d23d1': 'AIN_FB_CORR_VAL_59',
    '3e23d1': 'AIN_FB_CORR_VAL_60',
    '3f23d1': 'AIN_FB_CORR_VAL_61',
    '4023d1': 'AIN_FB_CORR_VAL_62',
    '4123d1': 'AIN_FB_CORR_VAL_63',
    '4223d1': 'AIN_FB_CORR_VAL_64',
    '4323d1': 'AIN_FB_CORR_VAL_65',
    '4423d1': 'AIN_FB_CORR_VAL_66',
    '4523d1': 'AIN_FB_CORR_VAL_67',
    '4623d1': 'AIN_FB_CORR_VAL_68',
    '4723d1': 'AIN_FB_CORR_VAL_69',
    '4823d1': 'AIN_FB_CORR_VAL_70',
    '4923d1': 'AIN_FB_CORR_VAL_71',
    '4a23d1': 'AIN_FB_CORR_VAL_72',
    '4b23d1': 'AIN_FB_CORR_VAL_73',
    '4c23d1': 'AIN_FB_CORR_VAL_74',
    '4d23d1': 'AIN_FB_CORR_VAL_75',
    '4e23d1': 'AIN_FB_CORR_VAL_76',
    '4f23d1': 'AIN_FB_CORR_VAL_77',
    '5023d1': 'AIN_FB_CORR_VAL_78',
    '5123d1': 'AIN_FB_CORR_VAL_79',
    '5223d1': 'AIN_FB_CORR_VAL_80',
    '5323d1': 'AIN_FB_CORR_VAL_81',
    '5423d1': 'AIN_FB_CORR_VAL_82',
    '5523d1': 'AIN_FB_CORR_VAL_83',
    '5623d1': 'AIN_FB_CORR_VAL_84',
    '5723d1': 'AIN_FB_CORR_VAL_85',
    '5823d1': 'AIN_FB_CORR_VAL_86',
    '5923d1': 'AIN_FB_CORR_VAL_87',
    '5a23d1': 'AIN_FB_CORR_VAL_88',
    '5b23d1': 'AIN_FB_CORR_VAL_89',
    '5c23d1': 'AIN_FB_CORR_VAL_90',
    '5d23d1': 'AIN_FB_CORR_VAL_91',
    '5e23d1': 'AIN_FB_CORR_VAL_92',
    '5f23d1': 'AIN_FB_CORR_VAL_93',
    '6023d1': 'AIN_FB_CORR_VAL_94',
    '6123d1': 'AIN_FB_CORR_VAL_95',
    '6223d1': 'AIN_FB_CORR_VAL_96',
    '6323d1': 'AIN_FB_CORR_VAL_97',
    '6423d1': 'AIN_FB_CORR_VAL_98',
    '6523d1': 'AIN_FB_CORR_VAL_99',
    '6623d1': 'AIN_FB_CORR_VAL_100',
    '6723d1': 'AIN_FB_CORR_VAL_101',
    '6823d1': 'AIN_FB_CORR_VAL_102',
    '6923d1': 'AIN_FB_CORR_VAL_103',
    '6a23d1': 'AIN_FB_CORR_VAL_104',
    '6b23d1': 'AIN_FB_CORR_VAL_105',
    '6c23d1': 'AIN_FB_CORR_VAL_106',
    '6d23d1': 'AIN_FB_CORR_VAL_107',
    '6e23d1': 'AIN_FB_CORR_VAL_108',
    '6f23d1': 'AIN_FB_CORR_VAL_109',
    '7023d1': 'AIN_FB_CORR_VAL_110',
    '7123d1': 'AIN_FB_CORR_VAL_111',
    '7223d1': 'AIN_FB_CORR_VAL_112',
    '7323d1': 'AIN_FB_CORR_VAL_113',
    '7423d1': 'AIN_FB_CORR_VAL_114',
    '7523d1': 'AIN_FB_CORR_VAL_115',
    '7623d1': 'AIN_FB_CORR_VAL_116',
    '7723d1': 'AIN_FB_CORR_VAL_117',
    '7823d1': 'AIN_FB_CORR_VAL_118',
    '7923d1': 'AIN_FB_CORR_VAL_119',
    '7a23d1': 'AIN_FB_CORR_VAL_120',
    '7b23d1': 'AIN_FB_CORR_VAL_121',
    '7c23d1': 'AIN_FB_CORR_VAL_122',
    '7d23d1': 'AIN_FB_CORR_VAL_123',
    '7e23d1': 'AIN_FB_CORR_VAL_124',
    '7f23d1': 'AIN_FB_CORR_VAL_125',
    '8023d1': 'AIN_FB_CORR_VAL_126',
    '8123d1': 'AIN_FB_CORR_VAL_127',
    '8223d1': 'AIN_FB_CORR_VAL_128',
    '0123f0': 'DC_TACHOMETER_VOLTAGE_MV_PER_1000RPM',
    '0223f0': 'DC_TACHOMETER_AIN_USED',
    '0323f0': 'DC_TACHOMETER_AIN_OFFSET',
    '002400': 'SYSTEM_POLARITY',
    '002430': 'CMD_SRC',
    '002431': 'LOCALREMOTE_CTL',
    '012432': 'CMD_SRC_EGEARING_INPUT_GEAR',
    '022432': 'CMD_SRC_EGEARING_OUTPUT_GEAR',
    '012433': 'CMD_SRC_STDIR_STEP_OUT',
    '022433': 'CMD_SRC_STDIR_STEP_IN',
    '012434': 'CMD_SRC_AIN_USED',
    '022434': 'CMD_SRC_AIN_MOTION_OFFSET',
    '032434': 'CMD_SRC_AIN_VEL_DEADBAND',
    '042434': 'CMD_SRC_AIN_MOTION_RANGE',
    '012435': 'CMD_SRC_PWM_MODE',
    '022435': 'CMD_SRC_PWM_INPUT_MOTION_OFFSET',
    '032435': 'CMD_SRC_PWM_INPUT_VEL_DEADBAND',
    '042435': 'CMD_SRC_PWM_INPUT_MOTION_RANGE',
    '052435': 'CMD_SRC_PWM_DUTY_ACT',
    '062435': 'CMD_SRC_PWM_PERIOD_ACT',
    '012436': 'CMD_SRC_IGEN_FUNC_TYPE',
    '022436': 'CMD_SRC_IGEN_AMPLITUDE',
    '032436': 'CMD_SRC_IGEN_FREQ_10_MHZ',
    '00243a': 'CMD_SRC_INTGT_VAL',
    '012500': 'POS_CTL_KP',
    '022500': 'POS_CTL_KI',
    '032500': 'POS_CTL_KD',
    '042500': 'POS_CTL_IWDUP_K',
    '052500': 'POS_CTL_VEL_FF_K',
    '062500': 'POS_CTL_ACC_FF_K',
    '072500': 'POS_CTL_ILIM',
    '012501': 'VEL_CTL_KP',
    '022501': 'VEL_CTL_KI',
    '032501': 'VEL_CTL_KD',
    '042501': 'VEL_CTL_IWDUP_K',
    '052501': 'VEL_CTL_ACC_FF_K',
    '062501': 'VEL_CTL_ILIM',
    '012502': 'FLUX_CTL_KP',
    '022502': 'FLUX_CTL_KI',
    '032502': 'FLUX_CTL_K_SCALING',
    '012503': 'TORQUE_CTL_KP',
    '022503': 'TORQUE_CTL_KI',
    '032503': 'TORQUE_CTL_K_SCALING',
    '012504': 'TORQUE_DEM_LPF_ENABLED',
    '022504': 'TORQUE_DEM_LPF_CUTOFF_FREQ',
    '012505': 'TORQUE_ACT_LPF_ENABLED',
    '022505': 'TORQUE_ACT_LPF_CUTOFF_FREQ',
    '002506': 'MAX_TORQUE_CTE_SPEED',
    '012507': 'CTL_LOOPS_BYPASS_TORQUE_LOOP',
    '022507': 'CTL_LOOPS_POS_FB_OPENLOOP',
    '032507': 'CTL_LOOPS_VEL_FB_OPENLOOP',
    '042507': 'CTL_LOOPS_TORQUE_FB_OPENLOOP',
    '052507': 'CTL_LOOPS_VEL_MODE_USES_POS_LOOP',
    '002508': 'TORQUE_WINDOW',
    '002509': 'TORQUE_WINDOW_TIME',
    '01250a': 'DSIG_MAX_ENTRIES',
    '02250a': 'DSIG_FILLED_ENTRIES',
    '03250a': 'DSIG_ENTRY_NUM',
    '04250a': 'DSIG_ENTRY_VAL',
    '05250a': 'DSIG_INJ_POINT',
    '06250a': 'DSIG_NCYCLES',
    '07250a': 'DSIG_UPDATE_RATE',
    '08250a': 'DSIG_OUTPUT_VAL',
    '002510': 'ENABLE_CURR_LPF',
    '012600': 'CURR_PHASE_A',
    '022600': 'CURR_PHASE_B',
    '032600': 'CURR_PHASE_C',
    '012601': 'CURR_D',
    '022601': 'CURR_Q',
    '012602': 'CURR_THOUSANDS_PHASE_A',
    '022602': 'CURR_THOUSANDS_PHASE_B',
    '032602': 'CURR_THOUSANDS_PHASE_C',
    '012603': 'CURR_DEM_STEPPERS_COIL_1',
    '022603': 'CURR_DEM_STEPPERS_COIL_2',
    '012610': 'VOLTAGE_PHASE_A',
    '022610': 'VOLTAGE_PHASE_B',
    '032610': 'VOLTAGE_PHASE_C',
    '012611': 'VOLTAGE_D',
    '022611': 'VOLTAGE_Q',
    '012700': 'STEPPER_NUM_OF_MICROSTEPS_BITS',
    '022700': 'STEPPER_RUN_CURR',
    '032700': 'STEPPER_STANDBY_CURR',
    '042700': 'STEPPER_NUM_OF_STEPS_PER_REV',
    '052700': 'STEPPER_NUM_OF_PHASES',
    '062700': 'STEPPER_ENHANCED_CURR_MODE',
    '012701': 'MOTOR_PARAMS_R_PH2PH',
    '022701': 'MOTOR_PARAMS_L_PH2PH',
    '032701': 'MOTOR_PARAMS_MAG_PPITCH',
    '042701': 'MOTOR_PARAMS_K_BACKEMF',
    '052701': 'MOTOR_PARAMS_STROKE_UM',
    '062701': 'MOTOR_PARAMS_K_TORQUE',
    '012702': 'I2T_PARAMS_PEAK_CURR',
    '022702': 'I2T_PARAMS_PEAK_TIME',
    '012a02': 'DIN_POLARITY',
    '022a02': 'DOUT_POLARITY',
    '012a03': 'AIN_1_VAL',
    '022a03': 'AIN_2_VAL',
    '032a03': 'AIN_3_VAL',
    '042a03': 'AIN_4_VAL',
    '052a03': 'AIN_5_VAL',
    '062a03': 'AIN_6_VAL',
    '072a03': 'AIN_7_VAL',
    '082a03': 'AIN_8_VAL',
    '012a04': 'AOUT_1_VAL_11BITS',
    '022a04': 'AOUT_2_VAL_16BITS',
    '012a05': 'BRAKE_MODE',
    '022a05': 'BRAKE_DELAY_BEFORE_RELEASE',
    '032a05': 'BRAKE_DELAY_AFTER_ENABLE',
    '042a05': 'BRAKE_DUTY_CYCLE',
    '052a05': 'BRAKE_FULL_RELEASE_PULSE_TIME',
    '062a05': 'BRAKE_FREQ',
    '012a08': 'AOUT_AUTO_MODE_ENABLED',
    '022a08': 'AOUT_AUTO_SOURCE_REGISTER',
    '032a08': 'AOUT_AUTO_DEST_OUTPUT',
    '042a08': 'AOUT_AUTO_MAX_REPR_VAL',
    '012a0a': 'PWM_INPUTS_MAX_PWM_FREQ',
    '022a0a': 'PWM_INPUTS_PWM_PERIOD_1',
    '032a0a': 'PWM_INPUTS_PWM_DUTY_1',
    '042a0a': 'PWM_INPUTS_PWM_PERIOD_2',
    '052a0a': 'PWM_INPUTS_PWM_DUTY_2',
    '012a0b': 'PWM_OUTPUTS_MAX_PWM_FREQ',
    '022a0b': 'PWM_OUTPUTS_PWM_PERIOD_1',
    '032a0b': 'PWM_OUTPUTS_PWM_DUTY_1',
    '042a0b': 'PWM_OUTPUTS_PWM_PERIOD_2',
    '052a0b': 'PWM_OUTPUTS_PWM_DUTY_2',
    '012a10': 'GPI_MAPPING_1_FUNC',
    '022a10': 'GPI_MAPPING_2_FUNC',
    '032a10': 'GPI_MAPPING_3_FUNC',
    '042a10': 'GPI_MAPPING_4_FUNC',
    '052a10': 'GPI_MAPPING_5_FUNC',
    '062a10': 'GPI_MAPPING_6_FUNC',
    '072a10': 'GPI_MAPPING_7_FUNC',
    '082a10': 'GPI_MAPPING_8_FUNC',
    '092a10': 'GPI_MAPPING_HS_1_FUNC',
    '0a2a10': 'GPI_MAPPING_HS_2_FUNC',
    '012a11': 'GPO_MAPPING_1_FUNC',
    '022a11': 'GPO_MAPPING_2_FUNC',
    '032a11': 'GPO_MAPPING_3_FUNC',
    '042a11': 'GPO_MAPPING_4_FUNC',
    '052a11': 'GPO_MAPPING_5_FUNC',
    '062a11': 'GPO_MAPPING_6_FUNC',
    '072a11': 'GPO_MAPPING_7_FUNC',
    '082a11': 'GPO_MAPPING_8_FUNC',
    '092a11': 'GPO_MAPPING_9_FUNC',
    '0a2a11': 'GPO_MAPPING_10_FUNC',
    '012c00': 'GPR_ACCUM',
    '022c00': 'GPR_W2',
    '032c00': 'GPR_W3',
    '042c00': 'GPR_W4',
    '052c00': 'GPR_W5',
    '062c00': 'GPR_W6',
    '072c00': 'GPR_W7',
    '082c00': 'GPR_W8',
    '092c00': 'GPR_W9',
    '0a2c00': 'GPR_W10',
    '0b2c00': 'GPR_W11',
    '0c2c00': 'GPR_W12',
    '0d2c00': 'GPR_W13',
    '0e2c00': 'GPR_W14',
    '0f2c00': 'GPR_W15',
    '102c00': 'GPR_W16',
    '112c00': 'GPR_W17',
    '122c00': 'GPR_W18',
    '132c00': 'GPR_W19',
    '142c00': 'GPR_W20',
    '152c00': 'GPR_W21',
    '162c00': 'GPR_W22',
    '172c00': 'GPR_W23',
    '182c00': 'GPR_W24',
    '192c00': 'GPR_W25',
    '1a2c00': 'GPR_W26',
    '1b2c00': 'GPR_W27',
    '1c2c00': 'GPR_W28',
    '1d2c00': 'GPR_W29',
    '1e2c00': 'GPR_W30',
    '1f2c00': 'GPR_W31',
    '202c00': 'GPR_W32',
    '212c00': 'GPR_W33',
    '222c00': 'GPR_W34',
    '232c00': 'GPR_W35',
    '242c00': 'GPR_W36',
    '252c00': 'GPR_W37',
    '262c00': 'GPR_W38',
    '272c00': 'GPR_W39',
    '282c00': 'GPR_W40',
    '292c00': 'GPR_W41',
    '2a2c00': 'GPR_W42',
    '2b2c00': 'GPR_W43',
    '2c2c00': 'GPR_W44',
    '2d2c00': 'GPR_W45',
    '2e2c00': 'GPR_W46',
    '2f2c00': 'GPR_W47',
    '302c00': 'GPR_W48',
    '312c00': 'GPR_W49',
    '322c00': 'GPR_W50',
    '332c00': 'GPR_W51',
    '342c00': 'GPR_W52',
    '352c00': 'GPR_W53',
    '362c00': 'GPR_W54',
    '372c00': 'GPR_W55',
    '382c00': 'GPR_W56',
    '392c00': 'GPR_W57',
    '3a2c00': 'GPR_W58',
    '3b2c00': 'GPR_W59',
    '3c2c00': 'GPR_W60',
    '3d2c00': 'GPR_W61',
    '3e2c00': 'GPR_W62',
    '3f2c00': 'GPR_W63',
    '402c00': 'GPR_W64',
    '412c00': 'GPR_W65',
    '422c00': 'GPR_W66',
    '432c00': 'GPR_W67',
    '442c00': 'GPR_W68',
    '452c00': 'GPR_W69',
    '462c00': 'GPR_W70',
    '472c00': 'GPR_W71',
    '482c00': 'GPR_W72',
    '492c00': 'GPR_W73',
    '4a2c00': 'GPR_W74',
    '4b2c00': 'GPR_W75',
    '4c2c00': 'GPR_W76',
    '4d2c00': 'GPR_W77',
    '4e2c00': 'GPR_W78',
    '4f2c00': 'GPR_W79',
    '502c00': 'GPR_W80',
    '512c00': 'GPR_W81',
    '522c00': 'GPR_W82',
    '532c00': 'GPR_W83',
    '542c00': 'GPR_W84',
    '552c00': 'GPR_W85',
    '562c00': 'GPR_W86',
    '572c00': 'GPR_W87',
    '582c00': 'GPR_W88',
    '592c00': 'GPR_W89',
    '5a2c00': 'GPR_W90',
    '5b2c00': 'GPR_W91',
    '5c2c00': 'GPR_W92',
    '5d2c00': 'GPR_W93',
    '5e2c00': 'GPR_W94',
    '5f2c00': 'GPR_W95',
    '602c00': 'GPR_W96',
    '612c00': 'GPR_W97',
    '622c00': 'GPR_W98',
    '632c00': 'GPR_W99',
    '642c00': 'GPR_W100',
    '012c01': 'REG_CMDS_ADD_CONSTANT_TO_ACCUMULATOR',
    '022c01': 'REG_CMDS_ACCUMULATOR_DIVIDE_CONSTANT',
    '032c01': 'REG_CMDS_XOR_CONSTANT_TO_ACCUMULATOR',
    '042c01': 'REG_CMDS_ACCUMULATOR_MULTIPLY_CONSTANT',
    '052c01': 'REG_CMDS_AND_CONSTANT_TO_ACCUMULATOR',
    '062c01': 'REG_CMDS_OR_CONSTANT_TO_ACCUMULATOR',
    '072c01': 'REG_CMDS_SUBSTRACT_CONSTANT_FROM_ACCUMULATOR',
    '082c01': 'REG_CMDS_SHIFT_LEFT_ACCUMULATOR_BY_CONSTANT',
    '092c01': 'REG_CMDS_SHIFT_RIGHT_ACCUMULATOR_BY_CONSTANT',
    '0a2c01': 'REG_CMDS_ADD_REGISTER_TO_ACCUMULATOR',
    '0b2c01': 'REG_CMDS_ACCUMULATOR_DIVIDE_REGISTER_',
    '0c2c01': 'REG_CMDS_XOR_REGISTER_TO_ACCUMULATOR',
    '0d2c01': 'REG_CMDS_ACCUMULATOR_MULTIPLY_REGISTER_',
    '0e2c01': 'REG_CMDS_AND_REGISTER_TO_ACCUMULATOR',
    '0f2c01': 'REG_CMDS_OR_REGISTER_TO_ACCUMULATOR',
    '102c01': 'REG_CMDS_SUBSTRACT_REGISTER_FROM_ACCUMULATOR',
    '112c01': 'REG_CMDS_SHIFT_LEFT_ACCUMULATOR_BY_REGISTER_',
    '122c01': 'REG_CMDS_SHIFT_RIGHT_ACCUMULATOR_BY_REGISTER_',
    '132c01': 'REG_CMDS_ABSOLUTE_ACCUMULATOR',
    '142c01': 'REG_CMDS_ACCUMULATOR_COMPLEMENT',
    '152c01': 'REG_CMDS_WRITE_ACCUMULATOR_TO_REGISTER',
    '162c01': 'REG_CMDS_WRITE_REGISTER32_TO_ACCUMULATOR',
    '172c01': 'REG_CMDS_WRITE_REGISTER16_TO_ACCUMULATOR',
    '012c02': 'SEQ_CMDS_DO_IF_IO_IS_"OFF"',
    '022c02': 'SEQ_CMDS_DO_IF_IO_IS_"ON"',
    '032c02': 'SEQ_CMDS_END_PROGRAM',
    '042c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_BELOW_VAL',
    '052c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_HIGHER_VAL',
    '062c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_EQUAL_VAL',
    '072c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_UNEQUAL_VAL',
    '082c02': 'SEQ_CMDS_IF_IO_IS_"OFF"',
    '092c02': 'SEQ_CMDS_IF_IO_IS_"ON"',
    '0a2c02': 'SEQ_CMDS_IF_BIT_OF_ACCUMULATOR_IS_SET',
    '0b2c02': 'SEQ_CMDS_IF_BIT_OF_ACCUMULATOR_IS_CLEAR',
    '0c2c02': 'SEQ_CMDS_REPEAT',
    '0d2c02': 'SEQ_CMDS_WAIT_MILISECONDS_VAL',
    '0e2c02': 'SEQ_CMDS_WAIT_FOR_INDEX',
    '0f2c02': 'SEQ_CMDS_WAIT_FOR_IO_TO_BE_"OFF"',
    '102c02': 'SEQ_CMDS_WAIT_FOR_IO_TO_BE_"ON"',
    '112c02': 'SEQ_CMDS_IF_ANALOG_IS_BELOW',
    '122c02': 'SEQ_CMDS_IF_ANALOG_IS_HIGHER',
    '132c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_BELOW_REGISTER',
    '142c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_HIGHER_REGISTER',
    '152c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_EQUAL_REGISTER',
    '162c02': 'SEQ_CMDS_IF_ACCUMULATOR_IS_UNEQUAL_REGISTER',
    '172c02': 'SEQ_CMDS_WAIT_MILLISECONDS_REGISTER',
    '012c03': 'LEARNED_POS_LEARN_CURR_POS',
    '022c03': 'LEARNED_POS_LEARN_TGT_POS',
    '032c03': 'LEARNED_POS_MOVE_INDEX_TABLE_POS',
    '012c04': 'MACRO_CMDS_MACRO_CALL',
    '022c04': 'MACRO_CMDS_RETURN_FROM_MACRO_CALL',
    '032c04': 'MACRO_CMDS_MACRO_JUMP',
    '042c04': 'MACRO_CMDS_RESET_MACROS',
    '052c04': 'MACRO_CMDS_JUMP_ABSOLUTE',
    '062c04': 'MACRO_CMDS_JUMP_RELATIVE',
    '072c04': 'MACRO_CMDS_MACRO_CALL_INTERRUPT',
    '082c04': 'MACRO_CMDS_UNPUSH_MACRO',
    '012c05': 'MACRO_ACC_NUM',
    '022c05': 'MACRO_ACC_CMD',
    '032c05': 'MACRO_CMD',
    '042c05': 'MACRO_UNPROTECTED_ACCESS',
    '012c06': 'TIMERS_ACC_1_COUNT_UP_VAL',
    '022c06': 'TIMERS_ACC_2_COUNT_UP_VAL',
    '032c06': 'TIMERS_ACC_3_COUNT_DOWN_VAL',
    '042c06': 'TIMERS_ACC_4_COUNT_DOWN_VAL',
    '012c07': 'INTERRUPT_1_VECTOR',
    '022c07': 'INTERRUPT_2_VECTOR',
    '032c07': 'INTERRUPT_3_VECTOR',
    '042c07': 'INTERRUPT_4_VECTOR',
    '052c07': 'INTERRUPT_5_VECTOR',
    '062c07': 'INTERRUPT_6_VECTOR',
    '072c07': 'INTERRUPT_7_VECTOR',
    '082c07': 'INTERRUPT_8_VECTOR',
    '092c07': 'INTERRUPT_9_VECTOR',
    '0a2c07': 'INTERRUPT_10_VECTOR',
    '0b2c07': 'INTERRUPT_11_VECTOR',
    '0c2c07': 'INTERRUPT_12_VECTOR',
    '012c08': 'INTERRUPT_1_ENABLED',
    '022c08': 'INTERRUPT_2_ENABLED',
    '032c08': 'INTERRUPT_3_ENABLED',
    '042c08': 'INTERRUPT_4_ENABLED',
    '052c08': 'INTERRUPT_5_ENABLED',
    '062c08': 'INTERRUPT_6_ENABLED',
    '072c08': 'INTERRUPT_7_ENABLED',
    '082c08': 'INTERRUPT_8_ENABLED',
    '092c08': 'INTERRUPT_9_ENABLED',
    '0a2c08': 'INTERRUPT_10_ENABLED',
    '0b2c08': 'INTERRUPT_11_ENABLED',
    '0c2c08': 'INTERRUPT_12_ENABLED',
    '012c09': 'POINTER_ACCESS_POINTER_TO_REG',
    '022c09': 'POINTER_ACCESS_CONTENT_OF_REG',
    '032c09': 'POINTER_ACCESS_WRITE_CONTENT_TO_REG',
    '012c0a': 'MACRO_DEBUG_ACT_NUM',
    '022c0a': 'MACRO_DEBUG_ACT_CMD_NUM',
    '032c0a': 'MACRO_DEBUG_MACRO_STATUS',
    '012c50': 'MON_CONFIG_SAMPLING_RATE',
    '022c50': 'MON_CONFIG_ENABLE_MODE',
    '032c50': 'MON_CONFIG_TRIG_DELAY',
    '012c51': 'MON_RESULT_MAX_ENTRY',
    '022c51': 'MON_RESULT_FILLED_ENTRY_VALS',
    '032c51': 'MON_RESULT_ENTRY_NUM',
    '042c51': 'MON_RESULT_ACT_ENTRY_TABLE_1',
    '052c51': 'MON_RESULT_ACT_ENTRY_TABLE_2',
    '062c51': 'MON_RESULT_ACT_ENTRY_TABLE_3',
    '072c51': 'MON_RESULT_ACT_ENTRY_TABLE_4',
    '012c52': 'MON_MAPPING_CHANNEL_1',
    '022c52': 'MON_MAPPING_CHANNEL_2',
    '032c52': 'MON_MAPPING_CHANNEL_3',
    '042c52': 'MON_MAPPING_CHANNEL_4',
    '012c55': 'MON_TRIG_1_MODE',
    '022c55': 'MON_TRIG_1_SRC_REG',
    '032c55': 'MON_TRIG_1_POS_THRESHOLD',
    '042c55': 'MON_TRIG_1_NEG_THRESHOLD',
    '052c55': 'MON_TRIG_1_DIG_IN_MSK',
    '062c55': 'MON_TRIG_1_DELAY_IN_SAMPLES',
    '012d00': 'OPEN_LOOP_PARAMS_TGT_VOLTAGE',
    '022d00': 'OPEN_LOOP_PARAMS_TGT_FREQ',
    '012ff0': 'HW_CFG_CURR_SENSING_RESISTOR_VAL',
    '022ff0': 'HW_CFG_PREAMPLIFIER_GAIN',
    '032ff0': 'HW_CFG_VGA_AVAIL',
    '042ff0': 'HW_CFG_TEMP_SENSOR_AVAIL',
    '052ff0': 'HW_CFG_MAX_ABSOLUTE_TEMP_MC',
    '062ff0': 'HW_CFG_MIN_ABSOLUTE_TEMP_MC',
    '072ff0': 'HW_CFG_VBUS_SENSOR_AVAIL',
    '082ff0': 'HW_CFG_MAX_ABSOLUTE_VOLTAGE_MV',
    '092ff0': 'HW_CFG_MIN_ABSOLUTE_VOLTAGE_MV',
    '0a2ff0': 'HW_CFG_NOMINAL_CURR_MA_RMS_VAL',
    '0b2ff0': 'HW_CFG_PEAK_CURR_MA_RMS_VAL',
    '0c2ff0': 'HW_CFG_MAXIMUM_PEAK_TIME_100US',
    '0d2ff0': 'HW_CFG_MAXIMUM_CURR_MA_PEAK_VAL',
    '0e2ff0': 'HW_CFG_STEPPER_IN_3PHASES_AVAIL',
    '0f2ff0': 'HW_CFG_NVM_AVAIL',
    '102ff0': 'HW_CFG_HW_ERROR_AVAIL',
    '112ff0': 'HW_CFG_TEMP_SENSOR_OFFSET_MV',
    '122ff0': 'HW_CFG_TEMP_SENSOR_GAIN_MVC',
    '132ff0': 'HW_CFG_VBUS_SENSOR_GAIN',
    '142ff0': 'HW_CFG_DEADTIME_NS',
    '152ff0': 'HW_CFG_PWM_FREQ_SCALE_LEGACY',
    '162ff0': 'HW_CFG_BOOSTRAP_CHARGE_TIME_MS',
    '172ff0': 'HW_CFG_NTC_SENSOR_AVAIL',
    '182ff0': 'HW_CFG_NTC_REXT_OHM',
    '192ff0': 'HW_CFG_NTC_R25_OHM',
    '1a2ff0': 'HW_CFG_NTC_B25_K',
    '1b2ff0': 'HW_CFG_RESOLVER_AVAIL',
    '1c2ff0': 'HW_CFG_NODE_ID_BY_HW',
    '1d2ff0': 'HW_CFG_PWM_FREQ',
    '1e2ff0': 'HW_CFG_AVAIL_DIN',
    '1f2ff0': 'HW_CFG_AVAIL_DOUT',
    '202ff0': 'HW_CFG_AVAIL_AINS',
    '212ff0': 'HW_CFG_AVAIL_ANALOG_OUTPUTS',
    '222ff0': 'HW_CFG_COMMERCIAL_PRODUCT_ID',
    '232ff0': 'HW_CFG_COMMERCIAL_SERIAL',
    '242ff0': 'HW_CFG_2_PHASES_SWITCHING_SCHEME',
    '252ff0': 'HW_CFG_DRIVER_EN_IN_UART_COM',
    '262ff0': 'HW_CFG_AVAIL_CURR_SENSORS',
    '272ff0': 'HW_CFG_DIN_POL_MSK',
    '282ff0': 'HW_CFG_DOUT_POL_MSK',
    '292ff0': 'HW_CFG_ANALOG_REF_VOLTAGE',
    '2a2ff0': 'HW_CFG_AIN_1_2_PARAMS',
    '2b2ff0': 'HW_CFG_AIN_3_4_PARAMS',
    '2c2ff0': 'HW_CFG_ANALOG_OUTPUT_1_2_PARAMS',
    '2d2ff0': 'HW_CFG_MACRO_PARAMS',
    '2e2ff0': 'HW_CFG_SUP_MOTOR_TYPES',
    '2f2ff0': 'HW_CFG_SUP_COMM_INTERFACES',
    '302ff0': 'HW_CFG_SUP_FBS',
    '312ff0': 'HW_CFG_PWM_MAXIMUM_DUTY_CYCLE',
    '322ff0': 'HW_CFG_CURR_LOOP_FREQ',
    '332ff0': 'HW_CFG_POSVEL_LOOP_FREQ',
    '342ff0': 'HW_CFG_SUP_CMD_SRC',
    '352ff0': 'HW_CFG_SAFE_TORQUE_OFF_INPUT',
    '362ff0': 'HW_CFG_ALTERNATIVE_FREQ_PWM_HZ',
    '372ff0': 'HW_CFG_CURR_LOW_PASS_FILTER_OUTPUT',
    '382ff0': 'HW_CFG_AIN_5_PARAMS',
    '392ff0': 'HW_CFG_OPEN_LOAD_PROTECTION_INPUT',
    '3a2ff0': 'HW_CFG_SHUNT_OUTPUT',
    '3b2ff0': 'HW_CFG_BRAKE_OUTPUT',
    '002ff1': 'HW_CFG_PASS',
    '002ff2': 'EDS_VERSION',
    '002ff3': 'HW_AVAIL_REGISTERS',
    '012ff4': 'HW_ID_VERSION',
    '022ff4': 'HW_ID_VARIANT',
    '032ff4': 'HW_ID_PROG_DATE',
    '042ff4': 'HW_ID_CFG_REVISION',
    '002ff5': 'BUILD_NUM',
    '002ffd': 'CURR_RANGE_MAX',
    '002ffe': 'DRIVE_NAME',
    '002fff': 'RESET_DEVICE',
    '00603f': 'ERR_CODE',
    '006040': 'CTL_WORD',
    '006041': 'STS_WORD',
    '006042': 'VL_VEL_TGT',
    '006043': 'VL_VEL_DEM',
    '006044': 'VL_VEL_ACT',
    '016046': 'VL_VEL_MIN',
    '026046': 'VL_VEL_MAX',
    '016048': 'VL_VEL_ACC_DELTA_SPEED',
    '026048': 'VL_VEL_ACC_DELTA_TIME',
    '016049': 'VL_VEL_DEC_DELTA_SPEED',
    '026049': 'VL_VEL_DEC_DELTA_TIME',
    '006060': 'OP_MODE',
    '006061': 'OP_MODE_DISP',
    '006062': 'POS_DEM',
    '006063': 'POS_ACT_INT',
    '006064': 'POS_ACT',
    '006065': 'FOLLOWING_ERR_WINDOW',
    '006066': 'FOLLOWING_ERR_TIMEOUT',
    '006067': 'POS_WINDOW',
    '006068': 'POS_WINDOW_TIME',
    '006069': 'VEL_SENSOR_ACT',
    '00606b': 'VEL_DEM',
    '00606c': 'VEL_ACT',
    '00606d': 'VEL_WINDOW',
    '00606e': 'VEL_WINDOW_TIME',
    '00606f': 'VEL_THRESHOLD',
    '006070': 'VEL_THRESHOLD_TIME',
    '006071': 'TORQUE_TGT',
    '006072': 'TORQUE_MAX',
    '006073': 'CURR_MAX',
    '006074': 'TORQUE_DEM',
    '006075': 'MOTOR_RATED_CURR',
    '006076': 'MOTOR_RATED_TORQUE',
    '006077': 'TORQUE_ACT',
    '006078': 'CURR_ACT',
    '006079': 'DC_LINK_VOLTAGE',
    '00607a': 'POS_TGT',
    '00607c': 'HOME_OFFSET',
    '01607d': 'SW_PLIM_MIN',
    '02607d': 'SW_PLIM_MAX',
    '00607e': 'POLARITY',
    '00607f': 'PROFILE_VEL_MAX',
    '006080': 'MOTOR_SPEED_MAX',
    '006081': 'PROFILE_VEL',
    '006083': 'PROFILE_ACC',
    '006084': 'PROFILE_DEC',
    '006085': 'QSTOP_DEC',
    '006086': 'MOTION_PROFILE_TYPE',
    '006087': 'TORQUE_SLOPE',
    '006088': 'TORQUE_PROFILE_TYPE',
    '01608f': 'PENC_ENC_INCREMENTS',
    '02608f': 'PENC_MOTOR_REVS',
    '016090': 'VENC_ENC_INCREMENTS',
    '026090': 'VENC_MOTOR_REVS',
    '016091': 'GEAR_RATIO_MOTOR_SHAFT_REVS',
    '026091': 'GEAR_RATIO_DRIVING_SHAFT_REVS',
    '016092': 'FEED_CONSTANT',
    '026092': 'FEED_CONSTANT_SHAFT_REVS',
    '006098': 'HOMING_METHOD',
    '016099': 'HOMING_SPEED_SWITCH_SEARCH',
    '026099': 'HOMING_SPEED_ZERO_SEARCH',
    '00609a': 'HOMING_ACC',
    '0060a8': 'SI_UNIT_POS',
    '0060a9': 'SI_UNIT_VEL',
    '0060aa': 'SI_UNIT_ACC',
    '0060b2': 'TORQUE_OFFSET',
    '0160c1': 'INTERP_DATA_RECORD_1ST_SP',
    '0160c2': 'INTERP_TIME_PERIOD_VAL',
    '0260c2': 'INTERP_TIME_PERIOD_INDEX',
    '0160c4': 'INTERP_DATA_CFG_BUF_MAX_SIZE',
    '0260c4': 'INTERP_DATA_CFG_BUF_ACT_SIZE',
    '0360c4': 'INTERP_DATA_CFG_BUF_ORG',
    '0460c4': 'INTERP_DATA_CFG_BUF_POS',
    '0560c4': 'INTERP_DATA_CFG_RECORD_SIZE',
    '0660c4': 'INTERP_DATA_CFG_BUF_CLEAR',
    '0060c5': 'ACC_MAX',
    '0060c6': 'DEC_MAX',
    '0060e0': 'TORQUE_PLIM',
    '0060e1': 'TORQUE_NLIM',
    '0060f4': 'FOLLOWING_ERR_ACT',
    '0060fa': 'CTL_EFFORT',
    '0060fc': 'POS_DEM_INT',
    '0060fd': 'DOUT',
    '0160fe': 'DOUT_PHY',
    '0260fe': 'DOUT_MSK',
    '0060ff': 'VEL_TGT',
    '006402': 'MOTOR_TYPE',
    '006502': 'SUP_DRIVE_MODES',
    '006505': 'HTTP_DRIVE_CATALOG_ADDRESS'
}
""" dict: Mapping of addresses to register IDs. """
