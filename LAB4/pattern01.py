#Lab 4 Pattern #01
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import driver

def letter(row,col):
	if row == 9 and col ==9:
		return 'Z'
	else:
		return 'G'

if __name__ == '__main__':
	driver.comparePatterns(letter)
	

