# dictionary is a key value pair data type in python. pair of key and value is called item
# properies of dictionary is: unordered, mutable, can not contain duplicate key, can contain duplicate values.

# student = {
#     "name" : "Uday",
#     "Class" : "3rd year",
#     "Branch" : "CSE",
#     "Roll_no" : "23CS101",
#     "Address" : "Jaipur"
# }

# print("this is my dictionary", student)
# print("type of my dictionary is:", type(student))
# print("length of my dictionary is:", len(student))

# print("Find value at specific key ..................")
# print(student["name"])
# print(student["Class"])
# print(student["Branch"])
# print(student["Roll_no"])

# print("Use of get() function............") # used to find out the value at specific key
# print(student.get("name"))

# print("Keys of my dictionary is:", student.keys()) # used to find out the keys in dictionary
# print("Values in my dictionary is:", student.values()) # used to find out valuse in dictionary
# print("Items in dictionary is:", student.items()) # used to find out items in dictionary

# student["CGPA"] = 9.2 # add new key with value
# student["name"] = "Vishal" # update the value of key name 
# print(student)

# print(student.update({"name" : "Sunil"}))
# print(student)

student = {
    "name" : ["Uday", "Sunil"],  # adding multiple values in a single key using list, tuple 
    "Class" : "3rd year",
    "Branch" : ["CSE", "AI"],
    "Roll_no" : "23CS101",
    "Address" : "Jaipur",
}

a = input("Enter your key") # print the value of key given by user
print(student[a])

print(student.setdefault("name ","vishal"))

print(student)
