//Growth example
#include <iostream>
using namespace std;

int main()
{
    int population = 100;
    cout << "Year\tPopulation\n";
    for (int year = 0; year < 100; year = year + 5)
    {
        cout << year << "\t" << population << "\n";
        population = population * 2;
    }
    return 0;
}
