import numpy as np

def haversine(th):
    return np.sin(th/2)**2

def havlaw(lon1, lat1, lon2, lat2, radius):
    hav_central_angle = haversine(lat2 - lat1) + np.cos(lat1)*np.cos(lat2)*haversine(lon2 - lon1)
    return 2*radius*np.arcsin(np.sqrt(hav_central_angle))