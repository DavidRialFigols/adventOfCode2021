import pandas as pd

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[ch for ch in num] for num in fin.read().splitlines()]
    return data

def process_data_1(data):
    result = []
    num_data = len(data)
    for i in range(len(data[0])):
        if sum([int(num[i]) for num in data])/float(num_data) >= 0.5: result.append('1')
        else: result.append('0')
    result_inv = [str((int(i)+1)%2) for i in result]
    result = int(''.join(result), 2)
    result_inv = int(''.join(result_inv), 2)
    return result*result_inv

def process_data_2(data):
    df = pd.DataFrame(data, columns=[f"bit{i}" for i in range(len(data[0]))])
    for i in range(len(data[0])):
        mean = sum(df[f"bit{i}"].apply(lambda x: int(x)))/float(df.shape[0])
        if mean >= 0.5: bit = '1'
        else: bit = '0'
        df = df[df[f"bit{i}"] == bit]
        if df.shape[0] == 1:
            oxy = ''.join(df.iloc[0].tolist())
            break
    
    df = pd.DataFrame(data, columns=[f"bit{i}" for i in range(len(data[0]))])
    for i in range(len(data[0])):
        mean = sum(df[f"bit{i}"].apply(lambda x: int(x)))/float(df.shape[0])
        if mean >= 0.5: bit = '0'
        else: bit = '1'
        df = df[df[f"bit{i}"] == bit]
        if df.shape[0] == 1:
            co2 = ''.join(df.iloc[0].tolist())
            break
    oxy = int(oxy, 2)
    co2 = int(co2, 2)
    return oxy*co2


if __name__ == "__main__":
    day = "03"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2:{result_2}")
