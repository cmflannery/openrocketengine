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


def main():
    prop.prompt_for_propellants()


if __name__ == "__main__":
    print "Lets build a rocket engine!\n"

    main()
else:
    print "\"engine_builder.py\" must be run as the main script"
