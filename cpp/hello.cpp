//Name:  Your name here
//Email:  Your email here
//Date:  November 2019
//My first program in C++

/*
These two lines include commands that allow you to print to the screen 
and read input that the user has entered, using standard names and defintions.
 The #include statement is similar in functionality to the import statements
  in Python.
*/

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

/*
Code in C++ programs occurs in functions. Each program is expected to 
have a main() function that is called (invoked) when the program is run.
 The int before the function name is what type of data is returned
  when the function ends. 
In this case, the function will return an int or integer value.
*/
int main() //C++ programs all have a main() function
{
    /*
C++ uses the curly brackets ('{' and '}') to indicate blocks of code, 
instead of indenting. Indenting code is considered good style, 
but you have more freedom to decide how much to indent versus Python.
 For function definitions and multiple lines of code in a block, 
 the use of the brackets is required.


cout << is used for printing to the terminal. Note that, as a general rule, 
commands in C++ end in a semi-colon.
*/
    cout << "Hello, World!"; //Print "Hello, World!" to the terminal
                             /*
When this function ends, it returns the integer 0,
 a common value for a program ending normally.
*/

    return 0; //Standard way to end function

    /*
The closing bracket for the definition of the function, main(). 
All opening brackets must have a matching closing bracket.
*/
}

/*
Once you have it typed in and saved as hello.cpp, 
try compiling the program. In a terminal window, t
ravel to the directory where you saved your file and type:

g++ hello.cpp -o hello
When it returns without an error, you can run it by typing:
./hello

*/