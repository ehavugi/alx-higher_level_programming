#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    n_type = "is positive"
elif number == 0:
    n_type = "is zero"
else:
    n_type = "is negative"
print(f"{number} is {n_type}")
