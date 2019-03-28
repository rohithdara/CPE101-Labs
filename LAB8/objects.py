#Lab 8 Objects
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

from utility import *

class Point:
   #Constructor
   #int,int->None
   def __init__(self,x1,y1):
      self.x = x1
      self.y = y1
   #Equality
   #point,point->bool
   def __eq__(self,other):
      return type(other) == Point and epsilon_equal(self.x, other.x, epsilon=0.00001) and epsilon_equal(self.y, other.y, epsilon=0.00001)
class Circle:
   #Constructor
   #point,point->None
   def __init__(self,r,c):
      self.radius = r
      self.center = c

