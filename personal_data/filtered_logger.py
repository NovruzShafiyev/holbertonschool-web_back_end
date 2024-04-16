#!/usr/bin/env python3

"""
filtered_logger module
"""

import re


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """
    Replace occurrences of certain field values in the log message with redaction.

    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all fields in the log line (message)

    Returns:
        str: obfuscated log message
    """
    return re.sub(r'(?<=^|{})(?:{}=[^{}]*)(?={}|\Z)'.format(separator, '|'.join(fields), separator, separator), f'{fields[0]}={redaction}', message)
