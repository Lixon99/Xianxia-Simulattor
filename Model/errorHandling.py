def errorHandling(func):
    def innerFunction(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            print(f'Error: {func.__name__}() takes {func.__code__.co_argcount} positional arguments but {len(args)} were given.')
        except Exception as e:
            print(f'An error occured: {e}')    
    return innerFunction