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


def create_xlsx(engine):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
    file_name = "engine_" + st + ".xlsx"
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    worksheet.write('B2', 'openrocketengine')
    worksheet.write('B3', 'Thrust')
    worksheet.write('C3', engine.thrust)
    worksheet.write('B4', 'Throat Area')
    worksheet.write('C4', engine.Athroat)
    worksheet.write('B5', 'Nozzle Exit Area')
    worksheet.write('C5', engine.Aexit)

    write_units(worksheet, engine.units)
    workbook.close()

    print "\nEngine outputs have been generated in",
    print file_name

    return 0


def write_units(worksheet, units):
    if units == "0":
        worksheet.write('D3', 'lbf')
        worksheet.write('D4', 'in^2')
        worksheet.write('D5', 'in^2')
    elif units == "1":
        worksheet.write('D3', 'N')
        worksheet.write('D4', 'm^2')
        worksheet.write('D5', 'm^2')
