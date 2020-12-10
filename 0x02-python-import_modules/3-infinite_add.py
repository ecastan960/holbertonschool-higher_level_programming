#!/usr/bin/python3
import sys
number = len(sys.argv) - 1
add = 0
if number == 0:
    print("0")
elif number == 1:
    print(sys.argv[number])
else:
    for x in range(number):
        add = add + int(sys.argv[x + 1])
    print(add)
