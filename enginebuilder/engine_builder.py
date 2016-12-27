#!/usr/bin/env python
import os
import sys
import inspect
# allow imports from subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
        (inspect.getfile(inspect.currentframe()))[0], "performance")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
# imports from 'common' subfolder
from prompts import *
from calculations import *
# Class definitions used to build engines.
# Manages engine development scripts
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


def main():
    units = prompt_for_units()
    thrust = prompt_for_thrust(units)
    propellants = prop.prompt_for_propellants()

    calc_performance(thrust, propellants, units)


if __name__ == "__main__":
    print "Lets build a rocket engine!\n"

    main()
else:
    print "\"engine_builder.py\" must be run as the main script"
