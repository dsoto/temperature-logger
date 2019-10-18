# Temperature Logger

This is a simple multi-channel temperature logger board and real-time display application.

The temperature logger uses temperature sensors with a digital interface that responds to requests for data over serial and is implemented in CircuitPython.

The real-time display uses a python streaming graphing app (Bokeh) to request temperature data from the logger board and post to a graph on a laptop or computer.

# Mapping Sensors

The sensors in the legend are specified by the pin used for the chip select.
This pin is visible on the silkscreen of the feather board.

# Running

> bokeh serve --show temperature_graph.py

# TODO

- upload schematic to repo
- put serial port in command line args or dropdown menu
- implement file logging
