#https://python-visualization.github.io/folium/quickstart.html
import folium

m = folium.Map(location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13)

folium.Circle(
    radius=100,
    location=[45.5244, -122.6699],
    popup="The Waterfront",
    color="crimson",
    fill=False,
).add_to(m)

folium.CircleMarker(
    location=[45.5215, -122.6261],
    radius=50,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.PolyLine(
    locations=[[45.5215, -122.6261],[45.5215, -122.7261]], color='#FF0000'
).add_to(m)

m.save("index.html")