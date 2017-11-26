from __future__ import division, absolute_import, print_function
""" enginemanager """
import os
import subprocess
import numpy as np
from .thermo import *
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.0.2"
__status__ = "alpha"

# engine class retrieves and stores all outputs for each run
class Engine():
    """Create and optimize liquid engine design"""
    def __init__(self, thrust, Tc, pc, pa, MR, MW, gamma, **kwargs):
        defaultParameters = ['thrust', 'Tc', 'pc', 'pa', 'MR', 'MW', 'gamma']
        self.parameters = {'thrust': thrust, 'Tc':Tc, 'pc': pc, 'pa': pa,
                                 'MR': MR, 'MW':MW, 'gamma':gamma}

        if 'pe' in kwargs:
            self.parameters['pe'] = kwargs['pe']
        else:
            self.parameters['pe'] = self.parameters['pa']

        self.set_constants()

        self.Thermo = Thermodynamics(self.parameters, self.constants)
        self.parameters = Thermo.parameters

    def set_constants(self):
        """ Define useful SI constants.

            Units:
                Rbar: [kJ/kmol-K]
                g0: [m/s^2] """
        self.constants = {'Rbar': 8314, 'g0': 9.81}
        return self.constants

    @property
    def thrust(self):
        return self.parameters['thrust']

    @property
    def Tc(self):
        return self.designParamters['Tc']

    @property
    def pc(self):
        return self.parameters['pc']

    @property
    def pa(self):
        return self.parameters['pa']

    @property
    def pe(self):
        return self.parameters['pe']

    @property
    def MR(self):
        return self.parameters['MR']

    @property
    def MW(self):
        return self.parameters['MW']

    @property
    def gamma(self):
        return self.parameters['gamma']

    @property
    def Rspecific(self):
        return self.parameters['Rspecific']

    @property
    def cstar(self):
        return self.parameters['cstar']

    @property
    def Cf(self):
        return self.parameters['Cf']

    @property
    def Isp(self):
        return self.parameters['Isp']

    @property
    def mdot(self):
        return self.parameters['mdot']

    @property
    def mdot_ox(self):
        return self.parameters['mdot_ox']

    @property
    def mdot_f(self):
        return self.parameters['mdot_f']

    @property
    def Tt(self):
        return self.parameters['Tt']


def main():
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    print("\n\nLets build a rocket engine!\n")

    eng = Engine()
    eng.start_building()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt: exiting...\n")
