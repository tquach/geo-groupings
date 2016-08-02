import unittest

from geogroups.geopoints import Grouping
from geogroups.model import Point


class GroupingTest(unittest.TestCase):
    def test_empty_points(self):
        grouping = Grouping([])
        b = grouping.group_by_proximity(0)
        self.assertEqual(len(b), 0)

    def test_partition(self):
        grouping = Grouping([Point('a', 46.290001, -63.121111)])
        b = grouping.group_by_proximity(1)
        self.assertEqual(len(b), 1)
