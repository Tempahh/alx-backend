#!/usr/bin/python3
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """ LRU cache system that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize LRU cache system
        """
        super().__init__()
        self.cache_keys = OrderedDict()

    def put(self, key, item):
        """ Add key/value pair to cache data
        If number of items in cache data is higher than
        BaseCaching.MAX_ITEMS, discard the oldest item
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_keys.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_keys.popitem(last=False)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.cache_keys[key] = None
        self.cache_data[key] = item

    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)