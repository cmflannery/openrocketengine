#!/usr/bin/env python
from equations import *
import propellant as prop
# Equations used to define engine parameters and performance
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


def prompt_for_thrust():
    confirmed = False
    while not(confirmed):
        thrust = raw_input("Enter the target thrust: ")
        print "Thrust: ",
        print thrust
        while True:
            verify = raw_input("Correct? [Y/n]: ")
            verify = verify.upper()
            if verify == "Y":
                confirmed = True
                return thrust
            elif verify == "N":
                confirmed = False
                break
            else:
                print "Enter 'Y' or 'n'"
