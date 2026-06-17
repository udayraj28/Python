# tupe is data type in python, it is a collection of immutable item 
# properties of tuple is: immutable, heterogeneous, allow duplicate values, ordered

tpl = (1,2,3,4,5,6,"hello",2.5)
print("this is my first tuple:", tpl)
print("length of my tuple is:", len(tpl))
print("type of my tuple is:", type(tpl))

print("indexing in tuple>>>>>>>>>>>>>>>>>>>")
print(tpl[0])
print(tpl[1])
print(tpl[2])
print(tpl[3])

print("slicing in tuple>>>>>>>>>>")
print(tpl[2:4])
print(tpl[0:5:2])

print("operation in tuple>>>>>>>>>>>>>>>>>")

print(tpl.count(4)) # it return the no of time 4 occur in tuple
print(tpl.index(5)) # it return the index value of 5

print(tpl[::-1]) # reverse the tuple

print("Tuple Unpacking >>>>>>>>>>>>>>>>>>>>>>>>>>>")
a, b, c = (1,2,3) # in tuple unpacking we assign the variable to each element in tuple 
print(a)          # every elememt should have a assigned variable otherwise it shows error
print(b)
print(c)


a = 1,2   # it behave like a tuple by default 
print(a)
print(type(a))
print(len(a))


#For doing other operations in tuple we have to first done typecasting 

print("Typecasting >>>>>>>>>>>>>>>>>>>>>>>..........")

b = (1,2,3,4,56,4,6,2,2,"uday")
print("This is tuple before typecasting", b)

print("Type casing in python tuple")
print("Convert tuple into list")
lst = list(b)
print("this is my tuple convert into list after typecasting:", lst)
print("length of my list:", len(lst))
print("type of my list:", type(lst))

lst.append(100)
print("List after adding item", lst)
print("Again convert list into tuple using type casting")
b = tuple(lst)

print("tuple after adding item:", b)

# use of in operator in tuple 

print("uday" in b)
