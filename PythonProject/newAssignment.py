# 10 july 2025

# assignment 1 - Create a class called Car with attributes: brand, model, year and add a method display_info() to print the details

class Cars:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def printDisplayInfo(self):
        return self.brand, self.model, self.year

car1 = Cars("Tesla", "Model 3", "2020")
print(car1.printDisplayInfo())

# assignment 2 - Write a program that counts how many times each character appears in a given string using dictionary

s1 = "hello world"
# {'h':1, 'e':1, 'l':3...}
d = {}

for items in s1:
    if items in d:
        d[items] = d[items] + 1


    else:
        d[items] = 1

print(d)

for key, items in d.items():
    if items<2:
        print(key, end= '' )

print()

# assignment 3 - invert the keys and values for the given dictionary

d1 = {'a': 1, 'b': 2}
d2 = {}

for key, value in d1.items():
    d2[value] = key
    print(d2)

print(d2)


# assignment 4 - merge the two dictionaries into one. if the same key exists in both, sum their values

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
dict3 = {}

for key, value in dict1.items():
    if key in dict2:
        dict3[key] = dict1[key] + dict2[key]

    else:
        dict3[key] = value

print(dict3)

for key, value in dict2.items():
    if key not in dict3:
        dict3[key] = value

print(dict3)

# assignment 5 - from a class of student marks, find the student with the highest marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = [
    Student("Alice", 85),
    Student("John", 92),
    Student("David", 97)
]

highest_name = ""
highest_marks = 0

for items in students:
    if items.marks > highest_marks:
        highest_marks = items.marks
        highest_name = items.name

print(f"top student: {highest_name}, marks: {highest_marks}")


# assignment 6 - group words from a list into a dictionary by their length

words = ['hi', 'hello', 'hey', 'sun', 'python']
grouped = {}

for items in words:
    length = len(words)
    if length not in grouped:
        grouped[length] = []

    grouped[length].append(words)

for key, value in grouped.items():
    print("length {key}: {value}")


# assignment 7 - count how many times each digit appears in a given number.

d3 = {1122334455}
d4 = {}

# for key, value in d3.items():



