students = []
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #everytime different dictionary is created
        students.append({"name":name, "house":house})
def getName(s):
    return s["name"]
for s in sorted(students, key = getName):
    print(s["name"] + " is in " + s["house"])

