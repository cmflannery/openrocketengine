#!/usr/bin/env python
""" enginemanager """
import os
import subprocess
import numpy as np
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.0.2"
__status__ = "alpha"

# engine class retrieves and stores all outputs for each run
class Engine():
    """Create and optimize liquid engine design"""
    def __init__(self, thrust, Tc, pc, pa, MR, MW, gamma, **kwargs):
        self.thrust = thrust
        self.Tc = Tc
        self.pc = pc
        self.pa = pa
        self.MR = MR
        self.MW = MW  # [g/mol]
        self.gamma = gamma
        self.constants() # define some useful constants

        if 'pe' in kwargs:
            self.pe = kwargs['pe']
        else:
            self.pe = self.pa

    def characterize_engine(self):
        self.get_Rspecific()
        self.get_cstar()
        self.get_Cf()
        self.get_Isp()

    def constants(self):
        self.Rbar = 8.314  # J/mol*K
        self.g0 = 9.81  # m/s^2
        return self.Rbar, self.g0

    def get_Rspecific(self, Rbar=None, MW=None):
        if Rbar == None:
            Rbar = self.Rbar
        if MW == None:
            MW = self.MW
        self.Rspecific = self.Rbar/self.MW
        return self.Rspecific

    def get_pexit(self, pa=14.7, **kwargs):
        """ pressure values are given in atm
            - default pambient is  1 """
        self.pe = pa
        return self.pa

    def get_cstar(self, g0=None, gamma=None, Rspecific=None, Tc=None):
        if g0 == None:
            g0 = self.g0
        if gamma == None:
            gamma = self.gamma
        if Rspecific == None:
            Rspecific = self.Rspecific
        if Tc == None:
            Tc = self.Tc
        self.cstar = np.sqrt(g0*gamma*Rspecific*Tc)/(gamma*np.sqrt((2/(gamma+1))**((gamma+1)/(gamma-1))))
        return self.cstar

    def get_Cf(self, gamma=None, pe=None, pc=None):
        if gamma == None:
            gamma = self.gamma
        if pe == None:
            pe = self.pe
        if pc == None:
            pc = self.pc
        self.Cf = np.sqrt((2*gamma**2/(gamma-1))*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-(pe/pc)**((gamma-1)/gamma)))
        return self.Cf

    def get_Isp(self, cstar=None, Cf=None, g0=None):
        if cstar == None:
            cstar = self.cstar
        if Cf == None:
            Cf = self.Cf
        if g0 == None:
            g0 = self.g0
        self.Isp = cstar*Cf/g0
        return self.Isp


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
