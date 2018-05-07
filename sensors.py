#!/usr/bin/env python3

import smbus2   # smbus2 module to open i2c bus and write/read sensor data
import time     # to make it sleep
import csv      # saving it in the local file
from datetime import datetime   # to save datetime when the sensor readings were done

def temp_and_humidity():
    lst = []    # to write readings in the list and write it in the local csv file
    lst.append(str(datetime.now()))    # timestamp 

    # opening i2c bus 1
    bus = smbus2.SMBus(1)
    
    # SHT31 sensor address: 0x44(68)
    bus.write_i2c_block_data(0x44, 0x2C, [0x06])
    
    time.sleep(0.5)    # sleeping for 0.5 seconds
    
    # reading data
    # data returns a list of [Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC]
    data = bus.read_i2c_block_data(0x44, 0x00, 6)

    temp_msb = data[0]
    temp_lsb = data[1]
    temp_crc = data[2]

    humidity_msb = data[3]
    humidity_lsb = data[4]
    humidity_crc = data[5]

    # we need Temp MSB, LSB and Humidity LSB, CRC so that we can convert to other temperature scales
    temp = temp_msb * 256 + temp_lsb
    celcius_temp = -45 + (175 * temp / 65535.0)
    fahren_temp = -49 + (315 * temp / 65535.0)
    lst.append(fahren_temp)
    humidity = 100 * (humidity_msb * 256 + humidity_lsb) / 65535.0
    lst.append(humidity)
    with open('sensor_readings.csv', 'a') as csvfile:
        csvfile.write('{0}, {1}, {2}\n'.format(lst[0], lst[1], lst[2]))


# def write_on_csv_file(data):
#     with open('sensor_readings.csv', 'a') as csvfile:
#     csvfile.write('{0}, {1}, {2}\n'.format(data[0], data[1], data[2]))


if __name__ == '__main__':
    temp_and_humidity()

"""
References:
- Python3 SmBus2 Package Tutorial
    - https://pypi.org/project/smbus2/
- Temp MSB and Humidity LSB conversion 
    - http://www.pibits.net/code/raspberry-pi-sht31-sensor-example.php#codesyntax_1
"""