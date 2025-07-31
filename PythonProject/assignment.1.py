# 23rd june 2024


# assignment 1 - what is a set in python? how is it different from a list?
# a set in python is an unordered collection of items. they are different from lists as they cannot be changed and do not accept duplicate values

s = {1, 3, 5, 7, 3, 5}
print(s)

l1 = [1, 3, 5, 7, 3, 5]
print(l1)

# assignment 2 - remove number 2 from a set

s1 = {1, 3, 4, 2, 7}
s1.remove(2)
print(s1)

# assignment 4 - check if key "grade" exists in the dictionary

d1 = {
    "name": "alice",
    "age": 20,
    "city": "new york"
}

if "grade" in d1:
    print("grade is present")
else:
    print("grade is absent")


# assignment 5 - loop through the dictionary and print all keys and values

d2 = {"name": "alice", "age": 20, "city": "new york", "grade": 85}

for key, value in d2.items():
    print(key, value)

# assignment 6 - check if two sets have any elements in common

s2 = {1, 2, "a", 3, 4, 5, "b"}
s3 = {"a", "c", 4, "d", 5, 6}

s4 = s2.intersection(s3)
print(s4)


# assignment 7 -

s5 = set()

for items in range(1, 10):
    s5.add(items)

print(s5)

# assignment 8 -

d3 = {}

for items in range(1, 6):
    d3[items] = items*items

print(d3)

# assignment 9-

d4 = {'a': 10, 'b': 35, 'c': 20, 'd': 25, 'e': 30}
max = 0
result = ""
for key, value in d4.items():
   if value > max:
       max = value
       result = key

print(result)
print(max)

