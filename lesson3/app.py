# Functions
# A function is a reusable block of code that performs a specific task.
# A function can return a value or print a value.

# Defining a function

# def name_of_function(optional_variable):
#   # Do something in the function

# def greet():
#     print("Good evening sir!")

# greet()
# greet()
# greet()

# def greet(name):
#     print(f"Good morning {name}")


# greet("Paul")
# greet("Anabel")

# def add(a, b):
#     return a+b


# print(add(4, 5))

# Default Arguments in functions

def multiply(num1, num2=4):
    return num1 * num2


# print(multiply(3, 5))

# *args and **kwargs in python


def add_numbers(numbers):
    print(numbers)
    total = 0

    for number in numbers:
        total = total + number

    return total


# Useful functions for data science beginners

def mean(*numbers):
    """Calculate the mean of a list of numbers."""
    return add_numbers(numbers) / len(numbers)


# print(mean(1, 2, 3, 4, 5, 6, 7))


# **kwargs

# def student(**data):
#     print(data)


# student(name="Paul", age=30, height="9cm", income=100000, state="Delta")

# Assignment

# Write a function that can add range(10) and return the value

def add_ranges(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


print(add_ranges(range(100)))
print(add_ranges(range(50)))
print(add_ranges(range(100)))
