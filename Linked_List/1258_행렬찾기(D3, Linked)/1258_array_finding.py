import sys
sys.stdin = open('input.txt', 'r')

def func_count(old_row, old_col):
    global N_matrix
    row = old_row
    col = old_col
    while N_matrix[row][col] != 0:
        N_matrix[row][col] = 0
        col += 1

        if N_matrix[row][col] == 0:
            row += 1
            x_length = col - old_col
            col = old_col

    y_length = row - old_row

    pair_list.append([y_length, x_length])



test_case = int(input())
for test in range(test_case):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    pair_list = []

    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] != 0:
                func_count(row, col)
    for j in range(len(pair_list)):
        for i in range(len(pair_list) - 1):
            if pair_list[i][0]*pair_list[i][1] > pair_list[i+1][0]*pair_list[i+1][1]:
                pair_list[i], pair_list[i+1] = pair_list[i+1], pair_list[i]
            elif pair_list[i][0]*pair_list[i][1] == pair_list[i+1][0]*pair_list[i+1][1]:
                if pair_list[i][0] > pair_list[i+1][0]:
                    pair_list[i], pair_list[i + 1] = pair_list[i + 1], pair_list[i]

    print('#{} {}'.format(test+1, len(pair_list)), end=' ')
    for pair in pair_list:
        for i in pair:
            print(i, end=' ')

    print()

# by 이길현
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:
#             x, y = 0, 0
#             while arr[i+x][j]:
#                 x += 1
#             while arr[i][j+y]:
#                 y += 1
#             ret.append((x, y))
#
#             for m in range(x):
#                 for n in range(y):
#                     arr[i+m][j+n] = 0
#
# ret = sorted(sorted(ret, key=lambda p: p[0]), key=lambda p: p[0] * p[1])