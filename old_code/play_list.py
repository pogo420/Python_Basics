list=[]
print type(list)
#using append function one at time
list.append({"one":1,"two":2})
# a list can contain a dictionary
print type(list[0])

list.append([1,2,'a',3.5])
# a list can contain a list
print list[0],"\t",list[1]
print type(list[0]),type(list[1])

list.append((1,'a',0.5))
# a list can contain a tuple
print list[0],"\t",list[1],"\t",list[2]
print type(list[0]),type(list[1]),type(list[2])

print "deleting index 1"
del(list[1])

list1=["ram","sam","ram",1,2,3,1]
print list1

list1.remove("ram")
print list1

list1.reverse()
print list1

list1.sort()
print list1

print "list1.pop():",list1.pop()
print "list1:",list1

print len(list1)
