import sys
sys.stdin = open('sample_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def maze_recursion(row, col):
    global N_matrix, cnt, find
    N_matrix[row][col] = -1

    for i in range(4):
        if find == 1:
            return None
        check_row = row + dy[i]
        check_col = col + dx[i]

        if check_row >= 0 and check_col >= 0 and check_row < N and check_col < N:
            if N_matrix[check_row][check_col] == 3:
                find = 1
                return None
            if N_matrix[check_row][check_col] == 0:
                cnt += 1
                maze_recursion(check_row, check_col)

    if find == 0:
        cnt -= 1

test_case = int(input())
for test in range(test_case):
    N = int(input())
    N_matrix = [list(map(int, list(input()))) for i in range(N)]

    cnt = 0
    find = 0
    for row in range(N):
        if 2 in N_matrix[row]:
            maze_recursion(row, N_matrix[row].index(2))

    if find == 0:
        cnt = 0

    print('#{} {}'.format(test+1, cnt))





