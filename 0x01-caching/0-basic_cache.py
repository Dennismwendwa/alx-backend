#!/usr/bin/env python3
"""This script implements put and get methods"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This is the parent caching class"""
    def put(self, key, item):
        """This method adds items to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """This method gets items from the cache"""
        if key is not None:
            return self.cache_data.get(key)
