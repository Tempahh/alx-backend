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
        self.cache_key = []

    # There's a typo in the code. It should be `self.cache_keys` instead of `self.cache_key` for consistency.
    # Here's the corrected version:

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
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.cache_key.pop(0)  # Corrected from self.cache_key to self.cache_keys
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item
        self.cache_key.append(key)  # Corrected from self.cache_key to self.cache_keys

    def get(self, key):
        """Return value in self.cache_data linked to key.
        If key is None or key does not exist in self.cache_data, return None.
        """
        if key is not None:
            if key in self.cache_data:
                # update access order
                self.cache_key.remove(key)
                self.cache_key.append(key)
                return self.cache_data[key]  # return value associated with key
        return None