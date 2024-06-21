import folium
import folium.map 
#folium needed
#pip install folium 
fg=folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(data=(open("india_states.json","r",encoding="utf-8-si").read())))
map=folium.map(Location=[20000,75000],zoom_start=4)
map.add
