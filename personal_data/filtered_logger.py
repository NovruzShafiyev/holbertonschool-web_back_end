#!/usr/bin/env python3
"""
Filter log messages by obfuscating specified fields.
"""

import re

def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
  """
  Filters a log message by obfuscating specified fields.
  """
  pattern = rf"(?:{separator})({'|'.join(fields)})=(.*?)(?={separator}|$)"
  return re.sub(pattern, rf"\1={redaction}", message)
