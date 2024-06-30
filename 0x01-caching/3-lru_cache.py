#!/usr/bin/python3

""" LRU cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
LRU algorithm must be used to manage the cache
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
    Uses LRU algorithm to manage cache.
    """

    def __init__(self):
        """ Initialize LRU cache system
        """
        super().__init__()
        self.cache_keys = OrderedDict()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
        item value for the key
        If key or item is None, do nothing.
        When number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS:
            - discard the least recently used item in self.cache_keys
            - discard the least recently used item in self.cache_data
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
        """Return value in self.cache_data linked to key.
        If key is None or key does not exist in self.cache_data, return None.
        """
        # Directly return the value associated with 'key' or None if 'key' is not found.
        return self.cache_data.get(key)
