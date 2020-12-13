/*
The number of Instagram monthly active users grew from ∼130 million in 2013 to ∼1000
million (1 billion) in 2019. The average annual growth rate can then be estimated as
avgGrowth = %growth
number-of-years =
100 ·
1000−130
130
2019 − 2013
= 134%
We can thus estimate the average annual growth: avgGrowth = 134%.
Write a complete C++ program that asks the user for a year greater than 2013 (assume
user complies) and prints the estimated number (in millions) of monthly active Instagram
users in that year.
*/

//Instagram monthly active users V1
#include <iostream>
using namespace std;
int main()
{
    double past = 130;
    double avgGrowth = past * 1.34;
    int year = 0;
    cout << "Please enter a year between 2013 and 2018: ";
    cin >> year;
    double users = (past + (avgGrowth * (year - 2013))) / 12;
    cout << "The number of Social Network users in ";
    cout << year << " is approximately " << users;
    cout << " billions" << endl;
    return 0;
}