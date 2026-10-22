email = input("Enter the email address: ").strip()
username, domain = email.split("@")
if username and domain.endswith(".com"):
    print("Valid")
else:
    print("Invalid")
#can be valid for hello@.come which is wrong.