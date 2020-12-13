"""

Let's look at some of the shades of red that are available. Here's our plan (or pseudocode):

Create a turtle, tess.
For 10, 20, 30, ..., 250,
   Move forward 10 steps
   Make the turtle a bit larger each time
   Make the turtle a bit more red each time
Let's change each piece of our "To Do" list into Python code:
Create a turtle, tess.
We've done this before. We import the turtle module and set up the turtle. One new thing we need to do, is to tell the turtle library that we would like to represent colors as decimal numbers:
"""

# A program that demonstrates the shades of red
# Fall 2017

import turtle  # Import the turtle drawing package

turtle.colormode(255)  # Allows colors to be given as 0...255
tess = turtle.Turtle()  # Create a turtle##
# To keep our drawing from running off the screen, we'll move tess backwards before we start our loop:

tess.backward(100)  # Move her backwards, to give more space to draw
# For 10, 20, 30, ..., 250,
# This can be done with a for-loop and a range that starts at 10, stops at 255, and steps up by 10 each time:

for i in range(0, 255, 10):
    # Move forward 10 steps
    tess.forward(10)  # Move forward
    # Make the turtle a bit larger each time
    tess.pensize(i)  # Set the drawing size to be i (larger each time)
    # Make the turtle a bit more red each time
    tess.color(i, 0, 0)  # Set the red channel to be i (brighter each time)
