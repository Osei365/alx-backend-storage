#!/usr/bin/env python3
'''module web.py.'''

import redis
import requests
from functools import wraps
from typing import Callable


def getpage_deco(func: Callable) -> Callable:
    '''decorates the get_page.'''
    @wraps(func)
    def wrapper(url) -> str:
        '''gets number of times url is accessed'''
        client = redis.Redis()
        client.incr(f'count:{url}')
        cache = client.get(f'{url}')
        if cache:
            return cache.decode('utf-8')
        result = func(url)
        client.set(f'{url}', result, 10)
        return result
    return wrapper


@getpage_deco
def get_page(url: str) -> str:
    '''displays html content of url'''
    return requests.get(url).text
