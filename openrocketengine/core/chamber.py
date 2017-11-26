from __future__ import division, absolute_import, print_function


class Chamber():
    def __init__(self, thermo):
        self.thermo = thermo
        pass

    def get_At(self, **kwargs):
        """ get_At returns the calculated area of the throat """
        if 'mdot' in kwargs:
            mdot = kwargs['mdot']
        else:
            mdot = self.thermo['mdot']
        if 'cstar' in kwargs:
            cstar = kwargs['cstar']
        else:
            cstar = self.thermo['cstar']
        if 'pc' in kwargs:
            pc = kwargs['pc']
        else:
            pc = self.thermo['pc']
        self.At = cstar * mdot / pc
        return self.At

    def get_Ae(self, **kwargs):
        """ get_Ae returns the exit area of the rocket, assuming ideal expansion
        in a non-vacuum environment """
        return self.calc_A(Ma=self.Ma_exit)

    def calc_A(self, **kwargs):
        """ calc_A returns the area at an arbitrary station relative to the
        critical value, i.e. the throat in choked flow

        calc_A does not set any property of the class or class instance, only
        a value is returned """
        if 'Ma' not in kwargs:
            print('Mach number must be specified when calling calc_A')
            return 0
        Ma = kwargs['Ma']

        if 'At' in kwargs:
            At = kwargs['At']
        else:
            At = self.At
        if 'gamma' in kwargs:
            gamma = kwargs['gamma']
        else:
            gamma = self.thermo['gamma']

        return At*1/Ma*((1 + ((gamma-1)/2)*Ma**2)/(1 + ((gamma-1)/2)))**((gamma+1)/(2*(gamma-1)))
