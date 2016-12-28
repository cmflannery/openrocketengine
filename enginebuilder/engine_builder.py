#!/usr/bin/env python
import os
import sys
import inspect
# allow imports from subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
        (inspect.getfile(inspect.currentframe()))[0], "performance")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
        (inspect.getfile(inspect.currentframe()))[0], "nozzle")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
        (inspect.getfile(inspect.currentframe()))[0], "common")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
# imports from 'common' subfolder
from prompts import *
from propellant import *
from equations import *
from nozzle import *
from gen_output import *
from conversions import *
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


# engine class retrieves and stores all outputs for each run
class engine:
    def __init__(self):
        self.pchamber = 75.  # assumption for testing

    def start_building(self):
        self.pprompts()
        self.calc_performance(self.thrust, self.propellants, self.units)
        self.calc_nozzle(self.thrust, self.propellants, self.units)
        create_xlsx(self)

    def pprompts(self):
        self.units = prompt_for_units()
        if self.units == "test":
            self.thrust = 500
            self.propellants = ["O2", "CH4"]
            self.pambient = 1
            self.pexit = 1
            print "\nSetting test parameters: "
            print "\t Thrust =",
            print self.thrust
            print "\t Propellants:",
            print self.propellants
            print "\n"
            self.units = "0"
        else:
            self.thrust = prompt_for_thrust(self.units)
            self.propellants = prompt_for_propellants()
            self.alt = prompt_for_altitude()
            if self.alt == "0":
                self.pambient = 1
                self.pexit = 1
            elif self.alt == "1":
                self.pambient = 0
                self.pexit = 1  # very non-ideal assumption.. how can this be improved??
            self.FoS = prompt_for_FoS()

    def calc_performance(self, thrust, propellants, units):
        self.Isp = pull_Isp(propellants)
        self.gamma = pull_gamma(propellants)
        self.Tc = pull_Tc(propellants)
        self.wdot = get_wdot([thrust, self.Isp], 0)
        self.pthroat = get_pthroat([self.pchamber, self.gamma], 0)
        self.epsilon = get_epsilon([self.gamma, self.pchamber, self.pexit], 0)
        self.Cf = get_Cf([self.pexit, self.pchamber, self.pambient, self.gamma,
                          self.epsilon], 0)  # need to get

    def calc_nozzle(self, thrust, propellants, units):
        pchamber_converted = convert_pressure(self.pchamber, self.units)
        self.Athroat = get_Athroat([self.wdot, self.Isp, pchamber_converted,
                                    self.Cf], 0)
        self.Aexit = get_Aexit([self.epsilon, self.Athroat], 0)


def main():
    os.system('cls')  # clear console screen
    print "Lets build a rocket engine!\n"
    eng = engine()
    eng.start_building()

if __name__ == "__main__":
    main()
else:
    print "\"engine_builder.py\" must be run as the main script"
