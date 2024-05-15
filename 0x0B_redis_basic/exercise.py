#!/usr/bin/env python3
"""
This module defines a Cache class that provides an interface for storing and retrieving data in a Redis database.
"""

import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieve the data stored at the given key from Redis and optionally convert it using the provided callable.

        Args:
            key (str): The key for the data in Redis.
            fn (Optional[Callable]): The function to convert the data back to the desired format.

        Returns:
            Optional[Union[str, bytes, int, float]]: The retrieved data, possibly converted using fn, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data stored at the given key from Redis and convert it to a UTF-8 string.

        Args:
            key (str): The key for the data in Redis.

        Returns:
            Optional[str]: The retrieved data as a UTF-8 string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data stored at the given key from Redis and convert it to an integer.

        Args:
            key (str): The key for the data in Redis.

        Returns:
            Optional[int]: The retrieved data as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
