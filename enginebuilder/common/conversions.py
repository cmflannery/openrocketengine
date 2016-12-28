#!/usr/bin/env python
import numpy as np
# conversions.py performs unit conversions
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


# convert_pressure (expects atm input)
# val - values to be converted
# output - declares output form
#   output == 0
def convert_pressure(val, units):
    if units == "0":
        return float(val) * 14.6959487758  # atm -> psi
    elif units == "1":
        return float(val) * 101325  # atm -> N/m^2
    # code here
    return 0


def convert_MW(val, inputt, output):
    if (inputt == 0) and (output == 0):
        val = val / 453.59237
    return val
