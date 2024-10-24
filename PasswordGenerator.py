import random
import string

characters = ''

# Function to check that the input is a number greater than 1
def get_password_length():
    while True:
        length = input("Enter password length (must be a number greater than 1): ")
        if length.isdigit() and int(length) > 1:
            return int(length)
        else:
            print("Invalid input! Please enter a valid number greater than 1.")

# Ask the user for password length
length = get_password_length()

# Remainder of password generation options
upper = int(bool(input("Enter 1 if capital letters are desired or 0 if not desired: ")))
if upper:
    characters += string.ascii_uppercase
lower = int(bool(input("Enter 1 if lower case is desired or 0 if not desired: ")))
if lower:
    characters += string.ascii_lowercase
punctuation = int(bool(input("Enter 1 if punctuation is desired or 0 if not desired: ")))
if punctuation:
    characters += string.punctuation

# Check for selected characters
if not characters:
    print("No character sets selected. Exiting.")
else:
    # Generate password
    password = ''.join(random.choice(characters) for i in range(length)) 
    print(f"Your password is: {password}")
