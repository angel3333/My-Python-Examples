# Using RegEx, construct a password validation that contains
# At least 8 characters
# contains any type of letters, numbers and $%#@
# and ends with a number

import re

pattern = re.compile(r'[a-zA-Z0-9$%#@]{8,}\d$')
string = 'user123$#@3'
a = pattern.fullmatch(string)

if a == None:
    print('your password must be at least 8 digits long\n contain letters, numbers, any of these symbols $%#@ and end with a number')

else:
    print('logged in')
