from __future__ import division, absolute_import, print_function


class chamber():
    def __init__(self, thermo):
        self.thermo = thermo
        pass

    def get_At(self, **kwargs):
        """ get_At returns the calculated area of the throat """
        if self.At not in locals():
            if 'mdot' in kwargs:
                mdot = kwargs['mdot']
            else:
                mdot = thermo['mdot']
            if 'cstar' in kwargs:
                cstar = kwargs['cstar']
            else:
                cstar = thermo['cstar']
            if 'pc' in kwargs:
                pc = kwargs['pc']
            else:
                pc = thermo['pc']
            self.At = cstar * mdot / pc
        return self.At
