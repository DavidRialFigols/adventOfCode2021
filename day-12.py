import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split('-') for i in fin.read().rstrip().split("\n")]
    return data

def find_path_1(actual_path, data):
    last_visit = actual_path[-1]
    paths = 0
    for i in data: 
        if last_visit == i[0]:
            if 'end' == i[1]:
                paths += 1
            elif i[1].isupper() or i[1] not in actual_path:
                paths += find_path_1(actual_path + [i[1]], data)
        elif last_visit == i[1]:
            if 'end' == i[0]:
                paths += 1
            elif i[0].isupper() or i[0] not in actual_path:
                paths += find_path_1(actual_path + [i[0]], data)

    return paths

def find_path_2(actual_path, data, visited_small_caves, enable_sm_cv):
    last_visit = actual_path[-1]
    paths = 0
    for i in data: 
        if last_visit == i[0]:
            if 'end' == i[1]:
                paths += 1
            elif (i[1].isupper() or enable_sm_cv or visited_small_caves[i[1]]<1) and i[1]!='start':
                if i[1].islower():
                    if visited_small_caves[i[1]]==1:
                        paths += find_path_2(actual_path + [i[1]], data, visited_small_caves.copy(), False)
                    else:
                        visited = visited_small_caves.copy()
                        visited[i[1]]+=1
                        paths += find_path_2(actual_path + [i[1]], data, visited, enable_sm_cv)
                else:
                    paths += find_path_2(actual_path + [i[1]], data, visited_small_caves.copy(), enable_sm_cv)
        elif last_visit == i[1]:
            if 'end' == i[0]:
                paths += 1
            elif (i[0].isupper() or enable_sm_cv or visited_small_caves[i[0]]<1) and i[0]!='start':
                if i[0].islower():
                    if visited_small_caves[i[0]]==1:
                        paths += find_path_2(actual_path + [i[0]], data, visited_small_caves.copy(), False)
                    else:
                        visited = visited_small_caves.copy()
                        visited[i[0]]+=1
                        paths += find_path_2(actual_path + [i[0]], data, visited, enable_sm_cv)
                else:
                    paths += find_path_2(actual_path + [i[0]], data, visited_small_caves.copy(), enable_sm_cv)
    return paths

def process_data_1(data):
    return find_path_1(['start'], data)

def process_data_2(data):
    visited_small_caves = {}
    for i in data:
        for c in i:
            if c.islower() and c not in visited_small_caves:
                visited_small_caves[c] = 0
    return find_path_2(['start'], data, visited_small_caves, True)


if __name__ == "__main__":
    day = "12"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(np.copy(data).tolist())
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
