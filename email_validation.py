import re
email=input("Enter email")
x = re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)
# r before the string indicates a raw string, which treats backslashes as literal characters.
# \\. represents a literal dot.

if x:
    print("valid email")
else:
    print("Invalid email")