#!/usr/bin/env python
import os
import json
""" Design and determine propellant values """

path = os.path.dirname(__file__)
prop_file = os.path.join(path, 'propellant_resources',
                         'propellant.json')
with open(prop_file) as propellant_raw:
    propellant_data = json.load(propellant_raw)
    propellant_raw.close()


class PropValues(object):
    def __init__(self, propellants):
        self.propellants = propellants
        self.pull_all()

    def pull_all(self):
        self.Isp = self.pull_Isp()
        self.MR = self.pull_MR()
        self.Tc = self.pull_Tc()
        self.gamma = self.pull_gamma()
        self.L_star = self.pull_L_star()
        self.MW = self.pull_MW()

    # pull_Isp(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_Isp(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["Isp"]  # in s
        return 0

    # pull_MR(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_MR(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["MR"]  # unitless
        return 0

    # pull_Isp(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_Tc(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["Tc"]  # in K
        return 0

    # pull_MR(propellants[], propellant_data[])
    #   propellants[0] : Oxidizer
    #   propellants[1] : Fuel
    def pull_gamma(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["gamma"]  # unitless
        return 0

    def pull_MW(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["MW"]  # in g/mol
        return 0

    def pull_L_star(self):
        for prop in propellant_data["Propellants_Dict"]:
            if (prop["Oxidizer"] == self.propellants[0]) and \
                    (prop["Fuel"] == self.propellants[1]):
                return prop["L_star"]  # in cm
        return 0
