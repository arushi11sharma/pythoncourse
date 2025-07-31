# assignment 1 - print even and odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

for item in numbers:
    if item %2 == 0:
        print(item, "is even")
    else:
        print(item, "is odd")

# assignment 2 - find the largest number in a list

l1 = [5, 10, -150, 25, 30, 15, 40]
largest = l1[0]

for item in l1:
    if item > largest:
        largest = item

print("largest number in the list:", largest)

# assignment 3 - count even numbers in a list

l2 = [12, 22, 43, 27, 36, 4, 7, 9]
count = 0
odd_numbers = 0

for num in l2:
    if num % 2 == 0:
        count = count + 1
    else:
        odd_numbers = odd_numbers + 1

print("even numbers:", count)

print("odd numbers:", odd_numbers)


# assignment 4 - sum of numbers in a list

l3 = [5, 10, 15, 20, 25, 30]
total = 0

for item in l3:
    total = total + item

print("the sum is", total)


# assignment 5 - calculate area of square and area of rectangle

# area of square
a = 5
area = a*a
print("area of a square is", area)

# area of a rectangle

l = 2.2
b = 4
area =  l*b
print("area of a rectangle is", area)

# assignment 6 - remove 'green' from list

colours = ["red", "green", "blue"]
colours.remove("green")
print(colours)

# assignment 7 - check if 'Alice' is present

names = ["john", "jerry", "elaine", "george", "alice", "kat"]

if "alice" in names:
    print("alice is here")
else:
    print("alice is not found")

# assignment 8 - add item to a specific index in a list

l4 = [1, 2, 3, 4, 5, 6, 7, 8]

print(l4)
print(l4[3])
l4[3] = "hey"
l4.insert(1, "hello")
print(l4)

# assignment 9 - print squares of all numbers in a list and store in a new list

l5 = [1, 2, 3, 4, 5]
empty_list = []

for item in l5:
    sqr = item*item
    empty_list.append(sqr)

print(empty_list)

# assignment 10 - find the second largest number in a list

l6 = [2, 6, 3, 9, 22, 58, 76, 10]
largest = l6[0]
second_largest = l6[0]

for item in l6:
    if item > largest:
        second_largest = largest
        largest = item

print("the largest number in the list is:", largest)
print("the second largest number in the list is:", second_largest)





# assignment 11 - check if list is empty or not

l7 = []

if len(l7)== 0:
     print("the list is empty")
else:
    print("the list is not empty")


l8 = [2, 4, 5, 7, 11]
print(l8[::-1])




