import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split(" | ") for i in fin.read().rstrip().split("\n")]
    data = [(inp.split(" "), outp.split(" ")) for inp, outp in data]
    return data

def process_data_1(data):
    counter = 0
    for l in data:
        for outp in l[1]:
            if len(outp) in [2, 3, 4, 7]:
                counter += 1
    return counter

def process_data_2(data):
    counter = 0
    for line in data:
        nums = {}
        while len(nums) < 10:
            for n in line[0]:
                if len(n) == 2 and 1 not in nums:
                    nums[1] = set([c for c in n])
                elif len(n) == 3 and 7 not in nums:
                    nums[7] = set([c for c in n])
                elif len(n) == 4 and 4 not in nums:
                    nums[4] = set([c for c in n])
                elif len(n) == 7 and 8 not in nums:
                    nums[8] = set([c for c in n])
                if len(n) == 6 and ( (6 not in nums) or (0 not in nums) or (9 not  in nums) ) and ( 1 in nums ) and ( 4 in nums ):
                    letters = set([c for c in n])
                    if (6 not in nums) and (not nums[1].issubset(letters)):
                        nums[6] = letters
                        continue
                    if (9 not in nums) and (nums[4].issubset(letters)):
                        nums[9] = letters
                        continue
                    if (0 not in nums) and (6 in nums) and (9 in nums):
                        if letters != nums[6] and letters != nums[9]:
                            nums[0] = letters
                            continue
                if len(n) == 5 and ( (2 not in nums) or (5 not in nums) ) and (0 in nums) and (4 in nums) and (7 in nums) and (9 in nums):
                    for letter in n:
                        if (5 not in nums):
                            if (letter not in nums[7]) and (letter in nums[4]) and (letter in nums[0]):
                                nums[5] = set([c for c in n])
                                break
                        if (2 not in nums):
                            print(letter)
                            if ( (letter not in nums[7]) and (letter not in nums[9]) ):
                                print('trying 2')
                                nums[2] = set([c for c in n])
                                break
                if len(n) == 5 and (3 not in nums) and (5 in nums) and (2 in nums) and (1 in nums):
                    letters = set([c for c in n])
                    if (letters != nums[5]) and (letters != nums[2]):
                        nums[3] = letters
            print(f"nums: {nums} | len = {len(nums)}")
        num = ''
        for n in line[1]:
            letters = set([c for c in n])
            for i in nums:
                if letters == nums[i]:
                    num += str(i)
                    break
        counter += int(num)
        print(num)
    return counter


if __name__ == "__main__":
    day = "08"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(data)
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
