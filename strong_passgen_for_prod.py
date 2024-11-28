import string
import secrets

# Store all characters in lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Prompt the user for the number of characters in the password
while True:
    try:
        user_input = input("How many characters do you want in your password? ")
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your password must be at least 8 characters long.")
        else:
            break
    except ValueError:  # Catch invalid inputs that cannot be converted to an integer
        print("Invalid input. Please enter a valid number.")

# Shuffle all character lists securely
s1 = secrets.SystemRandom().sample(s1, len(s1))
s2 = secrets.SystemRandom().sample(s2, len(s2))
s3 = secrets.SystemRandom().sample(s3, len(s3))
s4 = secrets.SystemRandom().sample(s4, len(s4))

# Calculate portions of the password
part1 = round(characters_number * 0.3)  # 30% lowercase and uppercase letters
part2 = round(characters_number * 0.2)  # 20% digits and punctuation

# Generate the password components
result = []
for x in range(part1):
    result.append(secrets.choice(s1))
    result.append(secrets.choice(s2))

for x in range(part2):
    result.append(secrets.choice(s3))
    result.append(secrets.choice(s4))

# Ensure the result has the exact number of characters requested
while len(result) < characters_number:
    result.append(secrets.choice(s1 + s2 + s3 + s4))

# Shuffle the final password securely and join into a string
secrets.SystemRandom().shuffle(result)
password = "".join(result)

# Output the generated password
print("Strong Password:", password)
