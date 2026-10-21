def main():
    name = input("What's your name? ")
    with open("name.txt", "a") as file:
        file.write(name + "\n")
main()