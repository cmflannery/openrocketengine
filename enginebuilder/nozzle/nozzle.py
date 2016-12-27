#!/usr/bin/env python
from equations import *
# nozzle.py calculated the dimensions of the nozzle based on user input and
# calculated performance parameters
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


# Athroat (nozzle throat area)
def get_Athroat(var, option):
    wdot = float(var[0])
    Isp = float(var[1])
    pchamber = float(var[2])
    Cf = float(var[3])
    return wdot*Isp/(pchamber*Cf)    
