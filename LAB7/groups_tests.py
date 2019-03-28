#Lab 7 Groups Tests
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from groups import *

class TestGroups(unittest.TestCase):
   def test_groups_of_3(self):
      self.assertEqual(groups_of_3([1,2,3,4,5,6]),[[1,2,3],[4,5,6]])
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8]),[[1,2,3],[4,5,6],[7,8]])
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8,9,10]),[[1,2,3],[4,5,6],[7,8,9],[10]])


if __name__ == '__main__':
   unittest.main()