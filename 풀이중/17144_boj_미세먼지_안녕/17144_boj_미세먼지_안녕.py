import sys
sys.stdin = open('input.txt', 'r')

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

R, C, T = map(int, input().split())
A_matrix = [list(map(int, input().split())) for i in range(R)]

ac = []
for row in range(R):
    for col in range(C):
        if A_matrix[row][col] == -1:
            ac.append(row)

for t in range(T):
    dust_list = []
    for row in range(R):
        for col in range(C):
            if A_matrix[row][col] >= 5:
                dust_list.append([row, col, A_matrix[row][col]])

    for r, c, m in dust_list:
        div_m = m//5
        for dy, dx in D:
            row_tmp = r + dy
            col_tmp = c + dx
            if 0 <= row_tmp < R and 0 <= col_tmp < C and A_matrix[row_tmp][col_tmp] != -1:
                A_matrix[r][c] -= div_m
                A_matrix[row_tmp][col_tmp] += div_m

    for i in range(ac[0] - 1, 0, -1):
        A_matrix[i][0] = A_matrix[i-1][0]
    for i in range(C-1):
        A_matrix[0][i] = A_matrix[0][i+1]
    for i in range(ac[0]):
        A_matrix[i][C-1] = A_matrix[i+1][C-1]
    for i in range(C-1, 1, -1):
        A_matrix[ac[0]][i] = A_matrix[ac[0]][i-1]
    A_matrix[ac[0]][1] = 0

    for i in range(ac[1] + 1, R-1):
        A_matrix[i][0] = A_matrix[i+1][0]
    for i in range(C-1):
        A_matrix[R-1][i] = A_matrix[R-1][i+1]
    for i in range(R-1, ac[1], -1):
        A_matrix[i][C-1] = A_matrix[i-1][C-1]
    for i in range(C-1, 1, -1):
        A_matrix[ac[1]][i] = A_matrix[ac[1]][i-1]
    A_matrix[ac[1]][1] = 0


ans = 0
for row in range(R):
    for col in range(C):
        if A_matrix[row][col] > 0:
            ans += A_matrix[row][col]

print(ans)