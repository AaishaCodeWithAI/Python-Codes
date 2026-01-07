# ================================
# String Formatting Examples
# Concatenation, format(), f-strings
# ================================

# Variables
first_name = "Alicia"
last_name = "Jha"
age = 20
marks = 87

# 1️⃣ String Concatenation
print("=== Concatenation ===")
full_name = first_name + " " + last_name
# Need to convert non-strings (like age) to string using str()
message_concat = "My name is " + full_name + " and I am " + str(age) + " years old."  
print(message_concat)

# 2️⃣ Using format()
print("\n=== format() Method ===")
# Positional placeholders
message_format = "My name is {} {} and I am {} years old.".format(first_name, last_name, age)
print(message_format)

# Named placeholders
message_format_named = "Student {n} scored {m} marks.".format(n=first_name, m=marks)
print(message_format_named)

# 3️⃣ f-Strings (Recommended)
print("\n=== f-Strings ===")
# Insert variables directly inside {} for readability and simplicity
message_fstring = f"My name is {first_name} {last_name} and I am {age} years old."
print(message_fstring)

# Using expressions inside f-strings
print(f"Example calculation inside f-string: 10 + 5 = {10 + 5}")
print(f"Student {first_name} scored {marks} marks and passed the exam.")

# Notes:
# message_concat, message_format, message_format_named, and message_fstring
# all store the combined strings for different string formatting methods

