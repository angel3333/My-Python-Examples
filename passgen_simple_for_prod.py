import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for the password from these :
      1. Digits
      2. Letters
      3. Special Characters
      4. All
      5. Exit
      ''')

characterList = ""

# Getting character set for password
while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        characterList = characterList + string.digits
        break
    elif choice == 2:
        characterList = characterList + string.ascii_letters
        break
    elif choice == 3:
        characterList = characterList + string.punctuation
        break
    elif choice == 4:
        characterList = characterList + string.digits + string.ascii_letters + string.punctuation
        break
    elif choice == 5:
        break
    else:
        print("Invalid choice")

# Generating password
if len(characterList) >= length:
    password = "".join(random.sample(characterList, length))

# Printing password
    print("Your secure password is: " + password)
else:
    print("Not enough characters in the selected character set to generate a password of the specified length.")
