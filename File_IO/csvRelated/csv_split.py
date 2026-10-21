students = []
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #everytime different dictionary is created
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)
for s in students:
    print(s["name"] + " is in " + s["house"])

