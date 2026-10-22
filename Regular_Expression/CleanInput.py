import re
name = input("Enter your name: ").strip()
if matches:= re.search(r"^(.+), *(.+)$",name):
    name = f"{matches.group(2)} {matches.group(1)}"
print(name)