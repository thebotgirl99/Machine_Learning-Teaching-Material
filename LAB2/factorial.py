# -*- coding: utf-8 -*-
"""
@author: Devasena

Write a program which can compute the factorial of a given numbers by taking input from the user

"""

"1. You can use recursive functions to easily solve factorials"
def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

number = int(input("enter the number you want to compute the factorial for:"))
if number < 0:
    print("factorial for negative numbers does not exist")
elif number == 0:
    print("1")
else:
    print(factorial(number))

"2. or you can directly use the math library"
import math

number = int(input("enter the number you want to compute the factorial for:"))
if number < 0:
    print("factorial for negative numbers does not exist")
elif number == 0:
    print("1")
else:
    answer = math.factorial(number)
    print(answer)

