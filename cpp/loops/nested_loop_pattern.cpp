//Another C++ program; Demonstrates loops
#include <iostream>
using namespace std;

int main()
{
    int i, j, size;
    cout << "Enter size: ";
    cin >> size;
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
            cout << "*";
        cout << endl;
    }
    cout << "\n\n";
    for (i = size; i > 0; i--)
    {
        for (j = 0; j < i; j++)
            cout << "*";
        cout << endl;
    }
    return 0;
}
