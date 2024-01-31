#!/usr/bin/env python3
"""This script uses LRUCache for cache system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This class implements LRUCache cache system"""
    def __init__(self):
        """Initialize LRUCache class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """This method add items to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.order.append(key)
    
    def get(self, key):
        """This method get item from the cache"""
        if key is not None:
            if key in self.order:
                self.order.remove(key)
                self.order.append(key)
            return self.cache_data.get(key)
