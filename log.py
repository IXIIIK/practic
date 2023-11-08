def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'аргументы функции: {args}')
        print(f'результат функции {log.__name__}: {res}')
        return res
    return wrapper

@log
def sum_int(num1, num2):
    return num1 + num2

sum_int(1, 2)