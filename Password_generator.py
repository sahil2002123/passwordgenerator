import random

lower = "abcdefghijklmnopqrstuvwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = "0123456789"

symbols = "!@#$%^&*()_+"

def generate_password(lenght):
    characters = lower + upper + num + symbols
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password

length = int(input("Enter the lenght of the password: "))
password = generate_password(length)
print(f"Generate the  Password: {password} ")
