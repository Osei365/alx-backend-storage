#!/usr/bin/env python3
'''module 10-update'''


def update_topics(mongo_collection, name, topics):
    '''updates collection documents.'''
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )
