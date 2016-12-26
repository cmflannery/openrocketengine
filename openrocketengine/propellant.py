#!/usr/bin/env python
import os
import json
from prompts import *
# chemistry,py calculates propellant properties and chooses optimum values
# based on use input
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"

with open('propellant.json') as propellant_raw:
    propellant_data = json.load(propellant_raw)
    propellant_raw.close()


# prompt_for_propellants():
#   prompt user for propellants
def prompt_for_propellants():
    confirmed = False
    propellants = []
    while not(confirmed):
        propellants = []
        propellants.append(raw_input("Enter oxidizer in atomic forumula, \
                i.e. O2: "))
        propellants.append(raw_input("Enter fuel in atomic formula/shorthand, \
                i.e. RP1: "))
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


# pull_Isp(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_Isp(propellants, propellant_data):
    for prop in propellant_data["Propellants_Dict"]:
        if (prop["Oxidizer"] == propellants[0]) and \
                (prop["Fuel"] == propellants[1]):
            return prop["Isp"]
    return 0


# pull_MR(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_MR(propellants, propellant_data):
    for prop in propellant_data["Propellants_Dict"]:
        if (prop["Oxidizer"] == propellants[0]) and \
                (prop["Fuel"] == propellants[1]):
            return prop["MR"]
    return 0


# main()
#   used for testing and debugging
#   only executes when main script
def main():
    propellants = prompt_for_propellants()
    Isp = pull_Isp(propellants, propellant_data)
    MR = pull_MR(propellants, propellant_data)
    print Isp
    print MR

if __name__ == "__main__":
    main()
