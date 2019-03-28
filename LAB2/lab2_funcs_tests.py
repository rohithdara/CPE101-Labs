#Lab 2 Test Cases
#Name:Rohith Dara
#Section:01
##############################################################
import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_math_func1(self):
      self.assertAlmostEqual(funcs.math_func1(0,4),9.14285714286)
      self.assertEqual(funcs.math_func1(5,4),5.90625)
      pass


   def test_math_func2(self):
      self.assertEqual(funcs.math_func2(2.0,5.0,3.0),-1.0)
      self.assertEqual(funcs.math_func2(2.0,5.0,-3.0),0.5)
      pass

   def test_d(self):
      self.assertEqual(funcs.math_func3(5,3,4,8),5.0990195135927845)
      self.assertEqual(funcs.math_func3(10,15,2,3),14.422205101855956)
      pass
      
   def test_is_negative(self):
      self.assertTrue(funcs.is_negative(-7))
      self.assertFalse(funcs.is_negative(10))
      pass

   def test_dividable_by_5(self):
      self.assertTrue(funcs.divisible_by_5(10))
      self.assertFalse(funcs.divisible_by_5(12))
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

