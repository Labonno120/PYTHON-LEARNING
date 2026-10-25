students = [
    {"name" : "Bristy", "house":"Feni"},
    {"name" : "Hai", "house" : "rongpur"},
    {"name" : "Joya", "house" : "sonaimuri"},
    {"name" : "Sohan", "house" : "sonaimuri"}
]
houses = set()
for student in students:
        houses.add(student["house"])
for house in sorted(houses):
    print(house)