import sys
sys.stdin = open('input.txt', 'r')

dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]

def omok_check(row, col, dy, dx, color):
    global cnt, init_row, init_col
    while 0 <= row < N and 0 <= col < N and N_matrix[row][col] == color:
        row += dy * (-1)
        col += dx * (-1)

    init_row = row + dy
    init_col = col + dx

    cnt = 0
    new_row = row + dy
    new_col = col + dx



    while 0 <= new_row < N and 0 <= new_col < N and N_matrix[new_row][new_col] == color:
        cnt += 1
        new_row += dy
        new_col += dx





N = 19
N_matrix = [list(map(int, input().split())) for i in range(N)]
cnt = 0
init_row, init_col = 0, 0
try:
    for row in range(19):
        for col in range(19):
            if N_matrix[row][col] != 0:
                color = N_matrix[row][col]
                for i in range(4):
                    if 0 <= row + dy[i] < N and 0 <= col + dx[i] < N and N_matrix[row + dy[i]][col + dx[i]] == color:
                        omok_check(row, col, dy[i], dx[i], color)
                        if cnt == 5:
                            raise ValueError

except ValueError:
    print(color)
    print(init_row + 1, init_col + 1)

else:
    print(0)