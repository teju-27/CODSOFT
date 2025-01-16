import random
import string
def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    characters = list(string.ascii_lowercase)
    if use_uppercase:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_symbols:
        characters.extend(string.punctuation)
    if not characters:
        raise ValueError("No characters available to generate password. Enable at least one character set.")
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        password = generate_password(length, include_uppercase, include_digits, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")