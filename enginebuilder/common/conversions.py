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


# convert_pressure
# val - values to be converted
# input - declares input form
# output - declares output form
def convert_pressure(val, inputt, output):
    # code here
    return 0


def convert_MW(val, inputt, output):
    if (inputt == 0) and (output == 0):
        val = val / 453.59237
    return val
