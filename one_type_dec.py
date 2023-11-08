import functools as ft

def one_type(type_of_arg):
    def warp(func):
        @ft.wraps(func)

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if type(res) != type(type_of_arg):
                return 'недопустимый аргумент'
            return res
        return wrapper
    return warp
   
       

@one_type()
def abc(a):
    return a

print(abc())

# Декоратор сравнивает тип аргумента, который в него передали
# Если типы совпадают, то функция "abc()" возвращает аргумент переданный в нее
# В противном случае выбрасывается ошибка
