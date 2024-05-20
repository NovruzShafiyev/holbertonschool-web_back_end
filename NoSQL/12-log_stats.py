#!/usr/bin/env python3
"""
    script that provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient(host="localhost", port=27017)

    collection = client.logs.nginx

    # first line
    numb_docs = collection.count_documents({})
    print("{} logs".format(numb_docs))
    print("Methods:")

    # second line
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for meth in method:
        numb_each_method = collection.count_documents({"method": meth})
        print("\tmethod {}: {}".format(meth, numb_each_method))

    get_count = collection.count_documents({"method": "GET",
                                            "path": "/status"})
    print("{} status check".format(get_count))
