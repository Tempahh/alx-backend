#!/usr/bin/python3

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """ Override put method and assign item value to the key in cache_data
        dictionary.
        If either key or item is None, do nothing.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key, first_item = next(iter(self.cache_data.items()))
            print(f"DISCARD: {first_key} ")
            del self.cache_data[first_key]
        self.cache_data[key] = item
        

    def get(self, key):
        """ Override get method and return value linked to key in cache_data
        dictionary.
        If key is None or key does not exist in cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
