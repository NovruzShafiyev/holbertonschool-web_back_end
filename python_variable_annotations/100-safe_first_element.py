#!/usr/bin/env python3
"""
    Duck typing sequence Any
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Args:
            lst: Any data type

        Return:
            None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
