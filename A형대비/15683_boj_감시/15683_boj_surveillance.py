import sys
sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1, 0]
dy = [-1, 0, 1, 0, -1]

def surveil_5(row, col):
    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        while 0 <= new_row < N and 0 <= new_col < M:
            if matrix[new_row][new_col] == 0:
                matrix[new_row][new_col] = '#'
            elif matrix[new_row][new_col] == 6:
                break
            new_row += dy[i]
            new_col += dx[i]

def surveil_4(row, col):
    # 방향 정하기
    direction = 0
    min_zero = 99999
    for i in range(4):
        zero_cnt = 0
        new_row = row + dy[i]
        new_col = col + dx[i]
        while 0 <= new_row < N and 0 <= new_col < M:
            if matrix[new_row][new_col] == 0:
                zero_cnt += 1
            elif matrix[new_row][new_col] == 6:
                break
            new_row += dy[i]
            new_col += dx[i]
        if zero_cnt < min_zero:
            min_zero = zero_cnt
            direction = i
    
    # 정한 방향으로 #채우기
    for i in range(4):
        if i == direction:
            continue
        new_row = row + dy[i]
        new_col = col + dx[i]
        while 0 <= new_row < N and 0 <= new_col < M:
            if matrix[new_row][new_col] == 0:
                matrix[new_row][new_col] = '#'
            elif matrix[new_row][new_col] == 6:
                break
            new_row += dy[i]
            new_col += dx[i]

def surveil_3(row, col):
    # 각 방향 0개수 구하기
    zero_cnt_list = []
    for i in range(4):
        zero_cnt = 0
        new_row = row + dy[i]
        new_col = col + dx[i]
        while 0 <= new_row < N and 0 <= new_col < M:
            if matrix[new_row][new_col] == 0:
                zero_cnt += 1
            elif matrix[new_row][new_col] == 6:
                break
            new_row += dy[i]
            new_col += dx[i]
        zero_cnt_list.append(zero_cnt)
    zero_cnt_list.append(zero_cnt_list[0])

    # 방향 정하기
    direction = 0
    max_zero = 0
    for i in range(len(zero_cnt_list) - 1):
        if zero_cnt_list[i] + zero_cnt_list[i + 1] > max_zero:
            max_zero = zero_cnt_list[i] + zero_cnt_list[i + 1]
            direction = i

    # 정한 방향으로 # 채우기
    for i in range(5):
        if i == direction or i == direction + 1:
            new_row = row + dy[i]
            new_col = col + dx[i]
            while 0 <= new_row < N and 0 <= new_col < M:
                if matrix[new_row][new_col] == 0:
                    matrix[new_row][new_col] = '#'
                elif matrix[new_row][new_col] == 6:
                    break
                new_row += dy[i]
                new_col += dx[i]


def surveil_2(row, col):
    # 가로 또는 세로의 0개수 구하기
    zero_cnt_ho = 0
    zero_cnt_ver = 0
    for i in matrix[row]:
        if i == 0:
            zero_cnt_ho += 1
    for i in range(N):
        if matrix[i][col] == 0:
            zero_cnt_ver += 1
    # 방향 정하기
    if zero_cnt_ho > zero_cnt_ver:
        direction = 1
    else:
        direction = 0

    # 정한 방향 #로 채우기
    for i in range(4):
        if i == direction or i == direction + 2:
            new_row = row + dy[i]
            new_col = col + dx[i]
            while 0 <= new_row < N and 0 <= new_col < M:
                if matrix[new_row][new_col] == 0:
                    matrix[new_row][new_col] = '#'
                elif matrix[new_row][new_col] == 6:
                    break
                new_row += dy[i]
                new_col += dx[i]


def surveil_1(row, col):
    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        while 0 <= new_row < N and 0 <= new_col < M:
            if matrix[new_row][new_col] == 0:
                matrix[new_row][new_col] = '#'
            elif matrix[new_row][new_col] == 6:
                break
            new_row += dy[i]
            new_col += dx[i]

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(N)]

# 5부터 채우기
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 5:
            surveil_5(row, col)

# 4 비교 후 채우기
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 4:
            surveil_4(row, col)

# 3 비교 후 채우기
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 3:
            surveil_3(row, col)

# 2 비교 후 채우기
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 2:
            surveil_2(row, col)

# 1 비교 후 채우기
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 1:
            surveil_1(row, col)

# 사각지대 개수
cnt_blind = 0
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 0:
            cnt_blind += 1

print(cnt_blind)
