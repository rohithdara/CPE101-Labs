#Lab 7 Groups
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#This function takes a single list and returns a nested list with each sublist having 3 items (if the end doesn't have enough for 3 items, make a sublist with however many there are left)
#list->list
def groups_of_3(l1):
   i = 0
   final = []
   while i < len(l1):
      final.append(l1[i:i+3])
      i += 3
   return final


