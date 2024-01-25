#!/usr/bin/env python3
'''module web.py.'''

import redis
import requests
from functools import wraps
from typing import Callable


client = redis.Redis()


def getpage_deco(func: Callable) -> Callable:
    '''decorates the get_page.'''
    @wraps(func)
    def wrapper(url) -> str:
        '''gets number of times url is accessed'''
        client.incr(f'count:{url}')
        cache = client.get(f'{url}')
        if cache:
            return cache.decode('utf-8')
        result = func(url)
        client.set(f'count:{url}', 0)
        client.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@getpage_deco
def get_page(url: str) -> str:
    '''displays html content of url'''
    return requests.get(url).text
