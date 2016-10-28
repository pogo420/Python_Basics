import os
file_obj=open("test_file01.txt","a")
file_obj.write("Cool file")
file_obj.close()
os.rename("test_file01.txt","cool_file01.pdf")
file_obj.write("\nCool file:open")

