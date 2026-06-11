# print("hello python!!")

num = 10
print(num)

# Variable can br declared by any alphabet or _ but not by number

age = 10
Age = 21

# variable can not be declared using special characters except _
_name = "python"


# String ✌️

name = "Uday"
print("This is my first string:", name)
print("Type of variable name is:", type(name))  # type function is used to find out thr type of variable
print("Length of my string is:", len(name)) # len() function is used to find out the the length of the string

print("indexing..........")  # indexing is start from 0 and reverse indexing start from -1
print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("Slicing...........")
print(name[0:3]) # start indexing from 0 to 2
print(name[0:3:2]) # print value from 0 to 2 with skip value 2
print(name[::-1])  # reverse the string


print("Upper case...............")
name = "Uday"
print("upper case of name is:", name.upper()) # .upper() function is used to change the string in upper case

print("Lower case...............")
name = "UDAY RAJ SHARMA"
print("lowe case of name is:", name.lower()) # .lower() function is used to change the string in lower case

print("Case fold funtion...............")
x = "ROHIT"
print(x.casefold())  # casefold() function also use to change the string in lower case

print("Title function.......")
name = "sunil"
print(name.title()) # title() function used to make the first letter of the each word capital in a sentence

print("Capitalize function..........")
name = "ritik is good"
print(name.capitalize()) # only make the first letter capital in sentence


# print(name.index("i"))
# print(name.count("r"))
# print(name.find("n"))

college = "hello anand"
print(college.replace("hello", "hiii"))
print(college.upper())

# print = 1
# print(print)

# str = 5
# print(str)


num = "1234"
print(num.isdigit()) # used to find out wharther stored value is digit or not

char = "hello"
print(char.isalpha()) # used to find out whether stored value is alphabetic or not

char_1 = "hello1234"
print(char_1.isalnum()) # used to find our whether stored value is alphanumeric or not

name = "  Uday Raj Sharma"
print(name.split())  # used to split the string in list

print(name.strip()) # used to remove space from starting and trailing


# intro = '''n Python, errors help programmers identify and fix problems in their code.
#  One common error is TypeError: 'str' object is not callable, which occurs when a string value is mistakenly used as a function.
#  This usually happens when a variable containing text is followed by parentheses (), 
#  causing Python to attempt to call the string as if it were a function. 
#  Understanding this error helps developers write more accurate and efficient Python programs.
# '''

# print(intro)

# name = "Uday Raj Sharma"
# print(f"My name is {name}") # it is a formating string in this we use the variablr directly in the string


# path = r"D:\Desktop1\Desktop\Upflairs training\Python>"  # raw string used to store path
# print(path)


college_name = "Anand International College of Engineering"
college_address = "Kanota, Jaipur"

print(college_name + " " + college_address)

# print(college_name * college_address)  #can not multiply string 

print(college_address * 3)

print("an" in college_name)  # here "in " is an operator used to find out whether the specific character or word is present in string or not