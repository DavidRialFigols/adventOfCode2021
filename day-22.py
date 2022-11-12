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

def calculate_interjections(actual_instructions, new_instruction):
    interjections = []
    new_block = new_instruction[1]
    for instruction in actual_instructions:
        block = instruction[1]
        for coord in range(3):
            has_interjection = ((block[coord][0]<=new_block[coord][0] and new_block[coord][0]<=block[coord][1]) or (new_block[coord][0]<=block[coord][0] and block[coord][0]<=new_block[coord][1]))
            if not has_interjection:
                break
        if has_interjection:
            interjection = []
            for coord in range(3):
                interjection.append([max(block[coord][0], new_block[coord][0]), min(block[coord][1], new_block[coord][1])])
            # if the instruction in actual_instruction was added, then subtract the interjection.
            # If the instruction in actual_instruction was subtracted, then it means there was a larger one that was added (cause there is no new block added if it is OFF).
            # So, when the instruction in actual_instruction is subtracted, the interjection has to be added.
            interjection = [not instruction[0], interjection]
            interjections.append(interjection)
    return interjections

def calculate_blocks(actual_instructions):
    num_blocks = 0
    for i in actual_instructions:
        b = i[1]
        if i[0]:
            num_blocks += (b[0][1]-b[0][0]+1) * ((b[1][1]-b[1][0]+1)) * ((b[2][1]-b[2][0]+1))
        else:
            num_blocks -= (b[0][1]-b[0][0]+1) * ((b[1][1]-b[1][0]+1)) * ((b[2][1]-b[2][0]+1))
    return num_blocks

def process_data_2(data):
    actual_instructions = []
    for instruction in data:
        action = instruction[0]
        interjections = calculate_interjections(actual_instructions, instruction)
        if action:
            actual_instructions.append(instruction)
        if len(interjections) > 0:
            for i in interjections:
                actual_instructions.append(i)

    return calculate_blocks(actual_instructions)
    


if __name__ == "__main__":
    day = "22"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
