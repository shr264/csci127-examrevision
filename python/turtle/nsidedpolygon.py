#A program that demonstrates turtles stamping

import turtle

taylor = turtle.Turtle()
taylor.color("purple")
taylor.shape("turtle")

n = 20

for i in range(n):
  taylor.forward(30)
  taylor.stamp()
  taylor.left(360/n)