#Lab 4 Pattern#06
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import driver

def letter(row,col):
	if row == col or row + col==6:
		return 'X'
	else:
		return 'O'

if __name__ == '__main__':
	driver.comparePatterns(letter)