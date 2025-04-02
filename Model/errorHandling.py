# Denne fil handler errors i programmet
def errorHandling(func):
    def innerFunction(*args, **kwargs): # *args og **kwargs er en måde at tage imod et vilkårlige antal argumenter
        try:
            return func(*args, **kwargs)
        except TypeError:
            # Denne error printer en besked, hvis der er for mange argumenter i en function
            print(f'Error: {func.__name__}() takes {func.__code__.co_argcount} positional arguments but {len(args)} were given.')
        except Exception as e:
            # Denne error printer en besked, hvis der er en anden error
            print(f'An error occured: {e}')    
    return innerFunction