import random

# Data Structures for Data Science
# Lists, Tuples, Sets, and Dictionaries

# Lists
# A list is an ordered collection of items that can be changed (mutable).

# football_players = ["Messi", 2, "Ronaldo", 3, "Neymar", 4, "Mbappe", True, False, (1, 2, 3), [4, 5, 6], {"name": "Paul"}]
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# letters = ["a", "b", "c", "d", "e", "f", "g"]
# numbers_plus_letters = [1,3,4] + ['a', 'b', 'c']
# print(["*"] * 10)
# print(numbers_plus_letters)
# # print(len(football_players))
# print(len(number))
# print(len(letters))

# Printing index in a list
# print(number[0])
# print(number[1])
# print(letters[0])
# print(letters[5])
# print(letters[-1])
# print(number[-1])
# print(number[-2])

# Changing values in a list
# number[0] = 10
# number[1] = 90
# number[2] = 100
# print(number)

# letters[2] = "x"
# letters[3] = "y"    
# letters[-3] = "z"
# print(letters)

# Adding items to a list
# number.append(10)
# number.append(11)
# number.append(12)
# print(number)

# Assignment

# Create a list of 5 of your favorite foods
# Perform the following operations on the list:
# 1. Print the length of the list
# 2. Change the first and last item in the list to a different food
# 3. Add a new food item to the end of the list
# 4. Print the updated list

# Removing items from a list

# number = [1, 8, 3, 2, 5, 6, 7, 9, 4]
# letters = ['a', 'e', 'd', 'b', 'g', 'c', 'f']

# number.pop()  
# print(number)
# number.pop(4)  
# print(number)
# del number[3:7]
# print(number)

# number_list = list(range(10))
# tuple_list = list((10, 50, 100, 150, 200))
# print(number_list)
# print(tuple_list)

# Sorting a list
# number.sort()
# print(number)
# letters.sort()
# print(letters)

# Unique Elements: Write a function that takes a list as input and returns a new 
# list containing a new list with unique elements from the original list and the input list.

# original_list = [1, 2, 2, 8, 9, 10]

# def new_list(input_list):
#     for item in input_list:
#         if item not in original_list:
#             original_list.append(item)
#     return original_list

# print(new_list([10, 20, 30]))


# Remove Duplicates In-Place: Write a function that removes all duplicate 
# elements from a list without creating a new list. 
# This means you should modify the original list directly. 
# The order of the remaining elements can be changed.

# original_list = [1, 2, 2, 8, 3, 9, 9, 4, 10, 10, 3, 5, 6, 7, 8]

# print(8 in original_list)
# print(20 in original_list)

# def remove_duplicates(input_list):
#     new_list = []
    
#     for item in input_list:
#         if item in new_list:
#             continue
#         new_list.append(item)

#     return new_list

# print(remove_duplicates(original_list))

# Tuples
# A tuple is an ordered collection of items that cannot be changed (immutable).

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# ((1,2,3), (4,5,6), (7,8,9))
# range_tuple = tuple(range(10))

# numbers[2] = 10  
# print(numbers)

# Assignment
# Given a tuple of numbers (10, 20, 30, 40, 50), 
# write a single line of code that creates a 
# new tuple containing the last three elements.

# numbers = (10, 20, 30, 40, 50)
# print(numbers[2:])

# Dictionaries

# A dictionary is an unordered collection of key-value pairs that can be changed (mutable).

# student = {"ada": 23, "ade": 25, "peter": 22, "Mike": 26, "John": 24, "Paul": 28, "Ruth": 27}
orders = {1: "Iphone", 2: "Television", 3: "Laptop", 4: "Tablet"}
# mixed = {"name": "John", 1: [1, 2, 3], "is_student": True, "courses": ("Math", "Science")}

# print(student)
# print(student["ada"])
# print(student["ade"])

# student["messi"] = 30
# print(student)

# keys(), values(), items()

# students_keys = student.keys()
# print(students_keys)

# students_values = student.values()
# print(students_values)

# students_items = student.items()
# print(students_items)

# get(), setdefault(), pop()

# order = orders.get(5, "Key Not Found")
# print(order)

orders.setdefault(6, "Smart Watch")
# print(orders)

# orders.pop(5, "Key Not Found")
# print(orders)

# Assignment 
# Find the most number of occourence in the word "Photosynthesis"

words = "Photosynthesis"
words_count = {}

# for letter in words:
#     letter = letter.lower()
#     if letter in words_count:
#         words_count[letter] = words_count[letter] + 1
#     else:
#         words_count[letter] = 1
#     print(words_count)

# for letter in words:
#     letter = letter.lower()
#     words_count[letter] = words_count.get(letter, 0)
#     words_count[letter] += 1


for letter in words:
    letter = letter.lower()
    words_count.setdefault(letter, 0)
    words_count[letter] += 1

words_count_values = list(words_count.items())
words_count_values.sort(key=lambda item: item[1], reverse=True)
first_value = list(words_count_values[0])
print(f"The letter '{first_value[0]}' occurs the most with a count of {first_value[1]} times.")




# student = {"ada": 23, "ade": 25, "peter": 22, "Mike": 26, "John": 24, "Paul": 28, "messi": 27}

student_values = list(student.items())
print(student_values)

def get_value(item):
    return item[1]

student_values.sort(key=get_value, reverse=True)
print(dict(student_values))