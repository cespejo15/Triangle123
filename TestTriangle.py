# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(12, 5, 13), 'Right', '12,5,13 is a Right triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles', '3,3,5 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 is an Isosceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(3, 5, 7), 'Scalene', '3,5,7 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(11, 4, 8), 'Scalene', '11,4,8 is a Scalene triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be an Equilateral triangle')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be an Equilateral triangle')

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(1, 4, 8), 'NotATriangle', '1,4,8 is not a triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(12, 3, 5), 'NotATriangle', '12,3,5 is not a triangle')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(1, 14, 6), 'NotATriangle', '1,14,6 is not a triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(1, 218, 310), 'InvalidInput', '1,218,310 is an invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-4, 12, 3), 'InvalidInput', '-4,12,3 is an invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(3.0, 1.0, 4.2), 'InvalidInput', '3.0,1.0,4.2 is an invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
