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

total_dis = 9999999
for chi_list in combinations(every_chicken, M):
    total_tmp = 0
    for home in every_home:
        min_tmp = 999999
        for chi in chi_list:
            dis = abs(home[0]-chi[0]) + abs(home[1]-chi[1])
            if dis < min_tmp:
                min_tmp = dis
        total_tmp += min_tmp
    if total_tmp < total_dis:
        total_dis = total_tmp

print(total_dis)