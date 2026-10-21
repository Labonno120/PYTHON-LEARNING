name = []
with open("name.txt", "r") as file:
    for line in file:
        name.append(line.strip())
for n in sorted(name):
    print("Hello, " + n)


