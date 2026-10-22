email = input("Enter the email address: ").strip()
username, domain = email.split("@")
if username and domain and "." in domain:
    print("Valid")
else:
    print("Invalid")
