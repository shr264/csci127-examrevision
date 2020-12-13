/*
convert to c++
age = int(input('Please enter age: '))
while age < 0:
    print('Entered a negative number.')
    age = int(input('Please enter age: '))
print('You entered your age as:', age)
*/

#include <iostream>
using namespace std;

int main()
{
    int age; //The index variable for the loop
    cout << "Please enter age: " << endl;
    cin >> age;

    //Loop will repeat 10 times:
    while (age < 0)
    {
        cout << "Entered a negative number." << endl;
        cout << "Please enter age: " << endl;
        cin >> age;
    }

    cout << "You entered your age as:" << age << endl;

    return 0;
}