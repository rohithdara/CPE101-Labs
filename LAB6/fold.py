#Lab 6 Fold
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#This function returns the sum of every value in a list
#str->int
def sum(l1):
   total = 0
   for x in l1:
      if type(x) == int or type(x) == float or type(x) == list:
         if type(x)==list:
            for y in x:
               if type(y) == int or type(y) == float:
                  total += y
         else:
            total += x
   return total


#This function returns the index of the smallest value in a list
#str->int
def index_of_smallest(l2):
   if l2 == []:
      return -1
   smallest = l2[0]
   smallest_index = 0
   for x in range(len(l2)):
      if type(l2[x])==list:
         for y in range(len(l2[x])):
            if l2[x][y] < smallest:
               smallest = l2[x][y]
               smallest_index = x
      else:
         if l2[x] < smallest:
            smallest = l2[x]
            smallest_index = x

   return smallest_index

 










