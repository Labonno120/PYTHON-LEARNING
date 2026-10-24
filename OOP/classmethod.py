import random
class Student:
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # initializing class, beacuse its class itself
    def __init__(self,name,house):
        self.house = house
        self.name = name
    def __str__(self):
        return (self.name + " is from " + self.house)
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()