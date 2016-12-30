def main():
    try:
        
        x=int(input("Enter a value:"))
        print "You Entered:"
        
    except Exception:
        
        print "Wrong!!"

    else:
        print "No Error"

    finally:
        print "The END"
    


if __name__=='__main__':
    main()


'''
>>> 
Enter a value:67
You Entered:
No Error
The END
>>> ================================ RESTART ================================
>>> 
Enter a value:yu
Wrong!!
The END
>>> 
