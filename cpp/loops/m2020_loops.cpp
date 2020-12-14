#include <iostream>
using namespace std;

int main()
{
    for (int i = 0; i < 6; i++)
    {
        for (int j = 1; j < 6; j++)
        {
            if (j % 2 == 0)
            {
                cout << "0";
            }
            else
            {
                cout << "1";
            }
        }
        cout << endl;
    }

    /*

    we get 

10101
10101
10101
10101
10101
10101
    
    */

    cout << endl;
    cout << endl;
    cout << endl;

    for (int i = 0; i < 6; i++)
    {
        for (int j = 1; j < 6; j++)
        {
            if (i % 3 == 0)
            {
                cout << "0";
            }
            else
            {
                cout << "1";
            }
        }
        cout << endl;
    }

    /*

    we get 

00000
11111
11111
00000
11111
11111
    
    */

    return 0;
}
