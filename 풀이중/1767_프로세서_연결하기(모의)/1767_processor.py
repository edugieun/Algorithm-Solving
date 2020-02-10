import sys
sys.stdin = open('input.txt', 'r')

direciton = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def DFS(core_idx, cnt_core, len_line):
    global max_core, min_line

    if (core_idx) == len(cores):
        if cnt_core > max_core:
            max_core = cnt_core
            min_line = len_line
        elif cnt_core == max_core and len_line < min_line:
            min_line = len_line
        return

    for d_row, d_col in direciton:
        pos_tmp = []
        is_connect = False
        new_row = cores[core_idx][0]
        new_col = cores[core_idx][1]
        while 1:
            if new_row == 0 or new_row == N - 1 or new_col == 0 or new_col == N-1:
                is_connect = True
                break

            new_row = new_row + d_row
            new_col = new_col + d_col

            if N_matrix[new_row][new_col] == 0:
                pos_tmp.append([new_row, new_col])
            else: break
        
        if is_connect:
            for pos in pos_tmp:
                N_matrix[pos[0]][pos[1]] = 2

            DFS(core_idx + 1, cnt_core + 1, len_line + len(pos_tmp))

            for pos in pos_tmp:
                N_matrix[pos[0]][pos[1]] = 0

    DFS(core_idx + 1, cnt_core, len_line)



testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    max_core = 0
    min_line = 999999
    edge_core = 0
    cores = []
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == 1:
                if 0 < row < N - 1 and 0 < col < N-1:
                    cores.append((row, col))

    DFS(0, 0, 0)
    print('#{} {}'.format(test + 1,min_line))