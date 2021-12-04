def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [int(i) for i in fin.read().splitlines()]
    return data

def process_data_1(data):
    last = data[0]
    counter = 0
    for i in data:
        if i > last: counter += 1
        last = i
    return counter

def process_data_2(data):
    last = sum(data[:3])
    counter = 0
    for i in range(1, len(data)-2):
        new = sum(data[i:i+3])
        if new > last: counter += 1
        last = new
    return counter


if __name__ == "__main__":
    day = "01"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")