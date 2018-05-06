
"""
    test_samples.py - Python3 program for unittesting samples.py functions
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 05/05/2018
"""

import unittest
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

"""
Here, I am using Python's unittest library to do testing and using two "assertAlmostEqual() and assertRaises()" functions.
"""
