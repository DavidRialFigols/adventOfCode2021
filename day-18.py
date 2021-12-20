import copy

def make_array(text_array):
    array = []
    num_open_array, i = 0, 0
    found_array = False
    while i<len(text_array):
        if text_array[i] == '[':
            num_open_array += 1
            if not found_array:
                found_array = True
                start_array = i
            i+=1
        elif text_array[i] == ']':
            num_open_array -= 1
            if num_open_array == 0:
                found_array = False
                array.append(make_array(text_array[start_array+1:i]))
            i+=1
        elif found_array or text_array[i] == ',':
            i+=1
        else: 
            array.append(int(text_array[i]))
            i += 1

    return array

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
        for i in range(len(data)):
            if data[i][0] == '[':
                data[i] = make_array(data[i][1:-1])
    return data

def calc_magnitude(pair):
    value_left = 3
    if type(pair[0]) == int: value_left *= pair[0]
    else: value_left *= calc_magnitude(pair[0]) 

    value_right = 2
    if type(pair[1]) == int: value_right *= pair[1]
    else: value_right *= calc_magnitude(pair[1])

    return value_left + value_right

def split(number):
    if number%2 == 0: return [int(number/2), int(number/2)]
    else: return [int((number-1)/2), int((number+1)/2)]

def add_sum(pair, value, side):
    if type(pair[side]) == int:
        pair[side] += value
    else:
        pair[side] = add_sum(pair[side], value, side)
    return pair

def check_explode(pair, depth, sum_left, sum_right):
    explode = False
    # print(f"ENTRADA | depth: {depth} | pair: {pair} | sum_left: {sum_left} | sum_right: {sum_right} | explode: {explode}")
    if depth == 5:
        if sum_left: pair[0] += sum_left
        if sum_right: pair[1] += sum_right
        # print(f"EXPLODE | depth: {depth} | pair: {pair} | sum_left: {pair[0]} | sum_right: {pair[1]} | explode: {explode}")
        return 0, pair[0],pair[1], True
    if type(pair[0]) == list:
        result = check_explode(pair[0], depth+1, False, sum_left)
        pair[0], sum_left, sum_inner_right, explode = result[0], result[1], result[2], result[3]
        if type(pair[1]) == int and sum_inner_right:
            pair[1] += sum_inner_right
        elif sum_inner_right:
            pair[1] = add_sum(pair[1], sum_inner_right, 0)
    else:
        if sum_left:
            pair[0] += sum_left
            sum_left = False
    if type(pair[1]) == list:
        result = check_explode(pair[1], depth+1, sum_right, False)
        pair[1], sum_inner_left, sum_right, explode_right = result[0], result[1], result[2], result[3]
        explode = explode or explode_right
        if type(pair[0]) == int and sum_inner_left:
            pair[0] += sum_inner_left
        elif sum_inner_left:
            pair[0] = add_sum(pair[0], sum_inner_left, 1)
    else:
        if sum_right:
            pair[1] += sum_right
            sum_right = False
    # print(f"SORTIDA | depth: {depth} | pair: {pair} | sum_left: {sum_left} | sum_right: {sum_right} | explode: {explode}")
    ended_check = depth==1 and explode==False
    return pair, sum_left, sum_right, explode, ended_check

def check_split(pair):
    # print(f"ENTRADA | pair: {pair}")
    has_split = False
    if type(pair[0]) == list:
        pair[0], has_split = check_split(pair[0])
        if has_split:
            # print(f"SORTIDA | pair: {pair} | has_split: {has_split}")
            return pair, has_split
    else:
        if pair[0] >= 10:
            # print(f"SPLIT | pair: {pair}")
            pair[0] = split(pair[0])
            has_split = True
            # print(f"SORTIDA | pair: {pair} | has_split: {has_split}")
            return pair, has_split

    if type(pair[1]) == list:
        pair[1], has_split_right = check_split(pair[1])
        has_split = has_split or has_split_right
    else:
        if pair[1] >= 10:
            # print(f"SPLIT | pair: {pair}")
            pair[1] = split(pair[1])
            has_split = True

    # print(f"SORTIDA | pair: {pair} | has_split: {has_split}")
    return pair, has_split


def recursive(pair):
    continuar = True
    while continuar:
        ended_check = False
        explode = False
        while not ended_check:
            pair, sum_left, sum_right, explode_aux, ended_check = check_explode(pair, 1, False, False)
            ended_check = ended_check and not explode_aux
            explode = explode or explode_aux
        pair, has_split = check_split(pair)
        continuar = has_split
    return pair


def process_data_1(data):
    suma = data[0]
    for i in range(1, len(data)):
        suma = [suma]
        suma.append(data[i])
        suma = recursive(suma)
    return calc_magnitude(suma)

def process_data_2(data):
    max_mag = 0
    for i in data:
        for j in data:
            if i!=j:
                mag = calc_magnitude(recursive([copy.deepcopy(i), copy.deepcopy(j)]))
                if mag > max_mag:
                    print(f"i: {i} | j: {j} | magnitude: {mag}")
                    max_mag = mag
    return max_mag


if __name__ == "__main__":
    day = "18"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
