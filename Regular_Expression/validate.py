import re
email = input("Enter the email address: ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")
#Typing in a sentence such as My email address is malan@harvard.edu. now is regarded as invalid.
#beacuse there is a period at the end of the sentences.
# the sententece should be end with .com beacuse of $
#malan@@@havard.edu will be valid which is a problem