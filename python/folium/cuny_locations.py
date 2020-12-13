##Let's use Pandas to read in the file. We will need to import pandas and folium:

import folium
import pandas as pd
##To read in the CSV file, we'll use pandas' CSV reader. We'll print out the campus locations to make sure that all were read in:

cuny = pd.read_csv('CUNYcampuses.csv')
print(cuny["Campus"])
##Note: we saved our CSV file to cunyLocations.csv. If you saved it to a different name, change the input parameters for read_csv() to the name of your file.
##Next, let's set up a map, centered on Hunter College:

mapCUNY = folium.Map(location=[40.768731, -73.964915])
##We need to add markers for each campus. We're going to iterate through the rows of dataframe to create the markers:

for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)
##For each row in the file, we find the latitude, longitude, and name of the campus, and use those to create a new marker which we add to our map. We repeat for each row, until we have made markers for all 23 campuses in the file.
##Lastly, let's save our map:

mapCUNY.save(outfile='cunyLocations.html')
## To view your map, open a browser. From the browser, open the file: cunyLocations.html.