"""
====================================================================
Python Data Types — Complete Guide
====================================================================

This file contains detailed explanations of all Python standard
data types, along with code examples that can be executed directly.

Variables store data in a program
Variables have names and hold values (data) of different types.
Variables are created by assigning a value using the '=' operator.
Example: age = 25, name = "Alice"

Python has several built-in data types, categorized into the following: 

1. Numeric Types
2. Sequence Types
3. Set Types
4. Mapping Type
5. Boolean Type
6. NoneType

Each section has notes and runnable code.
"""

# ===============================================================
# 1️⃣ Numeric Types
# ===============================================================

# --- Integer (int) ---
"""
The integer type stores whole numbers. Can be positive, negative, or zero.
Supports arithmetic operations. 
In Python, integers can be of arbitrary(unlimited) size (limited only by available memory).
"""
x = 42
y = -7
z = 0

print("Integer examples:", x, y, z)
print("Type of x:", type(x))

# --- Floating-point (float) ---
"""
Float type stores decimal numbers (numbers with fractional parts).
"""
pi = 3.1415
temp = -4.5
big_float = 1.2e5

print("\nFloat examples:", pi, temp, big_float)
print("Type of pi:", type(pi))

# --- Complex (complex) ---
"""
Complex type stores numbers with real and imaginary parts.
"""
z1 = 2 + 3j
z2 = complex(4, -1)
print("\nComplex examples:", z1, z2)
print("Real part of z1:", z1.real)
print("Imag part of z1:", z1.imag)
print("Type of z1:", type(z1))

# ===============================================================
# 2️⃣ Sequence Types
# ===============================================================

# --- String (str) ---
"""
String stores an ordered series or sequence of characters of alphabets, numerics and special characters that are enclosed in single or double quotes.
It is immutable (cannot be changed after creation).
There are various string operations like concatenation, slicing, formatting, repetition, etc.
"""
s = "Python"
print("\nString example:", s)
print("First char:", s[0])
print("Slice s[1:4]:", s[1:4])
print("Length:", len(s))

# --- List (list) ---
"""
A list is a sequence that stores ordered, indexable, mutable elements. It can store mixed types.
It needs to separate elements using commas and enclose them within square brackets [].
Same as String, the list supports indexing, slicing, concatenation, and repetition.
Similar to arrays in other languages, but more flexible.
"""
lst = [1, 2, 3, "Python", 3.14, True]
print("\nList example:", lst)
lst[1] = "Changed"
lst.append("New")
lst.pop(2)
print("Modified list:", lst)

# --- Tuple (tuple) ---
"""
Tuple stores ordered, immutable (cannot be changed after creation), read-only elements.
Similar to lists but with parentheses () instead of square brackets [].
Tuples are often used to group related data.
"""
t = (1, 2, 3, "Python")
print("\nTuple example:", t)
print("First element:", t[0])
print("Last element:", t[-1])
print("Length:", len(t))

# --- Range (range) ---
"""
A range represents an immutable (cannot be changed after creation) sequence of numbers, often used in loops.
"""
r = range(5)
print("\nRange example:", list(r))

r2 = range(2, 10, 2)
print("Range with step:", list(r2))
print("Slice of range r2[1:3]:", list(r2[1:3]))

# --- Bytes (bytes) ---
"""
Bytes are immutable (cannot be changed after creation) sequences of integers (0-255)
"""
b = b"hello"
print("\nBytes example:", b)
print("First byte:", b[0])
print("Slice b[1:4]:", b[1:4])

# --- Bytearray (bytearray) ---
"""
Bytearray is a mutable version of bytes
"""
ba = bytearray(b"hello")
ba[0] = 72  # ASCII for 'H'
print("Bytearray example after modification:", ba)

# ===============================================================
# 3️⃣ Set Types
# ===============================================================

# --- Set (set) ---
"""
Set stores unordered, unique (no duplicates) elements
"""
st = {1, 2, 3, 3, 2}
print("\nSet example:", st)
st.add(4)
st.remove(2)
print("Modified set:", st)

# --- Frozen set (frozenset) ---
"""
Frozen set is an immutable (cannot be changed after creation) version of a set.
"""
fst = frozenset([1, 2, 3])
print("Frozen set example:", fst)

# ===============================================================
# 4️⃣ Mapping Type
# ===============================================================

# --- Dictionary (dict) ---
"""
A dictionary stores key-value pairs. Keys are unique (no duplicates allowed). Values can be of any type.
Dictionaries are mutable (can be changed after creation) and unordered (no specific order).
"""
d = {"name": "Alice", "age": 25, "is_student": True}
print("\nDictionary example:", d)
d["age"] = 26
d["city"] = "Nepal"

for key, value in d.items():
    print(f"{key} : {value}")

# ===============================================================
# 5️⃣ Boolean Type
# ===============================================================

"""
Boolean type stores True or False values. It is often used in conditional statements and logical operations.
It is a subclass of integers where True is equivalent to 1 and False is equivalent to 0.
It supports logical operations like and, or, and not and comparison operations like ==, !=, >, <, >=, <=, etc.)
"""
flag = True
x = 10
y = 5
print("\nBoolean example:", flag)
print("x > y:", x > y)
print("flag and (x > y):", flag and (x > y))

# ===============================================================
# 6️⃣ NoneType
# ===============================================================

"""
NoneType represents 'no value'. It has a single value None.
It is often used to indicate the absence of a value or a null value. 
It is commonly used as a default value for function arguments or to signify that a variable has not been assigned a value yet.
It is different from False, 0, or an empty string/list/dictionary.
"""
n = None
print("\nNoneType example:", n)
print("Type of n:", type(n))

def greet(name=None):
    if name is None:
        print("Hello, Guest")
    else:
        print(f"Hello, {name}")

greet()
greet("Alice")
