
# Comparism Operators
# Comparism operators are used to compare two values and return a boolean result (True or False)
# a = 10
# b = 20
# print(a == b)  # False
# print(a != b)  # True
# print(a > b)  # False
# print(a < b)  # True
# print(a >= b)  # False
# print(a <= b)  # True

# Control Flow in Python
# Control flow statements allow you to execute certain blocks of code based on conditions
# if-else statements
# a = 10
# b = 20

# if a < b:
#     print("a is less than b")
# else:
#     print("a is not less than b")

# if a > b:
#     print("a is greater than b")
# else:
#     print("a is not greater than b")

# if a == b:
#     print("a is equal to b")
# else:
#     print("a is not equal to b")

# age_from_user = int(input("Enter your age: "))

# entry_age = 18

# # if-elif-else statements
# if age_from_user < entry_age:
#     print("Your age is below the entry age")
# elif age_from_user == entry_age:
#     print("You are just allowed to enter")
# else:
#     print("Your age is above the entry age")


# Logical Operators
# Logical operators are used to combine conditional statements
# print(a == 10 and b == 20)  # True
# print(a == 10 or b == 30)  # True
# print(not (a == 10))  # False
# Identity Operators


# saved_login = 1234

# # Input is always a string in Python
# user_input_as_str = input("Enter your login: ")
# # Convert the string input to an integer
# user_input_as_int = int(user_input_as_str)

# if user_input_as_int == saved_login:
#     print("Login successful")
# else:
#     print("Login failed, please try again")

# input_age = int(input("Enter your age: "))
# input_gender = input("Enter your gender 'M' for male and 'F' for female")

# if input_age < 18 and input_gender == "F":
#     print("Give her Teddy bear")
# elif input_age < 18 and input_gender == "M":
#     print("Give him toy car")
# elif input_age >= 18 and input_age < 30 and input_gender == "F":
#     print("Give her makeup kit")
# elif input_age >= 18 and input_age < 30 and input_gender == "M":
#     print("Give him a rolex watch")
# elif input_age >= 30 and input_age < 50 and input_gender == "F":
#     print("Give her a diamond necklace")
# elif 30 >= input_age < 50 and input_gender == "M":
#     print("Give him a luxury car")
# else:
#     print("Give them a gift card")

# room_temperature = 25  # Example room temperature in Celsius

# if room_temperature >= 25:
#     print("Turn on the Air conditioner")
# elif room_temperature < 25:
#     print("Turn on the heater")
# else:
#     print("Room temperature is okay, no action needed")

# print(True and False)  # False
# print(True or False)  # True
# print(not True)  # False
# print(not False)  # True
# print(not True and True)  # False
# print(not True or False)  # True #False
# print(not (True or False))  # False
# print(not (True and False))  # False #True

# # Loops in Python (for and while loops)

from time import sleep
numbers_0_to_5 = range(5)  # Generates numbers from 0 to 9

# for variable in iterable:

# Using a for loop to iterate through the numbers
# for number in [0, 1, 2, 3, 4, 5]:
#     print(number)  # Prints each number from 0 to 9

# greeeting = "Hello World"

# for char in greeeting:
#     print(char)  # Prints each character in the string "Hello World"

# # Getting even numbers from 0 to 20 using a for loop
# numbers_1_to_20 = range(1, 21)  # Generates numbers from 0 to 20

# for number in numbers_1_to_20:
#     if number % 2 == 0:  # Check if the number is even
#         print(number)  # Prints the even number

# numbers_0_to_5 = list(range(5))  # Generates numbers from 0 to 4
# print(numbers_0_to_5)  # Prints the list of numbers from 0 to 4

# for number in ["7", 9, 8]:  # Generates numbers from 0 to 4
#     print(number)  # Prints each number from 4 to 4
#     sleep(3)  # Pauses the execution for 1 second


# Assignment

# Loop over the number "Python Programming" and print out only the "p"s

# message = "Python programming"

# for char in message:
#     if char.lower() == "p":
#         print(char)

# While Loops
# number = 10

# while number > 0:
#     print(number)
#     number -= 1     # number = number - 1  # Decrement the number by 1

# Ask for user input until they enter 'quit'
# user_input = ""

# while user_input.lower() != "quit":
#     user_input = input("Enter a command (type 'quit' to exit): ")
#     print(f"You entered: {user_input}")


#  Infinite Loop

# while True:
#     user_input = input(
#         "Enter a number you want to output and 'exit' to exit: ")

#     if user_input.lower() == "exit":
#         print("Exiting the loop.")
#         break
#     print(f"You entered: {user_input}")

# Note: Be careful with infinite loops, they can cause your program to run indefinitely.
