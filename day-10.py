import numpy as np

inverse = {'[': ']', '(': ')', '{': '}', '<':'>'}
valors_1 = {')':3, ']':57, '}':1197, '>':25137}
valors_2 = {')':1, ']':2, '}':3, '>':4}

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[c for c in i] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    suma = 0
    for line in data:
        stack = []
        for c in line:
            if c in inverse:
                stack.append(c)
            elif inverse[stack[-1]]==c:
                stack.pop()
            else:
                suma += valors_1[c]
                break
    return suma

def process_data_2(data):
    valors = []
    for line in data:
        stack = []
        wrong_line = False
        for c in line:
            if c in inverse:
                stack.append(c)
            elif inverse[stack[-1]]==c:
                stack.pop()
            else:
                wrong_line = True
                break
        if not wrong_line:
            line_value = 0
            while len(stack) > 0:
                line_value *= 5
                line_value += valors_2[inverse[stack.pop()]]
            valors.append(line_value)
    print(f"valors: {valors}")
    valors.sort()
    return valors[int((len(valors)-1)/2)]


if __name__ == "__main__":
    day = "10"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
