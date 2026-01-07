# Taking input from the user
# input() lets the user type data, which is stored in a variable

name = input("Enter your name: ")  # User enters their name (string)
age = input("Enter your age: ")    # User enters their age (string)

# Print the input as strings
print("Hello", name)
print("You are", age, "years old")

# Convert age from string to integer
age_int = int(age)  # int() converts the string to a number
# Now age_int is an integer, so we can do math with it

# Example: calculate age next year
print("Next year, you will be", age_int + 1, "years old")
