from parent import hello
def hello_test():
    assert hello("Bristy") == "Hello, Bristy"
hello_test()

#folder structure:
"""
Unit_Test/
    parent.py
    tests/
        test_hello.py
        test_square.py
        __init__.py
"""