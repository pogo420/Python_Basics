import sys

file_object=open("test_file.txt","a")
print "file_object initial:",file_object.tell()
print file_object.closed
print file_object.name
print file_object.mode
#print "file_object initial:",file_object.tell()

file_object.write(sys.argv[1])
#file_object.close() #when not commented file_object1 is not getting latest data;Reason:It will only save the file once it is closed
file_object1=open("test_file.txt","r")
print "file_object1 initial:",file_object1.tell()
print file_object1.read()
print "file_object1 after read:",file_object1.tell()

