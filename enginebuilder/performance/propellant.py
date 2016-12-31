#!/usr/bin/env python
import os
import json
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


class prop_values:
    def __init__(self, propellants):
        self.propellants = propellants
        self.pull_all()

    def pull_all(self):
        self.Isp = self.pull_Isp()
        self.MR = self.pull_MR()
        self.Tc = self.pull_Tc()
        self.gamma = self.pull_gamma()

    # pull_Isp(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_Isp(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["Isp"]
        return 0

    # pull_MR(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_MR(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["MR"]
        return 0

    # pull_Isp(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_Tc(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["Tc"]
        return 0

    # pull_MR(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_gamma(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["gamma"]
        return 0

    def pull_MW(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["MW"]
        return 0
