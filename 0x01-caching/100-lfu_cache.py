#!/usr/bin/env python3
"""This script creates cache class using LFUCache system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This class creates class LFUCache using LFU system"""
    def __init__(self):
        """Initializes LFUCache"""
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """This method add items to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                keys_to_discard = [
                    k for k, v in self.frequency.items()
                    if v == min_frequency
                    ]
                if len(keys_to_discard) > 1:
                    discarded_key = self.order.pop(0)
                else:
                    discarded_key = keys_to_discard[0]
                if discarded_key in self.cache_data:
                    del self.cache_data[discarded_key]
                    del self.frequency[discarded_key]
                    print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.order.append(key)

    def get(self, key):
        """This method get item from cache by key"""
        if key is not None:
            if key in self.order:
                self.frequency[key] += 1
            return self.cache_data.get(key)
