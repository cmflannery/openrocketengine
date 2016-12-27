#!/usr/bin/env python
import os
import sys
import inspect
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
        (inspect.getfile(inspect.currentframe()))[0], "performance")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
        (inspect.getfile(inspect.currentframe()))[0], "nozzle")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
from equations import *
from propellant import *
# Calculations performed here use equations to determine engine design based
# on use input
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


# Constants (Version 1.0)
pchamber = 68  # atm


def calc_performance(thrust, propellants, units):
    Isp = pull_Isp(propellants)
    gamma = pull_gamma(propellants)
    Tc = pull_Tc(propellants)
    wdot = get_wdot([thrust, Isp], 0)
    pthroat = get_pthroat([pchamber, gamma], 0)

    print wdot
    print pthroat
    return 0


if __name__ == "__main__":
    calc_performance(500, ["O2", "CH4"], 1)
