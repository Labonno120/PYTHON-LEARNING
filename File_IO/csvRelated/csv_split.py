import csv
students = []
name = input("Enter the name: ")
home  = input("Enter the house name: ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["Name", "Home"])
    writer.writerow({"Name":name,"Home":home})
with open("students.csv", "r") as file:
    r = csv.DictReader(file)
    for line in r:
        #everytime different dictionary is created
        students.append({"name":line["Name"], "house":line["Home"]})
for s in sorted(students, key = lambda s: s["name"]):# hey python, here is a function with no name: Given a s, access their name and return to that key
    print(s["name"] + " is in " + s["house"])

