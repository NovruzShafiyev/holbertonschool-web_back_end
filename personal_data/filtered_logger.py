#!/usr/bin/env python3
"""
Logger
"""
import re
from typing import List
import logging
from os import environ
import mysql.connector import connection
from filtered_logger import get_logger, RedactingFormatter, PII_FIELDS

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values from the log record"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

    def filter_datum(fields: List[str], redaction: str, message: str,
                     separator: str) -> str:
        """returns log message obfuscated"""
        for field in fields:
            message = re.sub(f'{field}=(.*?){separator}',
                             f'{field}={redaction}{separator}', message)
        return message

    def get_logger() -> logging.Logger:
        """ takes no arguments and returns
        a logging.Logger object"""
        logger = logging.getLogger("user_data")
        logger.setLevel(logging.INFO)
        logger.propagate = False
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
        logger.addHandler(stream_handler)
        return logger

    def get_db() -> connection.MySQLConnection:
        """connect to database"""
        host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
        user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
        password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
        db_name = os.environ["PERSONAL_DATA_DB_NAME"]
        return mysql.connector.connect(host=host, user=user,
                                       password=password, database=db_name)

    def main():
        """main"""
        logger = get_logger()
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            log_line = RedactingFormatter.SEPARATOR.join(str(field)
                                                         for field in row)
            logger.info(RedactingFormatter().filter_datum(PII_FIELDS,
                                                          RedactingFormatter.
                                                          REDACTION,
                                                          log_line,
                                                          RedactingFormatter.
                                                          SEPARATOR))
            cursor.close()
            conn.close()

        if name == "main":
            main()
