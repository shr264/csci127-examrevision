/*
Write a complete C++ program that prints the change in population of predator and
prey following the Lotka-Volterra model:
r = 1.5r − .2rf
f = 0.95f + .1rf
where r is the number of prey (such as rabbits) each year and f is the number of predators
(such as foxes) each year. The rabbit population increases by 50% each year, but rf
5
are eaten
by foxes. The fox population decreases by 5% due to old age but increases in proportion
to the food supply, rf
10 . Assume that the starting population of prey (rabbits) is 500 and
starting population of predators (foxes) is 10. Your program should print for the first 10
years: the year, the number of prey and the number of predators.
*/

//Predator/Prey model
#include <iostream>
using namespace std;
int main()
{
    float r = 500, f = 10;
    int year;
    cout << "Year\tPrey\tPredators\n";
    for (year = 0; year < 10; year++)
    {
        cout << "\t" << year << "\t" << r << "\t" << f << "\n";
        r = 1.5 * r - .2 * r * f;
        f = 0.95 * f + .1 * r * f;
    }
    return 0;
}