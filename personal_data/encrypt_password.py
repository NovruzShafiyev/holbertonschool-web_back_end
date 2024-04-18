#!/usr/bin/env python3
"""
Encrypt Password module
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Returns hash"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password against its hashed version using bcrypt"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
