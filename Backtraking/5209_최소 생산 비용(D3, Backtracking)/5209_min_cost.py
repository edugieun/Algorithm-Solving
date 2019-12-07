import sys
sys.stdin = open('input.txt', 'r')


def backtrack():
    global min_cost, cost_tmp, row
    if cost_tmp >= min_cost:
        return

    if len(visited) == N and cost_tmp < min_cost:
        min_cost = cost_tmp
        return

    for col in range(N):
        if col not in visited:
            visited.append(col)
            cost_tmp += N_matrix[row][col]
            row += 1
            backtrack()
            row -= 1
            cost_tmp -= N_matrix[row][col]
            visited.pop()

test_case = int(input())

for test in range(test_case):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    min_cost = 0
    cost_tmp = 0
    for i in range(N):
        min_cost += N_matrix[i][i]

    visited = []
    row = 0
    backtrack()

    print('#{} {}'.format(test+1, min_cost))