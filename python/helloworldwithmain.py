"""
Using Python from the Command Line Interface
In addition to IDLE (and other development environments with graphical interfaces), Python can also be used directly from the command line. 
In fact, this is what the grading scripts do to evaluate your programs, since Gradescope uses a remote cloud server and does not have a graphics window.

To start, we need a command line interface (aka a terminal window). To launch the terminal, click on the terminal window icon in the left menu, 
or go to search option in the upper left corner and type and then open terminal.

In Lab 1, we launched IDLE from the terminal by typing:

$ idle3
We can use Python in a similar fashion. In a terminal window, change directories to where you stored your hello program above 
(see Lab 4 for changing directories at the command line).

Let's run your hello program from the command line. If your program is called hello.py, you would type at the command line:

$ python helloworldwithmain.py
Notice that the output goes directly to the terminal window. Try running other programs you have written from the command line.
"""


#Name:  your name here
#Date:  October 2017
#This program, uses functions, says hello to the world!

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()