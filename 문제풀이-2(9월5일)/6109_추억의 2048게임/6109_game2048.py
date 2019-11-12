import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')


def up_func():
    global N_matrix
    for col in range(N):
        end = 0
        row = 0
        while row < N-1:
            # 경계까지 모두 0인 경우 빠져나옴
            if end == 1:
                break
            # 처음이 0인경우
            if N_matrix[row][col] == 0:
                tmp = row + 1
                while tmp < N:
                    if N_matrix[tmp][col] != 0:
                        N_matrix[row][col], N_matrix[tmp][col] = N_matrix[tmp][col], N_matrix[row][col]
                        break
                    tmp += 1
                else:
                    end = 1
            # 현재 row는 0이 아니고 다음줄이 0인경우
            elif N_matrix[row + 1][col] == 0:
                tmp = row + 1
                while tmp < N:
                    if N_matrix[tmp][col] != 0:
                        N_matrix[row + 1][col], N_matrix[tmp][col] = N_matrix[tmp][col], N_matrix[row + 1][col]
                        break
                    tmp += 1
                else:
                    end = 1
            # 다음 수가 다를 경우
            elif N_matrix[row + 1][col] != N_matrix[row][col]:
                row += 1
            #같을 경우
            elif N_matrix[row + 1][col] == N_matrix[row][col]:
                N_matrix[row][col] += N_matrix[row + 1][col]
                N_matrix[row + 1][col] = 0
                row += 1


def down_func():
    global N_matrix
    for col in range(N):
        end = 0
        row = N - 1
        while row > 0:
            # 경계까지 모두 0인 경우 빠져나옴
            if end == 1:
                break
            # 처음이 0인경우
            if N_matrix[row][col] == 0:
                tmp = row - 1
                while tmp >= 0:
                    if N_matrix[tmp][col] != 0:
                        N_matrix[row][col], N_matrix[tmp][col] = N_matrix[tmp][col], N_matrix[row][col]
                        break
                    tmp -= 1
                else:
                    end = 1
            # 현재 row는 0이 아니고 다음줄이 0인경우
            elif N_matrix[row - 1][col] == 0:
                tmp = row - 1
                while tmp >= 0:
                    if N_matrix[tmp][col] != 0:
                        N_matrix[row - 1][col], N_matrix[tmp][col] = N_matrix[tmp][col], N_matrix[row - 1][col]
                        break
                    tmp -= 1
                else:
                    end = 1
            # 다음 수가 다를 경우
            elif N_matrix[row - 1][col] != N_matrix[row][col]:
                row -= 1
            #같을 경우
            elif N_matrix[row - 1][col] == N_matrix[row][col]:
                N_matrix[row][col] += N_matrix[row - 1][col]
                N_matrix[row - 1][col] = 0
                row -= 1


def left_func():
    global N_matrix
    for row in range(N):
        end = 0
        col = 0
        while col < N-1:
            # 경계까지 모두 0인 경우 빠져나옴
            if end == 1:
                break
            # 처음이 0인경우
            if N_matrix[row][col] == 0:
                tmp = col + 1
                while tmp < N:
                    if N_matrix[row][tmp] != 0:
                        N_matrix[row][col], N_matrix[row][tmp] = N_matrix[row][tmp], N_matrix[row][col]
                        break
                    tmp += 1
                else:
                    end = 1
            # 현재 row는 0이 아니고 다음줄이 0인경우
            elif N_matrix[row][col + 1] == 0:
                tmp = col + 1
                while tmp < N:
                    if N_matrix[row][tmp] != 0:
                        N_matrix[row][col + 1], N_matrix[row][tmp] = N_matrix[row][tmp], N_matrix[row][col + 1]
                        break
                    tmp += 1
                else:
                    end = 1
            # 다음 수가 다를 경우
            elif N_matrix[row][col + 1] != N_matrix[row][col]:
                col += 1
            #같을 경우
            elif N_matrix[row][col + 1] == N_matrix[row][col]:
                N_matrix[row][col] += N_matrix[row][col + 1]
                N_matrix[row][col + 1] = 0
                col += 1


def right_func():
    global N_matrix
    for row in range(N):
        end = 0
        col = N - 1
        while col > 0:
            # 경계까지 모두 0인 경우 빠져나옴
            if end == 1:
                break
            # 처음이 0인경우
            if N_matrix[row][col] == 0:
                tmp = col - 1
                while tmp >= 0:
                    if N_matrix[row][tmp] != 0:
                        N_matrix[row][col], N_matrix[row][tmp] = N_matrix[row][tmp], N_matrix[row][col]
                        break
                    tmp -= 1
                else:
                    end = 1
            # 현재 row는 0이 아니고 다음줄이 0인경우
            elif N_matrix[row][col - 1] == 0:
                tmp = col - 1
                while tmp >= 0:
                    if N_matrix[row][tmp] != 0:
                        N_matrix[row][col - 1], N_matrix[row][tmp] = N_matrix[row][tmp], N_matrix[row][col - 1]
                        break
                    tmp -= 1
                else:
                    end = 1
            # 다음 수가 다를 경우
            elif N_matrix[row][col - 1] != N_matrix[row][col]:
                col -= 1
            #같을 경우
            elif N_matrix[row][col - 1] == N_matrix[row][col]:
                N_matrix[row][col] += N_matrix[row][col - 1]
                N_matrix[row][col - 1] = 0
                col -= 1

test_case = int(input())

for test in range(test_case):
    N, direction = map(str, input().split())
    N = int(N)

    N_matrix = [list(map(int, input().split())) for i in range(N)]

    if direction == 'up':
        up_func()
    elif direction == 'down':
        down_func()
    elif direction == 'left':
        left_func()
    elif direction == 'right':
        right_func()

    print('#{}'.format(test+1))
    for row in N_matrix:
        print(' '.join(list(map(str, row))))

