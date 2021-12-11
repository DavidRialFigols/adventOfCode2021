import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[int(c) for c in i] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    flashes = 0
    entorn = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(1,-1),(1,0),(1,1)]
    for step in range(100):
        flashing = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1
                if data[i][j] > 9:
                    flashing.append((i,j))
        new_flashes = flashing.copy()
        while len(new_flashes) > 0:
            x,y = new_flashes.pop()
            for di, dj in entorn:
                if x+di>=0 and x+di < len(data):
                    if y+dj>=0 and y+dj < len(data[0]):
                        if (x+di,y+dj) not in flashing:
                            data[x+di][y+dj] += 1
                            if data[x+di][y+dj] > 9:
                                flashing.append((x+di,y+dj))
                                new_flashes.append((x+di,y+dj))
        for x,y in flashing:
            flashes += 1
            data[x][y] = 0
    return flashes

def process_data_2(data):
    flashing = []
    step = 0
    entorn = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(1,-1),(1,0),(1,1)]
    while len(flashing) < 100:
        flashing = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1
                if data[i][j] > 9:
                    flashing.append((i,j))
        new_flashes = flashing.copy()
        while len(new_flashes) > 0:
            x,y = new_flashes.pop()
            for di, dj in entorn:
                if x+di>=0 and x+di < len(data):
                    if y+dj>=0 and y+dj < len(data[0]):
                        if (x+di,y+dj) not in flashing:
                            data[x+di][y+dj] += 1
                            if data[x+di][y+dj] > 9:
                                flashing.append((x+di,y+dj))
                                new_flashes.append((x+di,y+dj))
        for x,y in flashing:
            data[x][y] = 0
        step += 1
    return step


if __name__ == "__main__":
    day = "11"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(np.copy(data).tolist())
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
