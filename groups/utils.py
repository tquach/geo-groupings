from math import radians, cos, sin, asin, sqrt

# Radius of earth in kilometers.
EARTH_RADIUS = 6371


def circle_distance(p1, p2):
    """
    Given two geometric points, calculate the haversine distance
    between two points on the earth as decimal degrees.
    """
    # longitude is x coord, latitude is y coord
    lon1, lat1, lon2, lat2 = map(radians, [p1.x, p1.y, p2.x, p2.y])

    # use haversine formula
    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1
    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return c * EARTH_RADIUS


def partition(arr, n):
    """ Partitions an array in n-sized groups.
    """
    return [arr[i::n] for i in xrange(n)]