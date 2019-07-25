from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import grid, row, column
from bokeh.io import curdoc
from bokeh.palettes import d3


import datetime
import numpy as np
import serial

def make_document(doc):

    def update():

        # get time stamp
        sample_time = datetime.datetime.now()

        # update data sources

        # print('attempting read')
        port = '/dev/tty.usbmodem14101'
        connection = serial.Serial(port, 9600, timeout=1)
        connection.write(b'5\r')
        temp0 = connection.read(20).decode("utf-8")[3:-2]
        connection.write(b'6\r')
        temp1 = connection.read(20).decode("utf-8")[3:-2]
        connection.close()


        temp_source.stream({'time':[sample_time],
                            'temp0':[float(temp0)],
                            'temp1':[float(temp1)]})



        # write to log file
        # with open(log_file, 'a') as f:
        #     f.write('\n')

    # create data stores
    temp_source = ColumnDataSource({'temp0':[], 'temp1':[], 'time':[]})

    # set up graphs and callback
    doc.add_periodic_callback(update, 1000)

    # define figures and layout
    temp_fig = figure(title='Temperature', x_axis_type='datetime')

    # generate trend lines and data points
    temp_fig.line(source=temp_source, x='time', y='temp0')
    temp_fig.line(source=temp_source, x='time', y='temp1')
    temp_fig.circle(source=temp_source, x='time', y='temp0')
    temp_fig.circle(source=temp_source, x='time', y='temp1')


    plots = temp_fig
    doc.add_root(plots)
    doc.title = "Temperature Plotting"


print('starting')

# log_file = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '-log.csv'

make_document(curdoc())
