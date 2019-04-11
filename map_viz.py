import osmapi
import unwrap_list as ul
from matplotlib import pyplot as pl
import numpy as np

OSM = osmapi.OsmApi()

bbox = [-73.566127, 45.444115, -73.539026, 45.453433]

raw_data = ul.unwrap(OSM.Map, bbox)
map_data = raw_data

for i in range(len(map_data) - 1, -1, -1):
    if map_data[i]['type'] == 'node':
        del map_data[i]


lon = np.array([])
lat = np.array([])
for ind, dic in enumerate(map_data):
    print(dic['data'])
    pass

lon = [1]
lat = [1]
pl.scatter(lon, lat)
pl.show()
