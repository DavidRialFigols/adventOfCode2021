def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split(",")
    data_dict = {}
    for i in range(10):
        data_dict[i] = 0
    print(data_dict)
    for i in data:
        data_dict[int(i)] += 1
    return data_dict

def calc_number_fish(data, days):
    for i in range(days):
        for key in data:
            if key == 0:
                data[9] += data[0]
                data[7] += data[0] 
                data[0] = 0
            else:
                data[key-1] += data[key]
                data[key] = 0
    return sum(data.values())

def process_data_1(data):
    return calc_number_fish(data, 80)

def process_data_2(data):
    return calc_number_fish(data, 256)


if __name__ == "__main__":
    day = "06"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data.copy())
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data.copy())
    print(f"result 2: {result_2}")
