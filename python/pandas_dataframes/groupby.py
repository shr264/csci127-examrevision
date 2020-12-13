#Import libraries.
import pandas as pd

#Read in the csv file.
rain = pd.read_csv('AustraliaRain.csv')

#Group the data by location averages.
groupAvg = rain.groupby('Location').mean()

#Print the average rainfall at each location.
print(groupAvg['Rainfall'])

## same thing but in a single line
#Group the data by location averages and print the average rainfall at each location.
print(rain.groupby('Location').mean()['Rainfall'])

##Finally, to retrieve the data for a particular location, for example "Albury", we can use groupby() along with get_group().
#Group the data by location get averages for group Albury.
alburyAvg = rain.groupby('Location').get_group('Albury').mean()

#Print the average rainfall.
print(alburyAvg['Rainfall'])

##This will output a single number: the average rainfall in "Albury"