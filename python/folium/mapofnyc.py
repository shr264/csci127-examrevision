##Let's make another map, focused on New York City. To do that, when we set up the map object, 
##we need to reset the location to New York City and the increase the zoom level:

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

##Let's add in a marker for Hunter College:
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

##and create the .html file:
mapCUNY.save(outfile='nycMap.html')