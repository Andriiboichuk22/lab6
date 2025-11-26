import random
import string


def generate_password(length=8, uppercase=True, digits=True, symbols=False):
    if length < 1:
        raise ValueError("Password length must be at least 1")

    characters = string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*()-_=+"

    return ''.join(random.choice(characters) for _ in range(length))
