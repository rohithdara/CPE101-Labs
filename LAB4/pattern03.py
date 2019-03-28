#Lab 4 Pattern#03
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import driver

def letter(row,col):
	if 0<=row<=19 and 0<=col<=9:
		return 'X'
	if 0<=row<=19 and 10<=col<=21:
		return 'O'

if __name__ == '__main__':
	driver.comparePatterns(letter)