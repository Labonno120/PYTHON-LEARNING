import re
email = input("Enter the email address: ").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
#bEnter the email address: BRISTY@HAVARD.EDU
#Valid