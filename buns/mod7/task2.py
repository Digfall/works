def memoize(func):
    cache = {}
    
    def wrapr(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))  
        if key in cache:
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        
        return result
    
    wrapr.__name__ = func.__name__
    wrapr.__doc__ = func.__doc__
    
    return wrapr

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(10)
print(result)
print(f"Имя функции: {fibonacci.__name__}")
print(f"Документация функции: {fibonacci.__doc__}")
