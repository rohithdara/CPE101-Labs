#Lab 4 Pattern#05
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import driver

def letter(row,col):
	if col >= row:
		return 'W'
	else:
		return 'T'



if __name__ == '__main__':
	driver.comparePatterns(letter)