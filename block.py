def block(func):
    score = 0
    def wrapper(*args, **kwargs):
        nonlocal score
        score += 1
        if score >= 3:
            return 'функция больше не может быть вызвана'
        return func(*args, **kwargs)
    return wrapper

@block
def abc():
    print(1)

