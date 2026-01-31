"""
========================================================================
Python Operators Demo — Interactive Version (Operators.py)
========================================================================

This file demonstrates all types of Python operators interactively.
Each section contains:
- Notes explaining the operator type
- Examples using user input
- Explanations for every line

Operators Covered:
1. Arithmetic
2. Comparison
3. Logical
4. Assignment
5. Membership
6. Identity
7. Bitwise

Author: Aaisha's Learning Repo
========================================================================
"""

# ===============================================================
# 1️⃣ USER INPUT
# ===============================================================

print("Welcome to Python Operators Interactive Demo!\n")

# Ask the user for two numbers to test arithmetic and comparison operators
num1 = int(input("Enter first number (num1): "))  
num2 = int(input("Enter second number (num2): "))

# Ask the user to input a list for membership operator tests
sequence = [item.strip() for item in input(
    "Enter a list of items separated by commas: ").split(',')]
# strip() removes spaces; split(',') splits input into list elements
item_to_check = input(
    "Enter an item to check if it exists in the list: ").strip()  

# Logical operator inputs
print("\nLogical Operators Test (True/False)")
p_input = input("Enter True or False for p: ")  
q_input = input("Enter True or False for q: ")  
# Convert string inputs to actual boolean values
p = True if p_input.lower() == 'true' else False
q = True if q_input.lower() == 'true' else False

# Identity operator inputs: two lists
list1 = input("Enter first list for identity test (comma separated): ").split(',')
list2 = input("Enter second list for identity test (comma separated): ").split(',')

# Separator for clarity
print("\n=================================================================")
print("Results:")

# ===============================================================
# 2️⃣ ARITHMETIC OPERATORS
# ===============================================================
"""
Arithmetic operators perform mathematical calculations on numbers.

+  Addition
-  Subtraction
*  Multiplication
/  Division (float division)
/  Floor division (integer division)
%  Modulus (remainder)
** Exponentiation (power)
"""

print("\n1. Arithmetic Operators:")
print(f"{num1} + {num2} =", num1 + num2)  # Addition
print(f"{num1} - {num2} =", num1 - num2)  # Subtraction
print(f"{num1} * {num2} =", num1 * num2)  # Multiplication
print(f"{num1} / {num2} =", num1 / num2 if num2 != 0 else "Cannot divide by zero")  # Float division
print(f"{num1} // {num2} =", num1 // num2 if num2 != 0 else "Cannot floor-divide by zero")  # Floor division
print(f"{num1} % {num2} =", num1 % num2 if num2 != 0 else "Cannot modulo by zero")  # Remainder
print(f"{num1} ** {num2} =", num1 ** num2)  # Exponentiation

# ===============================================================
# 3️⃣ COMPARISON OPERATORS
# ===============================================================
"""
Comparison operators compare values and return a boolean result (True/False).

==  Equal
!=  Not equal
>   Greater than
<   Less than
>=  Greater than or equal
<=  Less than or equal
"""

print("\n2. Comparison Operators:")
print(f"{num1} == {num2} :", num1 == num2)
print(f"{num1} != {num2} :", num1 != num2)
print(f"{num1} > {num2} :", num1 > num2)
print(f"{num1} < {num2} :", num1 < num2)
print(f"{num1} >= {num2} :", num1 >= num2)
print(f"{num1} <= {num2} :", num1 <= num2)

# ===============================================================
# 4️⃣ LOGICAL OPERATORS
# ===============================================================
"""
Logical operators combine boolean values:

and  → True if both operands are True
or   → True if at least one operand is True
not  → Reverses the boolean value
"""

print("\n3. Logical Operators:")
print(f"{p} and {q} :", p and q)
print(f"{p} or {q} :", p or q)
print(f"not {p} :", not p)

# ===============================================================
# 5️⃣ ASSIGNMENT OPERATORS
# ===============================================================
"""
Assignment operators combine a basic operation with assignment:

=   Assign value
+=  Add and assign
-=  Subtract and assign
*=  Multiply and assign
/=  Divide and assign
//= Floor divide and assign
%=  Modulus and assign
**= Exponentiation and assign
"""

print("\n4. Assignment Operators:")
temp = num1
print("Initial value:", temp)

temp += num2
print("After += :", temp)
temp -= num2
print("After -= :", temp)
temp *= num2
print("After *= :", temp)
temp /= num2 if num2 != 0 else 1
print("After /= :", temp)
temp //= num2 if num2 != 0 else 1
print("After //= :", temp)
temp %= num2 if num2 != 0 else 1
print("After %= :", temp)
temp **= 2
print("After **= :", temp)

# ===============================================================
# 6️⃣ MEMBERSHIP OPERATORS
# ===============================================================
"""
Membership operators check if a value exists in a sequence (list, string, tuple, etc.)

in      → True if value exists
not in  → True if value does not exist
"""

print("\n5. Membership Operators:")
print("List:", sequence)
print(f"'{item_to_check}' in list:", item_to_check in sequence)
print(f"'{item_to_check}' not in list:", item_to_check not in sequence)

# ===============================================================
# 7️⃣ IDENTITY OPERATORS
# ===============================================================
"""
Identity operators check if two objects occupy the same memory location.

is      → True if both objects are the same in memory
is not  → True if both objects are different in memory
"""

print("\n6. Identity Operators:")
print("List1:", list1)
print("List2:", list2)
print("list1 == list2 :", list1 == list2)  # Content equality
print("list1 is list2 :", list1 is list2)  # Memory identity
print("list1 != list2 :", list1 != list2)

# ===============================================================
# 8️⃣ BITWISE OPERATORS
# ===============================================================
"""
Bitwise operators work on binary representations of integers:

&   → AND
|   → OR
^   → XOR
~   → NOT
<<  → Left shift (multiply by 2^n)
>>  → Right shift (divide by 2^n)
"""

print("\n7. Bitwise Operators (integers only):")
print(f"{num1} & {num2} :", num1 & num2)
print(f"{num1} | {num2} :", num1 | num2)
print(f"{num1} ^ {num2} :", num1 ^ num2)
print(f"~{num1} :", ~num1)
print(f"{num1} << 1 :", num1 << 1)
print(f"{num1} >> 1 :", num1 >> 1)

# ===============================================================
# END OF OPERATORS DEMO
# ===============================================================
print("\n===== End of Python Operators Demo =====")
print("Thank you for using the Python Operators Interactive Demo!")
print("Run this file multiple times with different inputs to practice.")
