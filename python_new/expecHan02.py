class Errors(Exception):
    'Base class for all Exception'
    pass

class NonAdultError(Errors):
    'class for errors dealing with non value issues'
    pass

class Age(object):

    def takeiput(self):
        try:
            x=int(input("Enter your age MF:"))
            if x<18:
                raise NonAdultError
            else:
                print "you are Adult"

        except NonAdultError:
            print("Your are not adult!MF")


obj=Age()
obj.takeiput()

