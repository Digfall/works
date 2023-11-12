def validate_args(func):
    def wrapper(*args, **kwargs):
        
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        
        if not isinstance(args[0], int):
            return "Wrong types"
        
        if args[0] < 0:
            return "Negative argument"
        
        return func(*args, **kwargs)
    
    return wrapper

@validate_args
def example_func(x):
    return x

print(example_func(2))  
