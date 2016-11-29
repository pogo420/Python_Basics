'''
#################################
Version 1: Driving data to dictionary.
Version 2: Need to interact with excel sheet
#################################
'''
import os
import os.path
import inspect 
import re

path_search=r"C:\Users\arnabmux\Documents\codes\python\Regular_expression"

# creating a list of test files
file_list=[ temp for temp in os.listdir(path_search) if ".txt" in temp]

#declaring a list for storing files with complete path(absolute)
file_list_path=[]

file_det={}

#function for checking status
def test_status_checker(temp):
	match=re.search(r'(^Test status:)(.)(\w*)',temp)
	status=""
	if match:
		status= match.group(3)
	else:
		pass
		#print "no match"
	return status

#function for extracting lines of file
def file_parser(file_ptr):	
	status=""
	for temp1 in file_ptr:
		status=test_status_checker(temp1)
		if status:
			break
		else:
			pass
	return status
	
	
	
	#generating absolute path with file name
for temp in file_list:
	file_list_path.append(os.path.join(path_search,temp))

'''
verifying the list
print file_list_path
'''

for temp in file_list_path:
	file_ptr=open(temp,"r")
	file_det[os.path.basename(temp)]=file_parser(file_ptr) #storing data in dictionary 
	file_ptr.close()

#printing data of results

for temp in sorted(file_det.keys()):
		print temp,":",file_det[temp]

#print file_det

