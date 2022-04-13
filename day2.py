# list - a built-in datatype to store the collection of data. It is ordered, mutable and indexed.
ls = [1, 2, 3, 4]
students = ["Sagar", "Nitin", "Rachit", "Shivam"]
boolean_list = [True, False, False, False, True]
mixedtypelist = [1, 2, 3, "String1", "Haaris", True, False]
# print(ls)
# print(students)
# print(boolean_list)
# print(mixedtypelist)

# To get any specific value out of the list, we use indexes of the value.
# print(ls[1])
# print(students[3])
# print(mixedtypelist[5])

mixedtypelist[3] = "Another value"
# print(mixedtypelist)


# List Functions
# mystr = "This is a mobile"
# print(mystr[3])
# len() - return the number of values in the list 
# print("No. of values in the list :", len(students))
# print(mixedtypelist[2+2])

# Printing the last index of the list
# print(boolean_list[len(boolean_list) - 1])

# Adding into the list
fruits = ['Apple', 'Banana', 'Orange', 'Kiwi']
# fruits.append('Watermelon')
# fruit = 'Tangerine'
# fruits.insert(2, 'Litchi')
# fruits.insert(4, fruit)

vegetables = ['Carrot', 'Redish', 'Gourd']
fruits.extend(vegetables)

# Removing from the list
fruits.pop(4)
students2 = ["Hitesh", "Akash", "Akanksha", "Vihan", "Rihan",  "Akanksha"]
# students2.remove("Akanksha")
# fruits.clear()
# del(fruits)
# print(fruits)

friends = students2
print(friends)

friends.clear()
print(students2)
print(friends)

alphabets = ["e", "a", "b", "d",  "c", "z", "f", "g", "s"]
# print(alphabets)
# alphabets.sort()
# print(alphabets)

# students2.sort()
# print(students2)

ls = [1, 2, 3, 6, 2, 7, 5, 9, 4, 7, 8, 4, 6, 8, 4, 6, 3, 7, 3, 1, 4, 2, 6]
# print("No. of times :", students2.count("Akanksha"))
# print("No. of times :", ls.count(6))
# print("Index of 6 :", ls.index(6))
# print("Index of 6 :", ls.index(6, 4))
# print("Index of 6 :", ls.index(6, 4, 11))
# ls.sort(reverse=True)
# print(ls)
# ls.reverse()
# print(ls)


