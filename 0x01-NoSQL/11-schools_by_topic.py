#!/usr/bin/env python3
'''module 11-schools by topic.'''


def schools_by_topic(mongo_collection, topic):
    '''list documents based on query.'''
    res = []
    for doc in mongo_collection.find({'topics': topic}):
        res.append(doc)
    return res
