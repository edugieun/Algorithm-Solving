import sys
sys.stdin = open('input.txt', 'r')

def catch_fly(row, col):
    global catch_num, N_matrix
    tmp = 0
    for i in range(row, row + M):
        for j in range(col, col + M):
          tmp += N_matrix[i][j]

    if tmp > catch_num:
        catch_num = tmp

test_case = int(input())

for test in range(test_case):

    N, M = map(int, input().split())

    N_matrix = [list(map(int, input().split())) for i in range(N)]
    catch_num = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            catch_fly(row, col)

    print('#{} {}'.format(test+1, catch_num))