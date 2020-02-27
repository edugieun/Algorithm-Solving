import sys
sys.stdin = open('input.txt', 'r')

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
NM_matrix = [list(map(int, input().split())) for i in range(N)]
NM_matrix[r][c] = 2
clean_cnt = 1

while 1:
    for i in range(1, 5):
        d_tmp = (d + 4 - i) % 4
        r_tmp, c_tmp  = r + D[d_tmp][0], c + D[d_tmp][1]
        if 0 <= r_tmp < N and 0 <= c_tmp < M and NM_matrix[r_tmp][c_tmp] == 0:
            r, c, d = r_tmp, c_tmp, d_tmp
            NM_matrix[r][c] = 2
            clean_cnt += 1
            break
    else:
        d_tmp = (d + 2) % 4
        r_tmp, c_tmp = r + D[d_tmp][0], c + D[d_tmp][1]
        if 0 <= r_tmp < N and 0 <= c_tmp < M and NM_matrix[r_tmp][c_tmp] != 1:
            r, c = r_tmp, c_tmp
        else:
            break
print(clean_cnt)