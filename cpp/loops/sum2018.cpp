//Pluses and minuses
#include <iostream>
using namespace std;
int main()
{
    int i, j;
    for (i = 1; i <= 5; i++)
    {
        for (j = 1; j <= 5; j++)
            if ((i + j) % 2 == 0)
                cout << "+";
            else
                cout << "-";
        cout << endl;
    }
}
/*
Answer Key:
+-+-+
-+-+-
+-+-+
-+-+-
+-+-+
*/