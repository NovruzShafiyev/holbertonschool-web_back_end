#!/usr/bin/env python3

"""
This module defines a function for pagination.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index for the page.

    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
