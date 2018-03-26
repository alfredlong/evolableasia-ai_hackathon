from .cache_services import CacheService
from django.conf import settings


class InviteService:
    @staticmethod
    def prepare_game(game_rule, session_id):
        game_rule_cache = CacheService.get(settings.GAME_RULE_CACHE_PREFIX, session_id)
        if not game_rule_cache:
            CacheService.set(settings.GAME_RULE_CACHE_PREFIX, session_id, game_rule)
            return True
        return False

