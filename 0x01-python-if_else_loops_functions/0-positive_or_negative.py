#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    n_type = "positive"
elif number == 0:
    n_type = "zero"
else:
    n_type = "negative"
print(f"{number} is {n_type}")
