import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [int(i.split(" ")[-1]) for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    score = [0, 0]
    positions = data
    jugador = 0
    tirades = 0
    while max(score)<1000:
        positions[jugador] = ( (positions[jugador]+3*tirades+5)%10 )+1
        tirades = (tirades + 3)%1000
        score[jugador] += positions[jugador]
        jugador = (jugador+1)%2

    return min(score) * tirades

def multiverse(positions, score, jugador, num_multiverse):
    winners = [0,0]
    # sum of 3 numbers between 1,2,3 can only be 7 different values, from 3 to 9
    universe_multiplier = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    for i in range(3,10):
        new_score = score[jugador] + ( (positions[jugador]+i-1)%10 )+1
        if new_score >= 21:
            winners[jugador] += universe_multiplier[i]
        else:
            new_positions, new_scores = positions.copy(), score.copy()
            new_positions[jugador] = ( (positions[jugador]+i-1)%10 )+1
            new_scores[jugador] = new_score
            win1, win2 = multiverse(new_positions, new_scores, (jugador+1)%2, num_multiverse+1)
            winners[0] += win1*universe_multiplier[i]
            winners[1] += win2*universe_multiplier[i]
    return winners

def process_data_2(data):
    score = [0, 0]
    positions = data
    jugador = 0
    winners = multiverse(positions, score, jugador, 1)
    print(winners)
    return max(winners)


if __name__ == "__main__":
    day = "21"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
