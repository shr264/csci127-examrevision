#Intro Programming Lab:  A program with a herd of turtles

import turtle

def welcomeMessage():
    print()
    print("Welcome to our herd of turtles demonstration!")
    print()

def getInput():
    """
    Next, let's ask the user for the number of turtles. 
    Since the function call is on the right hand side of an equals sign, it returns a value (namely, the number of turtles) that we will use later in the program.
    """
    n = eval(input("Please enter the number of turtles: "))
    return(n)


def setUpScreen():
    """
    We still need to set up the turtle window and make it green. The turtle command to change the background color is
    bgcolor and colors can be referred by their names or the percentage of red, green, and blue ('RGB') in the color. Let's use the name to change the window color:
    """
    w = turtle.Screen()
    w.bgcolor("green")
    return w

def setUpTurtles(n):
    #Create a list of turtles
    #Make each turtle appear turtle-shaped
    #Change the color and default direction (so they don't run over each other)
    tList = []
    #Create turtles:
    for i in range(n):
        t = turtle.Turtle()
        t.shape("turtle")       #Make the turtle appear turtle-shaped
        tList.append(t)

    #Change their color from the blue default and default direction
    for i in range(n):
        tList[i].color(0,0,i/(2*n)+.5)
        tList[i].right(i*360/n)
    return tList

def moveForward(tList):
    for t in tList:
        t.forward(30)

def stamp(tList):
    for t in tList:
        t.stamp()

def main():
    welcomeMessage()            #Writes a welcome message to the shell
    numTurtles = getInput()     #Ask for number of turles
    w = setUpScreen()           #Set up a green turtle window
    turtleList = setUpTurtles(numTurtles) #Make a list of turtles, different colors
    for i in range(10):
        moveForward(turtleList) #Move each turtle in the list forward
        stamp(turtleList)       #Stamp where the turtle stopped


if __name__ == "__main__":
    main()