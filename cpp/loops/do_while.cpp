//Demonstrates do-while loops
#include <iostream>
using namespace std;

int main()
{
    int num;
    do
    {
        cout << "Enter an even number: ";
        cin >> num;
    } while (num % 2 != 0);

    cout << "You entered: "
         << num << ".\n";
    return 0;
}