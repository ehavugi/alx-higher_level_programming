#!/usr/bin/python3

MAX = 89
for i in range(1, MAX + 1):
    if i == 1:
        print("{:02d}".format(i), end="")
    elif (i % 10) != (i // 10) and (i % 10) > (i // 10):
        print(",{:02d}".format(i), end="")
print("")
