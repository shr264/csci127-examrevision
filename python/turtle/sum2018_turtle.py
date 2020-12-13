import turtle
tess = turtle.Turtle()
tess.shape("turtle")
def ramble(t,side):
    if side == 0:
        t.stamp()
    else:
        for i in range(side):
            t.forward(50)
            t.left(360/side)


#ramble(tess,0)
ramble(tess,8)