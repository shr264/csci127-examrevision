/*
 Assume the coastline erodes 1.5% each year. Write a complete C++ program that asks
the user for the starting elevation and computes the number of years it will take until the
coast is under water (sea level is considered to be 0).
Answer Key:


*/

#include <iostream>
using namespace std;
int main()
{
    cout << "Please enter the initial elevation in ft: ";
    double elevation = 0;
    cin >> elevation;
    int years = 0;
    while (elevation >= 0)
    {
        cout << elevation << endl;
        elevation = elevation - 0.015;
        years++;
    }
    cout << "It will take " << years << " years until the coast is under water.\n";
    return 0;
}