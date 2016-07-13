from math import radians, cos, sin, asin, sqrt, pi

# Radius of earth in km.
EARTH_RADIUS = 6371


def circle_distance(p1, p2):
    """
    Given two geometric points, calculate the haversine distance
    between two points on the earth as decimal degrees.
    """
    # longitude is x coord, latitude is y coord
    lon1, lat1, lon2, lat2 = map(radians, [p1.lon, p1.lat, p2.lon, p2.lat])

    # use haversine formula
    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1
    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return c * EARTH_RADIUS


def euclidean_distance(p1, p2):
    lon1, lat1, lon2, lat2 = map(radians, [p1.lon, p1.lat, p2.lon, p2.lat])
    return sqrt((lon1 - lon2) ** 2 + (lat1 - lat2) ** 2)
