import sys
sys.stdin = open('sample_input.txt', 'r')


def permut(N):
    if len(visited) == N + 1:
        permut_list.append(visited[:])

    for col in range(2, N + 1):
        if col not in visited:
            visited.insert(-1, col)
            permut(N)
            visited.pop(-2)

test_case = int(input())

for test in range(test_case):

    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    permut_list = []
    visited = [1, 1]
    permut(N)

    min_battery = 999999
    for order in permut_list:
        battery = 0
        for i in range(len(order) - 1):
            battery += N_matrix[order[i] - 1][order[i + 1] - 1]

        if battery < min_battery:
            min_battery = battery

    print('#{} {}'.format(test+1, min_battery))