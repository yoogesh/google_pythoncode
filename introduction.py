#all the import moules are used her
import sys
#write the moin function
def main():
    print('Hello There', sys.argv[1])
    print(repeat('Ram', False))
#argv[0] is the script name
#argv[1] and argv[2] are the command line argumemts

#standard way to call the main function

#user defined functions

def repeat (s, exclaim):

    """
    This is a new way of adding description about numners
    Advisable to use rather than the comment lines
    """
    #this fucntion returns s twice if exclaim is false and return with exclamatory mark if its true
    result = s * 2
    # * calculates the size of the resulting pbject at once
    # + calculates the size each time
    # both are overloaded coz they vary differently for different numbers
    if exclaim:
        result = result + '!!!'
    return result

if __name__ == '__main__':
    main()
#Run it using python filename.py __name__

"""
python standard libraries
sys - access to exit, argv, stdin, stdout
re - regular expressions
os - operating systems and file systems
"""

"""
Python Help funtion
help(len)
help(argv)
help(sys)
You will get the default docs about the package
"""
