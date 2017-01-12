#!/usr/bin/env python
import numpy as np
# conversions.py performs unit conversions
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class unit_converter(object):
    def __init__(self, parameters):
        self.params = parameters
        # start conversions
        self.start_pressure_conversions()
        self.convert_MW()
        self.convert_L_star()

    def start_pressure_conversions(self):
        self.params.pchamber = self.convert_pressure(self.params.pchamber)
        self.params.pexit = self.convert_pressure(self.params.pexit)
        self.params.pambient = self.convert_pressure(self.params.pambient)

    def convert_pressure(self, val):
        # converts pressure from atm to psi or N/m^2
        if self.params.units == "0":
            return float(val) * 14.6959487758  # atm -> psi
        elif self.params.units == "1":
            return float(val) * 101325.00  # atm -> N/m^2
        else:
            return -1

    def convert_MW(self):
        if self.params.units == "0":
            self.params.MW = self.params.MW * 0.002204622
            return 0
        elif self.params.units == "1":
            self.params.MW = self.params.MW
            return 0
        else:
            return -1

    def convert_L_star(self):
        if self.params.units == "0":
            self.params.L_star = self.params.L_star / 2.54
            return 0
        elif self.params.units == "1":
            self.params.L_star = self.params.L_star
            return 0
        else:
            return -1
