students = [
    {"name" : "Bristy", "house": "feni"},
    {"name": "hai", "house" : "feni"},
    {"name":"trishna", "house": "feni"},
    {"name":"jibon", "house": "sylhet"}
]
house = [
    st["name"] for st in students if st["house"] == "feni"
]
print(*house)