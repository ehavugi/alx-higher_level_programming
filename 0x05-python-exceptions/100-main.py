#!/usr/bin/python3
safe_print_integer = __import__('100-safe_print_integer_err').safe_print_integer_err

value = 98
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value  = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
