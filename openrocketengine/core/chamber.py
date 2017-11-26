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
