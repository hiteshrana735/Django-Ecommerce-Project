# ls = list(range(1, 51, 5))
# print(ls)
# for i in range(1, 31):
#     print(i, end=",")

# mystr = "My name is Haaris Saifi"
# mystr = "0123456789"
# for i in range(0, len(mystr)):
#     if i % 2 == 0:
#         print(mystr[i], end=" ")


# ls = list(range(0, 31))
# ls = [1, 2, 3, 4, 3, 2, 1, 2]
# print(ls, end=" ")
# if ls[0] == ls[len(ls) - 1]:
#     print("True")
# else:
#     print("False")

# arr = [3, 2, 6, 7, 8, 44, 66, 234, 244, 1, 65, 78, 22, 12]
# for i in arr:
#     if i != 1:
#         if i % 2 == 0:
#             print(i)
#         else:
#             continue
#     else:
#         break

# ls = [3, 2, 6, 7, 8, 44, 66, 234, 244, 1, 65, 78, 22, 12]
# for i in range(0, ls.index(1)):
#     if ls[i] % 2 == 0:
#         print(ls[i])


# Calculating the HCF 
# num1 = int(input("Enter a number\t"))
# # num1 = 24
# num2 = int(input("Enter another number\t"))
# # num2 = 18
# if num1 < num2:
#     for i in range(1, num1+1):
#         if num1 % i == 0 and num2 % i == 0:
#             hcf = i
#     print("HCF is :", hcf)            

# else:
#     for i in range(1, num2+1):
#         if num1 % i == 0 and num2 % i == 0:
#             hcf = i
#     print("HCF is :", hcf)  


# List comprehension
# names = [1, 2, 3, 4, 5, 6, 7, 8]
# squares = [1, 4, 9, 16, 25, 36]

# squares = []
# print(squares)
# for i in range(1, 11):
#     squares.append(i**2)

# print(squares)

# cubes = []
# print(cubes)
# for i in range(1, 11):
#     cubes.append(i**3)

# print(cubes)

# even_numbers = []
# for i in range(1, 51):
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)

# ls = list(range(0, 31, 5))
ls = [i**2 for i in range(0, 11)]

ls = [i for i in range(0, 31) if i % 3 == 0]

# Syntax for list comprehension - 
# [return_value for variable in collection if condition]

# List comprehension with if-else 
# Dictionary comprehensions

# List slicing and string slicing 
# slice 
print(ls)
# print(ls[3])
print(ls[2:8:2])

str = "This is a string"
print(str[6:])



# Email slicer
email = "shivkumarstudy0@gmail.com" 
email = "maghavahuja01@gmail.com"
email = "inest@hotmail.com"
username = email[0:email.index('@')]
domain_name = email[email.index('@') + 1:]
print(f"Username is {username} and domain name is {domain_name}")