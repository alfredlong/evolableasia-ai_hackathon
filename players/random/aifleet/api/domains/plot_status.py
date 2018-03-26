class PlotStatus(object):
    (FREE, HIT, MISS) = ('FREE', 'HIT', 'MISS')

    def __init__(self, hit_status, has_ship, prob):
        self.hit_status = hit_status
        self.has_ship = has_ship
        self.prob = prob

    def __str__(self):
        return 'hit_status:%(hit_status)s, has_ship:%(has_ship)s' % \
               {'hit_status': self.hit_status, 'has_ship': self.has_ship}

    class Meta:
        pass


