# with the help of Random and String Library, will be generating 12 length long password

import random
import string

pass_len = 12

char_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(char_values)

print("your random password is: " + password)

# same for loop operation can be done in list comprehension method

password_alternate = "".join([random.choice(char_values) for i in range(pass_len)])

print("your random password using alternate method is: " + password)