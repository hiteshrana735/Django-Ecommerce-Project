class Car:
    brand = "Volkswagen"
    model = "Polo"
    price = 1923000

    def show(self):
        return f"Details of the car :\nBrand name: {self.brand}\nModel name: {self.model}\nPrice: {self.price}"
# Instance 
# Inheritance 

class A(Car):
    brand = "Bugatti"
    def intro(self):
        print(f"Values are as follows: \nBrand: {self.brand}")

class B(A):
    pass

# obj = A()
# obj.intro()

# obj2 = B()
# print(obj2.brand)

class Phone:
    def __init__(s, brand, model, price):
        s.brandname = brand
        s.modelname = model
        s.price = price

P1 = Phone("Mi", "11i", 27000)
print(P1.brandname, P1.modelname, P1.price)

p2 = Phone("OnePlus", "Nord CE2", 24000)
print(p2.price)

p3 = Phone("Nokia", "2690", 132000)
print(p3.modelname)

class SmartPhone(Phone):
    def showOldValues(s):
        super().__init__("Mi", "Model", 12300)
        return f"Older Details:\nBrand: {s.brandname}\nModel: {s.modelname}\nPrice: {s.price}"

    def __init__(self, cam, proc):
        self.camera = cam
        self.processor = proc

mi = SmartPhone("48MP", "SD778")
mi.showOldValues()




# Polymorphism - 
class C1:
    def fn1(s):
        print("I am the fn1 function of C1 class")

class C2(C1):
    def fn1(s):
        print("I am the fn1 function of C2 class")


c1obj = C1()
c1obj.fn1()

c2obj = C2()
c2obj.fn1()

# Class shape -> function for calculating area
# shape --> circle --> 
# shape --> square -->

class Shape:
    def calcArea(s):
        print("Hello There")

class Circle(Shape):
    def calcArea(s, r):
        s.radius = r 
        return 3.14 * s.radius * s.radius 

class Square(Shape):
    def calcArea(s, side):
        s.side = side
        return s.side * s.side

c1 = Circle()
print(c1.calcArea(3))
sq1 = Square()
print(sq1.calcArea(3))

sp = Shape()
sp.calcArea()