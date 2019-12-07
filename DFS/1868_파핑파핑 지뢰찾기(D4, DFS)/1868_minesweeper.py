import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def numbering(row, col):
    global N_matrix
    cnt = 0
    for i in range(8):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if 0 <= new_row < N and 0 <= new_col < N and N_matrix[new_row][new_col] == '*':
            cnt += 1
    N_matrix[row][col] = cnt

# dfs
def zero_scan(row, col):
    global N_matrix
    N_matrix[row][col] = -1

    for i in range(8):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if 0 <= new_row < N and 0 <= new_col < N:
            if N_matrix[new_row][new_col] == 0:
                zero_scan(new_row, new_col)
            elif N_matrix[new_row][new_col] > 0:
                N_matrix[new_row][new_col] = -1

testcase = int(input())

for test in range(testcase):
    N = int(input())

    N_matrix = [list(input()) for i in range(N)]

    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == '.':
                numbering(row, col)

    click_cnt = 0
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == 0:
                click_cnt += 1
                zero_scan(row, col)


    for row in range(N):
        for col in range(N):
            if type(N_matrix[row][col]) == type(1) and N_matrix[row][col] > 0:
                click_cnt += 1

    print('#{} {}'.format(test+1, click_cnt))