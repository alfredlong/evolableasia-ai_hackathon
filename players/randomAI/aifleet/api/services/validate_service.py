from .cache_services import CacheService
from django.conf import settings
from api.domains.strategy import Strategy
from random import randint
from .strategy_service import StrategyService


class ValidateService(object):

    @staticmethod
    def validate_game_rule(game_rule_data):
        # TODO validate
        return True
