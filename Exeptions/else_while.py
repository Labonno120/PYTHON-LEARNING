# jotobar na integer input diba totobar ask korbe whats X?
# integer dile print kore dibe.
while True:
    try :
        X = int(input("Whats X? "))
    except ValueError:
        print("The input is not a Integer")
    else:
        print(X)
        break