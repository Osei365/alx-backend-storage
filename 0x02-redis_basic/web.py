#!/usr/bin/env python3
'''module web.py.'''

import redis
import requests
from functools import wraps
from typing import Callable


client = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker

@data_catcher
def get_page(url: str) -> str:
    '''tracks number of times a url is accessed'''
    return requests.get(url).text