import copy

def read_file(day):
    letter_conversion = {'A':0, 'B':1, 'C':2, 'D':3}
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
    # One move is represented like ((xo, yo), (xf, yf)) where (xo, yo) is the initial position and (xf, yf) is the final position
    pm = []
    for pos in positions.keys():
        if pos[1] == 2: # it means that the letter is at the bottom of the room
            if (pos[0], 1) in positions: # it has a letter above, so this letter can not move
                continue
            if positions[pos] == pos[0]: # the letter is in the correct room
                continue
            
            if (pos[0]-1, 0) not in positions:
                pm.append((pos, (pos[0]-1,0)))
            if (pos[0]+1, 0) not in positions:
                pm.append((pos, (pos[0]+1,0)))
            
        elif pos[1] == 1: # it means it has a letter under it
            


    

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
