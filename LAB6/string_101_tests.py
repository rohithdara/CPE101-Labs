#Lab 6 String Manipulation Test Cases
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from string_101 import *

class TestString(unittest.TestCase): 
   def test_rot_13(self):
      self.assertEqual(str_rot_13('alph abet'),'nycu norg')
      self.assertEqual(str_rot_13('InsTaGrAm'), 'IafGnGeAz')
      self.assertEqual(str_rot_13('fantASTIC'), 'snagAFGIC')

   def test_str_translate_101(self):
      self.assertEqual(str_translate_101('abcdcba', 'a', 'x'), 'xbcdcbx')
      self.assertEqual(str_translate_101('alphabet', 'a', 'd'), 'dlphdbet')
      self.assertEqual(str_translate_101('Extreme', 'E', 'z'), 'zxtreme')


if __name__ == '__main__':
   unittest.main()

