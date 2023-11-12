def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper
