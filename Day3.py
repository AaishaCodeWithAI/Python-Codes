for i in range (1, 11):
     print(i)
     
for i in range (2, 21, 2):
     print(i)

for char in "Python":
     print(char)

total = 0

for i in range(1, 11):
    total += i

print("Sum of first 10 numbers is:", total)

word = input("Enter word: ")

for ch in word:
    print(ch)

total = 0

for i in range(1, 11):
    total += i

print(total)

for i in range(5, -1, -1):
    print(i)

for i in range(1, 51):
    if i % 7 == 0:
        print("First number divisible by 7 is:", i)
        break

word = input("Enter word: ")
print(word[::-1])
