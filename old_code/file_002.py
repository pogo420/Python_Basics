f=open("test_file.txt","r")
print f.read()
f.seek(-6,2)
print f.read()
print __name__
print dir()