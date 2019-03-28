#Lab 8 Funcs Objects
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

from objects import *

#This function takes in 2 Points and returns the euclidean distace between them
#Point,Point->float
def distance(p1,p2):
   return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

#This function takes in 2 Circles and returns True if the circles overlap and False if they do ot overlap
#Circle,Circle->Bool
def circles_overlap(cir1,cir2):
   center_distance = ((cir1.center.x - cir2.center.x)**2 + (cir1.center.y - cir2.center.y)**2)**0.5
   radius_distance = cir1.radius + cir2.radius
   return center_distance < radius_distance





