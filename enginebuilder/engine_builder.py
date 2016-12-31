#!/usr/bin/env python
import os
import sys
import inspect
# allow imports from subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
                                 (inspect.getfile(inspect.currentframe()))[0],
                                 "performance")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
                                 (inspect.getfile(inspect.currentframe()))[0],
                                 "nozzle")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
                                 (inspect.getfile(inspect.currentframe()))[0],
                                  "common")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
# imports from 'common' subfolder
from prompts import *
from propellant import prop_values
from equations import performance
from nozzle import nozzle
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
        self.pchamber = 75.0  # assumption for testing

    def start_building(self):
        # create parameters obj
        self.parameters = parameters()
        # create performance/equations obj
        self.performance = performance(self.parameters)
        # create nozzle dimension obj
        self.nozzle = nozzle(self.performance, self.parameters)
        # self.outputs = outputs(self)
        print self.performance.wdot
        print self.parameters.Isp
        print self.parameters.pchamber
        print self.performance.Cf
        print self.performance.pthroat
        print self.performance.epsilon
        print self.nozzle.Athroat
        print self.nozzle.Aexit
        print self.nozzle.Vchamber


class parameters:
    def __init__(self):
        self.pchamber = 75.00  # constant, assumption
        self.start_prompts()
        self.start_propellants()
        self.convert()

    def start_prompts(self):
        self.units = prompt_for_units()
        if self.units == "test":
            self.thrust = 500.00
            self.propellants = ["O2", "CH4"]
            self.pambient = 1.00
            self.pexit = 1.00
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
                self.pambient = 1.00
                self.pexit = 1.00
            elif self.alt == "1":
                self.pambient = 0.00
                # needs to be improved
                self.pexit = 1.00  # very non-ideal assumption..
            self.FoS = prompt_for_FoS()

    def start_propellants(self):
        # create prop_values obj
        prop_data = prop_values(self.propellants)
        self.Isp = prop_data.Isp
        self.MR = prop_data.MR
        self.Tc = prop_data.Tc
        self.gamma = prop_data.gamma
        self.L_star = prop_data.L_star

    def convert(self):
        # temporary implicit unit conversions until unit_converte is finished
        self.pchamber = self.pchamber * 14.6959487758
        self.pambient = self.pambient * 14.6959487758
        self.pexit = self.pexit * 14.6959487758
        self.L_star = self.L_star / 2.54  # temporary implicit conversion


def main():
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print "Lets build a rocket engine!\n"
    eng = engine()
    eng.start_building()

if __name__ == "__main__":
    main()
else:
    print "\"engine_builder.py\" must be run as the main script"
