import sys, itertools, collections
sys.stdin = open('input.txt', 'r')

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def BFS(virus_arr, target_cnt_tmp):
    Q = collections.deque(virus_arr)
    a = [1, 2, 3]
    visit = [[False]*N for i in range(N)]
    for virus in virus_arr:
        visit[virus[0]][virus[1]] = True

    t_tmp = 0

    while Q:
        t_tmp += 1
        for i in range(len(Q)):
            now_virus = Q.popleft()
            for i in range(4):
                new_row = now_virus[0] + direction[i][0]
                new_col = now_virus[1] + direction[i][1]
                if 0 <= new_row < N and 0 <= new_col < N and not(visit[new_row][new_col]) and N_matrix[new_row][new_col] != 1:
                    Q.append([new_row, new_col])
                    visit[new_row][new_col] = True
                    if N_matrix[new_row][new_col] == 0:
                        target_cnt_tmp -= 1
                    if target_cnt_tmp == 0:
                        return t_tmp
    # Queue에 바이러스가 없음에도 아직 모두 감염시키지 못한 경우
    return -1

N, M = map(int, input().split())
N_matrix = [list(map(int, input().split())) for i in range(N)]

viruses = []
target_cnt = 0
for row in range(N):
    for col in range(N):
        # 비활성 바이러스 위치 좌표 저장
        if N_matrix[row][col] == 2:
            viruses.append([row, col])
        # 감염시켜야 할 타겟의 개수
        elif N_matrix[row][col] == 0:
            target_cnt += 1

min_time = 999999
# M개의 바이러스 선택하기 Combination)
for sel_virus in itertools.combinations(viruses, M):
    t = BFS(sel_virus, target_cnt)
    if t != -1 and min_time > t:
        min_time = t

if min_time == 999999:
    print(-1)
elif target_cnt == 0:
    print(0)
else:
    print(min_time)
