glonum=0

def inp_validator(number):
    if number>=1 and number<=99:
        return True
    else:
        return False

def octal(i): 
    data=hex(i)
    width=len(bin(glonum)[2:])
    return (data[2:]).rjust(width," ")

def hexa(i):
    data=hex(i)
    width=len(bin(glonum)[2:])
    return (data.upper()[2:]).rjust(width," ")

def binary(i):
    data=bin(i)
    width=len(bin(glonum)[2:])
    return data[2:].rjust(width," ")
    
def data_printer(number):
    for i in range(1,number+1):
        print str(i).rjust(len(bin(glonum)[2:])," "),octal(i),hexa(i),binary(i)
    
    
def print_formatted(number):
    global glonum
    glonum=number
    # your code goes here
    if inp_validator(number):
        data_printer(number)
    else:
        print "Invalid input"
		
if __name__=='__main__':
	n=int(raw_input())
	print_formatted(n)
	