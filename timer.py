import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print( f'время выполнения функции {func.__name__} = {end - start}')
        return res
    return wrapper


@timer
def abc():
    time.sleep(2)


