import input_take

def main():
    print("Inside main")
    x = input_take.get_int("What's X? ")
    print("Square:", x * x)


main()