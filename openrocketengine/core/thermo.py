from __future__ import division, absolute_import, print_function
""" enginemanager """
import os
import subprocess
import numpy as np
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.0.2"
__status__ = "alpha"

class Thermodynamics():
    """ Thermodynamics() evalates engine performance values from design parameters """
    def __init__(self, parameters, constants):
        self.thrust = parameters['thrust']
        self.Tc = parameters['Tc']  # chamber temperature
        self.pc = parameters['pc']  # chamber pressure
        self.pe = parameters['pe']  # exit pressure
        self.pa = parameters['pa']  # ambient pressure
        self.MR = parameters['MR']  # mass ratio
        self.MW = parameters['MW']  # molecular weight of propellants
        self.gamma = parameters['gamma']  # ratio of coefficients of heats

        self.constants = constants

    def characterize_engine(self):
        self.parameters['Rspecific'] = self.get_Rspecific()
        self.parameters['cstar'] = self.get_cstar()
        self.parameters['Cf'] = self.get_Cf()
        self.parameters['Isp'] = self.get_Isp()
        self.parameters['mdot'] = self.get_mdot()
        self.parameters['mdot_ox'] = self.get_mdot_ox()
        self.parameters['mdot_f'] = self.get_mdot_f()
        self.parameters['pt'] = self.get_pt()
        self.parameters['Tt'] = self.get_Tt()

    def get_Rspecific(self, **kwargs):
        """ Calculate the value of specific gas constant """
        if 'Rbar' in kwargs:
            Rbar = kwargs['Rbar']
        else:
            Rbar = self.constants['Rbar']
        if 'MW' in kwargs:
            MW = kwargs['MW']
        else:
            MW = self.MW
        self.Rspecific = Rbar/MW
        return self.Rspecific

    def get_cstar(self, **kwargs):
        """ cstar, characteristic velocity [m/s]
        get_cstar() calculates and returns the value of cstar

        typically,
            get_cstar(g0=g0, gamma=gamma, Rspecific=Rspecific, Tc=Tc)"""
        if 'g0' in kwargs:
            g0 = kwargs['g0']
        else:
            g0 = self.constants['g0']
        if 'gamma' in kwargs:
            gamma = kwargs['gamma']
        else:
            gamma = self.gamma
        if 'Rspecific' in kwargs:
            Rspecific = kwargs['Rspecific']
        else:
            Rspecific = self.Rspecific
        if 'Tc' in kwargs:
            Tc = kwargs['Tc']
        else:
            Tc = self.Tc

        self.cstar = np.sqrt(gamma*Rspecific*Tc)/(gamma*np.sqrt((2/(gamma+1))**((gamma+1)/(gamma-1))))
        return self.cstar

    def get_Cf(self, **kwargs):
        """ Cf, Thrust Coefficient

        typically,
            get_Cf(gamma=gamma, pe=pe, pc=pc) """
        if 'gamma' in kwargs:
            gamma = kwargs['gamma']
        else:
            gamma = self.gamma
        if 'pe' in kwargs:
            pe = kwargs['pe']
        else:
            pe = self.pe
        if 'pc' in kwargs:
            pc = kwargs['pc']
        else:
            pc = self.pc

        self.Cf = np.sqrt((2*gamma**2/(gamma-1))*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-(pe/pc)**((gamma-1)/gamma)))
        return self.Cf

    def get_Isp(self, **kwargs):
        """ Isp, Specific Impulse [s]

        Specific Impulse is a commonly used performance metric for rocket
        engines

        typically,
            get_Isp(cstar=cstar, Cf=Cf, g0=g0)"""

        if 'cstar' in kwargs:
            cstar = kwargs['kwargs']
        else:
            cstar = self.cstar
        if 'Cf' in kwargs:
            Cf = kwargs['Cf']
        else:
            Cf = self.Cf
        if 'g0' in kwargs:
            g0 = kwargs['g0']
        else:
            g0 = self.constants['g0']

        self.Isp = cstar*Cf/g0
        return self.Isp

    def get_mdot(self, **kwargs):
        """ mdot, total mass flow rate [kg/s]

        typically,
            get_mdot(Isp=Isp, thrust=thrust, g0=g0)"""

        if 'Isp' in kwargs:
            Isp = kwargs['Isp']
        else:
            Isp = self.Isp

        if 'thrust' in kwargs:
            thrust = kwargs['thrust']
        else:
            thrust = self.thrust

        if 'g0' in kwargs:
            g0 = kwargs['g0']
        else:
            g0 = self.constants['g0']

        self.mdot = thrust/(Isp*g0)
        return self.mdot

    def get_mdot_ox(self, **kwargs):
        """ mdot_ox, mass flow rate of oxidizer [kg/s]

        typically,
            get_mdot_ox(mdot=mdot, MR=MR) """
        if 'mdot' in kwargs:
            mdot = kwargs['mdot']
        else:
            mdot = self.mdot
        if 'MR' in kwargs:
            MR = kwargs['MR']
        else:
            MR = self.MR

        self.mdot_ox = MR/(MR+1)*mdot
        return self.mdot_ox

    def get_mdot_f(self, **kwargs):
        """ mdot_f, mass flow rate of fuel [kg/s]

        typically,
            get_mdot_f(mdot=mdot, MR=MR) """

        if 'mdot' in kwargs:
            mdot = kwargs['mdot']
        else:
            mdot = self.mdot
        if 'MR' in kwargs:
            MR = kwargs['MR']
        else:
            MR = self.MR
        self.mdot_f = 1/(MR+1)*mdot
        return self.mdot_f

    def get_pt(self, **kwargs):
        """ Calculate the theoat pressure

        Derived from the isentropic flow-critical pressure ratio """

        if 'pc' in kwargs:
            pc = kwargs['pc']
        else:
            pc = self.pc
        if 'gamma' in kwargs:
            gamma = kwargs['gamma']
        else:
            gamma = self.gamma

        self.pt = pc * (2/(gamma+1))**(gamma/(gamma-1))
        return self.pt

    def get_Tt(self, **kwargs):
        """ Calculate the throat temperature

        Derived from isentropic flow-critical temperature ratio """

        if 'Tc' in kwargs:
            Tc = kwargs['Tc']
        else:
            Tc = self.Tc
            self.Tt
        return self.Tt

    def set_Ma_exit(self, **kwargs):
        """ Calculate and set the mach number at nozzle exit

        derived from pressure ratio equation
        """

        if 'pc' in kwargs:
            pc = kwargs['pc']
        else:
            pc = self.pc
        if 'gamma' in kwargs:
            gamma = kwargs['gamma']
        else:
            gamma = self.gamma
        if 'pe' in kwargs:
            pe = kwargs['pe']
        else:
            pe = self.pe

        self.Ma_exit = (pc/pe)**((gamma-1)/(2*gamma))/(1+(gamma-1)/2)**(1/2)
        return self.Ma_exit

    def get_Ma_exit(self):
        """ get value of Ma_exit """

        return self.Ma_exit


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
