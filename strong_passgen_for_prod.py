import string
import secrets
from cryptography.fernet import Fernet
import os

# Step 1: Generate or retrieve a secure encryption key
key = os.environ.get('FERNET_KEY')
if not key:
    print("Encryption key is missing.")
    exit(1)
cipher_suite = Fernet(key)

# Step 2: Define all character sets for password generation
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Step 3: Ask user for password length
user_input = input("How many characters do you want in your password? ")
while True:
    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your password must be at least 8 characters long.")
        elif characters_number > 128:
            print("Your password length is too large. Please enter a reasonable number.")
        else:
            break
        user_input = input("Please, enter your number again: ")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        user_input = input("Please, enter your number again: ")

# Step 4: Securely shuffle the character lists using secrets.SystemRandom()
s1 = secrets.SystemRandom().sample(s1, len(s1))  # Securely shuffle lowercase letters
s2 = secrets.SystemRandom().sample(s2, len(s2))  # Securely shuffle uppercase letters
s3 = secrets.SystemRandom().sample(s3, len(s3))  # Securely shuffle digits
s4 = secrets.SystemRandom().sample(s4, len(s4))  # Securely shuffle punctuation

# Step 5: Create the password
all_chars = s1 + s2 + s3 + s4
result = [secrets.choice(all_chars) for _ in range(characters_number)]

# Step 6: Shuffle the result
secrets.SystemRandom().shuffle(result)

# Step 7: Join and encrypt the password
password = "".join(result)
encrypted_password = cipher_suite.encrypt(password.encode())

# Step 8: Store the encrypted password
try:
    with open("password_storage.txt", "wb") as file:
        file.write(encrypted_password)
    print("Your password has been securely generated and encrypted.")
except Exception as e:
    print(f"Error saving the password: {e}")
