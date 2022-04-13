# var1 = 20 
# var2 = 30
# Relational operators or Conditional operators -> >, <, >=, <=, ==, !=
# if var1 == var2:
#     print("The condition is true")
# else:
#     print("The condition is false")
# print("This is another print statement")
# Two numbers, Product More than 1000 -> print sum -> otherwise product 


num1 = 40
num2 = 40
# if num1 * num2 >= 1000:
#     print("Sum is", num1 + num2)
# else:
#     print("Product is", num1 * num2) 


# Multiple conditions -> 
# Logical operators -> AND, OR and NOT 

# if num1 < 30 or num2 < 30:
#     print("Both the conditions are true")
# else:
#     print("Both the conditions are not true")



# 2 ways ->
x = 44 
# if x < 10:
#     print("Con1 is true")
# elif x == 20:
#     print("Con2 is true")
# elif x > 20:
#     print("Con3 is true")

# Nested If-else
# if x > 10:
#     print("Con1 is true, x is greater than 10")
#     print("checking another condition ... ")
#     if x > 20:
#         print("Con2 is true, x is greater than 20")   
#     else:
#         print("Con2 is false, x is lesser than 20")
# else:
#     print("Con1 is false, x is lesser than 10")

# Take two numbers, print which one is greater?
# number1 = 34
# number2 = 34
# if number1 > number2:
#     print("Number 1 is greater than Number 2")

# elif number2 == number1:
#     print("Number 2 is equal to Number 1")

# else:
#     print("Number 2 is greater than Number 1")

# Take 3 numbers, Print which one is greatest, smallest and middle one?


value1 = 135
value2 = 135
value3 = 1250
if value1 > value2 and value1 > value3:
    print("Value 1 is greatest")
    if value2 > value3:
        print("Value 2 is middle one, Value 3 is smallest")
    else:
        print("Value 3 is middle one, Value 2 is smallest")

elif value2 > value1 and value2 > value3:
    print("Value 2 is greatest")
    if(value1 > value3):
        print("Value 1 is middle one and value 3 is smallest")
    else:
        print("Value 3 is middle one and value 1 is smallest")

elif value3 > value1 and value3 > value2:
    print("Value 3 is greatest")
    if value1 > value2:
        print("Value 1 is middle and value 2 is smallest")
    else:
        print("value 2 is middle and value 1 is smallest")

else:
    print("None of the values is greatest, middle or smallest")

# Taking user from input 
user_input = int(input("Enter a number"))
print(user_input + 10)

# BMI Calculator - Body Mass Index - 
# wt = 40
# m = 3 
# bmi = wt / m**2 