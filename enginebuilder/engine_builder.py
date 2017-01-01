#!/usr/bin/env python
import os
import sys
import inspect
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
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
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"

# debugging option
debug = False


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

        # debugging prints
        if debug:
            print self.performance.wdot
            print self.parameters.Isp
            print self.parameters.pchamber
            print self.performance.Cf
            print "L_star: ",
            print self.parameters.L_star
            print self.performance.pthroat
            print self.performance.epsilon
            print "Athroat: ",
            print self.nozzle.Athroat
            print self.nozzle.Aexit
            print self.nozzle.Vchamber


class parameters(object):
    # parameters class holds values from propellant.json
    # starts prompts to get input parameters from user
    #   prompts from /performance/prompts.py
    def __init__(self):
        self.pchamber = 75.00  # constant, assumption
        self.start_prompts()
        self.start_propellants()
        self.convert()

    def start_prompts(self):
        self.units = prompt_for_units()
        if self.units == "test":
            self.test_case()
        else:
            self.thrust = prompt_for_thrust(self.units)
            self.propellants = prompt_for_propellants()
            self.alt = prompt_for_altitude()
            if self.alt == "0":
                self.pambient = 1.00
                self.pexit = 1.00
            elif self.alt == "1":
                self.pambient = 0.00
                self.pexit = 0.10
            self.FoS = prompt_for_FoS()

    def test_case(self):
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
            self.alt = "0"

    def start_propellants(self):
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
    fname = os.path.join(os.getcwd(), 'resources', 'openrocketengine.txt')
    with open(fname, 'r') as fin:
        print fin.read()


def print_logo_text():
    # display ascii art text
    ShowText = 'OpenRocketEng'

    font = ImageFont.truetype('arialbd.ttf', 10)  # load the font
    size = font.getsize(ShowText)  # calc the size of text in pixels
    image = Image.new('1', size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ShowText, font=font)  # render the text to the bitmap
    for rownum in range(size[1]):
        # scan the bitmap:
        # print ' ' for black pixel and
        # print '#' for white one
        line = []
        for colnum in range(size[0]):
            if image.getpixel((colnum, rownum)):
                line.append(' '),
            else:
                line.append('#'),
        print ''.join(line)


def main():
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print_logo_image()
    print_logo_text()
    print "\n\nLets build a rocket engine!\n"

    eng = engine()
    eng.start_building()

if __name__ == "__main__":
    main()
else:
    print "\"engine_builder.py\" must be run as the main script"
