# print("Welcome to BMI Calculator")
# height = float(input("Enter you height(in mtrs.)"))
# weight = float(input("Enter you weight(in kgs.)"))
# print("Height is", height)
# print("weight is", weight)
# bmi = weight / (height ** 2)
# print("BMI : ", round(bmi, 1))
# if bmi <= 18.5:
#     print("You are Underweighed")

# elif bmi <= 24.9:
#     print("You are normally weighed")

# elif bmi <= 29.9:
#     print("You are Overweighed")

# else:
#     print("You are obese")

# Iterative Control structure
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
a = 1
# while a <= 50:
#     print(a)
#     a = a + 2 

# Membership operator
# ls = ['1', '2', '3', '4']
# if "2" not in ls:
#     print("Yes")
# else:
#     print("No")

student_names = ['Rachit', 'Shiv', 'Nitin', 'Maghav', 'Hitesh', 'Shivam', 'Chandresh', 'Shikha', 'Shibna', 'Xavier']

# while 'Rachit' in names:
#     print("It is present")
#     names.clear()

# Loops with conditional statements
# val = 1
# Even numbers 
# while val <= 50:
#     if val % 2 == 0:
#         print(val)
#     else:
#         print("Not an even number")
#     val += 1

# Create a list of odd numbers using while loop
odd_number_list = []
odd_number_count = 0
i = 1 
# while i <= 50:
#     if i % 2 != 0:
#         # print(i)
#         odd_number_list.append(i)
#         odd_number_count += 1
#     i += 1
# print(odd_number_list)
# print("The Amount of odd numbers is", len(odd_number_list))
# print("The Amount of odd numbers is", odd_number_count)
# print(f"The Amount of odd numbers is {odd_number_count}")
# print("The Amount of odd numbers is {}".format(odd_number_count))

# For Loop
for i in student_names:
    # print(i)
    if i.startswith('X'):
        print(i)