'''
Decorator usage in class
Check the variable argument usage:No worries about no of arguments
'''
def chars(c):
    def dec(func):
        def wrap(*var1,**var2):
            return "{0}\n{1}\n{0}".format(c*10,func(*var1,**var2))
        return wrap
    return dec



class TestClass:
    'documentation document'  

    @chars('#')
    def method1(self):
        return "I am a method"
        #print TestClass.__doc__


print TestClass.__doc__
a =TestClass()
print a.method1()
