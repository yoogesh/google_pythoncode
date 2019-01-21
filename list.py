"""
Lists are generally enclosed in square brackets. 
Access it using the index numbers
index starts from 0

"""

colors = ['red', 'green', 'blue']   
 
print("colours[0] :", colors[0])
print("colours[1] :",colors[1])
print("colours[2] :",colors[2])

"""
When 
a = colors 
It dosent make a copy 
Both a and colors point to the same memory 
"""

a = colors
a.append("Hello")

print("a[3] is: ", a[3])
print("colours[3] is:", colors[3])   #Now both colors and a point to the same location. Chnages in one will be reflected in another

c = a + colors  #Both the contents 4 + 4 is added to the c 
print("Length of c = a + colors is :", len(c))   


"""
FOR - like any other language 
IN - for var in list 
Checks whether var is in the list and loops it coz there is for 
"""
for name in colors:
    print(" \n Printing the contents in the list:", name)


"""
Range function yeilds numbers 0, 1, n-1 
range(a,b) returns a, a+1 b-1
but it doesnt include the last number

"""
for i in range(10):
    print("\n Range :", i)


"""
LIST METHODS 

list.append(elem) - adds a element at the end of the list 
list.insert(index,elem) - adds a element at the given index 
list.extend(list2) - adds the elements in list2 to this list 
list.index(elem) - searches the element in the list and gives it index
list.remove(elem) - searches the fist instance of the element and removes it 
list.sort()
list.reverse()
list.pop(index) - removes and returns the element at the given index 

"""

dummylist = ["ram", "yoogesh", "G"]
print("\n", dummylist)
dummylist.append("Hola")
print("\n", dummylist)
dummylist.insert(4, "Index4")
print(dummylist)
print("index of the ram", dummylist.index("ram"))
print(dummylist.pop(3))
print("\n", dummylist)

demo = ["Extended", "list"]
dummylist.extend(demo)
print("\n extended list is :", dummylist)

#list slicing 

