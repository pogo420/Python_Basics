def data(name):
    return name

def dec(func):
    def wrap(name):
        return "--"+func(name)+"--"
    return wrap

print "before applying change"
print data("pox")

data=dec(data)

print "after applying change"
print data("pox")
    
