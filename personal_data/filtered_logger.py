#!/usr/bin/env python3

"""
Main file
"""

import re

def filter_datum(fields, redaction, message, separator):
    """Obfuscate log message."""
    return re.sub(
        r'(?<=^|{})(?:{}=[^{}]*)(?={}|\Z)'.format(separator, '|'.join(fields), separator, separator),
        f'{fields[0]}={redaction}',
        message
    )
