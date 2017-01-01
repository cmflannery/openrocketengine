#!/usr/bin/env python
import numpy as np
# Equations used to define engine parameters and performance
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class performance:
    def __init__(self, parameters):
        self.params = parameters
        self.get_performance()

    def get_performance(self):
        self.g0 = self.get_g0()
        # self.pexit = self.get_pexit(int(self.params.alt))
        self.epsilon = self.get_epsilon(0)
        self.Cf = self.get_Cf(0)
        self.wdot = self.get_wdot(0)
        self.pthroat = self.get_pthroat(0)

    def get_g0(self):
        # set the constant, g0, based on choice of units
        if self.params.units == 0:
            return 32.174  # English Engineering (ft/s/s)
        elif self.params.units == 1:
            return 9.8066  # Metric (m/s/s)
        else:
            return -1

    def get_Rspecific(self):
        # set Rspecific
        if self.paramas.units == 0:
            return 18544.2/self.params.MW  # in^3 lb mol deg R
        elif self.params.units == 1:
            return 8314.459848/self.params.MW
        else:
            return -1

    def get_pexit(self, option):
        # get_pexit sets exit pressure
        # option chooses sea-level or vacuum design
        if option == 0:  # design for sea-level
            return 1.00  # exit pressure in atmospheres
        elif option == 1:  # design for vacuum engine`
            print "NOTE: NOT ALL FEATURES CURRENTLY SUPPORTED FOR VACUUM ENGINES"
            return 0.00

    def get_It(self, option):
        # set total impulse
        if option == 0:
            return self.params.thrust * self.params.time
        else:
            return False

    def get_Isp(self, option):
        # set Isp
        # option chooses form of equation
        if option == 0:
            return self.params.thrust / (self.params.mdot * self.params.g0)
        elif option == 1:
            return self.params.thrust / self.params.wdot
        elif option == 2:
            return self.params.cee_star * self.params.Cf / self.params.g0

    def get_cee_star(self, option):
        # set c* (characteristic velocity)
        if option == 0:
            cee_star = np.sqrt(self.params.g0 * self.params.gamma *
                               self.params.Rspecific * self.params.Tc_ns) / \
                              (self.params.gamma *
                               np.sqrt((2.0 / (self.params.gamma+1)) **
                                       ((self.params.gamma+1) /
                                        (self.params.gamma-1))))
            return cee_star

    def get_Cf(self, option):
        # set Cf (Coefficient of Thrust)
        if option == 0:
            Cf = np.sqrt((2*self.params.gamma**2)/(self.params.gamma-1) *
                         (2/(self.params.gamma+1)) **
                         ((self.params.gamma+1) / (self.params.gamma-1)) *
                         (1-(self.params.pexit/self.params.pchamber) **
                         ((self.params.gamma-1)/self.params.gamma))) + \
                self.epsilon*((self.params.pexit-self.params.pambient) /
                              self.params.pchamber)
            return Cf

    def get_wdot(self, option):
        # set wdot (weight flow rate)
        if option == 0:
            return self.params.thrust / self.params.Isp

    def get_pthroat(self, option):
        # set pthroat (nozzle throat pressure)
        if option == 0:
            return self.params.pchamber * ((self.params.gamma + 1)/2) ** \
                ((-self.params.gamma)/(self.params.gamma-1))

    def get_epsilon(self, option):
        # set epsilon (theoretical expansion ratio)
        if option == 0:
            return ((2/(self.params.gamma+1))**(1/(self.params.gamma-1)) *
                    (self.params.pchamber/self.params.pexit) **
                    (1/self.params.gamma)) / \
                np.sqrt(((self.params.gamma+1)/(self.params.gamma-1)) *
                        (1-(self.params.pexit/self.params.pchamber) **
                         ((self.params.gamma-1)/self.params.gamma)))
