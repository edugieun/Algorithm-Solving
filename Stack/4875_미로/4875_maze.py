import sys
sys.stdin = open('sample_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def maze_searching(start_y, start_x):
    global N_matrix, N, find

    if find == 1:
        return None

    for i in range(4):
        t_start_x = start_x + dx[i]
        t_start_y = start_y + dy[i]

        if t_start_x >= 0 and t_start_y >= 0 and t_start_x < N and t_start_y < N:
            if N_matrix[t_start_y][t_start_x] == 3:
                find = 1
                return None
            elif N_matrix[t_start_y][t_start_x] == 0:
                N_matrix[t_start_y][t_start_x] = -1
                maze_searching(t_start_y, t_start_x)


test_case = int(input())

for test in range(test_case):
    N = int(input())

    N_matrix = [list(map(int, list(input()))) for i in range(N)]

    for n_row in range(N):
        for n_col in range(N):
            if N_matrix[n_row][n_col] == 2:
                find = 0
                maze_searching(n_row, n_col)

    if find:
        print('#{} 1'.format(test+1))
    else:
        print('#{} 0'.format(test + 1))
