def meow(n:int) -> str:
    return ("meow\n") * n
number : int = int(input("Number: "))
#if i used only input without int the input is going to take string always
print(meow(number))