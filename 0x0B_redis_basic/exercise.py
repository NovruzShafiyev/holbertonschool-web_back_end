#!/usr/bin/env python3
"""
This module defines a Cache class that provides an interface for storing and retrieving data in a Redis database,
as well as counting method calls and storing call history.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count in Redis and then calls the original method.

        Args:
            self (Cache): The instance of the Cache class.
            *args: Positional arguments for the original method.
            **kwargs: Keyword arguments for the original method.

        Returns:
            Any: The return value of the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function in Redis.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that logs the input arguments and output of the decorated method.

        Args:
            self (Cache): The instance of the Cache class.
            *args: Positional arguments for the original method.
            **kwargs: Keyword arguments for the original method.

        Returns:
            Any: The return value of the original method.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        
        result = method(self, *args, **kwargs)
        
        self._redis.rpush(output_key, str(result))
        
        return result
    
    return wrapper

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

    @call_history
    @count_calls
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
