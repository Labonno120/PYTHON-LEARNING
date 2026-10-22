import re
email = input("Enter the email address: ").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
#bEnter the email address: bristy_123@gmail.gov
#Valid