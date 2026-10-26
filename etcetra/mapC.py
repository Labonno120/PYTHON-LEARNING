def yell(*words):
    uppercased = list(map(str.upper, words))
    print(*uppercased) # unpacking list
yell("This", "is", "Bristy")