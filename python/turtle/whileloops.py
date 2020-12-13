"""
We have been using for-loops to repeat tasks a fixed number of times
 (often called a definite loop). There is another type of loop that repeats while a condition holds (called a indefinite loop). The most common is a while-loop.

while condition:
   command1
   command2
   ...
   commandN
While the condition is true, the block of commands nested under the 
while statement are repeated.

For example, let's have a turtles continue their random walk as long as their x and y values are within 50
 of the starting point (to keep them from wandering off the screen):
"""

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

while (-50 < trey.xcor() < 50) and (-50 < trey.ycor() < 50):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)