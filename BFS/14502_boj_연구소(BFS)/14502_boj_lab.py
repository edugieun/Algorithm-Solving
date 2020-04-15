import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt', 'r')

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
NM_matrix = [list(map(int, input().split())) for i in range(N)]
empty_list = []

vir_list = []
for row in range(N):
    for col in range(M):
        if NM_matrix[row][col] == 0:
            empty_list.append((row, col))
        elif NM_matrix[row][col] == 2:
            vir_list.append((row, col))
least_vir = 999999
for wall_list in combinations(empty_list, 3):

    for r, c in wall_list:
        NM_matrix[r][c] = 1

    cnt = 0
    visit = [[False] * M for i in range(N)]
    Q = deque()
    for vir in vir_list:
        Q.append(vir)

    while Q and cnt < least_vir:
        v_r, v_c = Q.popleft()
        for dr, dc in D:
            tmp_r, tmp_c = v_r + dr, v_c + dc
            if 0 <= tmp_r < N and 0 <= tmp_c < M and (NM_matrix[tmp_r][tmp_c] == 0) and not visit[tmp_r][tmp_c]:
                visit[tmp_r][tmp_c] = True
                cnt += 1
                Q.append((tmp_r, tmp_c))
        if cnt > least_vir:
            break

    for r, c in wall_list:
        NM_matrix[r][c] = 0

    if cnt < least_vir:
        least_vir = cnt
print(len(empty_list) - least_vir - 3)