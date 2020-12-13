"""
Imported the pandas library that contains structures and functions for organizing and visualizing data. We also imported the pyplot library which pandas uses to create figures.
It read in a CSV file, containing NYC population historical data.
It displayed the data as a visual plot of years versus borough populations.
The last line shows the figure you created in a separate graphics window.
"""

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
##Before going on, let's print out the variable pop. It is a dataframe, described in the reading above:

print(pop)
##The last line of our first pandas program is:
pop.plot(x="Year")