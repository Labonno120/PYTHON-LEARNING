import sys
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    print("Hello, ", sys.argv[1])

#(.venv) macbook@NH-BD-LT-1006 Libraries % python sys_Lib.py Bristy
#Hello,  Bristy