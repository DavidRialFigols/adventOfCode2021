import copy
import operator
import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[int(i) for i in j] for j in fin.read().rstrip().split("\n")]
        min_scores = {}
        for line in range(len(data)):
            for col in range(len(data[0])):
                min_scores[f"{line}-{col}"] = float('inf')

    return data, min_scores

def greedy(data, min_scores, path, score):
    stack = [(path, score)]
    continuar = True
    while continuar:
        path, score = stack.pop()
        x,y = path[-1]
        continuar = (x,y) != (len(data)-1, len(data[0])-1)
        if continuar:
            if y+1 == len(data) or (x+1<len(data) and data[x+1][y] <= data[x][y+1]):
                next_score = score + data[x+1][y]
                stack.append((path+[(x+1,y)], next_score))
            else: 
                next_score = score + data[x][y+1]
                stack.append((path+[(x,y+1)], next_score))
    return score


def greedy_inv(data, min_scores, pos, score):
    x,y = pos[-1]
    if (x,y) == (0, 0):
        return score
    if x == 0 or (y > 0 and data[x][y-1] <= data[x-1][y]):
        return greedy_inv(data, min_scores, pos + [(x, y-1)], score+data[x][y-1])
    else:
        return greedy_inv(data, min_scores, pos + [(x-1, y)], score+data[x-1][y])


def search_path_with_turns(data, min_scores, path, score):
    global MIN_SCORE_FOUND
    stack = [(path, score, len(data)+len(data[0]))]
    sides = [(1,0),(0,1),(-1,0),(0,-1)]
    continuar = True
    while continuar:
        path, score, dist_end = stack.pop()
        x,y = path[-1]
        continuar = (x,y) != (len(data)-1, len(data[0])-1)
        if continuar:
            for di,dj in sides:
                if x+di>= 0 and x+di <= len(data)-1:
                    if y+dj>=0 and y+dj<= len(data[0])-1:
                        if (x+di,y+dj) not in path:
                            next_score = score + data[x+di][y+dj]
                            if min_scores[f"{x+di}-{y+dj}"] > next_score:
                                min_scores[f"{x+di}-{y+dj}"] = next_score
                                if max(di, dj) == 1: dist_to_end = dist_end-1
                                else: dist_to_end = dist_end+1
                                # print(f"coord: ({x+di,y+dj}) | dist_end: {dist_to_end}")
                                if next_score + dist_to_end < MIN_SCORE_FOUND:
                                    stack.append((path+[(x+di,y+dj)], next_score, dist_to_end))
        stack = sorted(stack, key=operator.itemgetter(1, 2), reverse=True)
    return score


def process_data_1(data, min_scores):
    global MIN_SCORE_FOUND
    MIN_SCORE_FOUND = search_path_with_turns(data, min_scores, [(0,0)], 0)
    return MIN_SCORE_FOUND

def process_data_2(data):
    data = np.array(data).transpose().tolist()
    for line in range(len(data)):
        length_line = len(data[line])
        for i in range(4):
            data[line] += [(j+i)%9+1 for j in data[line][:length_line]]
    data = np.array(data).transpose().tolist()
    for line in range(len(data)):
        length_line = len(data[line])
        for i in range(4):
            data[line] += [(j+i)%9+1 for j in data[line][:length_line]]
    print(len(data))
    print(len(data[0]))
    for line in range(len(data)):
        for col in range(len(data[0])):
            min_scores[f"{line}-{col}"] = float('inf')
    global MIN_SCORE_FOUND
    MIN_SCORE_FOUND = float('inf')
    MIN_SCORE_FOUND = search_path_with_turns(data, min_scores, [(0,0)], 0)
    return MIN_SCORE_FOUND


if __name__ == "__main__":
    global MIN_SCORE_FOUND
    MIN_SCORE_FOUND = float('inf')
    day = "15"
    data, min_scores = read_file(day)
    print(data)
    print(len(data), len(data[0]))
    result_1 = process_data_1(copy.deepcopy(data), copy.deepcopy(min_scores))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
