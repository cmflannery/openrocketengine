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

def print_logo_image():
    """print rocket image (ascii art) to console"""
    # prints ascii art of rocket stored in /resources/openrocketengine
    path = os.path.dirname(__file__)
    fname = os.path.join(path, 'resources', 'openrocketengine.txt')

    logo_image = AsciiImage(fname)
    logo_image.display_image()


def print_logo_text():
    """print OpenRocketEng to console"""
    # display ascii art text
    text_to_print = 'OpenRocketEng'

    logo_text = AsciiText(text_to_print)
    logo_text.display_text()


def main():
    """main function, starts program"""
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    print_logo_image()
    print_logo_text()
    print("\n\nLets build a rocket engine!\n")

    eng = Engine()
    eng.start_building()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt: exiting...\n")
