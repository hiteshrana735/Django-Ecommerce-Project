def add():
    print(2 + 2)

# add()

# Arguments - values that are passed to the function while calling it.

def add2(a, b):
    print(a + b)

# add2(20, 34)
# add2(50, 134)
# add2(20, 30, 40)
# add2(30,40)

def message(name):
    print(f"Hi {name}, How are you?")

# message("Asher")
# message("Rachit")
# message("Shivam")
# message("Hitesh")

def welcome(username = "Stranger"):
    print(f"Hi {username}, Welcome to our website")

# welcome("Asher")
# welcome()
# welcome()
# welcome("Nitin")
# welcome()
# welcome("Aarzoo")

def average(a, b, c):
    avg = (a + b + c) / 3
    print(f"Average is {avg}")

# average(2, 4, 6)
# average(2, 4, 6, 8, 10)

def avg(*a):
    sum = 0
    for i in a:
        sum += i

    print(f"The average is {sum / len(a)}")

numbers_list = [2, 4, 6, 8, 10]
# avg(*numbers_list)

ls = [1, 3, 5, 7, 9, 11, 13, 15]
# avg(*ls)

# Return statement

def sub(a, b):
    print(a - b)
    # return "This is a string"
    return a - b 


# sub(23, 3)
# sub(47, 4)

myresult = sub(10, 5)
myresult = sub(35, 6)
print("Value of myresult variable is", myresult)


# Function inside a function 
def intro():
    print("Hi I am a human")

def myIntroduction():
    intro()

def introduceYourself():
    myIntroduction()

# intro()
# myIntroduction()
# introduceYourself()


def f1(k):
    print(k)
    if k > 1:
        f1(k-1)

f1(15)