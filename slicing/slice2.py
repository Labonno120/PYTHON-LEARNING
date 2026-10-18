import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    for arg in sys.argv[1:]:
        print("Hello,", arg)
#(.venv) macbook@NH-BD-LT-1006 slicing % python slice2.py Bristy Trsihna Tonmoy
#Hello, Bristy
#Hello, Trsihna
#Hello, Tonmoy