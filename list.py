#list is a data type in python which is used to store many data
# Properties of list is : mutable, store duplicate value, heterogeneous, ordered
# array and list both are similar the only difference is array is homogeneous and list is heterogeneous

lst = [1, 2, 3, 4, 5, 6, "hello", "hii"]
# print("this is my first list:", lst)
# print("length of my list:", len(lst))
# print("type of my list:", type(lst))

# #Indexing and slicing in list

# print(lst[1:9]) # print values from 1 index to 8 index
# print(lst[0:9:2]) # print value form index 0 to index 8 with skip value 2

# lst.append(100)  # add 100 at last index
# print(lst)

# lst.insert(0, 1000)  # insert 1000 at 0 index

# lst.extend([1, 2, 3, 4])  # add multiple values in list

# new_lst = ["sunil", "Uday"]

# print(lst + new_lst)  # add new list in the old list 

# lst[1] = 97  # replace value at index 1

# lst.pop(1) # remove value at index 1

# lst.remove("hello") # remove value hello from list

# print(lst.index("hii"))  # give the index of value hii

# print(lst.count(2)) # give how many time 2 occur in list

# lst.reverse() # reverse the list

# lst.sort() # sort the list in ascending order


# print(lst)


# lst = [1, 2, 3, [4, 5, 6]]
# print(len(lst))

# print(lst[3][1])  # give value of index 3 in which index 2


lst = [1,2,3,4,5]
lst1 = [9,10,11,12,13]

# print(lst*lst1)
print(lst+lst1)
# print(lst1 - lst)
# print(lst/lst1)
print(lst* 2)

print(2 in lst)