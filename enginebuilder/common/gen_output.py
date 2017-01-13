#!/usr/bin/env python
import xlsxwriter
import datetime
import time
import os
# gen_output.py
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class Outputs(object):
    def __init__(self, engine):
        self.engine = engine
        self.output_dir = os.path.join(os.getcwd(), 'output')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.create_xlsx()

    def create_xlsx(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
        file_name = "engine_" + st + ".xlsx"
        file_path = os.path.join(os.getcwd(), 'output', file_name)
        self.workbook = xlsxwriter.Workbook(file_path)
        self.worksheet = self.workbook.add_worksheet()

        self.worksheet.write('B2', 'openrocketengine')
        self.worksheet.write('B3', 'Thrust')
        self.worksheet.write('C3', self.engine.parameters.thrust)
        self.worksheet.write('B4', 'Throat Area')
        self.worksheet.write('C4', self.engine.nozzle.Athroat)
        self.worksheet.write('B5', 'Nozzle Exit Area')
        self.worksheet.write('C5', self.engine.nozzle.Aexit)
        self.worksheet.write('B6', 'Vchamber')
        self.worksheet.write('C6', self.engine.nozzle.Vchamber)

        self.write_units()
        self.workbook.close()

        print "\nEngine outputs have been generated in the '/output'"
        print "The file name is:",
        print file_name

        return 0

    def write_units(self):
        if self.engine.parameters.units == "0":
            units_force = 'lbf'
            units_area = 'in^2'
            units_volume = 'in^3'
        elif self.engine.parameters.units == "1":
            units_force = 'N'
            units_area = 'm^2'
            units_volume = 'm^2'
        self.worksheet.write('D3', units_force)
        self.worksheet.write('D4', units_area)
        self.worksheet.write('D5', units_area)
        self.worksheet.write('D6', units_volume)
