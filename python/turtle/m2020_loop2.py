import turtle
t = turtle.Turtle()

num = 5
for i in range(num):
    if i % 2 == 0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)