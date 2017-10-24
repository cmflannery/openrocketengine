#!/usr/bin/env python
""" Equations used to define engine parameters and performance """


class Performance():
    def __init__(self, **kwargs):
        self.inputs
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
