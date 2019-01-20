"""
Python has a new string package str
there is an old package string
prefer not to use
"""

print("You can have '  inside double quotes")
print('Same way " inside single quotes')


"""
Python strings are immutable
means - they cannot be changed after they have created
"hello" + "man" builds a new string hello man
"""

# if s  = hello then s[1] is e
#because index starts from 0

a = 4.2
text = 'value of a is ' + str(a)
# text = string + a does not convert a automatically to stringself
#We have to use str function to convert it
print(text)

# there is no ++ operator. Instead += is applicable
print (5//5) #does the integer division

# raw - r - denotes the contents inside without treating any backslashes and quotes
value ='hello'
print(value.upper())

"""
given s contains a string
then these are the follwing commands
s.lower() s.upper()

s.strip() - returns a strign by removing whitespaces at the start and the end
s.isalpha()/isdigit()/ispace()
s.startswith()/ endswith()

s.find(other) - searches for the other string within the string and returns
th first index where it begins or -1 if not founf

s.split(,)
s.join(aaa,bbb,ccc) - joins and produce as one single result as aaabbbccc
"""

"""
STRING SLICES

Refers to sub parts .

String [start:End] - is the elements beginning at start
and extending up to but not including end

if s = h  e  l  l  o
       0  1  2  3  4
      -5 -4 -3 -2 -1
s[1:4]- is ell (starts at index 1 and exteds and not including 4)
s[1:] - ello (omitting the index defaults to the start or end)
s[:] - hello (omitting both always gives copy of the whole string)
s[1:1000] - ello (index is too big and truncated down to string lenght)

s[-4]- e from the 4th end
s[:-3]- He going up to but not including the last3 char

any index n - s[:n] + s[n:] = {value for value in variable}

"""




text = "%d days more for flight to %s" %(5, 'Chennai')
print(text)

"""
To add it to the next line
text = ( string content
        %(Corresponding content))
UNICODE ---- Generally python is not UNICODE

to create a unicode string use the letter u like r for raw

to read the unicode strings

value = s.encode('utf-8')

"""


"""
CONDITIONAL STATEMENTS

IF - checks for a condition and executes it if its true
elif - check for another clause
else: finaly do this if nothing matches

"""
