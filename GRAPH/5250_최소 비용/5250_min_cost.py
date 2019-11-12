import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def find_cost():
    Q = deque()
    Q.append((0, 0))
    check_matrix[0][0] = 0
    while Q:
        row, col = Q.popleft()
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row, new_col = row + direction[0], col + direction[1]
            if 0 <= new_row < N and 0 <= new_col < N:
                if N_matrix[new_row][new_col] > N_matrix[row][col]:
                    w = N_matrix[new_row][new_col] - N_matrix[row][col] + 1
                else:
                    w = 1

                if check_matrix[new_row][new_col] > check_matrix[row][col] + w:
                    check_matrix[new_row][new_col] = check_matrix[row][col] + w
                    Q.append((new_row, new_col))
    return check_matrix[N - 1][N - 1]


testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    check_matrix = [[0xffffffff] * N for i in range(N)]
    result = find_cost()
    print('#{} {}'.format(test+1, result))
