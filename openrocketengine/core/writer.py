import xlsxwriter
from string import ascii_uppercase

def generate(engine):
    """ generate()
    creates output excel file with engine performance and geometric parameters
    """
    outputName = 'engine.xlsx'
    workbook = xlsxwriter.Workbook(outputName)
    performanceWorksheet = workbook.add_worksheet('performance')
    geometryWorksheet = workbook.add_worksheet('geometry')

    headersFormat = workbook.add_format()
    headersFormat.set_bg_color(bg_color='#C7C7FF')

    performanceWorksheet.write('B2', 'Engine Name:')
    if engine.name != False:
        performanceWorksheet.write('C2', engine.name)
    
    # generate header
    performanceWorksheet.write('B3', 'Thrust', headersFormat)
    performanceWorksheet.write('B4', 'Thrust Vac', headersFormat)
    performanceWorksheet.write('B5', 'Isp', headersFormat)
    performanceWorksheet.write('B6', 'Isp Vac', headersFormat)
    performanceWorksheet.write('B7', 'mass flow rate', headersFormat)
    performanceWorksheet.write('B8', 'Mixture Ratio', headersFormat)

    # add data
    performanceWorksheet.write('C3', engine.thrust)
    performanceWorksheet.write('C4', engine.thrust_vac)
    performanceWorksheet.write('C5', engine.Isp)
    performanceWorksheet.write('C6', engine.Isp_vac)
    performanceWorksheet.write('C7', engine.mdot)
    performanceWorksheet.write('C8', engine.MR)
    performanceWorksheet.write('C9', engine.ue)

    # units
    performanceWorksheet.write('D3', 'N')
    performanceWorksheet.write('D4', 'N')
    performanceWorksheet.write('D5', 's')
    performanceWorksheet.write('D6', 's')
    performanceWorksheet.write('D7', 'kg/s')
    performanceWorksheet.write('D8', '1')
    performanceWorksheet.write('D9', 'm/s')

    print('Output Generated!')