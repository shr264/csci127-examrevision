import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

## Each column in the original spreadsheet is a column, or series. We can look at the column for the Bronx with:

print(pop['Bronx'])
##How would you look at the one for Brooklyn?
##A nice thing about series is that you can do basic arithmetic with them. For example,
print(pop['Bronx']*2)
##prints out double the values in the column.
##You can also use multiple columns in a calculation:
print(pop['Bronx']/pop['Total'])
##prints out the fraction of the total population that lives in the Bronx.
##We can save that series by creating a new column for it:
pop['Fraction'] = pop['Bronx']/pop['Total']
##We can save that series by creating a new column for it:
pop['Percentage'] = 100*pop['Bronx']/pop['Total']
#and then can use it to create a new graph:
pop.plot(x = 'Year', y = 'Fraction')
#We can save it to a file, by storing the current figure (via "get current figure" or gcf() function and then saving it:
fig = plt.gcf()
fig.savefig('fractionBX.png')