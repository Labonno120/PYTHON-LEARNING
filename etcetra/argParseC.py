import sys
import argparse
#creates a argumentparser
parser = argparse.ArgumentParser()
#tells python to expect the -n option
parser.add_argument("-n")
#access the value supplied after -n
args = parser.parse_args()

for i in range(int(args.n)):
    print("meow")