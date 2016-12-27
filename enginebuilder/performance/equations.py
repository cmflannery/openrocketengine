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


# import test
def import_test():
    print "equations imported"


# gravitational constant
#   Generally,
#     get_g0(units):
#   units == 0
#     English Engineering (ft/s/s)
#   units == 1
#     Metric (m/s/s)
def get_g0(units):
    if units == 0:
        return 32.174
    elif units == 1:
        return 9.8066
    else:
        return False


# exit pressure
#   Generally,
#     get_Pexit(option):
#   option == 0
#     Sea-level, N/m**2
#   option == 1
#     Sea-level, psi
#   option == 2
#     Vacuum
def get_Pexit(option):
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
#     var[] = force, time
#     get_It = force * time
def get_It(var, option):
    if option == 0:
        force = float(var[0])  # force float to preserve accuracy
        time = float(var[1])   #
        return force * time
    else:
        return False


# specific impulse
#   Generally,
#     get_Isp(var, option)
#   option == 0:
#       Isp = force/(mdot * g0)
#   option == 1:
#       Isp = force/wdot
#   option == 2:
#       Isp = cee_star*Cf/g0
def get_Isp(var, option):
    if option == 0:
        force = float(var[0])
        mdot = float(var[1])
        g0 = float(var[2])
        return force/(mdot*g0)
    elif option == 1:
        force = float(vat[0])
        wdot = float(var[1])
        return force/wdot
    elif option == 2:
        cee_star = float(var[0])
        Cf = float(var[1])
        g0 = float(var[2])
        return cee_star*Cf/g0


# c* (characteristic velocity)
#   Generally.
#       get_cee_star(var, option)
#   option == 0:
#
def get_cee_star(var, option):
    if option == 0:
        Rspecific = float(var[0])
        Tc_ns = float(var[1])
        g0 = float(var[2])
        gamma = float(var[3])
        cee_star = np.sqrt(g0*gamma*Rspecific*Tc_ns) / (gamma *
                    np.sqrt((2/(gamma+1))**((gamma+1)/(gamma-1))))
        return cee_star


# Cf (Coefficient of thrust)
#   Generally,
#       get_Cf(var, option)
def get_Cf(var, option):
    if option == 0:
        pe = var[0]  # exit pressure
        pc = var[1]  # chamber pressure at nozzle stagnation
        pa = var[2]  # ambient pressure
        gamma = var[3]  # ratio of coefficients of heat
        epsilon = var[4]  # nozzle area expansion ratio
        Cf = np.sqrt((2*gamma**2)/(gamma-1) *
                (2/(gamma+1))**((gamma+1)/(gamma-1)) *
                (1-(pe/pc)**((gamma-1)/gamma))) + epsilon*((pe-pa)/pc)
        return Cf


# wdot (weight flow rate)
#   Generally,
#       get_wdot(var, option)
#   Option == 0:
def get_wdot(var, option):
    if option == 0:
        force = float(var[0])
        Isp = float(var[1])
        wdot = force/Isp
        return wdot


# Pthroat (nozzle throat pressure)
#   Generally,
#       get_wdot(var, option)
#   Option == 0:
def get_pthroat(var, option):
    if option == 0:
        pchamber = float(var[0])
        gamma = float(var[1])
        pthroat = pchamber*((gamma + 1)/2)**((-gamma)/(gamma-1))
        return pthroat


# epsilon (theoretical expansion ratio)
#   option == 0:
#       Sea-level
#
def get_epsilon(var, option):
    if option == 0:
        gamma = var[0]
        pc = var[1]
        pe = var[2]
        epsilon = ((2/(gamma+1))**(1/(gamma-1))*(pc/pe)**(1/gamma)) / \
                np.sqrt(((gamama+1)/(gamma-1))*(1-(pe/pc)**((gamma-1)/gamma)))
        return epsilon
