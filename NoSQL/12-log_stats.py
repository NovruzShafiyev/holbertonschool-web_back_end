#!/usr/bin/env python3
"""
12-log_stats.py
Script to provide statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats():
    """
    Provide statistics about Nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count total number of documents in the collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents for each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents where method is GET and path is /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
