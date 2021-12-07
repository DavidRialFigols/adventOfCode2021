import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [int(i) for i in fin.read().rstrip().split(",")]
    return data

def obtain_naive_1(data):
    first = data[0]
    acum = 0
    for crab in data:
        acum += abs(first-crab)
    return acum

def obtain_naive_2(data):
    first = data[0]
    acum = 0
    for crab in data:
        acum += int(abs(first-crab)*(abs(first-crab)+1)/2)
    return acum

def process_data_1(data):
    unique = [i for i in range(min(data), max(data)+1)]
    min_value, min_found = data[0], obtain_naive_1(data)
    for u in unique:
        acum = 0
        for crab in data:
            acum += abs(u-crab)
            if acum >= min_found:
                break
        if acum < min_found:
            min_value, min_found = u, acum
    return min_found

def process_data_2(data):
    unique = [i for i in range(min(data), max(data)+1)]
    min_value, min_found = data[0], obtain_naive_2(data)
    for u in unique:
        acum = 0
        for crab in data:
            acum += int(abs(u-crab)*(abs(u-crab)+1)/2)
            if acum >= min_found:
                break
        if acum < min_found:
            min_value, min_found = u, acum
    return min_found


if __name__ == "__main__":
    day = "07"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data.copy())
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data.copy())
    print(f"result 2: {result_2}")
