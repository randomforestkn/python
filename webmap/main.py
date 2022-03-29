from folium import Map, FeatureGroup, Marker, Icon, CircleMarker, GeoJson, LayerControl
from pandas import read_csv


def color_producer(el):
    if el <= 1000:
        return 'green'
    elif el <= 2000:
        return 'orange'
    else:
        return 'red'

# create a map object
map = Map(location=[40.635892788767315, 22.94481275429977])

# add point to the map
fgv = FeatureGroup(name="Ηφαίστεια")


# read the file with pandas
data = read_csv("Volcanoes_USA.txt")

# convert a column from file to a python list
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

# use zip function to iterate two lists at a same time
# create dynamic popup message
for lt, ln, el in zip(lat, lon, elev):
        # fg.add_child(Marker(location=[lt,ln], popup=f"{el} m", icon=Icon(color=color_producer(el), prefix='fa' ,icon='circle')))
        fgv.add_child(CircleMarker([lt, ln],
    radius=10,
    popup=f"{el} m",
    color='grey',
    fill=True,
    fill_color=color_producer(el),
    fill_opacity=0.7,
    parse_html=False))

fgp = FeatureGroup(name="Πληθυσμός")


# add polygon layer to the map
fgp.add_child(GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

# add a layer control panel
map.add_child(LayerControl())


# convert the python object to html
map.save("map1.html")
