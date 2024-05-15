#!/usr/bin/env python3
"""
This module defines a function to fetch HTML content of a URL, track access count,
and cache the result with an expiration time using Redis.
"""

import requests
import redis
from typing import Callable
from functools import wraps

# Initialize the Redis client
redis_client = redis.Redis()

def track_access(method: Callable) -> Callable:
    """
    Decorator to track the number of times a URL is accessed and cache the result.
    
    Args:
        method (Callable): The function to be decorated.
    
    Returns:
        Callable: The decorated function.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to track access count and cache result.
        
        Args:
            url (str): The URL to fetch.
        
        Returns:
            str: The HTML content of the URL.
        """
        # Track access count
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        # Check if the content is cached
        cache_key = f"cached:{url}"
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')
        
        # Fetch the HTML content and cache it
        response = method(url)
        redis_client.setex(cache_key, 10, response)
        return response
    
    return wrapper

@track_access
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL.
    
    Args:
        url (str): The URL to fetch.
    
    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))
    print(f"Access count: {redis_client.get(f'count:{url}').decode('utf-8')}")
