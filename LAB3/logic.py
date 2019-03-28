#Lab 3
#
#Name: Rohith Dara
#Professor: S. Einakian
#Section: 01

#Take in a number and return true if it is even and false if it is odd
#int -> bool
def is_even(num):
   even = bool(num%2 == 0)
   return even

#Take in a number and return true if it is in any of the specified intervals and false if not
#float -> bool
def in_an_interval(num):
   interval = bool(-2<=num<9 or 22<num<42 or 12<num<=20 or 120<=num<=127)
   return interval


