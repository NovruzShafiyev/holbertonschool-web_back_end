import logging
import os
import mysql.connector

from typing import Tuple

PII_FIELDS: Tuple[str, str, str, str, str] = ("name", "email", "phone", "ssn", "password")

def get_db():
    """Return a connector to the database (mysql.connector.connection.MySQLConnection object)."""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', '')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )

def main():
    """Retrieve all rows in the users table and display each row under a filtered format."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        filtered_row = {field: "***" for field in PII_FIELDS}
        filtered_row.update(row)
        logging.info(filtered_row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
