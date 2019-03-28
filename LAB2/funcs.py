#Lab 2 Functions
#Name: Rohith Dara
#Section: 01

import math

def math_func1(x,y):
#Compute a mathematical equation
#float -> float
     x = float(x)
     y = float(y)
     answer = ((x**3) + (y**3))/(5*x + 7)
     return(answer)

def math_func2(a,b,c):
#Compute the upper value of the quadratic equation
#float ----> float
     a = float(a)
     b = float(b)
     c = float(c)
     quad = (-1*b + math.sqrt((b**2) - 4*a*c))/(2*a)
     return(quad)


def math_func3(x1,y1,x2,y2):
#Compute the euclidian distance between 2 points
#float -> float
     x1 = float(x1)
     y1 = float(y1)
     x2 = float(x2)
     y2 = float(y2)
     euclid = math.sqrt((x1-x2)**2+(y1-y2)**2)
     return(euclid)

def is_negative(negtest):
#Determine if a number is negative
#float ----> bool
     negtest = float(negtest)
     final = bool(negtest < 0)
     return(final)      

def divisible_by_5(div5):
#Determine if a number is divisible by 5
#float ----> bool
     div5 = float(div5)
     end = bool((div5) % 5 == 0)
     return(end)

