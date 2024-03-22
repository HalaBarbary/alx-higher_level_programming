#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number[-1] > 5:
    print(f"last digit of {number} is {number[-1]} and is greater than 5")
elif number[-1] == 0:
    print("last digit of {:d} is {:d} and is 0".format(number, number[-1]))
else:
    print(f"last digit of {number} is {number[-1]} and is less than 6 and not 0")
