#Lab 8 List Comprehension Tests
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   def test_distance_all(self):
      self.assertEqual(distance_all([Point(1,1),Point(2,2),Point(3,0)]),([1.4142135623730951, 2.8284271247461903, 3.0]))
      self.assertEqual(distance_all([Point(7,8),Point(-2,4),Point(6,0)]),([10.63014581273465, 4.47213595499958, 6.0]))
      self.assertEqual(distance_all([Point(3,2),Point(74,2),Point(7,1),Point(3,0)]),([3.605551275463989, 74.02702209328699, 7.0710678118654755, 3.0]))

   def test_are_in_first_quadrant(self):
      self.assertEqual(are_in_first_quadrant([Point(1,2),Point(-3,4),Point(3,4)]),[Point(1,2),Point(3,4)])
      self.assertEqual(are_in_first_quadrant([Point(3,2),Point(-3,-4),Point(74,0)]),[Point(3,2)])
      self.assertEqual(are_in_first_quadrant([Point(-8,2),Point(-3,-4),Point(4,4),Point(16,-3),Point(72,5)]),[Point(4,4),Point(72,5)])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

