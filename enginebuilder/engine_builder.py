""" engine_builder is the openrocketengine module """
#!/usr/bin/env python
import os
import subprocess
# imports from enginebuilder module
import enginebuilder.performance.propellant as prop
import enginebuilder.performance.equations as eqs
import enginebuilder.tca.nozzle as nzl
import enginebuilder.common.prompts as pts
import enginebuilder.common.gen_output as genout
import enginebuilder.common.conversions as conv
import enginebuilder.common.ascii_art as ascii_art
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
class Engine(object):
    """Create and optimize liquid engine design"""
    def __init__(self):
        self.pchamber = 75.0  # assumption for testing
        self.start_building()

    def start_building(self):
        """Create objects necessary to build and optimze engine"""
        # create parameters obj
        self.parameters = Parameters()
        # create performance/equations obj
        self.performance = eqs.Performance(self.parameters)
        # create nozzle dimension obj
        self.nozzle = nzl.Nozzle(self.performance, self.parameters)
        # create outputs obj
        self.outputs = genout.Outputs(self)


class Parameters(object):
    """parameters prompt user for inputs and pull data from resuorces"""
    def __init__(self):
        self.pchamber = 75.00  # constant, assumption
        self.get_prompts()
        self.get_prop_data()
        if self.units == '1':
            self.convert()

    def get_prompts(self):
        """get_prompts() creates UserPrompts instance

        responses are saved to Parameters instance as intrinsic Parameters"""
        prompt_responses = pts.UserPrompts()
        self.units = prompt_responses.units
        self.thrust = prompt_responses.thrust
        self.alt = prompt_responses.alt
        self.propellants = prompt_responses.propellants
        self.pambient = prompt_responses.pambient
        self.pexit = prompt_responses.pexit

    def get_prop_data(self):
        """get_prop_data() creates a PropValues instance

        results are saved to Parameters instance as intrinsic Parameters"""
        # create prop_values obj
        propdata = prop.PropValues(self.propellants)
        self.Isp = propdata.Isp
        self.MR = propdata.MR
        self.Tc = propdata.Tc
        self.gamma = propdata.gamma
        self.L_star = propdata.L_star
        self.MW = propdata.MW

    def convert(self):
        """convert creates an instances of the UnitConverter object

        if the user uses metric units, this method is called and the results
        are used to convert the units taken from data resources"""
        # create convert object
        convert_obj = conv.UnitConverter(self)
        # self.Tc = convert_obj.Tc
        self.L_star = convert_obj.L_star
        self.MW = convert_obj.MW


def print_logo_image():
    """print rocket image (ascii art) to console"""
    # prints ascii art of rocket stored in /resources/openrocketengine
    path = os.path.dirname(__file__)
    fname = os.path.join(path, 'resources', 'openrocketengine.txt')

    logo_image = ascii_art.AsciiImage(fname)
    logo_image.display_image()


def print_logo_text():
    """print OpenRocketEng to console"""
    # display ascii art text
    text_to_print = 'OpenRocketEng'

    logo_text = ascii_art.AsciiText(text_to_print)
    logo_text.display_text()


def main():
    """main function, starts program"""
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    print_logo_image()
    print_logo_text()
    print "\n\nLets build a rocket engine!\n"

    eng = Engine()
    eng.start_building()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\nKeyboardInterrupt: exiting...\n"
else:
    print "\"engine_builder.py\" must be run as the main script"
