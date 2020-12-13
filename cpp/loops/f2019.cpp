//Quote by Grace Hopper
#include <iostream>
using namespace std;
int main()
{
    cout << "One accurate measurement ";
    cout << "is \nworth a thousand ";
    cout << "expert ";
    cout << "opinions. " << endl
         << "G.H.";
    return 0;
}

/*
Answer Key:
One accurate measurement is
worth a thousand expert opinions.
G.H.
*/

#include <iostream>
using namespace std;
int main()
{
    double num = 0;
    double tot = 0;
    while (tot < 10)
    {
        cout << "Please enter amount\n";
        cin >> num;
        tot += num;
    }
    cout << tot << endl;
    return 0;
}

/*
Given the input: 5, 3, 4

Answer Key:
Please enter amount
Please enter amount
Please enter amount
12
*/

#include <iostream>
using namespace std;
int main()
{
    int i, j;
    for (i = 1; i < 5; i++)
    {
        for (j = 0; j < i; j++)
        {
            if (j % 2 == 0)
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
X
XO
XOX
XOXO
*/