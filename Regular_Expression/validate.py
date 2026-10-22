email = input("Enter the email address: ").strip()
if "@" in email :
    print("Valid")
else:
    print("Invalid")
# will be valid for hello@, hello@@, hello@domain which is wrong.
