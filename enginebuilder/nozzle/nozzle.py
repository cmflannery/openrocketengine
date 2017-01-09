#!/usr/bin/env python
import numpy as np
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


class nozzle(object):
    def __init__(self, performance, parameters):
        self.performance = performance
        self.parameters = parameters
        self.gen_nozzle_dims()

    def gen_nozzle_dims(self):
        self.Athroat = self.get_Athroat()
        self.Dthroat = self.get_Dthroat()
        self.Aexit = self.get_Aexit()
        self.Vchamber = self.get_Vchamber()
        self.Aachamber = self.get_Achamber()
        self.L = self.get_L()

    # Athroat (nozzle throat area)
    #   expects pchamber in atm
    def get_Athroat(self):
        """ returns cros-sectional area of throat """
        return (self.performance.wdot*self.parameters.Isp) / \
               (self.parameters.pchamber*self.performance.Cf)

    def get_Dthroat(self):
        """ returns diameter of throat """
        return np.sqrt(self.Athroat * 4.0 / np.pi)

    def get_Rthroat(self):
        """ returns radius of throat """
        return self.Dthroat / 2.0

    def get_Aexit(self):
        """ returns exit area """
        return self.performance.epsilon * self.Athroat

    def get_Vchamber(self):
        """ returns volume of the chamber """
        return self.parameters.L_star * self.Athroat

    def get_Achamber(self):
        """ returns cros-sectional area of the chamber """
        return -1

    def get_L(self):
        """ returns length of 15 degree conic based on expansion ratio """
        return ((np.sqrt(self.performance.epsilon) * self.Dthroat) -
                self.Dthroat) / np.tan(15.00/180.00*np.pi)


class bell(object):
    """Define dimensions and parameters for an 80deg bell nozzle."""
    def __init__(self, nozzle_obj, bell_percent):
        self.nozzle_obj = nozzle_obj
        self.bell_percent = bell_percent
        pass

    def get_Lbell(self):
        """ return bell length """
        return -1

    def before_throat(self):
        """ returns radius of curvature before throat """
        ratio = 1.5  # see Huzel and Huang
        self.D11 = nozzle_obj.Dthroat * ratio

    def after_throat(self):
        """ returns radius of curvature after throat """
        ratio = 0.382
        self.D12 = nozzle_obj.Dthroat * ratio

    def get_N():
        pass


class conic(object):
    """docstring for conic."""
    def __init__(self, arg):
        super(conic, self).__init__()
        pass
