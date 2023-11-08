def merge_dictiniry(dict1, dict2):
    res = {}
    for item in dict1:
        if dict1.get(item) == dict2.get(item):
            res[item] = dict1.get(item)
    return res


dict1 = {
    'a': 1,
    'c': 34,
    'd': 65
}

dict2 = {
    'c': 2,
    'c': 1,
    'd': 65
}

print(merge_dictiniry(dict1, dict2))