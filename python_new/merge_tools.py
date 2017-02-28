

def duplicate_remover(data_list):
	final_list=["" for _ in range(len(data_list))]
	
	for i,data in enumerate(data_list):
		for j in list(data):
			if j not in final_list[i]:
				final_list[i]=final_list[i]+j
			else:
				pass
	
	for dat in final_list:
		print dat
	
	
	
def merge_the_tools(string, k):
	str_len=len(string)
	split_ratio=str_len/k
	data_list=[0 for _ in range(split_ratio)]
	j=0
	for i in range(split_ratio):
		data_list[i]=string[j:j+k]
		j=j+k
		#print j
	
	#print data_list
	duplicate_remover(data_list)

	
merge_the_tools('AABCAAADA',3)	