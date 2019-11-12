import sys
sys.stdin = open('input.txt', 'r')


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    number = 99999
    max_cnt = 0
    for row in range(N):
        for col in range(N):
            value = N_matrix[row][col]
            start_value = value
            now_row = row
            now_col = col
            direction = 0
            cnt = 1
            while direction < 4:
                var_row = now_row + dy[direction]
                var_col = now_col + dx[direction]
                if 0 <= var_row < N and 0 <= var_col < N and N_matrix[var_row][var_col] == (value + 1):
                    cnt += 1
                    direction = 0
                    value += 1
                    now_row = var_row
                    now_col = var_col
                else:
                    direction += 1
            if cnt > max_cnt:
                max_cnt = cnt
                number = start_value
            if cnt == max_cnt:
                if start_value < number:
                    number = start_value


    print('#{} {} {}'.format(test + 1, number, max_cnt))


# recursion 초과
# def dfs(in_row, in_col, cnt):
#     global tmp_cnt
#     if tmp_cnt < cnt:
#         tmp_cnt = cnt
#
#     for i in range(4):
#         new_row = in_row + dy[i]
#         new_col = in_col + dx[i]
#
#         if 0 <= new_row < N and 0 <= new_col < N and (N_matrix[in_row][in_col] + 1) == N_matrix[new_row][new_col]:
#             dfs(new_row, new_col, cnt + 1)
#
#
# testcase = int(input())
#
# for test in range(testcase):
#     N = int(input())
#     N_matrix = [list(map(int, input().split())) for i in range(N)]
#
#     number = 99999
#     max_cnt = 0
#     for row in range(N):
#         for col in range(N):
#             tmp_cnt = 0
#             dfs(row, col, 1)
#             if tmp_cnt > max_cnt:
#                 max_cnt = tmp_cnt
#                 number = N_matrix[row][col]
#             elif tmp_cnt == max_cnt:
#                 if N_matrix[row][col] < number:
#                     number = N_matrix[row][col]
#     print('#{} {} {}'.format(test+1, number, max_cnt))