#!/usr/bin/env python
""" Equations used to define engine parameters and performance """


class Performance(object):
    def __init__(self, units='metric', **kwargs):
        self.inputs
        self.units = lower(units)
        self.set_constants(units=self.units)
        pass

    def set_constants(self, units):
        """ define some constants based on the value of units. """
        if units == 'metric':
            self.g0 = 9.81
            self.Rbar = 345.7
        elif units == 'english':
            self.g0 = 32.17
        pass

    def set_Rspecific(self):
        pass

    def get_pexit(self, pambient=14.7, **kwargs):
        """ pressure values are given in atm
            default pambient is  1 """
        self.pexit = pambient
        return self.pambient

    def get_cee_star(self):
        pass

    def get_Cf(self):
        return self.Cf

    def get_Isp(self):
        return self.Isp
        pass
