#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_d = abs(number) % 10
if number < 0:
    print(f"Last digit of {number} is -{l_d} and is less than 6 and not 0")
if l_d > 5 and number > 0:
    print(f"Last digit of {number} is {l_d} and is greater than 5")
elif l_d == 0:
    print(f"Last digit of {number} is {l_d} and is 0")
else:
    print(f"Last digit of {number} is {l_d} and is less than 6 and not 0")
