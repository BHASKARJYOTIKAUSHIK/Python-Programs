import folium
map=folium.Map(location=[26.7460, 94.2485],zoom_start=16)
folium.CircleMarker(location=[26.7460, 94.2485],radius=50)

map.save("maph1.html")

