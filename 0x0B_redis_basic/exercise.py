#!/usr/bin/env python3
"""
This module defines a Cache class that provides an interface for storing data in a Redis database.
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class for interacting with Redis.
    
    Attributes:
        _redis (redis.Redis): Redis client instance.
    """

    def __init__(self):
        """
        Initialize the Cache class.
        
        Create a Redis client instance and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
