#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = last_digit - 10
if last_digit > 5:
    n_type = "greater than 5"
elif last_digit == 0:
    n_type = "0"
else:
    n_type = "less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} and is {n_type}")
