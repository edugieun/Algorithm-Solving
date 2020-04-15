import sys
sys.stdin = open('input.txt', 'r')

def out_matrix(r, c, d):
    global cnt
    cnt += 1
    if r == -1:
        return 2
    elif c == N:
        return 3
    elif r == N:
        return 0
    elif c == -1:
        return 1

def wormhole(in_pos, worm_num):
    for out_pos in worm_list[worm_num]:
        if in_pos != out_pos:
            return out_pos

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
Block_list = [(), (2, 3, 1, 0), (1, 3, 0, 2), (3, 2, 0, 1), (2, 0, 3, 1), (2, 3, 0, 1)]

testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    worm_list = [[] for i in range(11)]
    for r in range(N):
        for c in range(N):
            if N_matrix[r][c] != 0:
                if N_matrix[r][c] >= 6:
                    worm_list[N_matrix[r][c]].append((r, c))

    max_cnt = 0
    for r in range(N):
        for c in range(N):
            if N_matrix[r][c] == 0:
                for direct in range(4):
                    tmp_r, tmp_c = r, c
                    tmp_direct = direct
                    cnt = 0
                    while 1:
                        tmp_r, tmp_c = tmp_r + D[tmp_direct][0], tmp_c + D[tmp_direct][1]
                        if 0 <= tmp_r < N and 0 <= tmp_c < N:
                            if (tmp_r == r and tmp_c == c) or (N_matrix[tmp_r][tmp_c] == -1):
                                if cnt > max_cnt:
                                    max_cnt = cnt
                                break
                            elif N_matrix[tmp_r][tmp_c] > 5:
                                tmp_r, tmp_c = wormhole((tmp_r, tmp_c), N_matrix[tmp_r][tmp_c])
                            elif N_matrix[tmp_r][tmp_c] > 0:
                                cnt += 1
                                tmp_direct = Block_list[N_matrix[tmp_r][tmp_c]][tmp_direct]
                        else:
                            tmp_direct = out_matrix(tmp_r, tmp_c, tmp_direct)
    print('#{} {}'.format(test+1, max_cnt))