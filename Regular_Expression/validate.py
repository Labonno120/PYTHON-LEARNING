import re
email = input("Enter the email address: ").strip()

if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")