class Wizard:
    def __init__(self,name):
        self.name = name
class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
def main():
    student = Student("Bristy","Feni")
    professor = Professor("Masudur Ramnan", "Image processing")
    print(student.name + " is from " + student.house)
    print(professor.name + " is teaching " + professor.subject)
main()