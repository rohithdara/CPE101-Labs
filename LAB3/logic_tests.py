#Lab 3 Logic Test Cases
#
#Name: Rohith Dara
#Professor Name: S. Einakian
#Section: 01

import unittest
import logic

#You can dlete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_is_even(self):
      self.assertTrue(logic.is_even(6))
      self.assertFalse(logic.is_even(7))
      self.assertFalse(logic.is_even(23455))
      self.assertTrue(logic.is_even(0))
      
   def test_in_an_interval(self):
   	self.assertFalse(logic.in_an_interval(-10))
   	self.assertTrue(logic.in_an_interval(0))
   	self.assertFalse(logic.in_an_interval(9))
   	self.assertTrue(logic.in_an_interval(20))
   	self.assertTrue(logic.in_an_interval(122))
   	self.assertTrue(logic.in_an_interval(127))
   	

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

