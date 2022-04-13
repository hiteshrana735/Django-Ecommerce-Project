# Functions - 
# Anonymous functions (lambda functions) -
from audioop import mul


def sq(x):
    return x ** 2

a = lambda x : x **2 

def printing(x):
    print("Yor wrote", x)
b = lambda x : print("You wrote", x)
# print(a(4))
b(2)

# Create a function that takes one number as input and rerturn square if the number is even and cube if the number is odd
# def sqorcube(x):
#     if x % 2 == 0:
#         return f"The square of {x} is {x ** 2}"

#     else:
#         return f"The cube of {x} is {x ** 3}"

# print(sqorcube(3))
# print(sqorcube(4))
sqc = lambda x : f"The square of {x} is {x ** 2}" if(x % 2 == 0) else f"The cube of {x} is {x ** 3}"

print(sqc(2))

multi = lambda x, y : x + y 
print(multi(2, 4))


# Creating a converter program 
# Length -> m -> cm
# Weight -> kg -> g 
# Temprature -> F -> C

# 1. Length -> m to cm or cm to m
# 2. Weight -> kg to g or g to kg
# 3. Temprature -> F to C or C to F