import sys
sys.stdin = open('bomber4_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N, n_B = map(int, input().split())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    kill = 0
    for i in range(n_B):
        y, x, power = map(int, input().split())
        for row in range(y, y + power):
            for col in range(x, x + power):
                if 0 <= row < N and 0 <= col < N:
                    kill += N_matrix[row][col]
                    N_matrix[row][col] = 0

    print('#{} {}'.format(test + 1, kill))