#include <iostream>
using namespace std;

int main()
{
    int number;
    cout << "Enter number: ";
    cin >> number;
    if ((number > 0 && number < 4) || number > 10)
    {
        cout << "A" << endl;
    }
    else if (number > 3 && number < 6)
    {
        cout << "B" << endl;
    }
    else if (number > 6 && number < 9)
    {
        cout << "C" << endl;
    }
    else
    {
        cout << "D" << endl;
    }
    return 0;
}