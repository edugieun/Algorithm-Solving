import sys
sys.stdin = open('input.txt', 'r')

# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# testcase = int(input())
#
# for test in range(testcase):
#     N, M, K = map(int, input().split())
#     NM_matrix = [list(map(int, input().split())) for i in range(N)]
#     cell = {}
#     for row in range(N):
#         for col in range(M):
#             if NM_matrix[row][col]:
#                 cell[(row, col)] = [NM_matrix[row][col], NM_matrix[row][col]]
#     time = 0
#     while time < K:
#         time += 1
#         new_cell = {}
#         for pos, stat in cell.items():
#             if cell[pos][0] == 0 and cell[pos][1] != 0:
#                 for i in range(4):
#                     n_row = pos[0] + dy[i]
#                     n_col = pos[1] + dx[i]
#                     if (n_row, n_col) not in cell and (n_row, n_col) not in new_cell:
#                         new_cell[(n_row, n_col)] = [stat[1], stat[1]]
#                     elif (n_row, n_col) not in cell and (n_row, n_col) in new_cell:
#                         if new_cell[(n_row, n_col)][1] < stat[1]:
#                             new_cell[(n_row, n_col)] = [stat[1], stat[1]]
#                 cell[pos][1] -= 1
#             else:
#                 cell[pos][0] -= 1
#
#         for n_pos, n_stat in new_cell.items():
#             cell[n_pos] = n_stat
#
#     cnt = 0
#     for stat in cell.values():
#         if stat[1] > 0:
#             cnt += 1
#
#     print('#{} {}'.format(test + 1, cnt))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

testcase = int(input())

for test in range(testcase):
    N, M, K = map(int, input().split())
    NM_matrix = [list(map(int, input().split())) for i in range(N)]
    # 1. 미리 최종적으로 완성될 크기의 matrix를 만들어 준다.
    final_matrix = [[0] * (M + K) for i in range(N + K)]
    # 2. 생명력 1~10에 해당하는 각각의 세포의 좌표를 저장할 리스트를 생성한다.
    cell_list = [[] for i in range(10 + 1)]

    for i in range(N):
        for j in range(M):
            # 3. 초기 세포의 위치를 찾는다.
            if NM_matrix[i][j] > 0:
                cell_life = NM_matrix[i][j]
                # 3-1. 찾은 세포를 final matrix의 정 가운데에 위치시킨다.
                final_matrix[i + K // 2][j + K // 2] = cell_life
                # 3-2. 세포의 위치를 해당 생명력에 추가한다.
                cell_list[cell_life].append((i + K // 2, j + K // 2))

    # 4. K시간 동안 for loop
    for time in range(K):
        # 4-1. K시간의 약수에서만 세포 증식 및 재배치가 일어나게 한다.
        # 예를 들면, K가 6일 경우 세포 증식이 가능한 세포들은 생명력이 6, 3, 2, 1인 세포들이다.
        # 이를 다시 말하면, 생명력이 2인 세포는 K가 2, 4, 6, 8.. 에 증식이 가능하고, 3인 세포는 3, 6, 9...에 증식이 가능하다.
        for v in range(10, 0, -1):
            if (time + 1) % (v + 1) != 0:
                continue
            survive_cells = []
            for c in cell_list[v]:
                # 세포의 생명력이 남은 시간보다 긴 경우, 최종적으로 그 세포는 생존해 있으므로 추가한다.
                # 반대로, 해당 세포가 최종 시간이 지나면 죽을 운명이라면 추가하지 않는다.
                if K - time < v:
                    survive_cells.append(c)
                for i in range(4):
                    if final_matrix[c[0] + dy[i]][c[1] + dx[i]] == 0:
                        final_matrix[c[0] + dy[i]][c[1] + dx[i]] = v
                        survive_cells.append((c[0] + dy[i], c[1] + dx[i]))
            # 세포 리스트를 살아있는 세포들로만 갱신한다.
            cell_list[v] = survive_cells

    print("#{} {}".format(test + 1, sum(len(c) for c in cell_list)))