import re
email = input("Enter the email address: ").strip()

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")
#before: 
#Enter the email address: bristy@@@gmail.com
#Valid
#Now: 
#Enter the email address: bristy@@gmail.com
#Invalid