import json
from math import radians, cos, sin, sqrt, atan2, degrees

from geogroups import utils


class Point(object):
    def __init__(self, id, lat, lon):
        self.id = id
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return str.format("id={}, lat={}, lon={}", self.id, self.lat, self.lon)


class Group(object):
    def __init__(self, points):
        self.points = points
        self.centroid = self._virtual_centroid()

    def update(self, points):
        prev_center = self.centroid
        self.points = points
        self.centroid = self._virtual_centroid()
        return utils.euclidean_distance(prev_center, self.centroid)

    def as_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def _virtual_centroid(self):
        x = 0.0
        y = 0.0
        z = 0.0

        total_points = len(self.points)
        for p in self.points:
            lat = degrees(p.lat)
            lon = degrees(p.lon)
            x += cos(lat) * cos(lon)
            y += cos(lat) * sin(lon)
            z += sin(lat)

        x = float(x / total_points)
        y = float(y / total_points)
        z = float(z / total_points)

        clon = atan2(y, x)
        central_sqrt = sqrt(x * x + y * y)
        clat = atan2(z, central_sqrt)
        return Point('centroid', radians(clat), radians(clon))

    def __str__(self):
        return str.format("Group[centroid={}, points={}]", self.centroid, self.points)