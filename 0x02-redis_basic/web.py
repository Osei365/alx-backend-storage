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
    def wrapper(url: str) -> str:
        '''wraps itself around func.'''
        client.incr(f"count:{url}")
        result = client.get(f"result:{url}")
        if result:
            return result.decode('utf-8')
        result = func(url)
        client.set(f"count:{url}", 0)
        client.setex(f"result:{url}", 10, result)
        return result
    return wrapper


@getpage_deco
def get_page(url: str) -> str:
    '''tracks number of times a url is accessed'''
    return requests.get(url).text
