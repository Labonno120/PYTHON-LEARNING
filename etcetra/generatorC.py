#normal code
def numbers():
    yield 1
    yield 2
    yield 3
def main():
    g = numbers()# creating objects
    print(next(g))# requesting one value at a time
    print(next(g))
    print(next(g))
    for i in numbers():
        print(i) #for loop automatically requests so we dont need next()
main()