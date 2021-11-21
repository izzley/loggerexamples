"""
Decorator which returns run time for a function
This decorator is an alternative to using the python timeit module. 
Calcs the difference between end & start times: https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator

Same principle except using using perf_counter: https://realpython.com/lessons/timing-functions-decorators/

What are decorators?  https://gist.github.com/Zearin/2f40b7b9cfc51132851a

Decorators can be reinforced to accept args: https://stackoverflow.com/questions/653368/how-to-create-a-python-decorator-that-can-be-used-either-with-or-without-paramet
"""
from functools import wraps
import logging
from time import perf_counter

def timing(func):
    """
    Runtime wrapper for functions. Also returns args and kwargs
    see module01.py for usage
    """
    @wraps(func)
    def wrap(*args, **kw):
        timestart = perf_counter()
        # run the func
        funcmeta = func(*args, **kw)
        timeend = perf_counter()
        runtime = timeend - timestart

        # @NOTE: !r will return repr of func and :.8f is 8 decimal places
        allmeta = f"func: {func.__name__!r}, args:{[args, kw]}, time taken: {runtime:.8f}"
        print(allmeta)

        return funcmeta
    return wrap