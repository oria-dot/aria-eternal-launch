
import redis

class DataCache:
    def __init__(self, host='localhost', port=6379):
        self.client = redis.StrictRedis(host=host, port=port, db=0)

    def set_cache(self, key, value, ttl=60):
        self.client.setex(key, ttl, value)

    def get_cache(self, key):
        return self.client.get(key)
