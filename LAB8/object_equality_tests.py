#Lab 8 Object Equality Tests
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      lmao1 = Point(1,2)
      lmao2 = Point(1,2)
      self.assertEqual(lmao1, lmao2)
      lmao1 = Point(1,3)
      lmao2 = Point(5,6)
      self.assertNotEqual(lmao1,lmao2)
      lmao1 = Point(5.0000000001,1)
      lmao2 = Point(5.0000000002,1)
      self.assertEqual(lmao1,lmao2)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

