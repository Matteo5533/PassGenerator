import random
import string

characters = ''

lenght = int(input("Enter password length "))
upper = int(bool(input("Enter 1 if capital letters are desired or 0 if not desired ")))
if upper >= 1:
    characters += string.ascii_uppercase
lower = int(bool(input("Enter 1 if lower case is desired or 0 if not desired ")))
if lower:
    characters += string.ascii_lowercase
punctuation = int(bool(input("Enter 1 if siblings are desired or 0 if they are not desired ")))
if punctuation:
    characters += string.punctuation

password = ''.join(random.choice(list(characters)) for i in range(lenght)) 

print(f"Your password is ", password)

