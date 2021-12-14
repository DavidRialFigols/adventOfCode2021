import numpy as np
from collections import Counter
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n\n")
        data = {
            'template': data[0],
            'pairs_array': data[1].split('\n'),
            'pairs': {},
            'letters': {}
        }
        for i in range(len(data['pairs_array'])):
            data['pairs'][data['pairs_array'][i].split(' -> ')[0]] = [data['pairs_array'][i].split(' -> ')[1], 0]
            if data['pairs_array'][i].split(' -> ')[1] not in data['letters']:
                data['letters'][data['pairs_array'][i].split(' -> ')[1]] = 0
        for i in range(len(data['template'])-1):
            data['pairs'][f"{data['template'][i]}{data['template'][i+1]}"][1] += 1
            print(data['pairs'])
            if data['template'][i] not in data['letters']:
                data['letters'][data['template'][i]] = 1
            else:
                data['letters'][data['template'][i]] += 1
        if data['template'][-1] not in data['letters']:
            data['letters'][data['template'][-1]] = 1
        else:
            data['letters'][data['template'][-1]] += 1
    return data

def step(data):
    pairs = copy.deepcopy(data['pairs'])
    for pair in pairs:
        data['pairs'][pair][1] -= pairs[pair][1]
        if f"{pair[0]}{data['pairs'][pair][0]}" in data['pairs']:
            # print(f"{pair[0]}{data['pairs'][pair][0]}")
            # print(data['pairs'][f"{pair[0]}{data['pairs'][pair][0]}"][1])
            data['pairs'][f"{pair[0]}{data['pairs'][pair][0]}"][1] += pairs[pair][1]
            # print(pairs)
            # print(data['pairs'][f"{pair[0]}{data['pairs'][pair][0]}"][1])
            # if data['pairs'][f"{pair[0]}{data['pairs'][pair][0]}"][1]==pairs[f"{pair[0]}{data['pairs'][pair][0]}"][1]:
            #     print('son iguals')
            #     print(pair)
            #     break
        if f"{data['pairs'][pair][0]}{pair[1]}" in data['pairs']:
            # print('he entrat =======================================')

            # print(f"{pair[0]}{data['pairs'][pair][0]}")
            # print(data['pairs'][f"{pair[0]}{data['pairs'][pair][0]}"][1])
            data['pairs'][f"{data['pairs'][pair][0]}{pair[1]}"][1] += pairs[pair][1]

            # print(pairs[pair][1])
            # print(data['pairs'][f"{pair[0]}{data['pairs'][pair][0]}"][1])
            # if data['pairs'][f"{data['pairs'][pair][0]}{pair[1]}"][1] == pairs[f"{data['pairs'][pair][0]}{pair[1]}"][1]:
            #     print('son iguals 2')
            #     print(pair)
            #     break
        data['letters'][data['pairs'][pair][0]] += pairs[pair][1]
    return data

    # for i in range(length_template):
    #     new_template += data['template'][i]
    #     if count:
    #         if data['template'][i] in letters_count:
    #             letters_count[data['template'][i]] += 1
    #         else:
    #             letters_count[data['template'][i]] = 1

    #     if i+1 < length_template:
    #         if f"{data['template'][i]}{data['template'][i+1]}" in data['pairs']:
    #             new_template += data['pairs'][f"{data['template'][i]}{data['template'][i+1]}"]
    #             if count:
    #                 if data['pairs'][f"{data['template'][i]}{data['template'][i+1]}"] in letters_count:
    #                     letters_count[data['pairs'][f"{data['template'][i]}{data['template'][i+1]}"]] += 1
    #                 else:
    #                     letters_count[data['pairs'][f"{data['template'][i]}{data['template'][i+1]}"]] = 1
    # data['template'] = new_template
    # if count:
    #     return letters_count.values()
    # return data

def process_data_1(data):
    days = 10
    for i in range(days):
        data = step(data)
    print(data['letters'])
    return max(data['letters'].values())-min(data['letters'].values())

def process_data_2(data):
    days = 40
    for i in range(days):
        data = step(data)
    print(data['letters'])
    return max(data['letters'].values())-min(data['letters'].values())


if __name__ == "__main__":
    day = "14"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
