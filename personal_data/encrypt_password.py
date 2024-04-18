#!/usr/bin/env python3
"""
Encrypt Password module
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with salt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    print(hash_password(password).decode('utf-8'))
    print(hash_password(password).decode('utf-8'))
    print(hash_password(password).decode('utf-8'))
