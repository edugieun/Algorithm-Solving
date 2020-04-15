import sys
sys.stdin = open('input.txt', 'r')

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def check(core_num, direction):
    cnt_line = 0
    tmp_row, tmp_col = core_pos[core_num]
    while 1:
        tmp_row, tmp_col = tmp_row + D[direction][0], tmp_col + D[direction][1]
        if tmp_row < 0 or tmp_row >= N or tmp_col < 0 or tmp_col >= N:
            return cnt_line
        elif N_matrix[tmp_row][tmp_col] != 0:
            return False
        cnt_line += 1

def connect(core_num, direction, add_line):
    tmp_row, tmp_col = core_pos[core_num]
    for i in range(add_line):
        tmp_row, tmp_col = tmp_row + D[direction][0], tmp_col + D[direction][1]
        N_matrix[tmp_row][tmp_col] = -1

def disconnect(core_num, direction, add_line):
    tmp_row, tmp_col = core_pos[core_num]
    for i in range(1, add_line + 1):
        tmp_row, tmp_col = tmp_row + D[direction][0], tmp_col + D[direction][1]
        N_matrix[tmp_row][tmp_col] = 0

def DFS(core_num, n_core, l_line, total_core):
    global max_core, min_line
    if core_num == total_core:
        if n_core > max_core:
            max_core = n_core
            min_line = l_line
        elif n_core == max_core and l_line < min_line:
            min_line = l_line
        return

    for i in range(4):
        add_line = check(core_num, i)
        if add_line:
            connect(core_num, i, add_line)
            DFS(core_num + 1, n_core + 1, l_line + add_line, total_core)
            disconnect(core_num, i, add_line)

    DFS(core_num + 1, n_core, l_line, total_core)

testcase = int(input())
for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    max_core = 0
    side_core = 0
    min_line = 0
    core_pos = []

    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == 1:
                if 0 < row < N-1 and 0 < col < N-1:
                    core_pos.append((row, col))
                else:
                    side_core += 1

    DFS(0, 0, 0, len(core_pos))
    print('#{} {}'.format(test + 1, min_line))