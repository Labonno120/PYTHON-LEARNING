import re
name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$",name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(name)