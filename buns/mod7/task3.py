import time


def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"
        return func(*args, **kwargs)
    return wrapper


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


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        if not hasattr(wrapper, 'total_time'):
            wrapper.total_time = 0
        wrapper.total_time += end - start
        return end
    return wrapper


@timer
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
@memoize
@validate_args
def fibonacci_with_memoize(n):
    if n < 2:
        return n
    else:
        return fibonacci_with_memoize(n - 1) + fibonacci_with_memoize(n - 2)


fibonacci(20)
fibonacci_with_memoize(20)

print(f"Время выполнения без memoize: {fibonacci.total_time} секунд") 
print(f"Время выполнения с memoize: {fibonacci_with_memoize.total_time} секунд")
