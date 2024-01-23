#!/usr/bin/env python3
'''module 8-all'''


def list_all(mongo_collection):
    '''list all documenst based on query.'''
    result = []
    for doc in mongo_collection.find({}):
        result.append(doc)
    return result
