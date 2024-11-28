import string
import random
import secrets
from cryptography.fernet import Fernet

# Step 1: Generate a secure encryption key (you should store this securely, not hardcoded here)
key = Fernet.generate_key()
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
            user_input = input("Please, enter your number again: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        user_input = input("Please, enter your number again: ")

# Step 4: Shuffle the character lists securely using a cryptographically secure PRNG
secrets.SystemRandom().shuffle(s1)
secrets.SystemRandom().shuffle(s2)
secrets.SystemRandom().shuffle(s3)
secrets.SystemRandom().shuffle(s4)

# Step 5: Calculate the portion of characters for each list
part1 = round(characters_number * 0.30)  # 30% of characters from lowercase letters
part2 = round(characters_number * 0.20)  # 20% of characters from digits and punctuation

# Step 6: Generate the password by appending characters from each list
result = []
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# Step 7: Ensure the result has the exact number of characters requested
while len(result) < characters_number:
    result.append(secrets.choice(s1 + s2 + s3 + s4))

# Step 8: Shuffle the result to avoid patterns
secrets.SystemRandom().shuffle(result)

# Step 9: Join the result to form the password
password = "".join(result)

# Step 10: Encrypt the password
encrypted_password = cipher_suite.encrypt(password.encode())

# Step 11: Store the encrypted password securely
with open("password_storage.txt", "wb") as file:
    file.write(encrypted_password)

print("Your password has been securely generated and encrypted.")
