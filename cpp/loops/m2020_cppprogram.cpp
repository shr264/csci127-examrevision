/*
zoom users grow by 2.1 daily
*/

#include <iostream>
using namespace std;

int main()
{
    float projected_users;
    float zoom_users = 10;
    int num_days = 0;

    cout << "\nPlease enter the amount > 10 in millions: ";
    cin >> projected_users;

    while (zoom_users < projected_users)
    {
        zoom_users = zoom_users + 2.1;
        num_days = num_days + 1;
        cout << "It takes " << num_days << " for Zoom to reach " << zoom_users << " millions users." << endl;
    }

    return 0;
}