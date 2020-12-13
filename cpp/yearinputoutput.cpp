/*

*/

//Another C++ program, demonstrating variables
#include <iostream>
using namespace std;

int main()
{
    int year;
    cout << "Enter a number: ";
    cin >> year;
    cout << "Hello" << year << "!!\n\n";
    return 0;
}

/*
For each variable, we need to specify what type of variable it is
 (whole number, real number, character, etc.) before we use it. 
 For real numbers, we can use float, as in Python. 
 We will introduce more data types next lab, but if you are curious, 
 here is a chart of some common types. Our program above:

Declares the variable year to be a whole number (integer).
Asks the user for a number.
Reads in the number the user entered and stores it in year.
Prints out a messsage with that number.
Ends the function (returning 0).
To summarize: cin is for input to the program, and cout is output 
from the program.
*/