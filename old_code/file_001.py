f=open("test_file.txt","w")
#print type(f)
print f. tell()
f.write("hi boss\nwhat the fuck!")
f.close()

''''
str=f.read()
print len(str)

'''




f=open("test_file.txt","a")
f.seek(7,0)
f.write("paul beatty!\n")
	
print f. tell()
f.close()

