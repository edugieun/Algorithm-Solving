import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
N_matrix = [list(map(int, input().split())) for i in range(N)]

height_set = set()
for row in range(N):
    for col in range(N):
        if N_matrix[row][col] not in height_set:
            height_set.add(N_matrix[row][col])

max_cnt = 1
for height in height_set:
    visit_matrix = [[False] * N for i in range(N)]
    cnt_tmp = 0
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] > height and visit_matrix[row][col] == False:
                visit_matrix[row][col] = True
                Q = deque()
                Q.append((row, col))
                # BFS
                while Q:
                    y, x = Q.popleft()
                    for d in dyx:
                        y_tmp = y + d[0]
                        x_tmp = x + d[1]
                        if 0 <= y_tmp < N and 0 <= x_tmp < N and N_matrix[y_tmp][x_tmp] > height and visit_matrix[y_tmp][x_tmp] == False:
                            visit_matrix[y_tmp][x_tmp] = True
                            Q.append((y_tmp, x_tmp))
                cnt_tmp += 1

    if cnt_tmp > max_cnt:
        max_cnt = cnt_tmp

print(max_cnt)