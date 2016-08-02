class Point(object):
    def __init__(self, uid, lat, lon):
        self.uid = uid
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return str.format("id={}, lat={}, lon={}", self.id, self.lat, self.lon)
