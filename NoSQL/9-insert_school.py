#!/usr/bin/env python3
"""
9-insert_school.py
Function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection

    Args:
    mongo_collection (pymongo.collection.Collection): The collection object to insert into.
    **kwargs: Key-value pairs representing the document to be inserted.

    Returns:
    ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
