import re
email = input("Enter the email address: ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("Valid")
else:
    print("Invalid")
#bEnter the email address: bristy_123@gmail.com
#Valid