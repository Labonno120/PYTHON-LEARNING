import re
email = input("Enter the email address: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
#Enter the email address: malan@cs50.havard.edu
#Valid