import cowsay
import sys
while True:
    if len(sys.argv) == 2:
      cowsay.cow("hello,",sys.argv[1])
      break
    else:
      print("enter a single argument")

#(.venv) macbook@NH-BD-LT-1006 packages % python say.py Alice
 # ______
#| hello, |
 # ======
  #    Alice