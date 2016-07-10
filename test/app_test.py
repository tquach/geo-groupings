import app
import os
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(BASE_DIR, "_data/points.json")

class TestApp(unittest.TestCase):
    def test_main(self):
        app.main(3, TEST_FILE)
        self.assertTrue(True)