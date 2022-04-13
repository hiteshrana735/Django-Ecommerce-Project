# Functions - 
# What is a function ?
# for i in range(1, 11):
#     print(i)
# Calculator - Add(), Sub(), Mul() and Divide()
def morningText():
    userTime = int(input("Enter the current time (Hours)\t"))
    if 6 < userTime < 12: 
        print("Hi, A very good Morning")
    else:
        print("Thank you. \nHave a good day")

# morningText()

def table():
    userinput = int(input("Enter a number to calculate the table"))
    for i in range(1, 11):
        print(userinput * i)
        
# table()

def evenNumber():
    userinput = int(input("Enter a number"))
    print(f"Printing the even numbers from 1 to {userinput} ... ")
    for i in range(1, userinput + 1):
        if i % 2 == 0:
            print(i, end=", ")
    print()

# evenNumber()
# evenNumber()

def message():
    print("Hi")

message()
# Arguments, Return Statements