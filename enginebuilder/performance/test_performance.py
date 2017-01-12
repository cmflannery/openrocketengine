#!/usr/bin/env python
import pytest
# import modules to test
from propellant import *
import equations
import curves


# unit tests
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


# integration tests
def test_inte():
    return 0


# system tests
def test_sys():
    return 0
