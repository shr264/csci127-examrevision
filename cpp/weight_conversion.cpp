//Another C++ program, demonstrating I/O & arithmetic
#include <iostream>
using namespace std;

int main()
{
    float kg, lbs;
    cout << "Enter kg: ";
    cin >> kg;
    lbs = kg * 2.2;
    cout << endl
         << "Lbs: " << lbs << "\n\n";
    return 0;
}
