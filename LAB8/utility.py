#Lab 8 Utility
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#This function redefines what is considered equal between 2 values by seeing if they are within 0.00001 of each other
#float,float,float->bool
def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)
