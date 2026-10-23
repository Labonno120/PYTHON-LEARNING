class Student:
    ...#placeholder for code that will be added later

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    student = Student() #creates a new object from the student class
    student.name = input("Name: ")
    student.house = input("House: ") # dot lets u access the attribute of the object
    return student # returning a class
if __name__ == "__main__":
    main()
