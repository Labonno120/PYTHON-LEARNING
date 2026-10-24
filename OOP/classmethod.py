import random
class Hat:
    def __init__(self):
      self.houses = ["Feni", "Dhaka", "Mirpur"]
    
    def rd(self, name):
        print(name + " is from " +random.choice(self.houses))

def main():
    hat = Hat()
    hat.rd("Harry")
if __name__ == "__main__":
    main()
