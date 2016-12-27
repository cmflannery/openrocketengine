#!/usr/bin/env python
import os
import json
from prompts import prompt_for_propellants
# chemistry,py calculates propellant properties and chooses optimum values
# based on use input
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery", "Michael Phalen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"

prop_file = os.path.join(os.getcwd(), 'performance', 'propellant.json')
with open(prop_file) as propellant_raw:
    propellant_data = json.load(propellant_raw)
    propellant_raw.close()


# pull_Isp(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_Isp(propellants):
    for prop in propellant_data["Propellants_Dict"]:
        if (prop["Oxidizer"] == propellants[0]) and \
                (prop["Fuel"] == propellants[1]):
            return prop["Isp"]
    return 0


# pull_MR(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_MR(propellants):
    for prop in propellant_data["Propellants_Dict"]:
        if (prop["Oxidizer"] == propellants[0]) and \
                (prop["Fuel"] == propellants[1]):
            return prop["MR"]
    return 0


# pull_Isp(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_Tc(propellants):
    for prop in propellant_data["Propellants_Dict"]:
        if (prop["Oxidizer"] == propellants[0]) and \
                (prop["Fuel"] == propellants[1]):
            return prop["Tc"]
    return 0


# pull_MR(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_gamma(propellants):
    for prop in propellant_data["Propellants_Dict"]:
        if (prop["Oxidizer"] == propellants[0]) and \
                (prop["Fuel"] == propellants[1]):
            return prop["gamma"]
    return 0


# main()
#   used for testing and debugging
#   only executes when main script
def main():
    propellants = prompt_for_propellants()
    Isp = pull_Isp(propellants)
    MR = pull_MR(propellants)
    print Isp
    print MR

if __name__ == "__main__":
    main()
