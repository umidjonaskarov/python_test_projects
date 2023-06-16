import random
import string

length = int(input('Enter character number: '))
special_symbols = input('Special symbols? (y/N): ').lower() == 'y'
capital_letters = input('Capital letters? (y/N): ').lower() == 'y'

def generate_password():
    characters = string.ascii_lowercase + string.digits
    if special_symbols:
        characters += "!@#$%^&*()"
    if capital_letters:
        characters += string.ascii_uppercase

    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Usage example
password = generate_password()
print("Generated Password:", password)
