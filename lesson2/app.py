
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


saved_login = 1234

# Input is always a string in Python
user_input_as_str = input("Enter your login: ")
# Convert the string input to an integer
user_input_as_int = int(user_input_as_str)

if user_input_as_int == saved_login:
    print("Login successful")
else:
    print("Login failed, please try again")
