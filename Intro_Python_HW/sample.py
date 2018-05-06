#!/usr/bin/env python3

"""
    sample.py - Python3 program to implement some python3 functions along with Unittest
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 04/05/2018
"""
## Problem 1:

# Part 1:
# add_two_numbers = lambda num1, num2: num1 + num2
def add_two_numbers(num1, num2):
    return num1 + num2

# subtract_two_numbers = lambda num1, num2: num2 - num1
def subtracts_two_numbers(num1, num2):
    return num2 - num1


# Part 2:
def multiply(num, times):
    result = 0
    for i in range(0, abs(times)):
        result = result + abs(num)
    if num < 0 and times < 0:
        return result
    if num < 0 or times < 0:
        return -result
    return result

def divide(num, divisor):
    if divisor == 0:
        return "Indeterminant Form!, You cannot divide by Zero [Zero Divison Error]"
    if num == 0:
        return 0
    count = 0
    abs_num = abs(num)
    abs_divisor = abs(divisor)
    while abs_num > 0:
        abs_num = subtracts_two_numbers(abs_divisor, abs_num)
        count = count + 1
        if abs_num == 0:
            if num < 0 and divisor < 0:
                return count
            if num < 0 or divisor < 0:
                return -count
            return count
    return "It doesn't divide"


## Problem 2:
def total_ASCII(str):
    total = 0
    for i in str:
        total += ord(i)
    return total
    
 # Problem 3
def length_guesser(my_string, my_length_guess):
    length = len(my_string)
    if length == my_length_guess:
        return 0
    elif length < my_length_guess:
        return -1
    else:
        return 1
    return "Something is wrong!"


if __name__ == '__main__':
    print(add_two_numbers(1, 10))
    print(subtracts_two_numbers(5, 15))
    print(multiply(-10, 10))
    print(divide(0, 0))
    print(total_ASCII("sadip"))
    print(length_guesser("sadjs", 3))
