#Lab 3 Conditional Functions
#
#Name: Rohith Dara
#Professor Name: S. Einakian
#Section: 01

#Takes in 2 numbers and returns the larger one
#float float -> float
def max_101(num1,num2):
   if num1>num2:
      return num1
   elif num2>num1:
      return num2

#Takes in 3 numbers and returns the largest one
#float float float -> float
def max_of_three(num1,num2,num3):
   if num1 > num2 and num1>num3:
      return num1
   elif num2>num1 and num2>num3:
      return num2
   elif num3>num1 and num3>num2:
      return num3

#Takes in the number of days late and returns the corresponding late fee
#int -> int
def rental_late_fee(days):
   if days <= 0:
      return 0
   elif 0<days<=9:
      return 5
   elif 9<days<=15:
      return 7
   elif 15<days<=24:
   	  return 19
   elif days>24:
      return 100