#!/usr/bin/python3

""" MRU cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
MRU algorithm must be used to manage the cache
"""


BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """ MRU cache system that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize MRU cache system
        """
        super().__init__()
        self.cache_key = []

    def put(self, key, item):
        """ Add key/value pair to cache data
        If number of items in cache data is higher than
        BaseCaching.MAX_ITEMS, discard the oldest item
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.cache_key.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item
        self.cache_key.append(key)

    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        if key is not None:
            if key in self.cache_data:
                # update access order
                self.cache_key.remove(key)
                self.cache_key.append(key)
                return self.cache_data[key]  # return value associated with key
        return None