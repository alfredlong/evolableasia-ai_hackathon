from .cache_services import CacheService
from django.conf import settings
from .strategy_service import StrategyService


class ShootService(object):
    grid_search_weight = 1

    @staticmethod
    def get_game_status(session_id, turn):
        game_status = CacheService.get(settings.GAME_STATUS_CACHE_PREFIX, session_id)
        game_rule = CacheService.get(settings.GAME_RULE_CACHE_PREFIX, session_id)
        if turn is not game_status.turn + 1:
            return game_status, game_rule, False
        return game_status, game_rule, True

    @staticmethod
    def shoot(game_status, game_rule):
        strategy = game_status.strategy
        print ("current strategy.mode:", strategy.mode)
        fire_point = StrategyService.do_random_search(game_status)
        return fire_point

    @staticmethod
    def update_game_status(fire_points, game_status, session_id):
        # update game status just fired points
        game_status.turn = game_status.turn + 1

        # update free points
        for fire_point in fire_points:
            if fire_point in game_status.strategy.free_points:
                game_status.strategy.free_points.remove(fire_point)
        # update to cache
        CacheService.set(settings.GAME_STATUS_CACHE_PREFIX, session_id, game_status)

    @staticmethod
    def create_response(fire_points):
        return {'coordinates': fire_points}