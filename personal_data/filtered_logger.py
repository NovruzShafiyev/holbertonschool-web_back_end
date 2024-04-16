#!/usr/bin/env python3

'''Filtered logger'''
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''Filtering values of the required fields'''
    for item in fields:
        message = re.sub(f"{item}=.*?{separator}",
                         f"{item}={redaction}{separator}", message)
    return message


def main() -> None:
    '''Main'''
    connector = get_db()

    cursor = connector.cursor()
    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()

    logger = get_logger()

    for line in data:
        logger.info(line)

    cursor.close()
    connector.close()


if __name__ == "__main__":
    main()
