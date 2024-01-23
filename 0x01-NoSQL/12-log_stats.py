#!/usr/bin/env python3
'''12-log_stats.py'''

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx
    print('{} logs'.format(col.count_documents({})))
    print('Methods:')
    print('\tmethod GET: {}'.format(col.count_documents({'method': 'GET'})))
    print('\tmethod POST: {}'.format(col.count_documents({'method': 'POST'})))
    print('\tmethod PUT: {}'.format(col.count_documents({'method': 'PUT'})))
    print('\tmethod PATCH: {}'.format(col.count_documents({'method': 'PATCH'})))
    print('\tmethod DELETE: {}'.format(col.count_documents({'method': 'DELETE'})))
    print('{} status check'.format(col.count_documents({'method': 'GET',
                                                        'path': '/status'})))
