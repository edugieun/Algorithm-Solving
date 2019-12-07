import sys
sys.stdin = open('sample_input.txt', 'r')

dx = [1, 0]
dy = [0, 1]

def min_route(row, col):
    global tmp_sum, min_sum

    if row == N-1 and col == N-1 and tmp_sum < min_sum:
        min_sum = tmp_sum


    for i in range(2):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < N and 0 <= new_col < N and min_sum > (tmp_sum + N_matrix[new_row][new_col]):
            tmp_sum += N_matrix[new_row][new_col]
            min_route(new_row, new_col)
            tmp_sum -= N_matrix[new_row][new_col]


test_case = int(input())

for test in range(test_case):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    # Initialization
    min_sum = 0
    for i in range(N):
        min_sum += N_matrix[0][i]
    for i in range(1, N):
        min_sum += N_matrix[i][N - 1]
    tmp_sum = N_matrix[0][0]

    min_route(0, 0)

    print('#{} {}'.format(test + 1, min_sum))