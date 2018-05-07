
"""
    test_samples.py - Python3 program for unittesting samples.py functions
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 05/05/2018
"""

import unittest # importing Python unitest module
from sample import add_two_numbers, subtracts_two_numbers, multiply, divide, total_ASCII, length_guesser

class TestSample(unittest.TestCase):
    def test_add_two_numbers(self):
        # Test 
        self.assertAlmostEqual(add_two_numbers(0, 0), 0)
        self.assertAlmostEqual(add_two_numbers(-10, 10), 0)
        self.assertAlmostEqual(add_two_numbers(-10, -10), (-10 + (-10)))
        self.assertAlmostEqual(add_two_numbers(-10.05, 10), ((-10.05) + 10))
    
    def test_subtracts_two_numbers(self):
        self.assertAlmostEqual(subtracts_two_numbers(10, 8), 8 - 10)
        self.assertAlmostEqual(subtracts_two_numbers(0, 0), 0 - 0)
    
    def test_multiply(self):
        self.assertAlmostEqual(multiply(0, 0), 0 * 0)
        self.assertAlmostEqual(multiply(0, -1), 0)
        self.assertAlmostEqual(multiply(-10, 10), -100)
        self.assertAlmostEqual(multiply(10, -10), -100)
        self.assertAlmostEqual(multiply(-10, -10), 100)
    
    # checking whether it returns right answer or not
    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 10/2)
        self.assertAlmostEqual(divide(-10, 1), -10/1)
        self.assertAlmostEqual(divide(0, 10), 0/10)
    
    # testing whether it returns value error or not
    def test_values(self):
        self.assertRaises(ValueError, divide, 10, 0)
    
    # def test_types(self):
    #     self.assertRaises(TypeError, add_two_numbers, 5, 1 + 5j)

"""
Here, I am using Python's unittest library to do testing and using two "assertAlmostEqual() and assertRaises()" functions.
"""
