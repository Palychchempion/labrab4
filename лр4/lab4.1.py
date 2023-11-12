import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    sum_dict = 0
    for i in data:
        s = i['score']
        s1 = i['weight']
        sum_dict += s * s1
    return round(sum_dict, 3)
print(task())