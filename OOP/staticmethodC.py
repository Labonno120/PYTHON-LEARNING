class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
def main():
    print(f"The Sum is {Calculator.add(2,3)}")
main()