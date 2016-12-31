#!/usr/bin/env python
import xlsxwriter
import datetime
import time
import os
# gen_output.py
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2016"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class outputs:
    def __init__(self, engine):
        self.engine = engine
        self.output_dir = os.path.join(os.getcwd(), 'output')
        self.create_xlsx()

    def create_xlsx(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
        file_name = "engine_" + st + ".xlsx"
        self.workbook = xlsxwriter.Workbook(file_name)
        self.worksheet = self.workbook.add_worksheet()

        self.worksheet.write('B2', 'openrocketengine')
        self.worksheet.write('B3', 'Thrust')
        self.worksheet.write('C3', self.engine.parameters.thrust)
        self.worksheet.write('B4', 'Throat Area')
        self.worksheet.write('C4', self.engine.nozzle.Athroat)
        self.worksheet.write('B5', 'Nozzle Exit Area')
        self.worksheet.write('C5', self.engine.nozzle.Aexit)

        self.write_units()
        self.workbook.close()

        print "\nEngine outputs have been generated in",
        print file_name

        return 0


    def write_units(self):
        if self.engine.parameters.units == "0":
            self.worksheet.write('D3', 'lbf')
            self.worksheet.write('D4', 'in^2')
            self.worksheet.write('D5', 'in^2')
        elif self.engine.parameters.units == "1":
            self.worksheet.write('D3', 'N')
            self.worksheet.write('D4', 'm^2')
            self.worksheet.write('D5', 'm^2')


    def create_output_dir(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
