import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_sum(self):
      self.assertEqual(sum([1,2,3,'panda']),6)
      self.assertEqual(sum([1,6,[8,10]]),25)
      self.assertEqual(sum([7,8,10]), 25)
   def test_index_of_smallest(self):
      self.assertEqual(index_of_smallest([1,2,3,1]),0)
      self.assertEqual(index_of_smallest([8,9,4,[0,1,3],0,6]), 3)
      self.assertEqual(index_of_smallest([]),-1)
      self.assertEqual(index_of_smallest([1,1,1,1]),0)
      self.assertEqual(index_of_smallest([5,7,4,-4,4,-10,11]),5)

      


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

