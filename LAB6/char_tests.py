#Lab 6 Char Test Cases
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_is_lower_101(self):
      self.assertEqual(is_lower_101('b'), True)
      self.assertEqual(is_lower_101('Z'), False)
      self.assertEqual(is_lower_101(' '), False)

   def test_char_rot13(self):
      self.assertEqual(char_rot13('m'), 'z')
      self.assertEqual(char_rot13('C'), 'P')
      self.assertEqual(char_rot13('z'), 'm')

if __name__ == '__main__':
   unittest.main()

