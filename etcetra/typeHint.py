def meow(n:int) -> str:
    """ showing that the function should return string type"""
    return ("meow\n") * n
number : int = int(input("Number: "))
#if i used only input without int the input is going to take string always
print(meow(number))
print(meow.__doc__)# showing docstring of function meow