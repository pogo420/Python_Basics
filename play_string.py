#declaring variables
str="Wipro_Intel Wipro_limited Intel_India"
a=76.56
b=100

print str
print "type(str):",type(str)
# usage of split
print str.split(" ",1)
#usage of join
print "*".join((str.split(" ",4)))
#use of format like c language
print "%s got %.2f out of %d" %(str,a,b) 

print "\nusage of slice operator : --------"
print "str[:] ",str[:]
print "str[:5]",str[:5]
print "str[5:]",str[5:]





