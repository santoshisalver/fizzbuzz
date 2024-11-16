# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:30:11 2024

@author: santo
"""

def fizzBuzz(r):
    for i in range(1, r):  # Loop through numbers from 1 to r-1
        if i % 3 == 0 and i % 5 == 0:  # Check if i is divisible by both 3 and 5
            print(str(i) + "=FizzBuzz")
        elif i % 3 == 0:  # Check if i is divisible by 3
            print(str(i) + "=Fizz")
        elif i % 5 == 0:  # Check if i is divisible by 5
            print(str(i) + "=Buzz")
        else:
            print(str(i))  # If not divisible by 3 or 5, just print the number

fizzBuzz(51)
