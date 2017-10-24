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
        self.designParameters = {'thrust': thrust, 'Tc':Tc, 'pc': pc, 'pa': pa,
                                 'MR': MR, 'MW':MW, 'gamma':gamma}

        if 'pe' in kwargs:
            self.designParameters['pe'] = kwargs['pe']
        else:
            self.designParameters['pe'] = self.designParameters['pa']

        self.set_constants()

        self.Thermo = Thermodynamics(self.designParameters, self.constants)

    def set_constants(self):
        """ Define useful SI constants.

            Units:
                Rbar: [kJ/kmol-K]
                g0: [m/s^2] """
        self.constants = {'Rbar': 8314, 'g0': 9.81}
        return self.constants

    @property
    def thrust(self):
        return self.designParameters['thrust']

    @property
    def Tc(self):
        return self.designParamters['Tc']

    @property
    def pc(self):
        return self.designParameters['pc']

    @property
    def pa(self):
        return self.designParameters['pa']

    @property
    def pe(self):
        return self.designParameters['pe']

    @property
    def MR(self):
        return self.designParameters['MR']

    @property
    def MW(self):
        return self.designParameters['MW']

    @property
    def gamma(self):
        return self.designParameters['gamma']

    @property
    def Rspecific(self):
        return self.Thermo.Rspecific

    @property
    def cstar(self):
        return self.Thermo.cstar

    @property
    def Cf(self):
        return self.Thermo.Cf

    @property
    def Isp(self):
        return self.Thermo.Isp

    @property
    def mdot(self):
        return self.Thermo.mdot

    @property
    def mdot_ox(self):
        return self.Thermo.mdot_ox

    @property
    def mdot_f(self):
        return self.Thermo.mdot_f


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
