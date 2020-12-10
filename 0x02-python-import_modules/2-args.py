#!/usr/bin/python3
import sys
number = len(sys.argv) - 1
if number == 0:
    print("0 arguments.")
else:
    if number == 1:
        print("1 argument:")
        print("1: {}:".format(sys.argv[number]))
    if number > 1:
        print("{} arguments".format(number))
        for x in range(number):
            print("{}: {}".format(x + 1, sys.argv[x + 1]))
