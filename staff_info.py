staff = {
    '1' : {
        'name': 'Jhon',
        'pos': 'dev',
        'check': 1000,
    },
    '2' : {
        'name': 'Ivan',
        'pos': 'dev',
        'check': 1300,
    },
    '3' : {
        'name': 'Bob',
        'pos': 'dev',
        'check': 500,
    }
}

def high_check(value):
    for id in staff:
        if staff[id]['check'] > value: 
            return staff[id]['name']


# Функция принимает базу работников и возвращает того у кого значение больше заданного