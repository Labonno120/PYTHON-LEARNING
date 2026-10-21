import csv
students = []
with open("students.csv", "r") as file:
    r = csv.reader(file)
    for line in r:
        #everytime different dictionary is created
        students.append({"name":line[0], "house":line[1]})

for s in sorted(students, key = lambda s: s["name"]):# hey python, here is a function with no name: Given a s, access their name and return to that key
    print(s["name"] + " is in " + s["house"])

