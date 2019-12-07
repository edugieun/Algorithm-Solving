import sys

sys.stdin = open('input.txt', 'r')

# 방법 1. 매트릭스 없이 세포들의 좌표값을 저장 / 매 시간 이미 죽은 세포를 포함한 모든 세포들의 좌표를 비교
# 죽은 세포의 정보를 따로 저장할 곳이 없으므로, 하나의 리스트에 모든 정보를 담아야 하므로, 세포 리스트는 끝없이 길어진다.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

testcase = int(input())

for test in range(testcase):
    N, M, K = map(int, input().split())
    NM_matrix = [list(map(int, input().split())) for i in range(N)]
    cell = {}
    # 1. 초기 매트릭스에서 초기 세포들의 좌표값과 생명력을 같이 저장한다.
    for row in range(N):
        for col in range(M):
            if NM_matrix[row][col]:
                # 1-1. 생명력을 리스트에 2번 저장하는 이유는 세포 활성까지 남은 시간과 생명력을 저장하기 위함이다.
                cell[(row, col)] = [NM_matrix[row][col], NM_matrix[row][col]]
    time = 0
    # 2. 시간을 1씩 증가 시킨다.
    while time < K:
        time += 1
        new_cell = {}
        # 3. 각각 세포의 좌표와 생명력을 읽는다.
        for pos, stat in cell.items():
            # 3-1. 세포의 활성까지 남은 시간이 0이 되면(세포가 활성되면) 증식을 하고, 생명력을 1씩 감소
            if cell[pos][0] == 0 and cell[pos][1] != 0:
                for i in range(4):
                    n_row = pos[0] + dy[i]
                    n_col = pos[1] + dx[i]
                    # 3-1-1. 증식한 곳의 좌표가 기존에 있던 좌표도 아니고, 이번 시간 동안 새로 증식된 좌표도 아니라면 new_cell에 추가한다.
                    # (시간소모원인) in 또는 not in 구문도 결국은 for 루프와 같다. 매 세포마다 세포 리스트를 for loop를 돌리니 시간이 소모된다.
                    if (n_row, n_col) not in cell and (n_row, n_col) not in new_cell:
                        new_cell[(n_row, n_col)] = [stat[1], stat[1]]
                    # 3-1-2. 기존에 있던 세포는 아니지만, 이번 시간동안 증식된 세포 중 같은 좌표를 가진다면,
                    elif (n_row, n_col) not in cell and (n_row, n_col) in new_cell:
                        # 더 큰 생명력을 가진 세포의 좌표로 바꾼다.
                        if new_cell[(n_row, n_col)][1] < stat[1]:
                            new_cell[(n_row, n_col)] = [stat[1], stat[1]]
                cell[pos][1] -= 1
            # 3-2. 세포가 아직 활성되지 않았다면, 활성까지 남은 시간을 1 감소한다.
            else:
                cell[pos][0] -= 1

        # 4. 세포 리스트를 갱신한다.
        # (시간소모원인) 살아있는 세포 정보 뿐만 아니라 죽어있는 세포 정보 또한 포함해야 하기 때문에 리스트는 점점 길어지게 되고, 시간 소모가 커진다.
        for n_pos, n_stat in new_cell.items():
            cell[n_pos] = n_stat

    # 5. 살아있는 세포들을 카운트한다.
    cnt = 0
    for stat in cell.values():
        if stat[1] > 0:
            cnt += 1

    print('#{} {}'.format(test + 1, cnt))

####################################################

# 방법 2. 최종 matrix를 미리 제작 / 매 시간 세포들을 확인하지 않고, 해당 시간에 번식 가능한 세포들만 확인
# 죽은 세포들이 배치될 matrix가 있으므로 비교문을 돌릴 세포 리스트에는 살아있는 세포 정보만 담으면 되므로, 리스트의 길이가 짧아진다.
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

    # 4. K시간 동안 for loop를 돌린다.
    for time in range(1, K + 1):
        # 4-1. 큰 생명력을 가진 세포부터 확인하며 큰 생명력을 가진 세포가 먼저 배치되도록 한다.
        for v in range(10, 0, -1):
            # 4-2. 문제에 따르면 생명력이 v인 세포는 time이 (v+1)의 배수일 때 번식한다.
            if time % (v + 1) != 0:
                continue
            survive_cells = []
            for c in cell_list[v]:
                # 4-3. 세포의 남은 생명력이 남은 시간(K-time)보다 긴 경우, 최종적으로 그 세포는 생존해 있으므로 추가한다.
                # 세포의 남은 생명력이 v가 아닌 (v-1)인 이유는 번식과 동시에 세포의 생명력이 -1 되기 때문이다.
                if (K - time) < (v - 1):
                    survive_cells.append(c)
                for i in range(4):
                    # 이미 세포 배치된 곳은 뛰어넘는다.
                    if final_matrix[c[0] + dy[i]][c[1] + dx[i]] == 0:
                        final_matrix[c[0] + dy[i]][c[1] + dx[i]] = v
                        survive_cells.append((c[0] + dy[i], c[1] + dx[i]))
            # 세포 리스트를 살아있는 세포들로만 갱신한다.
            cell_list[v] = survive_cells

    print("#{} {}".format(test + 1, sum(len(c) for c in cell_list)))
