#!/usr/bin/env python3
"""LIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class that sub classes Basecaching"""
    def __inti__(self):
        """Initialize class"""
        super().__init__()

    def put(self, key, item):
        """function that inserts into the cache"""
        if key is None or item is None:
            return
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_one, item_one = self.cache_data.popitem()
            print(f'DISCARD: {key_one}')
        self.cache_data[key] = item

    def get(self, key):
        """gets item stored at key"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.get(key)
        return value
