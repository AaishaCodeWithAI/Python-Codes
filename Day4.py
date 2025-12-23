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
