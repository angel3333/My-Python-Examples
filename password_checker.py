username = input('What is your username?')
password = input('What is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} letters long')