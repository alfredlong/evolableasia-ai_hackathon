class Strategy(object):
    GRID_SEARCH = 1
    TRACE_SEARCH = 2

    def __init__(self, mode, level, grid_points, tracing_points, free_points, hit_points, remain_ships):
        self.mode = mode
        self.level = level
        self.grid_points = grid_points
        self.tracing_points = tracing_points
        self.free_points = free_points
        self.hit_points = hit_points
        self.remain_ships = remain_ships

    class Meta:
        pass
