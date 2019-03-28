#Lab 6 Character Manipulation
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#This function returns True if the character is lowercase and False if not
#str->bool
def is_lower_101(char1):
   if ord('a') <= ord(char1) <= ord('z'):
      return True
   else:
      return False

#This function returns the rot13 encoding of the inputted character
#str->str
def char_rot13(char2):
   x = ord(char2)
   if ord('a') <= x <= ord('z'):
      if x <= ord('m'):
         x += 13
      elif x > ord('m'):
         x -= 13
   elif ord('A') <= x <= ord('Z'):
      if x <= ord('M'):
         x += 13
      elif x > ord('M'):
         x -= 13
   return chr(x)




