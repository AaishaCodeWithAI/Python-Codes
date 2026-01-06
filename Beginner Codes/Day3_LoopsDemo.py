# =========================================
# Python Loops Demonstration – All Types
# First: loops | Second: break & continue
# =========================================

print("===== PART 1: All Types of Loops =====")

# 1. Basic for loop
print("\n1. Basic for loop")
for i in range(5):
    print("i =", i)

# 2. For loop with custom start and step
print("\n2. For loop with start, stop, step")
for i in range(1, 10, 2):
    print("i =", i)

# 3. For loop iterating over a list
print("\n3. For loop over a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# 4. Nested for loops
print("\n4. Nested for loops")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# 5. For loop with else
print("\n5. For loop with else")
for i in range(3):
    print("i =", i)
else:
    print("For loop finished (else executed)")

# 6. Basic while loop
print("\n6. Basic while loop")
count = 0
while count < 5:
    print("count =", count)
    count += 1

# 7. While loop with else
print("\n7. While loop with else")
count = 0
while count < 3:
    print("count =", count)
    count += 1
else:
    print("While loop finished (else executed)")

# 8. Nested while loop
print("\n8. Nested while loops")
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# 9. Simulated do-while loop
print("\n9. Simulated do-while loop")
count = 0
while True:
    print("count =", count)
    count += 1
    if count >= 3:  # condition checked at end
        break

print("\n===== PART 2: Break and Continue =====")

# Break in for loop
print("\n1. Break in for loop")
for i in range(5):
    if i == 3:
        print("Breaking at i =", i)
        break
    print("i =", i)

# Continue in for loop
print("\n2. Continue in for loop")
for i in range(5):
    if i == 2:
        print("Skipping i =", i)
        continue
    print("i =", i)

# Break in while loop
print("\n3. Break in while loop")
count = 0
while count < 5:
    if count == 3:
        print("Breaking at count =", count)
        break
    print("count =", count)
    count += 1

# Continue in while loop
print("\n4. Continue in while loop")
count = 0
while count < 5:
    count += 1
    if count == 2:
        print("Skipping count =", count)
        continue
    print("count =", count)

# Break & continue in nested loops
print("\n5. Break & Continue in nested loops")
for i in range(1, 3):
    for j in range(1, 4):
        if j == 2:
            print(f"Skipping inner loop j={j}")
            continue
        print(f"i={i}, j={j}")
        if i == 2 and j == 3:
            print("Breaking inner loop")
            break

# Break & continue in simulated do-while
print("\n6. Break & Continue in simulated do-while loop")
count = 0
while True:
    count += 1
    if count == 2:
        print("Skipping count =", count)
        continue
    print("count =", count)
    if count >= 4:
        print("Breaking simulated do-while at count =", count)
        break

print("\n===== End of Loops Demo =====")
