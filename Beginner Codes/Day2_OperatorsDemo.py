# ===============================================
# Python Operators Demo – Interactive Version
# Covers: Arithmetic, Comparison, Logical,
# Assignment, Membership, Identity, Bitwise
# Beginner-friendly: every line explained
# ===============================================

# 1️⃣ User Input
print("Welcome to Python Operators Interactive Demo!\n")  # Greeting message

# Get two numbers from the user for arithmetic and other tests
num1 = int(input("Enter first number (num1): "))  # Convert input to integer
num2 = int(input("Enter second number (num2): ")) # Convert input to integer

# Membership input: create a list from user input
sequence = [item.strip() for item in input("Enter a list of items separated by commas: ").split(',')]
# split(',') splits input into list
item_to_check = input("Enter an item to check if it exists in the list: ").strip()  
# strip() removes extra spaces

# Logical input: ask user to enter True or False values
print("\nLogical Operators Test (True/False)")
p_input = input("Enter True or False for p: ")  
q_input = input("Enter True or False for q: ")  
# Convert string input to actual boolean values
p = True if p_input.lower() == 'true' else False
q = True if q_input.lower() == 'true' else False

# Identity input: two lists for identity operator tests
list1 = input("Enter first list for identity test (comma separated): ").split(',').strip()
list2 = input("Enter second list for identity test (comma separated): ").split(',').strip()

# Separator for results
print("\n==============================================")
print("Results:")

# 2️⃣ Arithmetic Operators
print("\n1. Arithmetic Operators:")
print(f"{num1} + {num2} =", num1 + num2)  # Addition
print(f"{num1} - {num2} =", num1 - num2)  # Subtraction
print(f"{num1} * {num2} =", num1 * num2)  # Multiplication
print(f"{num1} / {num2} =", num1 / num2 if num2 != 0 else "Cannot divide by zero")  # Division (float)
print(f"{num1} // {num2} =", num1 // num2 if num2 != 0 else "Cannot floor-divide by zero")  # Floor division
print(f"{num1} % {num2} =", num1 % num2 if num2 != 0 else "Cannot modulo by zero")  # Remainder
print(f"{num1} ** {num2} =", num1 ** num2)  # Exponentiation

# 3️⃣ Comparison Operators
print("\n2. Comparison Operators:")
print(f"{num1} == {num2} :", num1 == num2)  # Equal
print(f"{num1} != {num2} :", num1 != num2)  # Not equal
print(f"{num1} > {num2} :", num1 > num2)    # Greater than
print(f"{num1} < {num2} :", num1 < num2)    # Less than
print(f"{num1} >= {num2} :", num1 >= num2)  # Greater than or equal
print(f"{num1} <= {num2} :", num1 <= num2)  # Less than or equal

# 4️⃣ Logical Operators
print("\n3. Logical Operators:")
print(f"{p} and {q} :", p and q)  # AND: True if both True
print(f"{p} or {q} :", p or q)    # OR: True if any True
print(f"not {p} :", not p)        # NOT: True becomes False, False becomes True

# 5️⃣ Assignment Operators
print("\n4. Assignment Operators:")
temp = num1  # Initialize temp with num1
print("Initial value:", temp)
temp += num2  # Add num2 to temp
print("After += :", temp)
temp -= num2  # Subtract num2 from temp
print("After -= :", temp)
temp *= num2  # Multiply temp by num2
print("After *= :", temp)
temp /= num2 if num2 != 0 else 1  # Divide temp by num2 (float division)
print("After /= :", temp)
temp //= num2 if num2 != 0 else 1  # Floor division assignment
print("After //= :", temp)
temp %= num2 if num2 != 0 else 1  # Modulus assignment
print("After %= :", temp)
temp **= 2  # Exponent assignment (temp squared)
print("After **= :", temp)

# 6️⃣ Membership Operators
print("\n5. Membership Operators:")
print(f"List:", sequence)
print(f"'{item_to_check}' in list:", item_to_check in sequence)      # Check if item is in list
print(f"'{item_to_check}' not in list:", item_to_check not in sequence)  # Check if item is NOT in list

# 7️⃣ Identity Operators
print("\n6. Identity Operators:")
print(f"List1: {list1}")
print(f"List2: {list2}")
print("list1 == list2 :", list1 == list2)  # Are the lists equal in content
print("list1 != list2 :", list1 != list2)  # Are the lists not equal in content

# 8️⃣ Bitwise Operators
print("\n7. Bitwise Operators (integers only):")
print(f"{num1} & {num2} :", num1 & num2)  # AND
print(f"{num1} | {num2} :", num1 | num2)  # OR
print(f"{num1} ^ {num2} :", num1 ^ num2)  # XOR
print(f"~{num1} :", ~num1)                # NOT
print(f"{num1} << 1 :", num1 << 1)        # Left shift by 1 (multiply by 2)
print(f"{num1} >> 1 :", num1 >> 1)        # Right shift by 1 (divide by 2)

print("\n===== End of Operators Demo =====")
print("Thank you for using the Python Operators Interactive Demo!")
