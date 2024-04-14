#!/usr/bin/python3
''' Basic cache Basic cache Basic cache Basic cache
'''

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    ''' LFU cache class
    '''
    def __init__(self):
        ''' Initializer with additional list
        '''
        super().__init__()
        self.listC = {}

    def put(self, key, item):
        ''' Add an item in the cache
            and remove first if more than max items
        '''
        if key and item:
            self.cache_data[key] = item
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                first = sorted(self.listC.items(), key=lambda x: x[1])[0][0]
                print("DISCARD:", first)
                self.cache_data.pop(first)
                self.listC.pop(first)
            self.listC[key] = 0

    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = value
            self.listC[key] += 1
            return value
