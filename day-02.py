def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [tuple(i.split(" ")) for i in fin.read().splitlines()]
    return data

def process_data_1(data):
    fw = depth = 0
    for move, i in data:
        if move == 'forward': fw += int(i)
        elif move == 'down': depth += int(i)
        elif move == 'up': depth -= int(i)
    return depth*fw

def process_data_2(data):
    fw = depth = aim = 0
    for move, i in data:
        if move == 'forward': 
            fw += int(i)
            depth += aim*int(i)
        elif move == 'down': aim += int(i)
        elif move == 'up': aim -= int(i)
    return depth*fw


if __name__ == "__main__":
    day = "02"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
