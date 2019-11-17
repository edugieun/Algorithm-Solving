import sys
sys.stdin = open('input.txt', 'r')

def dfs(direc, mg_num):
    if not 0 <= mg_num < 4:
        return
    if direc == -1 and N_matrix[mg_num][2] == N_matrix[mg_num - direc][-2]:
        return
    elif direc == 1 and N_matrix[mg_num][-2] == N_matrix[mg_num - direc][2]:
        return

    dfs(direc, mg_num + direc)

    if abs(rot_mag - mg_num) == 1 or abs(rot_mag - mg_num) == 3:
        t_rot_dir = -rot_dir
    elif abs(rot_mag - mg_num) == 2:
        t_rot_dir = rot_dir

    if t_rot_dir == 1:
        change = N_matrix[mg_num].pop()
        N_matrix[mg_num].insert(0, change)
    elif t_rot_dir == -1:
        change = N_matrix[mg_num].pop(0)
        N_matrix[mg_num].append(change)


testcase = int(input())

for test in range(testcase):
    K = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(4)]

    for _ in range(K):
        rot_mag, rot_dir = map(int, input().split())
        rot_mag = rot_mag - 1

        # 왼쪽
        dfs(-1, rot_mag - 1)
        # 오른쪽
        dfs(1, rot_mag + 1)

        if rot_dir == 1:
            change = N_matrix[rot_mag].pop()
            N_matrix[rot_mag].insert(0, change)
        elif rot_dir == -1:
            change = N_matrix[rot_mag].pop(0)
            N_matrix[rot_mag].append(change)

    total_sum = 0
    for idx in range(4):
        if N_matrix[idx][0] == 1:
            total_sum += 2**idx
    print('#{} {}'.format(test+1, total_sum))
