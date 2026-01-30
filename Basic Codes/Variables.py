# Variables store data in a program
# Variables have names and hold values (data) of different types
print("--------Variable Types in Python:----------")
print()

# Numeric Variables
print("1.---Numeric Variables:---")
print()

print("Integer Variable and Float Variable")
print() 

age = 20                   # Integer: whole number
print("Age:", age)

height = 5.6               # Float: decimal number
print("Height:", height)
print() 

# Example of the division operator in all the earlier versions of Python 3:
print("Division Example:")
print ("The result of 5/2 for Python 3 is:", 5/2)  # Results in 2 for versions before Python 3.0, but it was later modified to always return 2.5 in Python 3.x
print ("If it were Python 2 or any earlier version of python before python 3, the result of 5/2 would be:", 5//2, ", which was mathmatical and logically, a mistake that's why, in python 3, it was modified.")  # Integer division in Python 2
print()

# String Variable
print("2.---String Variable:---")
name = "Alex"      # String: text
print("Name:", name) 
print()

#Since a string is indexed, we can access individual characters using their index positions.
print("Accessing characters in the string through slicing to get substring and using index:")
print() 
print("First character of name:", name[0])  # 'A'
first_letter = name[0]  # 'A' - Accessing first character using index

# Slicing a string to get a substring
print("First two letters of name:", name[0:2])  # 'Al'
letter = name[0:2]  # 'Al' - Slicing from index 0 to 2 (not inclusive of 2)

# Slicing with step value
print("Slicing with step value:", name[0:3:2])  # 'Ae'  - Slicing from index 0 to 4 with a step of 2
print() 

# List Variable
print("3. ---List Variable:---")
fruits = ["apple", "banana", "cherry"]  # List: ordered collection
print("Fruits:", fruits)
print()

# Accessing elements in a list
first_fruit = fruits[0]  # 'apple'
print("Accessing first fruit from list:")
print("First Fruit:", first_fruit)
print() 

# Tuple Variable
print("4.---Tuple Variable:---")
coordinates = (10, 20)  # Tuple: ordered, immutable collection
print("Coordinates:", coordinates)  
print()

# Accessing elements in a tuple
print("Accessing tuple of coordinates:")
x = coordinates[0]  # 10
y = coordinates[1]  # 20
print("X:", x, "Y:", y)
print()

# Dictionary Variable
print("5.---Dictionary Variable:---")
person = {"name": "John", "age": 30}  # Dictionary: key-value pairs
print("Person:", person)
print()

# Accessing values in a dictionary
print("Accessing values in a dictionary:")
person_name = person["name"]  # 'John'
person_age = person["age"]    # 30
print("Person Name:", person_name , "Person Age:", person_age)
print()

# Boolean Variable
print("6.---Boolean Variable:---")
is_student = True  # Boolean: True or False
print("Is Student:", is_student)
print() 

# NoneType Variable
print("7.---NoneType Variable:---")
data = None  # NoneType: represents the absence of a value
print("Data:", data)    
print() 
# Checking variable types
print("--------Checking Variable Types:----------")
print("Type of age:", type(age))               # <class 'int'>
print("Type of height:", type(height))         # <class 'float'>
print("Type of name:", type(name))             # <class 'str'>  
print("Type of fruits:", type(fruits))         # <class 'list'>
print("Type of coordinates:", type(coordinates)) # <class 'tuple'>
print("Type of person:", type(person))         # <class 'dict'>
print("Type of is_student:", type(is_student)) # <class 'bool'>
print("Type of data:", type(data))             # <class 'NoneType'>
# This program demonstrates different variable types in Python
