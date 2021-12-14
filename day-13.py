import numpy as np
import itertools

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n\n")
        data = {
            'coords': [ [int(i.split(',')[0]), int(i.split(',')[1])] for i in data[0].split('\n')],
            'instructions': data[1].split('\n')
        }
        for i in range(len(data['instructions'])):
            data['instructions'][i] = (data['instructions'][i].split(' ')[2].split('=')[0], int(data['instructions'][i].split(' ')[2].split('=')[1]))
    return data

def process_instruction(data, num_instruction):
    instr = data['instructions'][num_instruction]
    if instr[0] == 'x': axis=0
    else: axis=1
    for i in range(len(data['coords'])):
        if data['coords'][i][axis] > instr[1]:
            data['coords'][i][axis] -= 2*(data['coords'][i][axis] - instr[1])
    data['coords'].sort()
    data['coords'] = [k for k,_ in itertools.groupby(data['coords'])]
    return data

def process_data_1(data):
    data = process_instruction(data, 0)
    print(data['coords'])
    return len(process_instruction(data, 0)['coords'])

def process_data_2(data):
    for i in range(len(data['instructions'])):
        data = process_instruction(data, i)

    max_coords = ( max([i[0] for i in data['coords']]), max([i[1] for i in data['coords']]))
    print(max_coords)
    tauler = [[False for i in range(max_coords[1]+1)] for j in range(max_coords[0]+1)]
    for coord in data['coords']:
        tauler[coord[0]][coord[1]] = True
    for i in range(max_coords[1]+1):
        line = ''
        for j in range(max_coords[0]+1):
            if tauler[j][i]:
                line += '#'
            else: line += ' '
        print(line)
    return


if __name__ == "__main__":
    day = "13"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(np.copy(data).tolist())
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
