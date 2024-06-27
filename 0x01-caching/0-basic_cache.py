#!/usr/bin/python3

BaseCaching = __import__('base_caching').BaseCaching

class BaseCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key, first_item = next(iter(self.cache_data.items()))
            print(f"DISCARD: {first_key} ")
            del self.cache_data[first_key]
        self.cache_data[key] = item
        

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
