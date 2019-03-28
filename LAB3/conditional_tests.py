#Lab 3 Conditional Test Cases
#
#Name: Rohith Dara
#Professor Name: S. Einakian
#Section: 01

import unittest
import conditional
#You can delete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(conditional.max_101(17,28),28)
      self.assertEqual(conditional.max_101(1232123,66454524),66454524)
      self.assertEqual(conditional.max_101(23.14,534.23),534.23)
  
   def test_max_of_three(self):
   	self.assertEqual(conditional.max_of_three(8,6,5),8)
   	self.assertEqual(conditional.max_of_three(2,5,4),5)
   	self.assertEqual(conditional.max_of_three(2,8,25),25)
   	self.assertEqual(conditional.max_of_three(64,23,45),64)

   def test_rental_late_fee(self):
      self.assertEqual(conditional.rental_late_fee(7),5)
      self.assertEqual(conditional.rental_late_fee(28),100)
      self.assertEqual(conditional.rental_late_fee(0),0)
      self.assertEqual(conditional.rental_late_fee(20),19)
      self.assertEqual(conditional.rental_late_fee(15),7)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

