#!/usr/bin/env python
import numpy as np
# Equations used to define engine parameters and performance
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
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
        self.Pexit = self.get_Pexit(0)
        self.epsilon = self.get_epsilon(0)
        self.Cf = self.get_Cf(0)
        self.wdot = self.get_wdot(0)
        self.pthroat = self.get_pthroat(0)

    # gravitational constant
    #   Generally,
    #     get_g0(units):
    #   units == 0
    #     English Engineering (ft/s/s)
    #   units == 1
    #     Metric (m/s/s)
    def get_g0(self):
        if self.params.units == 0:
            return 32.174
        elif self.params.units == 1:
            return 9.8066
        else:
            return -1

    def get_Rspecific(self):
        if self.paramas.units == 0:
            return 18544.2/(self.params.MW*2.20462)  # in^3 lb mol deg R
        elif self.params.units == 1:
            return 8314.459848/self.params.MW
        else:
            return -1

    # exit pressure
    #   Generally,
    #     get_Pexit(option):
    #   option == 0
    #     Sea-level, N/m**2
    #   option == 1
    #     Sea-level, psi
    #   option == 2
    #     Vacuum
    def get_Pexit(self, option):
        if option == 0:
            return 101325.00   # exit pressure in atmospheres
        elif option == 1:
            return 14.6959
        elif option == 2:
            print "NOTE: NOT ALL FEATURES CURRENTLY SUPPORTED FOR VACUUM ENGINES"
            return 0.00

    # total impulse
    #   Generally,
    #     get_It(var, option):
    #   option == 0:
    #     var[] = thrust, time
    #     get_It = thrust * time
    def get_It(self, option):
        if option == 0:
            return self.params.thrust * self.params.time
        else:
            return False

    # specific impulse
    #   Generally,
    #     get_Isp(var, option)
    #   option == 0:
    #       Isp = thrust/(mdot * g0)
    #   option == 1:
    #       Isp = thrust/wdot
    #   option == 2:
    #       Isp = cee_star*Cf/g0
    def get_Isp(self, option):
        if option == 0:
            return self.params.thrust / (self.params.mdot * self.params.g0)
        elif option == 1:
            return self.params.thrust / self.params.wdot
        elif option == 2:
            return self.params.cee_star * self.params.Cf / self.params.g0

    # c* (characteristic velocity)
    #   Generally.
    #       get_cee_star(var, option)
    #   option == 0:
    #
    def get_cee_star(self, option):
        if option == 0:
            cee_star = np.sqrt(self.params.g0 * self.params.gamma *
                               self.params.Rspecific * self.params.Tc_ns) / \
                              (self.params.gamma *
                               np.sqrt((2.0 / (self.params.gamma+1)) **
                                       ((self.params.gamma+1) /
                                        (self.params.gamma-1))))
            return cee_star

    # Cf (Coefficient of thrust)
    #   Generally,
    #       get_Cf(var, option)
    def get_Cf(self, option):
        if option == 0:
            Cf = np.sqrt((2*self.params.gamma**2)/(self.params.gamma-1) *
                         (2/(self.params.gamma+1)) **
                         ((self.params.gamma+1) / (self.params.gamma-1)) *
                         (1-(self.params.pexit/self.params.pchamber) **
                         ((self.params.gamma-1)/self.params.gamma))) + \
                self.epsilon*((self.params.pexit-self.params.pambient) /
                              self.params.pchamber)
            return Cf

    # wdot (weight flow rate)
    #   Generally,
    #       get_wdot(var, option)
    #   Option == 0:
    def get_wdot(self, option):
        if option == 0:
            return self.params.thrust / self.params.Isp

    # Pthroat (nozzle throat pressure)
    #   Generally,
    #       get_wdot(var, option)
    #   Option == 0:
    def get_pthroat(self, option):
        if option == 0:
            return self.params.pchamber * ((self.params.gamma + 1)/2) ** \
                ((-self.params.gamma)/(self.params.gamma-1))

    # epsilon (theoretical expansion ratio)
    #   option == 0:
    #       Sea-level
    #
    def get_epsilon(self, option):
        if option == 0:
            return ((2/(self.params.gamma+1))**(1/(self.params.gamma-1)) *
                    (self.params.pchamber/self.params.pexit) **
                    (1/self.params.gamma)) / \
                np.sqrt(((self.params.gamma+1)/(self.params.gamma-1)) *
                        (1-(self.params.pexit/self.params.pchamber) **
                         ((self.params.gamma-1)/self.params.gamma)))
