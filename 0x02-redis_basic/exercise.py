#!/usr/bin/env python3
'''module 0-exercise.py.'''

import uuid
import redis
from functools import wraps
from typing import Union, Callable, Any


def call_history(method: Callable) -> Callable:
    '''uses rpush to save history'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''wraps decorated function.'''
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return method(self, *args, **kwargs)
    return wrapper


def count_calls(method: Callable) -> Callable:
    '''Tracks the number of calls made to a method in a Cache class.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''wraps giving function
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''The cache class.'''

    def __init__(self) -> None:
        '''initialize redis.'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''stores data in redis.'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''converts redis result to desired result.'''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''gets a str from a key.'''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        ''' gets an int from a key.'''
        return self.get(key, lambda x: int(x))
