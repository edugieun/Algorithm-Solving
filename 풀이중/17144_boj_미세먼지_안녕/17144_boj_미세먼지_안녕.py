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
t_tmp = 0
while 1:
    if t_tmp == T:
        break
    else:
        dust_list = []
        for row in range(R):
            for col in range(C):
                if A_matrix[row][col] >= 5:
                    dust_list.append([row, col, A_matrix[row][col]])

        new_dust = []
        for r, c, m in dust_list:
            div_m = m//5
            for dy, dx in D:
                row_tmp = r + dy
                col_tmp = c + dx
                if 0 <= row_tmp < R and 0 <= col_tmp < C and A_matrix[row_tmp][col_tmp] != -1:
                    A_matrix[r][c] -= div_m
                    new_dust.append([row_tmp, col_tmp, div_m])

        for r, c, m in new_dust:
            A_matrix[r][c] += m

        r, c = ac[0], 0
        for i in range(4):
            if i == 0:
                while r - 1 >= 0:
                    if A_matrix[r][c] == -1:
                        A_matrix[r-1][c] = 0
                    else:
                        A_matrix[r][c], A_matrix[r-1][c] = A_matrix[r-1][c], 0
                    r -= 1
            elif i == 1:
                while c + 1 < C:
                    A_matrix[r][c], A_matrix[r][c+1] = A_matrix[r][c+1], 0
                    c += 1
            elif i == 2:
                while r + 1 <= ac[0]:
                    A_matrix[r][c], A_matrix[r+1][c] = A_matrix[r+1][c], 0
                    r += 1
            elif i == 3:
                while c - 1 > 0:
                    A_matrix[r][c], A_matrix[r][c-1] = A_matrix[r][c-1], 0
                    c -= 1

        r, c = ac[1], 0
        for i in range(4):
            if i == 0:
                while r + 1 < R:
                    if A_matrix[r][c] == -1:
                        A_matrix[r+1][c] = 0
                    else:
                        A_matrix[r][c], A_matrix[r+1][c] = A_matrix[r+1][c], 0
                    r += 1
            elif i == 1:
                while c + 1 < C:
                    A_matrix[r][c], A_matrix[r][c+1] = A_matrix[r][c+1], 0
                    c += 1
            elif i == 2:
                while r - 1 >= ac[1]:
                    A_matrix[r][c], A_matrix[r-1][c] = A_matrix[r-1][c], 0
                    r -= 1
            elif i == 3:
                while c - 1 > 0:
                    A_matrix[r][c], A_matrix[r][c-1] = A_matrix[r][c-1], 0
                    c -= 1

        t_tmp += 1

ans = 0
for row in range(R):
    for col in range(C):
        if A_matrix[row][col] > 0:
            ans += A_matrix[row][col]

print(ans)