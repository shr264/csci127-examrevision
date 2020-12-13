/*

*/

/*
C++ has for-loops that have are similar, but not identical to for-loops in Python. The basic format is:

int i;

for (i = 0; i < 10; i++)
{
   command1
   command2
   ...
}


For the loop above,

The variable i first takes on the value 0.
Next, check if the variable i < 10?
If no, leave the loop.
If yes, do the commands in the body of the loop.
Add one to the variable i (abbreviated: i++).
Go to #2.
Let's use a loop to write "Hello, World!" to the screen 10 times:

*/

//Name:  Your name here
//Email:  Your email here
//Date:  November 2019
//Prints "Hello, World!" 10 times, using a loop

#include <iostream>
using namespace std;

int main()
{
    int i; //The index variable for the loop

    //Loop will repeat 10 times:
    for (i = 0; i < 10; i++)
    {
        cout << "Hello, World!\n";
    }
    return 0;
}