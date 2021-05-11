import geocoder
import folium

g = geocoder.ip('me')

myLocation = g.latlng

myMap = folium.Map(location=myLocation)

folium.Marker(myLocation).add_to(myMap)

myMap.save("myLocation.html")
