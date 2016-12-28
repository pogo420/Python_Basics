'''
# lamda for generating function
def gen(x): return lambda n: n+x

g=gen(3)
h=gen(4)
print g(2)
print h(2)

#lamda basic usage

y= lambda p: type(p)

print y([])
'''
# true potential of python
'''
string="This is true"
print string

tocken=string.split()

print tocken

tocken_len=map(lambda x:len(x),tocken)

print tocken_len

def rev(x):
        x.reverse()
        return x


tocken_rev=map(lambda x:"".join(rev(list(x))),tocken)

print tocken_rev

string_rev= " ".join(tocken_rev)

print string_rev
'''
'''
list1=["Paap","dog","Goat"]

x=filter(lambda p:p[0].isupper(),list1)

print x

'''

list2=["Sam","House","90"]

y=reduce(lambda x,y:x+y,list2)

print y










