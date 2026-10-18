import cowsay
import sys
while True:
    if len(sys.argv) == 2:
      cowsay.cow("Hello, "+ sys.argv[1]) # cowsay wants the whole string to work properly, so we concatenate the greeting and the name
      break
    else:
      print("enter a single argument")
"""
.venv) macbook@NH-BD-LT-1006 packages % python say.py Aradyika
  _______________
| Hello, Aradyika |
  ===============
               \
                \
                  ^__^
                  (oo)\_______
                  (__)\       )\/\
                      ||----w |
                      ||     ||
"""
