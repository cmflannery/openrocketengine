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
#   expects pchamber in atm
def get_Athroat(var, option):
    if option == 0:
        wdot = float(var[0])
        Isp = float(var[1])
        pchamber = float(var[2])
        pchamber = pchamber * 14.6959487758  # convert from atm to psi
        Cf = float(var[3])
        return wdot*Isp/(pchamber*Cf)
    return -1  # error, invalid option


def get_Aexit(var, option):
    if option == 0:
        epsilon = var[0]
        Athroat = var[1]
        return epsilon*Athroat
    return -1  # error, invalid option
