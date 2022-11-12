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

def calculate_interjection(actual_blocks, new_block):
    """
        1st: calculate interjection
        2nd: if the new instruction is ON, sum to the previous blocks the new blocks minus interjection
        3rd: if the new instruction is OFF, rest to the previous blocks the interjection
    """
    interjections = []
    for block in actual_blocks:
        for coord in range(3):
            has_interjection = ((block[coord][0]<=new_block[coord][0] and new_block[coord][0]<=block[coord][1]) or (new_block[coord][0]<=block[coord][0] and block[coord][0]<=new_block[coord][1]))
            if not has_interjection:
                break
        if has_interjection:
            interjection = []
            for coord in range(3):
                interjection.append([max(block[coord][0], new_block[coord][0]), min(block[coord][1], new_block[coord][1])])
            interjections.append(interjection)
    print()
    print(f'Interjections: {interjections}')
    print(f'Actual blocks: {actual_blocks}')
    print(f'New Block: {new_block}')

    return interjections
    
def remove_interjection(blocks, interjection):
    return blocks

def add_block(actual_blocks, new_block, interjections):
    # simplify new_block
    new_blocks = []
    
    
    actual_blocks.append(new_block)
    return actual_blocks

def remove_block(actual_blocks, interjection):
    return actual_blocks

def calculate_blocks(actual_blocks):
    return 26

def process_data_2(data):
    actual_blocks = []
    for i, instruction in enumerate(data):
        action = instruction[0]
        new_block = instruction[1]
        interjections = calculate_interjection(actual_blocks, new_block)
        if i==2:
            print()
            print()
            print(interjections)
            print(actual_blocks)
            print(new_block)
            break
        if action:
            add_block(actual_blocks, new_block, interjections)
        else:
            for interjection in interjections:
                remove_block(actual_blocks, interjection)

    return calculate_blocks(actual_blocks)
    


if __name__ == "__main__":
    day = "22"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
