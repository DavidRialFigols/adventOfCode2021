import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        iea = fin.readline().rstrip()
        img = fin.read().rstrip().split("\n")[1:]
        data = {"iea":iea, "img":img}
    return data

def add_outside(img, rows, cols, extra):
    out = [''.join([extra for j in range(cols+4)])]
    out += [out[0]]
    for i in range(rows):
        out += [extra+extra+img[i]+extra+extra]
    out += [out[0]]
    out += [out[0]]
    return out

def step(data, inft):
    img = data['img']
    rows, cols = len(img), len(img[0])
    extra = '-'
    img = add_outside(img, rows, cols, extra)
    next_img = copy.deepcopy(img)
    for i in range(rows+2):
        for j in range(cols+2):
            # center point is in i+2, j+1
            # i have to check: +0, +1 and +2
            num = int((img[i][j:j+3] + img[i+1][j:j+3] + img[i+2][j:j+3]).replace(extra, inft).replace('.','0').replace('#','1'), base=2)
            next_img[i+1] = next_img[i+1][:j+1] + data['iea'][num] + next_img[i+1][j+2:]
    data['img'] = next_img
    return data

def process_data_1(data):
    extra = '.'
    for i in range(2):
        if data['iea'][0] == '#':
            if i%2==1:
                extra = '#'
            elif data['iea'][-1] == '.':
                extra = '.'
        data = step(data, extra)

    num_lit = 0
    for line in data['img']:
        num_lit += line.count('#')

    return num_lit

def process_data_2(data):
    extra = '.'
    for i in range(50):
        if data['iea'][0] == '#':
            if i%2==1:
                extra = '#'
            elif data['iea'][-1] == '.':
                extra = '.'
        data = step(data, extra)

    num_lit = 0
    for line in data['img']:
        num_lit += line.count('#')

    return num_lit


if __name__ == "__main__":
    day = "20"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
