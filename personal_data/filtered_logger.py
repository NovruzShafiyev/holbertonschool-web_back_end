#!/usr/bin/env python3
"""Filter log messages by obfuscating specified fields.

This function obfuscates fields in a log message by replacing their values
with a redaction string using a regular expression.

Args:
    fields: List of field names to obfuscate.
    redaction: String to replace the obfuscated field values.
    message: The log message string.
    separator: The separator character between fields in the log message.

Returns:
    The obfuscated log message string.
"""

import re

def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
  """Filters a log message by obfuscating specified fields.

  Args:
      fields: List of field names to obfuscate.
      redaction: String to replace the obfuscated field values.
      message: The log message string.
      separator: The separator character between fields in the log message.

  Returns:
      The obfuscated log message string.
  """
  pattern = rf"(?:{separator})({'|'.join(fields)})=(.*?)(?={separator}|$)"
  return re.sub(pattern, rf"\1={redaction}", message)
