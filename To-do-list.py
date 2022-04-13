# import time
# ts = time.ctime(time.time())
# def add_new():
#     fp = open("todolist.txt", "a")
#     work = input("Enter Work :\t")
#     time = input("Enter time :\t")
#     entry = f"Work => {work} || Time => {time} || Entry created at - {ts}\n"
#     fp.write(entry)

# def view_all():
#     fp = open("todolist.txt", "r")
#     print(fp.read())

# print("*-*-*-*-*-*-WELCOME-*-*-*-*-*-*")
# print("Choose One: Press\n[1] To View Existing details\n[2] To Add New")
# choice = int(input("Enter here :\t"))
# if choice == 1:
#     view_all()
# elif choice == 2: 
#     add_new()
# else:
#     print("Invalid Choice")


# OOP - Object Oriented Programming System --> OOPS 

class Student:
    name = "Haaris"
    std = 12 

    def intro(self):
        return f"Hi, I am {self.name}. I read in class {self.std}"

    def changevalues(self, n, s):
        self.name = n
        self.std = s 

# s1 = Student()
# print(s1.name)
# print(s1.intro())

# s1.changevalues("Rachit", 23)
# print(s1.intro())

# s2 = Student()
# print(s2.name, s2.std)
# print(s2.intro())
# s2.changevalues("Shiv", 4)
# print(s2.intro())

# Instantiation : Creation of object(Instance)
# Create a class CAR with properties like brand, model and price. Create a method in it that shows all the values
# 
# 
class Car:
    brand = "Volkswagen"
    model = "Polo"
    price = 1923000

    def show(self):
        return f"Details of the car :\nBrand name: {self.brand}\nModel name: {self.model}\nPrice: {self.price}"

Car.brand = "Koeniesegg"
Car.model = "Regera"
Car.price = 0
c1 = Car()
print(c1.show())  

c2 = Car()
# c2.brand = "Lamborghini"
# c2.model = "Huracan Perfomante"
print(c2.show())  

c3 = Car()
# c3.brand = "Bugatti"
# c3.model = "Super chiron"
# c3.price = 121923000
print(c3.show())  

print(Car.brand)

c4 = Car()
print(c4.show())

# Create a class Employee with properties(Firstname, lastname, department, salary) and methods (i. to display all the values, ii. to change the name and iii. to change the salary) 