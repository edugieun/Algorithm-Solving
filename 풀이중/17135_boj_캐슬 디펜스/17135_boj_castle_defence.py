import sys
sys.stdin = open('input.txt', 'r')


def combination(com_arr, start):
    global max_kill

    if len(com_arr) == R:
        deep_copy_enermies = []
        for i in enermies:
            deep_copy_enermies.append(i[:])

        kill = play(com_arr, deep_copy_enermies, 0)
        if max_kill < kill:
            max_kill = kill
    else:
        for i in range(start, M):
            combination(com_arr + [M_arr[i]], i + 1)


def play(arrows, now_enermies, cnt):
    deep_copy_now_enermies = []

    for i in now_enermies:
        deep_copy_now_enermies.append(i[:])

    if not deep_copy_now_enermies:
        return cnt

    targets = set()
    for arrow in arrows:
        target = None
        for idx, enermy in enumerate(deep_copy_now_enermies):
            dis_e = abs(N - enermy[0]) + abs(arrow - enermy[1])
            if dis_e <= D:
                if target == None:
                    target = idx
                    target_dis = dis_e
                else:
                    if dis_e < target_dis:
                        target = idx
                        target_dis = dis_e
                    elif dis_e == target_dis and enermy[1] < deep_copy_now_enermies[target][1]:
                        target = idx
                        target_dis = dis_e
        if target != None:
            targets.add(target)

    # 죽은 적 제거
    for i in sorted(targets, reverse=True):
        deep_copy_now_enermies.remove(deep_copy_now_enermies[i])
        cnt += 1
    # 적 이동과 탈출한 적 제거
    numof_enermies = len(deep_copy_now_enermies)
    for i in range(numof_enermies - 1, -1, -1):
        if deep_copy_now_enermies[i][0] == (N - 1):
            deep_copy_now_enermies.remove(deep_copy_now_enermies[i])
        else:
            deep_copy_now_enermies[i][0] += 1

    return play(arrows, deep_copy_now_enermies, cnt)


N, M, D = map(int, input().split())
R = 3
N_matrix = [list(map(int, input().split())) for i in range(N)]
M_arr = [i for i in range(M)]
enermies = []
for row in range(N):
    for col in range(M):
        if N_matrix[row][col] == 1:
            enermies.append([row, col])

max_kill = 0
combination([], 0)

print(max_kill)