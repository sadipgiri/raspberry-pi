#!/usr/bin/env python3

"""
    read_sensor.py - Python3 program to read sensor data (temperature and humidity)
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 05/07/2018
"""

import RPi.GPIO as GPIO
import smbus
import time
from datetime import datetime

LED_PIN = 20    # the BCM pin number of our LED
GPIO_IS_SETUP = False    # is GPIO setmode and setup complete?
DEVICE_ADDRESS = 0x44    # the i2c address of our SHT-31 sensor

bus = smbus.SMBus(1)

def get_status():
    bus.write_byte_data(DEVICE_ADDRESS, 0xF3, 0x2D)
    block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 3)
    print("Status MSB: " + hex(block[0]))
    print("Status LSB: " + hex(block[1]))

def clear_status():
    bus.write_byte_data(DEVICE_ADDRESS, 0x30, 0x41)
    print("Status register is cleared!")

def get_reading():
    bus.write_byte_data(DEVICE_ADDRESS, 0x24, 0x00)
    time.sleep(0.015)
    block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 6)
    return block

def soft_reset():
    bus.write_byte_data(DEVICE_ADDRESS, 0x30, 0xA2)
    print("soft reset!")

def setup_gpio():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)    # set to Broadcom pin numbering
    GPIO.setup(LED_PIN, GPIO.OUT)    # allow writing to our LED pin
    GPIO_IS_SETUP = True

def led_on():
    # first, check if GPIO is setup - if it isn't, then run setup_gpio
    if not GPIO_IS_SETUP:
        setup_gpio()
    # now, turn the LED on
    GPIO.output(LED_PIN, 1)

def led_off():
    if not GPIO_IS_SETUP:
        setup_gpio()
    GPIO.output(LED_PIN, 0)

def convert_temperature_reading(temperature_msb, temperature_lsb, mode='c'):
    raw_temp = (temperature_msb << 8) | temperature_lsb
    if mode == 'c':
        temp_c = -45 + 175.0 * (raw_temp/(2**16 - 1))
        return temp_c
    if mode == 'f':
        temp_fahren = -49 + 315 * (raw_temp/(2**16 - 1))
        return temp_fahren
    raise ValueError("Mode is not defined: (c or f)")

def convert_humidity_reading(humidity_msb, humidity_lsb):
    raw_humid = (humidity_msb << 8) | humidity_lsb
    humid = (100 * raw_humid)/(2**16 - 1)
    return humid

def verify_sum(temp_crc, humidity_crc):
    return 0

def read_sensor(times=1):
    dcts = {}
    temps = []
    humids = []
    if times:
        for i in range(0, times):
            data = get_reading()
            temps.append(convert_temperature_reading(data[0], data[1]))
            humids.append(convert_humidity_reading(data[3], data[4]))
        dcts = {"temps": temps, "humids": humids}
        return dcts
    data = get_reading()
    dcts = {"temp": convert_temperature_reading(data[0], data[1]), "humid": convert_humidity_reading(data[3], data[4])}
    return dcts

def writing_to_file(loops=1):
    if loops:
        for i in range(0, loops):
            write_once_to_file()
        return
    write_once_to_file()

def write_once_to_file():
    data = get_reading()
    current_time = datetime.now()
    temp = convert_temperature_reading(data[0], data[1])
    humid = convert_humidity_reading(data[3], data[4])
    with open('readings.csv', 'a') as my_file:
        my_file.write('{0}, {1}, {2}\n'.format(str(current_time), temp, humid))
    my_file.close()

def read_file():
    my_file = open('readings.csv', 'r')
    line = my_file.readline()
    while line:
        print(line)
        line = my_file.readline()

def return_min_max_avg():
    my_file = open('readings.csv', 'r')
    lst = my_file.readlines()
    min =  float(lst[0].split(',')[1])
    max = float(0)
    number_of_observations = len(lst)
    sum = 0
    for i in lst:
        temporary_temp = float(i.split(',')[1])
        if min > temporary_temp:
            min = temporary_temp
        if max < temporary_temp:
            max = temporary_temp
        sum = sum + temporary_temp
    avg = sum/number_of_observations
    return {'min': min, 'max': max, 'avg': avg}


if __name__ == '__main__':
    # print(read_sensor(times=3))
    writing_to_file(loops=5)
    read_file()
    return_min_max_avg()

    #for i in range(0, 10):
    #led_on()
    #time.sleep(0.25)
    #led_off()
    #get_status()
    #time.sleep(0.25)
    #clear_status()
    #soft_reset()
    #GPIO.cleanup()





