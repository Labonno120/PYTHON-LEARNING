students = [
    {"name":"Bristy", "house":"Feni"},
    {"name":"Trishna", "house":"Feni"},
    {"name":"Tonmoy", "house":"Feni"},
    {"name":"hai","house":"rongpur"}
]

fenian = filter(lambda st: st["house"] == "Feni", students)
for student in sorted(fenian, key = lambda s: s["name"]):
    print(student["name"])