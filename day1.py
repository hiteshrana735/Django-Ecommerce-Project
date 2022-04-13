print("Hello Guys, welcome to the world of python")
var1 = 12
# Data type specifies the type of value that can be stored in a variable. 
# print(var1 + 12)
var2 = 12.3
var3 = "This is a string, I guess!"
var4 = [1, 2, 3, 4]
var5 = {
    "name": "Haaris", 
    "class" : 12
}
var6 = True
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(type(var5))
# print(type(var6))


# Concatenation - Merging of two strings or string and variables together
print("Value of var1 is " +  var3)
# + -> Addition

# F-strings 
print(f"Value of var1 is {var1} and var2 is {var2}")
print("Value of var1 is {} and var2 is {}".format(var1, var2))


# COMMENTS - Text. Internal Documentation.  
"""
THis
is a
multi line
comment
""" 
################################# INTEGER ####################################
# Functions - 
mynum = 34
# print(type(mynum))
abc = str(mynum)
convertingBack = int(abc)
print(pow(2, 3))
print(abs(-12))
# print(f"The datatype is {type(convertingBack)}:")

# STRING FUNCTIONS
mystr = "This is the string"
# print(len(mystr))
# print(mystr.upper())
# print(mystr.lower())
# print(mystr.split(" "))
newlist = mystr.split(" ")
print(newlist)
# print(mystr.count("s"))
# print(mystr.endswith("g"))
# print(mystr.startswith("T"))
# print(mystr.find("i"))
# print(mystr.index("t"))
# print(mystr.isspace())

# List Datatype - 
print(min(12, 43, 23, 2))
print(max(12, 43, 23, 2))