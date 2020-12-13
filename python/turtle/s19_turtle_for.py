import turtle
tori = turtle.Turtle()
def mystery(tina, n):
    for i in range(n):
        tina.left(90)
        tina.forward(50)
        tina.right(90)
        tina.forward(50)

mystery(tori, 3)