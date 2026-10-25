students = [
    {"name" : "Bristy", "house":"Feni"},
    {"name" : "Hai", "house" : "rongpur"},
    {"name" : "Joya", "house" : "sonaimuri"},
    {"name" : "Sohan", "house" : "sonaimuri"}
]
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
for house in houses:
    print(house)