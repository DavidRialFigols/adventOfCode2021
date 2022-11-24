import copy

def read_file(day):
    letter_conversion = {'A':0, 'B':2, 'C':4, 'D':6}
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = fin.read().rstrip().split("\n")[2:4]
        aux.append([letter_conversion[aux[0][3]], letter_conversion[aux[1][3]]])
        aux.append([letter_conversion[aux[0][5]], letter_conversion[aux[1][5]]])
        aux.append([letter_conversion[aux[0][7]], letter_conversion[aux[1][7]]])
        aux.append([letter_conversion[aux[0][9]], letter_conversion[aux[1][9]]])
        aux = aux[2:]
        data = 

    return data

def obtain_state_from_positions(positions):
    # a state is: (A1,A2,B1,B2,C1,C2,D1,D2) and each letter is (x,y)
    aux = []
    for pos in positions.keys():
        aux.append([positions[pos],pos])
    aux = sorted(aux, key=lambda x: x[0]+x[1][1])
    state = tuple([i[1] for i in aux])
    return state

states = {}

def obtain_possible_moves(state, actual_cost):
    # state = (A1,A2,B1,B2,C1,C2) where each letter is (x,y)
    # returns a list of possible next states with its cost
    ns = []
    
    if actual_cost > states[state]: return ns

    state = list(state)
    for i, pos in enumerate(state):
        letter = int(i/2)*2
        if pos[1]==0 and letter==pos[0]: # the letter is in the bottom of the correct room
            continue
        if pos[1]==1 and letter==pos[0] and (pos[0],0) in state: # the room has another letter
            if int(state.index((pos[0],0))/2)*2==letter: # the letter that is in the room is also good
                continue
        if pos[0]< 8 and pos[0] not in [0,2,4,6] and (pos[0]+1,pos[1]) not in state: # it can go right
            # if it is its correct room, it will move down if possible, if not it will not move
            # if it is not its correct room, it will continue moving right until it finds its room
            extra_cost = energy_consumption[letter]
            moving = letter>pos[0]
            moves_right = 1
            while (moving):
                if moves_right > 10: raise Exception("To many moves to the right!") # just to be sure there is no problem here
                if letter==pos[0]+moves_right: # it is its correct room
                    moving = False
                    if (pos[0]+moves_right, pos[1]-1) not in state: # there are empty spaces in the room
                        if (pos[0]+moves_right, pos[1]-2) not in state: # there are no letters in the room
                            fs = [state[j] if i!=j else (pos[0]+moves_right, 0) for j in range(len(state))]
                            if (fs not in states) or (states[fs]>actual_cost+extra_cost):
                                ns.append((fs, actual_cost+extra_cost+2*energy_consumption[letter]))
                        elif (int(state.index((pos[0]+moves_right,0))/2)*2==letter): # there is one more letter in the bottom of the room and it is a correct one
                            fs = [state[j] if i!=j else (pos[0]+moves_right, 1) for j in range(len(state))]
                            ns.append((fs, actual_cost+extra_cost+energy_consumption[letter]))
                else:
                    moves_right+=1
                    extra_cost += energy_consumption[letter]

        if ((pos[1] == 1) or (pos[1]==0 and (pos[0],1) not in state)) and (pos[0],2) not in state: # it can go up
            for j in [-1,1]: # moves up and side
                extra_cost = energy_consumption[letter]*(2-pos[1])
                movements = 1
                while ((pos[0]+j*movements >= -2) and (pos[0]+j*movements <= 8) and ((pos[0]+j*movements, 2) not in state)): # just to be sure the movement is inside the limits
                    if letter==pos[0]+j*movements: # it is its correct room, check if it can go down
                        if (pos[0]+j*movements, 1) not in state: # there are empty spaces in the room
                            if (pos[0]+j*movements, pos[1]-2) not in state: # there are no letters in the room
                                fs = [state[j] if i!=j else (pos[0]+j*movements, 0) for j in range(len(state))]
                                if (fs not in states) or (states[fs]>actual_cost+extra_cost):
                                    ns.append((fs, actual_cost+extra_cost+2*energy_consumption[letter]))
                                    break
                            elif (int(state.index((pos[0]+j*movements,0))/2)*2==letter): # there is one more letter in the bottom of the room and it is a correct one
                                fs = [state[j] if i!=j else (pos[0]+j*movements, 1) for j in range(len(state))]
                                ns.append((fs, actual_cost+extra_cost+energy_consumption[letter]))
                                break
                    elif pos[0]+j*movements not in [0,2,4,6]:
                        fs = [state[j] if i!=j else (pos[0]+j*movements, 2) for j in range(len(state))]
                        ns.append((fs, actual_cost+extra_cost))

                    movements+=1
                    extra_cost += energy_consumption[letter]


        if pos[0]>-2 and pos[0] not in [0,2,4,6] and (pos[0]-1,pos[1]) not in state: # it can go left
            # if it is its correct room, it will move down if possible, if not it will not move
            # if it is not its correct room, it will continue moving right until it finds its room
            extra_cost = energy_consumption[letter]
            moving = letter<pos[0]
            moves_left = 1
            while (moving):
                if moves_left > 10: raise Exception("To many moves to the right!") # just to be sure there is no problem here
                if letter==pos[0]-moves_left: # it is its correct room
                    moving = False
                    if (pos[0]-moves_left, pos[1]-1) not in state: # there are empty spaces in the room
                        if (pos[0]-moves_left, pos[1]-2) not in state: # there are no letters in the room
                            fs = [state[j] if i!=j else (pos[0]-moves_left, pos[1]-2) for j in range(len(state))]
                            if (fs not in states) or (states[fs]>actual_cost+extra_cost):
                                ns.append((fs, actual_cost+extra_cost+2*energy_consumption[letter]))
                        elif (int(state.index((pos[0]-moves_left,0))/2)*2==letter): # there is one more letter in the bottom of the room and it is a correct one
                            ns.append((fs, actual_cost+extra_cost+energy_consumption[letter]))
                else:
                    moves_left+=1
                    extra_cost += energy_consumption[letter]
    return ns

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
