def repeat_me(func):
    def decorator(*args, **kwargs):
        count = kwargs.get('count', 1)
        for i in range(count):
            func(*args)
    return decorator


@repeat_me
def example(text):
    print(text)


example('print me', count=5)
