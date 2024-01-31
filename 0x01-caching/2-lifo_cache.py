#!/usr/bin/env python3
"""This script implements LIFOCache system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This is the parent class"""
    def __init__(self):
        """Initializes the FIFOCache class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """This method adds items to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.queue.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """This method gets items from the cache"""
        if key is not None:
            return self.cache_data.get(key)
