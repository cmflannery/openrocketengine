from __future__ import division, absolute_import, print_function
import openrocketengine as ore


def test_Chamber():
    thermo = {
            'gamma': 1.27
              }
    chamber = ore.Chamber(thermo)
    assert chamber.get_At(mdot=2.3,cstar=5400,pc=3000) == 4.14
    assert chamber.calc_A() == 0
    assert chamber.calc_A(Ma=2) == 7.46561495970419
