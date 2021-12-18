import copy
import math

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split(" ")
        print(data)
        data = (data[2].split('..'), data[3].split('..'))
        data[0][0] = int(data[0][0][2:])
        data[0][1] = int(data[0][1][:-1])
        data[1][0] = int(data[1][0][2:])
        data[1][1] = int(data[1][1])
    return data

def calc_trajectory_1(data, vx, vy):
    x, y = 0,0
    max_y = 0
    while (y > data[1][0]):
        x += vx
        y += vy
        if vx > 0: vx -=1
        vy -= 1
        if y > max_y:
            max_y = y
        if x <= data[0][1] and x >= data[0][0] and y>=data[1][0] and y<=data[1][1]:
            if vy < 0:
                return max_y
    return False


def calc_trajectory_2(data, vx, vy):
    x, y = 0,0
    max_y = 0
    while (y > data[1][0]):
        x += vx
        y += vy
        if vx > 0: vx -=1
        vy -= 1
        if y > max_y:
            max_y = y
        if x <= data[0][1] and x >= data[0][0] and y>=data[1][0] and y<=data[1][1]:
            return True
    return False




def process_data_1(data):
    min_x = round(math.sqrt(abs(data[0][0])*2)-1)
    while min_x*(min_x+1)/2 < abs(data[0][0]):
        min_x += 1
    #if data[0][0] < 0: min_x *= -1

    max_x = round(math.sqrt(abs(data[0][1])*2))
    while max_x*(max_x+1)/2 > abs(data[0][1]):
        max_x -= 1
    #if data[0][1] < 0: max_x *= -1
    
    abs_data = ([min(abs(data[0][0]), abs(data[0][1])), max(abs(data[0][0]), abs(data[0][1]))],data[1])
    max_y = 0
    for vx in range(abs(max_x), abs(min_x)-1, -1):
        for vy in range(0, 150):
            pos_max_y = calc_trajectory_1(data, vx, vy)
            if pos_max_y and pos_max_y > max_y:
                max_y = pos_max_y
    
    return max_y

def process_data_2(data):
    min_x = round(math.sqrt(abs(data[0][0])*2)-1)
    while min_x*(min_x+1)/2 < abs(data[0][0]):
        min_x += 1
    #if data[0][0] < 0: min_x *= -1

    max_x = round(math.sqrt(abs(data[0][1])*2))
    while max_x*(max_x+1)/2 > abs(data[0][1]):
        max_x -= 1
    #if data[0][1] < 0: max_x *= -1
    
    abs_data = ([min(abs(data[0][0]), abs(data[0][1])), max(abs(data[0][0]), abs(data[0][1]))],data[1])
    max_y = 0
    possibilities = 0
    for vx in range(abs(max_x)+350, abs(min_x)-350, -1):
        for vy in range(-75, 500):
            possibilities += int(calc_trajectory_2(data, vx, vy))
    
    return possibilities


if __name__ == "__main__":
    day = "17"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
