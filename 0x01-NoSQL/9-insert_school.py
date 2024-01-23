#!/usr/bin/env python3
'''module 9-insert'''


def insert_school(mongo_collection, **kwargs):
    '''inserts into a database collection'''
    res_id = mongo_collection.insert_one(kwargs)
    return res_id.inserted_id
