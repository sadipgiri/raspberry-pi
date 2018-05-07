#!/usr/bin/env python3

from smbus2 import SMBus
import time
 
# opening i2c bus 1
bus = SMBus(1)
 
# SHT31 sensor address: 0x44(68)
bus.write_i2c_block_data(0x44, 0x2C, [0x06])
 
time.sleep(0.5)    # sleeping for 0.5 seconds
 
# reading data
# data returns a list of [Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC]
data = bus.read_i2c_block_data(0x44, 0x00, 6)
 
# we just need Temp MSB and Humidity LSB so that we can convert to other temperature scales
temp = data[0] * 256 + data[1]
celcius_temp = -45 + (175 * temp / 65535.0)
fahren_temp = -49 + (315 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0


if __name__ == '__main__':
    print (celcius_temp)
    print (fahren_temp)
    print (humidity)

"""
References:
- Python3 SmBus2 Package Tutorial
    - https://pypi.org/project/smbus2/
- Temp MSB and Humidity LSB conversion 
    - http://www.pibits.net/code/raspberry-pi-sht31-sensor-example.php#codesyntax_1
"""