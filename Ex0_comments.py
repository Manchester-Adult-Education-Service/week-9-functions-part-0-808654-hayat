# -------------------------------------------
# Exercise 0: Comments Practice
# -------------------------------------------
# In this exercise, you'll practice writing clear, helpful comments
# to explain Python code.
#
# Good comments should:
# - Explain WHAT the code does (not just repeat it)
# - Be clear and concise
# - Help someone else understand your code
#
# Below you'll find several code snippets.
# Add comments to explain what each section does.
# -------------------------------------------

# -------------------------------------------
# Task 1: Shopping Cart
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 1: Shopping Cart\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#creating a list called cart 
cart = ["apple", "bread", "milk", "eggs"]
#total_items is a variable about the number of items in the list 
total_items = len(cart) 
#printing a message showimg the total item in the list 
print(f"You have {total_items} items in your cart")
#using for loop to output each item in the list
for item in cart:
    print(f"- {item}")

# -------------------------------------------
# Task 2: Grade Calculator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 2: Grade Calculator\n"
      + "-------------------------------------------")

# Add comments to explain this code:

#creating a variable called score where the user entre the test score
#the variable is an integer, don`t forget to use int
#checking the grade using if, else block
#printing the grade
score = int(input("Enter your test score: "))

if score >= 70:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Your grade: {grade}")

# -------------------------------------------
# Task 3: Password Validator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 3: Password Validator\n"
      + "-------------------------------------------")

# Add comments to explain this code:

password = input("Create a password: ")    #ask the user to enter a password

is_long = len(password) >= 8               #checking that the password lengh is greater or equal to 8 
has_upper = password != password.lower()   #checking if the password contain an upper case
has_lower = password != password.upper()   #checking if the password contain a lower case

is_valid = is_long and has_upper and has_lower      #password validation

if is_valid:                                        #checking password validation 
    print("Password accepted!")                     #print "Password accepted" if is valid
else:
    print("Password rejected. Must be 8+ characters with upper and lowercase letters.")    #output "Password rejected" if is not valid 

# -------------------------------------------
# Task 4: Even Number Counter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 4: Even Number Counter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

numbers = [12, 7, 18, 5, 22, 9, 14]                           #creat a list of integer
even_count = 0                                                #counting the even numbers

for num in numbers:                                           #looping throught the list
    if num % 2 == 0:                                          #check if a number in the list is even
        even_count = even_count + 1                            

print(f"There are {even_count} even numbers in the list")     #output the total even number in the list

# -------------------------------------------
# Task 5: Student Records
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 5: Student Records\n"
      + "-------------------------------------------")

# Add comments to explain this code:

#creat a dictionary named student contain name, age, grades
#calculate the average grade by deviding the sum grades by the lengh of the grades
#round the average to 2 dicimals
student = {                
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78, 88]
}

average = sum(student["grades"]) / len(student["grades"])
average = round(average, 2)

print(f"Student: {student['name']}")
print(f"Age: {student['age']}")
print(f"Average grade: {average}")

# -------------------------------------------
# Task 6: Countdown Timer
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 6: Countdown Timer\n"
      + "-------------------------------------------")

# Add comments to explain this code:

countdown = 5

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Blast off!")

# -------------------------------------------
# Task 7: Menu Formatter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 7: Menu Formatter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

menu_items = ["burger", "pizza", "salad", "pasta"]
counter = 1

for item in menu_items:
    formatted_item = item.upper()
    print(f"{counter}. {formatted_item}")
    counter = counter + 1

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you've added comments to all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
