from parent import square
def main():
    test_square()
def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
main()
 #assert square(-3) == 9
#AssertionError