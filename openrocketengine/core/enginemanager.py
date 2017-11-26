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
    def __init__(self, **kwargs):
        defaultParameters = ['thrust', 'Tc', 'pc', 'pe', 'pa', 'MR', 'MW', 'gamma']
        try:
            self.thrust = kwargs['thrust']
            self.Tc = kwargs['Tc']
            self.pc = kwargs['pc']
            self.pa = kwargs['pa']
            self.pe = kwargs['pe']
            self.MR = kwargs['MR']
            self.MW = kwargs['MW']
            self.gamma = kwargs['gamma']
        except KeyError:
            print('Include all required parameters:', defaultParameters)
            raise

        # set constants
        self.__Rbar = 8314  # [kJ/Kmol-K]
        self.__g0 = 9.81  # m/s^2

################################################################################
#**************************** INDEPENDENT VARIABLES ****************************
################################################################################
    @property
    def Rbar(self):
        """ Rbar, universal gas constant """
        return self.__Rbar

    @property
    def g0(self):
        """ g0, gravitational parameter """
        return self.__g0

    @property
    def thrust(self):
        """ Thrust property [N] """
        return self.__thrust

    @thrust.setter
    def thrust(self, value):
        self.__thrust = value

    @property
    def Tc(self):
        """ Tc [K], chamber temperature property """
        return self.__Tc

    @Tc.setter
    def Tc(self, value):
        self.__Tc = value

    @property
    def pc(self):
        """ pc [Pa], chamber pressure property """
        return self.__pc

    @pc.setter
    def pc(self, value):
        self.__pc = value

    @property
    def pa(self):
        """ pa [Pa], ambient pressure property """
        return self.__pa

    @pa.setter
    def pa(self, value):
        self.__pa = value

    @property
    def pe(self):
        """ pe [Pa], exit pressure proprety """
        return self.__pe

    @pe.setter
    def pe(self, value):
        self.__pe = value

    @pe.deleter
    def pe(self):
        del self.__pe

    @property
    def MR(self):
        """" MR [1], mixture ratio property """
        return self.__MR

    @MR.setter
    def MR(self, value):
        self.__MR = value

    @property
    def MW(self):
        """ MW [1], gas molecular weight of propellants """
        return self.__MW

    @MW.setter
    def MW(self, value):
        self.__MW = value

    @property
    def gamma(self):
        """ gamma [1], ratio of coefficients of heats """
        return self.__gamma

    @gamma.setter
    def gamma(self, value):
        self.__gamma = value

################################################################################
#***************************** DEPENDENT VARIABLES *****************************
################################################################################
    @property
    def Rspecific(self):
        """ Rspecific [kg/kmol-K], specific gas constant """
        return self.Rbar/self.MW

    @Rspecific.setter
    def Rspecific(self, MW):
        self.__Rspecific = self.Rbar/MW

    @property
    def cstar(self):
        """ cstar, characteristic velocity [m/s]
            get_cstar() calculates and returns the value of cstar """
        gamma = self.gamma
        Rspecific = self.Rspecific
        Tc = self.Tc
        return np.sqrt(gamma*Rspecific*Tc)/(gamma*np.sqrt((2/(gamma+1))**((gamma+1)/(gamma-1))))

    @cstar.setter
    def cstar(self, value):
        """ value, dictionary containing gamma, Rspecific, and Tc """
        g0 = self.g0
        required = ['gamma', 'Rspecific', 'Tc']

        try:
            gamma = value['gamma']
            Rspecific = value['Rspecific']
            Tc = value ['Tc']
        except KeyError:
            print('Include all required parameters:', required)
            raise

        self.__cstar = np.sqrt(gamma*Rspecific*Tc)/(gamma*np.sqrt((2/(gamma+1))**((gamma+1)/(gamma-1))))

    @property
    def Cf(self):
        """ Cf, Thrust Coefficient """
        gamma = self.gamma
        pc = self.pc
        pe = self.pe
        return np.sqrt((2*gamma**2/(gamma-1))*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-(pe/pc)**((gamma-1)/gamma)))

    @Cf.setter
    def get_Cf(self, value):
        """ Cf, Thrust Coefficient """
        required = ['pe','pc','gamma']
        try:
            pe = value['pe']
            pc = value['pc']
            gamma = value['gamma']
        except KeyError:
            print('Include all required parameters:', required)
            raise

        self.__Cf = np.sqrt((2*gamma**2/(gamma-1))*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-(pe/pc)**((gamma-1)/gamma)))

    @property
    def Isp(self):
        cstar = self.cstar
        Cf = self.Cf
        g0 = self.g0
        return cstar*Cf/g0

    @Isp.setter
    def Isp(self, value):
        """ Isp, Specific Impulse [s]

        Specific Impulse is a commonly used performance metric for rocket
        engines
        """
        required = ['cstar', 'Cf']
        g0 = self.g0
        try:
            cstar = value['cstar']
            Cf = value['Cf']
        except KeyError:
            print('Include all required parameters:', required)
            raise
        self.__Isp = cstar*Cf/g0

    @property
    def mdot(self):
        """ mdot, total mass flow rate [kg/s]

        typically,
            get_mdot(Isp=Isp, thrust=thrust, g0=g0)"""
        thrust = self.thrust
        Isp = self.Isp
        g0 = self.g0
        return thrust/(Isp*g0)

    @property
    def mdot_ox(self):
        """ mdot_ox, mass flow rate of oxidizer [kg/s] """
        MR = self.MR
        mdot = self.mdot
        return MR/(MR+1)*mdot

    @property
    def mdot_f(self):
        """ mdot_f, mass flow rate of fuel [kg/s] """
        MR = self.MR
        mdot = self.mdot
        return 1/(MR+1)*mdot

    @property
    def Tt(self):
        """ Calculate the throat temperature

        Derived from isentropic flow-critical temperature ratio """

        # NEEDS WORK

        if 'Tc' in kwargs:
            Tc = kwargs['Tc']
        else:
            Tc = self.Tc
            self.Tt = 0
        return self.Tt

    @property
    def pt(self):
        """ Calculate the throat pressure

        Derived from the isentropic flow-critical pressure ratio """
        pc = self.pc
        gamma = self.gamma
        return pc * (2/(gamma+1))**(gamma/(gamma-1))

    @property
    def Ma_exit(self):
        """ Calculate and set the mach number at nozzle exit

        derived from pressure ratio equation
        """
        pc = self.pc
        gamma = self.gamma
        pe = self.pe
        return (pc/pe)**((gamma-1)/(2*gamma))/(1+(gamma-1)/2)**(1/2)

    @property
    def At(self):
        """ At returns the calculated area of the throat """
        mdot = self.mdot
        cstar = self.cstar
        pc = self.pc
        return cstar * mdot / pc

    @property
    def Ae(self):
        """ Ae returns the exit area of the rocket, assuming ideal expansion
        in a non-vacuum environment """
        return self.calc_A(self.Ma_exit)

    @property
    def Aratio(self):
        """ returns the expansion area ratio, Aexit/Athroat """

        return self.Ae/self.At

################################################################################
#********************************** FUNCTIONS **********************************
################################################################################

    def calc_A(self, Ma):
        """ calc_A returns the area at an arbitrary station relative to the
        critical value, i.e. the throat in choked flow

        calc_A does not set any property of the class or class instance, only
        a value is returned """

        At = self.At
        gamma = self.gamma

        return At*1/Ma*((1 + ((gamma-1)/2)*Ma**2)/(1 + ((gamma-1)/2)))**((gamma+1)/(2*(gamma-1)))



def main():
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    print("\n\nLets build a rocket engine!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt: exiting...\n")
