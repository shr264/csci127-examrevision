"""
Python has a built-in library for generating random numbers. To use it, you include at the top of your file:
import random
The random library includes a function that's similar to range, called randrange. As with range, you can specify the starting, stopping, and step values, and the function randrange chooses a number at random in that range. Some examples:
random.randrange(5) returns one of 0,1,2,3,4
random.randrange(1,10,2) returns one of 1,3,5,7,9
random.randrange(360) returns one of 0,1,2,...,359
"""

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)