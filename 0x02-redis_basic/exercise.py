#!/usr/bin/env python3
'''module 0-exercise.py.'''

import uuid
import redis
from typing import Union


class Cache:
    '''The cache class.'''

    def __init__(self) -> None:
        '''initialize redis.'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''stores data in redis.'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
