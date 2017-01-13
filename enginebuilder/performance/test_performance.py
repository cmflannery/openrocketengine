#!/usr/bin/env python
import pytest
# import modules to test
from propellant import *
from equations import *
from curves import *


# unit tests: classes and functions
class params_test(object):
    def __init__(self):
        self.units = 0
        self.MW = 48.00
        self.thrust = 100.00
        self.time = 10.0
        self.gamma = 1.00


def test_equations():
    params = params_test()
    # perform = performance(params)
    # assert perform.g0 == 32.174


# integration tests: passing classes, etc.
def test_inte():
    return 0
