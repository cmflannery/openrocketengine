#!/usr/bin/env python
""" enginemanager """
import os
import subprocess
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.0.2"
__status__ = "alpha"

# engine class retrieves and stores all outputs for each run
class Engine():
    """Create and optimize liquid engine design"""
    def __init__(self):
        pass

    def stuff(self):
        pass


def main():
    """main function, starts program"""
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    print("\n\nLets build a rocket engine!\n")

    eng = Engine()
    eng.start_building()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt: exiting...\n")
