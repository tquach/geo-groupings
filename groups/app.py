import logging
from pprint import pprint

import math
from shapely import geometry as geo
from shapely.geometry import LineString

from groups import utils

DEFAULT_PROXIMITY_DISTANCE = 10.0

class GroupingService(object):
    """ The GroupingService is responsible for partitioning a group of points by proximity.
    """

    def __init__(self, geodata, proximity_factor=DEFAULT_PROXIMITY_DISTANCE):
        self.logger = logging.getLogger(__file__)
        self.proximity_factor = proximity_factor
        self.geopoints = [{'id': node["id"],
                           'point': geo.Point(float(node["lon"]), float(node["lat"]))} for node in geodata]

    def group_by_proximity(self, num_groups):
        """ Group the set of points by proximity and return a list of lists of ids.
        """
        return self._group(num_groups, self.geopoints)

    def _group(self, num_groups, points):
        if len(points) == 1:
            return points
        elif len(points) == 2:
            p1 = points[0]
            p2 = points[1]
            if p1['point'].buffer(100.0).contains(p2['point']):
                self.logger.info("Found 2 nearby points")
                return [[p1, p2]]
            else:
                self.logger.info("Too far away")
                return [[p1], [p2]]
        else:
            self.logger.info("Partitioning in half ...")
            partitions = utils.partition(points, 2)
            left = self._group(1, partitions[0])
            right = self._group(1, partitions[1])

            # print "LEFT ", left
            # print "RIGHT", right

            return [left, right]

        #     p1.buffer()
        # p1 = geo.Point((-60.952436,-18.815953))
        # # p2 = geo.Point((-59.084514,-18.431761))
        # p2 = geo.Point(( -56.882002,-16.328691))
        # # p2 = geo.Point((-52.048018, -7.305926))
        # print p1.buffer(1.0).contains(p2), utils.circle_distance(p1, p2)
        # print p1.buffer(2.0).contains(p2)
        # print p1.buffer(3.0).contains(p2)
        # print p1.buffer(4.0).contains(p2)
        # print p1.buffer(5.0).contains(p2)
