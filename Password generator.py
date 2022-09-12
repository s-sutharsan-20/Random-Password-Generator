import string
import random

passwrd = string.ascii_letters+string.digits+string.punctuation

password = int(input("Enter the Number of Passwords :"))
length = int(input("Enter the length of the password(s): "))

print("List(s) of Generated passwords: ")

for _ in range(password):
    print(''.join(random.sample(passwrd, k=length)))
