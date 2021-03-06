import xml.etree.ElementTree as ET
import pandas as pd
import gpxpy as gpx
import numpy as np
import math
import datetime as dt
import haversine as h
import unwrap_list as ul


#Constants
def EARTH_RADIUS():
    return 6378137

def trackpoints(filepath):
    #Extract data from xml formatted .gpx file
    ns = {'ns': 'http://www.topografix.com/GPX/1/1'}
    tree = ET.parse(filepath)
    root = tree.getroot()
    trkpts = (root
                  .find('ns:trk', ns)
                  .find('ns:trkseg', ns)
                  .findall('ns:trkpt', ns))
    return trkpts

trkpts = trackpoints("C:\\Users\\Daniel\\Desktop\\4th_real_pace5_20_1_25km.gpx")
data_len = len(trkpts)

# TODO(DANIEL): Implement ignoring date if no change in date through file
'''
fst_pt = trkpts[0].find('ns:time', ns).text.split('T')
fst_dt = fst_pt[0].split('-')
lst_pt = trkpts[-1].find('ns:time', ns).text.split('T')
lst_dt = lst_pt[0].split('-')
not_same_date = 0
for i, j in fst_dt, lst_dt:
    if i != j:
        not_same_date = 1
        break
'''

'''
Unwraps data into an array
Indexes of array
Position
0, 1, 2: Longitude, Latitude, Elevation
Date
3, 4, 5: Year, Month, Day
Time
6, 7, 8: Hours, Minutes, Seconds
'''
pts = np.zeros((data_len, 9))
for ind, pnt in enumerate(trkpts):
    pts[ind, 0] = pnt.attrib['lon']
    pts[ind, 1] = pnt.attrib['lat']
    pts[ind, 2] = pnt.find('ns:ele', ns).text
    date_time = pnt.find('ns:time', ns).text.split('T')
    date = [float(i) for i in date_time[0].split('-')]
    time = [float(i) for i in date_time[1][:-1].split(':')]
    pts[ind, 3:6] = date
    pts[ind, 6:] = time

#Calculates the total time assuming ordered points
first_pt_dt = ul.unwrap(dt.datetime, [int(i) for i in pts[0, 3:]])
last_pt_dt = ul.unwrap(dt.datetime, [int(i) for i in pts[-1, 3:]])
total_time = last_pt_dt - first_pt_dt

#Computes Statistical data for the elevation markers
elevation_arr = pts[:, 2].copy()
std_elevation = np.std(elevation_arr)
mean_elevation = np.mean(elevation_arr)
min_elevation = min(elevation_arr)
max_elevation = max(elevation_arr)
std_elevation_percentage = std_elevation/(max_elevation - min_elevation)
elevation_arr -= mean_elevation
elevation_arr /= std_elevation

# will assume flat surface and no elevation to begin with
my_list = []
pos = np.radians(pts[:,:2].copy())
for i in range(data_len - 1):
    my_list.append(h.havlaw(pos[i, 0], pos[i, 1], pos[i + 1, 0], pos[i + 1, 1], EARTH_RADIUS()))
print('')

for i in range(data_len):
    pass


'''Inaccurate
dif_pos = np.cos(pos[1:, :] - pos[:-1, :])
my_list2 = np.arccos(dif_pos[:,1]*dif_pos[:,0])*EARTH_RADIUS
'''

#displays something


