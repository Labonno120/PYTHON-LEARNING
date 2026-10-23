class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gazipur", "Dhaka", "Feni", "Hyderabad"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return f"{self.name} from {self.house}"
    def charm(self):
        if self.patronus == "Stag":
            return "🐴"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russel terrier":
                return "🐶"
        else:
            return "🪄"

def main():
    student = get_student()
    print(student.charm())
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus) 
    
if __name__ == "__main__":
    main()
