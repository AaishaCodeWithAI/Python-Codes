# ================================
# Beginner Program: Personal Information
# ================================

# Collect user information
name = input("Enter your name: ")  # User enters their name
print("Hello, my name is " + name)  # Print using concatenation

age = int(input("Enter your age: "))  # Convert input to integer
print("I am " + str(age) + " years old.")  # Convert age back to string for printing

city = input("Enter your city: ")  # User enters city
print("I live in " + city + ".")

country = input("Enter your country: ")  # User enters country
print("I am from " + country + ".")

hobby = input("Enter your hobby: ")  # User enters hobby
print("My hobby is " + hobby + ".")

# This program collects basic personal information and prints it in a formatted way.

# Check data types of variables
print("\nData Types of the entered information:")
print("Name type:", type(name))  # str
print("Age type:", type(age))    # int

