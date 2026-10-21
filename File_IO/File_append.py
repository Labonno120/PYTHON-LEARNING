def main():
    name = input("What's your name? ")
    file = open("name.txt", "a")
    file.write(name + "\n")
    file.close()
main()