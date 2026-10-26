students = [
    {"name":"Bristy", "house":"Feni"},
    {"name":"Trishna", "house":"Feni"},
    {"name":"Tonmoy", "house":"Feni"},
    {"name":"hai","house":"rongpur"}
]

def isFeni(h):
    return h["house"] == "Feni"
fenian = filter(isFeni, students)
for student in sorted(fenian, key = lambda s: s["name"]):
    print(student["name"])