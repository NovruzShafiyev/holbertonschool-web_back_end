#!/usr/bin/env python3
"""
12-log_stats.py
Script to provide statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def get_log_stats():
    """
    Get statistics about Nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the logs.nginx collection
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})

    # Get the count of each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

    # Get the count of logs with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    get_log_stats()
