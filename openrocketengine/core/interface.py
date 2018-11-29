"""User interface for openrocketengine. Reads config files and outputs data"""
from __future__ import print_function, division, absolute_import
import os
import pandas as pd
import fire
from openrocketengine.core.rocket import Engine


standard_types = {
        'name': str,
        'units': str,
        'thrust': float,
        'Tc': float,
        'pc': float,
        'pe': float,
        'MR': float,
        'MW': float,
        'gamma': float,
        'lstar': float,
        'area_ratio': float
        }


def read_config(fname):
    """Parse configuration file and return a dictionary with the key value pairs

    Parameters:
        fname (str): file name, or path to file, of configuration file

    Returns:
        dict: contains all parameters and values parsed and typecast
    """
    assert os.path.isfile(fname), 'Error: {} does not exist in the working directory'.format(fname)
    with open(fname, 'r') as f:
        config = f.read()

    statements = [s for s in config.split('\n') if s != '']  # ignore empty lines
    parsed_config = [s for s in statements if s[0] != '#']  # ignore all comment lines
    configuration = {}
    # Read the configuration file and store all key-value pairs in a dictionary
    for thing in parsed_config:
        param_value = thing.split(' ')
        try:
            parameter = param_value[0].rstrip().lstrip()
            value = param_value[1].rstrip().lstrip()
            configuration[parameter] = value
        except IndexError:
            pass

    # Parse through the data and convert types
    for key in configuration.keys():
        try:
            std_type = standard_types[key]
        except KeyError:
            raise Exception('Error: {} is not a known configuration parameter'.format(key))

        if std_type != type(configuration[key]):
            configuration[key] = std_type(configuration[key])

    return configuration


def main(fname):
    configuration = read_config(fname)
    engine = Engine(**configuration)
    print(engine.ue)
    engine.generate_output()


def entry():
    """Command line entry point"""
    fire.Fire(main)


if __name__ == '__main__':
    fire.Fire(main)

