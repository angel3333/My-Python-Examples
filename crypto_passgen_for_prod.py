import string
import secrets
from cryptography.fernet import Fernet
import os

# Step 1: Generate or retrieve a secure encryption key
key = os.environ.get('FERNET_KEY')
if not key:
    print("Encryption key is missing. Please set the 'FERNET_KEY' environment variable.")
    exit(1)
cipher_suite = Fernet(key)

# Step 2: Define all character sets for password generation
s1 = list(string.ascii_lowercase)  # Lowercase letters
s2 = list(string.ascii_uppercase)  # Uppercase letters
s3 = list(string.digits)          # Digits
s4 = list(string.punctuation)     # Special characters

# Step 3: Ask user for password length
while True:
    try:
        characters_number = int(input("How many characters do you want in your password? "))
        if 8 <= characters_number <= 128:
            break
        print("Please choose a number between 8 and 128.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Step 4: Securely shuffle the character lists using secrets.SystemRandom()
secure_random = secrets.SystemRandom()
s1 = secure_random.sample(s1, len(s1))  # Securely shuffle lowercase letters
s2 = secure_random.sample(s2, len(s2))  # Securely shuffle uppercase letters
s3 = secure_random.sample(s3, len(s3))  # Securely shuffle digits
s4 = secure_random.sample(s4, len(s4))  # Securely shuffle punctuation

# Step 5: Create the password
# Ensure at least one character from each set is included
result = [
    secrets.choice(s1),
    secrets.choice(s2),
    secrets.choice(s3),
    secrets.choice(s4)
]

# Fill the remaining slots randomly
remaining_characters = characters_number - len(result)
result.extend(secrets.choice(s1 + s2 + s3 + s4) for _ in range(remaining_characters))

# Secure final shuffle
result = secure_random.sample(result, len(result))

# Step 6: Join and encrypt the password
password = "".join(result)
encrypted_password = cipher_suite.encrypt(password.encode())

# Step 7: Store the encrypted password securely
try:
    with open("password_storage.txt", "wb") as file:
        file.write(encrypted_password)
    print("Your password has been securely generated and encrypted.")
    print("The encrypted password has been saved in 'password_storage.txt'.")
    print("Ensure your encryption key is securely stored to decrypt the password.")
except IOError as e:
    print(f"File operation failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
