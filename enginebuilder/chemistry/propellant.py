#!/usr/bin/env python
import json
from prompts import *
# propellant.py defines functions to pull propellant properties from json
# tables
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
