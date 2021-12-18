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

def recursive(pair, depth, sum_left, sum_right):
    print(f"ENTRADA | pair: {pair} | sum_left: {sum_left} | sum_right: {sum_right}")
    check_again = True
    second_pass = False
    while check_again:
        check_again = False
        if depth == 5:
            print(f"EXPLODE | pair: {pair} | sum_left: {pair[0]} | sum_right: {pair[1]}")
            return 0, pair[0],pair[1]
        if type(pair[0]) == list:
            result = recursive(pair[0], depth+1, False, sum_left)
            pair[0], sum_left, sum_right = result[0], result[1], result[2]
            if type(pair[1]) == int and sum_right:
                pair[1] += sum_right
                sum_right = False
        else:
            if sum_left:
                pair[0] += sum_left
                sum_left = False
            if second_pass and sum_min_left:
                pair[0] += sum_min_left
                sum_left = False
            if pair[0] >= 10:
                print(f"SPLIT | pair: {pair} | sum_left: {sum_left} | sum_right: {sum_right}")
                pair[0] = split(pair[0])
                result = recursive(pair[0], depth+1, False, sum_left)
                pair[0], sum_left, sum_right = result[0], result[1], result[2]
                if type(pair[1]) == int and sum_right:
                    pair[1] += sum_right
                    sum_right = False

        if type(pair[1]) == list:
            result = recursive(pair[1], depth+1, sum_right, False)
            pair[1], sum_left, sum_right = result[0], result[1], result[2]
            if type(pair[0]) == int and sum_left:
                pair[0] += sum_left
                sum_left = False
                check_again = True
        elif not second_pass:
            if sum_right:
                pair[1] += sum_right
                sum_right = False
            if pair[1] >= 10:
                print(f"SPLIT | pair: {pair} | sum_left: {sum_left} | sum_right: {sum_right}")
                pair[1] = split(pair[1])
                result = recursive(pair[1], depth+1, sum_right, False)
                pair[1], sum_min_left, sum_right = result[0], result[1], result[2]
                if type(pair[0]) == int and sum_min_left:
                    pair[0] += sum_min_left
                    sum_min_left = False
                    check_again = True
                    second_pass = True

    print(f"SORTIDA | pair: {pair} | sum_left: {sum_left} | sum_right: {sum_right}")
    return pair, sum_left, sum_right


def process_data_1(data):
    suma = [data[0]]
    for i in range(1, len(data)):
        suma.append(data[i])
        print(f'SUMA: {suma}')
        suma, sum_left, sum_right = recursive(suma, 1, False, False)
    print(suma)
    return calc_magnitude(suma)

def process_data_2(data):
    return


if __name__ == "__main__":
    day = "18"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
