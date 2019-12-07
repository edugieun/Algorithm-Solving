import sys
sys.stdin = open('bomber3_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N, M = list(map(int, input().split()))

    N_matrix = [list(map(int, input().split())) for i in range(N)]

    max_bomb = 0
    for row in range(N-M + 1):
        for col in range(N-M + 1):
            bomb_damage = 0
            for bomb_row in range(M):
                for bomb_col in range(M):
                    bomb_damage += N_matrix[row + bomb_row][col + bomb_col]

            if max_bomb < bomb_damage:
                max_bomb = bomb_damage
                max_row, max_col = row, col

    print('#{} {} {} {}'.format(test+1, max_row, max_col, max_bomb))