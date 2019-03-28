#Lab 7 Parse Files
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import sys

#This function returns the count of each data type in a file as well as the sum of the floats/ints if prompted
#->str
def fileio():
   argval = sys.argv
   floats = 0
   ints = 0
   others = 0
   Sum = 0

   if len(argval) == 2:
      try:
         fin = open(argval[1])
         lines = fin.readlines()
         for i in lines:
            space =  ' '
            i = i.split( )
            for item in i:
               try:
                  item = int(item)
                  if type(item) == int:
                     ints +=1
                     Sum += item
               except:
                  try:
                     item = float(item)
                     if type(item) == float:
                        floats += 1
                        Sum += item
                  except:
                        others +=1
         print('Ints: %d' % ints)
         print('Floats: %d' % floats)
         print('Other: %d' % others)
      except IOError as err:
         print('Unable to open ' + argval[1])

   elif len(argval) == 3:
      if argval[1] == '-s':
         try:
            fin = open(argval[2])
            lines = fin.readlines()
            for i in lines:
               space =  ' '
               i = i.split( )
               for item in i:
                  try:
                     item = int(item)
                     if type(item) == int:
                        ints +=1
                        Sum += item
                  except:
                     try:
                        item = float(item)
                        if type(item) == float:
                           floats += 1
                           Sum += item
                     except:
                           others +=1
            print('Ints: %d' % ints)
            print('Floats: %d' % floats)
            print('Other: %d' % others)
            print('Sum: %.2f' % Sum)
         except IOError as err:
            print('Unable to open ' + argval[2])
      elif argval[2] == '-s':
         try:
            fin = open(argval[1])
            lines = fin.readlines()
            for i in lines:
               space =  ' '
               i = i.split( )
               for item in i:
                  try:
                     item = int(item)
                     if type(item) == int:
                        ints +=1
                        Sum += item
                  except:
                     try:
                        item = float(item)
                        if type(item) == float:
                           floats += 1
                           Sum += item
                     except:
                           others +=1
            print('Ints: %d' % ints)
            print('Floats: %d' % floats)
            print('Other: %d' % others)
            print('Sum: %.2f' % Sum)
         except IOError as err:
            print('Unable to open ' + argval[1])
      else:
         print('Usage: [-s] file_name')

   elif len(argval) <2 or len(argval)>3:
      print('Usage: [-s] file_name')

fileio()

