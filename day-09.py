import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[int(c) for c in i] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    suma = 0
    for line in range(len(data)):
        for num in range(len(data[line])):
            if line > 0: up = data[line-1][num]
            else: up = 10
            if line < len(data)-1: down = data[line+1][num]
            else: down = 10
            if num > 0: left = data[line][num-1]
            else: left = 10
            if num < len(data[line])-1: right = data[line][num+1]
            else: right = 10

            i = data[line][num]
            if i < up and i < down and i < left and i < right:
                print(f"num: {i} | pos: ({line},{num}) | up,down,left,right = ({up},{down},{left},{right})")
                suma += i + 1
    return suma

def calc_basin(basin, actual, data):
    value_basin = data[actual[0]][actual[1]]
    if (data[actual[0]-1][actual[1]] < 9) and ((actual[0]-1, actual[1]) not in basin):
        basin.add((actual[0]-1, actual[1]))
        sub_basin, value_sub_basin = calc_basin(basin, (actual[0]-1,actual[1]), data)
        basin = set.union(basin, sub_basin)
        value_basin += value_sub_basin
    if (data[actual[0]+1][actual[1]] < 9) and ((actual[0]+1, actual[1]) not in basin):
        basin.add((actual[0]+1, actual[1]))
        sub_basin, value_sub_basin = calc_basin(basin, (actual[0]+1,actual[1]), data)
        basin = set.union(basin, sub_basin)
        value_basin += value_sub_basin
    if (data[actual[0]][actual[1]-1] < 9) and ((actual[0], actual[1]-1) not in basin):
        basin.add((actual[0], actual[1]-1))
        print(basin)
        sub_basin, value_sub_basin = calc_basin(basin, (actual[0],actual[1]-1), data)
        basin = set.union(basin, sub_basin)
        value_basin += value_sub_basin
    if (data[actual[0]][actual[1]+1] < 9) and ((actual[0], actual[1]+1) not in basin):
        basin.add((actual[0], actual[1]+1))
        sub_basin, value_sub_basin = calc_basin(basin, (actual[0],actual[1]+1), data)
        basin = set.union(basin, sub_basin)
        value_basin += value_sub_basin
    return basin, value_basin


def process_data_2(data):
    data = [[10 for i in range(len(data[0]))]] + data + [[10 for i in range(len(data[0]))]]
    for i in range(len(data)):
        data[i] = [10] + data[i] + [10]

    to_check = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] < 9]
    print(to_check)
    top_basins = []
    while len(to_check) > 0:
        basin, value_basin = calc_basin(set([(to_check[0])]), to_check[0], data)
        for coord in basin:
            if coord in to_check:
                to_check.remove(coord)
        top_basins.append(len(basin))
    top_basins.sort(reverse=True)
    return np.prod(top_basins[:3])


if __name__ == "__main__":
    day = "09"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
