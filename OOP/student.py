def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Capeverde"
    print(f"{student['name']} from {student['house']}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}# returning a dictionary

if __name__ == "__main__":
    main()