"""
Decorator which returns run time for a function
This decorator is an alternative to using the python timeit module. 
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
        time_start = perf_counter()
        # run the func
        func_meta = func(*args, **kw)
        time_end = perf_counter()
        run_time = time_end - time_start

        # @NOTE: !r will return repr of func and :.8f is 8 decimal places
        all_meta = f"func: {func.__name__!r}, args:{[args, kw]}, time taken: {run_time:.8f}"
        print(all_meta)

        return func_meta
    return wrap