/*

*/

//Name:  CSci 127 Teaching Staff
//Date:  November 2017
//A program demonstrating if-else statements in C++
#include <iostream>
using namespace std;

int main()
{
    int num;
    cout << "Hello!" << endl;
    cout << "Enter a number: ";
    cin >> num;
    /*
We start by greeting the user and reading in a number.
Since we declared the type to be int, when we read in the number,
 we do not have to cast it to an integer. 
Instead, it is converted automatically to be a whole number.
*/
    if (num % 2 == 0)
    {
        cout << "Even number!\n";
    }
    else
    {
        cout << "Odd number\n";
    }
    /*
Much of the arithmetic carries over from Python. 
The code above uses the modulo, or remainder, 
operator to test if the number entered is even or odd 
and prints a message accordingly.*/
    return 0;
}