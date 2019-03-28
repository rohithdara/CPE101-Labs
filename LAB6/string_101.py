#Lab 6 String Manipulation
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#This function returns the rot13 encoded value of each value in the string
#str->str
def str_rot_13(s1):
   answer = ''
   for y in s1:
      x = ord(y)
      if x == ' ':
         continue
      elif ord('a') <= x <= ord('z'):
         if x <= ord('m'):
            x += 13
         elif x > ord('m'):
            x -= 13
      elif ord('A') <= x <= ord('Z'):
         if x <= ord('M'):
            x += 13
         if x > ord('M'):
            x -= 13
      answer += chr(x)
   return answer

#This function replaces a specified letter in a string with another specified list
#str,str,str->str
def str_translate_101(s2, let1, let2):
   new_str = ''
   x = list(map(lambda y: new_str + let2 if y == let1 else new_str + y, s2))
   return ''.join(x)

   '''new_str = ''
   for x in range(len(s2)):
      if s2[x] == let1:
         new_str += let2
      else:
         new_str += s2[x]
   return new_str'''
