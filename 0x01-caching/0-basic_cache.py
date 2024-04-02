#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that inherits from the BaseCaching class"""
    def __inti__(self, cache_data):
        """Initialize the subclass"""
        super().__init__()

    def put(self, key, item):
        """function thats inserts into the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets item stored at key"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.get(key)
        return value
