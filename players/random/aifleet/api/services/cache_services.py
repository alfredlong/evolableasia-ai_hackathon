from django.core.cache import cache
from django.conf import settings


# cache
class CacheService(object):
    @staticmethod
    def set(prefix, key, data):
        print("cache=>", prefix, key)
        unique_key = prefix + "_" + settings.MY_PLAYER_ID + "_" + key
        cache.set(unique_key, data, 3600)

    @staticmethod
    def get(prefix, key):
        print("cache=>", prefix, key, settings.MY_PLAYER_ID)
        unique_key = prefix + "_" + settings.MY_PLAYER_ID + "_" + key
        return cache.get(unique_key)
