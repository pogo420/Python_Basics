def continue_func():
	for counter in "Python":
		if(counter=="h"):
			print "Bingo"
			continue # whenever continue is encountered it neglects all statements after it and moves to the next iteration(Nearest loop) 
			print "after continue"
		print counter


def pass_func():
	for counter in "Python":
		if(counter=="h"):
			print "Bingo"
			pass #pass does nothing it is just like a stub
			print "after continue"
		print counter

		
print "Enter 1 for continue and 2 for pass"
choise=input()


if (choise==1):
	continue_func()
else:
	pass_func()