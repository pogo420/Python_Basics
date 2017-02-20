from string import ascii_lowercase as alpha

def print_rangoli(size):
	width=(4*size)-3
	for i in range(size-1):
		print ('-'.join(alpha[size-1:size-1-i:-1]+alpha[size-1-i:size])).center(width,'-')

	for i in range(size):
		print ('-'.join(alpha[size-1:i:-1]+alpha[i:size])).center(width,'-')
		
size=int(raw_input())
print_rangoli(size)