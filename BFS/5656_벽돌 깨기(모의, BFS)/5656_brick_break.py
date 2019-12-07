import sys
from itertools import product
from copy import deepcopy
sys.stdin = open('input.txt', 'r')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# BFS
def breaking(drop_case):
    new_matrix = deepcopy(WH_matrix)
    cnt = 0
    for col in drop_case:
        # 4. finding block position
        row = find_top(new_matrix, col)
        if row == H:
            continue

        Q = []
        Q.append((row, col, new_matrix[row][col]))
        new_matrix[row][col] = 0
        cnt += 1
        while Q:
            row, col, power = Q.pop(0)
            for k in range(1, power):
                for i in range(4):
                    new_row = row + dy[i] * k
                    new_col = col + dx[i] * k
                    if 0 <= new_row < H and 0 <= new_col < W and new_matrix[new_row][new_col]:
                        if new_matrix[new_row][new_col] > 1:
                            Q.append((new_row, new_col, new_matrix[new_row][new_col]))
                        new_matrix[new_row][new_col] = 0
                        cnt += 1
        rearrange(new_matrix)


    return cnt

def find_top(new_matrix, col):
    for i in range(H):
        if new_matrix[i][col] > 0:
            break
    else: return H
    return i

def rearrange(new_matrix):
    for i in range(W):
        check_pos = H - 1
        for j in range(H - 1, -1, -1):
            if new_matrix[j][i]:
                new_matrix[check_pos][i], new_matrix[j][i] = new_matrix[j][i], new_matrix[check_pos][i]
                check_pos -= 1

testcase = int(input())

for test in range(testcase):
    N, W, H = map(int, input().split())
    WH_matrix = [list(map(int, input().split())) for i in range(H)]

    total_block = 0
    for row in WH_matrix:
        for i in row:
            if i:
                total_block += 1

    # 1. Indexing the width of WH_matrix
    W_arr = [i for i in range(W)]
    # 2. Every case dropping N balls including duplication
    drop_cases = product(W_arr, repeat=N)
    # 3. breaking blocks each case
    min_left = 9999999
    for drop_case in drop_cases:
        cnt = breaking(drop_case)
        if (total_block - cnt) < min_left:
            min_left = (total_block - cnt)
            # end condition
            if min_left == 0:
                break


    print('#{} {}'.format(test+1, min_left))
