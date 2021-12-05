import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split(" -> ") for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    lines = {}
    coincidences = set()
    for l in data:
        start = (int(l[0].split(',')[0]), int(l[0].split(',')[1]))
        end = (int(l[1].split(',')[0]), int(l[1].split(',')[1]))
        if start[0] == end[0]:
            if start[0] not in lines:
                lines[start[0]] = []
            max_coord, min_coord = max(start[1], end[1]), min(start[1], end[1])
            for i in range(min_coord, max_coord+1):
                if i in lines[start[0]]:
                    coincidences.add((start[0], i))
                else:
                    lines[start[0]].append(i)
        if start[1] == end[1]:
            max_coord, min_coord = max(start[0], end[0]), min(start[0], end[0])
            for i in range(min_coord, max_coord+1):
                if i not in lines:
                    lines[i] = []
                if start[1] in lines[i]:
                    coincidences.add((i, start[1]))
                else:
                    lines[i].append(start[1])
    return len(coincidences)

def process_data_2(data):
    lines = {}
    coincidences = set()
    for l in data:
        start = (int(l[0].split(',')[0]), int(l[0].split(',')[1]))
        end = (int(l[1].split(',')[0]), int(l[1].split(',')[1]))
        if start[0] == end[0]:
            if start[0] not in lines:
                lines[start[0]] = []
            max_coord, min_coord = max(start[1], end[1]), min(start[1], end[1])
            for i in range(min_coord, max_coord+1):
                if i in lines[start[0]]:
                    coincidences.add((start[0], i))
                else:
                    lines[start[0]].append(i)
        elif start[1] == end[1]:
            max_coord, min_coord = max(start[0], end[0]), min(start[0], end[0])
            for i in range(min_coord, max_coord+1):
                if i not in lines:
                    lines[i] = []
                if start[1] in lines[i]:
                    coincidences.add((i, start[1]))
                else:
                    lines[i].append(start[1])
        if start[0] - end[0] == start[1] - end[1]:
            max_coord, min_coord = max(start[0], end[0]), min(start[0], end[0])
            diff = start[0] - start[1]
            for i in range(max_coord-min_coord+1):
                if min_coord+i not in lines:
                    lines[min_coord+i] = []
                if (min_coord+i) - diff in lines[min_coord+i]:
                    coincidences.add((min_coord+i, (min_coord+i)-diff))
                else:
                    lines[min_coord+i].append((min_coord+i)-diff)
        elif start[0] + start[1] == end[0] + end[1]:
            if start[0] < end[0]:
                start, end = end, start
            for i in range(start[0]-end[0]+1):
                if start[0]-i not in lines:
                    lines[start[0]-i] = []
                if start[1]+i in lines[start[0]-i]:
                    coincidences.add((start[0]-i, start[1]+i))
                else:
                    lines[start[0]-i].append(start[1]+i)
    print(lines)
    return len(coincidences)


if __name__ == "__main__":
    day = "05"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
