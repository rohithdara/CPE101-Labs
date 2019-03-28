#Lab 4 Pattern #02
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import driver

def letter(row,col):
	if 0<=row<=9 and 0<=col<=20:
		return 'R'
	if 10<=row<=20 and 0<=col<=20:
		return 'Q'


if __name__ == '__main__':
	driver.comparePatterns(letter)
