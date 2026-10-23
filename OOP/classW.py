class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name,house) #creates a new object from the student class
     # dot lets u access the attribute of the object
    return student # returning a class
if __name__ == "__main__":
    main()
