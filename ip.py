import geocoder
import folium

g = geocoder.ip('96.242.156.156')

myLocation = g.latlng

myMap = folium.Map(location=myLocation)

folium.Marker(myLocation).add_to(myMap)

myMap.save("myLocation.html")
