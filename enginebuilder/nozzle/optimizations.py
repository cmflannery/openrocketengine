#!/usr/bin/env python
import numpy as np
import deap
# optimizations.py
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class opt_contraction_ratio(object):
    """opt_contraction_ratio optimizes the contraction area ratio."""
    def __init__(self):
        super(opt_contraction_ratio, self).__init__()
