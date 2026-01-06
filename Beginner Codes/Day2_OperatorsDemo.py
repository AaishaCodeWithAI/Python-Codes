# ===============================================
# Python Operators Demo – Interactive Version
# ===============================================

# 1️⃣ User Input
print("Welcome to Python Operators Interactive Demo!\n")
num1 = int(input("Enter first number (num1): "))
num2 = int(input("Enter second number (num2): "))

# Membership input
sequence = input("Enter a list of items separated by commas (for membership test): ").split(',')
item_to_check = input("Enter an item to check if it exists in the list: ")

# Logical input
print("\nLogical Operators Test (True/False)")
p_input = input("Enter True or False for p: ")
q_input = input("Enter True or False for q: ")
p = True if p_input.lower() == 'true' else False
q = True if q_input.lower() == 'true' else False

# Identity test inputs
list1 = input("Enter first list for identity test (comma separated): ").split(',')
list2 = input("Enter second list for identity test (comma separated): ").split(',')

print("\n==============================================")
print("Results:")

# 2️⃣ Arithmetic Operators
print("\n1. Arithmetic Operators:")
print(f"{num1} + {num2} =", num1 + num2)
print(f"{num1} - {num2} =", num1 - num2)
print(f"{num1} * {num2} =", num1 * num2)
print(f"{num1} / {num2} =", num1 / num2 if num2 != 0 else "Cannot divide by zero")
print(f"{num1} // {num2} =", num1 // num2 if num2 != 0 else "Cannot divide by zero")
print(f"{num1} % {num2} =", num1 % num2 if num2 != 0 else "Cannot modulo by zero")
print(f"{num1} ** {num2} =", num1 ** num2)

# 3️⃣ Comparison Operators
print("\n2. Comparison Operators:")
print(f"{num1} == {num2} :", num1 == num2)
print(f"{num1} != {num2} :", num1 != num2)
print(f"{num1} > {num2} :", num1 > num2)
print(f"{num1} < {num2} :", num1 < num2)
print(f"{num1} >= {num2} :", num1 >= num2)
print(f"{num1} <= {num2} :", num1 <= num2)

# 4️⃣ Logical Operators
print("\n3. Logical Operators:")
print(f"{p} and {q} :", p and q)
print(f"{p} or {q} :", p or q)
print(f"not {p} :", not p)

# 5️⃣ Assignment Operators
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

# 6️⃣ Membership Operators
print("\n5. Membership Operators:")
print(f"List:", sequence)
print(f"'{item_to_check}' in list:", item_to_check in sequence)
print(f"'{item_to_check}' not in list:", item_to_check not in sequence)

# 7️⃣ Identity Operators
print("\n6. Identity Operators:")
print(f"List1: {list1}")
print(f"List2: {list2}")
print("list1 is list2 :", list1 is list2)
print("list1 is not list2 :", list1 is not list2)

# 8️⃣ Bitwise Operators
print("\n7. Bitwise Operators (integers only):")
print(f"{num1} & {num2} :", num1 & num2)
print(f"{num1} | {num2} :", num1 | num2)
print(f"{num1} ^ {num2} :", num1 ^ num2)
print(f"~{num1} :", ~num1)
print(f"{num1} << 1 :", num1 << 1)
print(f"{num1} >> 1 :", num1 >> 1)

print("\n===== End of Operators Demo =====")
