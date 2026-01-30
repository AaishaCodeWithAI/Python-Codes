"""
====================================================================
Slicing in Python — Complete Guide (Slicing.py)
====================================================================

This file explains slicing in Python with complete notes and
Examples for ALL data types that support slicing.

What is Slicing?
Slicing is a technique to extract a portion (subsequence) from a
sequence data type by specifying a range of indices.
Silcing creates a NEW object containing the extracted portion,
while the original object remains unchanged.

Slicing vs Indexing:
- Indexing retrieves a single element at a specific position.
- Slicing retrieves a range of elements (subsequence).

Slicing Characteristics:
- Works on sequence data types (str, list, tuple, range, bytes, bytearray)
- Returns a NEW object of the same type as the original
- Original object remains unchanged (immutable types)

Slicing Syntax:
    sequence[start : stop : step]

- start → index to begin (inclusive)
- stop  → index to end (exclusive)
- step  → jump value

Data types that support slicing:
1. str (String)
2. list
3. tuple
4. range
5. bytes
6. bytearray
"""

# ===============================================================
# 1️⃣ STRING SLICING (str)
# ===============================================================

"""
Strings are immutable sequences of characters.
Slicing allows you to extract a portion of a string by specifying a range of indices and returns a new string.
Original string remains unchanged.
"""

s = "PythonProgramming"

print("\n--- STRING SLICING ---")
print("Original string:", s)

print("s[0:6]  ->", s[0:6])      # Python
print("s[6:]   ->", s[6:])       # Programming
print("s[:6]   ->", s[:6])       # Python
print("s[::2]  ->", s[::2])      # PtoPormig
print("s[::-1] ->", s[::-1])     # Reverse string


# ===============================================================
# 2️⃣ LIST SLICING (list)
# ===============================================================

"""
Lists are mutable sequences.
It can be used to extract sublists and returns a NEW list.
Original list remains unchanged.
"""

lst = [10, 20, 30, 40, 50, 60]

print("\n--- LIST SLICING ---")
print("Original list:", lst)

print("lst[1:4]  ->", lst[1:4])   # [20, 30, 40]
print("lst[:3]   ->", lst[:3])    # [10, 20, 30]
print("lst[3:]   ->", lst[3:])    # [40, 50, 60]
print("lst[::2]  ->", lst[::2])   # [10, 30, 50]
print("lst[::-1] ->", lst[::-1])  # Reverse list


# ===============================================================
# 3️⃣ TUPLE SLICING (tuple)
# ===============================================================

"""
Tuples are immutable sequences.
It extracts sub-tuples and returns a NEW tuple.
"""

t = (1, 2, 3, 4, 5, 6)

print("\n--- TUPLE SLICING ---")
print("Original tuple:", t)

print("t[2:5]  ->", t[2:5])    # (3, 4, 5)
print("t[:4]   ->", t[:4])     # (1, 2, 3, 4)
print("t[::2]  ->", t[::2])    # (1, 3, 5)
print("t[::-1] ->", t[::-1])   # Reverse tuple


# ===============================================================
# 4️⃣ RANGE SLICING (range)
# ===============================================================

"""
Range is an immutable sequence of numbers.
it extracts the sub-range and returns another range object.
"""

r = range(0, 20, 2)

print("\n--- RANGE SLICING ---")
print("Original range:", list(r))

print("r[2:6]   ->", list(r[2:6]))   # [4, 6, 8, 10]
print("r[:5]    ->", list(r[:5]))    # [0, 2, 4, 6, 8]
print("r[::2]   ->", list(r[::2]))   # [0, 4, 8, 12, 16]
print("r[::-1]  ->", list(r[::-1]))  # Reverse range


# ===============================================================
# 5️⃣ BYTES SLICING (bytes)
# ===============================================================

"""
Bytes are immutable sequences of integers (0–255).
Mostly used in networking, files, encoding.
It extracts sub-bytes and returns a NEW bytes object.
"""

b = b"HELLOPYTHON"

print("\n--- BYTES SLICING ---")
print("Original bytes:", b)

print("b[0:5]  ->", b[0:5])    # b'HELLO'
print("b[5:]   ->", b[5:])     # b'PYTHON'
print("b[::2]  ->", b[::2])    # b'HLOYHN'
print("b[::-1] ->", b[::-1])   # Reverse bytes


# ===============================================================
# 6️⃣ BYTEARRAY SLICING (bytearray)
# ===============================================================

"""
Bytearray is a mutable version of bytes.
It extracts sub-bytearrays and returns a NEW bytearray.
"""

ba = bytearray(b"HELLOPYTHON")

print("\n--- BYTEARRAY SLICING ---")
print("Original bytearray:", ba)

print("ba[0:5]  ->", ba[0:5])    # bytearray(b'HELLO')
print("ba[5:]   ->", ba[5:])     # bytearray(b'PYTHON')
print("ba[::2]  ->", ba[::2])    # bytearray(b'HLOYHN')
print("ba[::-1] ->", ba[::-1])   # Reverse bytearray

# Demonstrating mutability
ba[0] = 104  # ASCII for 'h'
print("Modified bytearray:", ba)


# ===============================================================
# ❌ DATA TYPES THAT DO NOT SUPPORT SLICING
# ===============================================================

"""
The following data types DO NOT support slicing because
they are not ordered sequences:

- int
- float
- complex
- bool
- set
- dict
- NoneType
"""

print("\n--- NON-SLICABLE TYPES (INFO) ---")
print("int, float, complex, bool, set, dict, NoneType → No slicing")


# ===============================================================
# ✅ END OF FILE
# ===============================================================

"""
Summary:
Slicing works ONLY on sequence data types:
str, list, tuple, range, bytes, bytearray

This file is designed for:
✔ Learning
✔ Teaching
✔ GitHub reference
✔ Interview & exam preparation
"""
