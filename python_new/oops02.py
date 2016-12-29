class Test:
    'class docu'
    x=2
    j1=1
    def method1(self):
        self.p=Test.x+2
        self.j=Test.j1+1
        self.__doc__='obj document'


a=Test()
a.method1()

'''
print a.p
print Test.p
'''
print "object attributes:"
print a.__class__
print a.__module__
print a.__doc__

print "\ndir class:"
print dir(Test)
print "\ndir object:"
print dir(a)


print "\ndict class:"
for i in Test.__dict__.keys():
    print "{0}-->{1}".format(i,Test.__dict__[i])

print "\ndict object:"
for i in a.__dict__.keys():
    print "{0}-->{1}".format(i,a.__dict__[i])

'''
Direct execution:

>>> 
object attributes:
__main__.Test
__main__
obj document

dir class:
['__doc__', '__module__', 'j1', 'method1', 'x']

dir object:
['__doc__', '__module__', 'j', 'j1', 'method1', 'p', 'x']

dict class:
x-->2
__module__-->__main__
method1--><function method1 at 0x0000000002DB3828>
__doc__-->class docu
j1-->1

dict object:
p-->4
j-->2
__doc__-->obj document
>>>


------------------------------------------------------------
Importing case through another file:
import oops02
oops02.Test.__module__

>>> 
object attributes:
oops02.Test
oops02
obj document

dir class:
['__doc__', '__module__', 'j1', 'method1', 'x']

dir object:
['__doc__', '__module__', 'j', 'j1', 'method1', 'p', 'x']

dict class:
x-->2
__module__-->oops02
method1--><function method1 at 0x0000000002D83828>
__doc__-->class docu
j1-->1

dict object:
p-->4
j-->2
__doc__-->obj document
>>> 

'''




        
