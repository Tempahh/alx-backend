#!/usr/bin/python3

""" LIFO cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
LIFO algorithm must be used to manage the cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize FIFO cache system
        """
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """ Add key/value pair to cache data
        If number of items in cache data is higher than
        BaseCaching.MAX_ITEMS, discard the last item
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.cache_keys.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.cache_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)