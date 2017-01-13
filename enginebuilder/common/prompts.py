#!/usr/bin/env python
# Equations used to define engine parameters and performance
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class UserPrompts(object):
    def __init__(self):
        self.start_prompts()
        pass

    def start_prompts(self):
        self.units = self.prompt_for_units()
        if self.units == "test":
            self.test_case()
        else:
            self.thrust = self.prompt_for_thrust()
            self.propellants = self.prompt_for_propellants()
            self.alt = self.prompt_for_altitude()
            if self.alt == "0":
                self.pambient = 1.00
                self.pexit = 1.00
            elif self.alt == "1":
                self.pambient = 0.00
                self.pexit = 0.10
            self.FoS = self.prompt_for_FoS()

    def test_case(self):
            self.units = "0"
            self.alt = "0"
            self.thrust = 500.00
            self.propellants = ["O2", "CH4"]
            self.pambient = 1.00
            self.pexit = 1.00
            # print to user that test params are being set
            print "\nSetting test parameters: "
            print "\t Thrust =",
            print self.thrust
            print "\t Propellants:",
            print self.propellants
            print "\n"
            # finish printing

    def prompt_for_units(self):
        confirmed = False
        while not(confirmed):
            units = raw_input("Enter '0' to use English Engineering Units and '1' to use Metric Units \n(Note: Enter 'test' to use test case): ")
            if units == "0":
                print "Using English Engineering Units."
                confirmed = True
            elif units == "1":
                print "Using Metric Units."
                confirmed = True
            elif units.lower() == "test":
                return "test"
            else:
                print "Enter '1' or '0'"
        return units

    def prompt_for_thrust(self):
        confirmed = False
        while not(confirmed):
            if self.units == "0":
                thrust = raw_input("Enter the target thrust (lbf): ")
            elif self.units == "1":
                thrust = raw_input("Enter the target thrust (N): ")
            else:
                print "Error: Units not properly declared."
            print "Thrust: ",
            print thrust
            while True:
                verify = raw_input("Correct? [Y/n]: ")
                verify = verify.upper()
                if verify == "Y":
                    confirmed = True
                    return float(thrust)
                elif verify == "N":
                    confirmed = False
                    break
                else:
                    print "Enter 'Y' or 'n'"
        return -1

    # prompt_for_propellants():
    #   prompt user for propellants
    def prompt_for_propellants(self):
        confirmed = False
        propellants = []
        while not(confirmed):
            propellants = []
            propellants.append(raw_input("Enter oxidizer in atomic forumula, i.e. O2: "))
            propellants.append(raw_input("Enter fuel in atomic formula/shorthand, i.e. RP1: "))
            propellants[0] = propellants[0].upper()
            propellants[1] = propellants[1].upper()
            print "Oxidizer: ",
            print propellants[0]
            print "Fuel: ",
            print propellants[1]
            while True:
                response = raw_input("Correct? [Y/n]: ")
                if response.upper() == 'Y':
                    confirmed = True
                    break
                elif response.upper() == 'N':
                    confirmed = False
                    break
                else:
                    print "Please enter Y or n"
        return propellants

    def prompt_for_altitude(self):
        confirmed = False
        while not(confirmed):
            alt = raw_input("Enter '0' to design an engine for Sea-level or '1' for vacuum: ")
            if alt == "0":
                print "Designing for Sea-level."
                confirmed = True
            elif alt == "1":
                print "Vacuum engine design is not fully supported."
                print "Designing for Vacuum."
                confirmed = True
            else:
                print "Enter '1' or '0'"
        return alt

    def prompt_for_FoS(self):
        confirmed = False
        while not(confirmed):
            FoS = raw_input("Enter the desired factor of safety. \n(Note: 1.4 standard): ")
            print "FoS =",
            print FoS
            while True:
                response = raw_input("Is this value correct? [Y/n]: ")
                if response.lower() == "y":
                    confirmed = True
                    return FoS
                elif response.lower() == "n":
                    break
                else:
                    print "Please enter 'Y' or 'n'"
        return float(FoS)

    def prompt_for_nozzle(self):
        confirmed = False
        while not(confirmed):
            print "\nChoose a nozzle contour:"
            print "\t1. Conical"
            print "\t2. 80% bell"
            print "Enter your choice: ",
            nozzle_contour = raw_input()
            print "Nozzle Contour =",
            print nozzle_contour
            while True:
                response = raw_input("Is this value correct? [Y/n]: ")
                if response.lower() == "y":
                    confirmed = True
                    return nozzle_contour
                elif response.lower() == "n":
                    break
                else:
                    print "Please enter 'Y' or 'n'"
        return float(nozzle_contour)
