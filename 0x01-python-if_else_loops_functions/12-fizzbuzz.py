#!/usr/bin/python3

def fizzbuzz():
    ender = " "
    for i in range(1, 101):
        if ((i % 5) == 0) and ((i % 3) == 0):
            print("FizzBuzz", end=ender)
        elif (i % 3) == 0:
            print("Fizz", end=ender)
        elif (i % 5) == 0:
            print("Buzz", end=ender)
        else:
            print(i, end=ender)
