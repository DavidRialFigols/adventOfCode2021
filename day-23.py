import copy

def read_file(day):
    letter_conversion = {'A':0, 'B':2, 'C':4, 'D':6}
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")[2:4]
        print(data)
        data.append([letter_conversion[data[0][3]], letter_conversion[data[1][3]]])
        data.append([letter_conversion[data[0][5]], letter_conversion[data[1][5]]])
        data.append([letter_conversion[data[0][7]], letter_conversion[data[1][7]]])
        data.append([letter_conversion[data[0][9]], letter_conversion[data[1][9]]])
        data = data[2:]
    return data

def obtain_possible_moves(positions):
    # positions = {(position x, position y): letter, ...}
    # returns a list of possible moves
    # One move is represented like ((xo, yo), n) where n means:
    # 0: move up
    # 1: move right
    # 2: move down
    # 3: move right
    pm = []
    for pos in positions.keys():
        if pos[1]==0 and positions[pos]==pos[0]: # the letter is in the bottom of the correct room
            continue
        if pos[1]==1 and positions[pos]==pos[0] and (pos[0],0) in positions and positions[(pos[0],0)]==pos[0]: # the room is completed
            continue
        if (pos[0]+1,pos[1]) not in positions and :
        if (pos[0],pos[1]+1) not in positions:
        if (pos[0]-1,pos[1]) not in positions:
        if (pos[0],pos[1]-1) not in positions:
    return pm

def process_data_1(data):

    return

def process_data_2(data):
    return

energy_consumption = {0:1, 1:10, 2:100, 3:1000}

if __name__ == "__main__":
    day = "23"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
