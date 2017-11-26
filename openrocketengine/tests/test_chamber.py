from __future__ import division, absolute_import, print_function
import openrocketengine as ore


def test_Chamber():
    chamber_test = ore.Chamber(1)
    assert chamber_test.get_At(mdot=2.3,cstar=5400,pc=3000) == 4.14
