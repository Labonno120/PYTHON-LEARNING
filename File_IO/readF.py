with open("name.txt", "r") as file:
    contents = file.readlines()

for line in contents:
    print("hello", line.rstrip())

