def add(a, b):
    return f"{a} + {b} = {a + b}" 

def sub(a, b):
    return f"{a} - {b} = {a - b}" 

def multi(a, b):
    return f"{a} * {b} = {a * b}" 

def div(a, b):
    return f"{a} / {b} = {a / b}" 

print("\n******** Welcome to the Calculator ********")
num1 = int(input("\nPlease enter a number :\t"))
num2 = int(input("Enter another number : \t"))
print("\n************* Enter you choice *************")
choice = int(input("Press: \n[1] for addition\n[2] for subtraction\n[3] for multiplication, and\n[4] for division \n"))
# print(num1, num2, choice)

print("\n****************** Result ******************\n")
if choice == 1:
    print(add(num1, num2))

elif choice == 2:
    print(sub(num1, num2))

elif choice == 3:
    print(multi(num1, num2))

elif choice == 4:
    print(div(num1, num2))

else:
    print("Invalid Choice")
again = input("Do you want to continue [Y/N]")

while again == "Y" or again  == "y":
    print("\n******** Welcome to the Calculator ********")
    num1 = int(input("\nPlease enter a number :\t"))
    num2 = int(input("Enter another number : \t"))
    print("\n************* Enter you choice *************")
    choice = int(input("Press: \n[1] for addition\n[2] for subtraction\n[3] for multiplication, and\n[4] for division \n"))
    # print(num1, num2, choice)

    print("\n****************** Result ******************\n")
    if choice == 1:
        print(add(num1, num2))

    elif choice == 2:
        print(sub(num1, num2))

    elif choice == 3:
        print(multi(num1, num2))

    elif choice == 4:
        print(div(num1, num2))

    else:
        print("Invalid Choice")

    again = input("Do you want to continue [Y/N]: \t")
else:
    print("Exiting the calculator ...\nBye. Take care.")