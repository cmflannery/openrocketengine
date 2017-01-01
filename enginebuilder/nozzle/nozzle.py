#!/usr/bin/env python
# nozzle.py calculated the dimensions of the nozzle based on user input and
# calculated performance parameters
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class nozzle:
    def __init__(self, performance, parameters):
        self.performance = performance
        self.parameters = parameters
        self.gen_nozzle_dims()

    def gen_nozzle_dims(self):
        self.Athroat = self.get_Athroat()
        self.Aexit = self.get_Aexit()
        self.Vchamber = self.get_Vchamber()
        self.Aachamber = self.get_Achamber()

    # Athroat (nozzle throat area)
    #   expects pchamber in atm
    def get_Athroat(self):
        return (self.performance.wdot*self.parameters.Isp) / \
                (self.parameters.pchamber*self.performance.Cf)

    def get_Aexit(self):
        return self.performance.epsilon * self.Athroat

    def get_Vchamber(self):
        return self.parameters.L_star * self.Athroat

    def get_Achamber(self):
        return -1
