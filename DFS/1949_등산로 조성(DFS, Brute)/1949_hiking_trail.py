import sys
sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# dfs & brute
def dfs(row, col, matrix, chance, cnt):
    global K, max_length
    cnt += 1
    if cnt > max_length:
        max_length = cnt
    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if 0 <= new_row < N and 0 <= new_col < N:
            if matrix[new_row][new_col] < matrix[row][col]:
                tmp = matrix[row][col]
                matrix[row][col] = 100
                dfs(new_row, new_col, matrix, chance, cnt)
                matrix[row][col] = tmp
            elif chance == True and matrix[new_row][new_col] >= matrix[row][col] and matrix[new_row][new_col] - K < matrix[row][col]:
                tmp = matrix[new_row][new_col]
                matrix[new_row][new_col] = matrix[row][col] - 1
                chance = False
                tmp2 = matrix[row][col]
                matrix[row][col] = 100
                dfs(new_row, new_col, matrix, chance, cnt)
                chance = True
                matrix[row][col] = tmp2
                matrix[new_row][new_col] = tmp


testcase = int(input())

for test in range(testcase):
    N, K = map(int, input().split())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    max_height = 0
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] > max_height:
                max_height = N_matrix[row][col]

    max_length = 0
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == max_height:
                chance = True
                dfs(row, col, N_matrix, chance, 0)

    print('#{} {}'.format(test+1, max_length))