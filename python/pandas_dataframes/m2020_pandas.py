import pandas as pd 

fires =pd.read_csv('amazonFires.csv', encoding = "ISO-8859-1")

# number of data points for each date , i.e. how many rows does each unique value of date have in the dataframe?

print(fires['date'].value_counts())

# group the data by state and print the maximum number of fires in each state
groupBy = fires.groupby('state')
groupMax = groupBy.max()
print(groupMax['number'])

## OR

print(fires.groupby('state').max()['number'])

# with the grouped data, print the average number of fires in Alagoas

Alagoas = groupBy.get_group('Alagoas').mean()
print(Alagoas['number'])

## OR

print(fires.groupby('state').get_group('Alagoas').mean()['number'])
