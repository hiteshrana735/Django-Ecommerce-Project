dict = {'name': "Ankit",
        "class": 12,
        "Favourite_game": "Red dead Redemption"
        }
# print(dict)
# print(dict["name"], dict['class'], dict["Favourite_game"])
dict["Favourite_game"] = "COD Warzone"
# print(dict)

# DICT - Mutable, Ordered and does not allow the duplicate keys
# Create a dictionary EMPLOYEE, store his first name(String), last name(String), Salary(Number) and attendance(Boolean)
employee = {
    'firstname': "Zain",
    'lastname': "Khan",
    'salary': 23541,
    'present': True,
    'firstname2' : "Mahir",
}

# print(employee["firstname"])
# print(employee["lastname"])
# print(employee["salary"])
# print(employee["present"])
# print(employee["firstname2"])

# Dictionary functions
# print(employee.items())
# print(employee.keys())
# employee['department'] = "IT"
# print(employee)

car = {
    'brand' : 'Ford', 
    'model' : 'GT-40', 
    'Price' : 'Priceless', 
}
# print(car)
car['built'] = 1940
# print(car['built'])
dict2 = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
}
car.update(dict2)
# car.pop('key1')
# car.clear()
# del(car)
# print(car)
# print(car['brand'])
# print(car.keys())
# print(car.values())
# print(car.items())
# print(car.get())

# dictionary => Collection of items => Item =>a pair of key and value
numdict = {
    1 : 'Shubh', 
    2 : 'Preet',
}
print(numdict[2])

# Collection type datatype -> 
# List -> []
# Dictionary -> {}
# Tuple -> ()
# Set -> {}

tp = (1, 2, 3, 4, 3, 2, 5, 6, 4, 5, 4, 8, 4, 9, 4)
# print(tp, type(tp))
# print(tp[0])
# tp[1] = 12

# print(tp.count(2))
# print(tp.index(4))

# set - Collection type datatype, unordered, immutable, doesn't allow duplicate values
st = {1, 3, 5, "string1", 1, 3, 5, "string1"}
print(st)
print(st[0])
st[0] = "anotherstring"