# -------------------------------------------
# Exercise 0: Introduction to Functions
# -------------------------------------------
# In this exercise, we'll learn about Python functions together as a class.
#
# Functions are reusable blocks of code that:
# - Help us avoid repeating code
# - Make our programmes more organised
# - Can take inputs (parameters) and give outputs (return values)
#
# We'll work through each task together, step by step.
# -------------------------------------------

# -------------------------------------------
# Task 1: Simple Greeting Function
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 1: Simple Greeting Function\n"
      + "-------------------------------------------")

# Let's create a function called greet() that prints "Hello, World!"
# 
# Steps:
# 1. Use 'def' to define the function
# 2. Give it the name 'greet'
# 3. Add empty parentheses ()
# 4. Add a colon :
# 5. Indent the next line and add: print("Hello, World!")
#
# Then call the function by writing: greet()
#
# Write your code below:
def greet():
      print("Hello, world!")

greet()

# -------------------------------------------
# Task 2: Greeting with a Name
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 2: Greeting with a Name\n"
      + "-------------------------------------------")

# Now let's create a function called greet_person() that takes a parameter.
#
# The function should:
# - Have one parameter called 'name'
# - Print "Hello, [name]!" using an f-string
#
# Then call it twice:
# - greet_person("Alice")
# - greet_person("Bob")
#
# Example output:
# Hello, Alice!
# Hello, Bob!
#
# Write your code below:
def greet(name):
      print(f"Hello, {name}")

greet("hayat")
greet("Luay")

# -------------------------------------------
# Task 3: Adding Two Numbers
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 3: Adding Two Numbers\n"
      + "-------------------------------------------")

# Create a function called add_numbers() that:
# - Takes two parameters: num1 and num2
# - Returns the sum of num1 and num2 (use 'return')
#
# Then use the function:
# - Call add_numbers(5, 3) and store the result in a variable called result
# - Print the result
#
# Example output:
# 8
#
# Write your code below:
def add_numbers(num1, num2):
      return (num1+num2)

result = add_numbers(5, 3)
print(result)


# -------------------------------------------
# Task 4: Calculate Age
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 4: Calculate Age\n"
      + "-------------------------------------------")

# Create a function called calculate_age() that:
# - Takes one parameter: birth_year
# - Returns the age by subtracting birth_year from 2025
#
# Then use the function:
# - Call calculate_age(2000) and store it in a variable called age
# - Print: "You are [age] years old"
#
# Example output:
# You are 25 years old
#
# Write your code below:
def calculate_age(birth_year):
      return 2025-birth_year

age = calculate_age(2000)
print(f"you are {age} years old")


# -------------------------------------------
# Task 5: Check if Even
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 5: Check if Even\n"
      + "-------------------------------------------")

# Create a function called is_even() that:
# - Takes one parameter: number
# - Returns True if the number is even, False if odd
# - Hint: Use number % 2 == 0
#
# Then test it:
# - Call is_even(10) and print the result
# - Call is_even(7) and print the result
#
# Example output:
# True
# False
#
# Write your code below:
def is_even(number):
      return True if number % 2 == 0 else False

result = is_even(10)
print(result)

result = is_even(7)
print(result)
# -------------------------------------------
# Task 6: Price with Tax
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 6: Price with Tax\n"
      + "-------------------------------------------")

# Create a function called add_tax() that:
# - Takes one parameter: price
# - Calculates price + 20% tax (multiply price by 1.20)
# - Returns the total rounded to 2 decimal places
# - Hint: Use round(total, 2)
#
# Then use it:
# - Call add_tax(10.00) and store in a variable called final_price
# - Print: "Final price: £[final_price]"
#
# Example output:
# Final price: £12.0
#
# Write your code below:
def add_tax(price):
      return price*1.20 
      return round(total, 2)

final_price = add_tax(10.00)
print(f"Final price: £{final_price}")
# -------------------------------------------
# Task 7: Find Maximum
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 7: Find Maximum\n"
      + "-------------------------------------------")

# Create a function called find_max() that:
# - Takes two parameters: a and b
# - Returns the larger of the two numbers
# - Hint: Use an if/else statement
#
# Then test it:
# - Call find_max(15, 23) and print the result
# - Call find_max(100, 50) and print the result
#
# Example output:
# 23
# 100
#
# Write your code below:
def find_max(a, b):
      return a if a>b else b

result = find_max(15, 23)
print(result)

result = find_max(100, 50)
print(result)
# -------------------------------------------
# Task 8: Repeat Message
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 8: Repeat Message\n"
      + "-------------------------------------------")

# Create a function called repeat_message() that:
# - Takes two parameters: message and times
# - Uses a for loop to print the message that many times
# - Doesn't return anything (just prints)
#
# Then call it:
# - repeat_message("Python is fun!", 3)
#
# Example output:
# Python is fun!
# Python is fun!
# Python is fun!
#
# Write your code below:
def repeat_message(message, times):
      for i in range(times):
            print(f"{message}")

repeat_message("Python is fun!", 3)

# -------------------------------------------
# Well Done!
# -------------------------------------------
# You've learnt the basics of Python functions:
# - How to define a function (def)
# - How to add parameters
# - How to return values
# - How to call functions
#
# Functions make your code reusable and organised!
# -------------------------------------------
