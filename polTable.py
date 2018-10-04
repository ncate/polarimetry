import numpy as np


def create_weight_vector_table():
    table = {}
    table['HH'] = {}
    table["HH"]["a"] = 45
    table["HH"]["b"] = 0
    table["HH"]["e"] = 0
    table["HH"]["u"] = 0
    table["HH"]["c5"] = 0.707
    table["HH"]["c6"] = 0.707
    table["HH"]["c7"] = 0

    table['HV'] = {}
    table["HV"]["a"] = 90
    table["HV"]["b"] = 90
    table["HV"]["e"] = 0
    table["HV"]["u"] = 0
    table["HV"]["c5"] = 0
    table["HV"]["c6"] = 0
    table["HV"]["c7"] = 1

    table['VV'] = {}
    table["VV"]["a"] = 45
    table["VV"]["b"] = 180
    table["VV"]["e"] = 0
    table["VV"]["u"] = 0
    table["VV"]["c5"] = 0.707
    table["VV"]["c6"] = -0.707
    table["VV"]["c7"] = 0

    table['HH+VV'] = {}
    table["HH+VV"]["a"] = 0
    table["HH+VV"]["b"] = 0
    table["HH+VV"]["e"] = 0
    table["HH+VV"]["u"] = 0
    table["HH+VV"]["c5"] = 1
    table["HH+VV"]["c6"] = 0
    table["HH+VV"]["c7"] = 0

    table['HH-VV'] = {}
    table["HH-VV"]["a"] = 90
    table["HH-VV"]["b"] = 0
    table["HH-VV"]["e"] = 0
    table["HH-VV"]["u"] = 0
    table["HH-VV"]["c5"] = 0
    table["HH-VV"]["c6"] = 1
    table["HH-VV"]["c7"] = 0

    table['LL'] = {}
    table["LL"]["a"] = 90
    table["LL"]["b"] = 45
    table["LL"]["e"] = 0
    table["LL"]["u"] = 90
    table["LL"]["c5"] = 0
    table["LL"]["c6"] = 0.707
    table["LL"]["c7"] = np.complex(0,0.707)

    table["LR"] = {}
    table["LR"]["a"] = 0
    table["LR"]["b"] = 0
    table["LR"]["e"] = 0
    table["LR"]["u"] = 0
    table["LR"]["c5"] = 1
    table["LR"]["c6"] = 0
    table["LR"]["c7"] = 0

    table["RR"] = {}
    table["RR"]["a"] = 90
    table["RR"]["b"] = 45
    table["RR"]["e"] = 0
    table["RR"]["u"] = -90
    table["RR"]["c5"] = 0
    table["RR"]["c6"] = 0.707
    table["RR"]["c7"] = -np.complex(0, 0.707)

    return table
