import string
import random

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

# Shuffle all character lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate portions of the password
part1 = round(characters_number * 0.3)  # 30% lowercase and uppercase letters
part2 = round(characters_number * 0.2)  # 20% digits and punctuation

# Generate the password components
result = []
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# Ensure the result has the exact number of characters requested
while len(result) < characters_number:
    result.append(random.choice(s1 + s2 + s3 + s4))

# Shuffle the final password and join into a string
random.shuffle(result)
password = "".join(result)

# Output the generated password
print("Strong Password:", password)
