import re
password = input("What is your password and i'll give you your strength ")
output = ""
x = re.findall("[0-9]",password)
y = re.findall("[a-zA-Z]",password)
z = re.findall("\W", password)
if len(password) < 8:
    if len(x) == len(password):
        output = "the password '{0}' is a very weak password."
    elif len(y) == len(password):
        output = "the password '{0}' is a weak password."
    else:
        output = "I don't know the strength."
else:
    if len(z) > 1:
        output = "the password '{0}' is a very strong password."
    elif len(x) > 0 and len(y) > 0:
        output = "the password '{0}' is a strong password."
    else:
        output = "I don't know the strength."
print(output.format(password))