# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.
import time

import board
import busio
import digitalio

import adafruit_max31865


# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs1 = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
cs2 = digitalio.DigitalInOut(board.D6)  # Chip select of the MAX31865 board.

#sensor = adafruit_max31865.MAX31865(spi, cs)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor1 = adafruit_max31865.MAX31865(spi, cs1, rtd_nominal=100, ref_resistor=430.0, wires=3)
sensor2 = adafruit_max31865.MAX31865(spi, cs2, rtd_nominal=100, ref_resistor=430.0, wires=3)

# Main loop to print the temperature every second.
while True:
    # try sys.stdin.read(1) to read a character
    if input()=='5':
        print('{0:0.3f}'.format(sensor1.temperature))
    if input()=='6':
        print('{0:0.3f}'.format(sensor2.temperature))
