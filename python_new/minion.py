def minion(string):
	Stuart,Kevin=0,0
	s_length=len(string)
	vowel=['A','E','I','O','U']
	for i in xrange(s_length):
		if string[i] in vowel:
			Kevin+=len(string)-i
		else:
			Stuart+=len(string)-i
	
	if Stuart>Kevin:
		print "Stuart",Stuart
	elif Stuart==Kevin:
		print "Draw"
	else:
		print "Kevin",Kevin		
	#print vowelIndex

minion(raw_input())