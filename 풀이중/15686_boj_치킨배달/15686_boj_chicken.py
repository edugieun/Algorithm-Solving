import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

N_matrix = [list(map(int, input().split())) for i in range(N)]

every_chicken = []
every_home = []
for row in range(N):
    for col in range(N):
        if N_matrix[row][col] == 2:
            every_chicken.append([row, col])
        elif N_matrix[row][col] == 1:
            every_home.append([row, col])

for select_chicken in combinations(every_chicken, M):
    print(select_chicken)