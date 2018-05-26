#!/usr/bin/env python3

def crc8(msb, lsb):
    buffer = [msb, lsb] # put our bytes into a list
    polynomial = 0x31   # see the table 19 - polynomial
    crc = 0xFF          # see table 19 - initialization
    index = 0           # our index into our buffer
    for index in range(0, len(buffer)):
        crc ^= buffer[index]    # ^ is XOR
        for i in range(8, 0, -1):
            if crc & 0x80:
                crc = (crc << 1) ^ polynomial
            else:
                crc = (crc << 1)  
    return hex(crc & 0xFF)   # this will be the CRC we use for comparison

if __name__ == '__main__':
    print(crc8(0xBE, 0xEF)) # should return 0x90
