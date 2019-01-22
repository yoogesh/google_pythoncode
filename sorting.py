a = [5, 1, 6, 2]
print(a)
#This sorts the list, but the original list is untouched
print(sorted(a))

strs = ['aa', 'bb', 'zz', 'cc']
print(sorted(strs))
#you can customize the sorted function
#reverse = True means it will sort it in backwards
print(sorted(strs, reverse = True))
"""
Sorting with key
optional argument key
key takes 1 value and retruns 1 value
"""

#key = len --- this will calculate the length of the strings and then sort it

st= ['ccc', 'aaaa', 'd','bb']
print(sorted(st, key=len, reverse = True ))

"""
key = str.lower forces the sorting to treat
both uppercase and lowercase string as same
"""

"""
if you want to sort based on the last letter
create your function
and then assign it to key
def myfn(s):
    retun s[-1]
"""
"""
List.sort() - doesn't return anything
Returns None
but it changes the underlying List
Sort - doesn't work on enumerations
Sorted - works on everything
"""
print(a.sort()) #doesn't work because sort function retruns None
print(a)



"""
TUPLE - fixed size .Same like lists but the size cannot be changed
Immutable - but not that strict
only the size cannot be changed
but the contents can be changed
"""

mytuple = (5, 8 , 'Hola')
print(mytuple)
print(len(mytuple))
print(mytuple[2])
mytuple = (1, 6, 'Hi')
print(mytuple)

#mytuple[2] = 'Hola' cannot be done.
