import math
import sys
import random


class StrategyService(object):
    @staticmethod
    def do_random_search(game_status):
        free_points = game_status.strategy.free_points
        # is empty
        if not free_points:
            return [0, 0]
        fire_point = random.choice(free_points)
        return fire_point

