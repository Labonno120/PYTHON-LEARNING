import random
class Hat:
    houses = ["Feni", "Dhaka", "Mirpur"]
    @classmethod
    def rd(cls, name):
        print(name + " is from " +random.choice(cls.houses))

def main():
    Hat.rd("Harry")
if __name__ == "__main__":
    main()
