#Lab 8 List Comprehension
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

from objects import *

#This function takes in 2 Points and returns the euclidean distace between them
#Point,Point->float
def distance(p1,p2 = (0,0)):
   return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

#This function takes in a list of Points and returns a list of the distance of each Point and the origin
#list->list
def distance_all(list1):
   final = list(map(lambda x: distance(x,Point(0,0)),list1))
   return final

#This function takes in a list of Points and returns the points that are in the first quadrant of Cartesian plane
#list->list
def are_in_first_quadrant(list2):
   final = list(filter(lambda point: point.x > 0 and point.y > 0,list2))
   return final


