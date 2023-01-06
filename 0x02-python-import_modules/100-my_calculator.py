#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys

if __name__ == "__main__":
    if (len(sys.argv)) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = {
        "+": add,
        "-": sub,
        "/": div,
        "*": mul
        }
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator in ops.keys():
        print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
