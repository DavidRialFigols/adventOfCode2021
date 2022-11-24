
# Done by: https://github.com/Gravitar64/Advent-of-Code-2021/blob/main/Tag_23.py

from time import perf_counter as pfc
from heapq import heappop, heappush


def read_puzzle(filename):
  with open(filename) as f:
    return ''.join([c for c in f.read() if c in 'ABCD.'])


def can_leave_room(puzzle, room_pos):
  for a in room_pos:
    if puzzle[a] == '.': continue
    return a


def blocked(a,b,puzzle):
  step = 1 if a<b else -1
  for pos in range(a+step, b+step, step):
    if puzzle[pos] != '.': return True    


def get_possible_parc_pos(a,parc,puzzle):
  for b in [pos for pos in parc if puzzle[pos] == '.']:
    if blocked(a,b,puzzle): continue
    yield b


def move(a,b,puzzle):
  p = list(puzzle)
  p[a], p[b] = p[b], p[a]
  return ''.join(p)


def can_enter_room(a,b,amphi,puzzle,room_pos):
  for pos in room_pos:
    if puzzle[pos] == '.': best_pos = pos
    elif puzzle[pos] != amphi: return False
  if not blocked(a,b,puzzle): return best_pos


def possible_moves(puzzle, parc, stepout, target):
  for a in [pos for pos in parc if puzzle[pos] != '.']:
    amphi = puzzle[a]
    if (b:=can_enter_room(a, stepout[amphi], amphi, puzzle, target[amphi])):
      yield a,b
  for room in 'ABCD':
    if not (a:=can_leave_room(puzzle, target[room])): continue
    for b in get_possible_parc_pos(stepout[room], parc, puzzle):
      yield a,b


def solve(puzzle):
  energy = dict(A=1, B=10, C=100, D=1000)
  parc= [0,1,3,5,7,9,10]
  stepout = dict(A=2, B=4, C=6, D=8)
  target = {r: range(ord(r)-54,len(puzzle),4) for r in 'ABCD'}
  targetI = {v:key for key,val in target.items() for v in val}

  solution = '.'*11+'ABCD'*((len(puzzle)-11)//4)
  heap, seen = [(0,puzzle)], {puzzle:0}
  while heap:
    cost, state = heappop(heap)
    if state == solution: return cost
    for a,b in possible_moves(state, parc, stepout, target):
      p,r = (a,b) if a < b else (b,a)
      distance = abs(stepout[targetI[r]] - p) + (r-7)//4
      new_cost = cost + distance * energy[state[a]]
      moved = move(a,b,state)
      if seen.get(moved,999999) <= new_cost: continue
      seen[moved] = new_cost
      heappush(heap,(new_cost, moved))
  

  
start = pfc()
print(solve(read_puzzle("data/day-23a.txt")))
print(solve(read_puzzle("data/day-23b.txt")))
print(pfc()-start)