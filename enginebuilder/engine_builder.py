#!/usr/bin/env python
import os
import sys
import inspect
import subprocess
# imports from enginebuilder module
from performance.propellant import *
from performance.equations import *
from nozzle.nozzle import *
from common.prompts import *
from common.gen_output import *
from common.conversions import *
from common.ascii_art import *
# Class definitions used to build engines.
# Manages engine development scripts
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


# engine class retrieves and stores all outputs for each run
class engine(object):
    # engine class is primary class that openrocketengine uses to create a
    # liquid rocket engine
    # inputs and outputs are stored here.
    def __init__(self):
        self.pchamber = 75.0  # assumption for testing

    def start_building(self):
        # create parameters obj
        self.parameters = parameters()
        # create performance/equations obj
        self.performance = performance(self.parameters)
        # create nozzle dimension obj
        self.nozzle = nozzle(self.performance, self.parameters)
        # create outputs obj
        self.outputs = outputs(self)


class parameters(object):
    """ parameters class holds values from propellant.json starts prompts to
 get input parameters from user prompts from /performance/prompts.py"""
    def __init__(self):
        self.pchamber = 75.00  # constant, assumption
        self.get_prompts()
        self.get_prop_data()
        self.convert()

    def get_prompts(self):
        prompt_responses = user_prompts()
        self.units = prompt_responses.units
        self.thrust = prompt_responses.thrust
        self.alt = prompt_responses.alt
        self.propellants = prompt_responses.propellants
        self.pambient = prompt_responses.pambient
        self.pexit = prompt_responses.pexit

    def get_prop_data(self):
        # create prop_values obj
        prop_data = prop_values(self.propellants)
        self.Isp = prop_data.Isp
        self.MR = prop_data.MR
        self.Tc = prop_data.Tc
        self.gamma = prop_data.gamma
        self.L_star = prop_data.L_star
        self.MW = prop_data.MW

    def convert(self):
        # create convert object
        convert_obj = unit_converter(self)


def print_logo_image():
    # prints ascii art of rocket stored in /resources/openrocketengine
    path = os.path.dirname(__file__)
    fname = os.path.join(path, 'resources', 'openrocketengine.txt')

    logo_image = ascii_image(fname)
    logo_image.display_image()


def print_logo_text():
    # display ascii art text
    ShowText = 'OpenRocketEng'

    logo_text = ascii_text(ShowText)
    logo_text.display_text()


def main():
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    print_logo_image()
    print_logo_text()
    print "\n\nLets build a rocket engine!\n"

    eng = engine()
    eng.start_building()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\nKeyboardInterrupt: exiting...\n"
else:
    print "\"engine_builder.py\" must be run as the main script"
