from __future__ import division, absolute_import, print_function
import openrocketengine as ore


def test_Chamber():
    inputs = {
        'thrust' : 10000,
        'Tc' : 3000,
        'MW' : 20,
        'gamma' : 1.201,
        'MR' : 2.77,
        'pe' : 101000,
        'pa' : 100000,
        'pc' : 3000000,
        'gamma' : 1.21
    }
    const = {'Rbar': 8314, 'g0': 9.81}
    thermo = ore.Thermodynamics(inputs, const)
    assert thermo.set_Ma_exit()==thermo.get_Ma_exit()
