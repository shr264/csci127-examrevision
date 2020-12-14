/*
translate 

for i in range(5):
    for j in range(0,10,3):
        print(j, end=' ')
    print(i)
*/
#include <iostream>
using namespace std;

int main()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 10; j = j + 3)
        {
            cout << j << ' ';
        }
        cout << i << endl;
    }
    return 0;
}