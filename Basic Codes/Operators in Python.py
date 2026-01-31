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
8. Operator Precedence & Associativity

Author: Aaisha's Learning Repo
========================================================================
"""

# ===============================================================
# 1️⃣ USER INPUT
# ===============================================================
print("Welcome to Python Operators Interactive Demo!\n")

num1 = int(input("Enter first number (num1): "))  
num2 = int(input("Enter second number (num2): "))

sequence = [item.strip() for item in input(
    "Enter a list of items separated by commas: ").split(',')]
item_to_check = input(
    "Enter an item to check if it exists in the list: ").strip()  

print("\nLogical Operators Test (True/False)")
p_input = input("Enter True or False for p: ")  
q_input = input("Enter True or False for q: ")  
p = True if p_input.lower() == 'true' else False
q = True if q_input.lower() == 'true' else False

list1 = input("Enter first list for identity test (comma separated): ").split(',')
list2 = input("Enter second list for identity test (comma separated): ").split(',')

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
%  Modulus (remainder)
** Exponentiation (power)
"""

print("\n1. Arithmetic Operators:")
print(f"{num1} + {num2} =", num1 + num2)
print(f"{num1} - {num2} =", num1 - num2)
print(f"{num1} * {num2} =", num1 * num2)
print(f"{num1} / {num2} =", num1 / num2 if num2 != 0 else "Cannot divide by zero")
print(f"{num1} // {num2} =", num1 // num2 if num2 != 0 else "Cannot floor-divide by zero")
print(f"{num1} % {num2} =", num1 % num2 if num2 != 0 else "Cannot modulo by zero")
print(f"{num1} ** {num2} =", num1 ** num2)

# ===============================================================
# 3️⃣ COMPARISON OPERATORS
# ===============================================================
"""
Comparison operators return True or False.

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
Assignment operators combine an operation with assignment:

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
temp += num2; print("After += :", temp)
temp -= num2; print("After -= :", temp)
temp *= num2; print("After *= :", temp)
temp /= num2 if num2 != 0 else 1; print("After /= :", temp)
temp //= num2 if num2 != 0 else 1; print("After //= :", temp)
temp %= num2 if num2 != 0 else 1; print("After %= :", temp)
temp **= 2; print("After **= :", temp)

# ===============================================================
# 6️⃣ MEMBERSHIP OPERATORS
# ===============================================================
"""
Membership operators check if a value exists in a sequence.

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
print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)
print("list1 != list2 :", list1 != list2)

# ===============================================================
# 8️⃣ BITWISE OPERATORS
# ===============================================================
"""
Bitwise operators work on the binary representation of integers:

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
# 9️⃣ OPERATOR PRECEDENCE & ASSOCIATIVITY
# ===============================================================
"""
Operator precedence determines the order in which operations are evaluated.
Higher precedence operators are executed first.

Some common rules:
1. Parentheses () → highest precedence
2. Exponentiation ** → right-to-left associativity
3. Unary +, -, ~ → right-to-left
4. *, /, //, % → left-to-right
5. +, - → left-to-right
6. <<, >> → left-to-right
7. & → left-to-right
8. ^ → left-to-right
9. | → left-to-right
10. Comparison operators (==, !=, >, <, >=, <=) → left-to-right
11. Logical not → right-to-left
12. Logical and → left-to-right
13. Logical or → left-to-right
14. Assignment operators (=, +=, etc.) → right-to-left

Example demonstrating precedence and associativity:
"""

a = 5
b = 2
c = 3

print("\n8. Operator Precedence Example:")
# Without parentheses, ** evaluated first, then * and + left-to-right
result = a + b * c ** 2
print("Expression: a + b * c ** 2")
print("Calculated as: 5 + 2 * 3 ** 2 =", result)

# Using parentheses to override precedence
result2 = (a + b) * c ** 2
print("Expression with parentheses: (a + b) * c ** 2 =", result2)

# ===============================================================
# END OF OPERATORS DEMO
# ===============================================================
print("\n===== End of Python Operators Demo =====")
print("Thank you for using the Python Operators Interactive Demo!")
print("Run this file multiple times with different inputs to practice.")
