import turtle
tina = turtle.Turtle()
tina.color('#FF00FF')
n = 8
for i in range(n):
    tina.circle(50)
    tina.right(360/n)
    tina.forward(5)
