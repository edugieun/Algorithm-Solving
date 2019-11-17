import sys
sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

testcase = int(input())

for test in range(testcase):
    N, M, K = map(int, input().split())
    NM_matrix = [list(map(int, input().split())) for i in range(N)]
    cell = {}
    for row in range(N):
        for col in range(M):
            if NM_matrix[row][col]:
                cell[(row, col)] = [NM_matrix[row][col], NM_matrix[row][col]]
    time = 0
    while time < K:
        time += 1
        new_cell = {}
        for pos, stat in cell.items():
            if cell[pos][0] == 0 and cell[pos][1] != 0:
                for i in range(4):
                    n_row = pos[0] + dy[i]
                    n_col = pos[1] + dx[i]
                    if (n_row, n_col) not in cell and (n_row, n_col) not in new_cell:
                        new_cell[(n_row, n_col)] = [stat[1], stat[1]]
                    elif (n_row, n_col) not in cell and (n_row, n_col) in new_cell:
                        if new_cell[(n_row, n_col)][1] < stat[1]:
                            new_cell[(n_row, n_col)] = [stat[1], stat[1]]
                cell[pos][1] -= 1
            else:
                cell[pos][0] -= 1

        for n_pos, n_stat in new_cell.items():
            cell[n_pos] = n_stat

    cnt = 0
    for stat in cell.values():
        if stat[1] > 0:
            cnt += 1

    print('#{} {}'.format(test + 1, cnt))