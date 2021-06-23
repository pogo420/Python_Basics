import sys

file_ptr=open("test_file.txt","a")

print "Position before write:",file_ptr.tell() 

file_ptr.write(sys.argv[1])

print "Position after write:",file_ptr.tell() 

file_ptr.seek(-3,2) 

print "changing position:",file_ptr.tell() 

