#!/usr/bin/env python3
'''module 0-exercise.py.'''

import uuid
import redis
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
        '''converts redis result to desired result.'''
        data = self._redis.get(key)
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        '''gets a str from a key.'''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        ''' gets an int from a key.'''
        return self.get(key, lambda x: int(x))
