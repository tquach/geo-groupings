import json

import numpy
from scipy.spatial import distance
from sklearn.cluster.k_means_ import KMeans

from geogroups import logger
from geogroups.model import Point


def from_file(filename):
    logger.debug("Opening file %s", filename)
    with open(filename, 'rb') as f:
        contents = json.load(f)

    geopoints = [Point(node['id'], float(node['lat']), float(node['lon'])) for node in contents]
    return geopoints


class Grouping(object):
    def __init__(self, points):
        self.points = points

    def group_by_proximity(self, k=10):
        if len(self.points) == 0:
            return {}

        X = numpy.array([[p.lat, p.lon] for p in self.points])

        distance_matrix = distance.squareform(distance.pdist(X))
        db = KMeans(n_clusters=k).fit(distance_matrix)

        # re-attach ids
        grouped_points = {}
        for i, k in enumerate(db.labels_):
            logger.debug('idx, label [%s, %s]', i, k)
            if k not in grouped_points:
                grouped_points[k] = []
            point = self.points[i]
            grouped_points[k].append({'id': point.uid, 'lat': point.lat, 'lon': point.lon})

        logger.info('Finished grouping into %d groups.', len(grouped_points))
        return grouped_points

    def _group_by_dbscan(self, eps=1.5):
        # use haversine function for distance calculation
        # eps /= EARTH_RADIUS
        # df = pd.read_json('./test/_data/airports.small.json')
        # coords = df.as_matrix(columns=['lat', 'lon'])
        # db = DBSCAN(eps=eps, min_samples=1, algorithm='ball_tree', metric='haversine').fit(numpy.radians(coords))
        raise NotImplementedError("Unimplemented.")
