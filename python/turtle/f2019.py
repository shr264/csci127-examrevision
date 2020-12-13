import turtle
tara = turtle.Turtle()
tara.shape('turtle')
def ramble(tex, side):
    if side <= 0:
        tex.stamp()
    elif side <= 10:
        for i in range(3):
            tex.left(120)
            tex.forward(20)
    else:
        tex.right(90)
        tex.forward(side)
        ramble(tex, side//2)


#ramble(tara,5)
ramble(tara,160)