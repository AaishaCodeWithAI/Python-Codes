# Conditional Statements in Python

num= int(input("Enter the number: "))
if (num>0):
    print("Postive")
elif (num<0):
    print("Negative")
else:
    print("Zero")
#Checking if the number is Postive, Negative or Zero.
mark= int(input("Enter your marks: "))
if (mark>=90):
    print("A+")
elif (mark>=80):
    print("A")
elif (mark>=70):
    print("B")
else:
    print("C or below")
# Checking the grade based on marks.
age= int(input("Enter your age: "))
citizen= input("Are you a citizen? (yes/no): ")
if citizen.lower() == "yes":
    if age >= 18:
        print("You can vote.")
    else:
        print("You cannot vote yet.")
else:
    print("You must be a citizen to vote.")
# Checking voting eligibility based on age and citizenship.
signal = input("Enter traffic signal color (red/yellow/green): ")
if signal.lower() == "red":
    print("Stop")
elif signal.lower() == "yellow":
    print("Get Ready")
elif signal.lower() == "green":
    print("Go")
else:
    print("Invalid signal color")
# Traffic signal instructions based on color input.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "phoenix" and password == "phython123":
    print("Login Successful")
else:
    print("Incorrect username or password")
# Simple authentication check for username and password.
# This program demonstrates conditional statements in Python.

# =========================================
# Python Conditional Statements Demo
# =========================================

print("===== 1. Simple IF Statement =====")
x = int(input("Enter a number for IF test: "))
if x > 0:
    print(f"{x} is positive")

print("\n===== 2. IF-ELSE Statement =====")
y = int(input("Enter a number for IF-ELSE test: "))
if y % 2 == 0:
    print(f"{y} is even")
else:
    print(f"{y} is odd")

print("\n===== 3. IF-ELIF-ELSE Statement =====")
z = int(input("Enter a number for IF-ELIF-ELSE test: "))
if z > 0:
    print(f"{z} is positive")
elif z < 0:
    print(f"{z} is negative")
else:
    print(f"{z} is zero")

print("\n===== 4. Nested IF Statement =====")
num = int(input("Enter a number for Nested IF test: "))
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")

print("\n===== 5. Switch-Case using match-case (Python 3.10+) =====")
choice = input("Enter a fruit (apple, banana, cherry): ").lower()

try:
    match choice:
        case "apple":
            print("You chose Apple")
        case "banana":
            print("You chose Banana")
        case "cherry":
            print("You chose Cherry")
        case _:
            print("Unknown fruit")
except SyntaxError:
    print("match-case is available only in Python 3.10+")

print("\n===== 6. Switch-Case alternative using dictionary =====")
def switch_dict(fruit):
    return {
        "apple": "You chose Apple",
        "banana": "You chose Banana",
        "cherry": "You chose Cherry"
    }.get(fruit, "Unknown fruit")

fruit_input = input("Enter a fruit (apple, banana, cherry) for dict switch: ").lower()
print(switch_dict(fruit_input))

print("\n===== End of Conditional Statements Demo =====")

