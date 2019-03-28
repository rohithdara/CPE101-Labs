#Lab 4 Pattern#07
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import driver

def letter(row,col):
	if 4<=col<=9 and 2<=row<=3:
		return 'Z'
	if 4<=col<=6 and 4<=row<=5:
		return 'Z'
	if 7<=col<=9 and 4<=row<=5:
		return 'X'
	if 10<=col<=12 and 4<=row<=6:
		return 'B'
	if 7<=col<=9 and row == 6:
		return 'B'
	else:
		return 'T'

if __name__ == '__main__':
	driver.comparePatterns(letter)