# Data Structures for Data Science
# Lists, Tuples, Sets, and Dictionaries

# Lists
# A list is an ordered collection of items that can be changed (mutable).

# football_players = ["Messi", 2, "Ronaldo", 3, "Neymar", 4, "Mbappe", True, False, (1, 2, 3), [4, 5, 6], {"name": "Paul"}]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g"]
numbers_plus_letters = [1,3,4] + ['a', 'b', 'c']
print(["*"] * 10)
print(numbers_plus_letters)
# print(len(football_players))
print(len(number))
print(len(letters))

# Printing index in a list
print(number[0])
print(number[1])
print(letters[0])
print(letters[5])
print(letters[-1])
print(number[-1])
print(number[-2])

# Changing values in a list
number[0] = 10
number[1] = 90
number[2] = 100
print(number)

letters[2] = "x"
letters[3] = "y"    
letters[-3] = "z"
print(letters)

# Adding items to a list
number.append(10)
number.append(11)
number.append(12)
print(number)

# Assignment

# Create a list of 5 of your favorite foods
# Perform the following operations on the list:
# 1. Print the length of the list
# 2. Change the first and last item in the list to a different food
# 3. Add a new food item to the end of the list
# 4. Print the updated list
