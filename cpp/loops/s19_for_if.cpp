#include <iostream>
using namespace std;
int main()
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if (j == 2)
                cout << "*";
            else if (j % 2 == 0)
                cout << "X";
            else
                cout << "O";
        }
        cout << endl;
    }
    return 0;
}
/*
Answer Key:
XO*OX
XO*OX
XO*OX
XO*OX
XO*OX
*/
