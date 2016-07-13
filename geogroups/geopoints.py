import json
import random

from geogroups import logger, utils
from geogroups.model import Point, Group


def from_file(filename):
    logger.debug("Opening file %s", filename)
    with open(filename, 'rb') as f:
        contents = json.load(f)

    geopoints = [Point(node['name'], node['lat'], node['lon']) for node in contents]
    return geopoints


def group_by(points, size, resolution=1.5):
    seeds = random.sample(points, size)
    buckets = [Group([p]) for p in seeds]

    cnt = 0
    while True:
        groups = [[] for b in buckets]
        bucket_size = len(buckets)
        cnt += 1

        for p in points:
            min_distance = utils.euclidean_distance(p, buckets[0].centroid)
            min_idx = 0

            for i in range(bucket_size - 1):
                distance = utils.euclidean_distance(p, buckets[i + 1].centroid)
                if distance < min_distance:
                    min_distance = distance
                    min_idx += 1

            groups[min_idx].append(p)

        dmax = 0.0
        for i in range(bucket_size):
            if len(groups[i]) == 0:
                continue
            ddist = buckets[i].update(groups[i])
            dmax = max(dmax, ddist)

        if dmax < resolution:
            logger.debug('all done')
            break
    return buckets
