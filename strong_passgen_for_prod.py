import string
import random
import secrets

# Store all characters in lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")

# Check if the input is a valid number and greater than or equal to 8
while True:
    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your password must be at least 8 characters long.")
            user_input = input("Please, enter your number again: ")
        else:
            break
    except ValueError:  # Catch invalid inputs
        print("Invalid input. Please enter a valid number.")
        user_input = input("Please, enter your number again: ")

# Securely shuffle all character lists
s1 = secrets.SystemRandom().sample(s1, len(s1))
s2 = secrets.SystemRandom().sample(s2, len(s2))
s3 = secrets.SystemRandom().sample(s3, len(s3))
s4 = secrets.SystemRandom().sample(s4, len(s4))

# Calculate portions of the password
part1 = round(characters_number * 0.3)  # 30% lowercase and uppercase letters
part2 = round(characters_number * 0.2)  # 20% digits and punctuations

# Generate the password
result = []
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])
for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# Ensure the result has the exact number of characters requested
while len(result) < characters_number:
    result.append(secrets.choice(s1 + s2 + s3 + s4))

# Shuffle the final password securely
secrets.SystemRandom().shuffle(result)

# Join the result to form the password
password = "".join(result)

# Mask the password except for the last 4 characters
masked_password = '*' * (len(password) - 4) + password[-4:]

# Output the masked password
print("Generated password:", masked_password)
