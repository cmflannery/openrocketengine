"""User interface for openrocketengine. Reads config files and outputs data"""
import os
import pandas as pd
import fire


def read_config(fname):
    with open(fname, 'r') as f:
        config = f.read()


def main(fname):
    read_config(fname)


if __name__ == '__main__':
    fire.Fire(main)
