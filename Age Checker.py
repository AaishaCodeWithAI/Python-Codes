# Age Checker Program
print("=== AGE CHECKER ===")

# Get user input
age = int(input("How old are you? "))

# Check age for different activities
print("\nHere's what you can do:")

if age >= 18:
    print("✓ Vote in elections")
else:
    print("✗ Vote in elections (need to be 18+)")

if age >= 18:
    print("✓ Drink alcohol in the Nepal")
else:
    print("✗ Drink alcohol in the Nepal (need to be 18+)")

if age >= 18:
    print("✓ Get a driver's license in most states")
else:
    print("✗ Get a driver's license (need to be 18+)")

if age >= 65:
    print("✓ Get senior discounts")
else:
    print("✗ Get senior discounts (need to be 65+)")

# Special message based on age
if age < 13:
    print("\nYou're a kid!")
elif age < 20:
    print("\nYou're a teenager!")
elif age < 30:
    print("\nYou're in your twenties!")
else:
    print("\nYou're an adult!")
