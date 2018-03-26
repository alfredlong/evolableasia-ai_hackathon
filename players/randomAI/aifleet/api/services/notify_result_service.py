from .cache_services import CacheService
from django.conf import settings
from api.domains.shot_result import ShotResult
from api.domains.strategy import Strategy
from api.domains.plot_status import PlotStatus


class NotifyResultService(object):
    @staticmethod
    def get_game_status(session_id):
        game_status = CacheService.get(settings.GAME_STATUS_CACHE_PREFIX, session_id)
        # print("game status get", game_status)

        if not game_status:
            return game_status, False
        return game_status, True

    @staticmethod
    def update_result(session_id, game_status, shot_result):
        return True
