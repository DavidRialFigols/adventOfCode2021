import copy
import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split(" ") for i in fin.read().rstrip().split("\n")]
        for line in data:
            line[0] = line[0] == "on"
            line[1] = [i[2:].split("..") for i in line[1].split(",")]
            for i in line[1]:
                i[0], i[1] = int(i[0]), int(i[1])
    return data

def init_cube(min_coord, max_coord):
    return np.array([[[False for z in range(max_coord-min_coord)] for y in range(max_coord-min_coord)] for x in range(max_coord-min_coord)])

def process_data_1(data):
    min_coord, max_coord = -50, 50
    move_center = -min_coord
    cube = init_cube(min_coord,max_coord)
    for instruction in data:
        x_coords, y_coords, z_coords = instruction[1][0], instruction[1][1], instruction[1][2]
        cube[x_coords[0]+move_center:x_coords[1]+1+move_center, y_coords[0]+move_center:y_coords[1]+1+move_center, z_coords[0]+move_center:z_coords[1]+1+move_center] = instruction[0]
    return np.sum(cube)

def process_data_2(data):
    


if __name__ == "__main__":
    day = "22"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
