"""
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s begin call %s' % (text, func.__name__))
            f = func(*args, **kwargs)
            print('%s end call %s' % (text, func.__name__))
            return f
        return wrapper
    if isinstance(text,str):
        return decorator
    else:
        fs = text
        text = ''
        return decorator(fs)


@log#('aaa')
def now():
    print('lalala')


now()

