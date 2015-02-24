#!/usr/bin/env python
import re

def getsquare(userNumber):
	# Make sure the input is an integer number
	userNumber = int(userNumber)
	userNumber = userNumber**2


def stringstats(mystr):
	letters = re.compile('.')
	spaces = re.compile('\s')

	letterlist = letters.findall(mystr)
	spaceslist = spaces.findall(mystr)

	print "there are " + str(len(letterlist)) + " letters in " + mystr
	print "there are " + str(len(spaceslist)) + " spaces in " + mystr

def countletters(mystr):
	count = 1

	for i in range(len(mystr)):
		count = count + 1
	return count

# Ask for the number and store it in userNumber
userNumber = raw_input('Give me an integer number: ')
getsquare(userNumber)

# Print square of given number
print 'The square of your number is: ' + str(userNumber)

mystr = raw_input('Enter a string: ')
stringstats(mystr)

print "there are " + str(countletters(mystr)) + " characters in " + mystr
