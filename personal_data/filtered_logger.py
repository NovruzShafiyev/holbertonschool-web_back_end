#!/usr/bin/env python3

"""
filter_datum: Obfuscate log message fields based on specified criteria.

Arguments:
fields: List of strings representing fields to obfuscate.
redaction: String representing the obfuscation value for the field.
message: String representing the log line.
separator: String representing the character separating fields in the log line.

Returns:
String: Log message with specified fields obfuscated.
"""

import re

def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(r'(?<=^|{})(?:{}=[^{}]*)(?={}|$)'.format(separator, '|'.join(fields), separator, separator), lambda x: '{}={}'.format(x.group().split('=')[0], redaction), message)
