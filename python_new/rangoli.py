from __future__ import print_function
from string import ascii_lowercase as letters
def print_rangoli(limit):
	for i in range(limit-1):
	    print (('-'.join(letters[limit-1:limit-i-1:-1]+letters[ limit-i-1:limit])).center(limit*4-3,'-'))
	print("----")
	for i in range(limit):
		print (('-'.join((letters[limit-1 : i:-1])+letters[ i:limit])).center(limit*4-3,'-'))
	
	
print_rangoli(4)		
