print("Hello, World!")
# This is a simple Python script that prints "Hello, World!" to the console.
# It serves as a basic example of a Python program.
name = input("Enter your name: ")
print("Hello, " + name + "!")
# It also takes user input and greets the user by name.
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
# Additionally, it checks the user's age and informs them if they are a minor or an adult.
print("Hi there! My name is " + name + " and I am " + str(age) + " years old.")
# Finally, it summarizes the user's name and age in a single sentence.
print(f"Hi there! My name is {name} and I am {age} years old. So, I am {'a minor' if age < 18 else 'an adult'}.")
# Finally, it summarizes the user's name and age in a single sentence.
friends = ["Alice", "Bob", "Charlie"]

print(friends[0])   # first item (Alice)
print(friends[1])   # second item (Bob)
print(friends[2])   # third item (Charlie)

for friend in friends:
    print("Hello, " + friend + "!")
# It also demonstrates list usage and iteration by greeting a list of friends.
# This code is a simple demonstration of Python's print function, input handling, and basic control
