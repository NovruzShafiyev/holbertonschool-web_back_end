#!/usr/bin/env python3
''' Description: Augment the following code with the correct 
    type annotations.
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Union[Sequence[Any], None]) -> Union[Any, None]:
    ''' Return the first element of lst if there is any, otherwise None. '''
    if lst and len(lst) > 0:
        return lst[0]
    else:
        return None
