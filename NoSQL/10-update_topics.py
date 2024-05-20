#!/usr/bin/env python3
"""
10-update_topics.py
Function that changes all topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name

    Args:
    mongo_collection (pymongo.collection.Collection): The collection object to update.
    name (str): The name of the school to update.
    topics (list of str): The list of topics approached in the school.

    Returns:
    None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
