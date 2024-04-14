#!/usr/bin/env python3

from typing import Any, Optional, Sequence

def safe_first_element(lst: Sequence) -> Optional[Any]:
    """Return the first element of a sequence if it exists, otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None

if __name__ == "__main__":
    print(safe_first_element.__annotations__)
