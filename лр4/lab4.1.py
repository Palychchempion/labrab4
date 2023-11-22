import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    sum_dict = sum([i["score"]*i["weight"] for i in data])
    return round(sum_dict, 3)
print(task())
