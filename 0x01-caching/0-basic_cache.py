#!/usr/bin/env python3
"""task 00"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """initialization"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """store a key value pair"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return value of a key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
