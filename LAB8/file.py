#Lab 8 File Input
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#This function opens 'in.txt' and prints each line with a line number, character count, and the line text
#->str
def opener():
   fin = open('in.txt')

   linecount = 0
   for aline in fin:
      if len(aline) > 0:
         aline = aline.strip()
         print('Line {} ({} chars): {}'.format(linecount,len(aline),aline.rstrip()))
         linecount += 1
   fin.close()
opener()