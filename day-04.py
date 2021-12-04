import pandas as pd
import numpy as np
import re

def read_file(day):
    data = {}
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data['order'] = fin.readline().rstrip().split(",")
        data['bingos'] = fin.read().split('\n\n')
        for i in range(len(data['bingos'])):
            data['bingos'][i] = data['bingos'][i].strip().split("\n")
            for j in range(len(data['bingos'][i])):
                data['bingos'][i][j] = re.sub(' +', ' ', data['bingos'][i][j]).strip().split(" ")
    return data

def check_bingo(bingo):
    for line in bingo:
        if not any(line):
            return True
    bingo = np.transpose(np.array(bingo)).tolist()
    for line in bingo:
        for i in range(len(line)):
            if line[i] == 'False':
                line[i] = False
        if not any(line):
            bingo = np.transpose(np.array(bingo)).tolist()
            return True

def suma_bingo(bingo):
    return sum([int(i) for line in bingo for i in line])

def process_data_1(data):
    for num in data['order']:
        for bingo in data['bingos']:
            for line in bingo:
                if num in line:
                    for i in range(len(line)):
                        if line[i] == num:
                            line[i] = False
                            if check_bingo(bingo):
                                suma = suma_bingo(bingo)
                                return suma*int(num)
                            break
    return "No bingo"

def process_data_2(data):
    order_winners = []
    for num in data['order']:
        for bingo in range(len(data['bingos'])):
            if bingo not in order_winners:
                for line in data['bingos'][bingo]:
                    if num in line:
                        for i in range(len(line)):
                            if line[i] == num:
                                line[i] = False
                                if check_bingo(data['bingos'][bingo]):
                                    order_winners.append(bingo)
                                break
        if len(order_winners) == len(data['bingos']):
            break
    return suma_bingo(data['bingos'][order_winners[-1]])*int(num)


if __name__ == "__main__":
    day = "04"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
