#Lab 8 Funcs Objects Tests
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      point1 = Point(1,2)
      self.assertEqual(point1.x , 1)
      self.assertEqual(point1.y, 2)
      
      point2 = Point(-1,8)
      self.assertEqual(point2.x , -1)
      self.assertEqual(point2.y, 8)

      point3 = Point(-45,2)
      self.assertEqual(point3.x , -45)
      self.assertEqual(point3.y, 2)


   def test_circle(self):
      circle1 = Circle(5,Point(2,3))
      self.assertEqual(circle1.radius,5)
      self.assertEqual(circle1.center.x,2)
      self.assertEqual(circle1.center.y,3)

      
      circle2 = Circle(3,Point(-4,6))
      self.assertEqual(circle2.radius,3)
      self.assertEqual(circle2.center.x, -4)
      self.assertEqual(circle2.center.y,6)

      circle3 = Circle(25,Point(-2,4))
      self.assertEqual(circle3.radius,25)
      self.assertEqual(circle3.center.x,-2)
      self.assertEqual(circle3.center.y,4)

   def test_distance(self):
      p1 = Point(3,4)
      p2 = Point(6,7)
      self.assertAlmostEqual(distance(p1,p2),4.242640687119285)

      p1 = Point(1,1)
      p2 = Point(2,2)
      self.assertAlmostEqual(distance(p1,p2),1.4142135623730951)

      p1 = Point(0,0)
      p2 = Point(-1,0)
      self.assertAlmostEqual(distance(p1,p2),1)

   def test_circles_overlap(self):
      cir1 = Circle(5,Point(0,0))
      cir2 = Circle(2,Point(1,0))
      self.assertTrue(circles_overlap(cir1,cir2))

      cir1 = Circle(3,Point(4,5))
      cir2 = Circle(6,Point(2,2))
      self.assertTrue(circles_overlap(cir1,cir2))

      cir1 = Circle(1,Point(1,1))
      cir2 = Circle(2,Point(8,10))
      self.assertFalse(circles_overlap(cir1,cir2))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

