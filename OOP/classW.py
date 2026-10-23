class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return f"{self.name} from {self.house}"
    #getter for name
    @property
    def name(self):
        return self._name
    #setter for name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    #getter for house
    @property
    def house(self):
        return self._house
    #setter for house
    @house.setter
    def house(self, house):
        if house not in ["Feni", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin","Dhaka"]:
            raise ValueError("Invalid House")
        self._house = house

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
    student.house = "Feni"
    print(student)
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus) 
    
if __name__ == "__main__":
    main()
