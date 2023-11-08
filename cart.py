def sum_of_cart(items):
    res = [sum(items.get(i) for i in items)]
    return ' '.join(res)

    
items = {
    'phone': 1000,
    'apple': 1000,
    'banana': 500
}

#Функция принимает список товаров и выводит их общую сумму